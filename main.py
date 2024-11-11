import getpass
from users import User

def main():
    while True:
        print("\nMenu:\n0 - Exit\n1 - Register\n2 - Login")
        choice = input("Select an option: ")

        if choice == "0":
            print("Exiting program.")
            break

        elif choice == "1":
            username = input("Enter username: ")
            phone = input("Enter phone number (optional): ")
            password = getpass.getpass("Enter password: ")

            if User.is_valid_password(password):
                try:
                    user = User(username=username, phone_number=phone, password=password)
                    print(f"User '{username}' created successfully.")
                except ValueError as e:
                    print(e)
            else:
                print("Password is invalid. It must be at least 4 characters long.")

        elif choice == "2":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            user = User.get_user(username)

            if user and user.check_password(password):
                print("Login successful!")
                while True:
                    print("\n1 - View Info\n2 - Edit Info\n3 - Change Password\n4 - Logout")
                    user_choice = input("Select an option: ")

                    if user_choice == "1":
                        print(user)

                    elif user_choice == "2":
                        new_username = input("Enter new username: ")
                        new_phone = input("Enter new phone number: ")
                        if new_username and new_username != user.username:
                            if new_username in User._users:
                                print("Error: Username already taken.")
                            else:
                                del User._users[user.username]
                                user.username = new_username
                                User._users[new_username] = user
                        user.phone_number = new_phone or None
                        print("Information updated.")

                    elif user_choice == "3":
                        old_password = getpass.getpass("Enter current password: ")
                        new_password = getpass.getpass("Enter new password: ")
                        confirm_password = getpass.getpass("Confirm new password: ")
                        if user.update_password(old_password, new_password, confirm_password):
                            print("Password updated successfully.")
                        else:
                            print("Password update failed.")

                    elif user_choice == "4":
                        print("Logged out.")
                        break
                    else:
                        print("Invalid option.")
            else:
                print("Error: Invalid username or password.")

if __name__ == "__main__":
    main()
