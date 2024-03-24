from week7.persistence.cruds.role_crud import RoleCRUD
import logging


class RoleService:

    # constructor
    def __init__(self):
        self.role_crud = RoleCRUD()
        self.logger = logging.getLogger(__name__)

    # verify ID
    def is_id_privileged(self):
        return True

    # create
    def create_role(self, role_name, creator_id):
        if not role_name:
            logging.error("No role name provided")
            return False
        if not self.is_id_privileged:
            logging.error("Creator ID is not privileged")
        self.role_crud.create_role(role_name)

