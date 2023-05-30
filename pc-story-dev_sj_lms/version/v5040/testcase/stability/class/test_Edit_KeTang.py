# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File:
"""
from config import stability_conf
from handler.getWinHandler import get_win
from version.v5040.pageobject.createClass_page import ClassPageUseReload
from version.v5040.pageobject.lmsCourse_page import LmsPage
from version.v5040 import *


class TestEditKetang:
    def test_switch_win_1(self, get_web_driver):
        get_new_page_special(get_web_driver,"course/list")

    def test_click_search_logo(self,get_web_driver):
        LmsPage().click_search_logo(get_web_driver)

    def test_enter_search_content(self, get_web_driver):
        LmsPage().enter_search_content(get_web_driver, stability_conf.CLASSNAME, 20)

    # 11/15修改搜索bug后，交互变了，这个不要了; # 12.30又更改回来了
    # def test_switch_win_11(self, get_web_driver):
    #     get_new_page_special(get_web_driver,"searchKey=" + stability_conf.CLASSNAME)

    def test_click_ketang_item(self,get_web_driver):
        LmsPage().click_activities_item(get_web_driver)

    def test_switch_win_2(self, get_web_driver):
        get_new_page_special(get_web_driver,"processFlag")

    def test_click_edit_enter(self,get_web_driver):
        LmsPage().click_ketang_edit_enter(get_web_driver)

    def test_click_edit(self, get_web_driver):
        LmsPage().click_edit_btn(get_web_driver)

    def test_switch_win_3(self, get_driver):
        time.sleep(1)
        get_win(get_driver, 0)

    def test_switch_win_33(self, get_web_driver):
        get_new_page_special(get_web_driver,"unitId")

    def test_edit_allow_check(self, get_web_driver):
        LmsPage().click_edit_allow_check(get_web_driver)

    def test_click_edit_ensure(self, get_driver):
        LmsPage().click_edit_ensure_native(get_driver)

    def test_switch_win_4(self, get_web_driver):
        get_new_page_special(get_web_driver,"processFlag")

    def test_edit_ketang_close_12(self,get_web_driver):
        LmsPage().click_ketang_page_closed(get_web_driver)

    # def test_switch_win_5(self, get_web_driver):
    #     get_new_page_special(get_web_driver,"&searchKey=" + stability_conf.CLASSNAME)

    def test_switch_win_5(self, get_web_driver):
        get_new_page_special(get_web_driver, "course/list")

    # def test_search_content_del(self,get_web_driver):
    #     """ 清除搜索内容 """
    #     LmsPage().enter_search_content_del(get_web_driver)

    def test_switch_win_6(self, get_driver):
        get_win(get_driver, 0)
        time.sleep(2)

    def test_click_reload(self, get_driver):
        ClassPageUseReload().click_class_page_reload_btn(get_driver)



