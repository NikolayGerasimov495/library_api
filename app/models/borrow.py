from sqlalchemy import Column, Integer, ForeignKey, Date


from app.core.db import Base


class Borrow(Base):
    book_id = Column(Integer, ForeignKey('book.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    borrow_date = Column(Date)
    return_date = Column(Date)
