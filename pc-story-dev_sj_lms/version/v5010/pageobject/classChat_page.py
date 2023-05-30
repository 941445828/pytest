# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from version.v5000.pagelocator import classChat_locator as chat
from handler.eleHandler import find_element
import pyautogui
import pyperclip


class ClassChatPage:
    def get_chat_tap(self, driver):
        ele = chat.chat_tap
        ele_chat_tap = find_element(driver, ele[0], ele[1], ele[2])
        return ele_chat_tap

    def click_chat_tap(self, driver):
        self.get_chat_tap(driver).click()

    def get_chat_text_eidt(self, driver):
        ele = chat.chat_text_edit
        ele_chat_text_edit =  find_element(driver, ele[0], ele[1], ele[2])
        return ele_chat_text_edit

    def click_chat_text_eidt(self, driver):
        self.get_chat_text_eidt(driver).click()

    def enter_text(self, content):
        pyperclip.copy(content)
        pyautogui.hotkey('ctrl', 'v')

    def get_chat_send_btn(self, driver):
        ele = chat.chat_send_btn
        ele_send_btn = find_element(driver, ele[0], ele[1], ele[2])
        return ele_send_btn

    def click_chat_send_btn(self, driver):
        self.get_chat_send_btn(driver).click()





