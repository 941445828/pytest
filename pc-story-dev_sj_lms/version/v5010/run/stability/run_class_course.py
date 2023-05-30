# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File: 班群--课程--创建: 课堂、录播课、作业、测验、讨论、学习资料、单元主题； 公共复用方法； 查看学生成绩
        编辑: 课堂、录播课、作业、测验、讨论、学习资料
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
                 '../../testcase/test_CreateClass.py::TestUseTargetClass',  #  使用班群
                 '../../testcase/test_CreateClass.py::TestChangeCourseTab',  # 切换到课程tab
                 '../../testcase/stability/class/test_Create_UnitTopic.py',
                 '../../testcase/stability/class/test_Create_KeTang.py::TestCreateKeTang',  # 创建
                 '../../testcase/stability/class/test_Create_Luboke.py',
                 '../../testcase/stability/class/test_Create_Homework.py',
                 '../../testcase/stability/class/test_Create_Exam.py',
                 '../../testcase/stability/class/test_Create_Discuss.py',
                 '../../testcase/stability/class/test_Create_LearningMaterials.py',
                 '../../testcase/stability/class/test_CopyOtherClassActivities.py',
                 '../../testcase/stability/class/test_CheckScore.py::TestChangeWin',
                 '../../testcase/test_CreateClass.py::TestChangeScoreTab',  # 切换到成绩tab
                 '../../testcase/stability/class/test_CheckScore.py::TestCheckScore',
                 '../../testcase/test_CreateClass.py::TestChangeCourseTab',  # 切换到课程tab
                 '../../testcase/stability/class/test_Edit_KeTang.py',  # 编辑
                 '../../testcase/stability/class/test_Edit_Luboke.py',
                 '../../testcase/stability/class/test_Edit_Homework.py',
                 '../../testcase/stability/class/test_Edit_Exam.py',
                 '../../testcase/stability/class/test_Edit_Discuss.py',
                 '../../testcase/stability/class/test_Edit_LearnMaterials.py',
                 '../../testcase/test_QuitAPP.py'
                 ])

while True:
    run_course_activity()