
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.application.v1.books.schemas import BookCreate, BookRead
from app.application.v1.books.book_service import BookService
from app.infrastructure.books.book_repository_postgres import BookRepositoryPostgres
from app.infrastructure.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.books.book import Book
from app.errors.handler import SucessResponseEnvelope, ErrorResponseEnvelope
from fastapi.responses import JSONResponse


books_router_v1 = APIRouter(prefix="/v1/books")

def get_book_service(session: AsyncSession = Depends(get_session)):
    repo = BookRepositoryPostgres(session)
    return BookService(repo)

from app.application.v1.books.schemas import BookRead

@books_router_v1.get("/")
async def list_books(service: BookService = Depends(get_book_service)):
    books = await service.list_books()
    books_data = [BookRead(**b.__dict__).dict() for b in books]
    return JSONResponse(
        status_code=200,
        content=SucessResponseEnvelope(data=books_data).dict()
    )
@books_router_v1.get("/{book_id}")
async def get_book(book_id: int, service: BookService = Depends(get_book_service)):
    book = await service.get_book(book_id)
    if not book:
        return JSONResponse(
            status_code=404,
            content=ErrorResponseEnvelope(error={"code": "not_found", "message": "Book not found"}).dict()
        )
    book_data = BookRead.from_orm(book).dict()
    return JSONResponse(
        status_code=200,
        content=SucessResponseEnvelope(data=book_data).dict()
    )

@books_router_v1.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate, service: BookService = Depends(get_book_service)):
    book_instance = Book(id=None, **book.dict())
    created = await service.create_book(book_instance)
    created_data = BookRead.from_orm(created).dict()
    return JSONResponse(
        status_code=201,
        content=SucessResponseEnvelope(data=created_data).dict()
    )


@books_router_v1.put("/{book_id}")
async def update_book(book_id: int, book: BookCreate, service: BookService = Depends(get_book_service)):
    from app.domain.books.book import Book
    book_instance = Book(id=book_id, **book.dict())
    updated = await service.update_book(book_instance)
    updated_data = BookRead.from_orm(updated).dict()
    return JSONResponse(
        status_code=200,
        content=SucessResponseEnvelope(data=updated_data).dict()
    )

@books_router_v1.delete("/{book_id}")
async def delete_book(book_id: int, service: BookService = Depends(get_book_service)):
    await service.delete_book(book_id)
    return JSONResponse(
        status_code=204,
        content=SucessResponseEnvelope(data=None).dict()
    )
