from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
