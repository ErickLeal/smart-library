from abc import ABC, abstractmethod
from typing import List, Optional
from .book import Book

class BookRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[Book]:
        pass

    @abstractmethod
    async def get_by_id(self, book_id: int) -> Optional[Book]:
        pass

    @abstractmethod
    async def create(self, book: Book) -> Book:
        pass

    @abstractmethod
    async def update(self, book: Book) -> Book:
        pass

    @abstractmethod
    async def delete(self, book_id: int) -> None:
        pass
