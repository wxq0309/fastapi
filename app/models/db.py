from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_async_engine(settings.ASYNC_SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
