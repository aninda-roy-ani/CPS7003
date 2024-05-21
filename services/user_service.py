from persistence.cruds.user_crud import UserCRUD


class UserService:
    def __init__(self):
        self.user_crud = UserCRUD()

    def verify(self, username, password):
        user = self.user_crud.retrieve_user(username)
        if user:
            if user.password == password:
                return True
        return False

    def update_password(self, username, new_password):
        self.user_crud.update_user(username, new_password)

    def delete_user(self, username):
        self.user_crud.delete_user(username)

    def create_user(self, username, password):
        user = self.user_crud.retrieve_user(username)
        if user:
            return False
        self.user_crud.create_user(username, password)
        return True


