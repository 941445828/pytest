# coding = utf-8
"""
@Author: sujie
@Create on: 2021
@Modify on：
@File:
"""


import allure
from selenium.webdriver import ActionChains
from version.v5000.pageobject.createClass_page import CreateClassPage, ChangeToCourseTab, ChangeToScorseTab
from handler.yamlHandler import get_data
from handler.eleHandler import find_element


@allure.feature("班级")
@allure.story("测试-班级-创建班级")
class TestCreateClass:
    @allure.title('创建班级')
    @allure.description("测试：创建班级")
    def test_add_class_smoke(self, get_driver):
        """
        创建新班级
        """
        case = get_data('class.yaml')[0]

        # # 通过location获取'创建班级'
        # # 找到搜索框，从搜索框上鼠标下移至【创建班级】
        # ele_search = find_element(get_driver, "搜索框", 'ClassName', case['ele_classname_search'])
        # ActionChains(get_driver).move_to_element_with_offset(ele_search, 200, 80).click().perform()

        # 点击，创建班级，入口
        CreateClassPage().click_create_entry(get_driver)

        # 创建课程--输入班级名称
        CreateClassPage().input_class_name(get_driver, case['content_classname'])

        # 点击创建button
        CreateClassPage().click_create(get_driver)


"""
点击进入班级列表下的，第一个班级
"""
from version.v5000.pagelocator import createClass_locator as CC


class TestUseClass:
    def test_use_first_class(self, get_driver):
        """
        进入班级列表的第一个班级
        """
        ele = CC.Create
        ele_create = find_element(get_driver, ele[0], ele[1], ele[2])
        ActionChains(get_driver).move_to_element_with_offset(ele_create, 0, 100).click().perform()


class TestUseTargetClass:
    def test_use_target_class(self, get_driver):
        """
        进入指定名称的班级
        """
        case = get_data('baseConf.yaml')[0]
        class_name = case['target_classname']
        CreateClassPage().get_class(get_driver, class_name)


""" 班级下，切换到‘课程’tab """
class TestChangeCourseTab:
    def test_enter_course(self, get_driver):
        ChangeToCourseTab().click_course_tab(get_driver)


""" 班级下，切换到‘成绩’tab """
class TestChangeScoreTab:
    def test_enter_score(self, get_driver):
        # '成绩'
        ChangeToScorseTab().click_scorse_tab(get_driver)