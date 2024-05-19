-- Staff Members Table
CREATE TABLE IF NOT EXISTS Staff_member (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL UNIQUE,
    Password TEXT NOT NULL,
    First_name TEXT NOT NULL,
    Last_name TEXT NOT NULL,
    Role TEXT NOT NULL CHECK(Role IN ('Physician', 'Nurse', 'Moderator'))
);

-- Physicians Table
CREATE TABLE IF NOT EXISTS Physician (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Staff_member_id INTEGER NOT NULL,
    Specialty TEXT NOT NULL,
    Department TEXT NOT NULL,
    FOREIGN KEY (Staff_member_id) REFERENCES Staff_member (Id) ON DELETE CASCADE
);

-- Nurses Table
CREATE TABLE IF NOT EXISTS Nurse (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Staff_member_id INTEGER NOT NULL,
    Department TEXT NOT NULL,
    FOREIGN KEY (Staff_member_id) REFERENCES Staff_member (Id) ON DELETE CASCADE
);

-- Moderators Table
CREATE TABLE IF NOT EXISTS Moderator (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Staff_member_id INTEGER NOT NULL,
    FOREIGN KEY (Staff_member_id) REFERENCES Staff_member (Id) ON DELETE CASCADE
);

-- Staff Roles Table
CREATE TABLE IF NOT EXISTS Staff_role (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL UNIQUE
);

-- Patients Table
CREATE TABLE IF NOT EXISTS Patient (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    First_name TEXT NOT NULL,
    Last_name TEXT NOT NULL,
    Date_of_birth DATE NOT NULL,
    Gender TEXT NOT NULL,
    Contact_information TEXT NOT NULL
);

-- Medical Histories Table
CREATE TABLE IF NOT EXISTS Medical_history (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Patient_id INTEGER NOT NULL,
    Description TEXT NOT NULL,
    Date DATE NOT NULL,
    FOREIGN KEY (Patient_id) REFERENCES Patient (Id) ON DELETE CASCADE
);

-- Treatment Plans Table
CREATE TABLE IF NOT EXISTS Treatment_plan (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Patient_id INTEGER NOT NULL,
    Description TEXT NOT NULL,
    Start_date DATE NOT NULL,
    End_date DATE,
    FOREIGN KEY (Patient_id) REFERENCES Patient (Id) ON DELETE CASCADE
);

-- Diagnostic Reports Table
CREATE TABLE IF NOT EXISTS Diagnostic_report (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Patient_id INTEGER NOT NULL,
    Report TEXT NOT NULL,
    Date DATE NOT NULL,
    FOREIGN KEY (Patient_id) REFERENCES Patient (Id) ON DELETE CASCADE
);

-- Treatment Team Assignments Table
CREATE TABLE IF NOT EXISTS Treatment_team_assignment (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Treatment_plan_id INTEGER NOT NULL,
    Staff_member_id INTEGER NOT NULL,
    Role_id INTEGER NOT NULL,
    FOREIGN KEY (Treatment_plan_id) REFERENCES Treatment_plan (Id) ON DELETE CASCADE,
    FOREIGN KEY (Staff_member_id) REFERENCES Staff_member (Id) ON DELETE CASCADE,
    FOREIGN KEY (Role_id) REFERENCES Staff_role (Id) ON DELETE CASCADE
);
