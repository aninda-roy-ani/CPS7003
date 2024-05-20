from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from persistence.entities.employee import Employee
from database.sqlite3_database import DATABASE
import logging


class EmployeeCRUD:
    # constructor
    def __init__(self):
        self.engine = create_engine(DATABASE)
        self.Session = sessionmaker(bind=self.engine)
        self.logger = logging.getLogger(__name__)

    # create
    def create_employee(self, first_name, last_name, role_id):
        session = self.Session()
        try:
            employee = Employee(first_name=first_name, last_name=last_name, role_id=role_id)
            session.add(employee)
            session.commit()
            logging.info(f"Employee {employee.employee_id} created")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while creating employee: {str(e)}")
        finally:
            session.close()

    # retrieve
    def retrieve_employee(self, employee_id):
        session = self.Session()
        try:
            employee = session.query(Employee).filter_by(employee_id=employee_id).first()
            if employee:
                return employee
            else:
                logging.error(f"Employee with ID {employee_id} does not exist")
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving employee: {str(e)}")
        finally:
            session.close()

    def retrieve_all_employees(self):
        session = self.Session()
        try:
            employees = session.query(Employee).all()
            return employees
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving all employees: {str(e)}")
        finally:
            session.close()

    # update
    def update_employee(self, employee_id, first_name, last_name, role_id):
        session = self.Session()
        try:
            employee = session.query(Employee).filter_by(employee_id=employee_id).first()
            if employee:
                employee.first_name = first_name
                employee.last_name = last_name
                employee.role_id = role_id
                session.commit()
                logging.info(f"Employee with ID {employee_id} updated")
            else:
                logging.error(f"Employee with ID {employee_id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while updating employee: {str(e)}")
        finally:
            session.close()

    # delete
    def delete_employee(self, employee_id):
        session = self.Session()
        try:
            employee = session.query(Employee).filter_by(employee_id=employee_id).first()
            if employee:
                session.delete(employee)
                session.commit()
                logging.info(f"Employee with ID {employee_id} deleted")
            else:
                logging.error(f"Employee with ID {employee_id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while deleting employee: {str(e)}")
        finally:
            session.close()


if __name__ == "__main__":
    x = EmployeeCRUD()
    '''
    x.create_employee('prins', '111111', 'Prins', 'Butt', 5)
    x.create_employee('ani', '111111', 'Ani', 'Roy', 1)
    x.create_employee('messi', '111111', 'Messi', 'Lionel', 2)
    x.create_employee('neymar', '111111', 'Neymar', 'Jr', 3)
    x.create_employee('tiasha', '111111', 'Tiasha', 'Rubi', 4)
    '''

    employees = x.retrieve_all_employees()
    for employee in employees:
        print(employee.first_name, employee.last_name, employee.role_id)

