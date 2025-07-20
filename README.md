# Book Catalog API

A simple, modern RESTful API created for the purposes of a hometask.

## Features
- CRUD operations for books (Create, Read, Update, Delete)
- SQLite database with SQLAlchemy ORM
- Pydantic validation for all data
- Async endpoints for performance
- Auto-generated interactive API docs
- Unit and integration tests

## Requirements
- Python 3.8+

## Installation
1. **Clone the repository** (if needed):
   ```bash
   git clone <your-repo-url>
   cd hometask
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the App
Start the FastAPI server with:
```bash
uvicorn app.main:app --reload
```
- Visit [http://localhost:8000](http://localhost:8000) for a welcome message.
- Explore the interactive API docs at [http://localhost:8000/docs](http://localhost:8000/docs)
- Or see ReDoc at [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Running the Tests
To run all unit and integration tests:
```bash
python -m pytest
```

## Project Structure
```
hometask/
  app/
    __init__.py
    main.py         # FastAPI app and endpoints
    models.py       # SQLAlchemy models
    schemas.py      # Pydantic schemas
    crud.py         # CRUD logic
    database.py     # DB setup
    dependencies.py # FastAPI dependencies
  tests/
    test_main.py    # Integration tests (API)
    test_crud.py    # Unit tests (CRUD logic)
  requirements.txt
  README.md
```

## API Overview
- `GET /books/` — List all books
- `GET /books/{id}` — Get a book by ID
- `POST /books/` — Create a new book
- `PUT /books/{id}` — Update a book
- `DELETE /books/{id}` — Delete a book

All endpoints use JSON. See `/docs` for full details and try out the API interactively!

## Notes
- Data is stored in a local SQLite file (`books.db`).
- Pydantic ensures all data is validated (e.g., published year must be realistic).
- Error handling and edge cases are covered by both code and tests.
