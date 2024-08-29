import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from src.config import Config, config


class Base(DeclarativeBase):
    __abstract__ = True


class DataBaseTools:

    def __init__(self, _config: Config):
        self.engine = create_async_engine(
            url=_config.database_config.database_url,
            echo=True
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=asyncio.current_task
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()


db_tools = DataBaseTools(config)
