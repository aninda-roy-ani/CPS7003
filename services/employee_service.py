from persistence.cruds.employee_crud import EmployeeCRUD
import logging


class EmployeeService:

    # constructor
    def __init__(self):
        self.employee_crud = EmployeeCRUD()
        self.logger = logging.getLogger(__name__)

    # create
    def create_employee(self, first_name, last_name, role_id):
        if not first_name or not last_name or not role_id:
            logging.error("Missing employee creation info")
            return False
        self.employee_crud.create_employee(first_name, last_name, role_id)
        return True

    # retrieve
    def retrieve_employee(self, employee_id):
        if not employee_id:
            logging.error("No employee id provided")
            return None
        return self.employee_crud.retrieve_employee(employee_id)

    def retrieve_all_employees(self):
        return self.employee_crud.retrieve_all_employees()

    # update
    def update_employee(self, employee_id, first_name=None, last_name=None, role_id=None):
        if not employee_id:
            logging.error("No employee id provided")
            return False
        employee = self.employee_crud.retrieve_employee(employee_id)
        if not employee:
            logging.error(f"Employee with ID {employee_id} does not exist")
            return False
        if role_id:
            employee.role_id = role_id
        self.employee_crud.update_employee(employee_id, first_name, last_name, role_id)
        return True

    # delete
    def delete_employee(self, employee_id):
        if not employee_id:
            logging.error("No employee id provided")
            return False
        self.employee_crud.delete_employee(employee_id)
        return True
