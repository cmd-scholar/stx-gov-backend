from fastapi import APIRouter
from app.daos.api import router as daos_router
api_router = APIRouter()
include_api = api_router.include_router

routers = [
    (daos_router, "daos", "daos")
]

if len(routers) > 0:
    for router_item in routers:
        router, prefix, tag = router_item
        if tag:
            include_api(router, prefix=f"/{prefix}", tags=[tag])
        else:
            include_api(router, prefix=prefix)