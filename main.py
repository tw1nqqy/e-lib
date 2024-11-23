from models import Library
from schemas import Status


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
                year = input("Write down book year: ")
                library.add_book(title, author, year)

            case '2':
                try:
                    book_id = int(input("Write down book ID to delete: "))
                    library.remove_book(book_id)
                except ValueError:
                    print("Error: write down correct ID.")

            case '3':
                search_term = input("Write down title, author or yer to find book: ")
                found_books = library.find_books(search_term)
                if found_books:
                    for book in found_books:
                        print(book)
                else:
                    print("Books not found.")

            case '4':
                library.display_books()

            case '5':
                try:
                    book_id = int(input("Write down book ID to change status: "))
                    new_status = input("Choice book status:\n 1) Available\n 2) Issued")

                    new_status = Status.available if new_status == "1" else Status.issued

                    library.change_status(book_id, new_status)
                except ValueError:
                    print("Error: write down correct ID.")

            case '6':
                print("Exit from program.")
                break

            case _:
                print("Error: choose correct action.")


if __name__ == "__main__":
    main()