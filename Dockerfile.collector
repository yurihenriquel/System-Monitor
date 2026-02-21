FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install psutil requests

CMD ["python", "collector.py"]