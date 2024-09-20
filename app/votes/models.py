
from uuid import UUID

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Enum, event, Column
from app.core.models import UUIDModel, TimestampModel
from app.proposals.models import Proposal

vote_type = Enum("upvote", "downvote", name="vote_type", create_type=False)


@event.listens_for(SQLModel.metadata, "before_create")
def _create_enums(metadata, conn, **kw):
    vote_type.create(conn, checkfirst=True)

class VoteBase(SQLModel):
    created_by_id : UUID = Field(nullable=False, foreign_key="users.uuid", ondelete="CASCADE")
    proposal_id: UUID = Field(foreign_key="proposals.uuid", nullable=False)
    vote_type: str = Field(sa_column=Column("vote_type", vote_type, nullable=False))

class Vote(VoteBase, UUIDModel, TimestampModel, table=True):
    __tablename__ = "votes"
    proposal: "Proposal" = Relationship(back_populates="votes")

class VoteUpdate(SQLModel):
    vote_type: str = Field(sa_column=Column("vote_type", vote_type, nullable=False))