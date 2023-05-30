# coding = utf-8
"""
@Author: jie.su
@Create on:
@Modify on:
@File:
老师身份，循环运行：
标题栏处，摄像头开启/关闭
设置窗口里--视频tab，本地摄像头/禁用

前提：指定班群下需要有一个正在进行中的课节存在
"""
import pytest
from config import stability_conf
from config.updateConf import UpdateConfig


# 更新配置
UpdateConfig().get_app_version(app=stability_conf.APP_URL)
UpdateConfig().get_webdriver_version(webdriver_version=stability_conf.WEBDRIVER_VERSION)
UpdateConfig().get_login(name=stability_conf.LOGIN_USER_NAME, pw=stability_conf.LOGIN_PASS_WORD)
UpdateConfig().get_classname(classname=stability_conf.CLASSNAME)


def run_stu():
    pytest.main(['-vs',
                 '../../testcase/test_Login.py::TestLogin',
                 '../../testcase/test_CreateClass.py::TestUseTargetClass',  # 使用指定班群
                 '../../testcase/test_CreateClass.py::TestChangeCourseTab',  # 切换到课程tab
                 '../../testcase/test_AddOnlineCourse.py::TestEnterClassRoomH5',  # 进入教室内
                 '../../testcase/test_AddOnlineCourse.py::TestLuKeEnter',  # 录课模式, 进入教室后的提示确认; 非录课模式不用
                  # 循环对摄像头的设置操作
                 '../../testcase/stability/test_Teac_Loop_Camera_Setting.py'
                 ])


run_stu()

