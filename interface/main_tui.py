from interface.diagnosis_tui import DiagnosisTUI
from interface.employee_tui import EmployeeTUI
from interface.medical_history_tui import MedicalHistoryTUI
from interface.patient_tui import PatientTUI
from interface.role_tui import RoleTUI
from interface.treatment_plan_tui import TreatmentPlanTUI
from interface.treatment_team_assignment_tui import TreatmentTeamAssignmentTUI
from services.user_service import UserService


class MainTUI:
    def __init__(self):
        self.user = UserService()

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
8. GENERATE PATIENT DIAGNOSIS REPORT
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
                pass
            elif choice == '9':
                self.start()
            else:
                print('Invalid or empty input!')

    def signup(self):
        print()
        print('''
[A security code is needed which is provided from the
admin to restrict unauthorised users from signing up]
Enter the security code: ''')
        security_code = input()
        # There was a limitation in the project brief on what modules to be used!
        # Therefore, this is just a simple technique to restrict unauthorised users
        # since anyone opening the system to sign up and login doesn't make sense.
        if security_code == 'CPS7003':
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            self.user.create_user(username, password)
            print()
            self.start()
        else:
            print('Invalid security code! Going back!')
            print()
            self.start()

    def login(self):
        print()
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        if self.user.verify(username, password):
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
