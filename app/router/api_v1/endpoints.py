from fastapi import APIRouter
from app.daos.api import router as daos_router
from app.proposals.api import router as proposal_router
from app.votes.api import router as vote_router
from app.users.api import router as user_router
api_router = APIRouter()
include_api = api_router.include_router

routers = [
    (daos_router, "daos", "daos"),
    (proposal_router, "proposals", "proposals"),
    (vote_router, "votes", "votes"),
    (user_router, "users", "users"),
]

if len(routers) > 0:
    for router_item in routers:
        router, prefix, tag = router_item
        if tag:
            include_api(router, prefix=f"/{prefix}", tags=[tag])
        else:
            include_api(router, prefix=prefix)