import sqlite3
from pathlib import Path

DATA_DIR = Path("/app/data")
DB_PATH = DATA_DIR / "monitor.db"
SCHEMA_PATH = Path(__file__).parent / "schema.sql"

def get_connection():
    DATA_DIR.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    with open(SCHEMA_PATH, "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()