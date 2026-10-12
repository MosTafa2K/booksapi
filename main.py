from fastapi import FastAPI, Response, status

from book_crud import create_book, delete_book, get_all_books, get_book, update_book
from schemas import BookCreate, BookDetailResponse, BookResponse, BookUpdate

api = FastAPI()


@api.get("/books", response_model=list[BookResponse])
def books_list_endpoint():
    """Return all books in the database."""
    return get_all_books()


@api.post("/books", response_model=BookDetailResponse)
def insert_book_endpoint(book_data: BookCreate):
    """Create a new book from the request body and return it."""
    book = create_book(book_data.model_dump())
    return book


@api.get("/books/{book_id}", response_model=BookDetailResponse)
def get_single_book_endpoint(book_id: int):
    """Return the book identified by ``book_id``."""
    book = get_book(book_id)
    return book


@api.patch("/books/{book_id}", response_model=BookDetailResponse)
def update_book_endpoint(book_id: int, update_data: BookUpdate):
    """Apply the supplied fields to the book identified by ``book_id``."""
    updated_data = update_data.model_dump(exclude_unset=True, exclude_none=True)
    book = update_book(book_id, updated_data)
    return book


@api.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_endpoint(book_id: int):
    """Delete the book identified by ``book_id``."""
    delete_book(book_id)
