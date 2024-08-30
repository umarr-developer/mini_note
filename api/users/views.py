import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.schemas import GetUser, CreateUser, AuthUser
from src.database import db_tools
from utils import create_user_or_exc, get_user_or_exc

router = fastapi.APIRouter(prefix='/users', tags=['users'])


@router.post('/create/',
             response_model=GetUser,
             status_code=fastapi.status.HTTP_201_CREATED)
async def on_create_user(user_schema: CreateUser,
                         session: AsyncSession = Depends(db_tools.session_dependency)):
    return await create_user_or_exc(session, user_schema)


@router.post('/notes/')
async def on_all_notes(user_schema: AuthUser,
                       session: AsyncSession = Depends(db_tools.session_dependency)):
    user = await get_user_or_exc(session, user_schema)
    return user.notes
