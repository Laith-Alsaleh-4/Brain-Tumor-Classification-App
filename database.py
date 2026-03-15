import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('patients_data.db')
    c = conn.cursor()
    # Make sure all required columns are present
    c.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id TEXT PRIMARY KEY,
            name TEXT,
            diagnosis TEXT,
            confidence REAL,
            date TEXT,
            image_path TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_patient_record(p_id, p_name, p_diagnosis, p_confidence, p_image_path):
    conn = sqlite3.connect('patients_data.db')
    c = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute('''
        INSERT OR REPLACE INTO patients (id, name, diagnosis, confidence, date, image_path)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (p_id, p_name, p_diagnosis, p_confidence, now, p_image_path))
    conn.commit()
    conn.close()

# This is the function that was missing and caused the error.
def get_patient_by_id(p_id):
    conn = sqlite3.connect('patients_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM patients WHERE id = ?', (p_id,))
    data = c.fetchone()
    conn.close()
    return data