from pydantic import BaseModel, Extra


class BookBase(BaseModel):
    title: str
    description: str
    author_id: int
    available_copies: int

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookDB(BookBase):
    id: int

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1
        orm_mode = True
