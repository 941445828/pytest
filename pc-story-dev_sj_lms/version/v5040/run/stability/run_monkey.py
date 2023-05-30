# coding = utf-8
"""
@Author: jie.su
@Create on:
@Modify on:
@File: 原生部分，monkey测试
"""
import pytest
from config import stability_conf
import os
from config.updateConf import UpdateConfig
from functs import killPid


# 更新配置
UpdateConfig().get_app_version(app=stability_conf.APP_URL)
UpdateConfig().get_login(name=stability_conf.LOGIN_USER_NAME, pw=stability_conf.LOGIN_PASS_WORD)
UpdateConfig().get_classname(classname=stability_conf.CLASSNAME)
UpdateConfig().get_yunpanfolder(folder=stability_conf.YUNPANFLODER)
UpdateConfig().get_classforcopy(classname=stability_conf.CLASSFORCOPY)


def run_course_activity():
    killPid.kill_pid()
    pytest.main(['-vs',
                 '-reruns=2', '-reruns-delay=2',
                 '../../testcase/test_Login.py::TestLogin',
                 '../../testcase/test_CreateClass.py::TestUseTargetClass',  # 使用指定班群
                 '../../testcase/test_CreateClass.py::TestChangeCourseTab',  # 切换到课程tab
                 '../../testcase/test_AddOnlineCourse.py::TestEnterClassRoomH5',  # 进入教室内
                 '../../testcase/test_AddOnlineCourse.py::TestLuKeEnter',  # 录课模式, 进入教室后的提示确认; 非录课模式不用


                 '../../testcase/stability/test_ClassRoomMonkey.py::TestMonkey'

                 ])


run_course_activity()