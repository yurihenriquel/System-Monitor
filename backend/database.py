import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "metrics.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    schema_path = BASE_DIR / "schema.sql"

    with open(schema_path, "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()