import fastapi
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.notes.schemas import GetNote, CreateNote
from api.users.schemas import CreateUser, AuthUser
from crud import get_user_by_username, create_note
from database import db_tools
from src.utils import auth_user

router = fastapi.APIRouter(prefix='/notes', tags=['posts'])


@router.post('/create/',
             response_model=GetNote)
async def on_create_note(user_schema: AuthUser,
                         note_schema: CreateNote,
                         session: AsyncSession = Depends(db_tools.session_dependency)):
    user = await get_user_by_username(session, username=user_schema.username)
    if user:
        if auth_user(user, user_schema):
            return await create_note(session, note_schema, user.user_id)
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_401_UNAUTHORIZED,
            detail='invalid password'
        )
    raise fastapi.HTTPException(
        status_code=fastapi.status.HTTP_404_NOT_FOUND,
        detail='user not found'
    )
