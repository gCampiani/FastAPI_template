import datetime
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    admin: Optional[bool] = False


class UserList(UserBase):
    registered_on: datetime.datetime
