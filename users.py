import uuid
import hashlib
from typing import Optional, Dict, Union

class User:
    """
    A class to represent a user with basic authentication and management features.

    Attributes:
    id (str): Unique identifier for the user.
    username (str): The username of the user.
    phone_number (Optional[str]): The phone number of the user (optional).
    _password (str): The hashed password of the user (private).
    """

    _users: Dict[str, 'User'] = {}  # Dictionary to store users by their username

    def __init__(self, username: str, phone_number: Optional[str] = None, password: str = ""):
        """
        Initializes a new user and adds it to the user dictionary.

        Args:
        username (str): The username of the user.
        phone_number (Optional[str]): The phone number of the user (optional).
        password (str): The password of the user.
        
        Raises:
        ValueError: If the username is already taken.
        """
        if username in User._users:
            raise ValueError("Username already taken.")
        self.id: str = str(uuid.uuid4())  # Unique user ID
        self.username: str = username
        self.phone_number: Optional[str] = phone_number
        self._password: str = self._hash_password(password)  # Store hashed password
        User._users[username] = self  # Add user to the dictionary

    @staticmethod
    def _hash_password(password: str) -> str:
        """
        Hashes the password using SHA-256.

        Args:
        password (str): The password to be hashed.

        Returns:
        str: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def is_valid_password(password: str) -> bool:
        """
        Checks if the provided password meets the minimum length requirement.

        Args:
        password (str): The password to be validated.

        Returns:
        bool: True if the password is valid (at least 4 characters), False otherwise.
        """
        return len(password) >= 4

    def check_password(self, password: str) -> bool:
        """
        Checks if the provided password matches the stored hashed password.

        Args:
        password (str): The password to be checked.

        Returns:
        bool: True if the password matches the stored password, False otherwise.
        """
        return self._password == self._hash_password(password)

    def __str__(self) -> str:
        """
        Returns a string representation of the user's basic information (excluding the password).

        Returns:
        str: A formatted string displaying the user's ID, username, and phone number.
        """
        return f"ID: {self.id}\nUsername: {self.username}\nPhone: {self.phone_number}"

    @classmethod
    def get_user(cls, username: str) -> object | None:
        """
        Retrieves a user by their username.

        Args:
        username (str): The username of the user to retrieve.

        Returns:
        object | None: The `User` object if the username exists, or `None` if the user is not found.
        """
        return cls._users.get(username)

    def update_password(self, old_password: str, new_password: str, confirm_password: str) -> bool:
        """
        Updates the user's password after validating the old password and ensuring the new password meets the requirements.

        Args:
        old_password (str): The user's current password.
        new_password (str): The new password to set.
        confirm_password (str): Confirmation of the new password.

        Returns:
        bool: True if the password was successfully updated, False otherwise.
        """
        if not self.check_password(old_password):
            print("Error: Current password is incorrect.")
            return False
        if new_password != confirm_password:
            print("Error: New passwords do not match.")
            return False
        if not self.is_valid_password(new_password):
            print("Error: New password is invalid.")
            return False
        self._password = self._hash_password(new_password)
        return True
