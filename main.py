import getpass
from users import Users

def main():
    while True:
        print("Welcome to the User Management System")
        print("1. Register a new user")
        print("2. Login")
        print("0. Exit")
        
        choice = input("Please enter your choice: ")
        
        if choice == "0":
            print("Exiting program...")
            break
        elif choice == "1":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            
            phone_number = input("Enter phone number (leave blank if not provided): ")
            Users.register(username, password, phone_number)
            print(f"User {username} registered successfully!")
        elif choice == "2":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            if username in Users.AllUsers and Users.AllUsers[username]._password == Users._hash_password(password):
                print(f"Login successful! Welcome {username}.")
                while True:
                    print("1. Show user info")
                    print("2. Edit user info")
                    print("3. Change password")
                    print("4. Logout")
                    
                    user_choice = input("Please enter your choice: ")
                    
                    if user_choice == "1":
                        print(Users.AllUsers[username])
                    elif user_choice == "2":
                        new_username = input("Enter new username (leave blank if not changing): ")
                        new_phone_number = input("Enter new phone number (leave blank if not changing): ")
                        if new_username == "":
                            new_username = username
                        Users.update_user(username, new_username, new_phone_number)
                        print("User info updated successfully!")
                    elif user_choice == "3":
                        old_password = getpass.getpass("Enter your old password: ")
                        new_password = getpass.getpass("Enter your new password: ")
                       
                        confirm_password = getpass.getpass("Confirm your new password: ")
                        if new_password == confirm_password: 
                            Users.change_password(username, old_password, new_password)
                            print("Password changed successfully!")
                        else:
                            print("Error: Password change failed.")
                    elif user_choice == "4":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid username or password.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
