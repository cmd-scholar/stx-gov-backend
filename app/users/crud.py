from fastapi import HTTPException, status as https_status
from sqlalchemy import select, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel.ext.asyncio.session import AsyncSession
from uuid import UUID

from app.users.base import UserBase
from app.users.models import UserCreate, User


class UsersCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

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

    async def patch(self, data: UserCreate, user_id: UUID) -> UserBase:
        statement = select(User).where(User.uuid == user_id)
        result = await self.session.execute(statement)
        user = result.scalar_one_or_none()

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        values = data.model_dump(exclude_unset=True)
        for key, value in values.items():
            setattr(user, key, value)
        await self.session.commit()
        await self.session.refresh(user)

        return user

    async def get_user(self, user_id: UUID) -> UserBase:
        statement = select(User).where(User.uuid == user_id)
        result = await self.session.execute(statement)
        user = result.scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def delete(self, user_id: UUID) -> bool:
        try:
            user = await self.get_user(user_id)
            statement = delete(User).where(User.uuid == user_id)
            await self.session.execute(statement)
            await self.session.commit()

            return True
        except HTTPException as e:
            if e.status_code == https_status.HTTP_404_NOT_FOUND:
                raise e
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise HTTPException(status_code=https_status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))