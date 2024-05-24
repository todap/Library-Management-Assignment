import json
from pathlib import Path
from models import Book, User

class Storage:
    def __init__(self, books_file, users_file, checkouts_file):
        """
        Initialize the Storage class with file paths for books, users, and checkouts.

        Args:
            books_file (str): File path for storing books data.
            users_file (str): File path for storing users data.
            checkouts_file (str): File path for storing checkouts data.
        """
        self.books_file = Path(books_file)
        self.users_file = Path(users_file)
        self.checkouts_file = Path(checkouts_file)

    def load_books(self):
        """
        Load books data from the books file.

        Returns:
            list: List of Book objects loaded from the file.
        """
        try:
            if self.books_file.exists():
                with self.books_file.open('r') as f:
                    book_dicts = json.load(f)
                    return [Book(**book) for book in book_dicts]
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error loading books: {e}")
        return []

    def save_books(self, books):
        """
        Save books data to the books file.

        Args:
            books (list): List of Book objects to be saved.
        """
        book_dicts = [vars(book) for book in books]
        with self.books_file.open('w') as f:
            json.dump(book_dicts, f)

    def load_users(self):
        """
        Load users data from the users file.

        Returns:
            list: List of User objects loaded from the file.
        """
        if self.users_file.exists():
            with self.users_file.open('r') as f:
                user_dicts = json.load(f)
                users = []
                for user_dict in user_dicts:
                    user = User(user_dict['name'], user_dict['user_id'])
                    user.checked_out_books = [Book(**book) for book in user_dict['checked_out_books']]
                    users.append(user)
                return users
        return []

    def save_users(self, users):
        """
        Save users data to the users file.

        Args:
            users (list): List of User objects to be saved.
        """
        with self.users_file.open('w') as f:
            json.dump([user.to_dict() for user in users], f)

    def load_checkouts(self):
        """
        Load checkouts data from the checkouts file.

        Returns:
            list: List of checkouts data loaded from the file.
        """
        if self.checkouts_file.exists():
            with self.checkouts_file.open('r') as f:
                return json.load(f)
        return []

    def save_checkouts(self, checkouts):
        """
        Save checkouts data to the checkouts file.

        Args:
            checkouts (list): List of checkouts data to be saved.
        """
        with self.checkouts_file.open('w') as f:
            json.dump(checkouts, f)
