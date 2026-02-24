from flask import Blueprint, request, jsonify
from api.database import get_connection

api = Blueprint("api", __name__)


@api.route("/metrics", methods=["POST"])
def create_metrics():
    data = request.get_json()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO metrics (cpu, memory, disk)
        VALUES (?, ?, ?)
        """,
        (data["cpu"], data["memory"], data ["disk"])
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Metrics saved"}), 201

@api.route("/metrics", methods=["GET"])
def get_metrics():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM metrics ORDER BY id DESC")
    rows = cursor.fetchall()

    conn.close()

    metrics = []

    for row in rows:
        metrics. append({
            "id": row["id"],
            "cpu": row["cpu"],
            "memory": row["memory"],
            "disk": row["disk"],
            "created_at": row["created_at"],            
        })

    return jsonify(metrics), 200