from week4.database_layer import create_database as database
import sqlite3


# CREATE

def create_subject(title, subject_leader):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "INSERT INTO Subject (Title, SubjectLeader) VALUES (?,?)"
    params = (title, subject_leader)
    result = cursor.execute(query, params)

    conn.commit()
    conn.close()

    if result.rowcount > 0:
        return cursor.lastrowid
    else:
        return False


# READ

def get_subject(subject_id):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "SELECT * FROM Subject WHERE ID=?"
    params = (subject_id,)
    cursor.execute(query, params)
    subject = cursor.fetchone()

    conn.close()
    return subject

def get_subject_with_subject_leader(subject_leader):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "SELECT * FROM Subject WHERE SubjectLeader=?"
    params = (subject_leader,)
    cursor.execute(query, params)
    subject = cursor.fetchall()

    conn.close()
    return subject


def get_all_subjects():
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "SELECT * FROM Subject"
    cursor.execute(query)
    subjects = cursor.fetchall()

    conn.close()
    return subjects


# UPDATE

def update_subject(subject_id, new_subject_name, new_subject_leader):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "UPDATE Subject SET Title=?, SubjectLeader=? WHERE ID=?"
    params = (new_subject_name, new_subject_leader, subject_id)
    result = cursor.execute(query, params)

    conn.commit()
    conn.close()

    if result.rowcount > 0:
        return True
    else:
        return False


# DELETE

def delete_subject(subject_id):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "DELETE FROM Subject WHERE ID=?"
    params = (subject_id,)
    result = cursor.execute(query, params)

    conn.commit()
    conn.close()

    if result.rowcount > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    #create_subject("Computer Science",1)
    update_subject(1,"DATABASE", 1)
    print(get_all_subjects())