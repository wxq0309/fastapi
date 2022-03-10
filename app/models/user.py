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

    def to_dict(self):
        data = {
            "id": self.id,
            "username": self.username,
            "user_type": self.user_type,
            "create_time": self.create_time,
            "update_time": self.update_time,
            "phone": self.phone
        }
        return data


class MessageCode(Base, BaseMixIn):
    __tablename__ = "message_code"

    code = Column(String(length=6))
    user = Column(ForeignKey("user.id"))
