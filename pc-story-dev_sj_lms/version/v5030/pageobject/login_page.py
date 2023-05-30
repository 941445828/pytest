# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from selenium.webdriver.common.keys import Keys
from version.v5000.pagelocator import login_locator as Login
from handler.eleHandler import find_element


class LoginPage:
    def input_username(self, driver, user_name):
        # 获取元素
        ele = Login.UserName
        ele_username = find_element(driver, ele[0], ele[1], ele[2])[1]
        # 填充
        ele_username.click()
        ele_username.send_keys(Keys.CONTROL, 'a')
        ele_username.send_keys(Keys.DELETE)
        ele_username.send_keys(user_name)


    def input_pwd(self, driver, p_w_d):
        # 获取元素
        ele = Login.PassWord
        ele_pwd = find_element(driver, ele[0], ele[1], ele[2])[0]
        # 填充
        ele_pwd.send_keys(Keys.CONTROL, 'a')
        ele_pwd.send_keys(Keys.DELETE)
        ele_pwd.send_keys(p_w_d)


    def click_button_login(self, driver, ):
        # 获取元素
        ele = Login.LoginButton
        ele_loginbutton = find_element(driver, ele[0], ele[1], ele[2])
        # 点击
        ele_loginbutton.click()






