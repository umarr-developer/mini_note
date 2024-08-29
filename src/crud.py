from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from api.notes.schemas import CreateNote
from api.users.schemas import CreateUser
from src.models import User, Note
from src.hash import hash_password


async def create_user(session: AsyncSession, user_schema: CreateUser) -> User:
    user = User(username=user_schema.username, password=hash_password(user_schema.password))
    session.add(user)
    await session.commit()
    return user


async def get_user_by_username(session: AsyncSession, username: str) -> User:
    sql = select(User).options(joinedload(User.notes)).where(User.username == username)
    result: Result = await session.execute(sql)
    return result.scalar()


async def create_note(session: AsyncSession, note_schema: CreateNote, user_id: int) -> Note:
    note = Note(title=note_schema.title, body=note_schema.body, user_id=user_id)
    session.add(note)
    await session.commit()
    return note
