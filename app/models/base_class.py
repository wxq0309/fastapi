from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declared_attr


class BaseMixIn:
    create_time = Column(DateTime, nullable=True)
    update_time = Column(DateTime, nullable=True)


@as_declarative()
class Base:
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
