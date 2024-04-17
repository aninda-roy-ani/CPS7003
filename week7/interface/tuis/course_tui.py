from week7.services.course_service import CourseService


class CourseTUI:

    def __init__(self):
        self.course_service = CourseService()

    def create_course(self):
        print("Enter details for course creation")
        award = input("Enter Award: ")
        title = input("Enter Title: ")
        course_leader = int(input("Enter Course Leader ID: "))
        subject_id = int(input("Enter Subject ID: "))
        try:
            course = self.course_service.create_course(award, title, course_leader, subject_id)
            print(f"New course {course.Title} created successfully with ID: {course.CourseID}")
        except Exception as e:
            print(f"Error creating course: {str(e)}")

    def retrieve_all_courses(self):
        try:
            courses = self.course_service.retrieve_all_courses()
            for course in courses:
                print(f"ID: {course.CourseID}, Title: {course.Title}, Award: {course.Award}, "
                      f"SubjectLeaderID: {course.CourseLeader}, SubjectID: {course.SubjectID}")
        except Exception as e:
            print(f"Error retrieving all courses: {str(e)}")

    def retrieve_course_by_id(self):
        course_id = int(input("Enter Course ID: "))
        try:
            course = self.course_service.retrieve_course(course_id)
            print(f"ID: {course.CourseID}, Title: {course.Title}, Award: {course.Award}, "
                  f"CourseLeaderID: {course.CourseLeader}, SubjectID: {course.SubjectID}")
        except Exception as e:
            print(f"Error retrieving course: {str(e)}")

    def update_course(self):
        course_id = int(input("Enter Course ID to update: "))
        award = input("Enter Award: ")
        title = input("Enter Title: ")
        course_leader = input("Enter Course Leader ID: ")
        subject_id = input("Enter SubjectID: ")
        try:
            self.course_service.update_course(course_id, award, title, course_leader, subject_id)
            print(f"Course {title} with ID {course_id} has been updated")
        except Exception as e:
            print(f"Error updating course: {str(e)}")

    def delete_course(self):
        course_id = int(input("Enter Course to delete: "))
        try:
            self.course_service.delete_course(course_id)
            print(f"Course {course_id} has been deleted")
        except Exception as e:
            print(f"Error deleting course: {str(e)}")

    def menu(self):
        while True:
            print("\nCourse Management System")
            print("1. Add Course")
            print("2. Update Course")
            print("3. Delete Course")
            print("4. List Courses")
            print("5. Find Course by ID")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_course()
            elif choice == "2":
                self.update_course()
            elif choice == "3":
                self.delete_course()
            elif choice == "4":
                self.retrieve_all_courses()
            elif choice == "5":
                self.retrieve_course_by_id()
            elif choice == "6":
                print("Exiting Course Management System. ")
                break
            else:
                print("Invalid Choice. Please Try Again.")


