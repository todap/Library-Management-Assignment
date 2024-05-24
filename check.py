from datetime import datetime
from book import BookManager
from user import UserManager
from storage import Storage

class LibraryManagementSystem:
    def __init__(self, books_file, users_file, checkouts_file):
        """
        Initialize the LibraryManagementSystem class.

        Args:
            books_file (str): Path to the file containing book data.
            users_file (str): Path to the file containing user data.
            checkouts_file (str): Path to the file containing checkout data.
        """
        self.storage = Storage(books_file, users_file, checkouts_file)
        self.book_manager = BookManager()
        self.user_manager = UserManager()
        self.load_data()

    def load_data(self):
        """
        Load data from storage into book_manager, user_manager, and checkouts.
        """
        self.book_manager.books = self.storage.load_books()
        self.user_manager.users = self.storage.load_users()
        self.checkouts = self.storage.load_checkouts()

    def save_data(self):
        """
        Save data from book_manager, user_manager, and checkouts into storage.
        """
        self.storage.save_books(self.book_manager.books)
        self.storage.save_users(self.user_manager.users)
        self.storage.save_checkouts(self.checkouts)

    # Book operations
    def add_book_flow(self):
        """
        Flow for adding a book.
        """
        title = input("Enter title: ")
        if not title:
            print("Title cannot be empty.")
            return
        if not isinstance(title, str):
            print("Title must be a string.")
            return
        author = input("Enter author: ")
        if not author:
            print("Author cannot be empty.")
            return
        if not isinstance(author, str):
            print("Author must be a string.")
            return
        isbn = input("Enter ISBN: ")
        if not isbn:
            print("ISBN cannot be empty.")
            return
        if not isbn.isalnum():
            print("ISBN must contain only alphanumeric characters.")
            return
        self.add_book(title, author, isbn)

    def add_book(self, title, author, isbn):
        """
        Add a book to the book_manager.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.
            isbn (str): ISBN of the book.
        """
        self.book_manager.add_book(title, author, isbn)
        self.save_data()
        print("Book added.")

    def list_books(self):
        """
        List all the books in the book_manager.
        """
        if not self.book_manager.books:
            print("No books.")
        self.book_manager.list_books()

    def search_book_flow(self):
        """
        Flow for searching books.
        """
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        self.search_books(title, author, isbn)
        results = self.search_books(title, author, isbn)
        if not results:
            print("No books found.")

    def search_books(self, title=None, author=None, isbn=None):
        """
        Search books in the book_manager based on title, author, and/or ISBN.

        Args:
            title (str, optional): Title of the book to search for.
            author (str, optional): Author of the book to search for.
            isbn (str, optional): ISBN of the book to search for.
        """
        results = self.book_manager.search_books(title, author, isbn)
        for book in results:
            print(book)

    def update_book_flow(self):
        """
        Flow for updating a book.
        """
        isbn = input("Enter ISBN of the book to update: ")
        if not isbn:
            print("ISBN cannot be empty.")
            return
        title = input("Enter new title: ")
        author = input("Enter new author: ")
        self.update_book(isbn, title, author)

    def update_book(self, isbn, title=None, author=None):
        """
        Update a book in the book_manager.

        Args:
            isbn (str): ISBN of the book to update.
            title (str, optional): New title of the book.
            author (str, optional): New author of the book.
        """
        self.book_manager.update_book(isbn, title, author)
        self.save_data()
        print("Book updated.")

    def delete_book_flow(self):
        """
        Flow for deleting a book.
        """
        isbn = input("Enter ISBN of the book to delete: ")
        self.delete_book(isbn)

    def delete_book(self, isbn):
        """
        Delete a book from the book_manager.

        Args:
            isbn (str): ISBN of the book to delete.
        """
        self.book_manager.delete_book(isbn)
        self.save_data()
        print("Book deleted.")

    # User operations
    def add_user_flow(self):
        """
        Flow for adding a user.
        """
        name = input("Enter user name: ")
        if not name:
            print("Name cannot be empty.")
            return
        if not isinstance(name, str):
            print("Name must be a string.")
            return
        user_id = input("Enter user ID: ")
        if not user_id:
            print("User ID cannot be empty.")
            return
        if not user_id.isalnum():
            print("User ID must contain only alphanumeric characters.")
            return
        self.add_user(name, user_id)

    def add_user(self, name, user_id):
        """
        Add a user to the user_manager.

        Args:
            name (str): Name of the user.
            user_id (str): ID of the user.
        """
        self.user_manager.add_user(name, user_id)
        self.save_data()
        print("User added.")

    def list_users(self):
        """
        List all the users in the user_manager.
        """
        if not self.user_manager.users:
            print("No users.")
        self.user_manager.list_users()

    def search_user_flow(self):
        """
        Flow for searching users.
        """
        name = input("Enter name: ")
        user_id = input("Enter user ID: ")
        self.search_users(name, user_id)
        results = self.search_users(name, user_id)
        if not results:
            print("No users found.")

    def search_users(self, name=None, user_id=None):
        """
        Search users in the user_manager based on name and/or user ID.

        Args:
            name (str, optional): Name of the user to search for.
            user_id (str, optional): ID of the user to search for.
        """
        results = self.user_manager.search_users(name, user_id)
        for user in results:
            print(user)

    def update_user_flow(self):
        """
        Flow for updating a user.
        """
        user_id = input("Enter user ID of the user to update: ")
        if not user_id:
            print("User ID cannot be empty.")
            return
        name = input("Enter new name: ")
        self.update_user(user_id, name)

    def update_user(self, user_id, name=None):
        """
        Update a user in the user_manager.

        Args:
            user_id (str): ID of the user to update.
            name (str, optional): New name of the user.
        """
        self.user_manager.update_user(user_id, name)
        self.save_data()
        print("User updated.")

    def delete_user_flow(self):
        """
        Flow for deleting a user.
        """
        user_id = input("Enter user ID of the user to delete: ")
        self.delete_user(user_id)

    def delete_user(self, user_id):
        """
        Delete a user from the user_manager.

        Args:
            user_id (str): ID of the user to delete.
        """
        self.user_manager.delete_user(user_id)
        self.save_data()
        print("User deleted.")

    # Checkout and check-in operations
    def checkout_book_flow(self):
        """
        Flow for checking out a book.
        """
        user_id = input("Enter user ID: ")
        if not user_id:
            print("User ID cannot be empty.")
            return
        if not user_id.isalnum():
            print("User ID must contain only alphanumeric characters.")
            return
        isbn = input("Enter ISBN of the book to checkout: ")
        if not isbn:
            print("ISBN cannot be empty.")
            return
        if not isbn.isalnum():
            print("ISBN must contain only alphanumeric characters.")
            return
        self.checkout_book(user_id, isbn)

    def checkout_book(self, user_id, isbn):
        """
        Checkout a book for a user.

        Args:
            user_id (str): ID of the user.
            isbn (str): ISBN of the book.
        """
        user = self.user_manager.get_user_by_id(user_id)
        book = self.book_manager.get_book_by_isbn(isbn)

        if user and book:
            user.check_out_book(book)
            checkout_entry = {
                'user_id': user_id,
                'isbn': isbn,
                'checkout_time': datetime.now().isoformat()
            }
            self.checkouts.append(checkout_entry)
            self.save_data()
            print(f"Book '{book.title}' checked out by '{user.name}'.")
        else:
            print("Invalid user ID or book ISBN.")

    def checkin_book_flow(self):
        """
        Flow for checking in a book.
        """
        user_id = input("Enter user ID: ")
        if not user_id:
            print("User ID cannot be empty.")
            return
        if not user_id.isalnum():
            print("User ID must contain only alphanumeric characters.")
            return
        isbn = input("Enter ISBN of the book to check-in: ")
        if not isbn:
            print("ISBN cannot be empty.")
            return
        if not isbn.isalnum():
            print("ISBN must contain only alphanumeric characters.")
            return
        self.checkin_book(user_id, isbn)

    def checkin_book(self, user_id, isbn):
        """
        Check in a book for a user.

        Args:
            user_id (str): ID of the user.
            isbn (str): ISBN of the book.
        """
        user = self.user_manager.get_user_by_id(user_id)
        book = self.book_manager.get_book_by_isbn(isbn)

        if user and book:
            user.check_in_book(book)
            for checkout in self.checkouts:
                if checkout['user_id'] == user_id and checkout['isbn'] == isbn:
                    self.checkouts.remove(checkout)
                    break
            self.save_data()
            print(f"Book '{book.title}' checked in by '{user.name}'.")
        else:
            print("Invalid user ID or book ISBN.")

     