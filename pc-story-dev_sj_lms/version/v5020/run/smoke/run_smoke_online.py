# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 冒烟测试：在线教室--录课模式, 各功能冒烟case
       登录-创建课程-创建课节-进入教室内-功能点smoke
"""
import pytest


def smoke_online():
    pytest.main(['-vsq',
                 '../../testcase/test_Login.py',
                 '../../testcase/test_CreateClass.py::TestCreateClass',
                 '../../testcase/test_AddOnlineCourse.py::TestAddOnlineCourseLuKe',  # 创建课节--录课模式
                 '../../testcase/test_CreateClass.py::TestChangeCourseTab',
                 '../../testcase/test_AddOnlineCourse.py::TestEnterClassRoom',  # 进入教室内
                 '../../testcase/test_AddOnlineCourse.py::TestLuKeEnter',  # 录课模式, 进入教室后的提示确认; 非录课模式不用
                 '../../testcase/stability/test_OnlineClassRoom.py::TestAllStuMute',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolHandUp',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestAllStuEmpower',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestLunBoSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestCameraSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestCameraReset',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolPenSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolChooseSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolTextSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolRubberSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolNoteSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolChatSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestOnlineYunPanOpenFileSmoke',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestRoster', # 暂时不要
                 '../../testcase/stability/test_OnlineClassRoom.py::TestOnlineYunPanCloseFileSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolBoxOpenFileSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestSaveEdb',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestShaiZiSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestDaTiQiSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestJiShiQi',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestDingShiQiSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestAllStuOff',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestShareDeskTop',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestShareTeacher',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestPaintUsePenSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestTextEditSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestBrowserSmoke',
                 # '../../testcase/stability/test_OnlineClassRoom.py::TestGroupDiscuss',   # 新建班群无学生，不能分组
                 '../../testcase/stability/test_OnlineClassRoom.py::TestVideo',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestMaterialSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestRulerSmoke',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestRubberClearScreen',
                 '../../testcase/test_QuitOnlineClassRoom.py::TestQuitOnlineClassRoom',
                 '../../testcase/test_QuitAPP.py'
                 ])


smoke_online()