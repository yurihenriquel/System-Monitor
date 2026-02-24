from flask import Blueprint, request, jsonify
from api.database import get_connection

api = Blueprint("api", __name__)

@api.route("/metrics", methods=["POST"])
def save_metrics():
    data = request.json

    cpu = data.get("cpu")
    memory = data.get("memory")
    disk = data.get("disk")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO metrics (cpu, memory, disk)
        VALUES (?, ?, ?)
    """, (cpu, memory, disk))

    conn.commit()
    conn.close()

    return jsonify({
        "status": "success",
        "message": "Métricas salvas com sucesso"
    }), 201