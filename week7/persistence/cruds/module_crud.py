from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from week7.persistence.entities.module import Module
from week7.database.university import DATABASE
import logging


class ModuleCRUD:

    # constructor
    def __init__(self):
        self.engine = create_engine(DATABASE)
        self.Session = sessionmaker(bind=self.engine)
        self.logger = logging.getLogger(__name__)

    # create
    def create_module(self, code, title, level, module_leader, course_id):
        session = self.Session()
        try:
            module = {
                "Code" : code,
                "Title" : title,
                "Level" : level,
                "ModuleLeader" : module_leader,
                "CourseID" : course_id
            }
            new_module = Module(**module)
            session.add(new_module)
            session.commit()
            logging.info(f"Created module: {new_module.ModuleID}")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while creating module: {str(e)}")
        finally:
            session.close()

    # retrieve
    def retrieve_module(self, module_id):
        session = self.Session()
        try:
            module = session.query(Module).filter_by(ModuleID=module_id).first()
            if module:
                return module
            else:
                logging.error(f"No module with ModuleID: {module_id}")
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving module: {str(e)}")
        finally:
            session.close()

    def retrieve_all_modules(self):
        session = self.Session()
        try:
            modules = session.query(Module).all()
            return modules
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving all modules")
        finally:
            session.close()

    # update
    def update_module(self, module_id, code, title, level, module_leader, course_id):
        session = self.Session()
        try:
            module = session.query(Module).filter_by(ModuleID=module_id).first()
            if module:
                module.Code = code
                module.Title = title
                module.Level = level
                module.ModuleLeader = module_leader
                module.CourseID = course_id
                session.commit()
                logging.info(f"Module updated with ModuleID {module_id}")
            else:
                logging.error(f"ModuleID {module_id} not found")
        except SQLAlchemyError as e:
            logging.error(f"Error while updating module: {str(e)}")
        finally:
            session.close()

    # delete
    def delete_module(self, module_id):
        session = self.Session()
        try:
            module = session.query(Module).filter_by(ModuleID=module_id).first()
            if module:
                session.delete(module)
                session.commit()
                logging.info(f"Module deleted with ModuleID {module_id}")
            else:
                logging.error(f"Module not found with ModuleID{module_id}")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while deleting module: {str(e)}")
        finally:
            session.close()


if __name__ == "__main__":
    module = ModuleCRUD()
    '''
    module.create_module('CPS7003','Database',3,2,1)
    '''
    print(module.retrieve_module(1).Title)