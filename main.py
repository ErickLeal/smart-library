from fastapi import FastAPI
from app.application.books.book_controller import router as book_router
from app.infrastructure.base import Base
from app.infrastructure.database import engine
import asyncio

app = FastAPI()
app.include_router(book_router)

@app.on_event("startup")
async def on_startup():
    # Cria as tabelas no banco, se não existirem
    async with engine.begin() as conn:
        await conn.run_sync(Base.create_all)
