from typing import Union, Optional

from pydantic import BaseModel

from app.schemas.base import BaseSchemaModel


class UserBase(BaseModel):
    phone: str


class UserCreate(UserBase):
    password: str


class UserLogin(UserCreate):
    pass


class UserInfo(UserBase):
    id: int
    username: Optional[str] = None
    create_time: Optional[str] = None
    update_time: Optional[str] = None


class MessageCodeBase(BaseSchemaModel):
    code: Union[str, None]
    user: Union[UserBase, None]
