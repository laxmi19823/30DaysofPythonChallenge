from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from datetime import datetime
import logging

# -------------------- App Setup --------------------
app = FastAPI(title="📘 Book Manager API", version="1.0")

# -------------------- Logging Setup --------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"{request.method} {request.url}")
    return await call_next(request)

# -------------------- Database Config --------------------
DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# -------------------- Models --------------------
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)

Base.metadata.create_all(bind=engine)

# -------------------- Pydantic Schemas --------------------
class BookBase(BaseModel):
    title: str
    author: str
    year: int

    class Config:
        orm_mode = True

class BookOut(BookBase):
    id: int

# -------------------- Dependency --------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------- Routes --------------------

# ➕ Create a book
@app.post("/books/", response_model=BookOut, summary="Add a new book")
def create_book(book: BookBase, db: Session = Depends(get_db)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# 📚 Get all books
@app.get("/books/", response_model=list[BookOut], summary="View all books")
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

# 🔍 Get book by ID
@app.get("/books/{book_id}", response_model=BookOut, summary="Get book by ID")
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# ❌ Delete book by ID
@app.delete("/books/{book_id}", summary="Delete book by ID")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": f"Book {book_id} deleted successfully"}
