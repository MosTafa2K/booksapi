from datetime import datetime

from pydantic import BaseModel, Field


class Author(BaseModel):
    first_name: str
    last_name: str


class BookCreate(BaseModel):
    title: str
    isbn: str
    description: str
    author: Author
    genre: str
    available: bool
    published_year: datetime = Field(min_length=4, max_length=4)


class BookResponse(BaseModel):
    id: int
    title: str
    isbn: str
    genre: str
    available: bool
    published_year: int


class BookDetailResponse(BookCreate):
    id: int
    description: str
    author: Author
