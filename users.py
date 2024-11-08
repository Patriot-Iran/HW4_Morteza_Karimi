from typing import Optional, Dict
import uuid

class Users:
    AllUsers: Dict[str, "Users"] = {}

    def __init__(self, username: str, password: str, phone_number: Optional[str] = None):
       
        while username in self.AllUsers:
            username=input("enter new user name")
        
        self.username = username
        self._password = password
        self.phone_number = phone_number
        self.id = uuid.uuid4()  

        
        self.AllUsers[username] = self

  


