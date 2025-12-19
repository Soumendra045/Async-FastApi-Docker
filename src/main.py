from fastapi import FastAPI
# from db.main import engine, Base
from contextlib import asynccontextmanager


# from src.books.models import Book  
from src.routers import book_router
from src.db.init_db import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    # 🔹 Startup logic
    print("server started")
    await init_db()
    yield
    print("server stoped")
    # 🔹 Shutdown logic (optional)
    # await close_db_connections()

version = "v1"

app = FastAPI(
    version=version,
    lifespan=life_span
)
# @app.on_event("startup")
# async def startup():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all())

app.include_router(book_router.router)