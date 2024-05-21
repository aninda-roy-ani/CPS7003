from persistence.cruds.treatment_team_assignment_crud import TreatmentTeamAssignmentCRUD
from services.employee_service import EmployeeService
from services.role_service import RoleService
import logging


class TreatmentTeamAssignmentService:

    # constructor
    def __init__(self):
        self.assignment_crud = TreatmentTeamAssignmentCRUD()
        self.role_service = RoleService()
        self.employee_service = EmployeeService()
        self.logger = logging.getLogger(__name__)

    # create
    def create_assignment(self, patient_id, treatment_id, employee_id):
        if not all((patient_id, treatment_id, employee_id)):
            self.logger.error("Missing assignment creation info")
            return False
        self.assignment_crud.create_assignment(patient_id, treatment_id, employee_id)
        return True

    # retrieve
    def retrieve_assignment(self, assignment_id):
        if not assignment_id:
            self.logger.error("No assignment id provided")
            return None
        return self.assignment_crud.retrieve_assignment(assignment_id)

    def retrieve_assignment_by_treatment_id(self, treatment_id):
        teams = self.assignment_crud.retrieve_assignments_by_treatment_id(treatment_id)
        for team in teams:
            employee = self.employee_service.retrieve_employee(team.employee_id)
            team.name = employee.first_name + " " + employee.last_name
            team.role = self.role_service.retrieve_role(employee.role_id).role_name
        return teams

    def retrieve_assignment_by_patient_id(self, p):
        return self.assignment_crud.retrieve_assignments_by_patient_id(p)

    def retrieve_all_assignments(self):
        return self.assignment_crud.retrieve_all_assignments()

    # update
    def update_assignment(self, assignment_id, patient_id=None, treatment_id=None, employee_id=None):
        if not assignment_id:
            self.logger.error("No assignment id provided")
            return False
        assignment = self.assignment_crud.retrieve_assignment(assignment_id)
        if not assignment:
            self.logger.error(f"Assignment with ID {assignment_id} does not exist")
            return False
        self.assignment_crud.update_assignment(assignment_id, patient_id or assignment.patient_id, treatment_id or
                                               assignment.treatment_id, employee_id or assignment.employee_id)
        return True

    # delete
    def delete_assignment(self, assignment_id):
        if not assignment_id:
            self.logger.error("No assignment id provided")
            return False
        self.assignment_crud.delete_assignment(assignment_id)
        return True



if __name__ == "__main__":
    x = TreatmentTeamAssignmentService()
    '''
    x.create_assignment(1, 1, 5)
    x.create_assignment(1, 1, 3)
    x.create_assignment(1, 1, 2)
    x.delete_assignment(2)
    '''
    all = x.retrieve_all_assignments()
    print([a.assignment_id for a in all])