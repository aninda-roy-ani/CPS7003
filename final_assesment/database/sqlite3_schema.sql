-- Users Table
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role_id INTEGER,
    FOREIGN KEY (role_id) REFERENCES Roles(role_id)
);

-- Roles Table
CREATE TABLE IF NOT EXISTS Roles (
    role_id INTEGER PRIMARY KEY,
    role_name TEXT NOT NULL
);

-- Patients Table
CREATE TABLE IF NOT EXISTS Patients (
    patient_id INTEGER PRIMARY KEY,
    patient_name TEXT NOT NULL,
    date_of_birth DATE,
    gender TEXT,
    contact_information TEXT
);

-- Medical History Table
CREATE TABLE IF NOT EXISTS Medical_History (
    history_id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    admission_date DATE,
    discharge_date DATE,
    diagnosis TEXT,
    medical_notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Treatment Plan Table
CREATE TABLE IF NOT EXISTS Treatment_Plan (
    treatment_id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    treatment_details TEXT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Diagnosis Plan Table
CREATE TABLE IF NOT EXISTS Diagnosis_Plan (
    diagnosis_id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    diagnosis_details TEXT,
    diagnosis_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Treatment Team Assignment Table
CREATE TABLE IF NOT EXISTS Treatment_Team_Assignment (
    assignment_id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    user_id INTEGER,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
