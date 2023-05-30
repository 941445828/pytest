# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File:
"""
from version.v5000.pageobject.lmsCourse_page import LmsPage
from version.v5000 import *


class TestCreateExam:
    def test_switch_win_1(self, get_web_driver):
        get_new_page_special(get_web_driver,"&role=manager")

    def test_click_create_H5(self, get_web_driver):
        """ 课程tab下，H5上的【新建】"""
        LmsPage().click_H5_create(get_web_driver)

    def test_new_create_exam(self,get_web_driver):
        """ 点击 新建里的 测验"""
        LmsPage().click_exam(get_web_driver)

    def test_switch_win_2(self, get_web_driver):
        get_new_page_special(get_web_driver,"/ExamEditor")
        time.sleep(5)

    def test_exam_select_all(self,get_web_driver):
        """ 选题"""
        LmsPage().click_select_item(get_web_driver)

    def test_paper_set(self,get_web_driver):
        """组卷设置"""
        LmsPage().click_select_set(get_web_driver)

    def test_paper_title(self,get_web_driver):
        """输入 试卷 标题"""
        LmsPage().enter_exam_title(get_web_driver)

    def test_paper_publish(self,get_web_driver):
        """ 发布 """
        LmsPage().click_exam_publish(get_web_driver)



