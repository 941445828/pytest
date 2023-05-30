# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
import logging
from config import *


class LogMethod(logging.Logger):  # 继承了Logger类
    def __init__(self, name=None, level=None, file=None, format=None):
        """
        :param name: LOG_NAME
        :param level: LOG_SET_LEVEL
        :param file: LOG_FILE_URL
        :param format: LOG_FORMAT
        """

        # 设置收集器
        super(LogMethod, self).__init__(name)
        # 设置收集器级别
        self.setLevel(level)
        # 设置日志格式
        fmt = logging.Formatter(format)
        if file:
            file_handler = logging.FileHandler(file, encoding='utf-8', mode='a')
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)


logger = LogMethod(name=LOG_NAME, level=LOG_SET_LEVEL,
                   file=LOG_FILE_URL, format=LOG_FORMAT)
logger.info("********** log begin **********")
