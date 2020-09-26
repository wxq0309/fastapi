# -*- encoding: utf-8 -*-
"""
@File    :   deps.py    
@Contact :   1053522308@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/26 3:15 下午   wuxiaoqiang      1.0         None
"""
import jose
import jwt
import orm
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from starlette import status

from app.core.security import verify_password, SECRET_KEY, ALGORITHM
from app.models.user import Users

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/users/login")


async def get_user(email: str):
    try:
        user = Users.objects.get(email=email)
    except orm.exceptions.NoMatch as e:
        raise HTTPException(status_code=400, detail="User Does't Match !!!")
    else:
        return user


async def authenticate_user(email: str, password: str):
    user = await get_user(email)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


async def get_current_user(*, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        username: str = payload.get("username")
        if email is None or email is None:
            raise credentials_exception
    except jose.exceptions.ExpiredSignatureError:
        raise credentials_exception
    except JWTError as e:
        raise credentials_exception
    user = await Users.objects.limit(1).filter(email=email, username=username).all()
    if not user:
        raise credentials_exception

    return user[0]
