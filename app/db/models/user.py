import datetime
import uuid

from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.db.session import Base
from app.services import security


class User(Base):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    salt = Column(String(255), default="")
    registered_on = Column(DateTime, nullable=False)
    admin = Column(Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.change_password(password)
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def check_password(self, password: str) -> bool:
        return security.verify_password(self.salt + password, self.password)

    def change_password(self, password: str) -> None:
        self.salt = security.generate_salt()
        self.password = security.get_password_hash(self.salt + password)

    @property
    def serialize(self):
        """
        Return item in serializeable format
        """
        return {"email": self.email, "registered_on": self.registered_on, "admin": self.admin}