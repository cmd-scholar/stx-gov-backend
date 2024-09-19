# app/models/common.py

from sqlmodel import SQLModel, Field
from typing import List, Optional
from uuid import UUID
from app.core.models import TimestampModel, UUIDModel

class UserDaoLink(SQLModel, table=True):
    __tablename__ = 'user_dao_links'
    user_id: UUID = Field(foreign_key='users.uuid', primary_key=True)
    dao_id: UUID = Field(foreign_key='daos.uuid', primary_key=True)