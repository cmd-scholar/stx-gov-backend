from fastapi.params import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.database import get_async_session
from app.votes.crud import VotesCRUD


async def get_votes_crud(session: AsyncSession =  Depends(get_async_session)) -> VotesCRUD:
    return VotesCRUD(session=session)