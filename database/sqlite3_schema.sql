
CREATE TABLE IF NOT EXISTS Employee (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    role_id INTEGER,
    FOREIGN KEY (role_id) REFERENCES Roles(role_id)
);

-- Roles Table
CREATE TABLE IF NOT EXISTS Role (
    role_id INTEGER PRIMARY KEY AUTOINCREMENT,
    role_name TEXT UNIQUE NOT NULL
);

-- Patients Table
CREATE TABLE IF NOT EXISTS Patient (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT NOT NULL,
    date_of_birth DATE,
    gender TEXT,
    contact_no TEXT,
    address TEXT
);

-- Medical History Table
CREATE TABLE IF NOT EXISTS Medical_History (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    admission_date DATE,
    discharge_date DATE,
    diagnosis TEXT,
    medical_notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Treatment Plan Table
CREATE TABLE IF NOT EXISTS Treatment_Plan (
    treatment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    diagnosis_id INTEGER NOT NULL,
    treatment_details TEXT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (diagnosis_id) REFERENCES Diagnosis(diagnosis_id)
);

-- Diagnosis Plan Table
CREATE TABLE IF NOT EXISTS Diagnosis (
    diagnosis_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    diagnosis_details TEXT,
    diagnosis_date DATE,
    result TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Treatment Team Assignment Table
CREATE TABLE IF NOT EXISTS Treatment_Team_Assignment (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    treatment_id INTEGER NOT NULL,
    employee_id INTEGER,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (treatment_id) REFERENCES Treatment_Plan(treatment_id),
    FOREIGN KEY (user_id) REFERENCES Employee(employee_id)
);
