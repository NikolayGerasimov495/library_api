from app.crud.base import CRUDBase
from app.models.borrow import Borrow


class CRUDBorrow(CRUDBase):
    pass


borrow_crud = CRUDBorrow(Borrow)
