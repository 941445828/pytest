# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
import time
from handler.getWinHandler import get_win
from version.v5000.pageobject.quitApp_page import QuitAppPage
from handler.yamlHandler import get_data


class TestQuitAPP(object):
    def test_quit_app(self, get_driver, get_function_name):
        case = get_data('baseConf.yaml')[0]
        allHander = get_driver.window_handles
        mainHandle = case['mainHandle']
        for i in range(len(allHander)):
            if allHander[i] == mainHandle:
                get_driver.switch_to.window(allHander[i])

        # 查找元素--设置， 点击
        QuitAppPage().click_setting(get_driver)

        # 产生了新窗口，切换窗口
        get_win(get_driver, 0)
        time.sleep(2)

        # 查找元素--软件退出， 点击
        QuitAppPage().click_quit_app(get_driver)

        # 退出
        get_win(get_driver, 0)
        time.sleep(2)
        QuitAppPage().click_quit_yes(get_driver)