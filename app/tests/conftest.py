import pytest
from src import create_app

@pytest.fixture(scope="module")
def setup():
    app = create_app()
    app.config.from_object('src.config.TestingConfig')

    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens!

