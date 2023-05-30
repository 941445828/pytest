# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
import time
import pytest
import os
from config import *
from appium import webdriver as native_driver
from handler.logHandler import logger
from handler.getWinHandler import get_win
from selenium import webdriver as h5_driver
from handler.yamlHandler import get_data, YamlMethod
from functs.getPid import get_pid


@pytest.fixture(scope='session')
def get_driver():
    global driver
    desired_caps = {
        'app': get_data('baseConf.yaml')[0]['app_url'],
        'appArguments': "--UITest"
    }
    if desired_caps is not None:
        try:
            driver = native_driver.Remote(command_executor='http://127.0.0.1:4723', desired_capabilities=desired_caps)
        except Exception as msg:
            logger.error(msg)
            logger.error("====== nativedriver连接失败！ ======")
        else:
            logger.info("====== nativedriver已连接 ======")
            time.sleep(2)

            # login_pid = get_pid()
            # print('login_pid: {}'.format(login_pid))
            # logger.info('login_pid: {}'.format(login_pid))
            # case = get_data('login.yaml')[0]
            # case['login_pid'] = login_pid
            # YamlMethod(get_data('login.yaml')[1]).yaml_write(case)

            yield driver
            time.sleep(2)
            driver.quit()
            logger.info("====== nativedriver已断开 ======")
            return driver


@pytest.fixture(scope="session")
def get_web_driver():
    try:
        webview_page_url = INSPECT_URL  # INSPECT_URL = "127.0.0.1:7777"
        chrome_options = h5_driver.ChromeOptions()
        chrome_options.debugger_address = webview_page_url
        web_driver = h5_driver.Chrome(WEB_DRIVER_URL, options=chrome_options)
        time.sleep(2)
    except Exception as e:
        logger.error('webdriver 启动失败！ {}'.format(e))
    else:
        logger.info("====== webdriver已连接 ======")
        time.sleep(2)
        yield web_driver
        time.sleep(2)
        web_driver.quit()
        logger.info("====== webdriver已断开 ======")
        return web_driver


@pytest.fixture(scope="function")
def get_function_name(request):
    function_name = request.function.__name__
    logger.info('运行方法>>>>>：{}'.format(function_name))
    yield function_name