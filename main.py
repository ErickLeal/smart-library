
from fastapi import FastAPI
from app.application.v1.books.book_controller import books_router_v1
from app.errors.base import DatabaseError, ValidationError
from app.errors.handler import error_handler, pydantic_validation_handler
from fastapi.exception_handlers import RequestValidationError
from fastapi import Request
from fastapi.responses import JSONResponse
from app.infrastructure.base import Base
from app.infrastructure.database import engine
import asyncio


app = FastAPI()
app.add_exception_handler(DatabaseError, error_handler)
app.add_exception_handler(RequestValidationError, pydantic_validation_handler)
app.include_router(books_router_v1)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.create_all)
