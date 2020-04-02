import orm
from typing import Any
from fastapi import APIRouter, status, Body, Depends, Security
from fastapi.exceptions import HTTPException
from pydantic import Field

from dao.user import Users
from model.user import CreateUser
from service.jwt_service import get_password_hash, create_access_token, verify_password, get_current_user
# from controller.actions.user import create_user

router = APIRouter()


@router.post("/")
async def user(user: CreateUser):
    hash_password = get_password_hash(user.password)
    await Users.objects.create(email=user.email, phone=user.phone, password=hash_password, username=user.username)
    return create_access_token(data={"username": user.username, "email": user.email})


@router.post("/login")
async def user(email: str = Body(..., min_length=6), password: str = Body(..., min_length=6)):
    try:
        user = await Users.objects.get(email=email)
    except Exception as e:
        return HTTPException(status.HTTP_204_NO_CONTENT, detail="用户不存在")
    if not verify_password(password, user.password):
        return HTTPException(status.HTTP_401_UNAUTHORIZED, detail="用户信息错误")
    token = create_access_token(
        data={"username": user.username, "email": user.email, "scopes": [user.permission]})
    return {"username": user.username, "email": user.email, "id": user.id, "token": token}


@router.get("/me/")
# async def info(current_user: Users = Depends(get_current_user)):
async def info(current_user: Users = Security(get_current_user, scopes=['normal'])):
    return current_user


@router.get("/alls")
async def user(current_user: Users = Security(get_current_user, scopes=['admin'])):
    return await Users.objects.all()


@router.post("/password/")
async def reset_password(user: Users = Depends(get_current_user), new_pwd: str = Body(..., min_length=6), old_pwd: str = Body(..., min_length=6)):
    if verify_password(old_pwd, user.password):
        await user.update(password=get_password_hash(new_pwd))
        return {"code": 0, "msg": "密码修改成功"}
    return {"code": 1, "msg": "原密码错误"}


# 单个body属性可通过 embed设置
# @router.post("/test/")
# async def test(abd: str=Body(..., embed=True)):
#     print(abd)
