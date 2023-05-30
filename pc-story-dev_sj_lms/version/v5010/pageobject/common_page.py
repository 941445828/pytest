# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
import pyautogui
import pyperclip
import time
from handler.eleHandler import find_element
from version.v5000.pagelocator import common_locator as common


class ChooseFolder:
    def use_local_floder(self, driver, folder_url):
        """选择，本地文件夹"""
        pyperclip.copy(folder_url)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        ele_choose = common.choose_floder_btn
        ele_choose_btn = find_element(driver, ele_choose[0], ele_choose[1], ele_choose[2])
        ele_choose_btn.click()


class ChooseFile:
    def use_local_file(self, driver, file_url):
        """选择，打开本地文件"""
        pyperclip.copy(file_url)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        ele_open = common.Win_Open_btn
        ele_open_btn = find_element(driver, ele_open[0], ele_open[1], ele_open[2])
        ele_open_btn.click()


class ClassAppraise:
    def appraise_sure(self, driver):
        """关闭课节后，评价窗口上，点击【确定】"""
        ele = common.win_yes
        ele_yes = find_element(driver, ele[0], ele[1], ele[2])
        ele_yes.click()


class PromptChoose:
    def prompt_choose_yes(self, driver):
        """弹出的提示框上，选择【是】"""
        ele = common.prompt_yes
        ele_yes = find_element(driver, ele[0], ele[1], ele[2])
        ele_yes.click()

    def prompt_choose_no(self, driver):
        """弹出的提示框上，选择【否】"""
        ele = common.prompt_no
        ele_no = find_element(driver, ele[0], ele[1], ele[2])
        ele_no.click()

    def prompt_choose_sure(self, driver):
        """弹出的提示框上，选择【确定】"""
        ele = common.prompt_sure
        ele_sure = find_element(driver, ele[0], ele[1], ele[2])
        ele_sure.click()

    def prompt_choose_cancel(self, driver):
        """弹出的提示框上，选择【取消】"""
        ele = common.cancel_btn
        ele_cancel = find_element(driver, ele[0], ele[1], ele[2])
        ele_cancel.click()


    def prompt_choose_queren(self, driver):
        """弹出的提示框上，选择【确认】"""
        ele = common.prompt_queren
        ele_queren = find_element(driver, ele[0], ele[1], ele[2])
        ele_queren.click()

    def prompt_choose_open(self, driver):
        """弹出的提示框上，选择【打开】"""
        ele = common.open_btn
        ele_queren = find_element(driver, ele[0], ele[1], ele[2])
        ele_queren.click()

    def prompt_choose_done(self, driver):
        """弹出的提示框上，选择【完成】"""
        ele = common.done_btn
        ele_done = find_element(driver, ele[0], ele[1], ele[2])
        ele_done.click()