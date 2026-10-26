from fastapi import HTTPException
from sqlmodel import Session, select, update

from .models import Author, Book
from .schemas import BookCreate, BookUpdate


def get_all_books(db: Session):
    """Get all books from the database."""
    return db.exec(select(Book)).all()


def get_book(book_id: int, db: Session):
    """Get a book by its ID from the database.

    Args:
        book_id (int): The ID of the book to retrieve.

    Returns:
        dict: The book with the specified ID, or an error message if not found."""
    book = db.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


def create_book(data: BookCreate, db: Session):
    """Create a new book in the database.

    Args:
        data (dict): The book data to create.

    Returns:
        dict: The created book."""
    book_data = data.model_dump()
    author_data = book_data.pop("author")
    new_book = Book(**book_data, author=Author(**author_data))
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def update_book(book_id: int, updated_book: BookUpdate, db: Session):
    """Update a book by its ID in the database.

    Args:
        book_id (int): The ID of the book to update.
        updated_book (BookUpdate): The updated book data.

    Returns:
        dict: The updated book, or an error message if not found."""
    stmt = (
        update(Book)
        .where(Book.id == book_id)
        .values(**updated_book.model_dump(exclude_unset=True, exclude_none=True))
        .returning(Book)
    )
    result = db.exec(stmt)
    row = result.one_or_none()
    new_book = row[0]
    db.commit()
    return new_book if new_book is not None else None


def delete_book(book_id: int, db: Session):
    """Delete a book by its ID from the database.

    Args:
        book_id (int): The ID of the book to delete.

    Returns:
        dict: A success message, or an error message if the book is not found."""
    book = get_book(book_id, db)
    db.delete(book)
    db.commit()
