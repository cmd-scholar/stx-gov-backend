
from sqlmodel import Relationship
from typing import List
from app.core.models import TimestampModel, UUIDModel
from app.daos.base import DaoBase
from app.models.common import UserDaoLink
from app.users.models import User, UserRead

class Dao(TimestampModel, DaoBase, UUIDModel, table=True):
    __tablename__ = 'daos'
    members: List[User] = Relationship(back_populates='daos', link_model=UserDaoLink)
    creator: User = Relationship(back_populates="created_daos")

class DaoCreate(DaoBase):
    pass

class DaoRead(DaoBase, UUIDModel):
    pass
    # creator: UserRead

class DaoReadWithMembers(DaoRead):
    members: List[UserRead] = []