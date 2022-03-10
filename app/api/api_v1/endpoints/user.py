from functools import partial
from typing import Any, Union, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db, get_user, get_current_user
from app.core.security import get_password_hash, create_access_token, verify_password
from app.models.user import User
from app.schemas.base import OutPutSchemaModel
from app.schemas.user import UserCreate, UserLogin, UserInfo

router = APIRouter()


@router.post("/register", status_code=201, response_model=OutPutSchemaModel, description="用户注册", summary="用户注册")
async def register(user_obj: UserCreate, session: AsyncSession = Depends(get_db)) -> Any:
    _user = await get_user(user_obj, session)
    if _user:
        return OutPutSchemaModel(code=0, msg="用户已存在，请直接登录", data=[])
    else:
        hash_password = get_password_hash(user_obj.password)
        _user = User(password=hash_password, phone=user_obj.phone)
        session.add(_user)
        await session.flush()
        data = user_obj.dict().pop("password")
        return OutPutSchemaModel(code=1, msg="注册成功", data=data)


@router.post("/login", description="用户登录", summary="用户登录", response_model=OutPutSchemaModel)
async def login(user: UserLogin, session: AsyncSession = Depends(get_db)) -> Any:
    _user = await get_user(user, session)
    if not _user:
        return OutPutSchemaModel(msg="用户不存在")
    else:
        if not verify_password(user.password, _user.password):
            return OutPutSchemaModel(msg="登录失败，请确认账户或者密码是否存在")
        else:
            return OutPutSchemaModel(code=200, msg="登录成功", data={
                "phone": _user.phone, "id": _user.id,
                "token": create_access_token(data={"phone": user.phone, "id": _user.id})
            })


@router.get("/set_user_info", description="设置个人信息", summary="设置个人信息", response_model=UserInfo)
async def get_user_info(user: Optional[User] = Depends(get_current_user)):
    return user.to_dict()
