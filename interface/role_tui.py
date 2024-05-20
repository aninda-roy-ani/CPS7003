from services.role_service import RoleService


class RoleTUI:
    def __init__(self):
        self.role_service = RoleService()

    def create_role(self):
        role_name = input("Enter role name: ")
        try:
            if self.role_service.create_role(role_name):
                print(f"Role '{role_name}' created successfully.")
            else:
                print("Failed to create role.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to create role: {str(e)}")

    def display_all_roles(self):
        try:
            roles = self.role_service.retrieve_all_roles()
            if roles:
                print("All Roles:")
                for role in roles:
                    print(f"ID: {role.role_id}, Name: {role.role_name}")
            else:
                print("No roles found.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to retrieve roles: {str(e)}")

    def find_role_by_id(self):
        role_id = input("Enter role ID: ")
        try:
            role = self.role_service.retrieve_role(role_id)
            if role:
                print(f"ID: {role.role_id}, Name: {role.role_name}")
            else:
                print(f"Role with ID {role_id} not found.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to retrieve role: {str(e)}")

    def update_role(self):
        try:
            role_id = int(input("Enter role ID to update: "))
            new_role_name = input("Enter new role name: ")
            if self.role_service.update_role(role_id, new_role_name):
                print(f"Role ID {role_id} updated successfully.")
            else:
                print(f"Failed to update role with ID {role_id}.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to update role: {str(e)}")

    def delete_role(self):
        try:
            role_id = int(input("Enter role ID to delete: "))
            if self.role_service.delete_role(role_id):
                print(f"Role ID {role_id} deleted successfully.")
            else:
                print(f"Failed to delete role with ID {role_id}.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to delete role: {str(e)}")

    def menu(self):
        while True:
            print("\nRole Management System")
            print("1. Create Role")
            print("2. Display All Roles")
            print("3. Find Role by ID")
            print("4. Update Role")
            print("5. Delete Role")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_role()
            elif choice == "2":
                self.display_all_roles()
            elif choice == "3":
                self.find_role_by_id()
            elif choice == "4":
                self.update_role()
            elif choice == "5":
                self.delete_role()
            elif choice == "6":
                print("Exiting Role Management System.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


# To use the TUI
if __name__ == "__main__":
    role_tui = RoleTUI()
    role_tui.menu()
