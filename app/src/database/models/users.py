from dataclasses import dataclass

from shared.base_model import BaseModel


@dataclass
class Users(BaseModel):
    id: str
    password: str
    email: str
    is_active: bool
    is_company: bool
