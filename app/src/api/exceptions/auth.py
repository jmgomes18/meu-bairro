class AuthError(Exception):
    def __init__(self, error: str, status_code: int = 401) -> None:
        self.error = error
        self.status_code = status_code
