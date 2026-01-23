from flask import Flask, request, jsonify
from api.database import init_db, get_connection

def create_app():
    app = Flask(__name__)

    init_db()

    @app.route("/metrics", methods=["POST"])
    def receive_metrics():
        data = request.json

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO metrics (cpu, memory, disk, timestamp)
            VALUES (?, ?, ?, ?)
            """,
            (
                data["cpu"],
                data["memory"],
                data["disk"],
                data["timestamp"],
            ),
        )
    
        conn.commit()
        conn.close()

        return jsonify({"status": "ok"}), 201

    @app.route("/metrics", methods=["GET"])
    def list_metrics():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM metrics")
        rows = cursor.fetchall()

        conn.close()

        return jsonify(rows)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)