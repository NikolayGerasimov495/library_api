from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import validate_book_exists
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.book import book_crud
from app.schemas.book import (BookCreate,
                              BookDB,
                              BookUpdate)

router = APIRouter()


@router.post(
    '/',
    response_model=BookDB,
    dependencies=[Depends(current_superuser)],
)
async def create_book(
    book: BookCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.
    Создает книгу.
    """
    new_book= await book_crud.create(book, session)
    return new_book


@router.get('/',
            response_model=list[BookDB],
            )
async def get_all_books(
        session: AsyncSession = Depends(get_async_session),
):
    """Возвращает список всех авторов."""
    all_books = await book_crud.get_multi(session)
    return all_books


@router.get(
    '/{id}',
    response_model=BookDB,
)
async def get_book(
    book_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Показывает информацию о книге.
    """
    book = await book_crud.get(
        book_id, session
    )
    return book


@router.delete(
    '/{id}',
    response_model=BookDB,
    dependencies=[Depends(current_superuser)],
)
async def delete_book(
    book_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.

    Удаляет книгу.
    """
    book = await book_crud.remove(
        book_id, session
    )
    return book


@router.patch(
    '/{id}',
    response_model=BookDB,
    dependencies=[Depends(current_superuser)],
)
async def update_book(
        book_id: int,
        obj_in: BookUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.
    Обновление книги.
    """
    book = await validate_book_exists(book_id, session)
    updated_book = await book_crud.update(book, obj_in, session)
    return updated_book
