class Book:
    def __init__(self, title, author):
        """Initialize a book with title and author, defaulting to available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Book is already checked out

    def return_book(self):
        """Marks the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available."""
        return not self._is_checked_out

class Library:
    def __init__(self):
        """Initialize the library with an empty book list."""
        self._books = []

    def add_book(self, book):
        """Adds a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"{title} has been checked out.")
                return
        print(f"Sorry, '{title}' is either unavailable or does not exist in the library.")

    def return_book(self, title):
        """Returns a book to the library."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                print(f"{title} has been returned to the library.")
                return
        print(f"'{title}' does not exist in the library.")

    def list_available_books(self):
        """Lists all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books at the moment.")