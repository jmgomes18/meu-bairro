from src import create_app

def test_home_page(setup):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    flask_app = create_app()
    
    flask_app.config.from_object('src.config.TestingConfig')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200