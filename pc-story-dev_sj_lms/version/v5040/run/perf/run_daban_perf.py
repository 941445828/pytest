# coding = utf-8
"""
@Author: sujie
@Create on: 2023-2
@Modify on:
@File:
2023/2，性能需求更新
需求：https://www.notion.so/eeoof/2-981df8625a9c4c3ab15fd576ea4ed817
"""


import threading
import pytest
from config.updateConf import UpdateConfig
from functs.collect_perf import Collect
from config import utils
from config import perf_conf


def luke():
    """创建 在线 录课模式 教室时长>=30分钟"""
    pytest.main(['-vs',
                 '../../testcase/test_Login.py::TestLogin',
                 '../../testcase/test_CreateClass.py::TestUseTargetClass',  # 使用指定班群
                 '../../testcase/test_CreateClass.py::TestChangeCourseTab',  # 切换到课程tab
                 '../../testcase/stability/class/test_Create_KeTang.py::TestAfterCreate::test_sleep',
                 '../../testcase/test_AddOnlineCourse.py::TestEnterClassRoomH5',  # 进入教室内
                 '../../testcase/test_AddOnlineCourse.py::TestLuKeEnter',  # 录课模式, 进入教室后的提示确认; 非录课模式不用
                 '../../testcase/test_AddOnlineCourse.py::TestSleep::test_sleep',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestAllStuLunBoPerf',   # 开启轮播
                 '../../testcase/stability/test_OnlineClassRoom.py::TestSettingCamera',     # 摄像头开启虚化
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolHandUpPerf',  # 举手自动上台
                 '../../testcase/test_OnlineOpenFile.py::TestUseYunPanPerf',
                 '../../testcase/test_OnlineOpenFile.py::TestUseWenDangPerf',
                 '../../testcase/test_OnlineOpenFile.py::TestUseTargetFolderGrid::test_click_target_folder_grid',
                 # 循环步骤， 第一次
                 '../../testcase/test_OnlineOpenFile.py::TestUseTargetFilePerf::test_choose_pdf_file',  # 打开第一个课件 pdf
                 '../../testcase/test_OnlineOpenFile.py::TestPDFOperationPerf',   # pdf课件上操作向下滚动、上一页、下一页
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolChatTextPerf',      # 发布聊天
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolPenPerf',       # 画笔
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolRubberPerf',    # 橡皮擦
                 '../../testcase/stability/test_OnlineClassRoom.py::TestTeacherRewardAllPerf',  # 给台上学生发奖励
                 # 循环步骤， 第二次
                 '../../testcase/test_OnlineOpenFile.py::TestUseYunPanPerf',
                 '../../testcase/test_OnlineOpenFile.py::TestUseTargetFilePerf::test_choose_mp4_file',  # 打开第二个课件 mp4
                 '../../testcase/test_OnlineOpenFile.py::TestMP4PlayPerf',  # mp4 播放\滚动条\启动循环
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolChatSendTextAndCutPerf',      # 发布聊天
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolPenPerf',       # 画笔
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolRubberPerf',    # 橡皮擦
                 '../../testcase/stability/test_OnlineClassRoom.py::TestTeacherRewardAllPerf',  # 给台上学生发奖励
                 # 循环步骤， 第三次
                 '../../testcase/test_OnlineOpenFile.py::TestUseYunPanPerf',
                 '../../testcase/test_OnlineOpenFile.py::TestUseTargetFilePerf::test_choose_ppt_file',  # 打开第三个课件 ppt
                 '../../testcase/test_OnlineOpenFile.py::TestPPTOperationPerf',  # ppt课件上操作上一页、下一页
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolChatSendTextAndCutPerf',      # 发布聊天
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolPenPerf',       # 画笔
                 '../../testcase/stability/test_OnlineClassRoom.py::TestToolRubberPerf',    # 橡皮擦
                 '../../testcase/stability/test_OnlineClassRoom.py::TestTeacherRewardAllPerf',  # 给台上学生发奖励
                 # 视频墙&多向屏幕共享
                 '../../testcase/stability/test_OnlineClassRoom.py::TestVideoOneScreenPerf',  # 视频墙--无扩展屏存在
                 '../../testcase/stability/test_OnlineClassRoom.py::TestShareTeacherPerf',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestShareStudentPerf',
                 '../../testcase/stability/test_OnlineClassRoom.py::TestResponderPerf',   # 抢答器
                 '../../testcase/stability/test_OnlineClassRoom.py::TestAnswerPerf',    # 答题器
                 '../../testcase/stability/test_OnlineClassRoom.py::TestBrowserPerf',   # 浏览器
                 '../../testcase/stability/test_OnlineClassRoom.py::TestSaveEdbPerf',   # 保存板书至本地
                 '../../testcase/stability/test_OnlineClassRoom.py::TestRewardRankPerf',  # 奖励排行榜
                 '../../testcase/stability/test_OnlineClassRoom.py::TestAllStuLunBoPerf',  # 关闭轮播
                 '../../testcase/stability/test_OnlineClassRoom.py::TestRubberClearScreenPerf',  # 用例中含有清屏弹窗提示
                 # 退出教室
                 '../../testcase/test_QuitOnlineClassRoom.py::TestQuitLuKeOnlyOne',  # 仅自己退出
                 '../../testcase/test_QuitAPP.py'
                 ])


def collect():
    cpu_file_url = utils.get_cpu_csv_url(perf_conf.cpu_csv_name)  # 自定义CSV文件名字
    mem_file_url = utils.get_mem_csv_url(perf_conf.mem_csv_name)  # 自定义CSV文件名字
    Collect().collect(cpu_file_url, mem_file_url)


def luke_run():
    t1 = threading.Thread(target=luke)
    t2 = threading.Thread(target=collect)

    t1.start()
    t2.start()


if __name__ == "__main__":
    UpdateConfig().get_use_fps(is_use_fps=perf_conf.IS_USE_FPS)
    UpdateConfig().get_app_version(app=perf_conf.APP_URL)
    UpdateConfig().get_webdriver_version(webdriver_version=perf_conf.WEBDRIVER_VERSION)
    UpdateConfig().get_login(name=perf_conf.LOGIN_USER_NAME, pw=perf_conf.LOGIN_PASS_WORD)
    UpdateConfig().get_classname(classname=perf_conf.CLASSNAME)
    luke_run()