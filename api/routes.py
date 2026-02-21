from flask import Blueprint, jsonify

api = Blueprint("api", __name__, url_prefix="/api/v1")

@api.route("/health", methods=["GET"])
def health():
    return jsonify({
        "ststus": "success",
        "message": "API funcionando corretamente"
    }), 200