# -*- encoding: utf-8 -*-
"""
@File    :   deps.py    
@Contact :   1053522308@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/26 3:15 下午   wuxiaoqiang      1.0         None
"""
from typing import Generator, Union, Any, Optional

import jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import ExpiredSignatureError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from starlette import status

from app.core.security import verify_password, SECRET_KEY, ALGORITHM, oauth2_scheme, get_jwt_token
from app.models.db import SessionLocal
from app.models.user import User


async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
        await session.commit()


async def get_user(user: callable, session: AsyncSession) -> Any:
    stmt = select(User).where(User.phone == user.phone)
    results = await session.execute(stmt)
    try:
        _user = results.scalar()
    except AttributeError:
        return None
    if not _user:
        return None
    return _user


async def authenticate_user(email: str, password: str):
    user = await get_user(email)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


async def get_current_user(*, session: AsyncSession = Depends(get_db), payload: dict = Depends(get_jwt_token)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    try:
        _id: int = payload.get("id", None)
        phone: str = payload.get("phone", None)
        if _id is None or phone is None:
            raise credentials_exception
    except ExpiredSignatureError:
        raise credentials_exception
    except Exception:
        raise credentials_exception

    if _id:
        stmt = select(User).where(User.id == _id)
    else:
        stmt = select(User).where(User.phone == phone)
    results = await session.execute(stmt)
    user = results.scalar()
    if not user:
        raise credentials_exception

    return user
