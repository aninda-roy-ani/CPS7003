from services.noSql_database_service import DiagnosisReportService


class DiagnosisReportTUI:
    def __init__(self):
        self.service = DiagnosisReportService()

    def menu(self):
        pending = self.service.check_pending_reports()
        ready = self.service.check_available_reports()
        while True:
            print("\nPatients' Diagnosis Report Management")
            print("1. Check Pending Diagnosis Patients")
            print("2. Save New Diagnosis")
            print("3. Check Complete Diagnosis Patients")
            print("4. Get Diagnosis Report")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("Pending Diagnosis Patients:",pending)
            elif choice == 2:
                if len(pending) == 0:
                    print("No Pending Diagnosis Report to save!")
                else:
                    print("Enter Patient ID from",pending)
                    patient_id = input()
                    self.service.save_new_report(patient_id)
                    print("Saved successfully.")
            elif choice == 3:
                print("Available Reports of the Patients:",ready)
            elif choice == 4:
                if len(ready) == 0:
                    print("No Diagnosis Report to print!")
                else:
                    print("Enter Patient ID from", ready)
                    patient_id = input()
                    self.service.print_diagnosis_report(patient_id)
            elif choice == 5:
                print("Exiting Diagnosis Report Management")
                break
            else:
                print("Invalid or empty input!")


if __name__ == "__main__":
    diagnosis_report_tui = DiagnosisReportTUI()
    diagnosis_report_tui.menu()

