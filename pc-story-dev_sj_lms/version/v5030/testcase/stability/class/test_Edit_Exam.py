# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File:
"""
from version.v5000.pageobject.createClass_page import ClassPageUseReload
from version.v5000.pageobject.lmsCourse_page import LmsPage
from version.v5000 import *
from handler.getWinHandler import get_win


class TestEditExam:
    def test_switch_win_1(self, get_web_driver):
        # get_new_page_special(get_web_driver,"&role=manager")
        get_new_page_special(get_web_driver,"course/list")

    def test_click_search_logo(self,get_web_driver):
        LmsPage().click_search_logo(get_web_driver)

    def test_enter_search_content(self, get_web_driver):
        LmsPage().enter_search_content(get_web_driver, 'zjw_exam', 10)

    def test_click_exam_item(self,get_web_driver):
        LmsPage().click_activities_item(get_web_driver)

    def test_switch_win_2(self,get_web_driver):
        get_new_page_special(get_web_driver,"&role=manager&activityId=")

    def test_click_edit_enter(self,get_web_driver):
        LmsPage().click_exam_edit_enter(get_web_driver)

    def test_click_edit(self, get_web_driver):
        LmsPage().click_edit_btn(get_web_driver)

    def test_switch_win_3(self,get_web_driver):
        #  https://wsevlw001.eeo.im/client/pages/qbank/pc/?courseId=123239&role=manager&activityId=2492670&routerTo=ExamEditor&step=2#/ExamEditor
        get_new_page_special(get_web_driver,"&routerTo=ExamEditor&")

    def test_click_exam_edit_ensure(self, get_web_driver):
        time.sleep(2)
        LmsPage().click_exam_edit_ensure(get_web_driver)

    def test_switch_win_4(self,get_web_driver):
        time.sleep(2)  #  等待一下，否则切换页面报错机率高
        get_new_page_special(get_web_driver,"activityId=")

    def test_edit_exam_closed(self,get_web_driver):
        LmsPage().click_exam_page_closed(get_web_driver)


    def test_switch_win_5(self,get_web_driver):
        get_new_page_special(get_web_driver,"&searchKey=zjw_exam")

    def test_search_content_del(self,get_web_driver):
        """ 清除搜索内容 """
        LmsPage().enter_search_content_del(get_web_driver)

    def test_switch_win_6(self, get_driver):
        get_win(get_driver, 0)
        time.sleep(2)

    def test_click_reload(self, get_driver):
        ClassPageUseReload().click_class_page_reload_btn(get_driver)