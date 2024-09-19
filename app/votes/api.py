from fastapi import APIRouter, Depends, status as https_status
from uuid import UUID
from app.votes.crud import VotesCRUD
from app.votes.deps import get_votes_crud
from app.votes.models import Vote, VoteBase, VoteUpdate

router = APIRouter()


@router.get("", response_model=Vote, status_code=https_status.HTTP_200_OK)
async def get_votes(proposal_id: str, votes: VotesCRUD = Depends(get_votes_crud)):
    return await votes.get_votes(proposal_id)


@router.post("", response_model=VoteBase, status_code=https_status.HTTP_201_CREATED)
async def create_vote(data: VoteBase, votes: VotesCRUD = Depends(get_votes_crud)):
    vote = await votes.vote(data)
    return vote


@router.patch("/{vote_id}", response_model=VoteBase, status_code=https_status.HTTP_200_OK)
async def patch_vote(data: VoteUpdate, vote_id: UUID, votes: VotesCRUD = Depends(get_votes_crud)):
    vote = await votes.update_vote(vote_id, data)
    return vote