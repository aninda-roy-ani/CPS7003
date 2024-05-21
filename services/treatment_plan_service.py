from datetime import datetime

from persistence.cruds.treatment_plan_crud import TreatmentPlanCRUD
from persistence.entities.treatment_plan import TreatmentPlan
from services.treatment_team_assignment_service import TreatmentTeamAssignmentService
import logging


class TreatmentPlanService:

    # constructor
    def __init__(self):
        self.treatment_plan_crud = TreatmentPlanCRUD()
        self.treatment_team_assignment_service = TreatmentTeamAssignmentService()
        self.logger = logging.getLogger(__name__)

    # create
    def create_treatment_plan(self, patient_id, diagnosis_id, treatment_details, start_date, end_date):
        if not all((patient_id, diagnosis_id, treatment_details, start_date, end_date)):
            self.logger.error("Missing treatment plan creation info")
            return False
        self.treatment_plan_crud.create_treatment_plan(patient_id, diagnosis_id, treatment_details, start_date, end_date)
        return True

    # retrieve
    def retrieve_treatment_plan(self, treatment_id):
        if not treatment_id:
            self.logger.error("No treatment id provided")
            return None
        return self.treatment_plan_crud.retrieve_treatment_plan(treatment_id)

    def retrieve_treatment_plan_by_diagnosis_id(self, diagnosis_id):
        plans = self.treatment_plan_crud.retrieve_treatment_plan_by_diagnosis_id(diagnosis_id)
        for plan in plans:
            plan.assignments = (
                self.treatment_team_assignment_service.retrieve_assignment_by_treatment_id(plan.treatment_id))
        return plans

    def retrieve_treatment_plan_by_patient_id(self, patient_id):
        plans = self.treatment_plan_crud.retrieve_treatment_plan_by_patient_id(patient_id)
        return plans

    def retrieve_all_treatment_plans(self):
        return self.treatment_plan_crud.retrieve_all_treatment_plans()

    # update
    def update_treatment_plan(self, treatment_id, patient_id=None, diagnosis_id=None, treatment_details=None, start_date=None, end_date=None):
        if not treatment_id:
            self.logger.error("No treatment id provided")
            return False
        treatment_plan = self.treatment_plan_crud.retrieve_treatment_plan(treatment_id)
        if not treatment_plan:
            self.logger.error(f"Treatment plan with ID {treatment_id} does not exist")
            return False
        self.treatment_plan_crud.update_treatment_plan(treatment_id, patient_id or treatment_plan.patient_id,
                                                       diagnosis_id or treatment_plan.diagnosis_id,
                                                       treatment_details or treatment_plan.treatment_details,
                                                       start_date or treatment_plan.start_date,
                                                       end_date or treatment_plan.end_date)
        return True

    # delete
    def delete_treatment_plan(self, treatment_id):
        if not treatment_id:
            self.logger.error("No treatment id provided")
            return False
        self.treatment_plan_crud.delete_treatment_plan(treatment_id)
        return True


if __name__ == "__main__":
    x = TreatmentPlanService()
    x.create_treatment_plan(1, 1, 'Using injections', datetime(2024, 6, 1), datetime(2024, 6, 30))
    print(x.retrieve_treatment_plan(1).treatment_details)