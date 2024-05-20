from services.treatment_team_assignment_service import TreatmentTeamAssignmentService


class TreatmentTeamAssignmentTUI:
    def __init__(self):
        self.assignment_service = TreatmentTeamAssignmentService()

    def create_assignment(self):
        try:
            patient_id = int(input("Enter patient ID: "))
            treatment_id = int(input("Enter treatment ID: "))
            employee_id = int(input("Enter employee ID: "))
            if self.assignment_service.create_assignment(patient_id, treatment_id, employee_id):
                print("Assignment created successfully.")
            else:
                print("Failed to create assignment.")
        except ValueError:
            print("Invalid input! Please enter valid IDs.")

    def retrieve_assignment(self):
        try:
            assignment_id = int(input("Enter assignment ID: "))
            assignment = self.assignment_service.retrieve_assignment(assignment_id)
            if assignment:
                print(f"Assignment ID: {assignment.assignment_id}, Patient ID: {assignment.patient_id}, "
                      f"Treatment ID: {assignment.treatment_id}, Employee ID: {assignment.employee_id}")
            else:
                print(f"Assignment with ID {assignment_id} not found.")
        except ValueError:
            print("Invalid input! Please enter a valid ID.")

    def retrieve_all_assignments(self):
        assignments = self.assignment_service.retrieve_all_assignments()
        if assignments:
            print("All Assignments:")
            for assignment in assignments:
                print(f"Assignment ID: {assignment.assignment_id}, Patient ID: {assignment.patient_id}, "
                      f"Treatment ID: {assignment.treatment_id}, Employee ID: {assignment.employee_id}")
        else:
            print("No assignments found.")

    def update_assignment(self):
        try:
            assignment_id = int(input("Enter assignment ID to update: "))
            patient_id = int(input("Enter new patient ID (press Enter to keep current): ") or "0")
            treatment_id = int(input("Enter new treatment ID (press Enter to keep current): ") or "0")
            employee_id = int(input("Enter new employee ID (press Enter to keep current): ") or "0")
            if self.assignment_service.update_assignment(assignment_id, patient_id, treatment_id, employee_id):
                print("Assignment updated successfully.")
            else:
                print("Failed to update assignment.")
        except ValueError:
            print("Invalid input! Please enter valid IDs.")

    def delete_assignment(self):
        try:
            assignment_id = int(input("Enter assignment ID to delete: "))
            if self.assignment_service.delete_assignment(assignment_id):
                print("Assignment deleted successfully.")
            else:
                print(f"Assignment with ID {assignment_id} not found.")
        except ValueError:
            print("Invalid input! Please enter a valid ID.")

    def menu(self):
        while True:
            print("\nTreatment Team Assignment Management System")
            print("1. Create Assignment")
            print("2. Retrieve Assignment")
            print("3. Retrieve All Assignments")
            print("4. Update Assignment")
            print("5. Delete Assignment")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_assignment()
            elif choice == "2":
                self.retrieve_assignment()
            elif choice == "3":
                self.retrieve_all_assignments()
            elif choice == "4":
                self.update_assignment()
            elif choice == "5":
                self.delete_assignment()
            elif choice == "6":
                print("Exiting Treatment Team Assignment Management System.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


# To use the TUI
if __name__ == "__main__":
    assignment_tui = TreatmentTeamAssignmentTUI()
    assignment_tui.menu()
