from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import validate_author_exists
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.author import author_crud
from app.schemas.author import (AuthorCreate,
                                AuthorDB,
                                AuthorUpdate)

router = APIRouter()


@router.post(
    '/',
    response_model=AuthorDB,
    dependencies=[Depends(current_superuser)],
)
async def create_author(
    author: AuthorCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.

    Создает автора.
    """
    new_author = await author_crud.create(author, session)
    return new_author


@router.get('/',
            response_model=list[AuthorDB],
            )
async def get_all_authors(
        session: AsyncSession = Depends(get_async_session),
):
    """Возвращает список всех авторов."""
    all_authors = await author_crud.get_multi(session)
    return all_authors


@router.get(
    '/{id}',
    response_model=AuthorDB,
)
async def get_author(
    author_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Показывает информацию об авторе.
    """
    author = await author_crud.get(
        author_id, session
    )
    return author


@router.delete(
    '/{id}',
    response_model=AuthorDB,
    dependencies=[Depends(current_superuser)],
)
async def delete_author(
    author_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.

    Удаляет Автора.
    """
    author = await author_crud.remove(
        author_id, session
    )
    return author


@router.patch(
    '/{id}',
    response_model=AuthorDB,
    dependencies=[Depends(current_superuser)],
)
async def update_author(
        author_id: int,
        obj_in: AuthorUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.
    Обновление автора.
    """
    author = await validate_author_exists(author_id, session)
    updated_author = await author_crud.update(
        author, obj_in, session
    )
    return updated_author
