import requests
import time
import psutil
from datetime import datetime

API_URL = "http://api:5000/api/v1/metrics"

while True:
    data = {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
        "timestamp": datetime.utcnow().isoformat()
    }

    print("Enviando:", data)

    requests.post(API_URL, json=data)

    time.sleep(5)