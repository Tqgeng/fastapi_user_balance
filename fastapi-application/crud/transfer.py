from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User


async def get_user(session: AsyncSession, user_id: int) -> User:
    user = await session.scalar(select(User).where(User.id == user_id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


async def transfer_balance(
    session: AsyncSession,
    from_user: User,
    to_user_id: int,
    amount: int,
):
    if from_user.id == to_user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You cant send coins yourself",
        )

    if amount <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Amount not enough",
        )

    to_user = await get_user(session, to_user_id)

    if from_user.balance < amount:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough money",
        )

    from_user.balance -= amount
    to_user.balance += amount

    await session.commit()
