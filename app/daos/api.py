from fastapi import APIRouter, status as https_status, Depends
from app.daos.crud import DaosCRUD
from app.daos.deps import get_daos_crud
from app.daos.models import DaoRead, DaoCreate

router = APIRouter()

@router.get("", response_model=list[DaoRead], status_code=https_status.HTTP_200_OK)
async def read_daos(daos: DaosCRUD = Depends(get_daos_crud)):
    daos = await daos.get_all()
    return daos

@router.post("", response_model=DaoRead, status_code=https_status.HTTP_200_OK)
async def create_dao(data: DaoCreate, daos: DaoCreate = Depends(get_daos_crud)):
    dao = await daos.create(data=data)
    return dao