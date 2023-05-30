# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
import allure, time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from handler.getWinHandler import get_win
from handler.yamlHandler import get_data
from version.v5000.pageobject.addOnlineCourse_page import AddOnlineCoursePage
from version.v5000.pageobject.lmsCourse_page import LmsPage
from version.v5000 import *


@allure.feature("班级")
@allure.story("测试-班级-添加课节-录课模式")
class TestAddOnlineCourseLuKe(object):
    @allure.title('添加课节(在线教室)--录课模式')
    @allure.description("测试：添加课节(在线教室)--录课模式")
    def test_addonlinecourse(self, get_driver):
        case = get_data('class.yaml')[0]

        # 点击课程tab
        AddOnlineCoursePage().click_kecheng_tab(get_driver)

        # 点击“添加课节”
        AddOnlineCoursePage().click_addOnlineCourse_button(get_driver)

        # 填充 课节名称
        AddOnlineCoursePage().input_cousername(get_driver, case['online_course_name'])

        # 选择教学模式
        AddOnlineCoursePage().choose_coursemode(get_driver)

        # 勾选云端录课
        AddOnlineCoursePage().choose_lukemode(get_driver)

        # 滚动滚动条到最下方
        ActionChains(get_driver).key_down(Keys.PAGE_DOWN).perform()

        # 勾选网页直播
        AddOnlineCoursePage().choose_zhibo(get_driver)

        # 勾选网页回放
        AddOnlineCoursePage().choose_huifang(get_driver)

        # 点击创建
        AddOnlineCoursePage().click_create_button(get_driver)


@allure.feature("班级")
@allure.story("测试-班级-添加课节-非录课模式")
class TestAddOnlineCourseNoLuKe(object):
    @allure.title('添加课节(在线教室)-非录课模式')
    @allure.description("测试：添加课节(在线教室)-非录课模式")
    def test_addonlinecourse(self, get_driver):
        case = get_data('class.yaml')[0]

        # 点击课程tab
        AddOnlineCoursePage().click_kecheng_tab(get_driver)

        # 点击“添加课节”
        AddOnlineCoursePage().click_addOnlineCourse_button(get_driver)

        # 填充 课节名称
        AddOnlineCoursePage().input_cousername(get_driver, case['online_course_name'])

        # 选择教学模式
        AddOnlineCoursePage().choose_coursemode(get_driver)

        # 滚动滚动条到最下方
        ActionChains(get_driver).key_down(Keys.PAGE_DOWN).perform()

        # 点击创建
        AddOnlineCoursePage().click_create_button(get_driver)


class TestEnterClassRoomH5:
    def test_switch_win_1(self, get_web_driver):
        get_new_page_special(get_web_driver,"&role=manager")

    def test_click_search_logo(self,get_web_driver):
        LmsPage().click_search_logo(get_web_driver)

    def test_enter_search_content(self, get_web_driver):
        case = get_data('baseConf.yaml')[0]
        classname = case['target_classname']
        LmsPage().enter_search_content(get_web_driver, classname, 5)

    def test_begin_class(self, get_web_driver):
        AddOnlineCoursePage().click_btn_begin_class(get_web_driver)
        time.sleep(5)

    def test_changeto_native_driver(self, get_driver):
        get_win(get_driver, 0)
        time.sleep(5)

    def test_enter_classroom(self, get_driver):
        # 点击教室内--进入教室
        AddOnlineCoursePage().click_enter(get_driver)
        time.sleep(5)


class TestEnterWisdomClassRoomH5:
    # 智慧教室进入教室
    def test_begin_class(self, get_web_driver):
        AddOnlineCoursePage().click_btn_begin_class(get_web_driver)
        time.sleep(5)

    def test_changeto_native_driver(self, get_driver):
        get_win(get_driver, 0)
        time.sleep(5)


class TestEnterClassRoom:
    def test_enter(self, get_driver):
        # 点击上课
        AddOnlineCoursePage().click_enter_room(get_driver)

        time.sleep(5)
        get_win(get_driver, 0)
        time.sleep(2)

        # 点击教室内--进入教室
        AddOnlineCoursePage().click_enter(get_driver)
        time.sleep(5)

class TestLuKeEnter:
    def test_luke_enter(self, get_driver):
        """录课模式,进入教室后的提示"""
        # 点击录课提示的 “确定”
        AddOnlineCoursePage().click_sure(get_driver)

        # 点击“立即录课”
        AddOnlineCoursePage().click_luke(get_driver)
