from week7.persistence.cruds.auth_crud import AuthCRUD
import logging

class AuthService:

    # constructor
    def __init__(self):
        self.auth_crud = AuthCRUD()
        self.logger = logging.getLogger(__name__)

    # create new auth
    def create_auth(self, username, password):
        if username is None or password is None:
            logging.warning("username or password is empty")
            return None
        if len(password) < 6:
            logging.warning("password must be at least 6 characters")
            return None
        self.auth_crud.create_auth(username, password)

    # authentication
    def is_authenticated(self, username, password):
        saved_password = self.auth_crud.retrieve_auth(username)
        if password != saved_password:
            logging.warning("password is incorrect")
            return False
        logging.info(f"Authenticated username {username}")
        return True

    # update password
    def update_password(self, username, password):
        self.auth_crud.update_auth(username, password)