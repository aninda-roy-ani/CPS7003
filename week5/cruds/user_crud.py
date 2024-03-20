from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from week5.database.university import DATABASE_PATH
from week5.entities.user import User


class UserCRUD:

    # constructor
    def __init__(self, session):
        #self.engine = create_engine(f"sqlite:///{DATABASE_PATH}")
        self.Session = session
        #self.session = sessionmaker(bind=self.engine)

    # create
    def create_user(self, first_name, last_name, email, role):
        session = self.Session()

        try:
            user = {"FirstName": first_name, "LastName": last_name, "Email": email, "RoleID": role}
            new_user = User(**user)
            session.add(new_user)
            session.commit()
            return new_user

        except Exception as e:
            session.rollback()
            print(f"Error: {e}")
        finally:
            session.close()

    # retrieve
    def retrieve_user(self, id):
        session = self.Session()

        try:
            user = session.query(User).filter_by(UserID=id).first()

        finally:
            session.close()

    def retrieve_all_user(self):
        session = self.Session()
        try:
            users = session.query(User).all()
            return users
        finally:
            session.close()

    # update
    def update_user(self, id, first_name, last_name, email, role):
        session = self.Session()

        try:
            updated_user = session.query(User).filter_by(UserID=id).first()
            if updated_user:
                updated_user.FirstName = first_name
                updated_user.LastName = last_name
                updated_user.Email = email
                updated_user.RoleID = role
                session.commit()
                return updated_user
        except Exception as e:
            session.rollback()
            print(f"error: {e}")
        finally:
            session.close()

    # delete
    def delete_user(self, id):
        session = self.Session()

        try:
            delete_user = session.query(User).filter_by(UserId=id).first()
            if User:
                session.delete(User)
                session.commit()
                return delete_user

        except Exception as e:
            session.rollback()
            print(f"error: {e}")
        finally:
            session.close()

'''
engine = create_engine(f"sqlite:///{DATABASE_PATH}")
session = sessionmaker(bind=engine)
u = UserCRUD(session)
u.create_user("Aninda", "Roy Ani", "2313005@live.stmarys.ac.uk", 1)
'''

