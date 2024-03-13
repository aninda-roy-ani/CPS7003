from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from week5.database.database import DATABASE_PATH
from week5.entities.role import Role


class RoleCRUD:

    # constructor
    def __init__(self, session):
        self.engine = create_engine(f"sqlite:///{DATABASE_PATH}")
        self.Session = session

    # create
    def create_role(self, role_name):
        session = self.Session()

        try:
            role = {"RoleName": role_name}
            new_role = Role(**role)
            session.add(new_role)
            session.commit()
            return new_role
        except Exception as e:
            session.rollback()
            print(f"Error: {e}")
        finally:
            session.close()

    # retrieve
    def retrieve_role(self, id):
        session = self.Session()
        try:
            role = session.query(Role).filter_by(RoleID=id).first()

        finally:
            session.close()

    def retrieve_all_roles(self, id):
        session = self.Session()

        try:
            role = session.query(Role).all()
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
                return role

        except Exception as e:
            session.rollback()
            print(f"Error: {e}")
        finally:
            session.close()

    # delete
    def delete_role(self, id):
        session = self.Session()

        try:
            role = session.query(Role).filter_by(roleId=id).first()
            if role:
                session.delete(role)
                session.commit()
                # returns the deleted role
                return role

        except Exception as e:
            session.rollback()
            print(f"error: {e}")
        finally:
            session.close()
