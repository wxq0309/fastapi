from datetime import datetime, timedelta

import orm
import jwt
from jwt import PyJWTError
from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from starlette.exceptions import HTTPException
from passlib.context import CryptContext

from dao.user import Users

SECRET_KEY = "ahsdkjhdf443hdhufjds89u839074ounfls556dsd5f5gd4fgdr"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=['bcrypt'])

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token", scheme_name="TOKEN")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token", scheme_name="TOKEN", scopes={
                                     "normal": "Read information about current user", "admin": "admin user"})


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


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
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return {"code": 201, "msg": "新建账户成功", "data": {"token": encoded_jwt, "username": to_encode['username'], "email": to_encode['email']}}


async def get_current_user(*, token: str = Depends(oauth2_scheme), security_scopes: SecurityScopes):
    # 根据权限力度进行接口上的限制
    if security_scopes.scopes:
        authenticate_value = f"TOKEN scopes={security_scopes.scope_str}"
    else:
        authenticate_value = "TOKEN"

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        username: str = payload.get("username")

        token_scopes = payload.get("scopes", [])

        if email is None or email is None:
            raise credentials_exception
    except PyJWTError as e:
        raise credentials_exception
    user = await Users.objects.limit(1).filter(email=email, username=username).all()
    if not user:
        raise credentials_exception

    for scope in security_scopes.scopes:
        if scope not in token_scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
            )
    return user[0]
