# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 获取ClassIn.exe的PID
"""
import psutil
from handler.logHandler import logger


def get_pid():
    pids = psutil.pids()  # 获取全部pid（list类型）
    pid_name = []  # 解析pids，获取所用程序的pid
    for pid in pids:
        try:
            p = psutil.Process(pid)
            pid_name.append("%d,%s" % (pid, p.name()))
        except Exception:
            logger.error('psutil.Process（）方法报错了！捕获')
    # print(pid_name)
    list_len = len(pid_name)
    for i in range(list_len):
        if 'ClassIn.exe' in pid_name[i]:
            target_pid = pid_name[i].split(',')[0]
            # print(target_pid)
            # logger.info('获取到pid: {} '.format(target_pid))
            return target_pid
        else:
            continue




# get_pid()
