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
    def create_user(self, username, password):
        session = self.Session()
        try:
            user = User(username=username, password=password)
            session.add(user)
            session.commit()
            logging.info(f"User {username} created")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while creating user: {str(e)}")
        finally:
            session.close()

    # retrieve
    def retrieve_user(self, username):
        session = self.Session()
        try:
            user = session.query(User).filter_by(username=username).first()
            if user:
                return user
            else:
                logging.error(f"User {username} does not exist")
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving user: {str(e)}")
        finally:
            session.close()

    # update
    def update_user(self, username, password):
        session = self.Session()
        try:
            user = session.query(User).filter_by(username=username).first()
            if user:
                user.password = password
                session.commit()
                logging.info(f"User {username} updated")
            else:
                logging.error(f"User {username} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while updating user: {str(e)}")
        finally:
            session.close()

    # delete
    def delete_user(self, username):
        session = self.Session()
        try:
            user = session.query(User).filter_by(username=username).first()
            if user:
                session.delete(user)
                session.commit()
                logging.info(f"User {username} deleted")
            else:
                logging.error(f"User {username} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while deleting user: {str(e)}")
        finally:
            session.close()
