import uuid
import hashlib
from typing import Optional, Dict, Union

class User:
    _users: Dict[str, 'User'] = {}  # دیکشنری برای نگهداری کاربران

    def __init__(self, username: str, phone_number: Optional[str] = None, password: str = ""):
        if username in User._users:
            raise ValueError("Username already taken.")
        self.id: str = str(uuid.uuid4())
        self.username: str = username
        self.phone_number: Optional[str] = phone_number
        self._password: str = self._hash_password(password)  # رمزگذاری گذرواژه
        User._users[username] = self

    @staticmethod
    def _hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def is_valid_password(password: str) -> bool:
        return len(password) >= 4

    def check_password(self, password: str) -> bool:
        return self._password == self._hash_password(password)

    def __str__(self) -> str:
        return f"ID: {self.id}\nUsername: {self.username}\nPhone: {self.phone_number}"

    @classmethod
    def get_user(cls, username: str) -> Union['User', None]:
        return cls._users.get(username)

    def update_password(self, old_password: str, new_password: str, confirm_password: str) -> bool:
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
