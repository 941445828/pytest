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
import allure
from config import *


@allure.feature("班级")
@allure.story("测试--创建课堂（稳定性用）")
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


@allure.feature("班级")
@allure.story("测试--创建非录课课堂")
class TestCreateNoLuKeKeTang:
    @allure.title('H5，切换页面')
    @allure.description("H5，切换页面")
    def test_switch_win_1(self, get_web_driver, get_function_name):
        get_new_page_special(get_web_driver, "course/list")

    @allure.title('点击新建')
    @allure.description("课程tab下点击新建")
    def test_click_create_H5(self, get_web_driver, get_function_name):
        """ 课程tab下，H5上的【新建】"""
        LmsPage().click_H5_create(get_web_driver)

    @allure.title('选择新建课堂')
    @allure.description("选择新建课堂")
    def test_new_create_ketang(self, get_web_driver, get_function_name):
        """ 点击 新建 --课堂"""
        LmsPage().click_ketang_new(get_web_driver)

    @allure.title('原生，切换窗口')
    @allure.description("原生，切换窗口")
    def test_native_change_win(self, get_driver, get_function_name):
        get_win(get_driver, -2)

    @allure.title('选择在线教室模式')
    @allure.description("选择在线教室模式")
    def test_click_online_mode(self, get_driver, get_function_name):
        LmsPage().click_online_mode(get_driver)

    @allure.title('点击发布')
    @allure.description("点击发布")
    def test_new_create_ketang_publish(self, get_driver, get_function_name):
        """发布"""
        time.sleep(1)
        get_win(get_driver, -2)
        LmsPage().click_pulish_ketang(get_driver)


@allure.feature("班级")
@allure.story("测试--创建录课课堂")
class TestCreateLuKeKeTang:
    @allure.title('H5，切换页面')
    @allure.description("H5，切换页面")
    def test_switch_win_1(self, get_web_driver, get_function_name):
        get_new_page_special(get_web_driver, "course/list")

    @allure.title('点击新建')
    @allure.description("课程tab下点击新建")
    def test_click_create_H5(self, get_web_driver, get_function_name):
        """ 课程tab下，H5上的【新建】"""
        LmsPage().click_H5_create(get_web_driver)

    @allure.title('选择新建课堂')
    @allure.description("选择新建课堂")
    def test_new_create_ketang(self, get_web_driver, get_function_name):
        """ 点击 新建 --课堂"""
        LmsPage().click_ketang_new(get_web_driver)

    @allure.title('原生，切换窗口')
    @allure.description("原生，切换窗口")
    def test_native_change_win(self, get_driver, get_function_name):
        get_win(get_driver, -2)

    @allure.title('选择在线教室模式')
    @allure.description("选择在线教室模式")
    def test_click_online_mode(self, get_driver, get_function_name):
        LmsPage().click_online_mode(get_driver)

    @allure.title('滚动条滚动到页面最下方')
    @allure.description("滚动条滚动到页面最下方")
    def test_get_page_down(self, get_driver, get_function_name):
        LmsPage().get_page_down(get_driver)
        time.sleep(2)

    @allure.title('选择录制教室')
    @allure.description("选择录制教室")
    def test_click_luke_room(self, get_driver, get_function_name):
        LmsPage().click_luke_room(get_driver)

    @allure.title('选择现场录制')
    @allure.description("选择现场录制")
    def test_click_luke_onsite(self, get_driver, get_function_name):
        LmsPage().click_luke_onsite(get_driver)

    @allure.title('选择网页直播')
    @allure.description("选择网页直播")
    def test_click_page_zhibo(self, get_driver, get_function_name):
        LmsPage().click_page_zhibo(get_driver)

    @allure.title('选择网页回放')
    @allure.description("选择网页回放")
    def test_click_page_huifang(self, get_driver, get_function_name):
        LmsPage().click_page_huifang(get_driver)

    @allure.title('点击发布')
    @allure.description("点击发布")
    def test_new_create_ketang_publish(self, get_driver, get_function_name):
        """发布"""
        time.sleep(1)
        get_win(get_driver, -2)
        LmsPage().click_pulish_ketang(get_driver)


class TestAfterCreate:
    def test_sleep(self, get_function_name):
        time.sleep(time_sleep[2] * 6)
