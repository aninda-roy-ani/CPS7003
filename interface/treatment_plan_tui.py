from datetime import datetime

from services.treatment_plan_service import TreatmentPlanService


class TreatmentPlanTUI:
    def __init__(self):
        self.treatment_plan_service = TreatmentPlanService()

    def create_treatment_plan(self):
        try:
            patient_id = int(input("Enter patient ID: "))
            diagnosis_id = int(input("Enter diagnosis ID: "))
            treatment_details = input("Enter treatment details: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")

            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')

            if self.treatment_plan_service.create_treatment_plan(patient_id, diagnosis_id, treatment_details, start_date, end_date):
                print("Treatment plan created successfully.")
            else:
                print("Failed to create treatment plan.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to create treatment plan: {str(e)}")

    def display_all_treatment_plans(self):
        try:
            plans = self.treatment_plan_service.retrieve_all_treatment_plans()
            print("All Treatment Plans:")
            for plan in plans:
                print(f"ID: {plan.treatment_id}, Patient ID: {plan.patient_id}, Diagnosis ID: {plan.diagnosis_id}, "
                      f"Details: {plan.treatment_details}, Start Date: {plan.start_date.strftime('%Y-%m-%d')}, "
                      f"End Date: {plan.end_date.strftime('%Y-%m-%d')}")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to retrieve treatment plans: {str(e)}")

    def find_treatment_plan_by_id(self):
        treatment_id = int(input("Enter treatment plan ID: "))
        try:
            plan = self.treatment_plan_service.retrieve_treatment_plan(treatment_id)
            if plan:
                print(f"ID: {plan.treatment_id}, Patient ID: {plan.patient_id}, Diagnosis ID: {plan.diagnosis_id}, "
                      f"Details: {plan.treatment_details}, Start Date: {plan.start_date.strftime('%Y-%m-%d')}, "
                      f"End Date: {plan.end_date.strftime('%Y-%m-%d')}")
            else:
                print(f"Treatment plan with ID {treatment_id} not found.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to retrieve treatment plan: {str(e)}")

    def update_treatment_plan(self):
        try:
            treatment_id = int(input("Enter treatment plan ID to update: "))
            patient_id = input("Enter new patient ID (leave blank to keep current): ")
            diagnosis_id = input("Enter new diagnosis ID (leave blank to keep current): ")
            treatment_details = input("Enter new treatment details (leave blank to keep current): ")
            start_date = input("Enter new start date (YYYY-MM-DD) (leave blank to keep current): ")
            end_date = input("Enter new end date (YYYY-MM-DD) (leave blank to keep current): ")

            patient_id = int(patient_id) if patient_id else None
            diagnosis_id = int(diagnosis_id) if diagnosis_id else None
            start_date = datetime.strptime(start_date, '%Y-%m-%d') if start_date else None
            end_date = datetime.strptime(end_date, '%Y-%m-%d') if end_date else None

            if self.treatment_plan_service.update_treatment_plan(treatment_id, patient_id, diagnosis_id, treatment_details, start_date, end_date):
                print("Treatment plan updated successfully.")
            else:
                print("Failed to update treatment plan.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to update treatment plan: {str(e)}")

    def delete_treatment_plan(self):
        treatment_id = int(input("Enter treatment plan ID to delete: "))
        try:
            if self.treatment_plan_service.delete_treatment_plan(treatment_id):
                print(f"Treatment plan with ID {treatment_id} deleted successfully.")
            else:
                print(f"Treatment plan with ID {treatment_id} not found.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to delete treatment plan: {str(e)}")

    def menu(self):
        while True:
            print("\nTreatment Plan Management System")
            print("1. Create Treatment Plan")
            print("2. Display All Treatment Plans")
            print("3. Find Treatment Plan by ID")
            print("4. Update Treatment Plan")
            print("5. Delete Treatment Plan")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_treatment_plan()
            elif choice == "2":
                self.display_all_treatment_plans()
            elif choice == "3":
                self.find_treatment_plan_by_id()
            elif choice == "4":
                self.update_treatment_plan()
            elif choice == "5":
                self.delete_treatment_plan()
            elif choice == "6":
                print("Exiting Treatment Plan Management System.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


# To use the TUI
if __name__ == "__main__":
    treatment_plan_tui = TreatmentPlanTUI()
    treatment_plan_tui.menu()
