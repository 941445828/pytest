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
from version.v5040.pageobject.addOnlineCourse_page import AddOnlineCoursePage
from version.v5040.pageobject.lmsCourse_page import LmsPage, StuLmsPage
from version.v5040 import *
from config import *
from version.v5040.pageobject.createClass_page import ClassPageUseReload


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


@allure.feature("班级")
@allure.story("测试--进入教室")
class TestEnterClassRoomH5:
    @allure.title('H5，切换页面')
    @allure.description("H5，切换页面")
    def test_switch_win_1(self, get_web_driver, get_function_name):
        get_new_page_special(get_web_driver,"&role=")   # &role=teacher、 role=manager

    @allure.title('课程tab，页面reload')
    @allure.description("课程tab")
    def test_click_reload(self, get_driver, get_function_name):
        ClassPageUseReload().click_class_page_reload_btn(get_driver)

    @allure.title('搜索功能')
    @allure.description("点击搜索logo")
    def test_click_search_logo(self,get_web_driver, get_function_name):
        LmsPage().click_search_logo(get_web_driver)

    @allure.title('搜索功能')
    @allure.description("输入搜索内容")
    def test_enter_search_content(self, get_web_driver, get_function_name):
        case = get_data('baseConf.yaml')[0]
        classname = case['target_classname']
        LmsPage().enter_search_content(get_web_driver, classname, 5)

    @allure.title('点击item列表上的【上课】')
    @allure.description("点击item列表上的【上课】")
    def test_begin_class(self, get_web_driver, get_function_name):
        AddOnlineCoursePage().click_btn_begin_class(get_web_driver)
        time.sleep(5)

    @allure.title('原生，切换窗口')
    @allure.description("原生，切换窗口")
    def test_changeto_native_driver(self, get_driver, get_function_name):
        get_win(get_driver, 0)
        time.sleep(5)

    @allure.title('初入教室内，点击【进入教室】')
    @allure.description("初入教室内，点击【进入教室】")
    def test_enter_classroom(self, get_driver, get_function_name):
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

@allure.feature("班级")
@allure.story("测试--进入教室，录课模式")
class TestLuKeEnter:
    @allure.title('录课模式，提示上点击【确定】')
    @allure.description("录课模式，提示上点击【确定】")
    def test_luke_enter_ensure(self, get_driver, get_function_name):
        """录课模式,进入教室后的提示"""
        # 点击录课提示的 “确定”
        AddOnlineCoursePage().click_sure(get_driver)

    @allure.title('录课模式，点击【立即录课】')
    @allure.description("录课模式，点击【立即录课】")
    def test_luke_click_begin(self, get_driver, get_function_name):
        # 点击“立即录课”
        AddOnlineCoursePage().click_luke(get_driver)


class TestSleep:
    def test_sleep(self, get_function_name):
        time.sleep(time_sleep[2] * 12)


#################################### 以下，是学生端操作
class TestStuEnterClassRoomH5:
    def test_switch_win_1(self, get_web_driver, get_function_name):
        get_new_page_special(get_web_driver,"role=student")

    @allure.title('搜索功能')
    @allure.description("点击搜索logo")
    def test_stu_click_search_logo(self,get_web_driver, get_function_name):
        StuLmsPage().stu_click_search_logo(get_web_driver)