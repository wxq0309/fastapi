# -*- encoding: utf-8 -*-
"""
@File    :   statusCode.py    
@Contact :   1053522308@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/28 9:18 下午   wuxiaoqiang      1.0        队列消费状态枚举类型
"""
from enum import Enum


class MQCode(Enum):
    """
    0 未入队列 1 已入队列 2 已消费 3 消费异常
    """
    NotEntered = 0
    Queued = 1
    Consumed = 2
    AbnormalConsumption = 3

