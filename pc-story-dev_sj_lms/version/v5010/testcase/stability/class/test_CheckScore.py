# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File:
"""
from handler.getWinHandler import get_win
from version.v5010.pageobject.lmsCourse_page import LmsPage
from handler.logHandler import logger
from version.v5010 import *


class TestChangeWin:
    def test_switch_win(self, get_driver):
        logger.info('窗口list： {}'.format(get_driver.window_handles))
        get_win(get_driver,0)
        time.sleep(2)

class TestCheckScore:
    def test_switch_win_1(self, get_web_driver):
        get_new_page_special(get_web_driver,"score")

    def test_change_to_study_activity(self,get_web_driver):
        """切换到 学习活动 tab"""
        LmsPage().click_study_activity(get_web_driver)

    def test_click_student(self,get_web_driver):
        """ 点击 学生列表 下的 第一个人"""
        LmsPage().click_student(get_web_driver)

    def test_switch_win_2(self, get_web_driver):
        get_new_page_special(get_web_driver,"&role=manager&isStudentView=")

    def test_view_score_close_05(self,get_web_driver):
        """关闭 学生 成绩页面"""
        LmsPage().click_score_page_closed(get_web_driver)