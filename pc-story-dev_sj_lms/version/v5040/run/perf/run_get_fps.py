# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
import pytest
import threading
from config.updateConf import UpdateConfig
from functs.collect_perf import Collect
from config import utils
from config import perf_conf


if __name__ == '__main__':
    UpdateConfig().get_app_version(app=perf_conf.APP_URL)
    UpdateConfig().get_webdriver_version(webdriver_version=perf_conf.WEBDRIVER_VERSION)
    UpdateConfig().get_login(name=perf_conf.LOGIN_USER_NAME, pw=perf_conf.LOGIN_PASS_WORD)
    UpdateConfig().get_classname(classname=perf_conf.CLASSNAME)
    pytest.main(['-vs',
                 '../../testcase/test_Login.py',
                 '../../testcase/test_CreateClass.py::TestUseTargetClass',
                 '../../testcase/test_CreateClass.py::TestChangeCourseTab',
                 '../../testcase/test_AddOnlineCourse.py::TestEnterClassRoomH5',  # 进入教室内
                 '../../testcase/test_AddOnlineCourse.py::TestLuKeEnter',  # 录课模式, 进入教室后的提示确认; 非录课模式不用
                 '../../testcase/perf/test_GetFPS.py'
                 ])
