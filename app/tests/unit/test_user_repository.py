from uuid import uuid4

import pytest
from src.api.modules.users.dto import UserDTO
from src.api.modules.users.infra import UserRepository
from src.database.database import db


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

    assert str(created_user.id) == mock_user_dto.id
    assert created_user.email == mock_user_dto.email

    db.session.delete(created_user)
    db.session.commit()
