from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud, database, dependencies

app = FastAPI()

# Initialize DB
@app.on_event("startup")
def on_startup():
    database.init_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Catalog API"}

@app.get("/books/", response_model=List[schemas.BookRead])
async def list_books(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    return crud.get_books(db, skip=skip, limit=limit)

@app.get("/books/{book_id}", response_model=schemas.BookRead)
def get_book(book_id: int, db: Session = Depends(dependencies.get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books/", response_model=schemas.BookRead, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_book(db, book)

@app.put("/books/{book_id}", response_model=schemas.BookRead)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(dependencies.get_db)):
    updated = crud.update_book(db, book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(dependencies.get_db)):
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return None 