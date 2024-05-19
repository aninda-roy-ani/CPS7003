from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from persistence.entities.patient import Patient
from database.sqlite3_database import DATABASE
import logging


class PatientCRUD:
    # constructor
    def __init__(self):
        self.engine = create_engine(DATABASE)
        self.Session = sessionmaker(bind=self.engine)
        self.logger = logging.getLogger(__name__)

    # create
    def create_patient(self, patient_name, date_of_birth, gender, contact_no, address):
        session = self.Session()
        try:
            patient = Patient(patient_name=patient_name, date_of_birth=date_of_birth, gender=gender,
                              contact_no=contact_no, address=address)
            session.add(patient)
            session.commit()
            logging.info(f"Patient {patient_name} created")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while creating patient: {str(e)}")
        finally:
            session.close()

    # retrieve
    def retrieve_patient(self, patient_id):
        session = self.Session()
        try:
            patient = session.query(Patient).filter_by(patient_id=patient_id).first()
            if patient:
                return patient
            else:
                logging.error(f"Patient with ID {patient_id} does not exist")
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving patient: {str(e)}")
        finally:
            session.close()

    def retrieve_all_patients(self):
        session = self.Session()
        try:
            patients = session.query(Patient).all()
            return patients
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving all patients: {str(e)}")
        finally:
            session.close()

    # update
    def update_patient(self, patient_id, patient_name, date_of_birth, gender, contact_no, address):
        session = self.Session()
        try:
            patient = session.query(Patient).filter_by(patient_id=patient_id).first()
            if patient:
                patient.patient_name = patient_name
                patient.date_of_birth = date_of_birth
                patient.gender = gender
                patient.contact_no = contact_no
                patient.address = address
                session.commit()
                logging.info(f"Patient with ID {patient_id} updated")
            else:
                logging.error(f"Patient with ID {patient_id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while updating patient: {str(e)}")
        finally:
            session.close()

    # delete
    def delete_patient(self, patient_id):
        session = self.Session()
        try:
            patient = session.query(Patient).filter_by(patient_id=patient_id).first()
            if patient:
                session.delete(patient)
                session.commit()
                logging.info(f"Patient with ID {patient_id} deleted")
            else:
                logging.error(f"Patient with ID {patient_id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while deleting patient: {str(e)}")
        finally:
            session.close()
