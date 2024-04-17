from week7.services.subject_service import SubjectService


class SubjectTUI:

    def __init__(self):
        self.subject_service = SubjectService()

    def create_subject(self):
        title = input("Enter Subject Title: ")
        subject_leader = input("Enter Subject Leader ID: ")
        try:
            self.subject_service.create_subject(title, subject_leader)
            print(f"Subject {title} Created")
        except Exception as e:
            print(f"Error while creating subject: {str(e)}")

    def delete_subject(self):
        id = input("Enter Subject ID: ")
        try:
            self.subject_service.delete_subject(id)
            print(f"Subject with ID {id} Deleted")
        except Exception as e:
            print(f"Error while deleting subject: {str(e)}")

    def update_subject(self):
        id = input("Enter Subject ID to update: ")
        title = input("Enter Subject Title: ")
        subject_leader = input("Enter Subject Leader ID: ")
        try:
            self.subject_service.update_subject(id, title, subject_leader)
            print(f"Subject with ID {id} Updated")
        except Exception as e:
            print(f"Error while updating subject: {str(e)}")

    def list_subjects(self):
        try:
            subjects = self.subject_service.retrieve_all_subjects()
            for subject in subjects:
                print(f"Subject ID: {subject.SubjectID}, Title: {subject.Title}, Subject Leader ID: {subject.SubjectLeader}")
        except Exception as e:
            print(f"Error while retrieving subjects: {str(e)}")

    def find_subject_by_id(self):
        subject_id = input("Enter Subject ID: ")
        try:
            subject = self.subject_service.retrieve_subject(subject_id)
            print(f"SubjectID: {subject.SubjectID}, Title: {subject.Title}, Subject Leader ID: {subject.SubjectLeader}")
        except Exception as e:
            print(f"Error while retrieving subject: {str(e)}")

    def menu(self):
        while True:
            print("\nSubject Management System")
            print("1. Add Subject")
            print("2. Update Subject")
            print("3. Delete Subject")
            print("4. List Subjects")
            print("5. Find Subject by ID")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_subject()
            elif choice == "2":
                self.update_subject()
            elif choice == "3":
                self.delete_subject()
            elif choice == "4":
                self.list_subjects()
            elif choice == "5":
                self.find_subject_by_id()
            elif choice == '6':
                print("Exiting Subject Management System.")
                break
            else:
                print("Invalid Choice. Please try again.")