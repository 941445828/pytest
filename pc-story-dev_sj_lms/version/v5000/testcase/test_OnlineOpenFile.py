# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from version.v5000.pageobject.onlineOpenFile_page import OnlineOpenFilePage
from handler.yamlHandler import get_data
import allure
from config import perf_conf
from version.v5000 import *


@allure.feature("教室")
@allure.story("测试--在线教室打开课件")
class TestOpenFiles(object):
    def test_open(self, get_driver):

        OnlineOpenFilePage().get_ClassroomPage(get_driver)

        OnlineOpenFilePage().get_ToolbarWrapper(get_driver)

        OnlineOpenFilePage().click_yunpan(get_driver)

    def test_use_wendang(self, get_web_driver):
        get_new_page_special(get_web_driver, "inspector")
        OnlineOpenFilePage().click_wendang(get_web_driver)

    def test_open_file(self, get_web_driver):
        case = get_data('class.yaml')[0]
        # 点击文件夹
        OnlineOpenFilePage().click_folder(get_web_driver, case['folder_name'])
        # 点击要打开的课件

        files_list = perf_conf.open_files_setting
        print('open:')
        for i in range(len(files_list)):
            print(files_list[i])
            OnlineOpenFilePage().click_file(get_web_driver, files_list[i])
            time.sleep(60)
        time.sleep(90)


class TestOpenFilesClassIn(object):
    def test_open(self, get_driver):

        OnlineOpenFilePage().get_ClassroomPage(get_driver)

        OnlineOpenFilePage().get_ToolbarWrapper(get_driver)

        OnlineOpenFilePage().click_yunpan(get_driver)

    def test_use_wendang(self, get_web_driver):
        OnlineOpenFilePage().click_wendang(get_web_driver)

    def test_open_file(self, get_web_driver):
        case = get_data('class.yaml')[0]
        # 点击文件夹
        OnlineOpenFilePage().click_folder(get_web_driver, case['folder_name'])
        # 点击要打开的课件

        files_list = perf_conf.open_files_setting
        print('open:')
        for i in range(len(files_list)):
            print(files_list[i])
            OnlineOpenFilePage().click_file(get_web_driver, files_list[i])
            time.sleep(60)
        time.sleep(90)





