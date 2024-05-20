from datetime import datetime
from services.patient_service import PatientService


class PatientTUI:
    def __init__(self):
        self.patient_service = PatientService()

    def create_patient(self):
        patient_name = input("Enter patient name: ")
        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
        gender = input("Enter gender: ")
        contact_no = input("Enter contact number: ")
        address = input("Enter address: ")
        try:
            date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')
            if self.patient_service.create_patient(patient_name, date_of_birth, gender, contact_no, address):
                print(f"Patient '{patient_name}' created successfully.")
            else:
                print("Failed to create patient.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to create patient: {str(e)}")

    def display_all_patients(self):
        try:
            patients = self.patient_service.retrieve_all_patients()
            print("All Patients:")
            for patient in patients:
                print(f"ID: {patient.patient_id}, Name: {patient.patient_name}, DOB: {patient.date_of_birth.strftime('%Y-%m-%d')}, Gender: {patient.gender}, Contact: {patient.contact_no}, Address: {patient.address}")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to retrieve patients: {str(e)}")

    def find_patient_by_id(self):
        patient_id = int(input("Enter patient ID: "))
        try:
            patient = self.patient_service.retrieve_patient(patient_id)
            if patient:
                print(f"ID: {patient.patient_id}, Name: {patient.patient_name}, DOB: {patient.date_of_birth.strftime('%Y-%m-%d')}, Gender: {patient.gender}, Contact: {patient.contact_no}, Address: {patient.address}")
            else:
                print(f"Patient with ID {patient_id} not found.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to retrieve patient: {str(e)}")

    def update_patient(self):
        patient_id = int(input("Enter patient ID to update: "))
        patient_name = input("Enter new patient name (leave blank to keep current): ")
        date_of_birth = input("Enter new date of birth (YYYY-MM-DD) (leave blank to keep current): ")
        gender = input("Enter new gender (leave blank to keep current): ")
        contact_no = input("Enter new contact number (leave blank to keep current): ")
        address = input("Enter new address (leave blank to keep current): ")
        try:
            date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d') if date_of_birth else None
            if self.patient_service.update_patient(patient_id, patient_name, date_of_birth, gender, contact_no, address):
                print("Patient updated successfully.")
            else:
                print("Failed to update patient.")
        except Exception as e:
            print(f"Failed to update patient: {str(e)}")

    def delete_patient(self):
        patient_id = int(input("Enter patient ID to delete: "))
        try:
            if self.patient_service.delete_patient(patient_id):
                print(f"Patient with ID {patient_id} deleted successfully.")
            else:
                print(f"Patient with ID {patient_id} not found.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to delete patient: {str(e)}")

    def display_patient_diagnostic_details(self):
        patient_id = int(input("Enter patient ID to retrieve diagnostic details: "))
        try:
            details = self.patient_service.retrieve_patient_diagnostic_details(patient_id)
            if details:
                patient_info = details["patient_info"]
                print(f"Patient Info: ID: {patient_info['patient_id']}, Name: {patient_info['patient_name']}, DOB: {patient_info['date_of_birth']}, Gender: {patient_info['gender']}, Contact: {patient_info['contact_no']}, Address: {patient_info['address']}")
                print("Diagnosis:")
                for diag in details["diagnosis"]:
                    print(f"  Diagnosis ID: {diag['diagnosis_id']}, Details: {diag['diagnosis_details']}, Date: {diag['diagnosis_date']}, Result: {diag['result']}")
                    print("  Treatment Plans:")
                    for tp in diag["treatment_plans"]:
                        print(f"    Treatment ID: {tp['treatment_id']}, Details: {tp['treatment_details']}, Start Date: {tp['start_date']}, End Date: {tp['end_date']}")
                        print("    Assigned Teams:")
                        for team in tp["assigned_teams"]:
                            print(f"      Name: {team['name']}, Role: {team['role']}")
            else:
                print(f"Failed to retrieve diagnostic details for patient ID {patient_id}.")
        except Exception as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                print("Invalid or empty input!")
            else:
                print(f"Failed to retrieve diagnostic details: {str(e)}")

    def menu(self):
        while True:
            print("\nPatient Management System")
            print("1. Create Patient")
            print("2. Display All Patients")
            print("3. Find Patient by ID")
            print("4. Update Patient")
            print("5. Delete Patient")
            print("6. Display Patient Diagnostic Details")
            print("7. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_patient()
            elif choice == "2":
                self.display_all_patients()
            elif choice == "3":
                self.find_patient_by_id()
            elif choice == "4":
                self.update_patient()
            elif choice == "5":
                self.delete_patient()
            elif choice == "6":
                self.display_patient_diagnostic_details()
            elif choice == "7":
                print("Exiting Patient Management System.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


# To use the TUI
if __name__ == "__main__":
    patient_tui = PatientTUI()
    patient_tui.menu()
