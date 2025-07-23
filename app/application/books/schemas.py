from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    pages: int

class BookRead(BookCreate):
    id: int
    is_old: bool
    is_big: bool

    class Config:
        orm_mode = True
