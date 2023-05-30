# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File:
"""
from version.v5000.pageobject.lmsCourse_page import LmsPage
from version.v5000 import *


class TestCreateLearningMaterials:
    def test_switch_win_1(self, get_web_driver):
        get_new_page_special(get_web_driver,"&role=manager")

    def test_click_create_H5(self, get_web_driver):
        """ 课程tab下，H5上的【新建】"""
        LmsPage().click_H5_create(get_web_driver)

    def test_new_create_learning_materials(self, get_web_driver):
        LmsPage().click_learning(get_web_driver)

    def test_switch_win_2(self, get_web_driver):
        get_new_page_special(get_web_driver,"/material/")

    def test_learning_materials_title(self,get_web_driver):
        LmsPage().enter_learn_title(get_web_driver)

    def test_learning_materials_content(self,get_web_driver):
        LmsPage().enter_learn_content(get_web_driver)

    def test_learning_materials_publish(self,get_web_driver):
        LmsPage().click_publish_btn(get_web_driver)




