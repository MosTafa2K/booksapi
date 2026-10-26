from datetime import date

from sqlmodel import Field, Relationship, SQLModel


class Author(SQLModel, table=True):
    id: int = Field(primary_key=True, unique=True)
    first_name: str = Field(min_length=5)
    last_name: str = Field(min_length=5)
    books: list["Book"] = Relationship(back_populates="author")


class Book(SQLModel, table=True):
    id: int = Field(primary_key=True, unique=True)
    title: str = Field(min_length=5)
    isbn: str = Field(min_length=10, max_length=13)
    description: str = Field()
    genre: str = Field()
    published_year: int = Field(ge=1900, le=date.today().year)  # noqa: DTZ011
    available: bool = Field(default=False)

    author_id: int = Field(foreign_key="author.id")
    author: Author = Relationship(back_populates="books")
