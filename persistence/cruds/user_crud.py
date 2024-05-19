from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from persistence.entities.user import User
from database.sqlite3_database import DATABASE
import logging


class UserCRUD:
    # constructor
    def __init__(self):
        self.engine = create_engine(DATABASE)
        self.Session = sessionmaker(bind=self.engine)
        self.logger = logging.getLogger(__name__)

    # create
    def create_user(self, username, password, first_name, last_name, role_id):
        session = self.Session()
        try:
            user = User(username=username, password=password, first_name=first_name, last_name=last_name, role_id=role_id)
            session.add(user)
            session.commit()
            logging.info(f"User {username} created")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while creating user: {str(e)}")
        finally:
            session.close()

    # retrieve
    def retrieve_user(self, user_id):
        session = self.Session()
        try:
            user = session.query(User).filter_by(user_id=user_id).first()
            if user:
                return user
            else:
                logging.error(f"User with ID {user_id} does not exist")
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving user: {str(e)}")
        finally:
            session.close()

    def retrieve_all_users(self):
        session = self.Session()
        try:
            users = session.query(User).all()
            return users
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving all users: {str(e)}")
        finally:
            session.close()

    # update
    def update_user(self, user_id, username, password, first_name, last_name, role_id):
        session = self.Session()
        try:
            user = session.query(User).filter_by(user_id=user_id).first()
            if user:
                user.username = username
                user.password = password
                user.first_name = first_name
                user.last_name = last_name
                user.role_id = role_id
                session.commit()
                logging.info(f"User with ID {user_id} updated")
            else:
                logging.error(f"User with ID {user_id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while updating user: {str(e)}")
        finally:
            session.close()

    # delete
    def delete_user(self, user_id):
        session = self.Session()
        try:
            user = session.query(User).filter_by(user_id=user_id).first()
            if user:
                session.delete(user)
                session.commit()
                logging.info(f"User with ID {user_id} deleted")
            else:
                logging.error(f"User with ID {user_id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while deleting user: {str(e)}")
        finally:
            session.close()


if __name__ == "__main__":
    x = UserCRUD()
    x.create_user('prins', '111111', 'Prins', 'Butt', 5)
    x.create_user('ani', '111111', 'Ani', 'Roy', 1)
    x.create_user('messi', '111111', 'Messi', 'Lionel', 2)
    x.create_user('neymar', '111111', 'Neymar', 'Jr', 3)
    x.create_user('tiasha', '111111', 'Tiasha', 'Rubi', 4)
    users = x.retrieve_all_users()
    for user in users:
        print(user.username, user.first_name, user.last_name, user.role_id)

