# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File:
"""
from version.v5000.pageobject.lmsCourse_page import LmsPage
from version.v5000 import *
from handler.getWinHandler import get_win


# @pytest.mark.P1
class TestCreateKeTang:
    def test_switch_win_1(self, get_web_driver):
        get_new_page_special(get_web_driver,"course/list")

    def test_moveto_last_unit(self, get_web_driver):
        """ 焦点定位至单元列表的最后一个，让’+‘号显示出来"""
        LmsPage().move_to_unit(get_web_driver)

    def test_click_add_btn(self, get_web_driver):
        """ 点击'+'号 """
        LmsPage().click_add_btn(get_web_driver)
        time.sleep(2)

    def test_click_ketang(self, get_web_driver):
        """ 点击-课堂， 添加课堂 """
        LmsPage().click_ketang(get_web_driver)

    def test_native_change_win(self, get_driver):
        get_win(get_driver, -2)

    def test_click_online_mode(self, get_driver):
        LmsPage().click_online_mode(get_driver)

    def test_get_page_down(self, get_driver):
        LmsPage().get_page_down(get_driver)
        time.sleep(2)

    def test_click_luke_room(self, get_driver):
        LmsPage().click_luke_room(get_driver)

    def test_click_luke_onsite(self, get_driver):
        LmsPage().click_luke_onsite(get_driver)

    def test_click_page_zhibo(self, get_driver):
        LmsPage().click_page_zhibo(get_driver)

    def test_click_page_huifang(self, get_driver):
        LmsPage().click_page_huifang(get_driver)

    def test_new_create_ketang_publish(self, get_driver):
        """发布"""
        time.sleep(1)
        get_win(get_driver, -2)
        LmsPage().click_pulish_ketang(get_driver)


class TestCreateNoLuKeKeTang:
    def test_switch_win_1(self, get_web_driver):
        get_new_page_special(get_web_driver, "course/list")

    def test_click_create_H5(self, get_web_driver):
        """ 课程tab下，H5上的【新建】"""
        LmsPage().click_H5_create(get_web_driver)

    def test_new_create_ketang(self, get_web_driver):
        """ 点击 新建 --课堂"""
        LmsPage().click_ketang_new(get_web_driver)

    def test_native_change_win(self, get_driver):
        get_win(get_driver, -2)

    def test_click_online_mode(self, get_driver):
        LmsPage().click_online_mode(get_driver)

    def test_new_create_ketang_publish(self, get_driver):
        """发布"""
        time.sleep(1)
        get_win(get_driver, -2)
        LmsPage().click_pulish_ketang(get_driver)


class TestCreateLuKeKeTang:
    def test_switch_win_1(self, get_web_driver):
        get_new_page_special(get_web_driver, "course/list")

    def test_click_create_H5(self, get_web_driver):
        """ 课程tab下，H5上的【新建】"""
        LmsPage().click_H5_create(get_web_driver)

    def test_new_create_ketang(self, get_web_driver):
        """ 点击 新建 --课堂"""
        LmsPage().click_ketang_new(get_web_driver)

    def test_native_change_win(self, get_driver):
        get_win(get_driver, -2)

    def test_click_online_mode(self, get_driver):
        LmsPage().click_online_mode(get_driver)

    def test_get_page_down(self, get_driver):
        LmsPage().get_page_down(get_driver)
        time.sleep(2)

    def test_click_luke_room(self, get_driver):
        LmsPage().click_luke_room(get_driver)

    def test_click_luke_onsite(self, get_driver):
        LmsPage().click_luke_onsite(get_driver)


    def test_click_page_zhibo(self, get_driver):
        LmsPage().click_page_zhibo(get_driver)

    def test_click_page_huifang(self, get_driver):
        LmsPage().click_page_huifang(get_driver)

    def test_new_create_ketang_publish(self, get_driver):
        """发布"""
        time.sleep(1)
        get_win(get_driver, -2)
        LmsPage().click_pulish_ketang(get_driver)
