from fastapi import APIRouter
from fastapi.params import Depends

from app.proposals.crud import ProposalsCRUD
from app.proposals.deps import get_proposals_crud
from app.proposals.models import ProposalRead, ProposalCreate

router = APIRouter()
@router.get("", response_model=list[ProposalRead])
async def get_proposals_by_dao(dao_id: str, proposals: ProposalsCRUD = Depends(get_proposals_crud)):
    proposals = await proposals.get_by_dao_id(dao_id=dao_id)
    return proposals

@router.post("", response_model=ProposalCreate)
async def create_proposal(data: ProposalCreate, proposals: ProposalsCRUD = Depends(get_proposals_crud)):
    proposal = await proposals.create(data)
    return proposal

@router.get("/{proposal_id}", response_model=ProposalRead)
async def get_proposal(proposal_id: str, proposals: ProposalsCRUD = Depends(get_proposals_crud)):
    proposal = await proposals.get_by_id(proposal_id)
    return proposal