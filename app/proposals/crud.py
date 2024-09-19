from sqlalchemy import select
from sqlmodel.ext.asyncio.session import AsyncSession
from uuid import UUID
from datetime import datetime, timezone
from app.proposals.models import ProposalCreate, Proposal, ProposalRead


class ProposalsCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    def _convert_to_naive_utc(self, dt: datetime) -> datetime:
        if dt.tzinfo is not None:
            return dt.astimezone(timezone.utc).replace(tzinfo=None)
        return dt

    async def create(self, proposal: ProposalCreate) -> ProposalCreate:
        values = proposal.model_dump()
        if 'end_date' in values and values['end_date'] is not None:
            values['end_date'] = self._convert_to_naive_utc(values['end_date'])
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