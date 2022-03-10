# -*- encoding: utf-8 -*-
"""
@File    :   config.py    
@Contact :   1053522308@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/26 3:22 下午   wuxiaoqiang      1.0         None
"""
from typing import Optional, Dict, Any

from pydantic import validator, BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str

    CELERY_RESULT_BACKEND: Any
    CELERY_NAME: str
    BROKER_URL: Any
    SECRET_KEY: str
    ALGORITHM: str

    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_SERVER: str
    MYSQL_DB: str

    EMAIL_HOST_NAME: str
    EMAIL_PORT: str
    EMAIL_USER: str
    EMAIL_PASSWORD: str

    LOG_NAME: str

    SQLALCHEMY_DATABASE_URI: Optional[str]
    ASYNC_SQLALCHEMY_DATABASE_URI: Optional[str]

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        return f"mysql://{values['MYSQL_USER']}:{values['MYSQL_PASSWORD']}@{values['MYSQL_SERVER']}/{values['MYSQL_DB']}"

    @validator("ASYNC_SQLALCHEMY_DATABASE_URI", pre=True)
    def async_database_url(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        return f"mysql+aiomysql://{values['MYSQL_USER']}:{values['MYSQL_PASSWORD']}@{values['MYSQL_SERVER']}/{values['MYSQL_DB']}"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
