import os

class Config:
    FLASK_ENV = os.getenv("FLASK_ENV", "production")
    DEBUG = os.getenv("FLASK_DEBUG", "False") == "True"
    PORT = int(os.getenv("PORT", 5000))
    DB_PATH = os.getenv("DB_PATH", "data/monitor.db")