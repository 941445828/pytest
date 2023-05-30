# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 获取ClassIn.exe的PID
"""
import psutil
from handler.logHandler import logger
from functs import getPid
import os
import time


def kill_pid():
    pid = getPid.get_pid()
    if pid is None:
        return True
        # logger.info('无ClassIn.exe运行中！')
    else:
        use_str = 'taskkill /pid ' + pid + ' /t /f'
        print('ClassIn.exe 进程存在，将关闭进程！')
        logger.error('ClassIn.exe 进程存在，将关闭以下： ')
        logger.error(use_str)
        os.system(use_str)
        time.sleep(5)


# kill_pid()