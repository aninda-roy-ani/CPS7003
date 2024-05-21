from NoSQL_services.diagnosis_report_NoSQL_service import DiagnosisReportService, logger


class DiagnosisReportTUI:
    def __init__(self):
        self.service = DiagnosisReportService()

    def menu(self):
        while True:
            print("\nPatients' Diagnosis Report Management")
            print("1. Check Pending Diagnosis Patients")
            print("2. Save New Diagnosis")
            print("3. Check Complete Diagnosis Patients")
            print("4. Get Diagnosis Report")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                pending = self.service.check_pending_reports()
                print("Pending Diagnosis Patients:",pending)
            elif choice == 2:
                pending = self.service.check_pending_reports()
                if len(pending) == 0:
                    print("No Pending Diagnosis Report to save!")
                else:
                    print("Enter Patient ID from",pending)
                    patient_id = input()
                    self.service.save_new_report(patient_id)
            elif choice == 3:
                ready = self.service.check_available_reports()
                print("Available Reports of the Patients:",ready)
            elif choice == 4:
                ready = self.service.check_available_reports()
                if len(ready) == 0:
                    print("No Diagnosis Report to print!")
                else:
                    print("Enter Patient ID from", ready)
                    patient_id = input()
                    if not patient_id.strip():
                        print("Invalid or empty input!")
                        continue
                    logger.debug(f"Fetching report for Patient ID: {patient_id}")
                    self.service.print_diagnosis_report(int(patient_id))
            elif choice == 5:
                print("Exiting Diagnosis Report Management")
                break
            else:
                print("Invalid or empty input!")


if __name__ == "__main__":
    diagnosis_report_tui = DiagnosisReportTUI()
    diagnosis_report_tui.menu()

