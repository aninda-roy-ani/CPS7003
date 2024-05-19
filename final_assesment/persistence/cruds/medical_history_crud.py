from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from final_assesment.persistence.entities.medical_history import MedicalHistory
from final_assesment.database.sqlite3_database import DATABASE
import logging


class MedicalHistoryCRUD:
    # constructor
    def __init__(self):
        self.engine = create_engine(DATABASE)
        self.Session = sessionmaker(bind=self.engine)
        self.logger = logging.getLogger(__name__)

    # create
    def create_medical_history(self, patient_id, admission_date, discharge_date, diagnosis, medical_notes):
        session = self.Session()
        try:
            history = MedicalHistory(patient_id=patient_id, admission_date=admission_date, discharge_date=discharge_date,
                                     diagnosis=diagnosis, medical_notes=medical_notes)
            session.add(history)
            session.commit()
            logging.info(f"Medical history for Patient ID {patient_id} created")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while creating medical history: {str(e)}")
        finally:
            session.close()

    # retrieve
    def retrieve_medical_history(self, history_id):
        session = self.Session()
        try:
            history = session.query(MedicalHistory).filter_by(history_id=history_id).first()
            if history:
                return history
            else:
                logging.error(f"Medical history with ID {history_id} does not exist")
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving medical history: {str(e)}")
        finally:
            session.close()

    def retrieve_all_medical_history(self):
        session = self.Session()
        try:
            histories = session.query(MedicalHistory).all()
            return histories
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving all medical histories: {str(e)}")
        finally:
            session.close()

    # update
    def update_medical_history(self, history_id, patient_id, admission_date, discharge_date, diagnosis, medical_notes):
        session = self.Session()
        try:
            history = session.query(MedicalHistory).filter_by(history_id=history_id).first()
            if history:
                history.patient_id = patient_id
                history.admission_date = admission_date
                history.discharge_date = discharge_date
                history.diagnosis = diagnosis
                history.medical_notes = medical_notes
                session.commit()
                logging.info(f"Medical history with ID {history_id} updated")
            else:
                logging.error(f"Medical history with ID {history_id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while updating medical history: {str(e)}")
        finally:
            session.close()

    # delete
    def delete_medical_history(self, history_id):
        session = self.Session()
        try:
            history = session.query(MedicalHistory).filter_by(history_id=history_id).first()
            if history:
                session.delete(history)
                session.commit()
                logging.info(f"Medical history with ID {history_id} deleted")
            else:
                logging.error(f"Medical history with ID {history_id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while deleting medical history: {str(e)}")
        finally:
            session.close()
