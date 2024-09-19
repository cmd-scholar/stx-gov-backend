from sqlmodel import Relationship
from typing import List
from app.core.models import TimestampModel, UUIDModel
from app.users.base import UserBase
from app.models.common import UserDaoLink

class User(UserBase, TimestampModel,UUIDModel,  table=True):
    __tablename__ = "users"
    daos: List["Dao"] = Relationship(back_populates="members", link_model=UserDaoLink)
    created_daos: List["Dao"] = Relationship(back_populates="creator")

class UserRead(UserBase, UUIDModel):
    daos: List["DaoRead"] = []
    created_daos: List["DaoRead"] = []

class UserCreate(UserBase):
    pass