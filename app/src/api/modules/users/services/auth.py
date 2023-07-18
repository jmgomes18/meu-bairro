from logging import Logger
from typing import Dict

from src.api.exceptions import AuthError
from src.api.modules.users.infra import UserRepository

logger = Logger("auth_service")


class AuthService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def get_token_auth_header(self, headers: Dict):
        """
        Obtains the Access Token from the Authorization Header
        """
        try:
            auth = headers.get("Authorization")

            if not auth:
                raise AuthError(error="Authorization header missing")

            parts = auth.split()

            if parts[0].lower() != "bearer":
                raise AuthError(error="Authorization header must start with Bearer")

            elif len(parts) == 1:
                raise AuthError(error="Token not found")

            elif len(parts) > 2:
                raise AuthError(error="Authorization header must be <Bearer> + <Token>")

            return parts[1]
        except Exception as e:
            logger.error(f"{e}")
            return {
                "status_code": 500,
                "message": "Something is wrong, please try again",
            }
