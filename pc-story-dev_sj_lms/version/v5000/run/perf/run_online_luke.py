# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 场景描述：登录--进入班级--创建课节（录课模式）--进入教室--打开多个课件（间隔1分组）--课件全部打开后在教室内停留60s--退出教室--退出教室，获取cpu/mem
"""

import threading
import pytest
from config.updateConf import UpdateConfig
from functs.collect_perf import Collect
from config import utils
from config import perf_conf


def luke():
    """创建 在线 录课模式 教室"""
    pytest.main(['-vs',
                 '../../testcase/test_Login.py',
                 '../../testcase/test_CreateClass.py::TestUseTargetClass',
                 '../../testcase/test_AddOnlineCourse.py::TestAddOnlineCourseLuKe',    # 创建课节--录课模式
                 '../../testcase/test_AddOnlineCourse.py::TestEnterClassRoom',  #  进入教室内
                 '../../testcase/test_AddOnlineCourse.py::TestLuKeEnter',  # 录课模式, 进入教室后的提示确认; 非录课模式不用
                 '../../testcase/test_OnlineOpenFile.py',
                 '../../testcase/test_QuitOnlineClassRoom.py::TestQuitOnlineClassRoom',
                 '../../testcase/test_QuitAPP.py'
                 ])

def get_fps():
    while True:
        pytest.main(['-vs',
                     '../../testcase/perf/test_GetFPS.py'
                     ])


def collect():
    cpu_file_url = utils.get_cpu_csv_url(perf_conf.cpu_csv_name)  # 自定义CSV文件名字
    mem_file_url = utils.get_mem_csv_url(perf_conf.mem_csv_name)  # 自定义CSV文件名字
    Collect().collect(cpu_file_url, mem_file_url)


def luke_run():
    t1 = threading.Thread(target=luke)
    t2 = threading.Thread(target=collect)
    t3 = threading.Thread(target=get_fps)

    t1.start()
    t2.start()
    t3.start()


if __name__ == "__main__":
    UpdateConfig().updateConfig(app=perf_conf.APP_URL, name=perf_conf.LOGIN_USER_NAME, pw=perf_conf.LOGIN_PASS_WORD, classname=perf_conf.CLASSNAME)
    luke_run()
