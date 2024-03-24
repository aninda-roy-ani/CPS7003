from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from week7.persistence.entities.auth import Auth
from week7.database.university import DATABASE
from cryptography.fernet import Fernet
import logging


class AuthCRUD:

    # constructor
    def __init__(self):
        self.engine = create_engine(DATABASE)
        self.Session = sessionmaker(bind=self.engine)
        self.logger = logging.getLogger(__name__)
        self.__fernet = Fernet(Fernet.generate_key())

    # create
    def create_auth(self, username, password):
        session = self.Session()
        try:
            auth = {
                "Username": username,
                "Password": password  # self.__fernet.encrypt(password.encode())
            }
            auth = Auth(**auth)
            session.add(auth)
            session.commit()
            logging.info(f"auth created for Username {username}")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while Creating Auth Info: {str(e)}")
        except Exception as e:
            logging.error(f"Error during encryption: {str(e)}")
        finally:
            session.close()

    # retrieve
    def retrieve_auth(self, username):
        session = self.Session()
        try:
            auth = session.query(Auth).filter_by(Username=username).first()
            if auth:
                return auth.Password  # self.__fernet.decrypt(auth.Password).decode()
            else:
                logging.error("Username does not exist")
        except SQLAlchemyError as e:
            logging.error(f"Error during Auth Retrieval: {str(e)}")
        except Exception as e:
            logging.error(f"Error during Decryption: {str(e)}")
        finally:
            session.close()

    # update
    def update_auth(self, username, password):
        session = self.Session()
        try:
            auth = session.query(Auth).filter_by(Username=username).first()
            if auth:
                auth.Password = password
                session.commit()
                logging.info(f"Password updated for Username {username}")
            else:
                logging.error("Username does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error during password update: {str(e)}")
        finally:
            session.close()


if __name__ == "__main__":
    auth = AuthCRUD()
    # auth.create_auth("aninda", "pass12")
    auth.update_auth("aninda", "pass12")
    print(auth.retrieve_auth("aninda"))
