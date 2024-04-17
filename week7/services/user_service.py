from week7.persistence.cruds.user_crud import UserCRUD
import logging


class UserService:

    # constructor
    def __init__(self):
        self.user_crud = UserCRUD()
        self.logger = logging.getLogger(__name__)

    # create
    def create_user(self, first_name, last_name, email, role_id):
        if not first_name or not last_name or not email or not role_id:
            logging.error("Fields cannot be empty")
            return None
        self.user_crud.create_user(first_name, last_name, email, role_id)

    # retrieve
    def retrieve_user(self, user_id):
        if not user_id:
            logging.error("user_id cannot be empty")
            return None
        return self.user_crud.retrieve_user(user_id)

    def retrieve_all_users(self):
        return self.user_crud.retrieve_all_users()

    def retrieve_user_by_email(self, email):
        if not email:
            logging.error("Email cannot be empty")
            return None
        return self.user_crud.retrieve_user_by_email(email)

    # update
    def update_user(self, user_id, first_name, last_name, email, role_id):
        if not user_id or not first_name or not last_name or not email or not role_id:
            logging.error("Fields cannot be empty")
            return None
        return self.user_crud.update_user(user_id, first_name, last_name, email, role_id)

    # delete
    def delete_user(self, user_id):
        if not user_id:
            logging.error("user_id cannot be empty")
            return None
        self.user_crud.delete_user(user_id)

