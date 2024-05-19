from datetime import datetime

from persistence.cruds.medical_history_crud import MedicalHistoryCRUD
import logging


class MedicalHistoryService:

    # constructor
    def __init__(self):
        self.medical_history_crud = MedicalHistoryCRUD()
        self.logger = logging.getLogger(__name__)

    # create
    def create_medical_history(self, patient_id, admission_date, discharge_date, diagnosis, medical_notes):
        if not all((patient_id, admission_date, discharge_date, diagnosis, medical_notes)):
            self.logger.error("Missing medical history creation info")
            return False
        self.medical_history_crud.create_medical_history(patient_id, admission_date, discharge_date, diagnosis, medical_notes)
        return True

    # retrieve
    def retrieve_medical_history(self, history_id):
        if not history_id:
            self.logger.error("No history id provided")
            return None
        return self.medical_history_crud.retrieve_medical_history(history_id)

    def retrieve_all_medical_histories(self):
        return self.medical_history_crud.retrieve_all_medical_history()

    # update
    def update_medical_history(self, history_id, patient_id=None, admission_date=None, discharge_date=None, diagnosis=None, medical_notes=None):
        if not history_id:
            self.logger.error("No history id provided")
            return False
        history = self.medical_history_crud.retrieve_medical_history(history_id)
        if not history:
            self.logger.error(f"Medical history with ID {history_id} does not exist")
            return False
        if patient_id:
            history.patient_id = patient_id
        if admission_date:
            history.admission_date = admission_date
        if discharge_date:
            history.discharge_date = discharge_date
        if diagnosis:
            history.diagnosis = diagnosis
        if medical_notes:
            history.medical_notes = medical_notes
        self.medical_history_crud.update_medical_history(history_id, patient_id, admission_date, discharge_date, diagnosis, medical_notes)
        return True

    # delete
    def delete_medical_history(self, history_id):
        if not history_id:
            self.logger.error("No history id provided")
            return False
        self.medical_history_crud.delete_medical_history(history_id)
        return True


if __name__ == "__main__":
    x = MedicalHistoryService()
    x.create_medical_history(2, datetime(2020, 1, 1), datetime(2020, 1, 20), 'Hamstring', 'Muscular')
    all = x.retrieve_all_medical_histories()
    for a in all:
        print(a.history_id, a.patient_id, a.admission_date, a.discharge_date, a.diagnosis, a.medical_notes)