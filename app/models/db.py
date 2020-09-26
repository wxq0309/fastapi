import databases
import sqlalchemy

from app.core.config import settings

database = databases.Database(settings.SQLALCHEMY_DATABASE_URI)

metadata = sqlalchemy.MetaData()


async def create_connection():
    await database.connect()


async def disconnect():
    await database.disconnect()
