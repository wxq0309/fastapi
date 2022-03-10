from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_class import Base, BaseMixIn


class User(Base, BaseMixIn):
    __tablename__ = "user"

    username = Column(String(50), nullable=True)
    phone = Column(String(length=11), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    user_type = Column(Integer, default=0)
    message_code = relationship("MessageCode")


class MessageCode(Base, BaseMixIn):
    __tablename__ = "message_code"

    code = Column(String(length=6))
    user = Column(ForeignKey("user.id"))
