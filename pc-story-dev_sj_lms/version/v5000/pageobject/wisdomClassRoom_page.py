# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 智慧教室
"""
from pagelocator import wisdomClassRoom_locator as Wisdom
from handler.eleHandler import find_element


class WisdomSetting:
    def get_bottom_bar(self, driver):
        ele = Wisdom.MainMenuBar
        ele_bar = find_element(driver, ele[0], ele[1], ele[2])
        return ele_bar

    def click_more(self, driver):
        ele = Wisdom.More
        ele_more = self.get_bottom_bar(driver).find_elements_by_class_name(ele[2])[1]
        ele_more.click()

    def click_quit(self, driver):
        ele = Wisdom.Quit
        ele_quit = find_element(driver, ele[0], ele[1], ele[2])
        ele_quit.click()

    def click_setting(self, driver):
        ele = Wisdom.Setting
        ele_set = find_element(driver, ele[0], ele[1], ele[2])
        ele_set.click()

    def click_regular(self, driver):
        ele = Wisdom.SettingButton
        ele_regu = find_element(driver, ele[0], ele[1], ele[2])[0]
        ele_regu.click()

    def click_focusmode(self, driver):
        ele = Wisdom.FocusCheck
        ele_focus = find_element(driver, ele[0], ele[1], ele[2])
        ele_focus.click()

    def get_setting_win(self, driver):
        ele = Wisdom.SettingWin
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def click_setting_win_closed(self, driver):
        ele = Wisdom.SettingWinClosed
        ele_win_closed = self.get_setting_win(driver).find_elements_by_class_name(ele[2])[0]
        ele_win_closed.click()


