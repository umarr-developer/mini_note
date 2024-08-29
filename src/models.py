from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(length=64), unique=True)
    password: Mapped[bytes] = mapped_column(nullable=False)
    notes: Mapped[list['Note']] = relationship(back_populates='user')


class Note(Base):
    __tablename__ = 'notes'

    note_id = Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title = Mapped[str] = mapped_column(String(length=32))
    body = Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    user: Mapped[User] = relationship(back_populates='notes')
