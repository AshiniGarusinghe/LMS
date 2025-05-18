# db.py
import sqlite3

# Connect and create table
def connect():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER,
            issued_to TEXT
        )
    """)
    conn.commit()
    conn.close()

# Add new book
def add_book(title, author, year):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title, author, year, issued_to) VALUES (?, ?, ?, ?)",
                (title, author, year, None))
    conn.commit()
    conn.close()

# View all books
def view_books():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

# Search books
def search_books(keyword):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
                (f'%{keyword}%', f'%{keyword}%'))
    rows = cur.fetchall()
    conn.close()
    return rows

# Issue book
def issue_book(book_id, user):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET issued_to = ? WHERE id = ?", (user, book_id))
    conn.commit()
    conn.close()

# Return book
def return_book(book_id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET issued_to = NULL WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

# Delete book
def delete_book(book_id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
