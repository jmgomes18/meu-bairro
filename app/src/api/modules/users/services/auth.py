from logging import Logger

from flask_jwt_extended import create_access_token
from src.api.exceptions import AuthError

logger = Logger("auth_service")


class AuthService:
    def __init__(self, app) -> None:
        self.app = app
        # self.config = config
        # self.oauth = OAuth(app)
        # self.auth_domain = os.environ.get("AUTH_DOMAIN")
        # self.auth0 = self.oauth.register(
        #     "auth0",
        #     client_id=os.environ.get("CLIENT_ID"),
        #     client_secret=os.environ.get("AUTH_SECRET"),
        #     api_base_url=f"https://{self.auth_domain}",
        #     access_token_url=f"https://{self.auth_domain}/oauth/token",
        #     authorize_url=f"https://{self.auth_domain}/authorize",
        #     client_kwargs={"scope": "openid profile email"},
        # )

        # self.jwt = JWTManager(app)

        # @self.jwt.unauthorized_loader
        def unauthorized_callback(error):
            return AuthError(error="Invalid token")

    def authenticate_user(self, username, password):
        # Your authentication logic goes here
        # Validate the user's credentials and return the user object if authenticated.
        # For demonstration purposes, we'll use a dummy user object.
        if username == "user" and password == "pass":
            return {"id": 1, "username": "user"}

        return None

    def create_access_token(self, user):
        return create_access_token(identity=user["id"])
