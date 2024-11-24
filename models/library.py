from .book import Book
from schemas import Status
import sqlite3
from typing import List


class Library:
    def __init__(self, db_name='library.db'):
        try:
            self.connection = sqlite3.connect(db_name)
            self.create_table()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def create_table(self):
        try:
            with self.connection:
                self.connection.execute('''
                    CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        year INTEGER NOT NULL,
                        status TEXT CHECK(status IN ('available', 'issued')) NOT NULL
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_book(self, title: str, author: str, year: int) -> int:
        try:
            with self.connection:
                cursor = self.connection.execute('''
                    INSERT INTO books (title, author, year, status) VALUES (?, ?, ?, ?)
                ''', (title, author, year, "available"))
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding book: {e}")
            return -1  # Indicate failure

    def remove_book(self, book_id: int):
        try:
            with self.connection:
                cursor = self.connection.execute('DELETE FROM books WHERE id = ?', (book_id,))
                if cursor.rowcount == 0:
                    raise ValueError("Book with this ID not found.")
                print("Book removed successfully.")
        except ValueError as ve:
            print(ve)
        except sqlite3.Error as e:
            print(f"Error removing book: {e}")

    def find_books(self, title: str | None = None, author: str | None = None, year: int | None = None) -> List[Book]:
        query = 'SELECT * FROM books'
        params = []

        if title or author or year:
            query += f' WHERE 1=1'

        if title:
            query += ' AND title LIKE ?'
            params.append(f'%{title}%')
        if author:
            query += ' AND author LIKE ?'
            params.append(f'%{author}%')
        if year:
            query += ' AND year = ?'
            params.append(year)

        try:
            cursor = self.connection.execute(query, params)
            return [Book(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error finding books: {e}")
            return []

    def change_status(self, book_id: int, new_status: Status):
        try:
            with self.connection:
                cursor = self.connection.execute('UPDATE books SET status = ? WHERE id = ?',
                                                 (new_status.value, book_id))
                if cursor.rowcount == 0:
                    raise ValueError("Book with this ID not found.")
                print("Book status updated successfully.")
        except ValueError as ve:
            print(ve)
        except sqlite3.Error as e:
            print(f"Error changing book status: {e}")

    def display_books(self) -> List[Book]:
        try:
            cursor = self.connection.execute('SELECT * FROM books')
            return [Book(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error displaying books: {e}")
            return []
