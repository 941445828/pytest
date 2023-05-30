# coding = utf-8
"""
@Author: jie.su
@Create on:
@Modify on:
@File: 稳定性之循环执行  启动app-登录-退出 操作
"""
import pytest
from config import stability_conf
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
                 '../../testcase/test_QuitAPP.py'
                 ])


while True:
    run_course_activity()