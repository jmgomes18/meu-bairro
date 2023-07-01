from typing import Dict


class BaseModel:
    def __init__(self, **data):
        self.__dict__.update(data)

    def to_dict(self, exclude_unset: bool = False) -> Dict:
        if exclude_unset:
            return {
                k: v
                for k, v in self.__dict__.items()
                if v is not None and k != "_sa_instance_state"
            }
        else:
            return {
                key: value
                for key, value in self.__dict__.items()
                if key != "_sa_instance_state"
            }

    @classmethod
    def from_dict(cls, data: Dict) -> "BaseModel":
        return cls(**data)
