CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT UNIQUE,
    phone_number TEXT,
    hire_date DATE,
    job_title TEXT,
    salary REAL
);
CREATE TABLE job_title (
    job_title_id INTEGER PRIMARY KEY,
    title_name TEXT,
    description TEXT,
    base_salary REAL
);
CREATE TABLE location (
    location_id INTEGER PRIMARY KEY,
    city TEXT,
    state TEXT,
    country TEXT
);
CREATE TABLE task (
    task_id INTEGER PRIMARY KEY,
    task_name TEXT,
    description TEXT
);
CREATE TABLE employee_task (
    employee_id INTEGER
    task_id INTEGER
);
CREATE TABLE department (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT,
    manager_id INTEGER,
    location_id INTEGER
);
