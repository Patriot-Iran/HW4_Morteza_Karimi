import getpass
from users import Users

def main():
    """
    Main function to run the User Management System. Provides options to register, login,
    and access user account management features.
    """
    while True:
        # Display main menu options
        print("Welcome to the User Management System")
        print("1. Register a new user")
        print("2. Login")
        print("0. Exit")
        
        # Get user's choice for main menu
        choice = input("Please enter your choice: ")
        
        if choice == "0":
            # Exit program
            print("Exiting program...")
            break
        elif choice == "1":
            # Register a new user
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            phone_number = input("Enter phone number (leave blank if not provided): ")
            
            # Register the user with optional phone number
            Users.register(username, password, phone_number)
            print(f"User {username} registered successfully!")
        elif choice == "2":
            # User login process
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            
            # Check if username exists and password matches
            if username in Users.AllUsers and Users.AllUsers[username]._password == Users._hash_password(password):
                print(f"Login successful! Welcome {username}.")
                
                # Logged-in user options
                while True:
                    print("1. Show user info")
                    print("2. Edit user info")
                    print("3. Change password")
                    print("4. Logout")
                    
                    # Get user choice for account management options
                    user_choice = input("Please enter your choice: ")
                    
                    if user_choice == "1":
                        # Display user information
                        print(Users.AllUsers[username])
                    elif user_choice == "2":
                        # Edit user information
                        new_username = input("Enter new username (leave blank if not changing): ")
                        new_phone_number = input("Enter new phone number (leave blank if not changing): ")
                        if new_username == "":
                            new_username = username
                        Users.update_user(username, new_username, new_phone_number)
                        print("User info updated successfully!")
                    elif user_choice == "3":
                        # Change user password
                        old_password = getpass.getpass("Enter your old password: ")
                        new_password = getpass.getpass("Enter your new password: ")
                        confirm_password = getpass.getpass("Confirm your new password: ")
                        
                        # Check if new password and confirmation match
                        if new_password == confirm_password:
                            Users.change_password(username, old_password, new_password)
                            print("Password changed successfully!")
                        else:
                            print("Error: Password change failed.")
                    elif user_choice == "4":
                        # Logout from account management
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                # Handle invalid login credentials
                print("Invalid username or password.")
        else:
            # Handle invalid main menu choice
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
