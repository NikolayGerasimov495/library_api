from datetime import date

from pydantic import BaseModel, Extra


class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: date

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    pass


class AuthorDB(AuthorBase):
    id: int

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1
        orm_mode = True
