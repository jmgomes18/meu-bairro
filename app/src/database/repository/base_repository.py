from typing import List

from src.database.database import db
from src.shared.base_dto import BaseDTO
from src.shared.base_model import BaseModel

from .base_repository_interface import BaseRepositoryInterface


class BaseRepository(BaseRepositoryInterface):
    def __init__(self, model: BaseModel, dto: BaseDTO) -> None:
        self.model = model
        self.dto = dto

    def create(self, dto: BaseDTO) -> BaseModel:
        data = self.model.from_dict(dto.to_dict())
        db.session.add(data)
        db.session.commit()
        return data

    def read(self, id: str) -> BaseModel:
        return db.session.query(self.model).filter_by(id=id).first()

    def update(self, dto: BaseDTO) -> BaseModel:
        data = self.model.from_dict(dto.to_dict())
        result = (
            db.session.query(self.model)
            .filter_by(id=id)
            .update(data.to_dict(exclude_unset=True))
        )
        db.session.commit()
        return result

    def delete(self, id: str) -> None:
        data = db.session.query(self.model).filter_by(id=id).first()
        db.session.delete(data)
        db.session.commit()

    def list(self) -> List[BaseModel]:
        return db.session.query(self.model).all()
