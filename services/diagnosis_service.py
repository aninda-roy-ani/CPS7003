from datetime import datetime

from persistence.cruds.diagnosis_crud import DiagnosisCRUD
from services.treatment_plan_service import TreatmentPlanService
from services.treatment_team_assignment_service import TreatmentTeamAssignmentService
import logging


class DiagnosisService:

    # constructor
    def __init__(self):
        self.diagnosis_crud = DiagnosisCRUD()
        self.treatment_plan_service = TreatmentPlanService()
        self.treatment_team_assignment_service = TreatmentTeamAssignmentService()
        self.logger = logging.getLogger(__name__)

    # create
    def create_diagnosis_plan(self, patient_id, diagnosis_details, diagnosis_date, result):
        if not all((patient_id, diagnosis_details, diagnosis_date, result)):
            self.logger.error("Missing diagnosis plan creation info")
            return False
        self.diagnosis_crud.create_diagnosis_plan(patient_id, diagnosis_details, diagnosis_date, result)
        return True

    # retrieve
    def retrieve_diagnosis_plan(self, diagnosis_id):
        if not diagnosis_id:
            self.logger.error("No diagnosis id provided")
            return None
        return self.diagnosis_crud.retrieve_diagnosis_plan(diagnosis_id)

    # retrieve all
    def retrieve_all_diagnosis_plans(self):
        return self.diagnosis_crud.retrieve_all_diagnosis_plans()

    def retrieve_diagnosis_by_patient_id(self, patient_id):
        diagnoses = self.diagnosis_crud.retrieve_diagnosis_by_patient_id(patient_id)
        for diagnose in diagnoses:
            diagnose.treatment_plans = (self.treatment_plan_service.retrieve_treatment_plan_by_diagnosis_id
                                       (diagnose.diagnosis_id))
        return diagnoses

    # update
    def update_diagnosis_plan(self, diagnosis_id, patient_id=None, diagnosis_details=None, diagnosis_date=None, result=None):
        if not diagnosis_id:
            self.logger.error("No diagnosis id provided")
            return False
        diagnosis_plan = self.diagnosis_crud.retrieve_diagnosis_plan(diagnosis_id)
        if not diagnosis_plan:
            self.logger.error(f"Diagnosis plan with ID {diagnosis_id} does not exist")
            return False
        if not patient_id:
            patient_id = diagnosis_plan.patient_id
        if not diagnosis_details:
            diagnosis_details = diagnosis_plan.diagnosis_details
        if not diagnosis_date:
            diagnosis_date = diagnosis_plan.diagnosis_date
        if not result:
            result = diagnosis_plan.result
        self.diagnosis_crud.update_diagnosis_plan(diagnosis_id, patient_id, diagnosis_details, diagnosis_date, result)
        return True

    # delete
    def delete_diagnosis_plan(self, diagnosis_id):
        if not diagnosis_id:
            self.logger.error("No diagnosis id provided")
            return False
        self.diagnosis_crud.delete_diagnosis_plan(diagnosis_id)
        return True


if __name__ == "__main__":
    x = DiagnosisService()
    alls = x.retrieve_all_diagnosis_plans()
    for a in alls:
        print(a.diagnosis_id, a.diagnosis_date, a.diagnosis_details)