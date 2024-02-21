from week4.database_layer import create_database as database
import sqlite3


# CREATE

def create_role(role_name):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "INSERT INTO Role (RoleName) VALUES (?)"
    params = (role_name,)
    result = cursor.execute(query, params)

    conn.commit()
    conn.close()

    if result.rowcount > 0:
        return cursor.lastrowid
    else:
        return False


# READ

def get_role(role_id):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "SELECT * FROM Role WHERE RoleID=?"
    params = (role_id,)
    cursor.execute(query, params)
    role = cursor.fetchone()

    conn.close()
    return role

def get_role_by_name(role_name):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "SELECT * FROM Role WHERE RoleName=?"
    params = (role_name,)
    cursor.execute(query,params)
    role = cursor.fetchall()

    conn.close()
    return role

def get_all_roles():
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "SELECT * FROM Role"
    cursor.execute(query)
    roles = cursor.fetchall()

    conn.close()
    return roles


# UPDATE

def update_role(role_id, new_role_name):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "UPDATE Role SET RoleName=? WHERE RoleID=?"
    params = (new_role_name, role_id)
    result = cursor.execute(query, params)

    conn.commit()
    conn.close()

    if result.rowcount > 0:
        return True
    else:
        return False


# DELETE

def delete_role(role_id):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "DELETE FROM Role WHERE RoleID=?"
    params = (role_id,)
    result = cursor.execute(query, params)

    conn.commit()
    conn.close()

    if result.rowcount > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    #create_role("STAFF")
    #update_role(1, "ROLE_STUDENT")
    #delete_role(2)
    print(get_all_roles())