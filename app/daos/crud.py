from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.daos.models import DaoRead, Dao


class DaosCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list[DaoRead]:
        statement = select(Dao)
        results = await self.session.execute(statement)
        daos = results.scalars().all()

        return daos