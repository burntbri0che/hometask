import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Book
from app import crud, schemas

@pytest.fixture(scope="function")
def db():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_make_and_get(db):
    book = schemas.BookCreate(title="UnitTest", author="Tester", published_year=2021, summary="Unit test book.")
    b = crud.create_book(db, book)
    assert b.id is not None
    got = crud.get_book(db, b.id)
    assert got.title == "UnitTest"
    assert got.author == "Tester"
    assert got.published_year == 2021
    assert got.summary == "Unit test book."

def test_update_and_remove(db):
    book = schemas.BookCreate(title="ToUpdate", author="Tester", published_year=2022, summary=None)
    b = crud.create_book(db, book)
    upd = schemas.BookUpdate(title="Updated", author="Tester", published_year=2022, summary="Updated summary.")
    changed = crud.update_book(db, b.id, upd)
    assert changed.title == "Updated"
    assert changed.summary == "Updated summary."
    gone = crud.delete_book(db, b.id)
    assert gone
    assert crud.get_book(db, b.id) is None 