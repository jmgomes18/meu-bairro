from src import create_app
from src.database.entities import Users

class TestUsers:

    def test_password_hashing(self, setup):
        flask_app = create_app()
        with flask_app.test_client():
            user = Users()
            password = "my_password"
            user.password = password
            assert user.check_password(password)

    def test_password_check(self, setup):
        flask_app = create_app()
        with flask_app.test_client():
            user = Users()
            password = "my_password"
            wrong_password = "wrong_password"
            user.password = password
            assert user.check_password(password)
            assert not user.check_password(wrong_password)