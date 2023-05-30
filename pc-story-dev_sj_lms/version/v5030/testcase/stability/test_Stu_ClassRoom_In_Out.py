# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 学生身份，循环运行：进教室-退教室
"""


import time
from version.v5030.pageobject.createClass_page import ClassPageUseReload


class TestStuSleep:
    def test_stu_sleep(self):
        time.sleep(30)


class TestClassCourseReload:
    def test_click_reload(self, get_driver):
        ClassPageUseReload().click_class_page_reload_btn(get_driver)

