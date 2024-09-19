from sqlmodel import SQLModel, Field
from uuid import UUID

class UserDaoLink(SQLModel, table=True):
    __tablename__ = 'user_dao_links'
    user_id: UUID = Field(foreign_key='users.uuid', primary_key=True)
    dao_id: UUID = Field(foreign_key='daos.uuid', primary_key=True)