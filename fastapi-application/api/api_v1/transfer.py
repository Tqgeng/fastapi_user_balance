from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.fastapi_users_router import current_active_user
from core.models import User, db_helper
from core.shemas.transfer import TransferRequest
from core.config import settings
from crud.transfer import transfer_balance

router = APIRouter(
    prefix=settings.api.v1.transfer,
    tags=["Transfer"],
)


@router.post("")
async def transfer(
    request: TransferRequest,
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    await transfer_balance(
        session,
        user,
        request.to_user_id,
        request.amount,
    )
    return {"message": "success"}
