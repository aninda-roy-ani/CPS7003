from week5.services.role_service import RoleService

class RoleTUI:
    def __init__(self, session):
        self.role_service = RoleService(session)

    def create_role(self):
        role_name = input("Enter role name: ")
        creator_id = int(input("Enter creator ID: "))
        try:
            new_role = self.role_service.create_role(role_name, creator_id)
            print(f"Role '{new_role.RoleName}' created successfully with ID {new_role.RoleID}")
        except Exception as e:
            print(f"Failed to create role: {str(e)}")

    def display_all_roles(self):
        try:
            roles = self.role_service.get_all_roles()
            print("All Roles:")
            for role in roles:
                print(f"ID: {role.RoleID}, Name: {role.RoleName}")
        except Exception as e:
            print(f"Failed to retrieve roles: {str(e)}")

    def update_role(self):
        role_id = int(input("Enter role ID to update: "))
        new_role_name = input("Enter new role name: ")
        updater_id = int(input("Enter updater ID: "))
        try:
            updated_role = self.role_service.update_role(role_id, new_role_name, updater_id)
            print(f"Role '{updated_role.RoleName}' updated successfully.")
        except Exception as e:
            print(f"Failed to update role: {str(e)}")

    def delete_role(self):
        role_id = int(input("Enter role ID to delete: "))
        deleter_id = int(input("Enter deleter ID: "))
        try:
            if self.role_service.delete_role(role_id, deleter_id):
                print(f"Role with ID {role_id} deleted successfully.")
            else:
                print(f"Role with ID {role_id} not found.")
        except Exception as e:
            print(f"Failed to delete role: {str(e)}")

    def menu(self):
        while True:
            print("\nRole Management System")
            print("1. Create Role")
            print("2. Display All Roles")
            print("3. Update Role")
            print("4. Delete Role")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_role()
            elif choice == "2":
                self.display_all_roles()
            elif choice == "3":
                self.update_role()
            elif choice == "4":
                self.delete_role()
            elif choice == "5":
                print("Exiting Role Management System.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")