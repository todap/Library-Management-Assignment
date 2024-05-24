from models import User

class UserManager:
    def __init__(self):
        """
        Initialize the UserManager class.
        """
        self.users = []

    def add_user(self, name, user_id):
        """
        Add a new user to the user list.

        Args:
            name (str): The name of the user.
            user_id (int): The ID of the user.
        """
        user = User(name, user_id)
        self.users.append(user)

    def update_user(self, user_id, name=None):
        """
        Update the name of a user with the given user ID.

        Args:
            user_id (int): The ID of the user to update.
            name (str, optional): The new name for the user. Defaults to None.
        """
        user = self.get_user_by_id(user_id)
        if user:
            if name:
                if not isinstance(name, str):
                    print("Name must be a string.")
                    return
                user.name = name

    def delete_user(self, user_id):
        """
        Delete a user with the given user ID.

        Args:
            user_id (int): The ID of the user to delete.
        """
        user = self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)

    def list_users(self):
        """
        Print the details of all users in the user list.
        """
        for user in self.users:
            print(user)

    def search_users(self, name=None, user_id=None):
        """
        Search for users based on name and/or user ID.

        Args:
            name (str, optional): The name to search for. Defaults to None.
            user_id (int, optional): The user ID to search for. Defaults to None.

        Returns:
            list: A list of users matching the search criteria.
        """
        results = []
        for user in self.users:
            if (not name or name.lower() in user.name.lower()) and \
               (not user_id or user_id == user.user_id):
                results.append(user)
        return results

    def get_user_by_id(self, user_id):
        """
        Get a user by their user ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            User: The user object with the specified user ID, or None if not found.
        """
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
