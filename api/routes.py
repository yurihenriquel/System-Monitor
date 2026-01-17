from flask import Blueprint, jsonify
from backend.database import get_connection

metrics_bp = Blueprint("/metrics", __name__)

@metrics_bp.route("/metrics", methods=["GET"])
def get_metrics():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            created_at,
            cpu_percent,
            memory_percent,
            disk_percent
        FROM metrics
        ORDER BY created_at DESC
        LIMIT 10
""")

    rows = cursor.fetchall()
    conn.close()

    data = [
        {
            "created_ate": row[0],
            "cpu_percent": row[1],
            "memory_percent": row[2],
            "disk_percent": row[3],
        }
        for row in rows
    ]
    return jsonify(data)