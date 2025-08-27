from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.shemas.user import (
    UserRead,
    UserUpdate,
)
from .fastapi_users_router import fastapi_users
from core.config import settings
from crud.users import get_all_users

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"],
)

# /me /{id}
router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)


@router.get("", response_model=list[UserRead])
async def get_all(session: AsyncSession = Depends(db_helper.session_getter)):
    users = await get_all_users(session)
    return users
