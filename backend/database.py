import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "database" / "monitor.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        schema_path = Path(__file__).resolve().parent.parent / "database" / "schema.sql"
        with open(schema_path) as f:
            cursor.executescript(f.read())
        conn.commit()