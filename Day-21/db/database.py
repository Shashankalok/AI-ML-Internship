import sqlite3

# Create connection
conn = sqlite3.connect("patients.db", check_same_thread=False)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    heart_rate INTEGER,
    oxygen_level INTEGER,
    risk_score INTEGER,
    status TEXT,
    timestamp TEXT
)
""")

conn.commit()