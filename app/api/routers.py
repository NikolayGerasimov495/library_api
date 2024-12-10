from fastapi import APIRouter

from app.api.endpoints import (author_router, borrow_router, book_router,
                               user_router)

main_router = APIRouter()
main_router.include_router(
    author_router, prefix='/authors', tags=['Authors']
)
main_router.include_router(
    book_router, prefix='/books', tags=['Books']
)
main_router.include_router(
    borrow_router, prefix='/borrows', tags=['Borrows']
)
main_router.include_router(user_router)
