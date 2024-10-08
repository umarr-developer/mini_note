import bcrypt
import fastapi
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.schemas import AuthUser, CreateUser
from src.crud import get_user_by_username, create_user
from src.models import User
from src.speller import speller_query


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
    if user:
        auth_user(user, user_schema)
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


async def correct_note(note_body: str) -> str:
    speller = await speller_query(note_body)
    for word in speller:
        note_body = note_body[:word['pos']] + word['s'][0] + note_body[word['pos'] + word['len']:]
    return note_body
