# coding = utf-8
"""
教室内稳定性脚本： 支持在线教室的 录课模式 和 非录课模式。 前置设置：需要先建好录课模式 或 非录课模式的在线教室。

注1：在线教室内工具栏顺序需为：点击、选择、画笔、橡皮擦、文本工具、截图、激光笔、云盘、工具箱、课程、课堂笔记、聊天、花名册， 否则容易报错
注2： 工具箱默认展示两行，顺序如下，否则容易报错。
第一行：打开文件、保存/分享板书、屏幕共享、骰子； 第二行：答题器、小黑板、计时器、定时器
展开更多后，第三行：投屏工具、抢答器、随机选人、分组讨论； 第四行：协作、奖励排行榜、浏览器、物理实验
第五行：化学实验、教学素材库、辅助摄像头、VNC； 第六行： 作业、测验、拖拽激光笔、 直播聊天
第七行：视频墙、 围棋小黑板、尺规工具、几何图形。

注3： 使用投屏工具功能时，首次使用会有系统弹窗，可以先行人工干预，关闭弹窗
注4： 云盘的元素定位，匹配使用默认的网格视图查找 （列表视图会找不到）
"""
import pytest
from config import stability_conf
from config.updateConf import UpdateConfig
from functs import killPid


# 更新配置
UpdateConfig().get_app_version(app=stability_conf.APP_URL)
UpdateConfig().get_login(name=stability_conf.LOGIN_USER_NAME, pw=stability_conf.LOGIN_PASS_WORD)
UpdateConfig().get_classname(classname=stability_conf.CLASSNAME)


def run_online_classroom():
    killPid.kill_pid()
    pytest.main(['-vs',
                 '-reruns=2', '-reruns-delay=2',
                 '../../testcase/test_Login.py::TestLogin',
                 '../../testcase/test_CreateClass.py::TestUseTargetClass',
                 '../../testcase/test_CreateClass.py::TestChangeCourseTab',
                 '../../testcase/test_AddOnlineCourse.py::TestEnterClassRoomH5',  # 进入教室内
                 '../../testcase/test_AddOnlineCourse.py::TestLuKeEnter',  # 录课模式, 进入教室后的提示确认; 非录课模式不用
                 '../../testcase/stability/test_OnlineClassRoom.py::TestSettingCamera',  # 摄像头开启虚化
                 '../../testcase/stability/test_OnlineClassRoom.py::TestOnlineDoubleClickCamera',  # 摄像头全屏
                 '../../testcase/stability/test_OnlineClassRoom.py::TestAllStuMute',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolHandUp',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestAllStuEmpower',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestAllStuLunBo',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestOnlineCamera',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestCameraReset',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolPen',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolChoose',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolText',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolCut',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolRubber',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolNote',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolChat',
                 '../../testcase/test_OnlineOpenFile.py::TestUseYunPanPerf',
                 '../../testcase/test_OnlineOpenFile.py::TestUseWenDangPerf',
                 '../../testcase/test_OnlineOpenFile.py::TestUseTargetFolderGrid::test_click_target_folder_grid',
                 '../../testcase/test_OnlineOpenFile.py::TestOpenFile::test_open_files_random_grid',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestRoster',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestOnlineYunPanCloseFile',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolBoxOpenFile',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestSaveEdbToLocal',    # 保存板书到本地
                 '../../testcase/stability/test_OnlineClassRoom.py::TestShaiZi',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestDaTiQi',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestJiShiQi',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestDingShiQi',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestAllStuOff',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestShareDeskTop',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestShareTeacher',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestPaintUsePen',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestPaintUseText',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestTextEdit',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestBrowser',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestGroupDiscuss', # 课节中需要有2个以上的学生存在
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestVideo',     # 视频墙--有扩展屏存在
                 '../../testcase/stability/test_OnlineClassRoom.py::TestVideoOneScreen',  # 视频墙--无扩展屏存在
                 '../../testcase/stability/test_OnlineClassRoom.py::TestMaterial',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestRuler',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestTouPing',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestSuiJiXuanRen',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestCollaboration',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestRewardRank',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestAssistCamera',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestGo',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestGeometry',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestSaveEdbToYunPan',  # 保存板书到云盘
                 '../../testcase/stability/test_OnlineClassRoom.py::TestRubberClearScreen',  # 用例中含有清屏弹窗提示
                 # '../../testcase/test_QuitOnlineClassRoom.py::TestQuitNoLuKeOnlyOne',  # 非录课模式, 仅自己离开教室
                 '../../testcase/test_QuitOnlineClassRoom.py::TestQuitLuKeOnlyOne',    # 录课模式, 仅自己离开教室
                 '../../testcase//stability/test_OnlineClassRoom.py::TestClassOverAppraise', # 若退出教室无评价弹窗，可以省略此步
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
