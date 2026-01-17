from flask import Flask
from api.routes import metrics_bp

app = Flask(__name__)

app.register_blueprint(metrics_bp)

if __name__ == "__main__":
    app.run(debug=True)