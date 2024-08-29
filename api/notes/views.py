import fastapi
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.notes.schemas import GetNote, CreateNote
from api.users.schemas import AuthUser
from crud import create_note
from database import db_tools
from utils import get_user_or_exc

router = fastapi.APIRouter(prefix='/notes', tags=['posts'])


@router.post('/create/',
             response_model=list[GetNote])
async def on_create_note(user_schema: AuthUser,
                         note_schema: CreateNote,
                         session: AsyncSession = Depends(db_tools.session_dependency)):
    user = await get_user_or_exc(session, username=user_schema.username)
    return await create_note(session, note_schema, user.user_id)
 