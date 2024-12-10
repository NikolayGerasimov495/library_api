from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Borrow, Author, Book
from app.models.user import User


async def validate_author_exists(author_id: int, session: AsyncSession):
    author = await session.get(Author, author_id)
    if author is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Автор не найден."
        )
    return author


async def check_user_id_exists(
        user_id: int,
        session: AsyncSession,
):
    user = await session.get(
        User, user_id
    )
    if user is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Пользователь не найден!'
        )
    return user


async def check_borrow_exists(borrow_id: int, session: AsyncSession):
    borrow = await session.get(Borrow, borrow_id)
    if not borrow:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Выдача не найдена"
        )
    return borrow


async def validate_book_exists(book_id: int, session: AsyncSession):
    book = await session.get(Book, book_id)
    if book is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Книга не найдена."
        )
    return book