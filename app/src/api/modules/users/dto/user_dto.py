from typing import Dict
from typing import Optional

from src.database.models import Users
from src.shared.base_dto import BaseDTO


class UserDTO(BaseDTO):
    def __init__(
        self,
        id: Optional[str],
        password: Optional[str],
        email: Optional[str],
        is_active: Optional[bool],
        is_company: Optional[bool],
    ) -> None:
        self.id = id
        self.password = password
        self.email = email
        self.is_active = is_active
        self.is_company = is_company

    def to_dict(self):
        return {
            "id": self.id,
            "password": self.password,
            "email": self.email,
            "is_active": self.is_active,
            "is_company": self.is_company,
        }

    @classmethod
    def from_dict(cls, dto: Dict):
        return cls(
            id=dto.get("id"),
            password=dto.get("password"),
            email=dto.get("email"),
            is_active=dto.get("is_active"),
            is_company=dto.get("is_company"),
        )

    @classmethod
    def from_model(cls, user: Users):
        return cls(
            id=user.id,
            email=user.email,
            password=user.password,
            is_active=user.is_active,
            is_company=user.is_company,
        )
