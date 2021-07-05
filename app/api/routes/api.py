from fastapi import APIRouter

from app.api.routes.auth import user


router = APIRouter()
router.include_router(user.router, tags=["Auth"], prefix="/user")

