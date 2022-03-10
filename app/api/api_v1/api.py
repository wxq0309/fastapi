# -*- encoding: utf-8 -*-
"""
@File    :   api.py    
@Contact :   1053522308@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/26 3:18 下午   wuxiaoqiang      1.0         None
"""
from fastapi import APIRouter

from app.api.api_v1.endpoints import user

api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["users"])
