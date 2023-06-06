import uuid
import bcrypt
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Column, String, DateTime, UUID, Boolean
from app.src.database.db_base import Base

class Users(Base):
    __tablename__ = "users"

    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    _password = Column("password", String(100), nullable=False)
    email = Column("email", String(100), nullable=False)
    is_active = Column("is_active", Boolean, nullable=False, default=True)
    is_company = Column("is_company", String(15), nullable=False)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column(
        "updated_at", DateTime, default=datetime.now(), onupdate=datetime.now()
    )

    def __repr__(self) -> str:
        return f"User({self.email}, {self.is_active}, {self.is_company})"

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = bcrypt.hashpw(value.encode(), bcrypt.gensalt()).decode()

    @password.expression
    def password(self):
        return self._password

    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self._password.encode())