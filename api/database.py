import sqlite3
from pathlib import Path
from api.config import DB_NAME

DATA_DIR = Path("/app/data")
SCHEMA_PATH = Path(__file__).parent / "schema.sql"


def get_connection():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DATA_DIR / DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    with open(SCHEMA_PATH, "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()