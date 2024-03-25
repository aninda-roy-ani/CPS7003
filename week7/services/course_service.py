from week7.persistence.cruds.course_crud import CourseCRUD
import logging


class CourseService:

    # constructor
    def __init__(self):
        self.course_crud = CourseCRUD()
        self.logger = logging.getLogger(__name__)

    # create
    def create_course(self,  award, title, course_leader, subject_id):
        if not award or not title or not course_leader or not subject_id:
            logging.error("Fields can not be empty")
            return None
        self.course_crud.create_course(award, title, course_leader, subject_id)

    # retrieve
    def retrieve_course(self, course_id):
        if not course_id:
            logging.error("Course id cannot be empty")
            return None
        return self.course_crud.retrieve_course(course_id)

    def retrieve_all_courses(self):
        return self.course_crud.retrieve_all_courses()

    # update
    def update_course(self, course_id, award, title, course_leader, subject_id):
        if not course_id or not award or not title or not course_leader or not subject_id:
            logging.error("Fields can not be empty")
            return None
        self.course_crud.update_course(course_id, award, title, course_leader, subject_id)

    # delete
    def delete_course(self, course_id):
        if not course_id:
            logging.error("Course id cannot be empty")
            return None
        self.course_crud.delete_course(course_id)


if __name__ == "__main__":
    service = CourseService()
