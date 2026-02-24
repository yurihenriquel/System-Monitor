import os

class Config:
    DB_PATH = os.getenv("DB_PATH", "data/monitor.db")