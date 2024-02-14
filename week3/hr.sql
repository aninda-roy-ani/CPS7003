
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
CREATE TABLE department (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT,
    manager_id INTEGER,
    location_id INTEGER,
    FOREIGN KEY (location_id) REFERENCES location(location_id)
);
CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT UNIQUE,
    phone_number TEXT,
    hire_date DATE,
    job_title TEXT,
    salary REAL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES department(department_id)
);
CREATE TABLE employee_task (
    employee_id INTEGER,
    task_id INTEGER,
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
    FOREIGN KEY (task_id) REFERENCES task(task_id)
);
CREATE TABLE category (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT UNIQUE
);
ALTER TABLE task
ADD COLUMN category_id INTEGER,
ADD CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES category(category_id);

