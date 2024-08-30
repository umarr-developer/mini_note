import fastapi
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.notes.schemas import GetNote, CreateNote
from api.users.schemas import AuthUser
from crud import create_note, get_note
from database import db_tools
from utils import get_user_or_exc, correct_note

router = fastapi.APIRouter(prefix='/notes', tags=['posts'])


@router.post('/create/',
             response_model=GetNote)
async def on_create_note(user_schema: AuthUser,
                         note_schema: CreateNote,
                         session: AsyncSession = Depends(db_tools.session_dependency)):
    user = await get_user_or_exc(session, user_schema)
    note_schema.body = await correct_note(note_schema.body)
    note_schema.title = await correct_note(note_schema.title)

    return await create_note(session, note_schema, user.user_id)


@router.post('/{note_id}',
             response_model=GetNote)
async def on_get_note(note_id: int,
                      user_schema: AuthUser,
                      session: AsyncSession = Depends(db_tools.session_dependency)):
    user = await get_user_or_exc(session, user_schema)
    return await get_note(session, note_id, user.user_id)
