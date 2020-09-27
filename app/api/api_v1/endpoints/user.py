import random

from fastapi import APIRouter, status, Body, Depends, Security, Query
from fastapi.exceptions import HTTPException

from app.api import deps
from app.api.deps import get_current_user
from app.core.celery_app import celery_app
from app.core.security import get_password_hash, create_access_token, verify_password
from app.models.user import Users
from app.schemas.user import CreateUser

router = APIRouter()


@router.post("/register")
async def user(user: CreateUser):
    hash_password = get_password_hash(user.password)
    await Users.objects.create(email=user.email, phone=user.phone, password=hash_password, username=user.username)
    task = celery_app.send_task("app.api.api_v1.tasks.emails.decoratorEmail",
                                args=[user.email, "".join([str(random.randint(1, 9)) for i in range(6)])])
    print(task, "---------")
    return create_access_token(data={"username": user.username, "email": user.email})


@router.post("/login")
async def user(email: str = Body(..., min_length=6), password: str = Body(..., min_length=6)):
    try:
        user = await Users.objects.get(email=email)
    except Exception as e:
        return HTTPException(status.HTTP_204_NO_CONTENT, detail="用户不存在")
    if not verify_password(password, user.password):
        return HTTPException(status.HTTP_401_UNAUTHORIZED, detail="密码错误请重试")
    token = create_access_token(data={"username": user.username, "email": user.email, "scopes": [user.permission]})
    return {"username": user.username, "email": user.email, "id": user.id, "token": token}


@router.get("/me")
async def user(current_user: Users = Depends(deps.get_current_user)):
    return current_user


@router.get("/alls")
async def user(current_user: Users = Security(get_current_user, scopes=['admin'])):
    return await Users.objects.all()


@router.post("/password/")
async def reset_password(user: Users = Depends(get_current_user), new_pwd: str = Body(..., min_length=6),
                         old_pwd: str = Body(..., min_length=6)):
    if verify_password(old_pwd, user.password):
        await user.update(password=get_password_hash(new_pwd))
        return {"code": 0, "msg": "密码修改成功"}
    return {"code": 1, "msg": "原密码错误"}


@router.get("/activated")
async def activated_account(code: str = Query(max_length=6, min_length=6, default="123456")):
    return {"msg": "账户激活成功", "code": code}
