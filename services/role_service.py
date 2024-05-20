from persistence.cruds.role_crud import RoleCRUD
import logging


class RoleService:

    # constructor
    def __init__(self):
        self.role_crud = RoleCRUD()
        self.logger = logging.getLogger(__name__)

    # create
    def create_role(self, role_name):
        if not role_name:
            self.logger.error("No role name provided")
            return False
        self.role_crud.create_role(role_name)
        return True

    # retrieve
    def retrieve_role(self, role_id):
        if not role_id:
            self.logger.error("No role id")
            return None
        return self.role_crud.retrieve_role(role_id)

    def retrieve_all_roles(self):
        return self.role_crud.retrieve_all_roles()

    # update
    def update_role(self, role_id, role_name):
        if not role_id or not role_name:
            logging.error("Role update info missing")
            return False
        role = self.role_crud.retrieve_role(role_id)
        if not role:
            self.logger.error(f"Role with ID {role_id} does not exist")
            return False
        self.role_crud.update_role(role_id or role.role_id, role_name or role.role_name)
        return True

    # delete
    def delete_role(self, role_id):
        if not role_id:
            self.logger.error("No role id provided")
            return False
        self.role_crud.delete_role(role_id)
        return True


if __name__ == "__main__":
    role = RoleService()
    print(role.retrieve_all_roles())
    print(role.retrieve_role(4).role_name)


