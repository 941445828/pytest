# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File:
"""
from version.v5000.pageobject.lmsCourse_page import LmsPage
from version.v5000 import *


class TestCreateDiscuss:
    def test_switch_win_1(self, get_web_driver):
        get_new_page_special(get_web_driver,"&role=manager")

    def test_click_create_H5(self, get_web_driver):
        """ 课程tab下，H5上的【新建】"""
        LmsPage().click_H5_create(get_web_driver)

    def test_new_create_discuss(self,get_web_driver):
        """ 点击 新建里的 讨论"""
        LmsPage().click_discuss(get_web_driver)

    def test_switch_win_2(self, get_web_driver):
        get_new_page_special(get_web_driver,"discuss")

    def test_discuss_input_title(self,get_web_driver):
        """ 填写 讨论 标题 """
        LmsPage().enter_dis_title(get_web_driver)

    def test_discuss_input_content(self,get_web_driver):
        """ 填写 讨论 内容"""
        LmsPage().enter_dis_content(get_web_driver)

    def test_discuss_publish(self,get_web_driver):
        """ 发布"""
        LmsPage().click_publish_btn(get_web_driver)
