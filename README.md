# Books API

A simple library management API built with [FastAPI](https://fastapi.tiangolo.com/).

The application does not use a database. Books are stored in an in-memory Python list, so all changes are lost when the application stops.

## Requirements

- Python 3.13 or newer

## Installation and running

Install the project dependencies and start the development server:

```bash
uv sync
uv run uvicorn main:api --reload
```

You can also install the dependencies with `pip`:

```bash
pip install -e .
uvicorn main:api --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at `/docs`.

## Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/books` | Get a list of books |
| POST | `/books` | Add a new book |
| GET | `/books/{book_id}` | Get a specific book |
| PATCH | `/books/{book_id}` | Update selected fields of a book |
| DELETE | `/books/{book_id}` | Delete a book |

## Example request

To create a book, send a `POST` request to `/books` with JSON data like this:

```json
{
  "title": "The Pragmatic Programmer",
  "isbn": "9780135957059",
  "description": "A practical guide to software development.",
  "author": {
    "first_name": "Andrew",
    "last_name": "Hunt"
  },
  "genre": "Programming",
  "available": true,
  "published_year": 1999
}
```

## License

This project is licensed under the [MIT License](LICENSE).
