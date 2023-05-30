# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from version.v5000.pageobject.login_page import LoginPage
from handler.yamlHandler import get_data, YamlMethod
from handler.logHandler import logger
import time, allure, pytest
from handler.getWinHandler import get_win


@pytest.mark.run(order=0)
@allure.feature("登录")
@allure.story("测试--ClassIn登录")
class TestLogin(object):
    @allure.title('登录')
    @allure.description("输入用户名")
    def test_input_username(self, get_driver, get_function_name):
        case = get_data('baseConf.yaml')[0]
        # logger.info("login--用例 {}：".format(case))
        get_driver.maximize_window()  # 使窗口前置，获取焦点
        LoginPage().input_username(get_driver, case['content_username'])

    @allure.title('登录')
    @allure.description("输入密码")
    def test_input_pwd(self, get_driver, get_function_name):
        case = get_data('baseConf.yaml')[0]
        LoginPage().input_pwd(get_driver, case['content_pwd'])

    @allure.title('登录')
    @allure.description("点击【登录】")
    def test_click_login_btn(self, get_driver, get_function_name):
        LoginPage().click_button_login(get_driver)
        # 有窗口切换，强制等待
        time.sleep(5)
        # 登录后窗口改变，获取新窗口
        get_win(get_driver, -1)
        time.sleep(2)

        #  将主窗口handle存入yaml
        allHander = get_driver.window_handles
        mainHandle = allHander[-1]

        case = get_data('baseConf.yaml')[0]
        case['mainHandle'] = mainHandle
        YamlMethod(get_data('baseConf.yaml')[1]).yaml_write(case)
        logger.info("主窗口： {}".format(mainHandle))