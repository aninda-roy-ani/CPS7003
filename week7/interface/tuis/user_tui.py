from week7.services.user_service import UserService


class UserTUI:

    def __init__(self):
        self.user_service = UserService()

    def create_user(self):
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email: ")
        role_id = input("Enter Role ID: ")
        try:
            self.user_service.create_user(first_name, last_name, email, role_id)
            print(f"User created successfully")
        except Exception as e:
            print(f"Error creating user: {str(e)}")

    def retrieve_all_users(self):
        try:
            users = self.user_service.retrieve_all_users()
            for user in users:
                print(f"Name: {user.FirstName} {user.LastName}, Email: {user.Email}, RoleID: {user.UserID}")
        except Exception as e:
            print(f"Error retrieving users: {str(e)}")

    def retrieve_user_by_id(self):
        id = input("Enter User ID: ")
        try:
            user = self.user_service.retrieve_user(id)
            print(f"User ID: {user.UserID}, Name: {user.FirstName} {user.LastName}, Email: {user.Email}, RoleID: {user.RoleID}")
        except Exception as e:
            print(f"Error retrieving user with UserID: {str(e)}")

    def retrieve_user_by_email(self):
        email = input("Enter Email: ")
        try:
            user = self.user_service.retrieve_user_by_email(email)
            print(f"User ID: {user.UserID}, Name: {user.FirstName} {user.LastName}, Email: {user.Email}, RoleID: {user.RoleID}")
        except Exception as e:
            print(f"Error retrieving user with email: {str(e)}")

    def update_user(self):
        user_id = input("Enter User ID to update: ")
        first_name = input("Enter new First Name: ")
        last_name = input("Enter new Last Name: ")
        email = input("Enter new Email: ")
        role_id = input("Enter new Role ID: ")
        try:
            self.user_service.update_user(user_id, first_name, last_name, email, role_id)
            print(f"Updated User with UserID {user_id}")
        except Exception as e:
            print(f"Error updating user: {str(e)}")

    def delete_user(self):
        user_id = input("Enter User ID to delete: ")
        try:
            self.user_service.delete_user(user_id)
            print(f"Deleted User with UserID {user_id}")
        except Exception as e:
            print(f"Error deleting User: {str(e)}")

    def menu(self):
        while True:
            print("\nUser Management System")
            print("1. Add user")
            print("2. Update user")
            print("3. Delete user")
            print("4. Find All Users")
            print("5. Find User with ID")
            print("6. Find User with Email")
            print("7. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_user()
            elif choice == "2":
                self.update_user()
            elif choice == "3":
                self.delete_user()
            elif choice == "4":
                self.retrieve_all_users()
            elif choice == "5":
                self.retrieve_user_by_id()
            elif choice == "6":
                self.retrieve_user_by_email()
            elif choice == "7":
                print("Exiting User Management System.")
                break
            else:
                print("Invalid choice")


if __name__ == "__main__":
    user_tui = UserTUI()
    user_tui.menu()

