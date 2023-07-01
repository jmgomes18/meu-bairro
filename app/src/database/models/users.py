from dataclasses import dataclass


@dataclass
class Users:
    id: str
    password: str
    email: str
    is_active: bool
    is_company: bool
