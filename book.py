from models import Book

class BookManager:
    def __init__(self):
        """
        Initialize the BookManager class.
        """
        self.books = []

    def add_book(self, title, author, isbn):
        """
        Add a new book to the book list.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        book = Book(title, author, isbn)
        self.books.append(book)

    def update_book(self, isbn, title=None, author=None):
        """
        Update the details of a book.

        Args:
            isbn (str): The ISBN of the book to be updated.
            title (str, optional): The new title of the book. Defaults to None.
            author (str, optional): The new author of the book. Defaults to None.
        """
        book = self.get_book_by_isbn(isbn)
        if book:
            if title:
                if not isinstance(title, str):
                    print("Title must be a string.")
                    return
                book.title = title
            if author:
                if not isinstance(author, str):
                    print("Author must be a string.")
                    return
                book.author = author

    def delete_book(self, isbn):
        """
        Delete a book from the book list.

        Args:
            isbn (str): The ISBN of the book to be deleted.
        """
        book = self.get_book_by_isbn(isbn)
        if book:
            self.books.remove(book)

    def list_books(self):
        """
        List all the books in the book list.
        """
        for book in self.books:
            print(book)

    def search_books(self, title=None, author=None, isbn=None):
        """
        Search for books based on title, author, and/or ISBN.

        Args:
            title (str, optional): The title of the book to search for. Defaults to None.
            author (str, optional): The author of the book to search for. Defaults to None.
            isbn (str, optional): The ISBN of the book to search for. Defaults to None.

        Returns:
            list: A list of books that match the search criteria.
        """
        results = []
        for book in self.books:
            if (not title or title.lower() in book.title.lower()) and \
               (not author or author.lower() in book.author.lower()) and \
               (not isbn or isbn == book.isbn):
                results.append(book)
        return results

    def get_book_by_isbn(self, isbn):
        """
        Get a book object based on its ISBN.

        Args:
            isbn (str): The ISBN of the book to retrieve.

        Returns:
            Book: The book object with the specified ISBN, or None if not found.
        """
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
