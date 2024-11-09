from typing import Optional, Dict
import uuid
import hashlib

class Users:
    AllUsers: Dict[str, "Users"] = {}

    def __init__(self, username: str, password: str, phone_number: Optional[str] = None):
        """
    A class to represent and manage user accounts within a system.
    
    Attributes:
        AllUsers (Dict[str, "Users"]): A dictionary storing all registered users,
                                       with usernames as keys and user objects as values.
    
    Methods:
        __init__(username: str, password: str, phone_number: Optional[str] = None):
            Initializes a new user with a username, hashed password, and optional phone number,
            and assigns a unique user ID.
        """
        self.username = username
        self._password = self._hash_password(password)
        self.phone_number = phone_number
        self.id = uuid.uuid4()
        self.AllUsers[username] = self

    @staticmethod
    def _hash_password(password: str) -> str:
        """
        Hashes a password using SHA-256.
        
        Args:
            password (str): The password to hash.
        
        Returns:
            str: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    @classmethod
    def register(cls, username: str, password: str, phone_number: Optional[str] = None) -> "Users":
        """
        Registers a new user with a unique username.
        
        Args:
            username (str): The desired username.
            password (str): The desired password.
            phone_number (Optional[str]): The user's phone number.
        
        Returns:
            Users: The created user instance.
        """
        while username in cls.AllUsers:
            username = input("The entered username exists. Try another one, please:\n")
        
        while len(password) < 4:
            password = input("Password should be 4 or more characters. Enter a new one:\n")
            
        return cls(username, password, phone_number)

    @classmethod
    def update_user(cls, username: str, new_username: str, phone_number: Optional[str]):
        """
        Updates username and phone number of an existing user.
        
        Args:
            username (str): The current username.
            new_username (str): The new username.
            phone_number (Optional[str]): The new phone number.
        """
        user = cls.AllUsers[username]
        if new_username and new_username != username:
            cls.AllUsers.pop(username)
            user.username = new_username
            cls.AllUsers[new_username] = user
        if phone_number is not None:
            user.phone_number = phone_number
            
    @classmethod
    def change_password(cls, username: str, old_password: str, new_password: str) -> bool:
        """
        Changes the password for a user.
        
        Args:
            username (str): The username of the user.
            old_password (str): The old password.
            new_password (str): The new password.
        
        Returns:
            bool: True if the password was changed successfully, False otherwise.
        """
        user = cls.AllUsers[username]
        if user._password == cls._hash_password(old_password):
            user._password = cls._hash_password(new_password)
            return True
        return False

    def __str__(self) -> str:
        """
        String representation of the user.
        
        Returns:
            str: A summary of the user information.
        """
        return f"Username: {self.username}, Phone Number: {self.phone_number}, ID: {self.id}"
