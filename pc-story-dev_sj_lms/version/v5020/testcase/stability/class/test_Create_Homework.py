# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File:
"""

from version.v5000.pageobject.lmsCourse_page import LmsPage
from version.v5000 import *


class TestCreateHomework:
    def test_switch_win_1(self, get_web_driver):
        get_new_page_special(get_web_driver,"&role=manager")

    def test_click_create_H5(self, get_web_driver):
        """ 课程tab下，H5上的【新建】"""
        LmsPage().click_H5_create(get_web_driver)

    def test_new_create_hw(self,get_web_driver):
        """ 点击 新建里的 作业"""
        LmsPage().click_homework(get_web_driver)

    def test_switch_win_2(self, get_web_driver):
        get_new_page_special(get_web_driver,"homework")

    def test_hw_input_name(self, get_web_driver):
        """ 作业，输入名称 """
        LmsPage().enter_hw_name(get_web_driver)

    def test_hw_input_content(self,get_web_driver):
        """ 作业，输入内容 """
        LmsPage().enter_hw_content(get_web_driver)

    def test_hw_publish(self, get_web_driver):
        """ 点击 发布"""
        LmsPage().click_publish_btn(get_web_driver)