# coding = utf-8
"""
@Author: jie.su
@Create on:
@Modify on:
@File:
老师身份，循环运行：
视频文件： 开启播放—调整进度—暂停播放—调整进度
音频文件： 开启播放—调整进度—暂停播放—调整进度


此脚本需要前置动作：
老师动作： 登录ClassIn后，进入教室，打开后面脚本要操作的音、视频文件，退出教室，停留在im页面，运行脚本

"""
import pytest
from config import stability_conf
from config.updateConf import UpdateConfig


# 更新配置
UpdateConfig().get_app_version(app=stability_conf.APP_URL)
UpdateConfig().get_login(name=stability_conf.LOGIN_USER_NAME, pw=stability_conf.LOGIN_PASS_WORD)
UpdateConfig().get_classname(classname=stability_conf.CLASSNAME)


def run_stu():
    pytest.main(['-vs',
                 '../../testcase/test_CreateClass.py::TestUseTargetClass',  # 使用指定班群
                 '../../testcase/test_CreateClass.py::TestChangeCourseTab',  # 切换到课程tab
                 '../../testcase/test_AddOnlineCourse.py::TestEnterClassRoomH5',  # 进入教室内
                 '../../testcase/test_AddOnlineCourse.py::TestLuKeEnter',  # 录课模式, 进入教室后的提示确认; 非录课模式不用
                 # 循环对文件开始/暂停/调整进度条的操作
                 '../../testcase/stability/test_Teac_Loop_File.py::TestTeacherLoopFile::test_teacher_loop_mp3_mp4'
                 ])


run_stu()

