from fastapi import APIRouter, status as https_status, Depends

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