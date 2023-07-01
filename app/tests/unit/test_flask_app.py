from src import create_app
from src.database.database import db


def test_home_page(setup):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    flask_app = create_app()

    flask_app.config.from_object("src.config.TestingConfig")

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get("/")
        assert response.status_code == 200


def test_database_connection(setup):
    flask_app = create_app()
    flask_app.config.from_object("src.config.TestingConfig")

    with flask_app.test_client():
        db.create_all()
        connection = db.engine.connect()
        assert connection
        connection.close()
        db.drop_all()
