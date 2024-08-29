import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.schemas import GetUser, CreateUser, AuthUser
from database import db_tools
from src.crud import create_user, get_user_by_username

router = fastapi.APIRouter(prefix='/users', tags=['users'])


@router.post('/create/',
             response_model=GetUser,
             status_code=fastapi.status.HTTP_201_CREATED)
async def on_create_user(user_schema: CreateUser,
                         session: AsyncSession = Depends(db_tools.session_dependency)):
    user = await get_user_by_username(session, user_schema.username)
    if not user:
        return await create_user(session, user_schema)
    raise fastapi.HTTPException(
        status_code=fastapi.status.HTTP_401_UNAUTHORIZED,
        detail='this username is already taken'
    )


@router.post('/notes/')
async def on_all_notes(user_schema: AuthUser,
                       session: AsyncSession = Depends(db_tools.session_dependency)):
    user = await get_user_by_username(session, user_schema.username)
    if user:
        return user.notes
    raise fastapi.HTTPException(
        status_code=fastapi.status.HTTP_404_NOT_FOUND,
        detail='user not found'
    )
