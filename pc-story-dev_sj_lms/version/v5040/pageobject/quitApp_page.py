# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from version.v5000.pagelocator import quitApp_locator as Quit
from handler.eleHandler import find_element


class QuitAppPage:
    # 点击“设置”
    def click_setting(self, driver):
        ele = Quit.setting
        ele_setting = find_element(driver, ele[0], ele[1], ele[2])[6]
        ele_setting.click()

    # 点击“软件退出”
    def click_quit_app(self, driver):
        ele = Quit.quit_app
        ele_quit_app = find_element(driver, ele[0], ele[1], ele[2])[9]
        ele_quit_app.click()

    # 获取“确定退出登录提示框”
    def get_quit_promote(self, driver):
        ele = Quit.quit_prompt
        ele_quit_promote = find_element(driver, ele[0], ele[1], ele[2])
        return ele_quit_promote

    # “确定退出登录提示框”上点击“确定”
    def click_quit_yes(self, driver):
        ele_quit_yes = self.get_quit_promote(driver).find_elements_by_class_name('QPushButton')[0]
        ele_quit_yes.click()