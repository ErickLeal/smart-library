from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.application.books.schemas import BookCreate, BookRead
from app.application.books.book_service import BookService
from app.infrastructure.books.book_repository_postgres import BookRepositoryPostgres
from app.infrastructure.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.books.book import Book

router = APIRouter()

def get_book_service(session: AsyncSession = Depends(get_session)):
    repo = BookRepositoryPostgres(session)
    return BookService(repo)

@router.get("/books", response_model=List[BookRead])
async def list_books(service: BookService = Depends(get_book_service)):
    return await service.list_books()

@router.get("/books/{book_id}", response_model=BookRead)
async def get_book(book_id: int, service: BookService = Depends(get_book_service)):
    book = await service.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/books", response_model=BookRead, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate, service: BookService = Depends(get_book_service)):

    book_instance = Book(id=None, **book.dict())
    return await service.create_book(book_instance)

@router.put("/books/{book_id}", response_model=BookRead)
async def update_book(book_id: int, book: BookCreate, service: BookService = Depends(get_book_service)):
    from app.domain.books.book import Book
    book_instance = Book(id=book_id, **book.dict())
    return await service.update_book(book_instance)

@router.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int, service: BookService = Depends(get_book_service)):
    await service.delete_book(book_id)
