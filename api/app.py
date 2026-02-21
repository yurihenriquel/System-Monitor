from flask import Flask
from api.routes import api
from api.config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(api)


@app.errorhandler(404)
def not_found(error):
    return {
        "status": "error",
        "message": "Rota não encontrada"
    }, 404


@app.errorhandler(500)
def internal_error(error):
    return {
        "status": "error",
        "message": "Erro interno do servidor"
    }, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config["PORT"])