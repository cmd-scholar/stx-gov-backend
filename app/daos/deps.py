from fastapi.params import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.database import get_async_session
from app.daos.crud import DaosCRUD


async def get_daos_crud(session: AsyncSession =  Depends(get_async_session)) -> DaosCRUD:
    return DaosCRUD(session=session)