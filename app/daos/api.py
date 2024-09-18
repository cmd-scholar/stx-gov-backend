from fastapi import APIRouter, status as https_status, Depends

from app.daos.crud import DaosCRUD
from app.daos.deps import get_daos_crud
from app.daos.models import DaoRead

router = APIRouter()

@router.get("/", response_model=DaoRead, status_code=https_status.HTTP_200_OK)
async def read_daos(daos: DaosCRUD = Depends(get_daos_crud)):
    await daos.get_all()
