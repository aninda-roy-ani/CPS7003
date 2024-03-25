from week7.persistence.cruds.role_crud import RoleCRUD
import logging


class RoleService:

    # constructor
    def __init__(self):
        self.role_crud = RoleCRUD()
        self.logger = logging.getLogger(__name__)

    # create
    def create_role(self, role_name):
        if not role_name:
            logging.error("No role name provided")
            return False
        self.role_crud.create_role(role_name)

    # retrieve
    def retrieve_role(self, role_id):
        if not role_id:
            logging.error("No role id")
            return None
        return self.role_crud.retrieve_role(role_id)

    def retrieve_all_roles(self):
        return self.role_crud.retrieve_all_roles()

    # update
    def update_role(self, role_id, role_name):
        if not role_id or not role_name:
            logging.error("Role update info missing")
            return False
        self.role_crud.update_role(role_id, role_name)

    # delete
    def delete_role(self, role_id):
        if not role_id:
            logging.error("No role id provided")
            return False
        self.role_crud.delete_role(role_id)


if __name__ == "__main__":
    role = RoleService()
    print(role.retrieve_all_roles())


