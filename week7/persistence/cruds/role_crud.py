from week7.persistence.entities.role import Role
from week7.database.university import DATABASE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
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
            role = {
                "RoleName": role_name
            }
            new_role = Role(**role)
            session.add(new_role)
            session.commit()
            logging.info(f"New Role {role_name} has been created")
            return new_role
        except Exception as e:
            session.rollback()
            logging.error(f"Error in Role Creation: {str(e)}")
        finally:
            session.close()

    # retrieve
    def retrieve_role(self, id):
        session = self.Session()
        try:
            role = session.query(Role).filter_by(RoleID=id).first()
            if role:
                return role
            else:
                logging.error(f"Role with RoleID {id} does not exist")
        except Exception as e:
            logging.error(f"Error in Role Retrieval: {str(e)}")
        finally:
            session.close()

    def retrieve_role_by_role_name(self, role_name):
        session = self.Session()
        try:
            role = session.query(Role).filter_by(RoleName=role_name).first()
            if role:
                # return f"{role.RoleID} {role.RoleName}"
                return role
            else:
                logging.error(f"Role with name {role_name} does not exist")
        except SQLAlchemyError as e:
            logging.error(f"Error in Role Retrieval by name: {str(e)}")
        finally:
            session.close()

    def retrieve_all_roles(self):
        session = self.Session()
        try:
            roles = session.query(Role).all()
            return roles
        except SQLAlchemyError as e:
            logging.error(f"Error in Roles Retrieval: {str(e)}")
        finally:
            session.close()

    # update
    def update_role(self, id, role_name):
        session = self.Session()
        try:
            role = session.query(Role).filter_by(RoleID=id).first()
            if role:
                role.RoleName = role_name
                session.commit()
                logging.info(f"Role {role_name} has been updated")
            else:
                logging.error(f"RoleID {id} does not exist")
                # raise ValueError(f"RoleID {id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error in Role Update: {str(e)}")
        finally:
            session.close()

    # delete
    def delete_role(self, id):
        session = self.Session()
        try:
            role = session.query(Role).filter_by(RoleID=id).first()
            if role:
                session.delete(role)
                session.commit()
                logging.info(f"role {id} has been deleted")
            else:
                logging.error(f"role {id} does not exist")
                # raise ValueError(f"role {id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error in Role Deletion: {str(e)}")
        finally:
            session.close()


if __name__ == "__main__":
    role = RoleCRUD()
    '''
    role.create_role("STUDENT")
    roles = role.retrieve_all_roles()
    for r in roles:
        print(r.RoleID, r.RoleName)
    print(role.retrieve_role(1).RoleName)
    print(role.retrieve_role_by_role_name('STUDENT'))
    role.create_role("ASSOCIATE PROFESSOR")
    '''
    role.retrieve_all_roles()