import pytest
from src import create_app
from src.database.database import db
from src.database.entities import Users


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object("src.config.TestingConfig")

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope="function")
def test_client(test_app):
    return test_app.test_client()


@pytest.fixture(scope="function")
def base_user(test_client):
    user = Users(
        email="test@example.com",
        password="test_pass",
        is_active=True,
        is_company="Company",
    )
    db.session.add(user)
    db.session.commit()
    yield user
    db.session.delete(user)
    db.session.commit()
    db.session.close()


def test_create_user(test_client):
    user = Users(
        email="test@example.com",
        password="test_pass",
        is_active=True,
        is_company="Company",
    )
    db.session.add(user)

    retrieved_user = db.session.query(Users).filter_by(email="test@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.email == "test@example.com"
    db.session.close()


def test_read_user(base_user):
    retrieved_user = db.session.query(Users).filter_by(email="test@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.email == "test@example.com"


def test_update_user(base_user):
    base_user.is_active = False
    db.session.commit()

    updated_user = db.session.query(Users).filter_by(email="test@example.com").first()
    assert updated_user is not None
    assert not updated_user.is_active


def test_delete_user(base_user):
    db.session.delete(base_user)
    db.session.commit()

    deleted_user = db.session.query(Users).filter_by(email="test@example.com").first()
    assert deleted_user is None
