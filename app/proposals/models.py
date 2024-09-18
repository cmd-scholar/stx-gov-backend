from datetime import datetime
from sqlmodel import SQLModel, Field
from app.core.models import UUIDModel, TimestampModel
from uuid import UUID


class ProposalBase(SQLModel):
    created_by: str = Field(nullable=False)
    user_id: UUID = Field(default=None, nullable=False)
    upvotes: int = Field(default=0, nullable=False)
    downvotes: int = Field(default=0, nullable=False)
    status: bool = Field(nullable=False)
    title: str = Field(nullable=False)
    description: str = Field(nullable=False)
    end_date: datetime = Field(nullable=False)


class Proposal(ProposalBase, UUIDModel, TimestampModel, table=True):
    __tablename__ = "proposals"


class ProposalRead(ProposalBase):
    ...

class ProposalCreate(ProposalBase):
    ...

