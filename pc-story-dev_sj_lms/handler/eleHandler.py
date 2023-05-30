# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from handler.logHandler import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def find_element(driver, element, method, value, secs=10):
    try:
        wait = WebDriverWait(driver, secs)
        if method == 'Name':
            wait.until(ec.presence_of_element_located((By.NAME, value)))
            element = driver.find_element_by_name(value)
        elif method == 'ClassName':
            wait.until(ec.presence_of_element_located((By.CLASS_NAME, value)))
            element = driver.find_element_by_class_name(value)
        elif method == 'XPath':
            wait.until(ec.presence_of_element_located((By.XPATH, value)))
            element = driver.find_element_by_xpath(value)
        elif method == 'Names':
            wait.until(ec.presence_of_all_elements_located((By.NAME, value)))
            element = driver.find_elements_by_name(value)
        elif method == 'ClassNames':
            wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, value)))
            element = driver.find_elements_by_class_name(value)
        elif method == 'XPaths':
            wait.until(ec.presence_of_all_elements_located((By.XPATH, value)))
            element = driver.find_elements_by_xpath(value)
        else:
            logger.error("元素类型不存在！")
    except Exception as e:
        print(e)
        logger.error("元素：{} 没有定位到！".format(element))
    return element

