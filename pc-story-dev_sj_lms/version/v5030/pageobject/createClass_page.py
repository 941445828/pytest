# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from version.v5010.pagelocator import createClass_locator as CC
from handler.eleHandler import find_element


class CreateClassPage(object):
    def click_create_entry(self, driver):
        # 获取元素
        ele = CC.Create
        ele_create = find_element(driver, ele[0], ele[1], ele[2])
        # 点击
        ele_create.click()

    def input_class_name(self, driver, class_name):
        ele = CC.ClassName
        ele_class_name = find_element(driver, ele[0], ele[1], ele[2])
        ele_class_name.click()
        ele_class_name.clear()
        ele_class_name.send_keys(class_name)

    def click_create(self, driver):
        ele = CC.CreateButton
        ele_create = find_element(driver, ele[0], ele[1], ele[2])[1]
        ele_create.click()

    def get_class(self, driver, exist_class):
        ele_class = find_element(driver, '元素-'+ exist_class, 'Name', exist_class)
        ele_class.click()


class ChangeToCourseTab:
    def click_course_tab(self, driver):
        ele = CC.Course
        ele_course = find_element(driver, ele[0], ele[1], ele[2])
        ele_course.click()


class ChangeToScorseTab:
    def click_scorse_tab(self, driver):
        ele = CC.Score
        ele_score = find_element(driver, ele[0], ele[1], ele[2])
        ele_score.click()


class ClassPageUseReload:
        def click_class_page_reload_btn(self, driver):
            ele = CC.ReloadBtn
            ele_reload = find_element(driver, ele[0], ele[1], ele[2])
            # print(len(ele_reload))
            ele_reload[0].click()