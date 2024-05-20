from datetime import datetime

from persistence.cruds.patient_crud import PatientCRUD
from persistence.cruds.diagnosis_crud import DiagnosisCRUD
from persistence.cruds.treatment_plan_crud import TreatmentPlanCRUD
from persistence.cruds.treatment_team_assignment_crud import TreatmentTeamAssignmentCRUD

from services.diagnosis_service import DiagnosisService
from services.treatment_plan_service import TreatmentPlanService
from services.treatment_team_assignment_service import TreatmentTeamAssignmentService
import logging


class PatientService:

    # constructor
    def __init__(self):
        self.patient_crud = PatientCRUD()
        self.diagnosis_service = DiagnosisService()
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
        patient = self.retrieve_patient(patient_id)
        diagnosis = self.diagnosis_service.retrieve_diagnosis_by_patient_id(patient_id)
        return {
            "patient_info": {
                "patient_id": patient.patient_id,
                "patient_name": patient.patient_name,
                "date_of_birth": patient.date_of_birth.strftime('%Y-%m-%d'),
                "gender": patient.gender,
                "contact_no": patient.contact_no,
                "address": patient.address
            },
            "diagnosis": [
                {
                    "diagnosis_id": d.diagnosis_id,
                    "diagnosis_details": d.diagnosis_details,
                    "diagnosis_date": d.diagnosis_date.strftime('%Y-%m-%d'),
                    "result": d.result,
                    "treatment_plans": [
                        {
                            "treatment_id": t.treatment_id,
                            "treatment_details": t.treatment_details,
                            "start_date": t.start_date.strftime('%Y-%m-%d'),
                            "end_date": t.end_date.strftime('%Y-%m-%d'),
                            "assigned_teams": [
                                {
                                    "name": a.name,
                                    "role": a.role
                                } for a in t.assignments
                            ]
                        } for t in d.treatment_plans
                    ]
                } for d in diagnosis
            ]
        }


if __name__ == "__main__":
    x = PatientService()
    '''
    x.create_patient('Foden', datetime(1998,9,15), 'M', '9124068', 'London, England')
    x.update_patient(2, address='Rio De Janeiro, Brazil')
    print(x.retrieve_patient(2).patient_name, x.retrieve_patient(2).address)
    print(x.retrieve_patient(3).patient_name)
    '''
    print(x.retrieve_patient_diagnostic_details(1))