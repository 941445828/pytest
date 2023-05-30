# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File: 班群--课程--创建: 课堂2；录播课3；作业4；测验6； 讨论7； 学习资料8； 单元主题9； 公共复用方法； 查看学生成绩
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


if __name__ == "__main__":
    killPid.kill_pid()
    pytest.main(['-vs',
                 '-reruns=2', '-reruns-delay=2',
                 '../../testcase/test_Login.py::TestLogin',
                 '../../testcase/test_CreateClass.py::TestUseTargetClass',  #  使用班群
                 '../../testcase/test_CreateClass.py::TestChangeCourseTab',  # 切换到课程tab
                 '../../testcase/stability/class/test_Create_KeTang.py',
                 '../../testcase/stability/class/test_Create_Luboke.py',
                 '../../testcase/stability/class/test_Create_Homework.py',
                 '../../testcase/stability/class/test_Create_Exam.py',
                 '../../testcase/stability/class/test_Create_Discuss.py',
                 '../../testcase/stability/class/test_Create_LearningMaterials.py',
                 '../../testcase/stability/class/test_Create_UnitTopic.py',
                 '../../testcase/stability/class/test_CopyOtherClassActivities.py',
                 '../../testcase/stability/class/test_CheckScore.py::TestChangeWin',
                 '../../testcase/test_CreateClass.py::TestChangeScoreTab',  # 切换到成绩tab
                 '../../testcase/stability/class/test_CheckScore.py::TestCheckScore'
                 ])