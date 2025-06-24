from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Management API! Visit /docs to explore."}


class Book(BaseModel):
    id: int
    title: str
    author: str

books = []

@app.post("/books/")
def add_book(book: Book):
    for existing_book in books:
        if existing_book.id == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")
    books.append(book)
    return {"message": "Book added!", "book": book}

@app.get("/books/")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = updated_book
            return {"message": "Book updated", "book": updated_book}
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            deleted = books.pop(index)
            return {"message": "Book deleted", "book": deleted}
    raise HTTPException(status_code=404, detail="Book not found")
