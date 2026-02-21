from flask import Flask
import logging

from api.database import init_db
from api.routes import register_routes


def create_app():
    app = Flask(__name__)

    # configurar logger
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Inicializando banco de dados")
    init_db()

    register_routes(app)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)