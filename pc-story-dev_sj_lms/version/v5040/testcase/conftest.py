# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
import csv
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
import threading
from config import utils
from config import perf_conf


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

            # 开启获取FPS并发线程
            is_use_fps = get_data('baseConf.yaml')[0]['is_use_fps']
            thread = MyThread(driver)
            if is_use_fps == 'Y':
                thread.start()
            else:
                pass

            yield driver
            thread.stop()
            time.sleep(2)
            driver.quit()
            logger.info("====== nativedriver已断开 ======")


@pytest.fixture(scope="session")
def get_web_driver():
    global web_driver
    webdriver_version = get_data('baseConf.yaml')[0]['webdriver_version']
    try:
        webview_page_url = INSPECT_URL  # INSPECT_URL = "127.0.0.1:7777"
        chrome_options = h5_driver.ChromeOptions()
        chrome_options.debugger_address = webview_page_url
        if webdriver_version == 103:
            web_driver = h5_driver.Chrome(WEB_DRIVER_103, options=chrome_options)
        elif webdriver_version == 84:
            web_driver = h5_driver.Chrome(WEB_DRIVER_URL, options=chrome_options)
        else:
            print('需确认webdriver版本配置！')
            logger.info('需确认webdriver版本配置！')
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


@pytest.fixture(scope="function")
def get_function_name(request):
    function_name = request.function.__name__
    logger.info('运行方法>>>>>：{}'.format(function_name))
    yield function_name


class MyThread(threading.Thread):
    def __init__(self, driver):
        super(MyThread, self).__init__()
        self.driver = driver
        self._stop = threading.Event()

    # 开启线程
    def run(self):
        global fps
        while True:
            if self.stopped():
                return
            try:
                fps_text = (self.driver.find_element_by_xpath("(//*[@ClassName='TitleBar']/*[@ClassName='SystemStateLabel']/*[@ClassName='QLabel'])[4]")).get_attribute('Name')
                fps = fps_text.split(': ')[1]
            except Exception as e:
                logger.error(e)
                # print('0', str(int(time.time())))
                fps_content = ['0', utils.now_time()]
                with open(collect_fps(), 'a', newline='') as fps_file:
                    fps_csv = csv.writer(fps_file)
                    fps_csv.writerow(fps_content)
                time.sleep(2)
                pass
            else:
                # print(str(fps), str(int(time.time())))
                fps_content = [str(fps), utils.now_time()]
                with open(collect_fps(), 'a', newline='')as fps_file:
                    fps_csv = csv.writer(fps_file)
                    fps_csv.writerow(fps_content)
                time.sleep(2)


    # 停止获取tfp的进程
    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()


def collect_fps():
    fps_file_url = utils.get_fps_csv_url(perf_conf.fps_csv_name)  # 自定义CSV文件名字
    return fps_file_url