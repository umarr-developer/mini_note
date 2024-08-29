import bcrypt
import fastapi
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.schemas import AuthUser, CreateUser
from crud import get_user_by_username, create_user
from src.models import User


def validate_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hashed_password,
    )


def auth_user(user: User, user_schema: AuthUser) -> bool | None:
    auth = validate_password(user_schema.password, user.password)
    if auth:
        return auth
    raise fastapi.HTTPException(
        status_code=fastapi.status.HTTP_401_UNAUTHORIZED,
        detail='invalid password'
    )


async def get_user_or_exc(session: AsyncSession, user_schema: AuthUser) -> User | None:
    user = await get_user_by_username(session, user_schema.username)
    auth_user(user, user_schema)
    if user:
        return user
    raise fastapi.HTTPException(
        status_code=fastapi.status.HTTP_404_NOT_FOUND,
        detail='user not found'
    )


async def create_user_or_exc(session: AsyncSession, user_schema: CreateUser) -> User | None:
    user = await get_user_by_username(session, user_schema.username)
    if not user:
        return await create_user(session, user_schema)
    raise fastapi.HTTPException(
        status_code=fastapi.status.HTTP_401_UNAUTHORIZED,
        detail='this username is already taken'
    )
