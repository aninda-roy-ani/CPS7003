from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from week7.persistence.entities.user import User
from week7.database.university import DATABASE
import logging


class UserCRUD:

    # constructor
    def __init__(self):
        self.engine = create_engine(DATABASE)
        self.Session = sessionmaker(bind=self.engine)
        self.logger = logging.getLogger(__name__)

    # create
    def create_user(self, first_name, last_name, email, role_id):
        session = self.Session()
        try:
            user = {
                'FirstName': first_name,
                'LastName': last_name,
                'Email': email,
                'RoleID': role_id
            }
            new_user = User(**user)
            session.add(new_user)
            session.commit()
            logging.info(f'User created with id: {new_user.UserID}')
            return new_user
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f'Error in User Creation: {str(e)}')
        finally:
            session.close()

    # retrieve
    def retrieve_user(self, user_id):
        session = self.Session()
        try:
            user = session.query(User).filter_by(UserID=user_id).first()
            if user:
                # return f'[{user.UserID}, {user.FirstName}, {user.LastName}, {user.Email}, {user.RoleID}]'
                return user
            else:
                # raise ValueError(f'User with ID {user_id} does not exist')
                logging.error(f'User not found with id: {user_id}')
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f'Error in User Retrieval: {str(e)}')
        finally:
            session.close()

    def retrieve_all_users(self):
        session = self.Session()
        try:
            users = session.query(User).all()
            return users
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f'Error in All Users Retrieval: {str(e)}')
        finally:
            session.close()

    def retrieve_user_by_email(self, email):
        session = self.Session()
        try:
            user = session.query(User).filter_by(Email=email).first()
            if user:
                return user
            else:
                logging.error(f'User not found with email: {email}')
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f'Error in User Retrieval By Email: {str(e)}')
        finally:
            session.close()

    # update
    def update_user(self, user_id, first_name, last_name, email, role_id):
        session = self.Session()
        try:
            user = session.query(User).filter_by(UserID=user_id)
            if user:
                user.FirstName = first_name
                user.LastName = last_name
                user.Email = email
                user.RoleID = role_id
                session.commit()
                logging.info(f'Updated User Details for UserID: {user_id}')
            else:
                logging.error(f'User with ID: {user_id} not found')
                # raise ValueError(f'User with ID: {user_id} not found')
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f'Error in User Update: {str(e)}')
        finally:
            session.close()

    # delete
    def delete_user(self, user_id):
        session = self.Session()
        try:
            user = session.query(User).filter_by(UserID=user_id).first()
            if user:
                session.delete(user)
                session.commit()
                logging.info(f'User with ID: {user_id} deleted')
            else:
                logging.error(f'User with ID: {user_id} not found')
                # raise ValueError(f'User with ID: {user_id} not found')
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f'Error in User Deletion: {str(e)}')


if __name__ == '__main__':
    user1 = UserCRUD()
    '''
    print(user1.create_user('John', 'Doe', 'johndoe@yahoo.com', 1))
    print(user1.retrieve_user(1).Email)
    print(user1.retrieve_all_users()[0].Email)
    print(user1.retrieve_user_by_email('johndoe@yahoo.com'))
    '''
    print(user1.create_user('Prins', 'Butt', 'prinsbutt@stmarys.com', 2))