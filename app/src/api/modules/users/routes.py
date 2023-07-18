from . import users_blueprint  # noreorder # NOQA
from flask import jsonify
from src.api.adapters import HttpAdapter
from src.api.adapters import HttpResponse
from src.api.modules.users.services import AuthService


auth_service = AuthService(app="app")


@users_blueprint.route("/")
def index():
    return jsonify("users route")


@users_blueprint.route("/login", methods=["POST"])
def login():
    data = HttpAdapter.get_request_data()

    username = data.body.get("username")
    password = data.body.get("password")

    if user := auth_service.authenticate_user(username, password):
        access_token = auth_service.create_access_token(user)

        # Create an HTTP response using the HttpAdapter
        response_data = {"access_token": access_token}
        return HttpAdapter.make_response(HttpResponse(data=response_data))
    # Create an HTTP response for invalid credentials
    response_data = {"message": "Invalid credentials"}
    return HttpAdapter.make_response(HttpResponse(data=response_data, status_code=401))
