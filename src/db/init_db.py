from src.db.database import engine, Base

from src.books.models import Book  


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("✅ Tables after create:", Base.metadata.tables)