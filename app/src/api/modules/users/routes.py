from flask import jsonify
from . import users_blueprint

@users_blueprint.route('/')
def index():
    return jsonify('users route')
