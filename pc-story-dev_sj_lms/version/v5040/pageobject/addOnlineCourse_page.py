# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
import time
from version.v5000.pagelocator import addOnlineCourse_locator as AOC
from handler.eleHandler import find_element


class AddOnlineCoursePage(object):
    # 点击课程tab
    def click_kecheng_tab(self, driver):
        ele = AOC.Tab_KeCheng
        ele_kecheng_tab = find_element(driver, ele[0], ele[1], ele[2])[3]
        ele_kecheng_tab.click()

    # 点击’添加课节‘button
    def click_addOnlineCourse_button(self, driver):
        ele = AOC.Add_Course
        ele_add = find_element(driver, ele[0], ele[1], ele[2])
        ele_add.click()

    # 输入课节名称
    def input_cousername(self, driver, course_name):
        ele = AOC.Course_Text
        ele_course_text = find_element(driver, ele[0], ele[1], ele[2])
        ele_course_text.click()
        ele_course_text.clear()
        course_name = course_name.split('_')[0] + '_' + str(int(time.time()))
        ele_course_text.send_keys(course_name)

    # 选择在线教室模式
    def choose_coursemode(self, driver):
        ele = AOC.Course_Mode
        ele_teach_mode = find_element(driver, ele[0], ele[1], ele[2])[0]  # 在线教室
        ele_teach_mode.click()

    # 勾选录课
    def choose_lukemode(self, driver):
        ele = AOC.Luke_Mode
        ele_luke = find_element(driver, ele[0], ele[1], ele[2])
        ele_luke[0].click()   # 勾选录制教室
        ele_luke[1].click()   # 勾选录制现场

    # 勾选直播
    def choose_zhibo(self, driver):
        ele = AOC.ZhiBo
        ele_zhibo = find_element(driver, ele[0], ele[1], ele[2])
        ele_zhibo.click()

    # 勾选回放
    def choose_huifang(self, driver):
        ele = AOC.HuiFang
        ele_huifang = find_element(driver, ele[0], ele[1], ele[2])
        ele_huifang.click()

    # 点击创建button
    def click_create_button(self, driver):
        ele = AOC.CreateButton
        ele_create = find_element(driver, ele[0], ele[1], ele[2])
        ele_create.click()

    # 课程列表H5页，点击【上课】btn
    def click_btn_begin_class(self, driver):
        ele = AOC.H5_Enter_Room
        ele_enter = find_element(driver, ele[0], ele[1], ele[2])
        ele_enter[-1].click()

    # 点击”上课“，进入教室内
    def click_enter_room(self, driver):
        ele = AOC.Enter_Room
        ele_enter = find_element(driver, ele[0], ele[1], ele[2])
        ele_enter.click()

    # 点击教室内的 “进入教室”
    def click_enter(self, driver):
        ele = AOC.Enter
        ele_enter = find_element(driver, ele[0], ele[1], ele[2])
        ele_enter.click()

    # 点击录课提示的 “确定”
    def click_sure(self, driver):
        ele = AOC.Sure
        ele_sure = find_element(driver, ele[0], ele[1], ele[2])
        ele_sure.click()

    # 点击“立即录课”
    def click_luke(self, driver):
        ele = AOC.LuKe
        ele_luke = find_element(driver, ele[0], ele[1], ele[2])
        ele_luke.click()