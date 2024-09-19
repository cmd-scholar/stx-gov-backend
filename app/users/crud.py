from sqlalchemy import select
from sqlmodel.ext.asyncio.session import AsyncSession
from uuid import UUID

from app.users.base import UserBase
from app.users.models import UserCreate, User


class UsersCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    # def get_user(self, user_id: UUID) -> :


    async def create(self, data: UserCreate):
        values = data.model_dump()
        user = User(**values)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_all(self) -> list[UserBase]:
        statement = select(User)
        result = await self.session.execute(statement)
        users = result.scalars().all()

        return users