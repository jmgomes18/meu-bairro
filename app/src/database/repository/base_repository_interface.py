from abc import ABC
from abc import abstractmethod
from typing import List

from src.shared.base_dto import BaseDTO
from src.shared.base_model import BaseModel


class BaseRepositoryInterface(ABC):
    @abstractmethod
    def create(self, dto: BaseDTO) -> BaseModel:
        raise NotImplementedError

    @abstractmethod
    def read(self, id: str) -> BaseModel:
        raise NotImplementedError

    @abstractmethod
    def update(self, dto: BaseDTO) -> BaseModel:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[BaseModel]:
        raise NotImplementedError
