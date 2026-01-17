import psutil
import time
from datetime import datetime
from backend.database import init_db, get_connection


def collect_cpu_usage():
    return psutil.cpu_percent(interval=1)


def collect_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent


def save_metrics(metrics):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO metrics (cpu_percent, memory_percent)
    VALUES (?, ?)
""", (
    metrics["cpu_percent"],
    metrics["memory_percent"]
))

    conn.commit()
    conn.close()


def collect_metrics():
    timestamp = datetime.now().isoformat()

    data = {
        "timestamp": timestamp,
        "cpu_percent": collect_cpu_usage(),
        "memory_percent": collect_memory_usage()
    }

    return data


if __name__ == "__main__":
    init_db()

    while True:
        metrics = collect_metrics()
        save_metrics(metrics)
        print(metrics)
        time.sleep(5)
