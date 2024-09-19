
from uuid import UUID

from sqlmodel import SQLModel, Field
from sqlalchemy import Enum, event, Column
from app.core.models import UUIDModel, TimestampModel

vote_type = Enum("upvote", "downvote", name="vote_type", create_type=False)


@event.listens_for(SQLModel.metadata, "before_create")
def _create_enums(metadata, conn, **kw):
    vote_type.create(conn, checkfirst=True)

class VoteBase(SQLModel):
    proposal_id: UUID = Field(foreign_key="proposals.uuid", nullable=False)
    vote_type: str = Field(sa_column=Column("vote_type", vote_type, nullable=False))

class Vote(VoteBase, UUIDModel, TimestampModel, table=True):
    __tablename__ = "votes"