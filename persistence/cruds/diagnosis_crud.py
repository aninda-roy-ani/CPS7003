from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from persistence.entities.diagnosis import Diagnosis
from database.sqlite3_database import DATABASE
import logging


class DiagnosisCRUD:
    # constructor
    def __init__(self):
        self.engine = create_engine(DATABASE)
        self.Session = sessionmaker(bind=self.engine)
        self.logger = logging.getLogger(__name__)

    # create
    def create_diagnosis_plan(self, patient_id, diagnosis_details, diagnosis_date, result):
        session = self.Session()
        try:
            plan = Diagnosis(patient_id=patient_id, diagnosis_details=diagnosis_details,
                             diagnosis_date=diagnosis_date, result=result)
            session.add(plan)
            session.commit()
            logging.info(f"Diagnosis plan for Patient ID {patient_id} created")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while creating diagnosis plan: {str(e)}")
        finally:
            session.close()

    # retrieve
    def retrieve_diagnosis_plan(self, diagnosis_id):
        session = self.Session()
        try:
            plan = session.query(Diagnosis).filter_by(diagnosis_id=diagnosis_id).first()
            if plan:
                return plan
            else:
                logging.error(f"Diagnosis plan with ID {diagnosis_id} does not exist")
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving diagnosis plan: {str(e)}")
        finally:
            session.close()

    # retrieve all
    def retrieve_all_diagnosis_plans(self):
        session = self.Session()
        try:
            plans = session.query(Diagnosis).all()
            return plans
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving all diagnosis plans: {str(e)}")
        finally:
            session.close()

    def retrieve_diagnosis_by_patient_id(self, patient_id):
        session = self.Session()
        try:
            plan = session.query(Diagnosis).filter_by(patient_id=patient_id).all()
            if plan:
                return plan
            else:
                logging.error(f"Diagnosis plan with Patient ID {patient_id} does not exist")
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving diagnosis plan: {str(e)}")
        finally:
            session.close()

    # update
    def update_diagnosis_plan(self, diagnosis_id, patient_id, diagnosis_details, diagnosis_date, result):
        session = self.Session()
        try:
            plan = session.query(Diagnosis).filter_by(diagnosis_id=diagnosis_id).first()
            if plan:
                plan.patient_id = patient_id
                plan.diagnosis_details = diagnosis_details
                plan.diagnosis_date = diagnosis_date
                plan.result = result
                session.commit()
                logging.info(f"Diagnosis plan with ID {diagnosis_id} updated")
            else:
                logging.error(f"Diagnosis plan with ID {diagnosis_id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while updating diagnosis plan: {str(e)}")
        finally:
            session.close()

    # delete
    def delete_diagnosis_plan(self, diagnosis_id):
        session = self.Session()
        try:
            plan = session.query(Diagnosis).filter_by(diagnosis_id=diagnosis_id).first()
            if plan:
                session.delete(plan)
                session.commit()
                logging.info(f"Diagnosis plan with ID {diagnosis_id} deleted")
            else:
                logging.error(f"Diagnosis plan with ID {diagnosis_id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while deleting diagnosis plan: {str(e)}")
        finally:
            session.close()
