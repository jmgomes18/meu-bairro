from dataclasses import dataclass

from src.shared.base_model import BaseModel


@dataclass
class Users(BaseModel):
    id: str
    password: str
    email: str
    is_active: bool
    is_company: bool
