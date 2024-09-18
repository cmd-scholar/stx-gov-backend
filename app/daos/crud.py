from sqlalchemy import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.daos.models import DaoRead, Dao, DaoCreate


class DaosCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: DaoCreate) -> DaoRead:
        values = data.model_dump()
        dao = Dao(**values)
        self.session.add(dao)
        await self.session.commit()
        await self.session.refresh(dao)

        return dao

    async def get_all(self) -> list[DaoRead]:
        statement = select(Dao)
        result = await self.session.execute(statement)
        daos = result.scalars().all()
        return daos

