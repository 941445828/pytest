# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 录课&非录课模式，全员下课，都有弹窗提示”确定下课？“
录课模式， 仅自己离开，有弹窗提示”确定关闭教室？“
非录课模式，仅自己开始，无弹窗提示，直接退出教室
"""
import allure, time
from handler.getWinHandler import get_win
from version.v5000.pageobject.quitOnlineClassRoom_page import QuitOnlineClassRoomPage


@allure.feature("班级")
@allure.story("测试-班级-退出在线教室--全员下课")
class TestQuitOnlineClassRoom:
    """录课&非录课模式--全员下课"""
    @allure.title('退出(在线教室)--全员下课')
    @allure.description("测试：退出(在线教室)--全员下课")
    def test_quit_classroom(self, get_driver, get_function_name):
        QuitOnlineClassRoomPage().get_titlebar(get_driver)

        QuitOnlineClassRoomPage().get_thirdpart(get_driver)

        QuitOnlineClassRoomPage().get_toolbarinroom(get_driver)

        QuitOnlineClassRoomPage().click_close(get_driver)

        get_win(get_driver, 0)
        time.sleep(2)

        # # 通过locaion 退出
        # ele_win = find_element(get_driver, '仅自己离开、全员下课、取消', 'ClassName', 'ActionFinishClass')
        # ele_win.click()
        # ActionChains(get_driver).move_to_element_with_offset(ele_win, 80, 18).click().perform()
        # time.sleep(2)

        # 点击“全员下课”
        QuitOnlineClassRoomPage().click_all_end(get_driver)
        get_win(get_driver, 0)
        time.sleep(2)
        QuitOnlineClassRoomPage().click_all_sure(get_driver)
        time.sleep(2)
        get_win(get_driver, 0)
        time.sleep(2)


@allure.feature("班级")
@allure.story("测试-班级-退出在线教室--非录课模式--仅自己离开")
class TestQuitNoLuKeOnlyOne:
    @allure.title('退出(在线教室--非录课模式)--仅自己离开')
    @allure.description("测试：退出(在线教室--非录课模式)--仅自己离开")
    def test_quit(self, get_driver, get_function_name):
        QuitOnlineClassRoomPage().get_titlebar(get_driver)

        QuitOnlineClassRoomPage().get_thirdpart(get_driver)

        QuitOnlineClassRoomPage().get_toolbarinroom(get_driver)

        QuitOnlineClassRoomPage().click_close(get_driver)

        get_win(get_driver, 0)
        time.sleep(2)

        # 点击“仅自己离开”
        QuitOnlineClassRoomPage().click_end(get_driver)
        get_win(get_driver, 0)
        time.sleep(2)


@allure.feature("班级")
@allure.story("测试-班级-退出在线教室--录课模式--仅自己离开")
class TestQuitLuKeOnlyOne:
    @allure.title('退出(在线教室--录课模式)--仅自己离开')
    @allure.description("测试：退出(在线教室--录课模式)--仅自己离开")
    def test_quit(self, get_driver, get_function_name):
        QuitOnlineClassRoomPage().get_titlebar(get_driver)

        QuitOnlineClassRoomPage().get_thirdpart(get_driver)

        QuitOnlineClassRoomPage().get_toolbarinroom(get_driver)

        QuitOnlineClassRoomPage().click_close(get_driver)

        get_win(get_driver, 0)
        time.sleep(2)

        # 点击“仅自己离开”
        QuitOnlineClassRoomPage().click_end(get_driver)
        get_win(get_driver, 0)
        time.sleep(2)
        QuitOnlineClassRoomPage().click_sure(get_driver)
        time.sleep(2)
        get_win(get_driver, 0)
        time.sleep(2)




############### 学生端操作
class TestStuQuitOnlineClassRoom:
    def test_quit(self, get_driver, get_function_name):
        QuitOnlineClassRoomPage().get_titlebar(get_driver)
        QuitOnlineClassRoomPage().get_thirdpart(get_driver)
        QuitOnlineClassRoomPage().get_toolbarinroom(get_driver)
        QuitOnlineClassRoomPage().click_close(get_driver)
        get_win(get_driver, 0)
        time.sleep(2)


# class TestStu