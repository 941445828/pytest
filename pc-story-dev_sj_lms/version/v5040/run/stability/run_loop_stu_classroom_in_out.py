# coding = utf-8
"""
@Author: jie.su
@Create on:
@Modify on:
@File: 学生身份，循环运行：进入教室-退出教室

此脚本需要前置动作：
老师动作： 开启一个教室，老师打开摄像头、麦克风、打开mp3播放且循环、打开MP4播放且循环（可以加入一个其他学生，也起开摄像头、麦克风）
学生动作：需要先登录ClassIn（只登录，在im页面即可），学生启动本脚本后，将鼠标焦点聚焦在ClassIn客户端上（否则找不到会报错）
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
    pytest.main(['-vs', '--count=150', '--repeat-scope=session',  #  进出教室几次，修改count值
                 # 进入班群
                 '../../testcase/test_CreateClass.py::TestUseTargetClass',

                 # 进入教室内
                 '../../testcase/test_CreateClass.py::TestChangeCourseTab',
                 '../../testcase/test_AddOnlineCourse.py::TestStuEnterClassRoomH5::test_switch_win_1',
                 '../../testcase/stability/test_Stu_ClassRoom_In_Out.py::TestClassCourseReload::test_click_reload',
                 '../../testcase/test_AddOnlineCourse.py::TestStuEnterClassRoomH5::test_stu_click_search_logo',
                 '../../testcase/test_AddOnlineCourse.py::TestEnterClassRoomH5::test_enter_search_content',
                 '../../testcase/test_AddOnlineCourse.py::TestEnterClassRoomH5::test_begin_class',
                 '../../testcase/test_AddOnlineCourse.py::TestEnterClassRoomH5::test_changeto_native_driver',

                 # 教室内停留30s
                 '../../testcase/stability/test_Stu_ClassRoom_In_Out.py::TestStuSleep::test_stu_sleep',

                 # 退出教室
                 '../../testcase/test_QuitOnlineClassRoom.py::TestStuQuitOnlineClassRoom',

                 # 操作评价框
                 '../../testcase/stability/test_OnlineClassRoom.py::TestStuClassOverAppraise::test_cancel',   # 若班级无学生，可以省略此步
                 ])


run_stu()