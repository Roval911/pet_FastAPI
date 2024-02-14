from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase, declared_attr
from sqlalchemy import Column, String, UUID
from config import settings

DATABASE_URL = f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

engine = create_async_engine(DATABASE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id = Column(UUID, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
