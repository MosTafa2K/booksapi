# Books API

A simple library management API built with [FastAPI](https://fastapi.tiangolo.com/), [SQLModel](https://sqlmodel.tiangolo.com/), and PostgreSQL.

Books and authors are stored in a PostgreSQL database. The application creates the required database tables when it starts.

## Requirements

- Python 3.13 or newer
- PostgreSQL

## Configuration

Create a `.env` file in the project root. You can use `.env.example` as a starting point:

```env
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/booksdb
```

Replace the values with the connection details of your PostgreSQL database.

## Installation and running

Install the project dependencies and start the development server:

```bash
uv sync
uv run uvicorn main:api --reload
```

You can also install the dependencies with `pip`:

```bash
pip install -r requirements.txt
uvicorn main:api --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Sample data

To create the database tables and insert the sample authors and books, run:

```bash
python -m book.populate_db
```

If you are using uv, run:

```bash
uv run python -m book.populate_db
```

## Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/books` | Get a list of books |
| POST | `/books` | Add a new book and author |
| GET | `/books/{book_id}` | Get a specific book with its author details |
| PATCH | `/books/{book_id}` | Update selected book or author fields |
| DELETE | `/books/{book_id}` | Delete a book |

## Example request

To create a book, send a `POST` request to `/books` with JSON data like this:

```json
{
  "title": "The Pragmatic Programmer",
  "isbn": "9780135957059",
  "description": "A guide to effective software development practices.",
  "author": {
    "first_name": "Andrew",
    "last_name": "Fowler"
  },
  "genre": "Programming",
  "available": true,
  "published_year": 1999
}
```

To partially update a book, send only the fields that need to change:

```json
{
  "available": false,
  "author": {
    "last_name": "Updated"
  }
}
```

## License

This project is licensed under the [MIT License](LICENSE).
