from app.crud.base import CRUDBase
from app.models.book import Book


class CRUDBook(CRUDBase):
    pass


book_crud = CRUDBook(Book)
