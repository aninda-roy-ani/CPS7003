from week7.persistence.cruds.module_crud import ModuleCRUD
from week7.persistence.cruds.module_tutor_crud import ModuleTutorCRUD
import logging


class ModuleService:

    # constructor
    def __init__(self):
        self.module_crud = ModuleCRUD()
        self.module_tutor_crud = ModuleTutorCRUD()
        self.logger = logging.getLogger(__name__)

    # create
    def create_module(self, code, title, level, module_leader, course_id, tutor):
        if not code or not title or not level or not module_leader or not course_id or not tutor:
            logging.error("Fields can not be empty")
            return None
        module = self.module_crud.create_module(code, title, level, module_leader, course_id)
        self.module_tutor_crud.create_module_tutor(tutor, module.ModuleID)
        return module

    # retrieve
    def retrieve_module(self, module_id):
        if not module_id:
            logging.error("Module id can not be empty")
            return None
        return self.module_crud.retrieve_module(module_id)

    def retrieve_all_modules(self):
        return self.module_crud.retrieve_all_modules()

    def retrieve_module_tutor(self, id):
        return self.module_tutor_crud.retrieve_module_tutor(id)

    def retrieve_all_modules_tutor(self):
        return self.module_tutor_crud.retrieve_all_module_tutors()

    # update
    def update_module(self, module_id, code, title, level, module_leader, course_id):
        if not module_id or not code or not title or not level or not module_leader or not course_id:
            logging.error("Fields can not be empty")
            return None
        self.module_crud.update_module(module_id, code, title, level, module_leader, course_id)


    def update_module_tutor(self, id, module_id, user_id):
        return self.module_tutor_crud.update_module_tutor(id, user_id, module_id)

    # delete
    def delete_module(self, module_id):
        if not module_id:
            logging.error("Module id can not be empty")
            return None
        self.module_crud.delete_module(module_id)

    def delete_module_tutor(self, id):
        if not id:
            logging.error("id can not be empty")
            return None
        self.module_tutor_crud.delete_module_tutor(id)