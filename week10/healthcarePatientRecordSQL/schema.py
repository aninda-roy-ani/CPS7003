import sqlite3
import os

conn = sqlite3.connect('healthcare.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS patients (
id INTEGER PRIMARY KEY,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
dob DATE NOT NULL,
gender TEXT NOT NULL,
diagnosis TEXT NOT NULL)''')

patients = [
    (1, 'Jeremy', 'Morley', '1985-05-25', 'M', 'Asthma'),
    (2, 'Marla', 'Boston', '1956-08-12', 'F', 'Rheumatisam'),
    (3, 'Adele', 'St Esprit', '1933-05-16', 'F', 'Hypertension')
]

cur.executemany('INSERT OR IGNORE INTO patients VALUES (?,?,?,?,?,?)', patients)

conn.commit()

cur.execute('SELECT * FROM patients')
all_patients = cur.fetchall()
print("ALL PATIENTS: ")
for p in patients:
    print(p)
print("")

cur.execute("SELECT * FROM patients WHERE diagnosis = 'Asthma'")
d_patients = cur.fetchall()
print("ASTHMA PATIENTS: ")
for p in d_patients:
    print(p)
print("")

cur.execute("SELECT gender, COUNT(*) FROM patients GROUP BY GENDER")
gender_count = cur.fetchall()
print("PATIENTS BY GENDER: ")
for g in gender_count:
    print(g)

conn.close()

os.remove('healthcare.db')