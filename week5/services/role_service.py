import logging
from week5.cruds.role_crud import RoleCRUD


class RoleService:
    def __init__(self, session):
        self.session = session
        self.logger = logging.getLogger(__name__)

    def create_role(self, role_name, creator_id):
        if not role_name:
            raise ValueError("Role name can not be empty")

        if not self._is_id_privileged(creator_id):
            raise PermissionError("Permission required")

        self.role_crud = RoleCRUD(self.session)
        new_role = self.role_crud.create_role(role_name)

        self.logger.info(f"New role '{role_name}' has been created by '{creator_id}'")

        return new_role

    def retrieve_all_roles(self):
        self.role_crud = RoleCRUD(self.session)
        return self.role_crud.retrieve_all_roles()

    def update_role(self, role_id, new_role_name, updater_id):
        if not role_id:
            raise ValueError("Role ID can not be empty")

        if not self._is_id_privileged(updater_id):
            raise PermissionError("Permission required")

        self.role_crud = RoleCRUD(self.session)
        updated_role = self.role_crud.update_role(role_id, new_role_name)

        self.logger.info(f"Update to the existing role with RoleID: '{role_id}' was made by '{updater_id}'")

        return updated_role

    def delete_role(self, role_id, deleter_id):
        if not role_id:
            raise ValueError("Role ID can not be empty")

        if not self._is_id_privileged(deleter_id):
            raise PermissionError("Permission required")

        self.role_crud = RoleCRUD(self.session)
        deleted_role = self.role_crud.delete_role(role_id)

        self.logger.info(f"Role with Role ID: '{role_id}' was deleted by '{deleter_id}'")

        return

    def _is_id_privileged(self, id):
        return True if id else False