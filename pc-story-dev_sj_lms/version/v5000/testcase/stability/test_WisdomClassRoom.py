# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 智慧教室
"""
import time
from handler.getWinHandler import get_win
from pageobject.wisdomClassRoom_page import WisdomSetting



class TestFocusMode:
    def test_click_more(self, get_driver):
        WisdomSetting().click_more(get_driver)
        get_win(get_driver, 0)
        time.sleep(2)

    def test_click_setting(self, get_driver):
        WisdomSetting().click_setting(get_driver)

    def test_click_regular(self, get_driver):
        WisdomSetting().click_regular(get_driver)

    def test_click_focus(self, get_driver):
        WisdomSetting().click_focusmode(get_driver)

    def test_close_setting_win(self, get_driver):
        WisdomSetting().click_setting_win_closed(get_driver)









