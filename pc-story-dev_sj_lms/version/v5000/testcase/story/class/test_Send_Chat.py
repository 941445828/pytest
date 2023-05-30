# coding = utf-8
"""
@Author: sujie
@Create on: 2022-9-13
@Modify on：
@File: 课程下，发布5000条聊天数据
"""
from version.v5000.pageobject.classChat_page import ClassChatPage


class TestClassSendChat:
    def test_send_chat(self, get_driver):
        ClassChatPage().get_chat_tap(get_driver)
        ClassChatPage().click_chat_tap(get_driver)
        for i in range(1, 5001):
            ClassChatPage().get_chat_text_eidt(get_driver)
            ClassChatPage().click_chat_text_eidt(get_driver)
            ClassChatPage().enter_text(i)
            ClassChatPage().get_chat_send_btn(get_driver)
            ClassChatPage().click_chat_send_btn(get_driver)



