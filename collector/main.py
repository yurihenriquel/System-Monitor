import requests
from cpu import get_cpu_usage
from memory import get_memory_usage
from disk import get_disk_usage

API_URL = "http://api:5000/api/v1/metrics"

def send_metrics():
    data = {
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage()
    }

    response = requests.post(API_URL, json=data)
    print("Status:", response.status_code)

if __name__ == "__main__":
    send_metrics()