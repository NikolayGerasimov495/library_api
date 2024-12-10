from datetime import date
from typing import Optional

from pydantic import BaseModel, Extra


class BorrowBase(BaseModel):
    book_id: int
    user_id: int
    borrow_date: date
    return_date: Optional[date] = None

    class Config:
        extra = Extra.forbid


class BorrowCreate(BorrowBase):
    book_id: int
    user_id: int
    borrow_date: date


class BorrowUpdate(BaseModel):
    return_date: date

    class Config:
        orm_mode = True

class BorrowDB(BorrowBase):
    id: int

    class Config:
        extra = Extra.forbid
        orm_mode = True
