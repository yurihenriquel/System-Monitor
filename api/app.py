from flask import Flask
from api.routes import api
from api.database import init_db

app = Flask(__name__)

init_db()

app.register_blueprint(api, url_prefix="/api/v1")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)