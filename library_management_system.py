class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publication_year):
        if isbn in self.books:
            raise ValueError("A book with this ISBN already exists.")
        self.books[isbn] = Book(isbn, title, author, publication_year)

    def borrow_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not found.")
        book = self.books[isbn]
        if book.is_borrowed:
            raise ValueError("Book is currently borrowed.")
        book.is_borrowed = True

    def return_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not found.")
        book = self.books[isbn]
        if not book.is_borrowed:
            raise ValueError("Book was not borrowed.")
        book.is_borrowed = False

    def view_available_books(self):
        return [book for book in self.books.values() if not book.is_borrowed]
