import sqlite3

# Global variable
DATABASE_NAME = "university.db"


# Functions
def create_database(db_name, schema_file):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    with open(schema_file) as file:
        schema_script = file.read()
        cursor.executescript(schema_script)
        conn.commit()

    conn.close()


# Usage
if __name__ == "__main__":
    schema_file = "schema.sql"
    create_database(DATABASE_NAME, schema_file)
    print(f"Database '{DATABASE_NAME}' created from '{schema_file}' successfully.")