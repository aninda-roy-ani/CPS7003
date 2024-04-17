from week7.services.module_service import ModuleService


class ModuleTUI:

    def __init__(self):
        self.module_service = ModuleService()

    def create_module(self):
        print("Enter Module details")
        code = input("Enter Module Code: ")
        title = input("Enter Module Title: ")
        level = input("Enter Module Level: ")
        module_leader = int(input("Enter Module Leader ID: "))
        course_id = input("Enter Module Course ID: ")
        tutor = input("Enter Module Tutor ID: ")
        try:
            module = self.module_service.create_module(code, title, level, module_leader, course_id, tutor)
            print(f"Module {module.Title} is created")
        except Exception as e:
            print(f"Error creating module: {str(e)}")

    def retrieve_all_modules(self):
        try:
            modules = self.module_service.retrieve_all_modules()
            for module in modules:
                print(f"ModuleID: {module.ModuleID}, Code: {module.Code}, Title: {module.Title}, Level: {module.Level}"
                      f", Module Leader ID: {module.ModuleLeader}, CourseID: {module.CourseID}")
        except Exception as e:
            print(f"Error retrieving all modules: {str(e)}")

    def retrieve_all_module_tutors(self):
        try:
            modules = self.module_service.retrieve_all_modules_tutor()
            for module in modules:
                print(f"ID: {module.ID} ModuleID: {module.ModuleID}, UserID: {module.UserID}")
        except Exception as e:
            print(f"Error retrieving all module tutors: {str(e)}")

    def retrieve_module_by_id(self):
        module_id = int(input("Enter Module ID: "))
        try:
            module = self.module_service.retrieve_module(module_id)
            print(f"ModuleID: {module.ModuleID}, Code: {module.Code}, Title: {module.Title}, Level: {module.Level}"
                  f", Module Leader ID: {module.ModuleLeader}, CourseID: {module.CourseID}")
        except Exception as e:
            print(f"Error retrieving module: {str(e)}")

    def update_module(self):
        module_id = int(input("Enter Module ID to update: "))
        code = input("Enter Module Code: ")
        title = input("Enter Module Title: ")
        level = input("Enter Module Level: ")
        module_leader = int(input("Enter Module Leader ID: "))
        course_id = input("Enter Module Course ID: ")
        try:
            self.module_service.update_module(module_id, code, title, level, module_leader, course_id)
            print(f"Module {title} is updated")
        except Exception as e:
            print(f"Error updating module: {str(e)}")

    def update_module_tutor(self):
        tutor_id = int(input("Enter Module Tutor ID to update: "))
        module_id = int(input("Enter Module ID: "))
        user_id = int(input("Enter UserID: "))
        try:
            self.module_service.update_module_tutor(tutor_id, module_id, user_id)
            print(f"ModuleTutor {tutor_id} is updated")
        except Exception as e:
            print(f"Error updating module: {str(e)}")

    def delete_module(self):
        module_id = int(input("Enter Module ID to delete: "))
        try:
            self.module_service.delete_module(module_id)
            print(f"Module {module_id} is deleted")
        except Exception as e:
            print(f"Error deleting module: {str(e)}")

    def delete_module_tutor(self):
        tutor_id = int(input("Enter Module Tutor to delete: "))
        try:
            self.module_service.delete_module_tutor(tutor_id)
            print(f"ModuleTutor {tutor_id} is deleted")
        except Exception as e:
            print(f"Error deleting module: {str(e)}")

    def menu(self):
        while True:
            print("\nModule Management System")
            print("1. Add Module")
            print("2. List all Modules")
            print("3. List all Module-Tutors")
            print("4. Find Module by ModuleID")
            print("5. Update Module")
            print("6. Update Module-Tutor")
            print("7. Delete Module")
            print("8. Delete Module-Tutor")
            print("9. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_module()
            elif choice == "2":
                self.retrieve_all_modules()
            elif choice == "3":
                self.retrieve_all_module_tutors()
            elif choice == "4":
                self.retrieve_module_by_id()
            elif choice == "5":
                self.update_module()
            elif choice == "6":
                self.update_module_tutor()
            elif choice == "7":
                self.delete_module()
            elif choice == "8":
                self.delete_module_tutor()
            elif choice == "9":
                print("Exiting Module Management System")
                break
            else:
                print("Invalid Choice. Please try again.")


