# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File: 班群--课程--编辑: 课堂11；录播课12；作业13；测验14； 讨论15； 学习资料16；
"""
import pytest
from config import stability_conf
import os
from config.updateConf import UpdateConfig
from functs import killPid


UpdateConfig().get_app_version(app=stability_conf.APP_URL)
UpdateConfig().get_webdriver_version(webdriver_version=stability_conf.WEBDRIVER_VERSION)
UpdateConfig().get_login(name=stability_conf.LOGIN_USER_NAME, pw=stability_conf.LOGIN_PASS_WORD)
UpdateConfig().get_classname(classname=stability_conf.CLASSNAME)
UpdateConfig().get_yunpanfolder(folder=stability_conf.YUNPANFLODER)
UpdateConfig().get_classforcopy(classname=stability_conf.CLASSFORCOPY)


if __name__ == '__main__':
    killPid.kill_pid()
    pytest.main(['-vs',
                 '-reruns=2', '-reruns-delay=2',
                 '../../testcase/test_Login.py::TestLogin',
                 '../../testcase/test_CreateClass.py::TestUseTargetClass',  # 使用班群
                 '../../testcase/test_CreateClass.py::TestChangeCourseTab',  # 切换到课程tab
                 '../../testcase/stability/class/test_Edit_KeTang.py',
                 '../../testcase/stability/class/test_Edit_Luboke.py',
                 '../../testcase/stability/class/test_Edit_Homework.py',
                 '../../testcase/stability/class/test_Edit_Exam.py',
                 '../../testcase/stability/class/test_Edit_Discuss.py',
                 '../../testcase/stability/class/test_Edit_LearnMaterials.py'
])

