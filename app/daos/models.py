from sqlmodel import SQLModel, Field

from app.core.models import TimestampModel, UUIDModel


class DaoBase(SQLModel):
    img: str = Field(nullable=False)
    members: int = Field(nullable=False)
    short_desc: str = Field(nullable=False)
    name: str = Field(nullable=False)
    about: str = Field(nullable=False)

class Dao(TimestampModel, DaoBase, UUIDModel,table=True):
    __tablename__='daos'

class DaoCreate(DaoBase):
    ...

class DaoRead(DaoBase, UUIDModel):
    ...
