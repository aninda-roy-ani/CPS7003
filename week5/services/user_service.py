from week5.cruds.user_crud import UserCRUD


class UserService:

    def __init__(self, session):
        self.user_crud = UserCRUD(session)

    def create_user(self, first_name, last_name, email, role):
        return self.user_crud.create_user(first_name, last_name, email, role)

    def retrieve_user(self, id):
        return self.user_crud.retrieve_user(id)

    def retrieve_all_users(self):
        return self.user_crud.retrieve_all_user()

    def update_user(self, id, first_name, last_name, email, role):
        return self.user_crud.update_user(id, first_name, last_name, email, role)

    def delete_user(self, id):
        return self.user_crud.delete_user(id)