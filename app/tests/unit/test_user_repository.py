from uuid import uuid4

import pytest
from src.api.modules.users.dto import UserDTO
from src.api.modules.users.infra import UserRepository
from src.database.database import db
from src.database.models import Users


@pytest.fixture()
def mock_user_dto():
    yield UserDTO(
        id=str(uuid4()),
        email="test@email.com",
        password="teste",
        is_active=True,
        is_company=False,
    )


def test_create_user(setup, mock_user_dto):
    repository = UserRepository()

    created_user = repository.create(mock_user_dto)

    assert str(created_user.id) == mock_user_dto.id  # type: ignore
    assert created_user.email == mock_user_dto.email  # type: ignore

    db.session.delete(created_user)
    db.session.commit()


def test_check_login_and_password(setup):
    repository = UserRepository()

    user = Users(
        id=str(uuid4()),
        email="test@example.com",
        is_active=True,
        is_company=False,
    )  # type: ignore

    user.password = "test_pass"
    db.session.add(user)

    result = repository.check_email_and_password(user.email, user.password)  # type: ignore

    assert result == True


def test_incorrect_password(setup):
    repository = UserRepository()

    user = Users(
        id=str(uuid4()),
        email="test@example.com",
        is_active=True,
        is_company=False,
    )  # type: ignore

    user.password = "test_pass"
    db.session.add(user)
    result = repository.check_email_and_password(user.email, "wrong_password")  # type: ignore

    assert result is False


def test_incorrect_email(setup):
    repository = UserRepository()

    user = Users(
        id=str(uuid4()),
        email="test@example.com",
        is_active=True,
        is_company=False,
    )  # type: ignore

    user.password = "test_pass"
    db.session.add(user)
    result = repository.check_email_and_password("wrongemail@teste.com", user.password)  # type: ignore

    assert result is False
