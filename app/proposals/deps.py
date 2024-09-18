from fastapi.params import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.database import get_async_session
from app.proposals.crud import ProposalsCRUD


async def get_proposals_crud(session: AsyncSession =  Depends(get_async_session)) -> ProposalsCRUD:
    return ProposalsCRUD(session=session)