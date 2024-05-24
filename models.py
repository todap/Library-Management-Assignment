class Book:
    """Represents a book with title, author, ISBN, and availability."""

    def __init__(self, title, author, isbn, available=True):
        """
        Initialize a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            available (bool): Indicates whether the book is available or not (default: True).
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __repr__(self):
        """Return a string representation of the Book object."""
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', available={self.available})"

    def check_out(self):
        """Check out the book."""
        self.available = False

    def check_in(self):
        """Check in the book."""
        self.available = True


class User: 
    '''Represents a user with a name, user_id, and a list of checked out books.'''
    def __init__(self, name, user_id):
        """
        Initialize a User object.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        self.name = name
        self.user_id = user_id
        self.checked_out_books = []

    def __repr__(self):
        """Return a string representation of the User object."""
        return f"User('{self.name}', '{self.user_id}')"

    def check_out_book(self, book):
        """
        Check out a book.

        Args:
            book (Book): The book to be checked out.

        Raises:
            TypeError: If the book is not an instance of Book.
            ValueError: If the book is not available.
        """
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if book.available:
            self.checked_out_books.append(book)
            book.check_out()
        else:
            raise ValueError(f"Book '{book.title}' is not available.")

    def check_in_book(self, book):
        """
        Check in a book.

        Args:
            book (Book): The book to be checked in.

        Raises:
            TypeError: If the book is not an instance of Book.
            ValueError: If the book is not checked out by the user.
        """
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if book in self.checked_out_books:
            self.checked_out_books.remove(book)
            book.check_in()
        else:
            raise ValueError(f"Book '{book.title}' is not checked out by you.")

    def to_dict(self):
        """
        Convert the User object to a dictionary.

        Returns:
            dict: A dictionary representation of the User object.
        """
        return {
            'name': self.name,
            'user_id': self.user_id,
            'checked_out_books': [vars(book) for book in self.checked_out_books]
        }
