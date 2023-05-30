# coding = utf-8
"""
智慧教室 稳定性脚本： 支持录课模式 和 非录课模式。 前置设置：需要先建好录课模式 或 非录课模式的在线教室。
"""
import pytest
from config import stability_conf
from config.updateConf import UpdateConfig


# 更新配置
UpdateConfig().get_app_version(app=stability_conf.APP_URL)
UpdateConfig().get_login(name=stability_conf.LOGIN_USER_NAME, pw=stability_conf.LOGIN_PASS_WORD)
UpdateConfig().get_classname(classname=stability_conf.CLASSNAME)


def run_online_classroom():
    pytest.main(['-vs',
                 '-reruns=2', '-reruns-delay=2',
                 '../../testcase/test_Login.py',
                 '../../testcase/test_CreateClass.py::TestUseTargetClass',
                 '../../testcase/test_CreateClass.py::TestChangeCourseTab',
                 '../../testcase/test_AddOnlineCourse.py::TestEnterWisdomClassRoomH5',  # 进入教室内
                 # '../../testcase/test_AddOnlineCourse.py::TestLuKeEnter',  # 录课模式, 进入教室后的提示确认; 非录课模式不用
                 # 获取不到元素相关

                 # '../../testcase/stability/test_OnlineClassRoom.py::TestAllStuMute',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestToolHandUp',
                 # # '../../testcase/stability/test_OnlineClassRoom.py::TestAllStuEmpower',   # LMS没有全体授权
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestAllStuLunBo',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestOnlineCamera',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestCameraReset',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestToolPen',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestToolChoose',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestToolText',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestToolCut',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestToolRubber',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestToolNote',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestToolChat',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestOnlineYunPanOpenFile',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestRoster',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestOnlineYunPanCloseFile',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestToolBoxOpenFile',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestSaveEdb',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestShaiZi',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestDaTiQi',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestJiShiQi',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestDingShiQi',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestAllStuOff',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestShareDeskTop',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestShareTeacher',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestPaintUsePen',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestPaintUseText',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestTextEdit',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestBrowser',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestGroupDiscuss',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestVideo',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestMaterial',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestRuler',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestRubberClearScreen',
                 #
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestTouPing',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestSuiJiXuanRen',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestCollaboration',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestRewardRank',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestAssistCamera',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestGo',
                 '../../testcase/stability/test_WisdomClassRoom.py::TestFocusMode',
                # 退出
                 '../../testcase/test_QuitWisdomClassRoom.py::TestQuitWisdomClassRoom',  # 退出
                 # '../../testcase/test_QuitWisdomClassRoom.py::TestQuitEnsure',    # 录课模式,退出确认；非录课模式不需要
                 '../../testcase//stability/test_OnlineClassRoom.py::TestClassOverAppraise', # 若班级无学生，可以省略此步
                 '../../testcase/test_QuitAPP.py'
                 ])


while True:
    run_online_classroom()



# 举手、聊天、设置（NO）、画笔、花名册、选择&移动、橡皮、点击、文字、云盘
# 定时器、多向屏共享、答题器、小黑板、保存/分享板书、加载图片/板书
# 浏览器、视频墙、骰子、随机选人、抢答器、教学素材库、计时器、尺规工具
# 桌面共享、分组讨论、作业、拖拽激光笔、化学实验、围棋小黑板、奖励排行榜
# 物理实验室、文本写作、苹果投屏、辅助摄像头、测验、共享工具、ClassIn投屏

# 优化
#  屏幕共享--新样式； 投屏工具-系统提示； 视频墙-支持一个屏幕的情况； 所有功能涉及到保存本地的--更改保存的位置； 加了一个几何图形工具； 教室内的设置覆盖一下功能
