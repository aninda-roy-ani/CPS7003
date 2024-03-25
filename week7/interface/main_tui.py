from week7.services.auth_service import AuthService
from week7.interface.tuis.role_tui import RoleTUI
from week7.interface.tuis.user_tui import UserTUI
from week7.interface.tuis.subject_tui import SubjectTUI
from week7.interface.tuis.course_tui import CourseTUI
from week7.interface.tuis.module_tui import ModuleTUI


class MainTUI:

    def __init__(self):
        self.auth = AuthService()
        self.role_tui = RoleTUI()
        self.user_tui = UserTUI()
        self.subject_tui = SubjectTUI()
        self.course_tui = CourseTUI()
        self.module_tui = ModuleTUI()

    def menu(self):
        while True:
            print("\nUniversity Management System")
            print("1. Role Management System")
            print("2. User Management System")
            print("3. Subject Management System")
            print("4. Course Management System")
            print("5. Module Management System")
            print("6. Exit Program")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.role_tui.menu()
            elif choice == "2":
                self.user_tui.menu()
            elif choice == "3":
                self.subject_tui.menu()
            elif choice == "4":
                self.course_tui.menu()
            elif choice == "5":
                self.module_tui.menu()
            elif choice == "6":
                print("Thank you for using this program")
                break
            else:
                print("Invalid Choice! Please try again.")

    def start(self):
        print("\n\n         Welcome  to  the  University  Management  System!")
        print("        ---------------------------------------------------")
        username = input("\n              Enter your username: ")
        password = input("              Enter your password: ")
        if self.auth.is_authenticated(username, password):
            self.menu()
        else:
            exit(1)


if __name__ == "__main__":
    MainTUI().start()