from services.employee_service import EmployeeService


class EmployeeTUI:
    def __init__(self):
        self.employee_service = EmployeeService()

    def create_employee(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        role_id = int(input("Enter role ID: "))
        try:
            if self.employee_service.create_employee(first_name, last_name, role_id):
                print(f"Employee '{first_name} {last_name}' created successfully.")
            else:
                print("Failed to create employee.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to create employee: {str(e)}")

    def display_all_employees(self):
        try:
            employees = self.employee_service.retrieve_all_employees()
            print("All Employees:")
            for employee in employees:
                print(f"ID: {employee.employee_id}, Name: {employee.first_name} {employee.last_name}, Role ID: {employee.role_id}")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to retrieve employees: {str(e)}")

    def find_employee_by_id(self):
        employee_id = int(input("Enter employee ID: "))
        try:
            employee = self.employee_service.retrieve_employee(employee_id)
            if employee:
                print(f"ID: {employee.employee_id}, Name: {employee.first_name} {employee.last_name}, Role ID: {employee.role_id}")
            else:
                print(f"Employee with ID {employee_id} not found.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to retrieve employee: {str(e)}")

    def update_employee(self):
        employee_id = int(input("Enter employee ID to update: "))
        first_name = input("Enter new first name (leave blank to keep current): ")
        last_name = input("Enter new last name (leave blank to keep current): ")
        role_id = input("Enter new role ID (leave blank to keep current): ")
        role_id = int(role_id) if role_id else None
        try:
            if self.employee_service.update_employee(employee_id, first_name, last_name, role_id):
                print("Employee updated successfully.")
            else:
                print("Failed to update employee.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to update employee: {str(e)}")

    def delete_employee(self):
        employee_id = int(input("Enter employee ID to delete: "))
        try:
            if self.employee_service.delete_employee(employee_id):
                print(f"Employee with ID {employee_id} deleted successfully.")
            else:
                print(f"Employee with ID {employee_id} not found.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to delete employee: {str(e)}")

    def menu(self):
        while True:
            print("\nEmployee Management System")
            print("1. Create Employee")
            print("2. Display All Employees")
            print("3. Find Employee by ID")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_employee()
            elif choice == "2":
                self.display_all_employees()
            elif choice == "3":
                self.find_employee_by_id()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Exiting Employee Management System.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


# To use the TUI
if __name__ == "__main__":
    employee_tui = EmployeeTUI()
    employee_tui.menu()
