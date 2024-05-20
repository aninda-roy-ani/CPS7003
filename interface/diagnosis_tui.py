from datetime import datetime

from services.diagnosis_service import DiagnosisService


class DiagnosisTUI:
    def __init__(self):
        self.diagnosis_service = DiagnosisService()

    def create_diagnosis_plan(self):
        patient_id = int(input("Enter patient ID: "))
        diagnosis_details = input("Enter diagnosis details: ")
        diagnosis_date = input("Enter diagnosis date (YYYY-MM-DD): ")
        result = input("Enter diagnosis result: ")
        try:
            diagnosis_date = datetime.strptime(diagnosis_date, '%Y-%m-%d')
            if self.diagnosis_service.create_diagnosis_plan(patient_id, diagnosis_details, diagnosis_date, result):
                print(f"Diagnosis plan for patient ID '{patient_id}' created successfully.")
            else:
                print("Failed to create diagnosis plan.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to create diagnosis plan: {str(e)}")

    def display_all_diagnosis_plans(self):
        try:
            diagnoses = self.diagnosis_service.retrieve_all_diagnosis_plans()
            print("All Diagnosis Plans:")
            for diagnosis in diagnoses:
                print(f"ID: {diagnosis.diagnosis_id}, Patient ID: {diagnosis.patient_id}, Diagnosis Date: {diagnosis.diagnosis_date.strftime('%Y-%m-%d')}, Details: {diagnosis.diagnosis_details}")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to retrieve diagnosis plans: {str(e)}")

    def find_diagnosis_by_id(self):
        diagnosis_id = int(input("Enter diagnosis ID: "))
        try:
            diagnosis = self.diagnosis_service.retrieve_diagnosis_plan(diagnosis_id)
            if diagnosis:
                print(f"ID: {diagnosis.diagnosis_id}, Patient ID: {diagnosis.patient_id}, Diagnosis Date: {diagnosis.diagnosis_date.strftime('%Y-%m-%d')}, Details: {diagnosis.diagnosis_details}")
            else:
                print(f"Diagnosis plan with ID {diagnosis_id} not found.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to retrieve diagnosis plan: {str(e)}")

    def update_diagnosis_plan(self):
        diagnosis_id = int(input("Enter diagnosis ID to update: "))
        patient_id = input("Enter new patient ID (leave blank to keep current): ")
        diagnosis_details = input("Enter new diagnosis details (leave blank to keep current): ")
        diagnosis_date = input("Enter new diagnosis date (YYYY-MM-DD) (leave blank to keep current): ")
        result = input("Enter new diagnosis result (leave blank to keep current): ")
        try:
            patient_id = int(patient_id) if patient_id else None
            diagnosis_date = datetime.strptime(diagnosis_date, '%Y-%m-%d') if diagnosis_date else None
            if self.diagnosis_service.update_diagnosis_plan(diagnosis_id, patient_id, diagnosis_details, diagnosis_date, result):
                print("Diagnosis plan updated successfully.")
            else:
                print("Failed to update diagnosis plan.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to update diagnosis plan: {str(e)}")

    def delete_diagnosis_plan(self):
        diagnosis_id = int(input("Enter diagnosis ID to delete: "))
        try:
            if self.diagnosis_service.delete_diagnosis_plan(diagnosis_id):
                print(f"Diagnosis plan with ID {diagnosis_id} deleted successfully.")
            else:
                print(f"Diagnosis plan with ID {diagnosis_id} not found.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to delete diagnosis plan: {str(e)}")

    def menu(self):
        while True:
            print("\nDiagnosis Management System")
            print("1. Create Diagnosis Plan")
            print("2. Display All Diagnosis Plans")
            print("3. Find Diagnosis by ID")
            print("4. Update Diagnosis Plan")
            print("5. Delete Diagnosis Plan")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_diagnosis_plan()
            elif choice == "2":
                self.display_all_diagnosis_plans()
            elif choice == "3":
                self.find_diagnosis_by_id()
            elif choice == "4":
                self.update_diagnosis_plan()
            elif choice == "5":
                self.delete_diagnosis_plan()
            elif choice == "6":
                print("Exiting Diagnosis Management System.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


# To use the TUI
if __name__ == "__main__":
    diagnosis_tui = DiagnosisTUI()
    diagnosis_tui.menu()
