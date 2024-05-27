from interface.diagnosis_tui import DiagnosisTUI
from interface.employee_tui import EmployeeTUI
from interface.medical_history_tui import MedicalHistoryTUI
from interface.patient_tui import PatientTUI
from interface.role_tui import RoleTUI
from interface.treatment_plan_tui import TreatmentPlanTUI
from interface.treatment_team_assignment_tui import TreatmentTeamAssignmentTUI
from interface.diagnosis_report_tui import DiagnosisReportTUI
from NoSQL_services.user_auth_NoSQL_service import UserAuthService


class MainTUI:
    def __init__(self):
        self.user = UserAuthService()

    def start(self):
        print('''
ST. MARY'S MED TECH HEALTHCARE MANAGEMENT
-----------------------------------------
What do you want to do?
1. Login
2. Sign Up
3. Exit
Enter your choice: ''')
        choice = input()
        if choice == '1':
            self.login()
        elif choice == '2':
            self.signup()
        elif choice == '3':
            print("Thank you for using the system!")
            exit()
        else:
            print("Invalid input! Please try again.")

    def healthcare_management(self):
        while True:
            print('''
ST MARY'S MED TECH HEALTHCARE DATA MANAGEMENT SYSTEM
----------------------------------------------------
What do you want to do?
1. ROLE MANAGEMENT
2. EMPLOYEE MANAGEMENT
3. PATIENT MANAGEMENT
4. MEDICAL HISTORY MANAGEMENT
5. DIAGNOSIS PLAN MANAGEMENT
6. TREATMENT PLAN MANAGEMENT
7. TREATMENT TEAM ASSIGNMENT MANAGEMENT
8. PATIENTS' DIAGNOSIS REPORT MANAGEMENT
9. Exit
Enter your choice: ''')
            choice = input()
            if choice == '1':
                role_management = RoleTUI()
                role_management.menu()
            elif choice == '2':
                employee_management = EmployeeTUI()
                employee_management.menu()
            elif choice == '3':
                patient_management = PatientTUI()
                patient_management.menu()
            elif choice == '4':
                medical_history_management = MedicalHistoryTUI()
                medical_history_management.menu()
            elif choice == '5':
                diagnosis_plan_management = DiagnosisTUI()
                diagnosis_plan_management.menu()
            elif choice == '6':
                treatment_plan_management = TreatmentPlanTUI()
                treatment_plan_management.menu()
            elif choice == '7':
                assignment_management = TreatmentTeamAssignmentTUI()
                assignment_management.menu()
            elif choice == '8':
                report_management = DiagnosisReportTUI()
                report_management.menu()
            elif choice == '9':
                self.start()
            else:
                print('Invalid or empty input!')

    def signup(self):
        print()
        username = input('Enter username: ')
        password = input('Enter password: ')
        booli = self.user.sign_up(username, password)
        if not booli:
            print("Username already exists!")
            self.signup()
        else:
            print("Sign Up Successful!")
            self.start()

    def login(self):
        print()
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        if self.user.login(username, password):
            print('''
HEALTHCARE USER INTERFACE
-------------------------
You have successfully logged in.
What you want to do?
1. Update password
2. Delete your account
3. GO TO SYSTEM DATABASE MANAGEMENT
4. Exit
Enter your choice: ''')
            choice = int(input())
            if choice == 1:
                new_password = input('Enter new password: ')
                self.user.update_password(username, new_password)
                print("Password updated! Login again!")
                self.login()
            elif choice == 2:
                self.user.delete_user(username)
                self.start()
            elif choice == 3:
                self.healthcare_management()
            elif choice == 4:
                print()
                self.start()
            else:
                print('Invalid input!')
        else:
            print('Invalid username or password!')
            self.start()


if __name__ == '__main__':
    main = MainTUI()
    main.start()
