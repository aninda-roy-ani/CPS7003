from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from week7.persistence.entities.subject import Subject
from week7.database.university import DATABASE
import logging


class SubjectCRUD:

    # constructor
    def __init__(self):
        self.engine = create_engine(DATABASE)
        self.Session = sessionmaker(bind=self.engine)
        self.logger = logging.getLogger(__name__)

    # create
    def create_subject(self, title, subject_leader):
        session = self.Session()
        try:
            subject = {
                'Title': title,
                'SubjectLeader': subject_leader
            }
            new_subject = Subject(**subject)
            session.add(new_subject)
            session.commit()
            logging.info(f'Subject with Subject ID: {new_subject.SubjectID} created')
            return new_subject
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f'Error while creating subject: {str(e)}')
        finally:
            session.close()

    # retrieve
    def retrieve_subject(self, subject_id):
        session = self.Session()
        try:
            subject = session.query(Subject).filter_by(SubjectID=subject_id).first()
            if subject:
                return subject
                # return f'[{subject.SubjectID}, {subject.Title}, {subject.SubjectLeader}]'
            else:
                logging.error(f'No subject found with subject ID: {subject_id}')
                # raise ValueError(f'No subject with subject ID: {subject_id}')
        except SQLAlchemyError as e:
            logging.error(f'Error while retrieving subject: {str(e)}')
        finally:
            session.close()

    def retrieve_all_subjects(self):
        session = self.Session()
        try:
            subjects = session.query(Subject).all()
            return subjects
        except SQLAlchemyError as e:
            logging.error(f'Error while retrieving all subjects: {str(e)}')
        finally:
            session.close()

    # update
    def update_subject(self, subject_id, title, subject_leader):
        session = self.Session()
        try:
            subject = session.query(Subject).filter_by(SubjectID=subject_id).first()
            if subject:
                subject.Title = title
                subject.SubjectLeader = subject_leader
                session.commit()
                logging.info(f'Successfully updated Subject with SubjectID: {subject_id}')
            else:
                logging.error(f'Subject with SubjectID: {subject_id} is not found')
                # raise ValueError(f'Subject with SubjectID: {subject_id} is not found')
        except SQLAlchemyError as e:
            logging.error(f'Error while updating subject: {str(e)}')
        finally:
            session.close()

    # delete
    def delete_subject(self, subject_id):
        session = self.Session()
        try:
            subject = session.query(Subject).filter_by(SubjectID=subject_id).first()
            if subject:
                session.delete(subject)
                session.commit()
                logging.info(f'Successfully deleted Subject with SubjectID: {subject_id}')
            else:
                logging.error(f'Subject with SubjectID: {subject_id} is not found')
                # raise ValueError(f'Subject with SubjectID: {subject_id} is not found')
        except SQLAlchemyError as e:
            logging.error(f'Error while deleting subject: {str(e)}')
        finally:
            session.close()


if __name__ == '__main__':
    subject = SubjectCRUD()
    '''
    subject.create_subject('Computer Science',2)
    print(subject.retrieve_subject(1))
    '''
    subject.retrieve_subject(5)
    inp = input("Enter subject: ")