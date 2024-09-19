from sqlmodel import SQLModel, Field
from uuid import UUID

class DaoBase(SQLModel):
    img: str = Field(nullable=False)
    member_count: int = Field(nullable=False)
    short_desc: str = Field(nullable=False)
    name: str = Field(nullable=False)
    about: str = Field(nullable=False)
    created_by_id: UUID = Field(foreign_key="users.uuid")