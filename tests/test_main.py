import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_root():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to the Book Catalog API"}

@pytest.mark.asyncio
async def test_book_crud():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Create a book
        book = {
            "title": "This is me testing, creatig a book",
            "author": "Ibrahim Imran",
            "published_year": 2003,
            "summary": "The curious case of Benjamin Button. this is just me testing the crud operations for this task."
        }
        response = await ac.post("/books/", json=book)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == book["title"]
        assert data["author"] == book["author"]
        assert data["published_year"] == book["published_year"]
        assert data["summary"] == book["summary"]
        book_id = data["id"]

        # Get   book
        response = await ac.get(f"/books/{book_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == book["title"]

        # List all the books currently existing in the database
        response = await ac.get("/books/")
        assert response.status_code == 200
        assert any(b["id"] == book_id for b in response.json())

        # change the already existing information about the book.
        update = {"title": "Updated Book of Testing", "author": "Test Author Ibrahim Imran", "published_year": 1974, "summary": "Updated finally."}
        response = await ac.put(f"/books/{book_id}", json=update)
        assert response.status_code == 200
        assert response.json()["title"] == "Updated Book of Testing"

        # Delete the book
        response = await ac.delete(f"/books/{book_id}")
        assert response.status_code == 204

        # Ensure book is deleted
        response = await ac.get(f"/books/{book_id}")
        assert response.status_code == 404 