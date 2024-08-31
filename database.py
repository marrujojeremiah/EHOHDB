import sqlite3

def connect_db():
    return sqlite3.connect("client_db.sqlite3")

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Clients table
    cursor.execute('''CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        dob DATE,
        age INTEGER,
        weight REAL,
        ssn TEXT,
        diagnosis TEXT
    )''')
    
    # Doctors table
    cursor.execute('''CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY,
        client_id INTEGER,
        doctor_name TEXT,
        FOREIGN KEY(client_id) REFERENCES clients(id)
    )''')
    
    # Appointments table
    cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY,
        client_id INTEGER,
        appointment_date DATE,
        purpose TEXT,
        doctor_name TEXT,
        FOREIGN KEY(client_id) REFERENCES clients(id)
    )''')
    
    # Behaviors table
    cursor.execute('''CREATE TABLE IF NOT EXISTS behaviors (
        id INTEGER PRIMARY KEY,
        client_id INTEGER,
        behavior TEXT,
        duration INTEGER,
        behavior_date DATE,
        resolution TEXT,
        FOREIGN KEY(client_id) REFERENCES clients(id)
    )''')
    
    # AWOL table
    cursor.execute('''CREATE TABLE IF NOT EXISTS awol (
        id INTEGER PRIMARY KEY,
        client_id INTEGER,
        awol_date DATE,
        awol_time TEXT,
        cause TEXT,
        resolution TEXT,
        FOREIGN KEY(client_id) REFERENCES clients(id)
    )''')
    
    # Medications table
    cursor.execute('''CREATE TABLE IF NOT EXISTS medications (
        id INTEGER PRIMARY KEY,
        client_id INTEGER,
        medication TEXT,
        dosage TEXT,
        time TEXT,
        FOREIGN KEY(client_id) REFERENCES clients(id)
    )''')
    
    conn.commit()
    conn.close()

def get_clients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, first_name, last_name, dob, age, weight, ssn, diagnosis FROM clients")
    clients = cursor.fetchall()
    conn.close()
    return clients

def get_appointments():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT client_id, appointment_date, purpose, doctor_name FROM appointments")
    appointments = cursor.fetchall()
    conn.close()
    return appointments

def get_behaviors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT client_id, behavior_date, behavior, duration, resolution FROM behaviors")
    behaviors = cursor.fetchall()
    conn.close()
    return behaviors

def get_awol():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT client_id, awol_date, awol_time, cause, resolution FROM awol")
    awol_records = cursor.fetchall()
    conn.close()
    return awol_records

def get_medications():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT client_id, medication, dosage, time FROM medications")
    medications = cursor.fetchall()
    conn.close()
    return medications

def search_clients(first_name, last_name, dob):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, first_name, last_name, dob, age, weight, ssn, diagnosis FROM clients WHERE first_name=? AND last_name=? AND dob=?", 
                   (first_name, last_name, dob))
    results = cursor.fetchall()
    conn.close()
    return results
