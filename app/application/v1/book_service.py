from typing import List, Optional
from app.domain.books.book import Book
from app.domain.books.book_repository import BookRepository

class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    async def list_books(self) -> List[Book]:
        return await self.repository.get_all()

    async def get_book(self, book_id: int) -> Optional[Book]:
        return await self.repository.get_by_id(book_id)

    async def create_book(self, book: Book) -> Book:
        book.process_extra_info()
        return await self.repository.create(book)

    async def update_book(self, book: Book) -> Book:
        book.process_extra_info()
        return await self.repository.update(book)

    async def delete_book(self, book_id: int) -> None:
        await self.repository.delete(book_id)
