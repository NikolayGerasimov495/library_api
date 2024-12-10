from sqlalchemy import Column, Date, String

from app.core.db import Base


class Author(Base):
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    birth_date = Column(Date)
