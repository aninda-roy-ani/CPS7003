import sqlite3
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATABASE_PATH = os.path.join(PROJECT_ROOT, 'database', 'university.db')
SCHEMA_FILE = "university.sql"
DATABASE = f"sqlite:///{DATABASE_PATH}"


def create_database(db_name, schema_file):
    """
    Create a SQLite database using the provided schema file.

    Args:
        db_name (str): The name of the SQLite database.
        schema_file (str): The path to the SQL schema file.

    Returns:
        None
    """
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()

            with open(schema_file) as file:
                schema_script = file.read()
                cursor.executescript(schema_script)
                conn.commit()

        logger.info(f"Database '{db_name}' created from '{schema_file}' successfully.")
    except Exception as e:
        logger.error(f"Error creating database: {e}")


# Usage
if __name__ == "__main__":
    create_database(DATABASE_PATH, SCHEMA_FILE)
