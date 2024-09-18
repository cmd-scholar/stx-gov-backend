from sqlalchemy import select
from sqlmodel.ext.asyncio.session import AsyncSession
from uuid import UUID
from app.proposals.models import ProposalCreate, Proposal, ProposalRead


class ProposalsCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, proposal: ProposalCreate) -> ProposalCreate:
        values = proposal.model_dump()
        proposal = Proposal(**values)
        self.session.add(proposal)
        await self.session.commit()
        await self.session.refresh(proposal)
        return proposal

    async def get_by_dao_id(self, dao_id: UUID) -> list[ProposalRead]:
        statement = select(Proposal).where(Proposal.dao_id == dao_id)
        result = await self.session.execute(statement)
        proposals = result.scalars().all()

        return proposals

    async def get_by_id(self, proposal_id: UUID) -> ProposalRead:
        statement = select(Proposal).where(Proposal.uuid == proposal_id)
        result = await self.session.execute(statement)
        proposal = result.scalars().first()
        return proposal