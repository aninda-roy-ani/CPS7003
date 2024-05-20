from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from persistence.entities.treatment_team_assignment import TreatmentTeamAssignment
from database.sqlite3_database import DATABASE
import logging


class TreatmentTeamAssignmentCRUD:
    # constructor
    def __init__(self):
        self.engine = create_engine(DATABASE)
        self.Session = sessionmaker(bind=self.engine)
        self.logger = logging.getLogger(__name__)

    # create
    def create_assignment(self, patient_id, treatment_id, user_id):
        session = self.Session()
        try:
            assignment = TreatmentTeamAssignment(patient_id=patient_id, treatment_id=treatment_id, user_id=user_id)
            session.add(assignment)
            session.commit()
            logging.info(f"Assignment created for Patient ID {patient_id}, Treatment ID {treatment_id} and User ID {user_id}")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while creating assignment: {str(e)}")
        finally:
            session.close()

    # retrieve
    def retrieve_assignment(self, assignment_id):
        session = self.Session()
        try:
            assignment = session.query(TreatmentTeamAssignment).filter_by(assignment_id=assignment_id).first()
            if assignment:
                return assignment
            else:
                logging.error(f"Assignment with ID {assignment_id} does not exist")
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving assignment: {str(e)}")
        finally:
            session.close()

    def retrieve_assignments_by_treatment_id(self, treatment_id):
        session = self.Session()
        return session.query(TreatmentTeamAssignment).filter_by(treatment_id=treatment_id).all()

    def retrieve_all_assignments(self):
        session = self.Session()
        try:
            assignments = session.query(TreatmentTeamAssignment).all()
            return assignments
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving all assignments: {str(e)}")
        finally:
            session.close()

    # update
    def update_assignment(self, assignment_id, patient_id, treatment_id, user_id):
        session = self.Session()
        try:
            assignment = session.query(TreatmentTeamAssignment).filter_by(assignment_id=assignment_id).first()
            if assignment:
                assignment.patient_id = patient_id
                assignment.treatment_id = treatment_id
                assignment.user_id = user_id
                session.commit()
                logging.info(f"Assignment with ID {assignment_id} updated")
            else:
                logging.error(f"Assignment with ID {assignment_id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while updating assignment: {str(e)}")
        finally:
            session.close()

    # delete
    def delete_assignment(self, assignment_id):
        session = self.Session()
        try:
            assignment = session.query(TreatmentTeamAssignment).filter_by(assignment_id=assignment_id).first()
            if assignment:
                session.delete(assignment)
                session.commit()
                logging.info(f"Assignment with ID {assignment_id} deleted")
            else:
                logging.error(f"Assignment with ID {assignment_id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while deleting assignment: {str(e)}")
        finally:
            session.close()
