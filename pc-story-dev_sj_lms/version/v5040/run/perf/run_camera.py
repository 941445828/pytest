# coding = utf-8
"""
@Author: sujie
@Create on: 2023-2
@Modify on:
@File: 测试摄像头-打开虚拟背景
"""


import threading
import pytest
from config.updateConf import UpdateConfig
from functs.collect_perf import Collect
from config import utils
from config import perf_conf


def camera():
    pytest.main(['-vs',
                 '../../testcase/test_Login.py::TestLogin',
                 '../../testcase/test_CreateClass.py::TestUseTargetClass',  # 使用指定班群
                 '../../testcase/test_CreateClass.py::TestChangeCourseTab',  # 切换到课程tab
                 # '../../testcase/stability/class/test_Create_KeTang.py::TestCreateLuKeKeTang',  # 创建课节--录课模式
                 '../../testcase/test_AddOnlineCourse.py::TestEnterClassRoomH5',  # 进入教室内
                 '../../testcase/test_AddOnlineCourse.py::TestLuKeEnter',  # 录课模式, 进入教室后的提示确认; 非录课模式不用
                 '../../testcase/stability/test_OnlineClassRoom.py::TestSettingCamera',   # 摄像头开启虚化
                 '../../testcase/stability/test_OnlineClassRoom.py::TestOnlineDoubleClickCamera', # 摄像头全屏
                 '../../testcase/stability/test_OnlineClassRoom.py::TestSleepAfterVirtual',  # 摄像头开启虚化后，停留1800s（30分钟）观察数据

                 # 退出教室
                 '../../testcase/test_QuitOnlineClassRoom.py::TestQuitLuKeOnlyOne',  # 仅自己退出
                 '../../testcase//stability/test_OnlineClassRoom.py::TestClassOverAppraise',  # 若班级无学生，可以省略此步
                 '../../testcase/test_QuitAPP.py'
                 ])


def collect():
    cpu_file_url = utils.get_cpu_csv_url(perf_conf.cpu_csv_name)  # 自定义CSV文件名字
    mem_file_url = utils.get_mem_csv_url(perf_conf.mem_csv_name)  # 自定义CSV文件名字
    Collect().collect(cpu_file_url, mem_file_url)


def run():
    t1 = threading.Thread(target=camera)
    t2 = threading.Thread(target=collect)

    t1.start()
    t2.start()


if __name__ == "__main__":
    UpdateConfig().get_app_version(app=perf_conf.APP_URL)
    UpdateConfig().get_login(name=perf_conf.LOGIN_USER_NAME, pw=perf_conf.LOGIN_PASS_WORD)
    UpdateConfig().get_classname(classname=perf_conf.CLASSNAME)
    run()
