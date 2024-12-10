from app.crud.base import CRUDBase
from app.models.author import Author


class CRUDAuthor(CRUDBase):
    pass


author_crud = CRUDAuthor(Author)
