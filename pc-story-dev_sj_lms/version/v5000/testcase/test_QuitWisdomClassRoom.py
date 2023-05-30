# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
录课模式 - 退出：提示“你确定要关闭教室吗？录课正在进行中，关闭教室会中断录课。”
非录课模式 - 退出：无提示，直接退出教室
录课模式/非录课模式 - 下课：提示“还有x人在教室内，下课后将被退出且无法再次进入，确定要下课吗？”
"""
import allure, time
from selenium.webdriver import ActionChains
from handler.getWinHandler import get_win
from pageobject.wisdomClassRoom_page import WisdomSetting
from pageobject.common_page import PromptChoose


class TestQuitWisdomClassRoom(object):
    def test_click_more(self, get_driver):
        WisdomSetting().click_more(get_driver)
        get_win(get_driver, 0)

    def test_click_quit(self, get_driver):
        WisdomSetting().click_quit(get_driver)
        get_win(get_driver, 0)

class TestQuitEnsure:
    def test_click_sure(self, get_driver):
        PromptChoose().prompt_choose_yes(get_driver)



