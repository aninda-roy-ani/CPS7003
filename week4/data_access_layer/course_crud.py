from week4.database_layer import create_database as database
import sqlite3


# CREATE

def create_course(award, title, course_leader, subject_id):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "INSERT INTO Course (Award, Title, CourseLeader, SubjectID) VALUES (?, ?, ?, ?)"
    params = (award, title, course_leader, subject_id)
    result = cursor.execute(query, params)

    conn.commit()
    conn.close()

    if result.rowcount > 0:
        return cursor.lastrowid
    else:
        return False


# READ

def get_course(course_id):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "SELECT * FROM Course WHERE CourseID=?"
    params = (course_id,)
    cursor.execute(query, params)
    course = cursor.fetchone()

    conn.close()
    return course


def get_courses_with_course_leader(course_leader):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "SELECT * FROM Course WHERE CourseLeader = ?"
    params = (course_leader,)
    cursor.execute(query, params)
    courses = cursor.fetchall()

    conn.close()
    return courses


def get_all_courses():
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "SELECT * FROM Course"
    cursor.execute(query)
    courses = cursor.fetchall()

    conn.close()
    return courses


# UPDATE

def update_course(course_id, award, title, course_leader, subject_id):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "UPDATE Course SET Award=?, Title=?, CourseLeader=?, SubjectID=? WHERE ID=?"
    params = (award, title, course_leader, subject_id, course_id)
    result = cursor.execute(query, params)

    conn.commit()
    conn.close()

    if result.rowcount > 0:
        return True
    else:
        return False


# DELETE

def delete_course(course_id):
    conn = sqlite3.connect(database.DATABASE_NAME)
    cursor = conn.cursor()

    query = "DELETE FROM Course WHERE ID=?"
    params = (course_id,)
    result = cursor.execute(query, params)

    conn.commit()
    conn.close()

    if result.rowcount > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    #create_course("Masters","Computer Science", "Prins", 1)
    print(get_all_courses())
