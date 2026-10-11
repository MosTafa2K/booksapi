from fastapi import HTTPException, Response, status

database: list[dict] = [
    {
        "id": 1,
        "title": "The Pragmatic Programmer",
        "isbn": "9780135957059",
        "description": "راهنمایی کاربردی برای توسعه‌دهندگان نرم‌افزار.",
        "author": {
            "first_name": "Andrew",
            "last_name": "Hunt",
        },
        "genre": "Programming",
        "published_year": 1999,
        "available": True,
    },
    {
        "id": 2,
        "title": "Clean Code",
        "isbn": "9780132350884",
        "description": "اصول نوشتن کد خوانا، قابل نگهداری و تمیز.",
        "author": {
            "first_name": "Robert C.",
            "last_name": "Martin",
        },
        "genre": "Programming",
        "published_year": 2008,
        "available": True,
    },
    {
        "id": 3,
        "title": "1984",
        "isbn": "9780451524935",
        "description": "رمانی درباره جامعه‌ای تحت نظارت و کنترل کامل.",
        "author": {
            "first_name": "George",
            "last_name": "Orwell",
        },
        "genre": "Dystopian Fiction",
        "published_year": 1949,
        "available": False,
    },
    {
        "id": 4,
        "title": "Atomic Habits",
        "isbn": "9780735211292",
        "description": "روش‌های عملی برای ساخت عادت‌های خوب و پایدار.",
        "author": {
            "first_name": "James",
            "last_name": "Clear",
        },
        "genre": "Self-help",
        "published_year": 2018,
        "available": True,
    },
]


def get_all_books():
    """Get all books from the database."""
    return database


def get_book(book_id: int):
    """Get a book by its ID from the database.

    Args:
        book_id (int): The ID of the book to retrieve.

    Returns:
        dict: The book with the specified ID, or an error message if not found."""
    for book in database:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


def create_book(data: dict):
    """Create a new book in the database.

    Args:
        data (dict): The book data to create.

    Returns:
        dict: The created book."""
    new_book = {
        "id": len(database) + 1,
        **data,
    }
    database.append(new_book)
    return new_book


def update_book(book_id: int, updated_book: dict):
    """Update a book by its ID in the database.

    Args:
        book_id (int): The ID of the book to update.
        updated_book (dict): The updated book data.

    Returns:
        dict: The updated book, or an error message if not found."""

    book = get_book(book_id)
    book.update(updated_book)
    return book


def delete_book(book_id: int):
    """Delete a book by its ID from the database.

    Args:
        book_id (int): The ID of the book to delete.

    Returns:
        dict: A success message, or an error message if the book is not found."""
    book = get_book(book_id)
    database.remove(book)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
