from fastapi import FastAPI
from app.application.v1.books.book_controller import books_router_v1
from app.infrastructure.base import Base
from app.infrastructure.database import engine
import asyncio

app = FastAPI()
app.include_router(books_router_v1)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.create_all)
