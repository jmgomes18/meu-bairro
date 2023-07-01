from abc import ABC
from abc import abstractmethod


class BaseDTO(ABC):
    @abstractmethod
    def to_dict(self):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_dict(cls, dto_dict):
        raise NotImplementedError

    def __repr__(self):
        return f"{self.__class__.__name__}({self.to_dict()})"
