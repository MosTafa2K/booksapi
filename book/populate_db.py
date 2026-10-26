from sqlmodel import Session, SQLModel

from .database import engine
from .models import Author, Book

AUTHORS = [
    Author(first_name="George", last_name="Orwell"),
    Author(first_name="Robert", last_name="Martin"),
    Author(first_name="Andrew", last_name="Fowler"),
]

BOOKS = [
    Book(title="Nineteen Eighty-Four", isbn="9780451524935", description="A dystopian novel about surveillance and totalitarianism.", genre="Dystopian fiction", published_year=1949, available=True, author_id=1),
    Book(title="Animal Farm", isbn="9780451526342", description="An allegorical novella about power and political corruption.", genre="Political satire", published_year=1945, available=True, author_id=1),
    Book(title="Clean Code", isbn="9780132350884", description="A practical guide to writing readable and maintainable code.", genre="Programming", published_year=2008, available=True, author_id=2),
    Book(title="Clean Architecture", isbn="9780134494166", description="Principles for designing maintainable software systems.", genre="Programming", published_year=2017, available=False, author_id=2),
    Book(title="The Clean Coder", isbn="9780137081073", description="Advice and professional practices for software developers.", genre="Programming", published_year=2011, available=True, author_id=2),
    Book(title="The Pragmatic Programmer", isbn="9780135957059", description="A guide to effective software development practices.", genre="Programming", published_year=1999, available=True, author_id=3),
    Book(title="Programming Pearls", isbn="9780201657883", description="Practical problem-solving techniques for programmers.", genre="Programming", published_year=1999, available=False, author_id=3),
    Book(title="Refactoring", isbn="9780134757599", description="Techniques for improving the design of existing code.", genre="Programming", published_year=2018, available=True, author_id=3),
]


def populate_database() -> None:
    """Create the database tables and populate them with sample data."""
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add_all(AUTHORS)
        session.add_all(BOOKS)
        session.commit()

    print("Created 3 authors and 8 books.")


if __name__ == "__main__":
    populate_database()
