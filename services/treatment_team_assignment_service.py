from persistence.cruds.treatment_team_assignment_crud import TreatmentTeamAssignmentCRUD
import logging


class TreatmentTeamAssignmentService:

    # constructor
    def __init__(self):
        self.assignment_crud = TreatmentTeamAssignmentCRUD()
        self.logger = logging.getLogger(__name__)

    # create
    def create_assignment(self, patient_id, treatment_id, user_id):
        if not all((patient_id, treatment_id, user_id)):
            self.logger.error("Missing assignment creation info")
            return False
        self.assignment_crud.create_assignment(patient_id, treatment_id, user_id)
        return True

    # retrieve
    def retrieve_assignment(self, assignment_id):
        if not assignment_id:
            self.logger.error("No assignment id provided")
            return None
        return self.assignment_crud.retrieve_assignment(assignment_id)

    # retrieve all
    def retrieve_all_assignments(self):
        return self.assignment_crud.retrieve_all_assignments()

    # update
    def update_assignment(self, assignment_id, patient_id=None, treatment_id=None, user_id=None):
        if not assignment_id:
            self.logger.error("No assignment id provided")
            return False
        assignment = self.assignment_crud.retrieve_assignment(assignment_id)
        if not assignment:
            self.logger.error(f"Assignment with ID {assignment_id} does not exist")
            return False
        if patient_id:
            assignment.patient_id = patient_id
        if treatment_id:
            assignment.treatment_id = treatment_id
        if user_id:
            assignment.user_id = user_id
        self.assignment_crud.update_assignment(assignment_id, patient_id, treatment_id, user_id)
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
    '''
    x.delete_assignment(2)
    all = x.retrieve_all_assignments()
    print([a.assignment_id for a in all])