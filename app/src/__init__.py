from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy()
migrate = Migrate()
flask_bcrypt = Bcrypt()


@app.route("/")
def hello_world():
    return jsonify(hello="world")