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

def add_client(first_name, last_name, dob, age, weight, ssn, diagnosis):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clients (first_name, last_name, dob, age, weight, ssn, diagnosis) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (first_name, last_name, dob, age, weight, ssn, diagnosis))
    client_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return client_id

def add_doctor(client_id, doctor_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO doctors (client_id, doctor_name) VALUES (?, ?)", (client_id, doctor_name))
    conn.commit()
    conn.close()

def add_appointment(client_id, appointment_date, purpose, doctor_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO appointments (client_id, appointment_date, purpose, doctor_name) VALUES (?, ?, ?, ?)",
                   (client_id, appointment_date, purpose, doctor_name))
    conn.commit()
    conn.close()

def add_behavior(client_id, behavior, duration, behavior_date, resolution):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO behaviors (client_id, behavior, duration, behavior_date, resolution) VALUES (?, ?, ?, ?, ?)",
                   (client_id, behavior, duration, behavior_date, resolution))
    conn.commit()
    conn.close()

def add_awol(client_id, awol_date, awol_time, cause, resolution):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO awol (client_id, awol_date, awol_time, cause, resolution) VALUES (?, ?, ?, ?, ?)",
                   (client_id, awol_date, awol_time, cause, resolution))
    conn.commit()
    conn.close()

def add_medication(client_id, medication, dosage, time):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO medications (client_id, medication, dosage, time) VALUES (?, ?, ?, ?)",
                   (client_id, medication, dosage, time))
    conn.commit()
    conn.close()

# Create the tables
create_tables()

# Insert Client 1
client_id = add_client("Emily", "Johnson", "1990-04-12", 34, 135, "123-45-6789", "Anxiety Disorder")
add_doctor(client_id, "Dr. Sarah Thompson")
add_appointment(client_id, "2024-09-15", "Routine Checkup", "Dr. Sarah Thompson")
add_behavior(client_id, "Panic Attack", 15, "2024-08-20", "Breathing exercises")
add_awol(client_id, "2024-07-10", "14:00", "Overwhelmed", "Returned voluntarily")
add_medication(client_id, "Zoloft", "50 mg", "8:00 AM")

# Insert Client 2
client_id = add_client("Sarah", "Williams", "1985-11-22", 38, 150, "234-56-7890", "Bipolar Disorder")
add_doctor(client_id, "Dr. Michael Brown")
add_appointment(client_id, "2024-10-05", "Medication Review", "Dr. Michael Brown")
add_behavior(client_id, "Aggressive Outburst", 30, "2024-08-18", "Counseling session")
add_awol(client_id, "2024-07-18", "19:00", "Anger", "Found by staff")
add_medication(client_id, "Lithium", "300 mg", "9:00 AM")

# Insert Client 3
client_id = add_client("Olivia", "Davis", "1992-06-30", 32, 125, "345-67-8901", "Schizophrenia")
add_doctor(client_id, "Dr. James Miller")
add_appointment(client_id, "2024-09-22", "Therapy Session", "Dr. James Miller")
add_behavior(client_id, "Hallucinations", 45, "2024-08-22", "Medication adjustment")
add_awol(client_id, "2024-07-25", "21:00", "Delusions", "Returned by police")
add_medication(client_id, "Risperidone", "2 mg", "7:00 AM")

# Insert Client 4
client_id = add_client("Isabella", "Martinez", "1988-02-14", 36, 140, "456-78-9012", "Obsessive-Compulsive Disorder (OCD)")
add_doctor(client_id, "Dr. Rachel Wilson")
add_appointment(client_id, "2024-08-30", "Cognitive Behavioral Therapy (CBT)", "Dr. Rachel Wilson")
add_behavior(client_id, "Compulsive Cleaning", 60, "2024-08-25", "Distraction techniques")
add_awol(client_id, "2024-06-12", "11:00", "Anxiety", "Returned voluntarily")
add_medication(client_id, "Prozac", "20 mg", "8:00 AM")

# Insert Client 5
client_id = add_client("Mia", "Rodriguez", "1995-03-08", 29, 160, "567-89-0123", "Major Depressive Disorder")
add_doctor(client_id, "Dr. John Smith")
add_appointment(client_id, "2024-09-10", "Depression Assessment", "Dr. John Smith")
add_behavior(client_id, "Self-Isolation", 90, "2024-08-15", "Peer support")
add_awol(client_id, "2024-07-28", "16:00", "Depression", "Found by family")
add_medication(client_id, "Sertraline", "100 mg", "10:00 AM")

# Insert Client 6
client_id = add_client("Ava", "Garcia", "1993-09-05", 31, 145, "678-90-1234", "Borderline Personality Disorder (BPD)")
add_doctor(client_id, "Dr. Laura Johnson")
add_appointment(client_id, "2024-10-12", "Emotional Regulation Therapy", "Dr. Laura Johnson")
add_behavior(client_id, "Mood Swings", 20, "2024-08-27", "Dialectical Behavior Therapy (DBT)")
add_awol(client_id, "2024-06-30", "18:00", "Emotional distress", "Returned by staff")
add_medication(client_id, "Lamotrigine", "25 mg", "12:00 PM")
