from week7.services.role_service import RoleService


class RoleTUI:
    def __init__(self):
        self.role_service = RoleService()

    def create_role(self):
        role_name = input("Enter role name: ")
        try:
            new_role = self.role_service.create_role(role_name)
            print(f"Role '{new_role.RoleName}' created successfully with ID {new_role.RoleID}")
        except Exception as e:
            print(f"Failed to create role: {str(e)}")

    def display_all_roles(self):
        try:
            roles = self.role_service.retrieve_all_roles()
            print("All Roles:")
            for role in roles:
                print(f"ID: {role.RoleID}, Name: {role.RoleName}")
        except Exception as e:
            print(f"Failed to retrieve roles: {str(e)}")

    def find_role_by_id(self):
        role_id = input("Enter role id: ")
        try:
            role = self.role_service.retrieve_role(role_id)
            print(f"ID: {role.RoleID}, Name: {role.RoleName}")
        except Exception as e:
            print(f"Failed to retrieve role: {str(e)}")

    def update_role(self):
        role_id = int(input("Enter role ID to update: "))
        new_role_name = input("Enter new role name: ")
        try:
            updated_role = self.role_service.update_role(role_id, new_role_name)
            print(f"Role '{updated_role.RoleName}' updated successfully.")
        except Exception as e:
            print(f"Failed to update role: {str(e)}")

    def delete_role(self):
        role_id = int(input("Enter role ID to delete: "))
        try:
            if self.role_service.delete_role(role_id):
                print(f"Role with ID {role_id} deleted successfully.")
            else:
                print(f"Role with ID {role_id} not found.")
            print("Deleting role")
        except Exception as e:
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


if __name__ == "__main__":
    # Instantiate RoleTUI
    role_tui = RoleTUI()
    role_tui.menu()