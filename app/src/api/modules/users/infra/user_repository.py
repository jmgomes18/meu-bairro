from src.api.modules.users.dto import UserDTO
from src.database.database import db
from src.database.models import Users
from src.database.repository.base_repository import BaseRepository

from app.src.shared.base_model import BaseModel


class UserRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(Users, UserDTO)  # type: ignore

    def create(self, dto: UserDTO) -> BaseModel:
        data = self.model.from_dict(dto.to_dict())
        data.password = dto.password  # type: ignore
        db.session.add(data)
        db.session.commit()
        return data

    def check_email_and_password(self, email: str, password: str) -> bool:
        result = db.session.query(self.model).filter_by(email=email).first()
        return False if result is None else password == result.password
