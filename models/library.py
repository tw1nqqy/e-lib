from .book import Book
from schemas import Status


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.__books.append(new_book)
        print(f"Book '{title}' added to library.")

    def remove_book(self, book_id):
        for book in self.__books:
            if book.id == book_id:
                self.__books.remove(book)
                print(f"Book '{book.title}' deleted from library.")
                return
        print("Error: book with this ID not found.")

    def find_books(self, search_term):
        found_books = [book for book in self.__books if (search_term.lower() in book.title.lower() or
                                                         search_term.lower() in book.author.lower() or
                                                         search_term == str(book.year))]
        return found_books

    def display_books(self):
        if not self.__books:
            print("Library is empty.")
            return
        for book in self.__books:
            print(book)

    def change_status(self, book_id, new_status: Status):
        for book in self.__books:
            if book.id == book_id:
                book.status = new_status
                print(f"Book status '{book.title}' haas changed to '{new_status}'.")
                return
        print("Error: book with this ID not found.")
