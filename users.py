from typing import Optional, Dict
import uuid

class Users:
    AllUsers: Dict[str, "Users"] = {}

    def __init__(self, username: str, password: str, phone_number: Optional[str] = None):
        
        self.username = username
        self._password = password
        self.phone_number = phone_number
        self.id = uuid.uuid4() 
        self.AllUsers[username] = self 
    @classmethod
    def register(cls,username,password,phone_number:Optional[str]=None):
        while username in cls.AllUsers:
            username=input("the entred username is exist try another one please:\n")
        while len( password)<4:
            password=input("it should be 4 or more than 4 characters enter new newone:\n")
        cls.AllUsers[username]=cls(username, phone_number, password)
        return cls(username, phone_number, password)
        




