from asyncio.log import logger

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_user_id_exists,
                                check_borrow_exists)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.borrow import borrow_crud
from app.schemas.borrow import (BorrowCreate,
                                BorrowDB,
                                BorrowUpdate)
from app.services.processing import (decrease_available_copies,
                                     increase_available_copies)

router = APIRouter()


@router.post(
    '/',
    response_model=BorrowDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_borrow(
        borrow: BorrowCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.

    Создает запись о выдаче.
    """
    await check_user_id_exists(borrow.user_id, session)

    await decrease_available_copies(borrow.book_id, session)

    new_borrow = await borrow_crud.create(borrow, session)

    return new_borrow


@router.get('/',
            response_model=list[BorrowDB],
            )
async def get_all_borrows(
        session: AsyncSession = Depends(get_async_session),
):
    """Возвращает список всех выдач."""
    all_borrows = await borrow_crud.get_multi(session)
    return all_borrows


@router.get(
    '/{id}',
    response_model=BorrowDB,
)
async def get_borrow(
        borrow_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """
    Показывает информацию о конкретной выдаче.
    """
    borrow = await borrow_crud.get(
        borrow_id, session
    )
    return borrow


@router.patch(
    '/{id}/return',
    response_model=BorrowDB,
    dependencies=[Depends(current_superuser)],
)
async def update_borrow(
        id: int,
        obj_in: BorrowUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.
    Завершение выдачи.
    """
    borrow = await check_borrow_exists(id, session)

    borrow.return_date = obj_in.return_date

    await increase_available_copies(borrow.book_id, session)

    borrow_update = await borrow_crud.update(borrow, obj_in, session)
    return borrow_update
