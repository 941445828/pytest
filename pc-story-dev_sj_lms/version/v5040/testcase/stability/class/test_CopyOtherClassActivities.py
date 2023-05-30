# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File:
"""
from version.v5010.pageobject.lmsCourse_page import LmsPage
from handler.yamlHandler import get_data
from version.v5010 import *


class TestCopyOtherClassActivities:
    def test_switch_win_1(self, get_web_driver):
        get_new_page_special(get_web_driver,"&role=manager")

    def test_click_create_H5(self, get_web_driver):
        """ 课程tab下，H5上的【新建】"""
        LmsPage().click_H5_create(get_web_driver)

    def test_copy_class_activity(self, get_web_driver):
        LmsPage().click_copy(get_web_driver)

    def test_switch_win_2(self, get_web_driver):
        get_new_page_special(get_web_driver,"import")

    def test_copy_select_class(self, get_web_driver):
        case = get_data('baseConf.yaml')[0]
        copy_class = case['class_for_copy']
        LmsPage().choose_class(get_web_driver, copy_class)

    def test_switch_win_3(self, get_web_driver):
        get_new_page_special(get_web_driver,"activity-select")

    def test_select_unit(self, get_web_driver):
        LmsPage().choose_unit(get_web_driver)

    def test_copy_class_continue(self,get_web_driver):
        LmsPage().click_Continue(get_web_driver)

    def test_switch_win_4(self, get_web_driver):
        get_new_page_special(get_web_driver,"activity-setting")

    def test_copy_class_insure(self,get_web_driver):
        LmsPage().click_sure(get_web_driver)




