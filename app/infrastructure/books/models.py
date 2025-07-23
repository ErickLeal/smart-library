from sqlalchemy import Column, Integer, String, Boolean
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BookModel(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    pages = Column(Integer, nullable=False, default=0)
    is_big = Column(Boolean, nullable=False, server_default=sa.text('false'))
    is_old = Column(Boolean, nullable=False, server_default=sa.text('false'))   
