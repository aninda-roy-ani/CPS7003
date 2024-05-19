from datetime import datetime

from persistence.cruds.patient_crud import PatientCRUD
import logging


class PatientService:

    # constructor
    def __init__(self):
        self.patient_crud = PatientCRUD()
        self.logger = logging.getLogger(__name__)

    # create
    def create_patient(self, patient_name, date_of_birth, gender, contact_no, address):
        if not patient_name or not date_of_birth or not gender or not contact_no or not address:
            self.logger.error("Missing patient creation info")
            return False
        self.patient_crud.create_patient(patient_name, date_of_birth, gender, contact_no, address)
        return True

    # retrieve
    def retrieve_patient(self, patient_id):
        if not patient_id:
            self.logger.error("No patient id provided")
            return None
        return self.patient_crud.retrieve_patient(patient_id)

    def retrieve_all_patients(self):
        return self.patient_crud.retrieve_all_patients()

    # update
    def update_patient(self, patient_id, patient_name=None, date_of_birth=None, gender=None, contact_no=None, address=None):
        if not patient_id:
            self.logger.error("No patient id provided")
            return False
        patient = self.patient_crud.retrieve_patient(patient_id)
        if not patient:
            self.logger.error(f"Patient with ID {patient_id} does not exist")
            return False
        self.patient_crud.update_patient(patient_id, patient_name or patient.patient_name,
                                         date_of_birth or patient.date_of_birth,
                                         gender or patient.gender,
                                         contact_no or patient.contact_no,
                                         address or patient.address)
        return True

    # delete
    def delete_patient(self, patient_id):
        if not patient_id:
            self.logger.error("No patient id provided")
            return False
        self.patient_crud.delete_patient(patient_id)
        return True

    # retrieve_patient_diagnostic_details
    def retrieve_patient_diagnostic_details(self, patient_id):
        if not patient_id:
            self.logger.error("No patient id provided")
            return False



if __name__ == "__main__":
    x = PatientService()
    x.create_patient('Foden', datetime(1998,9,15), 'M', '9124068', 'London, England')
    x.update_patient(2, address='Rio De Janeiro, Brazil')
    print(x.retrieve_patient(2).patient_name, x.retrieve_patient(2).address)
    print(x.retrieve_patient(3).patient_name)