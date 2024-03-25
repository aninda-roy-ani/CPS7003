from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from week7.persistence.entities.module_tutor import ModuleTutor
from week7.database.university import DATABASE
import logging


class ModuleTutorCRUD:

    # constructor
    def __init__(self):
        self.engine = create_engine(DATABASE)
        self.Session = sessionmaker(bind=self.engine)
        self.logger = logging.getLogger(__name__)

    # create
    def create_module_tutor(self, user_id, module_id):
        session = self.Session()
        try:
            module_tutor = {
                "UserID": user_id,
                "ModuleID": module_id
            }
            new_module_tutor = ModuleTutor(**module_tutor)
            session.add(new_module_tutor)
            session.commit()
            logging.info(f"Module Tutor with ID {module_id} created")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while creating Module Tutor: {str(e)}")
        finally:
            session.close()

    # retrieve
    def retrieve_module_tutor(self, id):
        session = self.Session()
        try:
            module_tutor = session.query(ModuleTutor).filter_by(ID=id).first()
            if module_tutor:
                return module_tutor
            else:
                logging.error(f"Module Tutor with ID {id} does not exist")
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving Module: {str(e)}")
        finally:
            session.close()

    def retrieve_module_tutor_id(self, module_id, user_id):
        session = self.Session()
        try:
            module_tutor = session.query(ModuleTutor).filter_by(ModuleID=module_id).filter_by(UserID=user_id).first()
            if module_tutor:
                return module_tutor.ID
            else:
                logging.error(f"Module Tutor with Module ID {module_id} and UserID {user_id} does not exist")
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving Module Tutor ID: {str(e)}")
        finally:
            session.close()

    def retrieve_all_module_tutors(self):
        session = self.Session()
        try:
            module_tutors = session.query(ModuleTutor).all()
            return module_tutors
        except SQLAlchemyError as e:
            logging.error(f"Error while retrieving all module tutors: {str(e)}")
        finally:
            session.close()

    # update
    def update_module_tutor(self, id, user_id, module_id):
        session = self.Session()
        try:
            module_tutor = session.query(ModuleTutor).filter_by(ID=id).first()
            if module_tutor:
                module_tutor.UserID = user_id
                module_tutor.ModuleID = module_id
                session.commit()
                logging.info(f"Module Tutor with ID {id} is updated")
            else:
                logging.error(f"Module Tutor with ID {id} does not exist")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while updating module tutor: {str(e)}")
        finally:
            session.close()

    # delete
    def delete_module_tutor(self, id):
        session = self.Session()
        try:
            module_tutor = session.query(ModuleTutor).filter_by(ID=id).first()
            if module_tutor:
                session.delete(module_tutor)
                session.commit()
                logging.info(f"Module Tutor with ID {id} is deleted")
            else:
                logging.error(f"Module Tutor with ID {id} does not exists")
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error while deleting module tutor: {str(e)}")


if __name__ == "__main__":
    mt = ModuleTutorCRUD()
    '''
    mt.create_module_tutor(2,1)
    '''
    mt1 = mt.retrieve_module_tutor(1)
    print(f"{mt1.UserID} {mt1.ModuleID}")