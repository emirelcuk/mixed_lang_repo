class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author1
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(book)

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. List Books")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Book Title: ")
            author = input("Book Author: ")
            isbn = input("Book ISBN: ")
            library.add_book(Book(title, author, isbn))
            print("Book added.")

        elif choice == '2':
            isbn_to_remove = input("Enter ISBN of the book to remove: ")
            library.remove_book(isbn_to_remove)
            print("Book removed.")

        elif choice == '3':
            search_title = input("Enter title of the book to search: ")
            found_book = library.find_book_by_title(search_title)
            if found_book:
                print("Book Found:", found_book)
            else:
                print("Book not found.")

        elif choice == '4':
            print("Books in the library:")
            library.list_books()

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
