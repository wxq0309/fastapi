import databases
import sqlalchemy

DATABASE_URL = "mysql+pymysql://root:123456@localhost/ihou"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()


async def create_connection():
    await database.connect()


async def disconnect():
    await database.disconnect()