from fastapi import APIRouter
from fastapi.params import Depends
from starlette import status
from uuid import UUID
from app.core.models import StatusMessage
from app.proposals.crud import ProposalsCRUD
from app.proposals.deps import get_proposals_crud
from app.proposals.models import ProposalRead, ProposalCreate

router = APIRouter()
@router.get("", response_model=list[ProposalRead], status_code=status.HTTP_200_OK)
async def get_proposals_by_dao(dao_id: str, proposals: ProposalsCRUD = Depends(get_proposals_crud)):
    proposals = await proposals.get_by_dao_id(dao_id=dao_id)
    return proposals

@router.post("", response_model=ProposalCreate, status_code=status.HTTP_201_CREATED)
async def create_proposal(data: ProposalCreate, proposals: ProposalsCRUD = Depends(get_proposals_crud)):
    proposal = await proposals.create(data)
    return proposal

@router.get("/{proposal_id}", response_model=ProposalRead, status_code=status.HTTP_200_OK)
async def get_proposal(proposal_id: UUID, proposals: ProposalsCRUD = Depends(get_proposals_crud)):
    proposal = await proposals.get_by_id(proposal_id)
    return proposal

@router.delete("/{proposal_id}", response_model=StatusMessage, status_code=status.HTTP_200_OK)
async def delete_proposal(proposal_id: UUID, proposals: ProposalsCRUD = Depends(get_proposals_crud) ):
    return await proposals.delete(proposal_id)
