from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.domain.books.book import Book
from app.domain.books.book_repository import BookRepository
from app.infrastructure.books.models import BookModel

class BookRepositoryPostgres(BookRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> List[Book]:
        result = await self.session.execute(select(BookModel))
        books = result.scalars().all()
        return [Book(id=b.id, title=b.title, author=b.author, year=b.year, pages=b.pages) for b in books]

    async def get_by_id(self, book_id: int) -> Optional[Book]:
        book = await self.session.get(BookModel, book_id)
        if book:
            return Book(id=book.id, title=book.title, author=book.author, year=book.year, pages=book.pages)
        return None

    async def create(self, book: Book) -> Book:
        db_book = BookModel(title=book.title, author=book.author, year=book.year, pages=book.pages, is_big=book.is_big, is_old=book.is_old)
        self.session.add(db_book)
        await self.session.commit()
        await self.session.refresh(db_book)
        return Book(id=db_book.id, title=db_book.title, author=db_book.author, year=db_book.year, pages=db_book.pages, is_big=db_book.is_big, is_old=db_book.is_old)

    async def update(self, book: Book) -> Book:
        db_book = await self.session.get(BookModel, book.id)
        db_book.title = book.title
        db_book.author = book.author
        db_book.year = book.year
        db_book.pages = book.pages
        await self.session.commit()
        return Book(id=db_book.id, title=db_book.title, author=db_book.author, year=db_book.year, pages=db_book.pages)

    async def delete(self, book_id: int) -> None:
        db_book = await self.session.get(BookModel, book_id)
        await self.session.delete(db_book)
        await self.session.commit()
