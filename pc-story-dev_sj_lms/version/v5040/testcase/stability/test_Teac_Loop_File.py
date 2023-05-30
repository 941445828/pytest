# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 对文件的操作
"""
from handler.getWinHandler import get_win
from version.v5030.pageobject.onlineOpenFile_page import OnlineOpenFilePage, OnlineCloseFilePage, MP4Operation, MP3Operation
from version.v5030.pageobject.common_page import ChooseFolder, ChooseFile, ClassAppraise, PromptChoose
import time
from handler.logHandler import logger


class TestTeacherLoopFile:
    def test_teacher_loop_mp3_mp4(self, get_driver, get_function_name):
        for i in range(200):  # 此处循环一次约150s，循环200次约8.3334小时
            print('loop count : {}'.format(i))
            logger.info('loop count : {}'.format(i))
            self.operation_mp4(get_driver)
            self.operation_mp3(get_driver)

    def operation_mp4(self, get_driver):
        # print('选择mp4：')
        MP4Operation().use_mp4(get_driver)
        # print('开始：')
        MP4Operation().start_mp4(get_driver)
        time.sleep(30)
        # print('进度条：')
        MP4Operation().click_mp4_slider(get_driver)
        time.sleep(10)
        # print('暂停：')
        MP4Operation().stop_mp4(get_driver)
        time.sleep(10)
        # print('进度条：')
        MP4Operation().click_mp4_slider(get_driver)
        time.sleep(10)
        # print('开始：')
        MP4Operation().start_mp4(get_driver)


    def operation_mp3(self, get_driver):
        # print('选择mp3：')
        MP3Operation().use_mp3(get_driver)
        # print('开始：')
        MP3Operation().start_mp3(get_driver)
        time.sleep(30)
        # print('进度条：')
        MP3Operation().click_mp3_slider(get_driver)
        time.sleep(10)
        # print('暂停：')
        MP3Operation().stop_mp3(get_driver)
        time.sleep(10)
        # print('进度条：')
        MP3Operation().click_mp3_slider(get_driver)
        time.sleep(10)
        # print('开始：')
        MP3Operation().start_mp3(get_driver)

