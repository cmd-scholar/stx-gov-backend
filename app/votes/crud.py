from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List

from app.proposals.models import Proposal
from app.votes.models import Vote, VoteBase


class VotesCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def vote(self, data: VoteBase) -> VoteBase:
        try:
            values = data.model_dump()
            vote = Vote(**values)
            statement = select(Proposal).where(Proposal.uuid == vote.proposal_id)
            result = await self.session.execute(statement)
            proposal = result.scalar_one_or_none()
            if not proposal:
                raise ValueError("Proposal does not exist")
            if vote.vote_type == "upvote":
                proposal.upvotes += 1
            elif vote.vote_type == "downvote":
                proposal.downvotes += 1
            self.session.add(vote)
            proposal.total_votes = proposal.upvotes + proposal.downvotes
            await self.session.commit()
            await self.session.refresh(vote)
            await self.session.refresh(proposal)

            return vote
        except IntegrityError as e:
            await self.session.rollback()
            if 'unique constraint' in str(e).lower():
                raise ValueError("THis vote already exists.") from e
            elif 'foreign key constraint' in str(e).lower():
                raise ValueError("Invalid proposal or user id.") from e
            else:
                raise ValueError("An error occurred while processing vote.") from e
        except Exception as e:
            await self.session.rollback()
            raise ValueError(f"An unexpected error occurred: {str(e)}") from e

    async def get_votes(self, proposal_id) -> List[Vote]:
        statement = select(Vote).where(Vote.proposal_id == proposal_id)
        result = await self.session.execute(statement)
        votes =  result.scalars().all()
        return list(votes)