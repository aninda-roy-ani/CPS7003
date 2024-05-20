from datetime import datetime
from services.medical_history_service import MedicalHistoryService


class MedicalHistoryTUI:
    def __init__(self):
        self.medical_history_service = MedicalHistoryService()

    def create_medical_history(self):
        patient_id = int(input("Enter patient ID: "))
        admission_date = input("Enter admission date (YYYY-MM-DD): ")
        discharge_date = input("Enter discharge date (YYYY-MM-DD): ")
        diagnosis = input("Enter diagnosis: ")
        medical_notes = input("Enter medical notes: ")
        try:
            admission_date = datetime.strptime(admission_date, '%Y-%m-%d')
            discharge_date = datetime.strptime(discharge_date, '%Y-%m-%d')
            if self.medical_history_service.create_medical_history(patient_id, admission_date, discharge_date, diagnosis, medical_notes):
                print(f"Medical history for patient ID '{patient_id}' created successfully.")
            else:
                print("Failed to create medical history.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to create medical history: {str(e)}")

    def display_all_medical_histories(self):
        try:
            histories = self.medical_history_service.retrieve_all_medical_histories()
            print("All Medical Histories:")
            for history in histories:
                print(f"ID: {history.history_id}, Patient ID: {history.patient_id}, Admission Date: {history.admission_date.strftime('%Y-%m-%d')}, Discharge Date: {history.discharge_date.strftime('%Y-%m-%d')}, Diagnosis: {history.diagnosis}, Medical Notes: {history.medical_notes}")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to retrieve medical histories: {str(e)}")

    def find_medical_history_by_id(self):
        history_id = int(input("Enter medical history ID: "))
        try:
            history = self.medical_history_service.retrieve_medical_history(history_id)
            if history:
                print(f"ID: {history.history_id}, Patient ID: {history.patient_id}, Admission Date: {history.admission_date.strftime('%Y-%m-%d')}, Discharge Date: {history.discharge_date.strftime('%Y-%m-%d')}, Diagnosis: {history.diagnosis}, Medical Notes: {history.medical_notes}")
            else:
                print(f"Medical history with ID {history_id} not found.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to retrieve medical history: {str(e)}")

    def update_medical_history(self):
        history_id = int(input("Enter medical history ID to update: "))
        patient_id = input("Enter new patient ID (leave blank to keep current): ")
        admission_date = input("Enter new admission date (YYYY-MM-DD) (leave blank to keep current): ")
        discharge_date = input("Enter new discharge date (YYYY-MM-DD) (leave blank to keep current): ")
        diagnosis = input("Enter new diagnosis (leave blank to keep current): ")
        medical_notes = input("Enter new medical notes (leave blank to keep current): ")
        try:
            patient_id = int(patient_id) if patient_id else None
            admission_date = datetime.strptime(admission_date, '%Y-%m-%d') if admission_date else None
            discharge_date = datetime.strptime(discharge_date, '%Y-%m-%d') if discharge_date else None
            if self.medical_history_service.update_medical_history(history_id, patient_id, admission_date, discharge_date, diagnosis, medical_notes):
                print("Medical history updated successfully.")
            else:
                print("Failed to update medical history.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to update medical history: {str(e)}")

    def delete_medical_history(self):
        history_id = int(input("Enter medical history ID to delete: "))
        try:
            if self.medical_history_service.delete_medical_history(history_id):
                print(f"Medical history with ID {history_id} deleted successfully.")
            else:
                print(f"Medical history with ID {history_id} not found.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to delete medical history: {str(e)}")

    def menu(self):
        while True:
            print("\nMedical History Management System")
            print("1. Create Medical History")
            print("2. Display All Medical Histories")
            print("3. Find Medical History by ID")
            print("4. Update Medical History")
            print("5. Delete Medical History")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_medical_history()
            elif choice == "2":
                self.display_all_medical_histories()
            elif choice == "3":
                self.find_medical_history_by_id()
            elif choice == "4":
                self.update_medical_history()
            elif choice == "5":
                self.delete_medical_history()
            elif choice == "6":
                print("Exiting Medical History Management System.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


# To use the TUI
if __name__ == "__main__":
    medical_history_tui = MedicalHistoryTUI()
    medical_history_tui.menu()
