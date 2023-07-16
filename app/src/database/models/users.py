from dataclasses import dataclass
from typing import Optional

from src.database.entities import Users
from src.shared.base_model import BaseModel


@dataclass
class Users(BaseModel, Users):
    id: Optional[str]
    password: Optional[str]
    email: Optional[str]
    is_active: bool
    is_company: bool
