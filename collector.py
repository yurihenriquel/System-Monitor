import psutil
import time
import requests
from datetime import datetime

API_URL = "http://api:5000/metrics"

def collect_metrics():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent
    }

while True:
    metrics = collect_metrics()
    print(metrics)
    try:
        requests.post(API_URL, json=metrics)
    except Exception as e:
        print("Erro ao enviar métricas:", e)
    time.sleep(5)