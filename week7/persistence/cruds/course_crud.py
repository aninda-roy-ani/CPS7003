from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from week7.persistence.entities.course import Course
from week7.database.university import DATABASE
import logging


class CourseCRUD:

    # constructor
    def __init__(self):
        self.engine = create_engine(DATABASE)
        self.Session = sessionmaker(bind=self.engine)
        self.logger = logging.getLogger(__name__)

    # create
    def create_course(self, award, title, course_leader, subject_id):
        session = self.Session()
        try:
            course = {
                "Award": award,
                "Title": title,
                "CourseLeader": course_leader,
                "SubjectID": subject_id
            }
            new_course = Course(**course)
            session.add(new_course)
            session.commit()
            logging.info(f"Course added with CourseID: {new_course.CourseID}")
            return new_course
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error adding Course: {str(e)}")
        finally:
            session.close()

    # retrieve
    def retrieve_course(self, course_id):
        session = self.Session()
        try:
            course = session.query(Course).filter_by(CourseID=course_id).first()
            if course:
                return course
            else:
                logging.error(f"Course with CourseID: {course_id} not found")
        except SQLAlchemyError as e:
            logging.error(f"Error retrieving Course: {str(e)}")
        finally:
            session.close()

    def retrieve_all_courses(self):
        session = self.Session()
        try:
            courses = session.query(Course).all()
            return courses
        except SQLAlchemyError as e:
            logging.error(f"Error retrieving all courses: {str(e)}")
        finally:
            session.close()

    # update
    def update_course(self, course_id, award, title, course_leader, subject_id):
        session = self.Session()
        try:
            course = session.query(Course).filter_by(CourseID=course_id).first()
            if course:
                course.Award = award
                course.Title = title
                course.CourseLeader = course_leader
                course.SubjectID = subject_id
                session.commit()
                logging.info(f"Course with CourseID: {course_id} was updated")
                return course
            else:
                logging.error(f"Course with CourseID: {course_id} not found")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error updating course: {str(e)}")
        finally:
            session.close()

    # delete
    def delete_course(self, course_id):
        session = self.Session()
        try:
            course = session.query(Course).filter_by(CourseID=course_id).first()
            if course:
                session.delete(course)
                session.commit()
                logging.info(f"Course with CourseID: {course_id} deleted")
            else:
                logging.error(f"Course with CourseID: {course_id} not found")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error deleting course: {str(e)}")
        finally:
            session.close()


if __name__ == "__main__":
    course = CourseCRUD()
    '''
    course.create_course("Master's","Computer Science", 2, 1)
    '''
    course.update_course(1,'Masters Degree', 'Ms in Computer Science', 2, 1)
    print(course.retrieve_course(1).Award)
