from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, status
from sqlmodel import Session, SQLModel

from book.crud import (
    create_book,
    delete_book,
    get_all_books,
    get_book,
    update_book,
)
from book.database import engine, get_db
from book.models import Author, Book  # noqa
from book.schemas import BookCreate, BookDetailResponse, BookResponse, BookUpdate


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


api = FastAPI(lifespan=lifespan)


@api.get("/books", response_model=list[BookResponse])
def books_list_endpoint(db: Annotated[Session, Depends(get_db)]):
    """Return all books in the database."""
    return get_all_books(db)


@api.post("/books", response_model=BookDetailResponse)
def insert_book_endpoint(
    book_data: BookCreate, db: Annotated[Session, Depends(get_db)]
):
    """Create a new book from the request body and return it."""
    book = create_book(book_data, db)
    return book


@api.get("/books/{book_id}", response_model=BookDetailResponse)
def get_single_book_endpoint(book_id: int, db: Annotated[Session, Depends(get_db)]):
    """Return the book identified by ``book_id``."""
    book = get_book(book_id, db)
    return book


@api.patch("/books/{book_id}", response_model=BookDetailResponse)
def update_book_endpoint(
    book_id: int, update_data: BookUpdate, db: Annotated[Session, Depends(get_db)]
):
    """Apply the supplied fields to the book identified by ``book_id``."""
    book = update_book(book_id, update_data, db)
    return book


@api.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_endpoint(book_id: int, db: Annotated[Session, Depends(get_db)]):
    """Delete the book identified by ``book_id``."""
    delete_book(book_id, db)
