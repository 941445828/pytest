# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from selenium.webdriver.common.keys import Keys
from version.v5000.pagelocator import setting_locator as Set
from handler.eleHandler import find_element

class BasicSettingChangeLanguagePage:
    # 获取元素“设置”
    def find_setting(self, driver):
        ele = Set.setting
        ele_setting = find_element(driver, ele[0], ele[1], ele[2])[6]
        return ele_setting

    # 获取元素“设置”的内容
    def get_setting_text(self, driver):
        ele = self.find_setting(driver)
        ele_text = ele.get_attribute('Name')
        return ele_text

    # 点击“设置”
    def click_setting(self, driver):
        self.find_setting(driver).click()

    # 点击“系统设置”
    def click_os_setting(self, driver):
        ele = Set.os_setting
        ele_os_seting = find_element(driver, ele[0], ele[1], ele[2])[0]
        ele_os_seting.click()

    # 点击“基本设置”
    def click_basic_setting(self, driver):
        ele = Set.base_setting
        ele_basic_setting = find_element(driver, ele[0], ele[1], ele[2])
        ele_basic_setting.click()

    # 获取元素-软件语言选择框
    def get_ele_lang_dropmenu(self, driver):
        ele = Set.lang_dropmenu
        ele_lang_dropmenu = find_element(driver, ele[0], ele[1], ele[2])
        return ele_lang_dropmenu

    # 点击“软件语言选择框”
    def click_lang_dropmenu(self, driver):
        ele = self.get_ele_lang_dropmenu(driver)
        ele.click()

    # 切换语言，使用向下箭头切换语言
    def sendKeys_lang_dropmenu(self, driver):
        ele = self.get_ele_lang_dropmenu(driver)
        ele.send_keys(Keys.ARROW_DOWN)

    # 获取元素“重新启动软件弹窗提示”
    def get_reload_accept(self, driver):
        ele = Set.reload_accept
        ele_reload_accept = find_element(driver, ele[0], ele[1], ele[2])
        return ele_reload_accept

    # 点击，重新启动软件弹窗提示上的“否”
    def click_choose_no(self, driver):
        ele_choose_no = self.get_reload_accept(driver).find_elements_by_class_name('QPushButton')[1]
        ele_choose_no.click()