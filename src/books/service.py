from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.books.models import Book
from sqlalchemy.exc import NoResultFound


async def create_book(db: AsyncSession, book):
    new_book = Book(**book.dict())
    db.add(new_book)
    await db.commit()
    await db.refresh(new_book)

    return new_book

async def get_all_books(db:AsyncSession):
    result = await db.execute(select(Book))
    return result.scalars().all()

async def get_by_id(db: AsyncSession, book_id):
    result = await db.execute(select(Book).where(Book.uid == book_id))
    try:
        return result.scalar_one()  # returns single Book or raises error
    except NoResultFound:
        return None


async def update_book(db: AsyncSession, book_id: str, book_update):
    result = await db.execute(select(Book).where(Book.uid==book_id))

    book = result.scalar_one_or_none()

    if book is None:
        return None
    
    for key, value in book_update.model_dump(exclude_unset=True).items():
        setattr(book , key, value)

    await db.commit()
    await db.refresh(book)

    return book


async def delete_book(db: AsyncSession, book_id: str):
    result = await db.execute(select(Book).where(Book.uid == book_id))

    book = result.scalar_one_or_none()

    if book is None:
        return None
    
    await db.delete(book)
    await db.commit()

    return True