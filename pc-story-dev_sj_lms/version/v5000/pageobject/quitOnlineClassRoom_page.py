# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from version.v5000.pagelocator import quitOnlineClassRoom_locator as QUIT
from handler.eleHandler import find_element


class QuitOnlineClassRoomPage(object):
    def get_titlebar(self, driver):
        ele = QUIT.TitleBar
        ele_titlebar = find_element(driver, ele[0], ele[1], ele[2])
        return ele_titlebar

    def get_thirdpart(self, driver):
        ele = QUIT.Third_Part
        ele_third = self.get_titlebar(driver).find_elements_by_class_name(ele[2])[1]
        return ele_third

    def get_toolbarinroom(self, driver):
        ele = QUIT.ToolBarInRoom
        ele_tool = self.get_thirdpart(driver).find_element_by_class_name(ele[2])
        return ele_tool

    def click_close(self, driver):
        ele = QUIT.Close_Room
        ele_close = self.get_toolbarinroom(driver).find_elements_by_class_name(ele[2])[2]
        ele_close.click()

    def click_end(self, driver):
        ele = QUIT.End
        ele_end = find_element(driver, ele[0], ele[1], ele[2])
        ele_end.click()

    def click_sure(self, driver):
        ele = QUIT.Sure
        ele_sure = find_element(driver, ele[0], ele[1], ele[2])
        ele_sure.click()

    def click_all_end(self, driver):
        ele = QUIT.AllEnd
        ele_end = find_element(driver, ele[0], ele[1], ele[2])
        ele_end.click()

    def click_all_sure(self, driver):
        ele = QUIT.AllSure
        ele_sure = find_element(driver, ele[0], ele[1], ele[2])
        ele_sure.click()


