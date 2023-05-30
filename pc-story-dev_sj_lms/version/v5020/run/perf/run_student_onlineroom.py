# coding = utf-8
"""
@Author: sujie
@Create on: 2023-2
@Modify on:
@File:
2023/2，学生端，收集cpu、mem

"""


import threading
import pytest
from config.updateConf import UpdateConfig
from functs.collect_perf import Collect
from config import utils
from config import perf_conf


def luke():
    """创建 在线 录课模式 教室时长>=30分钟"""
    pytest.main(['-vs',
                 '../../testcase/test_Login.py::TestLogin',
                 '../../testcase/test_CreateClass.py::TestUseTargetClass',  # 使用指定班群
                 '../../testcase/test_CreateClass.py::TestChangeCourseTab',  # 切换到课程tab
                 # 进入教室内
                 '../../testcase/test_AddOnlineCourse.py::TestStuEnterClassRoomH5::test_switch_win_1',
                 '../../testcase/test_AddOnlineCourse.py::TestStuEnterClassRoomH5::test_stu_click_search_logo',
                 '../../testcase/test_AddOnlineCourse.py::TestEnterClassRoomH5::test_enter_search_content',
                 '../../testcase/test_AddOnlineCourse.py::TestEnterClassRoomH5::test_begin_class',
                 '../../testcase/test_AddOnlineCourse.py::TestEnterClassRoomH5::test_changeto_native_driver',

                 # 操作： 举手
                 '../../testcase/stability/test_OnlineClassRoom.py::TestStuSleep::test_time_sleep_60',  # 进入教室后，sleep60s再举手
                 '../../testcase/stability/test_OnlineClassRoom.py::TestStuHandUp::test_choose_handup',

                 # 老师端操作全员下课后，学生端自动关闭教室
                 '../../testcase/stability/test_OnlineClassRoom.py::TestStuSleep::test_time_sleep_1500',


                 # 退出教室
                 '../../testcase/test_QuitOnlineClassRoom.py::TestStuQuitOnlineClassRoom',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestStuClassOverAppraise::test_cancel',  # 若班级无学生，可以省略此步
                 '../../testcase/test_QuitAPP.py'
                 ])


def collect():
    cpu_file_url = utils.get_cpu_csv_url(perf_conf.cpu_csv_name)  # 自定义CSV文件名字
    mem_file_url = utils.get_mem_csv_url(perf_conf.mem_csv_name)  # 自定义CSV文件名字
    Collect().collect(cpu_file_url, mem_file_url)


def luke_run():
    t1 = threading.Thread(target=luke)
    t2 = threading.Thread(target=collect)

    t1.start()
    t2.start()


if __name__ == "__main__":
    UpdateConfig().get_app_version(app=perf_conf.APP_URL)
    UpdateConfig().get_login(name=perf_conf.LOGIN_USER_NAME, pw=perf_conf.LOGIN_PASS_WORD)
    UpdateConfig().get_classname(classname=perf_conf.CLASSNAME)
    luke_run()