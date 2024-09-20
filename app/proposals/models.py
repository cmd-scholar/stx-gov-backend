from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from app.core.models import UUIDModel, TimestampModel
from uuid import UUID
from typing import List


class ProposalBase(SQLModel):
    created_by_id: UUID = Field(nullable=False, foreign_key="users.uuid", ondelete="CASCADE")
    dao_id: UUID = Field(nullable=False, foreign_key="daos.uuid")
    upvotes: int = Field(default=0, nullable=False)
    downvotes: int = Field(default=0, nullable=False)
    total_votes: int = Field(default=0, nullable=True)
    status: bool = Field(nullable=False)
    title: str = Field(nullable=False)
    description: str = Field(nullable=False)
    end_date: datetime = Field(nullable=False)



class Proposal(ProposalBase, UUIDModel, TimestampModel, table=True):
    __tablename__ = "proposals"
    created_by: "User" = Relationship(back_populates="created_proposals")
    votes: List["Vote"] = Relationship(back_populates="proposal", cascade_delete=True)


class ProposalRead(UUIDModel, ProposalBase):
    ...

class ProposalCreate(ProposalBase):
    ...

