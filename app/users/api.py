from fastapi import APIRouter, status as https_status, Depends
from uuid import UUID

from app.core.models import StatusMessage
from app.users.base import UserBase
from app.users.crud import UsersCRUD
from app.users.deps import get_users_crud
from app.users.models import UserCreate

router = APIRouter()
@router.post('', response_model=UserBase, status_code=https_status.HTTP_201_CREATED)
async def create_user(user: UserCreate, users: UsersCRUD = Depends(get_users_crud)):
    user = await users.create(user)
    return user

@router.get('/all', response_model=list[UserBase], status_code=https_status.HTTP_200_OK)
async def get_all_users(users: UsersCRUD = Depends(get_users_crud)):
    return await users.get_all()

@router.get("/{user_id}", response_model=UserBase, status_code=https_status.HTTP_200_OK)
async def get_user_by_uuid(user_id: UUID, users: UsersCRUD = Depends(get_users_crud)):
    user = await  users.get_user(user_id=user_id)
    return user

@router.patch('/{user_id}', response_model=UserBase, status_code=https_status.HTTP_200_OK)
async def update_user(user_id: UUID, data: UserCreate, users: UsersCRUD = Depends(get_users_crud)):
    user = await users.patch(user_id=user_id, data=data)
    return user

@router.delete("/{user_id}", response_model=StatusMessage, status_code=https_status.HTTP_200_OK)
async def delete_user(user_id: UUID, users: UsersCRUD = Depends(get_users_crud)):
    status = await users.delete(user_id=user_id)
    return StatusMessage(status=status, message='User deleted')