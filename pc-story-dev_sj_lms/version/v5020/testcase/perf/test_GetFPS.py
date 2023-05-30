# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 从教室内，通过UI，获取FPS值
"""
from version.v5000.pageobject.onlineClassRoom_page import OnlineClassRoomPage

class TestGetFPS:
    def test_get(self, get_driver):
        # while True:
        #     OnlineClassRoomPage().get_titlebar(get_driver)
        #     OnlineClassRoomPage().get_titlebar_left(get_driver)
        #     OnlineClassRoomPage().get_fps_ele(get_driver)
        #     OnlineClassRoomPage().get_fps(get_driver)
        OnlineClassRoomPage().get_titlebar(get_driver)
        OnlineClassRoomPage().get_titlebar_left(get_driver)
        OnlineClassRoomPage().get_fps_ele(get_driver)
        OnlineClassRoomPage().get_fps(get_driver)

