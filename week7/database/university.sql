
CREATE TABLE IF NOT EXISTS Role (
    RoleID INTEGER PRIMARY KEY AUTOINCREMENT,
    RoleName TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS User (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    RoleID INTEGER NOT NULL,
    FOREIGN KEY (RoleID) REFERENCES Role(RoleID)
);

CREATE TABLE IF NOT EXISTS Subject (
    SubjectID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    SubjectLeader INTEGER NOT NULL,
    FOREIGN KEY (SubjectLeader) REFERENCES User(UserID)
);

CREATE TABLE IF NOT EXISTS Course (
    CourseID INTEGER PRIMARY KEY AUTOINCREMENT,
    Award TEXT NOT NULL,
    Title TEXT NOT NULL,
    CourseLeader INTEGER NOT NULL,
    SubjectID INTEGER NOT NULL,
    FOREIGN KEY (CourseLeader) REFERENCES User(UserID),
    FOREIGN KEY (SubjectID) REFERENCES Subject(SubjectID)
);

CREATE TABLE IF NOT EXISTS Module (
    ModuleID INTEGER PRIMARY KEY AUTOINCREMENT,
    Code TEXT NOT NULL,
    Title TEXT NOT NULL,
    Level INTEGER NOT NULL,
    ModuleLeader INTEGER NOT NULL,
    CourseID INTEGER NOT NULL,
    FOREIGN KEY (ModuleLeader) REFERENCES User(UserID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);

CREATE TABLE IF NOT EXISTS Module_Tutor (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER NOT NULL,
    ModuleID INTEGER NOT NULL,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (ModuleID) REFERENCES Module(ModuleID)
);

CREATE TABLE IF NOT EXISTS Auth (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL
)

