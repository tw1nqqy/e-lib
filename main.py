from models import Library
from schemas import Status
import json


def main():
    library = Library()

    while True:
        print("\n1. Add book")
        print("2. Delete book")
        print("3. Find book")
        print("4. Display all books")
        print("5. Change book status")
        print("6. Exit")

        choice = input("Choose action (1-6): ")

        match choice:

            case '1':
                title = input("Write down book title: ")
                author = input("Write down book author: ")
                year = int(input("Write down book year: "))
                library.add_book(title, author, year)

            case '2':
                try:
                    book_id = int(input("Write down book ID to delete: "))
                    library.remove_book(book_id)
                except ValueError:
                    print("Error: write down correct ID.")

            case '3':
                title = input("Write down title (or leave it empty): ")
                author = input("Write down author (or leave it empty): ")
                year_input = input("Write down year (or leave it empty): ")
                year = int(year_input) if year_input else None

                books_found = library.find_books(title=title or None, author=author or None, year=year)

                if books_found:
                    for book in books_found:
                        print(json.dumps(book.to_json(), ensure_ascii=False))
                else:
                    print("Books not found.")

            case '4':
                books = library.display_books()
                for book in books:
                    print(json.dumps(book.to_json(), ensure_ascii=False))

            case '5':
                book_id = int(input("Write down book ID to change status: "))
                new_status = input("Choice book status:\n 1) Available\n 2) Issued")

                new_status = Status.available if new_status == "1" else Status.issued
                try:
                    library.change_status(book_id, new_status)
                    print("Book status changed.")
                except ValueError as e:
                    print(e)

            case '6':
                print("Exit from program.")
                break

            case _:
                print("Error: choose correct action.")


if __name__ == "__main__":
    main()
