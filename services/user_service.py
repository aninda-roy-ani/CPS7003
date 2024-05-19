from persistence.cruds.user_crud import UserCRUD
import logging


class UserService:

    # constructor
    def __init__(self):
        self.user_crud = UserCRUD()
        self.logger = logging.getLogger(__name__)

    # create
    def create_user(self, username, password, first_name, last_name, role_id):
        if not username or not password or not role_id:
            logging.error("Missing user creation info")
            return False
        self.user_crud.create_user(username, password, first_name, last_name, role_id)
        return True

    # retrieve
    def retrieve_user(self, user_id):
        if not user_id:
            logging.error("No user id provided")
            return None
        return self.user_crud.retrieve_user(user_id)

    def retrieve_all_users(self):
        return self.user_crud.retrieve_all_users()

    # update
    def update_user(self, user_id, username=None, password=None, first_name=None, last_name=None, role_id=None):
        if not user_id:
            logging.error("No user id provided")
            return False
        user = self.user_crud.retrieve_user(user_id)
        if not user:
            logging.error(f"User with ID {user_id} does not exist")
            return False
        if username:
            user.username = username
        if password:
            user.password = password
        if role_id:
            user.role_id = role_id
        self.user_crud.update_user(user_id, username, password, first_name, last_name, role_id)
        return True

    # delete
    def delete_user(self, user_id):
        if not user_id:
            logging.error("No user id provided")
            return False
        self.user_crud.delete_user(user_id)
        return True
