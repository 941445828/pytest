# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File:
"""
from config import stability_conf
from handler.getWinHandler import get_win
from version.v5000.pageobject.lmsCourse_page import LmsPage
from version.v5000 import *


class TestCreateLuboke:
    def test_switch_win_1(self, get_web_driver):
        """ 切换H5 页面"""
        time.sleep(2)
        get_win(get_web_driver, 0)

    def test_click_create_H5(self, get_web_driver):
        """ 课程tab下，H5上的【新建】"""
        LmsPage().click_H5_create(get_web_driver)

    def test_new_create_luboke(self,get_web_driver):
        """ 点击 新建里的  录播课"""
        LmsPage().click_luboke(get_web_driver)

    def test_switch_win_2(self,get_web_driver):
        """切换，H5页面"""
        get_new_page_special(get_web_driver,"unitName")

    def test_luboke_input_name(self, get_web_driver):
        """ 录播课，输入名称 """
        LmsPage().enter_luboke_name(get_web_driver)

    def test_luboke_click_yunpan(self,get_web_driver):
        """选择云盘"""
        LmsPage().click_yunpan(get_web_driver)

    def test_switch_win_3(self,get_web_driver):
        get_new_page_special(get_web_driver,"cloud")

    def test_luboke_choose_folder(self, get_web_driver):
        """选择云盘 文件夹"""
        LmsPage().choose_folder(get_web_driver, stability_conf.YUNPANFLODER)

    def test_luboke_choose_file(self,get_web_driver):
        """选择云盘 文件"""
        LmsPage().choose_file(get_web_driver)

    def test_luboke_click_ensure(self,get_web_driver):
        """ 点击 【 确定】"""
        LmsPage().click_btn_ensure(get_web_driver)

    def test_switch_win_4(self,get_web_driver):
        """ 切换 h5"""
        get_new_page_special(get_web_driver,"unitName=")

    def test_luboke_pulish(self, get_web_driver):
        """ 点击 发布"""
        LmsPage().click_publish_btn(get_web_driver)