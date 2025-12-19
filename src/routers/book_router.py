from fastapi import Depends, APIRouter, HTTPException
from src.books.schemas import BookCreateModel, BookResponse, BookUpdateModel
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.database import get_db
from src.books.service import create_book, get_all_books, get_by_id, update_book, delete_book
from typing import List

router = APIRouter(
    prefix='/book',
    tags=['book']
)

@router.post('/',response_model=BookResponse, status_code=201)
async def create(book: BookCreateModel, db: AsyncSession = Depends(get_db)):
    return await create_book(db, book)

@router.get('/get_all_books',response_model=List[BookResponse])
async def get_books(db:AsyncSession = Depends(get_db)):
    books = await get_all_books(db)
    return books

@router.get('/get_by_id/{book_id}',response_model=BookResponse)
async def get_book_by_id(book_id: str, db:AsyncSession = Depends(get_db)):
    result = await get_by_id(db, book_id)

    return result

@router.put('/update_by_book_id/{book_id}',response_model=BookResponse)
async def update_by_book_id(book_id: str, book_update: BookUpdateModel, db: AsyncSession = Depends(get_db)):
    result = await update_book(db, book_id, book_update)

    if not result:
        raise HTTPException(status_code=404, detail='Book not found')

    return result

@router.delete('/delete_by_book_id/{book_id}')
async def delete_by_book_id(book_id: str, db: AsyncSession = Depends(get_db)):
    result = await delete_book(db, book_id)

    if not result:
        raise HTTPException(status_code=404, detail="Book not found")
    return 'Deleted'