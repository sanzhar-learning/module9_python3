import os
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3


DB_PATH = os.environ.get("DB_PATH", "books.db")

app = FastAPI()


def get_db():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT
        )
    """
    )
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM books")
    if cursor.fetchone()[0] == 0:
        BOOKS = [
            (1, "Crime and Punishment", "A psychological novel by Fyodor Dostoevsky."),
            (2, "1984", "A dystopian social science fiction novel by George Orwell."),
            (
                3,
                "To Kill a Mockingbird",
                "A gripping tale of racial injustice and childhood innocence.",
            ),
            (4, "The Great Gatsby", "A classic American novel about the Jazz Age."),
            (5, "Pride and Prejudice", "A romantic novel of manners by Jane Austen."),
        ]
        for book in BOOKS:
            cursor.execute(
                "INSERT OR REPLACE INTO books (id, title, description) VALUES (?, ?, ?)",
                book,
            )
        conn.commit()
    conn.close()


init_db()


class Book(BaseModel):
    title: str
    description: str


@app.get("/books")
def read_books():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description FROM books")
    books = cursor.fetchall()
    return [
        {"id": id, "title": title, "description": description}
        for id, title, description in books
    ]


@app.post("/books")
def create_book(book: Book):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO books (title, description) VALUES (?, ?)
        """,
        (book.title, book.description),
    )
    conn.commit()
    return {"message": "Book created successfully"}


@app.get("/books/{book_id}")
def read_book(book_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()
    if book:
        return {"id": book[0], "title": book[1], "description": book[2]}
    else:
        return {"message": "Book not found"}
