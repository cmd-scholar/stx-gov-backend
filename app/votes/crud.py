from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from uuid import UUID

from app.proposals.models import Proposal
from app.votes.models import Vote, VoteBase, VoteUpdate


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

    async def update_vote(self, vote_id: UUID, data: VoteUpdate) -> VoteBase:
        vote_statement = select(Vote).where(Vote.uuid == vote_id)
        vote_result = await self.session.execute(vote_statement)
        vote = vote_result.scalar_one_or_none()
        if not vote:
            raise HTTPException(status_code=404, detail="Vote does not exist.")

        proposal_statement = select(Proposal).where(Proposal.uuid == vote.proposal_id)
        proposal_result = await self.session.execute(proposal_statement)
        proposal = proposal_result.scalar_one_or_none()

        if not proposal:
            raise HTTPException(status_code=404, detail="Proposal does not exist.")

        old_vote_type = vote.vote_type
        new_vote_type = data.vote_type

        if old_vote_type != new_vote_type:
            if vote.vote_type == "upvote":
                proposal.upvotes -= 1
            elif vote.vote_type == "downvote":
                proposal.downvotes -= 1

            if new_vote_type == "upvote":
                proposal.upvotes += 1
            elif new_vote_type == "downvote":
                proposal.downvotes += 1

        for key, val in data.model_dump(exclude_unset=True).items():
            setattr(vote, key, val)

        proposal.total_votes = proposal.upvotes + proposal.downvotes

        await self.session.commit()
        await self.session.refresh(vote)
        await self.session.refresh(proposal)
        return vote