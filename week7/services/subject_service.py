from week7.persistence.cruds.subject_crud import SubjectCRUD
import logging


class SubjectService:

    # constructor
    def __init__(self):
        self.subject_crud = SubjectCRUD()
        self.logger = logging.getLogger(__name__)

    # create
    def create_subject(self, title, subject_leader):
        if not title or not subject_leader:
            logging.error(f"Fields cannot be empty")
            return None
        self.subject_crud.create_subject(title, subject_leader)

    # retrieve
    def retrieve_subject(self, subject_id):
        if not subject_id:
            logging.error(f"Subject ID cannot be empty")
            return None
        return self.subject_crud.retrieve_subject(subject_id)

    def retrieve_all_subjects(self):
        return self.subject_crud.retrieve_all_subjects()

    # update
    def update_subject(self, subject_id, title, subject_leader):
        if not subject_id or not title or not subject_leader:
            logging.error(f"Fields cannot be empty")
            return None
        self.subject_crud.update_subject(subject_id, title, subject_leader)

    # delete
    def delete_subject(self, subject_id):
        if not subject_id:
            logging.error(f"Subject ID cannot be empty")
            return None
        self.subject_crud.delete_subject(subject_id)