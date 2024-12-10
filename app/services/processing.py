from http import HTTPStatus

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.models import Book


async def decrease_available_copies(book_id: int, session: AsyncSession):
    book = await session.get(Book, book_id)
    if book is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Книга не найдена.")

    if book.available_copies <= 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Книга недоступна для выдачи.")

    book.available_copies -= 1
    session.add(book)
    await session.commit()
    await session.refresh(book)


async def increase_available_copies(book_id: int, session: AsyncSession):
    book = await session.get(Book, book_id)
    if book is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Книга не найдена.")

    book.available_copies += 1
    session.add(book)
    await session.commit()
    await session.refresh(book)
