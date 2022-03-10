# -*- encoding: utf-8 -*-
"""
@File    :   logger.py    
@Contact :   1053522308@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/28 7:45 下午   wuxiaoqiang      1.0         None
"""
import datetime
import logging
import os
from logging.handlers import RotatingFileHandler

from app.core.config import settings


class Logger:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, filename: str = settings.LOG_NAME, clevel=logging.DEBUG, flevel=logging.DEBUG):
        path = os.getcwd() + os.sep + "Logs"
        if not os.path.exists(path):
            os.makedirs(path)

        self.logger = logging.getLogger(path)
        self.logger.setLevel(clevel)

        fmt = logging.Formatter('[%(asctime)s.%(msecs)03d][%(levelname)s][%(filename)s][%(lineno)d] %(message)s',
                                '%Y-%m-%d %H:%M:%S')

        sHand = logging.StreamHandler()
        sHand.setFormatter(fmt)
        sHand.setLevel(clevel)
        if not os.path.exists(path + os.sep + filename):
            fp = open(path + os.sep + filename, "w")
            fp.close()
        fHand = RotatingFileHandler(path + os.sep + filename, maxBytes=1024 * 1024 * 50, backupCount=5)
        fHand.setFormatter(fmt)
        fHand.setLevel(flevel)
        self.logger.addHandler(sHand)
        self.logger.addHandler(fHand)

    def getlogger(self):
        return self.logger


logger = Logger()
