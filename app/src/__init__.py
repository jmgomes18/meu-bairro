from flask import Flask
from src.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from src.database.database import db
    db.init_app(app)
    
    register_blueprints(app)

    return app

def register_blueprints(app):
    from src.api.modules.users import users_blueprint
    app.register_blueprint(users_blueprint)