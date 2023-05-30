# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 对摄像头设置的操作
"""
from handler.getWinHandler import get_win
from version.v5030.pageobject.onlineClassRoom_page import OnlineClassRoomPage
import time
from handler.logHandler import logger


class TestTeacherLoopCameraSetting:
    def test_camera_setting(self, get_driver, get_function_name):
        for i in range(270):   # 此处循环1次约110s， 循环270次用时8.25小时
            print('loop count : {}'.format(i))
            logger.info('loop count : {}'.format(i))
            self.camera_title_block(get_driver)
            self.camera_use_usb_device(get_driver)
            self.camera_use_ban(get_driver)


    def camera_title_block(self, get_driver):
        OnlineClassRoomPage().click_title_block_camera(get_driver)
        time.sleep(30)

    def camera_use_usb_device(self, get_driver):
        OnlineClassRoomPage().click_setting_btn(get_driver)
        get_win(get_driver, 0)
        OnlineClassRoomPage().click_setting(get_driver)
        get_win(get_driver, 0)
        OnlineClassRoomPage().click_video(get_driver)
        OnlineClassRoomPage().click_video_list(get_driver)
        OnlineClassRoomPage().click_video_use_usb(get_driver)
        OnlineClassRoomPage().click_setting_win_close(get_driver)
        time.sleep(30)


    def camera_use_ban(self, get_driver):
        OnlineClassRoomPage().click_setting_btn(get_driver)
        get_win(get_driver, 0)
        OnlineClassRoomPage().click_setting(get_driver)
        get_win(get_driver, 0)
        OnlineClassRoomPage().click_video(get_driver)
        OnlineClassRoomPage().click_video_list(get_driver)
        OnlineClassRoomPage().click_video_ban(get_driver)
        OnlineClassRoomPage().click_setting_win_close(get_driver)
        time.sleep(30)







