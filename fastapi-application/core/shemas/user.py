import uuid

from fastapi_users import schemas

from core.types.user_id import UserIdType


class UserRead(schemas.BaseUser[UserIdType]):
    balance: int


class UserCreate(schemas.BaseUserCreate):
    balance: int = 1000


class UserUpdate(schemas.BaseUserUpdate):
    balance: int | None = None
