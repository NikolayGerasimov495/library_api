from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class Book(Base):
    title = Column(String, index=True)
    description = Column(String)
    author_id = Column(Integer, ForeignKey("author.id"))
    available_copies = Column(Integer)
