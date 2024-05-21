from pymongo import MongoClient
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class UserAuthService:
    def __init__(self):
        self.mongo_client = MongoClient('mongodb://localhost:27017/')
        self.mongo_db = self.mongo_client['healthcare_db']
        self.user_auth_collection = self.mongo_db['User_Auth']

    def sign_up(self, username, password):
        try:
            # Check if user already exists
            if self.user_auth_collection.find_one({'username': username}):
                logger.error(f"Sign up failed: User '{username}' already exists.")
                return False

            user = {
                'username': username,
                'password': password
            }
            self.user_auth_collection.insert_one(user)
            logger.info(f"User '{username}' signed up successfully.")
            return True
        except Exception as e:
            logger.error(f"Sign up failed: {str(e)}")
            return False

    def update_password(self, username, password):
        try:
            result = self.user_auth_collection.update_one(
                {'username': username},
                {'$set': {'password': password}}
            )

            if result.matched_count > 0:
                logger.info(f"Password updated successfully for user '{username}'.")
                return True
            else:
                logger.error(f"Password update failed: User '{username}' not found.")
                return False
        except Exception as e:
            logger.error(f"Password update failed: {str(e)}")
            return False

    def login(self, username, password):
        try:
            user = self.user_auth_collection.find_one({'username': username, 'password': password})
            if user:
                logger.info(f"User '{username}' logged in successfully.")
                return True
            else:
                logger.error(f"Login failed: Invalid username or password for user '{username}'.")
                return False
        except Exception as e:
            logger.error(f"Login failed: {str(e)}")
            return False

    def delete_user(self, username):
        try:
            result = self.user_auth_collection.delete_one({'username': username})
            if result.deleted_count > 0:
                logger.info(f"User '{username}' deleted successfully.")
                return True
            else:
                logger.error(f"Delete failed: User '{username}' not found.")
                return False
        except Exception as e:
            logger.error(f"Delete failed: {str(e)}")
            return False


if __name__ == "__main__":
    auth_service = UserAuthService()
    # Example usage:
    # Sign up a new user
    sign_up_success = auth_service.sign_up('testuser', 'testpassword')
    print(f"Sign up success: {sign_up_success}")

    # Update password for an existing user
    update_success = auth_service.update_password('testuser', 'newpassword')
    print(f"Password update success: {update_success}")

    # User login
    login_success = auth_service.login('testuser', 'newpassword')
    print(f"Login success: {login_success}")

    # Delete user
    delete_success = auth_service.delete_user('testuser')
    print(f"Delete success: {delete_success}")


