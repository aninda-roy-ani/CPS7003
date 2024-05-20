from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from persistence.entities.treatment_plan import TreatmentPlan
from database.sqlite3_database import DATABASE
import logging


class TreatmentPlanCRUD:
    # constructor
    def __init__(self):
        self.engine = create_engine(DATABASE)
        self.Session = sessionmaker(bind=self.engine)
        self.logger = logging.getLogger(__name__)

    # create
    def create_treatment_plan(self, patient_id, diagnosis_id, treatment_details, start_date, end_date):
        session = self.Session()
        try:
            plan = TreatmentPlan(patient_id=patient_id, diagnosis_id=diagnosis_id, treatment_details=treatment_details,
                                 start_date=start_date, end_date=end_date)
            session.add(plan)
            session.commit()
            logging.info(f"Treatment plan for Patient ID {patient_id} created")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while creating treatment plan: {str(e)}")
        finally:
            session.close()

    # retrieve
    def retrieve_treatment_plan(self, treatment_id):
        session = self.Session()
        try:
            plan = session.query(TreatmentPlan).filter_by(treatment_id=treatment_id).first()
            if plan:
                return plan
            else:
                logging.error(f"Treatment plan with ID {treatment_id} does not exist")
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving treatment plan: {str(e)}")
        finally:
            session.close()

    def retrieve_treatment_plan_by_diagnosis_id(self, diagnosis_id):
        session = self.Session()
        try:
            plan = session.query(TreatmentPlan).filter_by(diagnosis_id=diagnosis_id).all()
            if plan:
                return plan
            else:
                logging.error(f"Treatment plan with Diagnosis ID {diagnosis_id} does not exist")
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving treatment plan: {str(e)}")
        finally:
            session.close()

    def retrieve_all_treatment_plans(self):
        session = self.Session()
        try:
            plans = session.query(TreatmentPlan).all()
            return plans
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving all treatment plans: {str(e)}")
        finally:
            session.close()

    # update
    def update_treatment_plan(self, treatment_id, patient_id, diagnosis_id, treatment_details, start_date, end_date):
        session = self.Session()
        try:
            plan = session.query(TreatmentPlan).filter_by(treatment_id=treatment_id).first()
            if plan:
                plan.patient_id = patient_id
                plan.diagnosis_id = diagnosis_id
                plan.treatment_details = treatment_details
                plan.start_date = start_date
                plan.end_date = end_date
                session.commit()
                logging.info(f"Treatment plan with ID {treatment_id} updated")
            else:
                logging.error(f"Treatment plan with ID {treatment_id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while updating treatment plan: {str(e)}")
        finally:
            session.close()

    # delete
    def delete_treatment_plan(self, treatment_id):
        session = self.Session()
        try:
            plan = session.query(TreatmentPlan).filter_by(treatment_id=treatment_id).first()
            if plan:
                session.delete(plan)
                session.commit()
                logging.info(f"Treatment plan with ID {treatment_id} deleted")
            else:
                logging.error(f"Treatment plan with ID {treatment_id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while deleting treatment plan: {str(e)}")
        finally:
            session.close()
