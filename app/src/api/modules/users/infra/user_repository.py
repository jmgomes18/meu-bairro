from src.api.modules.users.dto import UserDTO
from src.database.database import db
from src.database.models import Users
from src.database.repository.base_repository import BaseRepository

from app.src.shared.base_model import BaseModel


class UserRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(Users, UserDTO)

    def create(self, dto: UserDTO) -> BaseModel:
        data = self.model.from_dict(dto.to_dict())
        data.password = dto.password
        print(data)
        db.session.add(data)
        db.session.commit()
        return data
