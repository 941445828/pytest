# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File: 作业重新批阅流程
"""
import random
import pyautogui
import pyautogui as pag
import win32api
import pynput
import pytest
import win32con
from version.v5000.pageobject.hw_h5_page import H5Page
import time
from handler.getWinHandler import get_win
from selenium.webdriver import ActionChains
from pynput.mouse import Controller
import numpy as np
import cv2


mouse = Controller()
keyboard = Controller()
c = pynput.mouse.Controller()
global list,list1
list = []
list1 = []

######8个作业图片全部批阅
@pytest.mark.run(order=1)
class TestHomework:
    def test_homework_course_01(self, get_driver):
        """ 点击班群名称， 进入班群， 切换到 作业 tab"""
        time.sleep(1)
        ele_search=H5Page().click_coursename(get_driver)
        ActionChains(get_driver).move_to_element_with_offset(ele_search, 200, 230).click().perform()
        time.sleep(1)
        H5Page().click_homework_tab(get_driver)

    def test_homework_account_02(self,get_web_driver):
        """ 点击教师账号，进入单个作业"""
        H5Page().click_tea_account(get_web_driver)

    def test_homework_student_03(self, get_web_driver):
        """ 点击学生，打开批阅作业页面 """
        time.sleep(1)
        H5Page().click_stu_account(get_web_driver)

    def test_homework_student_031(self, get_web_driver):
        """点击btn【重新批阅】--需要点击重新批阅后，再点击图片，才能出现编辑模式"""
        get_win(get_web_driver, 2)
        H5Page().click_btn_review(get_web_driver)

    def test_homework_pic_032(self, get_web_driver):
        """ 点击图片（大图， 可编辑） """
        time.sleep(2)
        H5Page().click_pic(get_web_driver)

    def test_homework_image_033(self, get_driver):
        """ 编辑图片--原生"""
        # 有窗口切换，强制等待
        time.sleep(1)
        # 登录后窗口改变，获取新窗口
        get_win(get_driver, -3)
        time.sleep(1)

        homeworkimg=H5Page().click_homework_image(get_driver)


        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -57, -37).perform()
        x, y = pag.position()
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -87, -37).perform()
        x, y = pag.position()
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -117, -37).perform()
        x, y = pag.position()
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -147, -37).perform()
        x, y = pag.position()
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -177, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -207, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -237, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)
        H5Page().click_homework_text(get_driver)
        time.sleep(1)
        print("添加文字完")
        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)

        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)
        # x, y = pag.position()
        win32api.SetCursorPos([p1, p2])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)
        H5Page().input_homework_text(get_driver,"89808098tun急急急吼吼吼吼韩国")

        time.sleep(1)
        win32api.SetCursorPos([p3, p4])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        H5Page().input_homework_text(get_driver,"3434并迅速必须八十八")

        H5Page().click_homework_shape(get_driver)

        H5Page().input_homework_shape(get_driver)

        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)

        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)
        # m = PyMouse()

        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')

        time.sleep(1)
        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)

        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)

        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')
        time.sleep(1)
        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)

        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)

        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')
        time.sleep(1)


        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)
        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)


        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')
        time.sleep(1)

    def test_homework_image_upload_04(self, get_driver):
        """ 点击云盘btn图标-上传云盘"""
        ele_clickhomeworkimgupload=H5Page().click_homework_image_upload(get_driver)
        time.sleep(1)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgupload).perform()
        x, y = pag.position()
        print(x,y)
        time.sleep(1)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        #1
        time.sleep(8)

    def test_homework_image_upload_ensure_05(self,get_web_driver):
        """ 上传云盘，点击【确定】 """
        time.sleep(2)
        get_win(get_web_driver, 3)
        H5Page().click_eidt_pic_finish(get_web_driver)


    def test_homework_image_save_06(self, get_driver):
        """ 点击保存本地btn图标 """
        time.sleep(1)
        ele_clickhomeworkimgsave=H5Page().click_homework_image_save(get_driver)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgsave).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)
        aa=random.randint(0,10000000)
        bb=random.randint(0,10000000)
        cc=aa+bb

        print("cc",cc)
        H5Page().click_upload_pic(cc)    # 保存

        list.append(cc)
        print("pic list",list)

        time.sleep(1)


    def test_homework_pic_next_07(self, get_driver):
        ele_clickhomeworkpicnext=H5Page().click_homework_pic_next(get_driver)
        time.sleep(1)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkpicnext).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# 第二张图片
    def test_homework_image_08(self, get_driver):
        # 有窗口切换，强制等待
        time.sleep(1)
        #点击表情按钮
        homeworkadaption=H5Page().click_self_adaptionhomework_image(get_driver)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -35, 5).perform()
        # ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -57, -37).perform()

        x, y = pag.position()
        print(x,y)
        time.sleep(1)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        #1
        time.sleep(2)
        homeworkimg=H5Page().click_homework_image(get_driver)


        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -57, -37).perform()
        x, y = pag.position()
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -87, -37).perform()
        x, y = pag.position()
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -117, -37).perform()
        x, y = pag.position()
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -147, -37).perform()
        x, y = pag.position()
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -177, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -207, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -237, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)
        H5Page().click_homework_text(get_driver)
        time.sleep(1)
        print("添加文字完")
        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)

        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)

        win32api.SetCursorPos([p1, p2])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        H5Page().input_homework_text(get_driver,"89808098tun急急急吼吼吼吼韩国")

        time.sleep(1)
        win32api.SetCursorPos([p3, p4])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        H5Page().input_homework_text(get_driver,"3434并迅速必须八十八")

        H5Page().click_homework_shape(get_driver)
        H5Page().input_homework_shape(get_driver)


        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)

        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)
        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')
        time.sleep(1)


        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)

        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)
        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')
        time.sleep(1)

        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)

        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)
        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')
        time.sleep(1)


        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)
        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)
        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')

        time.sleep(1)


    def test_homework_image_save_11(self, get_driver):
        """ 第二张图片， 只保存本地 """
        time.sleep(1)
        ele_clickhomeworkimgsave=H5Page().click_homework_image_save(get_driver)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgsave).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)
        aa=random.randint(0,10000000)
        bb=random.randint(0,10000000)
        cc=aa+bb

        print("cc",cc)
        H5Page().click_upload_pic(cc)

        list.append(cc)
        print("pic list",list)

        time.sleep(1)

    def test_homework_pic_next_12(self, get_driver):
        ele_clickhomeworkpicnext=H5Page().click_homework_pic_next(get_driver)
        time.sleep(1)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkpicnext).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# 第三张
    def test_homework_image_13(self, get_driver):
        time.sleep(1)
        #点击表情按钮
        homeworkadaption=H5Page().click_self_adaptionhomework_image(get_driver)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -35, 5).perform()

        x, y = pag.position()
        print(x,y)
        time.sleep(1)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        #1
        time.sleep(2)
        homeworkimg=H5Page().click_homework_image(get_driver)


        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -57, -37).perform()
        x, y = pag.position()
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -87, -37).perform()
        x, y = pag.position()
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -117, -37).perform()
        x, y = pag.position()
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -147, -37).perform()
        x, y = pag.position()
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -177, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -207, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -237, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)
        H5Page().click_homework_text(get_driver)
        time.sleep(1)
        print("添加文字完")
        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)

        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)

        win32api.SetCursorPos([p1, p2])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        H5Page().input_homework_text(get_driver,"89808098tun急急急吼吼吼吼韩国")

        time.sleep(1)
        win32api.SetCursorPos([p3, p4])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        H5Page().input_homework_text(get_driver,"3434并迅速必须八十八")

        H5Page().click_homework_shape(get_driver)
        H5Page().input_homework_shape(get_driver)

        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)

        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)
        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')

        time.sleep(1)
        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)

        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)
        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')

        time.sleep(1)
        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)

        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)
        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')
        time.sleep(1)

        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)
        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)

        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')
        time.sleep(1)


    def test_homework_image_save_16(self, get_driver):
        time.sleep(1)
        ele_clickhomeworkimgsave=H5Page().click_homework_image_save(get_driver)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgsave).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)
        aa=random.randint(0,10000000)
        bb=random.randint(0,10000000)
        cc=aa+bb


        print("cc",cc)
        H5Page().click_upload_pic(cc)

        list.append(cc)
        print("pic list",list)

        time.sleep(1)

    def test_homework_pic_next_17(self, get_driver):
        ele_clickhomeworkpicnext=H5Page().click_homework_pic_next(get_driver)
        time.sleep(1)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkpicnext).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# 第四张
    def test_homework_image_18(self, get_driver):
        time.sleep(1)
        #点击表情按钮
        homeworkadaption=H5Page().click_self_adaptionhomework_image(get_driver)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -35, 5).perform()
        # ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -57, -37).perform()

        x, y = pag.position()
        print(x,y)
        time.sleep(1)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        #1
        time.sleep(2)
        homeworkimg=H5Page().click_homework_image(get_driver)


        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -57, -37).perform()
        x, y = pag.position()
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -87, -37).perform()
        x, y = pag.position()
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -117, -37).perform()
        x, y = pag.position()
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -147, -37).perform()
        x, y = pag.position()
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -177, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -207, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -237, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)
        H5Page().click_homework_text(get_driver)
        time.sleep(1)
        print("添加文字完")
        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)

        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)

        win32api.SetCursorPos([p1, p2])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        H5Page().input_homework_text(get_driver,"89808098tun急急急吼吼吼吼韩国")

        time.sleep(1)
        win32api.SetCursorPos([p3, p4])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        H5Page().input_homework_text(get_driver,"3434并迅速必须八十八")

        H5Page().click_homework_shape(get_driver)
        H5Page().input_homework_shape(get_driver)

        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)

        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)
        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')

        time.sleep(1)
        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)

        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)
        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')

        time.sleep(1)
        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)

        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)
        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')
        time.sleep(1)

        p1= random.randint(700,1000)
        p2= random.randint(200,800)
        p3= random.randint(800,900)
        p4= random.randint(300,700)
        print("p1,p2",p1,p2)
        print("p3,p4",p3,p4)

        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')
        time.sleep(1)


    def test_homework_image_save_21(self, get_driver):
        time.sleep(1)
        ele_clickhomeworkimgsave=H5Page().click_homework_image_save(get_driver)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgsave).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)
        aa=random.randint(0,10000000)
        bb=random.randint(0,10000000)
        cc=aa+bb

        time.sleep(1)
        print("cc",cc)
        H5Page().click_upload_pic(cc)
        time.sleep(1)
        list.append(cc)
        print("pic list",list)

        time.sleep(1)



    def test_homework_pic_next_22(self, get_driver):
        ele_clickhomeworkpicnext=H5Page().click_homework_pic_next(get_driver)
        time.sleep(1)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkpicnext).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# 第五张
    def test_homework_image_23(self, get_driver):
        # # 有窗口切换，强制等待
        # time.sleep(1)
        # # 登录后窗口改变，获取新窗口
        # get_win(get_driver, -3)
        time.sleep(1)
        # 点击表情按钮
        homeworkadaption = H5Page().click_self_adaptionhomework_image(get_driver)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -35, 5).perform()
        # ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -57, -37).perform()

        x, y = pag.position()
        print(x, y)
        time.sleep(1)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        # 1
        time.sleep(2)
        homeworkimg = H5Page().click_homework_image(get_driver)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -57, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -87, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -117, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -147, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -177, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -207, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, 10, -10).perform()
        ActionChains(get_driver).move_to_element_with_offset(homeworkimg, -237, -37).perform()
        x, y = pag.position()
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)
        H5Page().click_homework_text(get_driver)
        time.sleep(1)
        print("添加文字完")
        p1 = random.randint(700, 1000)
        p2 = random.randint(200, 800)
        p3 = random.randint(800, 900)
        p4 = random.randint(300, 700)

        print("p1,p2", p1, p2)
        print("p3,p4", p3, p4)

        win32api.SetCursorPos([p1, p2])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        H5Page().input_homework_text(get_driver, "89808098tun急急急吼吼吼吼韩国")

        time.sleep(1)
        win32api.SetCursorPos([p3, p4])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        H5Page().input_homework_text(get_driver, "3434并迅速必须八十八")

        H5Page().click_homework_shape(get_driver)
        H5Page().input_homework_shape(get_driver)

        p1 = random.randint(700, 1000)
        p2 = random.randint(200, 800)
        p3 = random.randint(800, 900)
        p4 = random.randint(300, 700)

        print("p1,p2", p1, p2)
        print("p3,p4", p3, p4)
        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')

        time.sleep(1)
        p1 = random.randint(700, 1000)
        p2 = random.randint(200, 800)
        p3 = random.randint(800, 900)
        p4 = random.randint(300, 700)

        print("p1,p2", p1, p2)
        print("p3,p4", p3, p4)
        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')

        time.sleep(1)
        p1 = random.randint(700, 1000)
        p2 = random.randint(200, 800)
        p3 = random.randint(800, 900)
        p4 = random.randint(300, 700)

        print("p1,p2", p1, p2)
        print("p3,p4", p3, p4)
        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')
        time.sleep(1)

        p1 = random.randint(700, 1000)
        p2 = random.randint(200, 800)
        p3 = random.randint(800, 900)
        p4 = random.randint(300, 700)
        print("p1,p2", p1, p2)
        print("p3,p4", p3, p4)

        pyautogui.moveTo(p1, p2)

        pyautogui.dragTo(p3, p4, 0.1, button='left')
        time.sleep(1)




    def test_homework_image_save_26(self, get_driver):
        time.sleep(1)
        ele_clickhomeworkimgsave = H5Page().click_homework_image_save(get_driver)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgsave).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)
        aa = random.randint(0, 10000000)
        bb = random.randint(0, 10000000)
        cc = aa + bb

        print("cc", cc)
        H5Page().click_upload_pic(cc)
        list.append(cc)
        print("pic list", list)
        time.sleep(1)
  #########6
    def test_homework_pic_next_27(self, get_driver):
        ele_clickhomeworkpicnext=H5Page().click_homework_pic_next(get_driver)
        time.sleep(1)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkpicnext).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    def test_homework_image_save_28(self, get_driver):
        ele_clickhomeworkimgsave = H5Page().click_homework_image_save(get_driver)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgsave).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)
        aa = random.randint(0, 10000000)
        bb = random.randint(0, 10000000)
        cc = aa + bb

        print("cc", cc)
        H5Page().click_upload_pic(cc)
        list.append(cc)
        print("pic list", list)
        time.sleep(1)
    ###7
    def test_homework_pic_next_29(self, get_driver):
        ele_clickhomeworkpicnext=H5Page().click_homework_pic_next(get_driver)
        time.sleep(1)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkpicnext).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x,y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    def test_homework_image_save_30(self, get_driver):
        ele_clickhomeworkimgsave = H5Page().click_homework_image_save(get_driver)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgsave).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)
        aa = random.randint(0, 10000000)
        bb = random.randint(0, 10000000)
        cc = aa + bb

        print("cc", cc)
        H5Page().click_upload_pic(cc)
        list.append(cc)
        print("pic list", list)
        time.sleep(1)
    ###8

    def test_homework_pic_next_31(self, get_driver):
        ele_clickhomeworkpicnext = H5Page().click_homework_pic_next(get_driver)
        time.sleep(1)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkpicnext).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def test_homework_image_save_32(self, get_driver):
        ele_clickhomeworkimgsave = H5Page().click_homework_image_save(get_driver)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgsave).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)
        aa = random.randint(0, 10000000)
        bb = random.randint(0, 10000000)
        cc = aa + bb

        print("cc", cc)
        H5Page().click_upload_pic(cc)
        list.append(cc)
        print("pic list", list)
        time.sleep(1)

    def test_homework_homework_review_finish_new_33(self, get_driver):
        """找到btn【评分】， 点击旁边的【完成】 """
        ele_homeworkscore=H5Page().click_homework_score(get_driver)
        ActionChains(get_driver).move_to_element_with_offset(ele_homeworkscore, 150, 10).click().perform()
        time.sleep(1)


    def test_homework_homework_review_rereview_34(self, get_web_driver):
        """ 点击作业详情页面的【完成】 """
        get_win(get_web_driver, 2)
        H5Page().click_homework_finish(get_web_driver)
        # 再点击【重新批阅】
        H5Page().click_homework_re_review(get_web_driver)

    def test_homework_review_new_35(self, get_web_driver):
        """再点击图片"""
        H5Page().click_pic(get_web_driver)

#######################################
  #1
    def test_homework_image_save_40(self, get_driver):
        """ 图片编辑页面，点击保存本地，用于比较 """
        time.sleep(1)
        # 登录后窗口改变，获取新窗口
        get_win(get_driver, -3)
        time.sleep(1)
        homeworkadaption = H5Page().click_self_adaptionhomework_image(get_driver)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -35, 5).perform()
        # ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -57, -37).perform()

        x, y = pag.position()
        print(x, y)
        time.sleep(1)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        # 1
        time.sleep(2)
        ele_clickhomeworkimgsave = H5Page().click_homework_image_save(get_driver)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgsave).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x, y)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


        time.sleep(1)
        aa = random.randint(0, 10000000)
        bb = random.randint(0, 10000000)
        cc = 'review'

        dd = str(aa) + str(bb) + cc

        print("dd0", dd)


        H5Page().click_upload_pic(dd)
        list1.append(dd)
        print("pic list view0", list1)
        time.sleep(1)

    def test_homework_pic_next_42(self, get_driver):
        """点击下一张：把8张图片依次打开，再保存本地一份"""
        time.sleep(1)
        ele_clickhomeworkpicnext=H5Page().click_homework_pic_next(get_driver)
        time.sleep(1)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkpicnext).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x,y)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)


##2
    def test_homework_image_save_43(self, get_driver):
        time.sleep(1)
        homeworkadaption = H5Page().click_self_adaptionhomework_image(get_driver)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -35, 5).perform()
        # ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -57, -37).perform()

        x, y = pag.position()
        print(x, y)
        time.sleep(1)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        # 1
        time.sleep(2)
        ele_clickhomeworkimgsave = H5Page().click_homework_image_save(get_driver)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgsave).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x, y)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)
        aa = random.randint(0, 10000000)
        bb = random.randint(0, 10000000)
        cc = 'review'

        dd = str(aa) + str(bb) + cc

        print("dd1", dd)


        H5Page().click_upload_pic(dd)
        list1.append(dd)
        print("pic list view1", list1)
        time.sleep(1)

    def test_homework_pic_next_44(self, get_driver):
        time.sleep(1)
        ele_clickhomeworkpicnext = H5Page().click_homework_pic_next(get_driver)
        time.sleep(1)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkpicnext).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x, y)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        time.sleep(1)

    ##3
    def test_homework_image_save_45(self, get_driver):
        time.sleep(1)
        homeworkadaption = H5Page().click_self_adaptionhomework_image(get_driver)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -35, 5).perform()
        # ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -57, -37).perform()

        x, y = pag.position()
        print(x, y)
        time.sleep(1)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        # 1
        time.sleep(2)
        ele_clickhomeworkimgsave = H5Page().click_homework_image_save(get_driver)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgsave).perform()

        x, y = pag.position()
        time.sleep(1)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)
        aa = random.randint(0, 10000000)
        bb = random.randint(0, 10000000)
        cc = 'review'

        dd = str(aa) + str(bb) + cc

        print("dd2", dd)


        H5Page().click_upload_pic(dd)
        list1.append(dd)
        print("pic list view2", list1)
        time.sleep(1)

    def test_homework_pic_next_46(self, get_driver):
        time.sleep(1)
        ele_clickhomeworkpicnext = H5Page().click_homework_pic_next(get_driver)
        time.sleep(1)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkpicnext).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x, y)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)

##4
    def test_homework_image_save_47(self, get_driver):
        time.sleep(1)
        homeworkadaption = H5Page().click_self_adaptionhomework_image(get_driver)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -35, 5).perform()
        # ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -57, -37).perform()

        x, y = pag.position()
        print(x, y)
        time.sleep(1)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        # 1
        time.sleep(2)
        ele_clickhomeworkimgsave = H5Page().click_homework_image_save(get_driver)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgsave).perform()
        x, y = pag.position()
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)
        aa = random.randint(0, 10000000)
        bb = random.randint(0, 10000000)
        cc = 'review'

        dd = str(aa) + str(bb) + cc

        print("dd3", dd)


        H5Page().click_upload_pic(dd)
        list1.append(dd)
        print("pic list view3", list1)
        time.sleep(1)

    def test_homework_pic_next_48(self, get_driver):
        time.sleep(1)
        ele_clickhomeworkpicnext = H5Page().click_homework_pic_next(get_driver)
        time.sleep(1)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkpicnext).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x, y)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)

##5
    def test_homework_image_save_49(self, get_driver):
        time.sleep(1)
        homeworkadaption = H5Page().click_self_adaptionhomework_image(get_driver)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -35, 5).perform()
        # ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -57, -37).perform()

        x, y = pag.position()
        print(x, y)
        time.sleep(1)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        # 1
        time.sleep(2)
        ele_clickhomeworkimgsave = H5Page().click_homework_image_save(get_driver)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgsave).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x, y)
        win32api.SetCursorPos([x, y])
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)
        aa = random.randint(0, 10000000)
        bb = random.randint(0, 10000000)
        cc = 'review'

        dd = str(aa) + str(bb) + cc

        print("dd4", dd)


        H5Page().click_upload_pic(dd)
        list1.append(dd)
        print("pic list view4", list1)
        time.sleep(1)


    def test_homework_pic_next_50(self, get_driver):
        time.sleep(1)
        ele_clickhomeworkpicnext = H5Page().click_homework_pic_next(get_driver)
        time.sleep(1)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkpicnext).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x, y)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)

#6
    def test_homework_image_save_51(self, get_driver):
        time.sleep(1)
        homeworkadaption = H5Page().click_self_adaptionhomework_image(get_driver)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -35, 5).perform()
        # ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -57, -37).perform()

        x, y = pag.position()
        print(x, y)
        time.sleep(1)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        # 1
        time.sleep(2)

        ele_clickhomeworkimgsave = H5Page().click_homework_image_save(get_driver)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgsave).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x, y)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)
        aa = random.randint(0, 10000000)
        bb = random.randint(0, 10000000)
        cc = 'review'

        dd = str(aa) + str(bb) + cc

        print("dd4", dd)


        H5Page().click_upload_pic(dd)
        list1.append(dd)
        print("pic list view4", list1)
        time.sleep(1)


    def test_homework_pic_next_52(self, get_driver):
        time.sleep(1)
        ele_clickhomeworkpicnext = H5Page().click_homework_pic_next(get_driver)
        time.sleep(1)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkpicnext).perform()
        x, y = pag.position()

        print(x, y)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)

#7
    def test_homework_image_save_53(self, get_driver):
        time.sleep(1)
        homeworkadaption = H5Page().click_self_adaptionhomework_image(get_driver)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -35, 5).perform()
        # ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -57, -37).perform()

        x, y = pag.position()
        print(x, y)
        time.sleep(1)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        # 1
        time.sleep(2)
        ele_clickhomeworkimgsave = H5Page().click_homework_image_save(get_driver)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgsave).perform()
        x, y = pag.position()

        print(x, y)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)
        aa = random.randint(0, 10000000)
        bb = random.randint(0, 10000000)
        cc = 'review'

        dd = str(aa) + str(bb) + cc

        print("dd4", dd)


        H5Page().click_upload_pic(dd)
        list1.append(dd)
        print("pic list view4", list1)
        time.sleep(1)

    def test_homework_pic_next_54(self, get_driver):
        time.sleep(1)
        ele_clickhomeworkpicnext = H5Page().click_homework_pic_next(get_driver)
        time.sleep(1)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkpicnext).perform()
        x, y = pag.position()

        print(x, y)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)

##8
    def test_homework_image_save_55(self, get_driver):
        time.sleep(1)
        homeworkadaption = H5Page().click_self_adaptionhomework_image(get_driver)
        time.sleep(1)

        ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -35, 5).perform()
        # ActionChains(get_driver).move_to_element_with_offset(homeworkadaption, -57, -37).perform()

        x, y = pag.position()
        print(x, y)
        time.sleep(1)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)
        # 模拟鼠标左键放开。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        # 1
        time.sleep(2)
        ele_clickhomeworkimgsave = H5Page().click_homework_image_save(get_driver)
        ActionChains(get_driver).move_to_element(ele_clickhomeworkimgsave).perform()
        x, y = pag.position()
        time.sleep(1)
        print(x, y)
        win32api.SetCursorPos([x, y])
        time.sleep(1)
        # 模拟鼠标左键按下。
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(1)
        aa = random.randint(0, 10000000)
        bb = random.randint(0, 10000000)
        cc = 'review'

        dd = str(aa) + str(bb) + cc

        print("dd4", dd)


        H5Page().click_upload_pic(dd)
        list1.append(dd)
        print("pic list view4", list1)
        time.sleep(1)


    def test_homework_homework_review_finish_new_56(self, get_driver):
        """ 找到【评分】， 点击旁边的【完成】"""
        ele_homeworkscore=H5Page().click_homework_score(get_driver)

        ActionChains(get_driver).move_to_element_with_offset(ele_homeworkscore, 150, 10).click().perform()

        time.sleep(1)
    def test_homework_homework_review_rereview_57(self, get_web_driver):
        get_win(get_web_driver, 2)
        H5Page().click_homework_finish(get_web_driver)
        H5Page().click_review_closed(get_web_driver)



    def test_homework_pic_compare_600(self, get_web_driver):
        rootpath = H5Page().get_rootpath()

        image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[0]) + ".jpeg")
        # print("image1",image1)

        image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[0]) + ".jpeg")

        difference = cv2.subtract(image1, image2)
        print("difference", difference)
        result = not np.any(difference)  # if difference is all zeros it will return False

        try:
            assert result == True
            print("图片0一样")
        except AssertionError:
            print("图片0不一样")
            raise AssertionError

    def test_homework_pic_compare_601(self, get_web_driver):
        rootpath = H5Page().get_rootpath()

        image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[1]) + ".jpeg")

        image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[1]) + ".jpeg")

        difference = cv2.subtract(image1, image2)
        print("difference", difference)
        result = not np.any(difference)  # if difference is all zeros it will return False

        try:
            assert result == True
            print("图片1一样")
        except AssertionError:
            print("图片1不一样")
            raise AssertionError

    def test_homework_pic_compare_602(self, get_web_driver):
        rootpath = H5Page().get_rootpath()

        image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[2]) + ".jpeg")

        image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[2]) + ".jpeg")

        difference = cv2.subtract(image1, image2)
        print("difference", difference)
        result = not np.any(difference)  # if difference is all zeros it will return False

        try:
            assert result == True
            print("图片2一样")
        except AssertionError:
            print("图片2不一样")
            raise AssertionError

    def test_homework_pic_compare_603(self, get_web_driver):
        rootpath = H5Page().get_rootpath()

        image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[3]) + ".jpeg")

        image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[3]) + ".jpeg")

        difference = cv2.subtract(image1, image2)
        print("difference", difference)
        result = not np.any(difference)  # if difference is all zeros it will return False

        try:
            assert result == True
            print("图片3一样")
        except AssertionError:
            print("图片3不一样")
            raise AssertionError

    def test_homework_pic_compare_604(self, get_web_driver):
        rootpath = H5Page().get_rootpath()

        image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[4]) + ".jpeg")

        image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[4]) + ".jpeg")

        difference = cv2.subtract(image1, image2)
        print("difference", difference)
        result = not np.any(difference)  # if difference is all zeros it will return False

        try:
            assert result == True
            print("图片4一样")
        except AssertionError:
            print("图片4不一样")
            raise AssertionError

    def test_homework_pic_compare_605(self, get_web_driver):
        rootpath = H5Page().get_rootpath()

        image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[5]) + ".jpeg")

        image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[5]) + ".jpeg")

        difference = cv2.subtract(image1, image2)
        print("difference", difference)
        result = not np.any(difference)  # if difference is all zeros it will return False

        try:
            assert result == True
            print("图片5一样")
        except AssertionError:
            print("图片5不一样")
            raise AssertionError

    def test_homework_pic_compare_606(self, get_web_driver):
        rootpath = H5Page().get_rootpath()

        image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[6]) + ".jpeg")

        image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[6]) + ".jpeg")

        difference = cv2.subtract(image1, image2)
        print("difference", difference)
        result = not np.any(difference)  # if difference is all zeros it will return False

        try:
            assert result == True
            print("图片6一样")
        except AssertionError:
            print("图片6不一样")
            raise AssertionError

    def test_homework_pic_compare_607(self, get_web_driver):
        rootpath = H5Page().get_rootpath()

        image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[7]) + ".jpeg")

        image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[7]) + ".jpeg")

        difference = cv2.subtract(image1, image2)
        print("difference", difference)
        result = not np.any(difference)  # if difference is all zeros it will return False

        try:
            assert result == True
            print("图片7一样")
        except AssertionError:
            print("图片7不一样")
            raise AssertionError

    """
    另一种，图片比较方式
    """

    # def test_homework_pic_compare_600(self, get_web_driver):
    #         rootpath=H5Page().get_rootpath()
    #
    #
    #         image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/'+str(list[0])+".jpeg")
    #         print    ("image1",image1)
    #
    #         image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/'+str(list1[0])+".jpeg")
    #
    #
    #         difference = cv2.subtract(image1, image2)
    #         result = not np.any(difference)  # if difference is all zeros it will return False
    #
    #         try:
    #             assert result == True
    #             print("图片0一样")
    #         except AssertionError:
    #             print("图片0不一样")
    #             raise AssertionError
    #
    # def test_homework_pic_compare_601(self, get_web_driver):
    #         rootpath = H5Page().get_rootpath()
    #
    #         image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[1]) + ".jpeg")
    #
    #         image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[1]) + ".jpeg")
    #
    #         difference = cv2.subtract(image1, image2)
    #         result = not np.any(difference)  # if difference is all zeros it will return False
    #
    #         try:
    #             assert result == True
    #             print("图片1一样")
    #         except AssertionError:
    #             print("图片1不一样")
    #             raise AssertionError
    #
    # def test_homework_pic_compare_602(self, get_web_driver):
    #         rootpath = H5Page().get_rootpath()
    #
    #         image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[2]) + ".jpeg")
    #
    #         image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[2]) + ".jpeg")
    #
    #         difference = cv2.subtract(image1, image2)
    #         result = not np.any(difference)  # if difference is all zeros it will return False
    #
    #         try:
    #             assert result == True
    #             print("图片2一样")
    #         except AssertionError:
    #             print("图片2不一样")
    #             raise AssertionError
    #
    # def test_homework_pic_compare_603(self, get_web_driver):
    #         rootpath = H5Page().get_rootpath()
    #
    #         image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[3]) + ".jpeg")
    #
    #         image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[3]) + ".jpeg")
    #
    #         difference = cv2.subtract(image1, image2)
    #         result = not np.any(difference)  # if difference is all zeros it will return False
    #
    #         try:
    #                 assert result == True
    #                 print("图片3一样")
    #         except AssertionError:
    #                 print("图片3不一样")
    #                 raise AssertionError
    #
    # def test_homework_pic_compare_604(self, get_web_driver):
    #         rootpath = H5Page().get_rootpath()
    #
    #         image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[4]) + ".jpeg")
    #
    #         image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[4]) + ".jpeg")
    #
    #         difference = cv2.subtract(image1, image2)
    #         result = not np.any(difference)  # if difference is all zeros it will return False
    #
    #         try:
    #                     assert result == True
    #                     print("图片4一样")
    #         except AssertionError:
    #                     print("图片4不一样")
    #                     raise AssertionError
    #
    # def test_homework_pic_compare_605(self, get_web_driver):
    #         rootpath = H5Page().get_rootpath()
    #
    #         image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[5]) + ".jpeg")
    #
    #         image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[5]) + ".jpeg")
    #
    #         difference = cv2.subtract(image1, image2)
    #         result = not np.any(difference)  # if difference is all zeros it will return False
    #
    #         try:
    #                         assert result == True
    #                         print("图片5一样")
    #         except AssertionError:
    #                         print("图片5不一样")
    #                         raise AssertionError
    #
    # def test_homework_pic_compare_606(self, get_web_driver):
    #         rootpath = H5Page().get_rootpath()
    #
    #         image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[6]) + ".jpeg")
    #
    #         image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[6]) + ".jpeg")
    #
    #         difference = cv2.subtract(image1, image2)
    #         result = not np.any(difference)  # if difference is all zeros it will return False
    #
    #         try:
    #                             assert result == True
    #                             print("图片6一样")
    #         except AssertionError:
    #                             print("图片6不一样")
    #                             raise AssertionError
    #
    # def test_homework_pic_compare_607(self, get_web_driver):
    #             rootpath = H5Page().get_rootpath()
    #
    #             image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[7]) + ".jpeg")
    #
    #             image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[7]) + ".jpeg")
    #
    #             difference = cv2.subtract(image1, image2)
    #             result = not np.any(difference)  # if difference is all zeros it will return False
    #
    #             try:
    #                 assert result == True
    #                 print("图片7一样")
    #             except AssertionError:
    #                 print("图片7不一样")
    #                 raise AssertionError
        # def test_homework_pic_compare_603(self, get_web_driver):
        #     rootpath = HomeworkReviewPage().get_rootpath()
        #
        #     image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[3]) + ".jpeg")
        #
        #     image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[3]) + ".jpeg")
        #
        #     difference = cv2.subtract(image1, image2)
        #     result = not np.any(difference)  # if difference is all zeros it will return False
        #
        #     try:
        #         assert result == True
        #         print("图片3一样")
        #     except AssertionError:
        #         print("图片3不一样")
        #         raise AssertionError

        # def test_homework_pic_compare_604(self, get_web_driver):
        #     rootpath = HomeworkReviewPage().get_rootpath()
        #
        #     image1 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[4]) + ".jpeg")
        #
        #     image2 = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[4]) + ".jpeg")
        #
        #     difference = cv2.subtract(image1, image2)
        #     result = not np.any(difference)  # if difference is all zeros it will return False
        #
        #     try:
        #         assert result == True
        #         print("图片4一样")
        #     except AssertionError:
        #         print("图片4不一样")
        #     raise AssertionError


##################10/18
    # def test_homework_pic_compare_600(self, get_web_driver):
    #
    #     current_path = os.path.abspath(__file__)
    #     a = current_path.split('\\')[:-5]
    #     fat = '/'.join(a)
    #     rootpath = fat
    #     imageA = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[0]) + ".jpeg")
    #     imageB = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[0]) + ".jpeg")
    #
    #     grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    #     grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    #
    #     (score, diff) = structural_similarity(grayA, grayB, full=True)
    #     diff = (diff * 255).astype("uint8")
    #
    #     thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    #
    #     cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #
    #     cnts = cnts[1] if imutils.is_cv2() else cnts[0]
    #     print("cnts", cnts)
    #     try:
    #         assert cnts == ()
    #         print("图片0一样")
    #     except AssertionError:
    #
    #         for c in cnts:
    #             (x, y, w, h) = cv2.boundingRect(c)
    #             cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #             cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #
    #         # 用cv2.imshow 展现最终对比之后的图片， cv2.imwrite 保存最终的结果图片
    #
    #         # cv2.imshow("differ", imageB)
    #         cv2.imwrite("differ0.png", imageB)
    #         cv2.waitKey(0)
    #         print("图片0不一样")
    #         raise AssertionError
    #
    # def test_homework_pic_compare_601(self, get_web_driver):
    #     current_path = os.path.abspath(__file__)
    #     a = current_path.split('\\')[:-5]
    #     fat = '/'.join(a)
    #     rootpath = fat
    #     imageA = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[1]) + ".jpeg")
    #     imageB = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[1]) + ".jpeg")
    #
    #     grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    #     grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    #
    #     (score, diff) = structural_similarity(grayA, grayB, full=True)
    #     diff = (diff * 255).astype("uint8")
    #
    #     thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    #
    #     cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #
    #     cnts = cnts[1] if imutils.is_cv2() else cnts[0]
    #     print("cnts", cnts)
    #     try:
    #         assert cnts == ()
    #         print("图片1一样")
    #     except AssertionError:
    #
    #         for c in cnts:
    #             (x, y, w, h) = cv2.boundingRect(c)
    #             cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #             cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #
    #         # 用cv2.imshow 展现最终对比之后的图片， cv2.imwrite 保存最终的结果图片
    #
    #         # cv2.imshow("differ", imageB)
    #         cv2.imwrite("differ1.png", imageB)
    #         cv2.waitKey(0)
    #         print("图片1不一样")
    #         raise AssertionError
    # def test_homework_pic_compare_602(self, get_web_driver):
    #     current_path = os.path.abspath(__file__)
    #     a = current_path.split('\\')[:-5]
    #     fat = '/'.join(a)
    #     rootpath = fat
    #     imageA = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[2]) + ".jpeg")
    #     imageB = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[2]) + ".jpeg")
    #
    #     grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    #     grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    #
    #     (score, diff) = structural_similarity(grayA, grayB, full=True)
    #     diff = (diff * 255).astype("uint8")
    #
    #     thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    #
    #     cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #
    #     cnts = cnts[1] if imutils.is_cv2() else cnts[0]
    #     print("cnts", cnts)
    #     try:
    #         assert cnts == ()
    #         print("图片2一样")
    #     except AssertionError:
    #
    #         for c in cnts:
    #             (x, y, w, h) = cv2.boundingRect(c)
    #             cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #             cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #
    #         # 用cv2.imshow 展现最终对比之后的图片， cv2.imwrite 保存最终的结果图片
    #
    #         # cv2.imshow("differ", imageB)
    #         cv2.imwrite("differ2.png", imageB)
    #         cv2.waitKey(0)
    #         print("图片2不一样")
    #         raise AssertionError
    #
    # def test_homework_pic_compare_603(self, get_web_driver):
    #     current_path = os.path.abspath(__file__)
    #     a = current_path.split('\\')[:-5]
    #     fat = '/'.join(a)
    #     rootpath = fat
    #     imageA = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[3]) + ".jpeg")
    #     imageB = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[3]) + ".jpeg")
    #
    #     grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    #     grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    #
    #     (score, diff) = structural_similarity(grayA, grayB, full=True)
    #     diff = (diff * 255).astype("uint8")
    #
    #     thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    #
    #     cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #
    #     cnts = cnts[1] if imutils.is_cv2() else cnts[0]
    #     print("cnts", cnts)
    #     try:
    #         assert cnts == ()
    #         print("图片3一样")
    #     except AssertionError:
    #
    #         for c in cnts:
    #             (x, y, w, h) = cv2.boundingRect(c)
    #             cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #             cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #
    #         # 用cv2.imshow 展现最终对比之后的图片， cv2.imwrite 保存最终的结果图片
    #
    #         # cv2.imshow("differ", imageB)
    #         cv2.imwrite("differ3.png", imageB)
    #         cv2.waitKey(0)
    #         print("图片3不一样")
    #         raise AssertionError
    #
    # def test_homework_pic_compare_604(self, get_web_driver):
    #     current_path = os.path.abspath(__file__)
    #     a = current_path.split('\\')[:-5]
    #     fat = '/'.join(a)
    #     rootpath = fat
    #     imageA = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[4]) + ".jpeg")
    #     imageB = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[4]) + ".jpeg")
    #
    #     grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    #     grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    #
    #     (score, diff) = structural_similarity(grayA, grayB, full=True)
    #     diff = (diff * 255).astype("uint8")
    #
    #     thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    #
    #     cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #
    #     cnts = cnts[1] if imutils.is_cv2() else cnts[0]
    #     print("cnts", cnts)
    #     try:
    #         assert cnts == ()
    #         print("图片4一样")
    #     except AssertionError:
    #
    #         for c in cnts:
    #             (x, y, w, h) = cv2.boundingRect(c)
    #             cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #             cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #
    #         # 用cv2.imshow 展现最终对比之后的图片， cv2.imwrite 保存最终的结果图片
    #
    #         # cv2.imshow("differ4", imageB)
    #         cv2.imwrite("differ.png", imageB)
    #         cv2.waitKey(0)
    #         print("图片4不一样")
    #         raise AssertionError
    #
    # def test_homework_pic_compare_605(self, get_web_driver):
    #     current_path = os.path.abspath(__file__)
    #     a = current_path.split('\\')[:-5]
    #     fat = '/'.join(a)
    #     rootpath = fat
    #     imageA = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[5]) + ".jpeg")
    #     imageB = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[5]) + ".jpeg")
    #
    #     grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    #     grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    #
    #     (score, diff) = structural_similarity(grayA, grayB, full=True)
    #     diff = (diff * 255).astype("uint8")
    #
    #     thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    #
    #     cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #
    #     cnts = cnts[1] if imutils.is_cv2() else cnts[0]
    #     print("cnts", cnts)
    #     try:
    #         assert cnts == ()
    #         print("图片5一样")
    #     except AssertionError:
    #
    #         for c in cnts:
    #             (x, y, w, h) = cv2.boundingRect(c)
    #             cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #             cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #
    #         # 用cv2.imshow 展现最终对比之后的图片， cv2.imwrite 保存最终的结果图片
    #
    #         # cv2.imshow("differ", imageB)
    #         cv2.imwrite("differ5.png", imageB)
    #         cv2.waitKey(0)
    #         print("图片5不一样")
    #         raise AssertionError
    #
    # def test_homework_pic_compare_606(self, get_web_driver):
    #     current_path = os.path.abspath(__file__)
    #     a = current_path.split('\\')[:-5]
    #     fat = '/'.join(a)
    #     rootpath = fat
    #     imageA = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[6]) + ".jpeg")
    #     imageB = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[6]) + ".jpeg")
    #
    #     grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    #     grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    #
    #     (score, diff) = structural_similarity(grayA, grayB, full=True)
    #     diff = (diff * 255).astype("uint8")
    #
    #     thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    #
    #     cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #
    #     cnts = cnts[1] if imutils.is_cv2() else cnts[0]
    #     print("cnts", cnts)
    #     try:
    #         assert cnts == ()
    #         print("图片6一样")
    #     except AssertionError:
    #
    #         for c in cnts:
    #             (x, y, w, h) = cv2.boundingRect(c)
    #             cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #             cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #
    #         # 用cv2.imshow 展现最终对比之后的图片， cv2.imwrite 保存最终的结果图片
    #
    #         # cv2.imshow("differ", imageB)
    #         cv2.imwrite("differ6.png", imageB)
    #         cv2.waitKey(0)
    #         print("图片6不一样")
    #         raise AssertionError
    #
    # def test_homework_pic_compare_607(self, get_web_driver):
    #     current_path = os.path.abspath(__file__)
    #     a = current_path.split('\\')[:-5]
    #     fat = '/'.join(a)
    #     rootpath = fat
    #     imageA = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[7]) + ".jpeg")
    #     imageB = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[7]) + ".jpeg")
    #
    #     grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    #     grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    #
    #     (score, diff) = structural_similarity(grayA, grayB, full=True)
    #     diff = (diff * 255).astype("uint8")
    #
    #     thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    #
    #     cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #
    #     cnts = cnts[1] if imutils.is_cv2() else cnts[0]
    #     print("cnts", cnts)
    #     try:
    #         assert cnts == ()
    #         print("图片7一样")
    #     except AssertionError:
    #
    #         for c in cnts:
    #             (x, y, w, h) = cv2.boundingRect(c)
    #             cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #             cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #
    #         # 用cv2.imshow 展现最终对比之后的图片， cv2.imwrite 保存最终的结果图片
    #
    #         # cv2.imshow("differ", imageB)
    #         cv2.imwrite("differ7.png", imageB)
    #         cv2.waitKey(0)
    #         print("图片7不一样")
    #         raise AssertionError


