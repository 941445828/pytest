# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""

import time

def get_win(driver, num):
    """
    多窗口时，切换窗口
    :param driver:
    :param num:
    :return:
    """
    allHander = driver.window_handles
    driver.switch_to.window(allHander[num])
    return driver