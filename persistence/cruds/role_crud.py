from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from persistence.entities.role import Role
from database.sqlite3_database import DATABASE
import logging


class RoleCRUD:
    # constructor
    def __init__(self):
        self.engine = create_engine(DATABASE)
        self.Session = sessionmaker(bind=self.engine)
        self.logger = logging.getLogger(__name__)

    # create
    def create_role(self, role_name):
        session = self.Session()
        try:
            role = Role(role_name=role_name)
            session.add(role)
            session.commit()
            logging.info(f"Role {role_name} created")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while creating role: {str(e)}")
        finally:
            session.close()

    # retrieve
    def retrieve_role(self, role_id):
        session = self.Session()
        try:
            role = session.query(Role).filter_by(role_id=role_id).first()
            if role:
                return role
            else:
                logging.error(f"Role with ID {role_id} does not exist")
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving role: {str(e)}")
        finally:
            session.close()

    def retrieve_all_roles(self):
        session = self.Session()
        try:
            roles = session.query(Role).all()
            return roles
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving all roles: {str(e)}")
        finally:
            session.close()

    # update
    def update_role(self, role_id, role_name):
        session = self.Session()
        try:
            role = session.query(Role).filter_by(role_id=role_id).first()
            if role:
                role.role_name = role_name
                session.commit()
                logging.info(f"Role with ID {role_id} updated")
            else:
                logging.error(f"Role with ID {role_id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while updating role: {str(e)}")
        finally:
            session.close()

    # delete
    def delete_role(self, role_id):
        session = self.Session()
        try:
            role = session.query(Role).filter_by(role_id=role_id).first()
            if role:
                session.delete(role)
                session.commit()
                logging.info(f"Role with ID {role_id} deleted")
            else:
                logging.error(f"Role with ID {role_id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while deleting role: {str(e)}")
        finally:
            session.close()


if __name__ == "__main__":
    x = RoleCRUD()
    x.create_role('Senior Surgeon')
    x.create_role('Senior Consultant')
    x.create_role('Consultant')
    x.create_role('Nurse')
    x.create_role('Moderator')
    print(x.retrieve_all_roles())
    print()
    print(x.retrieve_role(3).role_name)
    print()
    x.update_role(7, 'xyz')
    x.update_role(5, 'Management')
    print(x.retrieve_role(5).role_name)