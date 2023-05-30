# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from selenium.webdriver.common.keys import Keys
from version.v5030.pagelocator import onlineClassRoom_locator as online
from handler.eleHandler import find_element
import pyautogui
from selenium.webdriver import ActionChains
import random
import time
from handler.logHandler import logger


class OnlineClassRoomPage(object):
    def get_screen(self):
        """获取当前screen 分辨率"""
        screen_x, screen_y = pyautogui.size()
        x = random.randint(50, screen_x - 80)
        y = random.randint(200, screen_y - 40)
        return x, y


    def get_whole_classRoom_page(self, driver):
        """获取整个教室页面区域"""
        ele = online.wholeLocation
        ele_whole_page = find_element(driver, ele[0], ele[1], ele[2])
        return ele_whole_page


    def get_room_titlebar(self, driver):
        """获取教室头部操作区域"""
        ele = online.titleBar
        ele_titlebar = find_element(driver, ele[0], ele[1], ele[2])
        return ele_titlebar


    """顶部设置"""
    def click_setting_btn(self, driver):
        ele = online.setting_area
        ele_setting = find_element(driver, ele[0], ele[1], ele[2])
        ele_setting.click()

    def click_setting(self, driver):
        """点击设置项"""
        ele = online.setting
        ele_setting = find_element(driver, ele[0], ele[1], ele[2])
        ele_setting.click()

    def click_virtual(self, driver):
        """点击虚拟背景item"""
        ele = online.virtual
        ele_virtual = find_element(driver, ele[0], ele[1], ele[2])
        ele_virtual.click()

    def click_background_virtual(self, driver):
        """ 点击 背景虚化"""
        ele = online.virtual_backup
        ele_item = find_element(driver, ele[0], ele[1], ele[2])
        ele_item.click()

    def click_setting_win_close(self, driver):
        """ 关闭 设置 窗口"""
        ele = online.setting_close
        ele_close = find_element(driver, ele[0], ele[1], ele[2])
        ele_close.click()

    def click_title_block_camera(self, driver):
        """标题栏上的摄像头设置"""
        ele = online.title_camera
        ele_camera = self.get_titlebar(driver).find_element_by_xpath(ele[2])
        ele_camera.click()

    def click_video(self, driver):
        ele = online.video
        ele_video = find_element(driver, ele[0], ele[1], ele[2])
        ele_video.click()

    def click_video_list(self, driver):
        ele = online.video_list
        ele_list = find_element(driver, ele[0], ele[1], ele[2])
        ele_list.click()

    def click_video_use_usb(self, driver):
        ele = online.video_usb_item
        ele_usb = find_element(driver, ele[0], ele[1], ele[2])
        ele_usb.click()

    def click_video_ban(self, driver):
        ele = online.video_ban_item
        ele_ban = find_element(driver, ele[0], ele[1], ele[2])
        ele_ban.click()

    """摄像头"""
    def get_camera(self, driver):
        """获取摄像头工具--随机获取台上一个摄像头，并移动它"""
        ele = online.camera
        cameras = find_element(driver, ele[0], ele[1], ele[2])
        ele_camera = None
        n = len(cameras)
        for i in range(n):
            ele_camera = find_element(driver, ele[0], ele[1], ele[2])[i]
        return ele_camera
    def move_camera(self, driver):
        """操作摄像头--移动位置.  除四周黑色条外，其他可操作区域, 再双击摄像头回归原位"""
        x = self.get_screen()[0]
        y = self.get_screen()[1]
        ActionChains(driver).drag_and_drop_by_offset(self.get_camera(driver), x, y).perform()
        ActionChains(driver).double_click(on_element=self.get_camera(driver)).perform()

    def double_click_camera(self, driver):
        ActionChains(driver).double_click(self.get_camera(driver)).perform()

    def move_camera_to_regular(self, driver):
        """操作摄像头--移动到固定位置, 再双击摄像头回归原位"""
        x = self.get_screen()[0]
        y = self.get_screen()[1]
        ActionChains(driver).drag_and_drop_by_offset(self.get_camera(driver), 500, 1500).perform()
        ActionChains(driver).double_click(on_element=self.get_camera(driver)).perform()


    def get_teacher_camera(self, driver):
        """获取 老师的摄像头"""
        ele = online.camera
        cameras = find_element(driver, ele[0], ele[1], ele[2])
        teacher_camera = cameras[-1]
        return teacher_camera

    def reward_all(self, driver):
        """台上学生奖励"""
        self.get_teacher_camera(driver).click()
        ele = online.reward_all
        ele_logo = find_element(driver, ele[0], ele[1], ele[2])
        ele_logo.click()


    def get_mainLotion(self, driver):
        """获取主体区域: 黑板+工具操作区域"""
        ele = online.mainLocation
        ele_main = find_element(driver, ele[0], ele[1], ele[2])
        ele_main.click()
        return ele_main


    def get_toolset(self, driver):
        """获取--整个工具栏区域"""
        ele = online.tookLocation
        ele_toolSet = find_element(driver, ele[0], ele[1], ele[2])
        return ele_toolSet


    """工具--点击"""
    def click_click_icon(self, driver):
        """获取工具--点击, 并操作点击事件"""
        ele = online.click_icon
        ele_click_icon = self.get_toolset(driver).find_elements_by_class_name(ele[2])[0]
        ele_click_icon.click()
        return ele_click_icon


    """工具--画笔"""
    def click_pen_icon(self, driver):
        """获取工具--画笔，点击"""
        ele = online.pen_icon
        ele_pen_icon = self.get_toolset(driver).find_elements_by_class_name(ele[2])[2]
        ele_pen_icon.click()
        return ele_pen_icon

    # 选择粗-细
    def choose_pen_sub(self, driver):
        subs = [online.pen_sub0, online.pen_sub1, online.pen_sub2, online.pen_sub3]
        ele = random.choice(subs)
        ele_pen_sub = find_element(driver, ele[0], ele[1], ele[2])
        ele_pen_sub.click()

    # 选择粗细--选择第一个设置--smoke用例使用
    def choose_pen_sub_first(self, driver):
        ele = online.pen_sub0
        ele_pen_sub = find_element(driver, ele[0], ele[1], ele[2])
        ele_pen_sub.click()

    # 选择连续状-点状
    def choose_pen_model(self, driver):
        models = [online.pen_solid, online.pen_dot]
        ele = random.choice(models)
        ele_pen_model = find_element(driver, ele[0], ele[1], ele[2])
        ele_pen_model.click()

    # 选择连续状-点状--选择第一个设置--smoke用例使用
    def choose_pen_model_first(self, driver):
        ele = online.pen_solid
        ele_pen_model = find_element(driver, ele[0], ele[1], ele[2])
        ele_pen_model.click()

    # 选择线条
    def choose_pen_line(self, driver):
        lines = [online.pen_curve, online.pen_line, online.pen_ellipse, online.pen_rectangle]
        ele = random.choice(lines)
        ele_pen_line = find_element(driver, ele[0], ele[1], ele[2])
        ele_pen_line.click()

    # 选择线条--选择第一个设置--smoke用例使用
    def choose_pen_line_first(self, driver):
        ele = online.pen_curve
        ele_pen_line = find_element(driver, ele[0], ele[1], ele[2])
        ele_pen_line.click()

    # 选择颜色
    def choose_pen_color(self, driver):
        colors = [online.pen_color1, online.pen_color2, online.pen_color3, online.pen_color4,
                  online.pen_color5, online.pen_color6, online.pen_color7, online.pen_color8,
                  online.pen_color9, online.pen_color10, online.pen_color11, online.pen_color12]
        ele = random.choice(colors)
        ele_pen_color = find_element(driver, ele[0], ele[1], ele[2])
        ele_pen_color.click()

    # 选择颜色--选择第一个设置--smoke用例使用
    def choose_pen_color_first(self, driver):
        ele = online.pen_color1
        ele_pen_color = find_element(driver, ele[0], ele[1], ele[2])
        ele_pen_color.click()

    def use_pen(self, driver):
        """使用工具"""
        self.click_pen_icon(driver)
        self.choose_pen_sub(driver)
        self.choose_pen_model(driver)
        self.choose_pen_line(driver)
        self.choose_pen_color(driver)
        x = self.get_screen()[0]
        y = self.get_screen()[1]
        pyautogui.moveTo(x, y)  # 鼠标移动到(x, y)
        m = self.get_screen()[0]
        n = self.get_screen()[1]
        pyautogui.dragTo(m, n, duration=0.5)  # 鼠标拖动到(m, n)

    # 画笔的设置全部选择第一个设置--smoke 使用
    def use_pen_first(self, driver):
        """使用工具"""
        self.click_pen_icon(driver)
        self.choose_pen_sub_first(driver)
        self.choose_pen_model_first(driver)
        self.choose_pen_line_first(driver)
        self.choose_pen_color_first(driver)
        pyautogui.moveTo(500, 500)  # 鼠标移动到(x, y)
        pyautogui.dragTo(1000, 1000, duration=0.5)  # 鼠标拖动到(m, n)


    """工具--选择&移动"""
    def get_choose_icon(self, driver):
        """获取工具--选择&移动, 点击"""
        ele = online.choose_icon
        ele_choose_icon = self.get_toolset(driver).find_elements_by_class_name(ele[2])[1]
        ele_choose_icon.click()
        return ele_choose_icon
    def use_choose_quick_copy(self, driver):
        """使用移动,把选择的内容移动一个位置"""
        self.get_choose_icon(driver)
        x = self.get_screen()[0]
        y = self.get_screen()[1]
        pyautogui.moveTo(x, y)  # 鼠标移动到(x, y)
        m = self.get_screen()[0]
        n = self.get_screen()[1]
        pyautogui.dragTo(m, n, duration=0.5)  # 鼠标拖动到(m, n)
        pyautogui.hotkey('ctrl', 'c')   # 将选中的内容，复制，粘贴
        pyautogui.hotkey('ctrl', 'v')

    def use_choose_quick_copy_smoke(self, driver):
        """使用移动,把选择的内容移动一个位置 -- smoke用例"""
        self.get_choose_icon(driver)
        pyautogui.moveTo(400, 400)  # 鼠标移动到(x, y)
        pyautogui.dragTo(900, 900, duration=0.5)  # 鼠标拖动到(m, n)
        pyautogui.hotkey('ctrl', 'c')   # 将选中的内容，复制，粘贴
        pyautogui.hotkey('ctrl', 'v')

    """工具--截图"""
    def get_cut_icon(self, driver):
        """ 获取工具--截图， 点击"""
        ele = online.cut_icon
        ele_cut_icon = self.get_toolset(driver).find_elements_by_class_name(ele[2])[5]
        ele_cut_icon.click()
        return ele_cut_icon

    def choose_cut(self, driver):
        """ 选择 截图 """
        ele = online.cut_cut
        ele_cut = find_element(driver, ele[0], ele[1], ele[2])
        ele_cut.click()
        x = self.get_screen()[0]
        y = self.get_screen()[1]
        pyautogui.moveTo(x, y)  # 鼠标移动到(x, y)
        m = self.get_screen()[0]
        n = self.get_screen()[1]
        pyautogui.dragTo(m, n, duration=0.5)  # 鼠标拖动到(m, n)
        # time.sleep(2)
        ActionChains(driver).double_click().perform()



    """工具--橡皮擦"""
    def get_rubber_icon(self, driver):
        """获取工具--橡皮擦， 点击"""
        ele = online.rubber_icon
        ele_rubber_icon = self.get_toolset(driver).find_elements_by_class_name(ele[2])[3]
        ele_rubber_icon.click()
        return ele_rubber_icon
    def choose_rubber_model(self, driver):
        """ 选择 橡皮擦 大小"""
        subs = [online.rubber_sub0, online.rubber_sub1, online.rubber_sub2]
        ele = random.choice(subs)
        ele_rubber_sub = find_element(driver, ele[0], ele[1], ele[2])
        ele_rubber_sub.click()

    def choose_rubber_model_smoke(self, driver):
        """ 选择 橡皮擦 大小--smoke使用"""
        ele = online.rubber_sub2
        ele_rubber_sub = find_element(driver, ele[0], ele[1], ele[2])
        ele_rubber_sub.click()

    def use_rubber_icon(self, driver):
        """ 使用工具 橡皮擦"""
        self.get_rubber_icon(driver)
        self.choose_rubber_model(driver)
        x = self.get_screen()[0]
        y = self.get_screen()[1]
        pyautogui.moveTo(x, y)  # 鼠标移动到(x, y)
        m = self.get_screen()[0]
        n = self.get_screen()[1]
        pyautogui.dragTo(m, n, duration=0.5)  # 鼠标按住左键，移动到(m, n)

    def use_rubber_icon_smoke(self, driver):
        """ 使用工具 橡皮擦--smoke使用"""
        self.get_rubber_icon(driver)
        self.choose_rubber_model_smoke(driver)
        pyautogui.moveTo(600, 600)  # 鼠标移动到(x, y)
        pyautogui.dragTo(800, 800, duration=0.5)  # 鼠标按住左键，移动到(m, n)

    def click_rubber_clear(self, driver):
        """ 点击橡皮擦上 清屏btn"""
        self.get_rubber_icon(driver)
        ele = online.rubber_clear_btn
        ele_clear = find_element(driver, ele[0], ele[1], ele[2])
        ele_clear.click()

    def click_clear_promt(self, driver):
        ele_prompt = online.rubber_clear_prompt
        ele_prompt_win = find_element(driver, ele_prompt[0], ele_prompt[1], ele_prompt[2])
        ele_prompt_win.click()


    """工具--文本"""
    def get_text_icon(self, driver):
        """获取工具--文本， 点击"""
        ele = online.text_icon
        ele_text_icon = self.get_toolset(driver).find_elements_by_class_name(ele[2])[4]
        ele_text_icon.click()
        return ele_text_icon

    def choose_text_sub(self, driver):
        """ 选择 文本 字号"""
        subs = [online.text_sub0, online.text_sub1, online.text_sub2, online.text_sub3]
        ele = random.choice(subs)
        ele_text_sub = find_element(driver, ele[0], ele[1], ele[2])
        ele_text_sub.click()

    def choose_text_sub_first(self, driver):
        """ 选择 文本 字号--选择第一个设置--smoke用"""
        ele = online.text_sub0
        ele_text_sub = find_element(driver, ele[0], ele[1], ele[2])
        ele_text_sub.click()

    def choose_text_color(self, driver):
        """ 选择 文本 颜色"""
        colors = [online.text_color1, online.text_color2, online.text_color3, online.text_color4,
                  online.text_color5, online.text_color6, online.text_color7, online.text_color8,
                  online.text_color9, online.text_color10, online.text_color11, online.text_color12]
        ele = random.choice(colors)
        ele_text_color = find_element(driver, ele[0], ele[1], ele[2])
        ele_text_color.click()

    def choose_text_color_first(self, driver):
        """ 选择 文本 颜色--选择第一个设置--smoke用"""
        ele = online.text_color1
        ele_text_color = find_element(driver, ele[0], ele[1], ele[2])
        ele_text_color.click()

    def use_text(self, driver):
        """ 添加 文本 文字"""
        self.get_text_icon(driver)
        self.choose_text_sub(driver)
        self.choose_text_color(driver)
        x = self.get_screen()[0]
        y = self.get_screen()[1]
        pyautogui.click(x, y)

    def use_text_smoke(self, driver):
        """ 添加 文本 文字--smoke使用"""
        self.get_text_icon(driver)
        self.choose_text_sub_first(driver)
        self.choose_text_color_first(driver)
        pyautogui.click(1000, 300)


    """工具--笔记"""
    def get_note_icon(self, driver):
        """获取工具--笔记， 点击"""
        ele = online.note_icon
        ele_note_icon = self.get_toolset(driver).find_elements_by_class_name(ele[2])[10]
        ele_note_icon.click()
        return ele_note_icon
    def use_note_location(self, driver):
        """课堂笔记区域， 获取焦点"""
        ele = online.noteLocation
        ele_note_location = find_element(driver, ele[0], ele[1], ele[2])
        ele_note_location.click()
        return ele_note_location
    def click_add_note(self, driver):
        """添加笔记button"""
        self.get_note_icon(driver)
        self.use_note_location(driver)
        ele = online.noteadd_icon
        ele_noteadd_icon = find_element(driver, ele[0], ele[1], ele[2])
        ele_noteadd_icon.click()
    def add_note_text(self, driver):
        """添加笔记内容"""
        ele = online.notetext_icon
        ele_notetext_icon = find_element(driver, ele[0], ele[1], ele[2])[-1]
        ele_notetext_icon.click()
        time.sleep(1)
        ele_notetext_icon.send_keys("add a note " + str(random.randint(1, 100)))
        pyautogui.moveRel(10, 10)
        pyautogui.click()
        time.sleep(2)

    def add_note_text_smoke(self, driver):
        """添加笔记内容--smoke用例"""
        ele = online.notetext_icon
        ele_notetext_icon = find_element(driver, ele[0], ele[1], ele[2])[-1]
        ele_notetext_icon.click()
        time.sleep(1)
        ele_notetext_icon.send_keys("add a note ")
        pyautogui.moveRel(10, 10)
        pyautogui.click()
        time.sleep(2)

    def close_note_win(self, driver):
        """关闭 笔记 窗口"""
        ele = online.note_win_close
        ele_close = find_element(driver, ele[0], ele[1], ele[2])
        ele_close.click()




    """工具--聊天"""
    def get_chat_icon(self, driver):
        """获取工具--聊天， 点击"""
        ele = online.chat_icon
        ele_chat_icon = self.get_toolset(driver).find_elements_by_class_name(ele[2])[11]
        ele_chat_icon.click()
        return ele_chat_icon
    def edit_chat_content(self, driver):
        """添加聊天内容"""
        self. get_chat_icon(driver)
        ele = online.chat_text_edit
        ele_chat_text = find_element(driver, ele[0], ele[1], ele[2])
        ele_chat_text.click()
        time.sleep(1)
    def click_chat_text_icon(self, driver):
        """点击 聊天的文字输入框"""
        ele = online.chat_text_edit
        ele_chat_text = find_element(driver, ele[0], ele[1], ele[2])
        ele_chat_text.click()
        time.sleep(1)
    def click_chat_cut_icon(self, driver):
        """点击 聊天的 截图icon"""
        ele = online.chat_cut
        ele_chat_cut = find_element(driver, ele[0], ele[1], ele[2])[1]
        ele_chat_cut.click()
        time.sleep(1)
    def add_chat_cut(self, driver):
        """选择截图范围"""
        x = self.get_screen()[0]
        y = self.get_screen()[1]
        pyautogui.moveTo(x, y)  # 鼠标移动到(x, y)
        m = self.get_screen()[0]
        n = self.get_screen()[1]
        print("截图范围，初始位置:{}, drag：{}".format((x, y), (m, n)))
        logger.info("截图范围，初始位置:{}, drag：{}".format((x, y), (m, n)))
        pyautogui.dragTo(m, n, duration=2)  # 鼠标拖动到(m, n)
        ActionChains(driver).double_click().perform()

    def click_add_chat(self, driver):
        """点击【发送】 聊天内容"""
        ele_send = online.chat_send_btn
        ele_send_btn = find_element(driver, ele_send[0], ele_send[1], ele_send[2])
        ele_send_btn.click()
    def close_chat_win(self, driver):
        """关闭聊天窗口"""
        ele = online.chat_win_close
        ele_close = find_element(driver, ele[0], ele[1], ele[2])[2]
        ele_close.click()



    """工具--举手上台"""
    def get_handup_icon(self, driver):
        """点击举手上台icon"""
        ele = online.handUpLocation
        ele_handup = find_element(driver, ele[0], ele[1], ele[2])
        ele_handup.click()
        return ele_handup
    def click_handup_box(self, driver):
        """点击选中"""
        ele = online.handup_box
        ele_box = find_element(driver, ele[0], ele[1], ele[2])
        ele_box.click()


# 花名册
    def get_roster_icon(self, driver):
        """打开花名册"""
        ele = online.roster_icon
        ele_roster_icon = self.get_toolset(driver).find_elements_by_class_name(ele[2])[12]
        ele_roster_icon.click()
        return ele_roster_icon

    def get_roster_tea_operate(self, driver):
        """获取 花名册上老师操作区域"""
        ele = online.roster_tea
        ele_tea = find_element(driver, ele[0], ele[1], ele[2])
        return ele_tea

    def click_stu_tab(self, driver):
        """切换到 班级学生 tab"""
        ele = online.roster_stu_tab
        ele_stu = find_element(driver, ele[0], ele[1], ele[2])[0]
        ele_stu.click()
    def get_stu_table(self, driver):
        """获取 班级学生 表格"""
        ele = online.roster_stu_table
        ele_talbe = find_element(driver, ele[0], ele[1], ele[2])[0]
        return ele_talbe

    def click_stu_table_title(self, driver):
        """点击 学生 表格 头"""
        eles = [online.roster_table_name, online.roster_table_on, online.roster_table_empower, online.roster_table_silence,
               online.roster_table_mike, online.roster_table_camera, online.roster_table_award, online.roster_table_handup,
               online.roster_table_out, online.roster_table_device]
        for i in range(10):
            ele = random.choice(eles)
            ele_func = find_element(driver, ele[0], ele[1], ele[2])
            ActionChains(driver).move_to_element(ele_func).click().click().perform()
            time.sleep(1)

    def click_stu_table_item(self, driver):
        ele = online.roster_stu_table_item
        ele_childs = find_element(driver, ele[0], ele[1], ele[2])
        ele_childs_len = len(ele_childs)
        num = ele_childs_len//10
        for j in range(20):
            for i in range(1, num):
                ele_childs[random.randint(10*i+1, 10*i+8)].click()
                time.sleep(1)

    def click_tea_tab(self, driver):
        """切换到 联席教师 tab"""
        ele = online.roster_tea_tab
        ele_tea = find_element(driver, ele[0], ele[1], ele[2])[1]
        ele_tea.click()
    def get_tea_table(self, driver):
        """获取 联席教师 表格"""
        ele = online.roster_tea_table
        ele_talbe = find_element(driver, ele[0], ele[1], ele[2])[1]
        return ele_talbe

    def click_tea_table_title(self, driver):
        """点击 老师 表格 头"""
        eles = [online.roster_table_teacher, online.roster_table_on,
               online.roster_table_mike, online.roster_table_camera, online.roster_table_device]
        for i in range(10):
            ele = random.choice(eles)
            ele_func = find_element(driver, ele[0], ele[1], ele[2])
            ActionChains(driver).move_to_element(ele_func).click().click().perform()
            time.sleep(1)


    def click_camera_reset(self, driver):
        """点击 摄像头 复位"""
        ele = online.roster_tea_camera_reset
        ele_reset = self.get_roster_tea_operate(driver).find_elements_by_class_name(ele[2])[0]
        ele_reset.click()

    def click_mute(self, driver):
        """点击 全体静音/取消静音"""
        ele = online.roster_tea_mute
        ele_mute = self.get_roster_tea_operate(driver).find_elements_by_class_name(ele[2])[1]
        ele_mute.click()

    def click_stu_off(self, driver):
        """点击 全体下台"""
        ele = online.roster_tea_stu_off
        ele_off = self.get_roster_tea_operate(driver).find_elements_by_class_name(ele[2])[2]
        ele_off.click()

    def click_stu_empower(self, driver):
        """点击 全体授权"""
        ele = online.roster_tea_stu_empower
        # ele_empower = self.get_roster_tea_operate(driver).find_elements_by_class_name(ele[2])[3]
        ele_empower = self.get_roster_tea_operate(driver).find_elements_by_class_name(ele[2])[2] # lms没有全体授权
        ele_empower.click()

    def close_roster_win(self, driver):
        """关闭花名册"""
        ele = online.roster_win_close
        ele_roster_icon = find_element(driver, ele[0], ele[1], ele[2])
        ele_roster_icon.click()

    def click_lunbo_open(self, driver):
        """花名册 轮播 点击 开启"""
        ele = online.roster_tea_lunbo_open
        ele_open = find_element(driver, ele[0], ele[1], ele[2])
        ele_open.click()

    def choose_who_lunbo(self, driver):
        """花名册 选择 轮播 受众人群"""
        ele = online.roster_lunbo_who
        ele_box = find_element(driver, ele[0], ele[1], ele[2])[0]
        ele_box.click()
        whos = [online.roster_lunbo_all, online.roster_lunbo_part]
        who = random.choice(whos)
        ele_who = find_element(driver, who[0], who[1], who[2])
        ActionChains(driver).move_to_element_with_offset(ele_who, 10, 10).click().perform()


    def choose_order_lunbo(self, driver):
        """花名册 选择 轮播 顺序"""
        ele = online.roster_lunbo_order
        ele_box = find_element(driver, ele[0], ele[1], ele[2])[1]
        ele_box.click()
        orders = [online.roster_lunbo_suiji, online.roster_lunbo_shunxu]
        order = random.choice(orders)
        ele_order = find_element(driver, order[0], order[1], order[2])
        ActionChains(driver).move_to_element_with_offset(ele_order, 10, 10).click().perform()


# 工具箱
    def click_toolbox_icon(self, driver):
        """ 点击工具箱， 打开工具箱，显示工具列表"""
        ele = online.toolbox_icon
        # ele_toolbox_icon = self.get_toolset(driver).find_elements_by_class_name(ele[2])[9]  # classin
        ele_toolbox_icon = self.get_toolset(driver).find_elements_by_class_name(ele[2])[8]  # LMS
        ele_toolbox_icon.click()
        return ele_toolbox_icon

    def get_toolbox_location(self, driver):
        """获取 工具箱 弹层 展示区域"""
        ele = online.toolboxLocation
        ele_location =find_element(driver, ele[0], ele[1], ele[2])
        return ele_location

    def click_more_btn(self, driver):
        """点击 下拉button 显示全部列表内容/收回全部列表"""
        ele = online.more_icon
        ele_more = self.get_toolbox_location(driver).find_elements_by_class_name(ele[2])[0]
        time.sleep(1)
        ele_more.click()

    def click_toolbox_close_win(self, driver):
        """关闭 工具箱 窗口"""
        ele =  online.toolbox_win_close
        ele_more = self.get_toolbox_location(driver).find_elements_by_class_name(ele[2])[1]
        time.sleep(1)
        ele_more.click()

    def scroll_toolbox_down(self, driver):
        """ 工具栏中, 滚动条滚动到最下方(需要先用click_more_btn展开更多)"""
        self.get_toolbox_location(driver).click()
        time.sleep(2)
        ActionChains(driver).key_down(Keys.PAGE_DOWN).perform()
        time.sleep(2)


    def click_openfile(self, driver):
        """ 点击--工具箱列表的 打开文件 """
        ele = online.openFile_icon
        ele_file = find_element(driver, ele[0], ele[1], ele[2])
        ele_file.click()

    def click_save_or_share(self, driver):
        """ 点击--工具箱列表的 保存/分析板书"""
        ele = online.saveEdb_icon
        ele_save = find_element(driver, ele[0], ele[1], ele[2])
        ele_save.click()

    def get_save_win(self, driver):
        """获取 保存和分享板书窗口"""
        ele = online.save_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        ele_win.click()
        return ele_win

    def click_save_to_local(self, driver):
        """ 点击 保存至本地 """
        ele = online.save_to_local
        ele_save = self.get_save_win(driver).find_elements_by_class_name(ele[2])[0]
        time.sleep(1)
        ele_save.click()

    def click_save_to_yunpan(self, driver):
        """ 点击 保存至云盘 """
        ele = online.save_to_yunpan
        ele_save = self.get_save_win(driver).find_elements_by_class_name(ele[2])[1]
        time.sleep(1)
        ele_save.click()


    def use_file_rename(self, driver):
        ele = online.save_file_name
        ele_name = self.get_save_win(driver).find_element_by_class_name(ele[2])
        ele_name.click()
        ele_name.clear()

    def get_save_as_win(self, driver):
        """获取  另存信息  窗口"""
        ele =  online.save_to_check
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def click_save_as_url(self, driver):
        """点击文件夹icon"""
        ele = online.save_to_local_url
        ele_folder = self.get_save_as_win(driver).find_elements_by_class_name(ele[2])[-1]
        ele_folder.click()


# 骰子
    def click_shaizi(self, driver):
        """ 点击--工具箱列表的 骰子"""
        ele = online.shaizi_icon
        ele_shaizi = find_element(driver, ele[0], ele[1], ele[2])
        ele_shaizi.click()

    def use_shaiziH5(self, driver):
        """骰子container是个H5"""
        ele = online.shaizi_H5
        ele_shaizi_h5 =  find_element(driver, ele[0], ele[1], ele[2])[0]
        for i in range(5):
            time.sleep(3)
            ele_shaizi_h5.click()

    def use_shaiziH5_smoke(self, driver):
        """骰子container是个H5"""
        ele = online.shaizi_H5
        ele_shaizi_h5 =  find_element(driver, ele[0], ele[1], ele[2])[0]
        time.sleep(3)
        ele_shaizi_h5.click()

    def click_shaizi_win_close(self, driver):
        """关闭骰子"""
        ele = online.shaizi_win_total
        ele_win_total = find_element(driver, ele[0], ele[1], ele[2])
        ele_close_btn = online.shaizi_win_close
        ele_win_close_btn = ele_win_total.find_element_by_class_name(ele_close_btn[2])
        ele_win_close_btn.click()

# 答题器
    def click_datiqi(self, driver):
        """ 点击--工具箱列表的 答题器"""
        ele = online.datiqi_icon
        ele_datiqi = find_element(driver, ele[0], ele[1], ele[2])
        ele_datiqi.click()

    def get_datiqi_win(self, driver):
        """获取 答题器 窗口整体"""
        ele = online.datiqi_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def choose_answer(self, driver):
        """设置 正确答案"""
        ele = online.datiqi_item
        for i in range(3):
            j =  random.randint(2, 5)
            ele_item = find_element(driver, ele[0], ele[1], ele[2])[j]
            ele_item.click()

    def choose_answer_first(self, driver):
        """设置 正确答案--选择设置第一项--smoke用例"""
        ele = online.datiqi_item
        ele_item = find_element(driver, ele[0], ele[1], ele[2])[2]
        ele_item.click()

    def click_begin(self, driver):
        """点击 开始答题"""
        ele = online.datiqi_begin_btn
        ele_begin = find_element(driver, ele[0], ele[1], ele[2])
        ele_begin.click()
        time.sleep(10)

    def edit_answer(self, driver):
        """修改答案"""
        ele = online.datiqi_item
        for i in range(3):
            j =  random.randint(0, 3)
            ele_item = find_element(driver, ele[0], ele[1], ele[2])[j]
            ele_item.click()

    def click_edit(self, driver):
        """点击 btn 修改答案"""
        ele = online.datiqi_edit_btn
        ele_begin = find_element(driver, ele[0], ele[1], ele[2])
        ele_begin.click()
        self.edit_answer(driver)

    def edit_answer_smoke(self, driver):
        """修改答案--选择固定设置项--smoke用例"""
        ele = online.datiqi_item
        ele_item = find_element(driver, ele[0], ele[1], ele[2])[3]
        ele_item.click()

    def click_edit_smoke(self, driver):
        """点击 btn 修改答案"""
        ele = online.datiqi_edit_btn
        ele_begin = find_element(driver, ele[0], ele[1], ele[2])
        ele_begin.click()
        self.edit_answer_smoke(driver)

    def click_end(self, driver):
        """点击 结束答题"""
        ele = online.datiqi_end_btn
        ele_end = find_element(driver, ele[0], ele[1], ele[2])
        ele_end.click()

    def click_datiqi_win_close(self, driver):
        """关闭答题器窗口"""
        ele = online.daqiti_win2_title
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        ele_close = online.datiqi_win_close
        ele_close_btn = ele_win.find_element_by_class_name(ele_close[2])
        ele_close_btn.click()

# 计时器
    def click_jishiqi(self, driver):
        """ 点击--工具箱列表的 计时器"""
        ele = online.jishiqi_icon
        ele_jishiqi = find_element(driver, ele[0], ele[1], ele[2])
        ele_jishiqi.click()

    def get_jishiqi_win(self, driver):
        """ 获取 计时器 窗口"""
        ele = online.jishiqi_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def click_begin_jishiqi(self, driver):
        """计时器，点击 开始"""
        ele = online.jishiqi_begin_btn
        ele_begin = find_element(driver, ele[0], ele[1], ele[2])
        ele_begin.click()

    def click_stop_jishiqi(self, driver):
        e = online.jishiqi_FloatButtons
        e_total = find_element(driver, e[0], e[1], e[2])
        e_total.click()

    def click_reset_jishiqi(self, driver):
        ele = online.jishiqi_reset_btn
        ele_reset = find_element(driver, ele[0], ele[1], ele[2])
        ele_reset.click()

    def click_continue_jishiqi(self, driver):
        ele = online.jishiqi_continue_btn
        ele_continue = find_element(driver, ele[0], ele[1], ele[2])
        ele_continue.click()

    def click_jishiqi_win_close(self, driver):
        ele = online.jishiqi_win_close
        ele_close = self.get_jishiqi_win(driver).find_element_by_class_name(ele[2])
        ele_close.click()

# 定时器
    def click_dingshiqi(self, driver):
        """ 点击--工具箱列表的 定时器"""
        ele = online.dingshiqi_icon
        ele_dingshiqi = find_element(driver, ele[0], ele[1], ele[2])
        ele_dingshiqi.click()

    def get_dingshiqi_win(self, driver):
        ele = online.dingshiqi_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def click_dingshiqi_edit(self, driver):
        """ 编辑 定时时长"""
        ele = online.dingshiqi_edit_btn
        for n in range(3):
            i = random.randint(1, 8)
            ele_edit = self.get_dingshiqi_win(driver).find_elements_by_class_name(ele[2])[i]
            ele_edit.click()

    def click_dingshiqi_edit_smoke(self, driver):
        """ 编辑 定时时长"""
        ele = online.dingshiqi_edit_btn
        ele_edit = self.get_dingshiqi_win(driver).find_elements_by_class_name(ele[2])[1]
        ele_edit.click()

    def click_dingshiqi_begin(self, driver):
        """点击 开始"""
        ele = online.dingshiqi_begin_btn
        ele_begin = find_element(driver, ele[0], ele[1], ele[2])
        ele_begin.click()
        time.sleep(10)

    def click_dingshiqi_win_close(self, driver):
        """关闭 定时器 窗口"""
        ele = online.dingshiqi_win_close
        ele_close = self.get_dingshiqi_win(driver).find_elements_by_class_name(ele[2])[0]
        ele_close.click()

# 共享工具
    def click_share_icon(self, driver):
        """ 点击--工具箱列表的 共享工具"""
        ele = online.shareTool_icon
        ele_share = find_element(driver, ele[0], ele[1], ele[2])
        ele_share.click()
# 桌面共享
    def click_share_desktop(self, driver):
        """点击--桌面共享"""
        ele = online.share_desktop
        ele_desktop = find_element(driver, ele[0], ele[1], ele[2])[0]
        ele_desktop.click()
        time.sleep(2)

    def click_share(self, driver):
        ele = online.share_btn
        ele_share = find_element(driver, ele[0], ele[1], ele[2])
        ele_share.click()

    def click_stu_share(self, driver):
        ele = online.share_student_send_btn
        ele_share = find_element(driver, ele[0], ele[1], ele[2])
        ele_share.click()

    def click_end_share(self, driver):
        ele = online.end_share_btn
        ele_end = find_element(driver, ele[0], ele[1], ele[2])
        ele_end.click()

    def click_share_sound(self, driver):
        """桌面共享--点击 共享声音"""
        ele = online.share_desktop_sound
        ele_sound = find_element(driver, ele[0], ele[1], ele[2])
        ele_sound.click()
        time.sleep(2)

    def click_share_start(self, driver):
        """桌面共享--点击 开始共享"""
        ele = online.share_desktop_start
        ele_start = find_element(driver, ele[0], ele[1], ele[2])
        ele_start.click()
        time.sleep(5)

    def click_share_desktop_close(self, driver):
        """桌面共享--点击 关闭窗口"""
        ele = online.share_desktop_close
        ele_close =  find_element(driver, ele[0], ele[1], ele[2])[-1]
        ele_close.click()
        time.sleep(5)

# 教师屏幕共享
    def click_share_teacher(self, driver):
        """点击 教师屏幕共享 """
        ele = online.share_teacher
        ele_teacher = find_element(driver, ele[0], ele[1], ele[2])[1]
        ele_teacher.click()
        time.sleep(5)

    def click_share_teacher_close(self, driver):
        """桌面共享--点击 关闭窗口"""
        ele = online.share_teacher_close
        ele_close =  find_element(driver, ele[0], ele[1], ele[2])[8]
        ele_close.click()
        time.sleep(5)


# 全体学生共享--逻辑：同一个教室内，第一次学生需要同意，后面不需要同意（暂不写）
    def click_share_student(self, driver):
        ele = online.share_student
        ele_student = find_element(driver, ele[0], ele[1], ele[2])[2]
        ele_student.click()


# 小黑板
    def click_xiaoheiban_icon(self, driver):
        """点击--工具箱列表的 小黑板"""
        ele = online.xiaoheiban_icon
        ele_icon = find_element(driver, ele[0], ele[1], ele[2])
        ele_icon.click()

    def click_xiaoneiban_paint(self, driver):
        """打开 小黑板 画板"""
        ele = online.xiaoheiban_paint
        ele_paint = find_element(driver, ele[0], ele[1], ele[2])[0]
        ele_paint.click()

    def use_paint_pen(self, driver):
        """小黑板 画板 使用画笔工具"""
        tools = online.xiaoheiban_paint_PainterController
        ele_tools = find_element(driver, tools[0], tools[1], tools[2])
        pen = online.xiaoheiban_paint_pen
        ele_pen = ele_tools.find_elements_by_class_name(pen[2])[1]
        ele_pen.click()
        painter = online.xiaoheiban_painter
        ele_painter = find_element(driver, painter[0], painter[1], painter[2])
        ActionChains(driver).drag_and_drop_by_offset(ele_painter, random.randint(-500, 500), random.randint(-220, 200)).perform()

    def use_paint_pen_smoke(self, driver):
        """小黑板 画板 使用画笔工具--smoke"""
        tools = online.xiaoheiban_paint_PainterController
        ele_tools = find_element(driver, tools[0], tools[1], tools[2])
        pen = online.xiaoheiban_paint_pen
        ele_pen = ele_tools.find_elements_by_class_name(pen[2])[1]
        ele_pen.click()
        painter = online.xiaoheiban_painter
        ele_painter = find_element(driver, painter[0], painter[1], painter[2])
        ActionChains(driver).drag_and_drop_by_offset(ele_painter, -100,  200).perform()

    def use_paint_text(self, driver):
        """小黑板 画板 使用工具文本"""
        tools = online.xiaoheiban_paint_PainterController
        ele_tools = find_element(driver, tools[0], tools[1], tools[2])
        text = online.xiaoheiban_paint_text
        ele_text = ele_tools.find_elements_by_class_name(text[2])[3]
        ele_text.click()
        painter = online.xiaoheiban_painter
        ele_painter = find_element(driver, painter[0], painter[1], painter[2])
        ActionChains(driver).move_to_element(ele_painter).click().perform()

    def click_paint_share(self, driver):
        """小黑板 画板 分发"""
        ele = online.xiaoheiban_share
        ele_share = find_element(driver, ele[0], ele[1], ele[2])
        ele_share.click()

    def click_paint_back(self, driver):
        """小黑板 画板 回收"""
        ele = online.xiaoheiban_back
        ele_back = find_element(driver, ele[0], ele[1], ele[2])
        ele_back.click()

    def click_panit_close(self, driver):
        """小黑板 画板 关闭窗口"""
        win = online.xiaoheiban_paint_prepare
        ele_win = find_element(driver, win[0], win[1], win[2])
        close = online.xiaoheiban_prepare_close
        ele_close = ele_win.find_element_by_class_name(close[2])
        ele_close.click()


    def click_xiaoneiban_text(self, driver):
        """打开 小黑板 文本"""
        ele = online.xiaoheiban_text
        ele_text = find_element(driver, ele[0], ele[1], ele[2])[1]
        ele_text.click()

    def use_text_edit(self, driver):
        """小黑板 文本 编辑"""
        ele = online.xiaoheiban_texter
        ele_edit = find_element(driver, ele[0], ele[1], ele[2])
        ele_edit.click()

# 分组讨论
    def click_group_icon(self, driver):
        """点击--工具箱列表的 分组讨论"""
        ele = online.group_icon
        ele_group = find_element(driver, ele[0], ele[1], ele[2])
        ele_group.click()

    def click_start_group(self, driver):
        """ 点击[开始分组] """
        ele = online.start_group_btn
        ele_start = find_element(driver, ele[0], ele[1], ele[2])
        ele_start.click()

    def click_begin_discuss(self, driver):
        """ 点击[开始讨论] """
        ele = online.begin_discuss_btn
        ele_begin =  find_element(driver, ele[0], ele[1], ele[2])
        ele_begin.click()

    def click_end_discuss(self, driver):
        """ 点击[结束讨论] """
        ele = online.end_discuss_btn
        ele_end =  find_element(driver, ele[0], ele[1], ele[2])
        ele_end.click()

    def click_re_group(self, driver):
        """ 点击[重新分组] """
        ele = online.re_group_btn
        ele_re = find_element(driver, ele[0], ele[1], ele[2])
        ele_re.click()

    def click_re_discuss(self, driver):
        """ 点击[再次讨论] """
        ele = online.re_discuss_btn
        ele_re = find_element(driver, ele[0], ele[1], ele[2])
        ele_re.click()

    def get_group_win(self, driver):
        """ 获取 讨论窗口 """
        ele = online.group_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def click_group_win_close(self, driver):
        """ 关闭 讨论窗口 """
        ele = online.group_win_close
        ele_close =  self.get_group_win(driver).find_elements_by_class_name(ele[2])[0]
        ele_close.click()


# 浏览器
    def click_browser_icon(self, driver):
        """点击--工具箱列表的 浏览器"""
        self.scroll_toolbox_down(driver)
        ele = online.browser_icon
        ele_icon = find_element(driver, ele[0], ele[1], ele[2])
        ele_icon.click()
    def click_browser_url(self, driver):
        """点击 输入网址 输入框, 输入框获取焦点"""
        ele = online.browser_url_edit
        ele_edit = find_element(driver, ele[0], ele[1], ele[2])
        ele_edit.click()
    def use_key_enter(self, driver):
        """ 使用键盘的  回车"""
        ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    def get_browser_win(self, driver):
        """ 获取 浏览器 窗口"""
        ele = online.browser_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win
    def click_browser_win_close(self, driver):
        """ 关闭 浏览器 窗口"""
        ele = online.browser_win_close
        ele_close = self.get_browser_win(driver).find_elements_by_class_name(ele[2])[2]  #find_element(driver, ele[0], ele[1], ele[2])[2]
        ele_close.click()


# 视频墙
    def click_video_icon(self, driver):
        """点击--工具箱列表的 视频墙"""
        self.scroll_toolbox_down(driver)
        ele = online.video_icon
        ele_video = find_element(driver, ele[0], ele[1], ele[2])
        ele_video.click()

    def click_switch(self, driver):
        """ 视频墙 窗口上 点击 转换窗口"""
        ele = online.wall_switch_screen
        ele_switch = find_element(driver, ele[0], ele[1], ele[2])[0]
        ele_switch.click()

    def click_save(self, driver):
        """视频墙 窗口上 点击 合影"""
        ele = online.wall_save
        ele_save = find_element(driver, ele[0], ele[1], ele[2])[1]
        ele_save.click()

    def click_phone_for_one_screen(self, driver):
        """视频墙 窗口上 点击 合影"""
        ele = online.wall_save
        ele_save = find_element(driver, ele[0], ele[1], ele[2])
        time.sleep(1)
        ele_save[0].click()

    def click_save_yunpan(self, driver):
        """保存窗口上,点击 保存到云盘"""
        ele = online.save_yunpan
        ele_yunpan = find_element(driver, ele[0], ele[1], ele[2])
        ele_yunpan.click()

    def get_wall_save_win(self, driver):
        """ 获取 保存 窗口"""
        ele = online.wall_save_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])[1]
        return ele_win

    def close_save_win(self, driver):
        """关闭 保存 窗口"""
        self.get_wall_save_win(driver).click()
        ele = online.save_win_close
        ele_close = self.get_wall_save_win(driver).find_elements_by_class_name(ele[2])[4]
        ele_close.click()

    def click_wall_setting(self, driver):
        """点击 视频墙窗口上的 设置"""
        ele = online.wall_setting
        ele_set = find_element(driver, ele[0], ele[1], ele[2])[2]
        ele_set.click()

    def click_wall_setting_for_one_screen(self, driver):
        """点击 视频墙窗口上的 设置"""
        ele = online.wall_setting
        ele_set = find_element(driver, ele[0], ele[1], ele[2])[1]
        ele_set.click()

    def click_wall_win_close(self, driver):
        """关闭 视频墙 窗口"""
        ele = online.wall_win_close
        ele_close = find_element(driver, ele[0], ele[1], ele[2])[5]
        ele_close.click()

    def click_wall_win_close_for_one_screen(self, driver):
        """关闭 视频墙 窗口"""
        ele = online.wall_win_close
        ele_close = find_element(driver, ele[0], ele[1], ele[2])[4]
        ele_close.click()

# 教学材料库
    def click_material_icon(self, driver):
        """点击--工具箱列表的 教学材料库"""
        ele = online.material_icon
        ele_material = find_element(driver, ele[0], ele[1], ele[2])
        ele_material.click()

    def get_material_win(self, driver):
        """ 获取 材料 窗口"""
        ele = online.material_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def click_choose_subject(self, driver):
        ele = online.material_subject
        n = len(find_element(driver, ele[0], ele[1], ele[2]))
        m = random.randint(0, n-1)
        ele_sub = find_element(driver, ele[0], ele[1], ele[2])[m]
        ele_sub.click()
        time.sleep(2)

    def click_material_item(self, driver):
        ele = online.material_item
        # n = len(find_element(driver, ele[0], ele[1], ele[2]))
        # m = random.randint(0, n - 1)
        # ele_item = find_element(driver, ele[0], ele[1], ele[2])[m]
        ele_item = find_element(driver, ele[0], ele[1], ele[2])[0]
        ele_item.click()
        time.sleep(2)

    def click_material_item_smoke(self, driver):
        ele = online.material_item
        ele_item = find_element(driver, ele[0], ele[1], ele[2])[0]
        ele_item.click()
        time.sleep(2)

    def click_material_win_close(self, driver):
        ele = online.material_win_close
        ele_close = self.get_material_win(driver).find_elements_by_class_name(ele[2])[1]
        ele_close.click()


# 尺规工具
    def click_ruler_icon(self, driver):
        """点击--工具箱列表的 尺规工具"""
        self.scroll_toolbox_down(driver)
        ele = online.ruler_icon
        ele_ruler = find_element(driver, ele[0], ele[1], ele[2])
        ele_ruler.click()

    def get_ruler_win(self, driver):
        ele = online.ruler_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def click_ruler_item(self, driver):
        """ 点击  尺规项"""
        ele = online.ruler_item
        ele_items = self.get_ruler_win(driver).find_elements_by_class_name(ele[2])
        n = len(ele_items)
        ele_item = ele_items[random.randint(0, n-1)]
        ele_item.click()
        time.sleep(2)

    def click_ruler_item_smoke(self, driver):
        """ 点击  尺规项"""
        ele = online.ruler_item
        ele_items = self.get_ruler_win(driver).find_elements_by_class_name(ele[2])
        ele_item = ele_items[0]
        ele_item.click()
        time.sleep(2)

    def click_ruler_win_close(self, driver):
        ele = online.ruler_win_close
        ele_close = self.get_ruler_win(driver).find_element_by_class_name(ele[2])
        ele_close.click()
        time.sleep(2)

# 几何图形工具
    def click_geometry_icon(self, driver):
        """点击--工具箱列表的 几何图形工具"""
        self.scroll_toolbox_down(driver)
        ele = online.geometry_icon
        ele_geometry = find_element(driver, ele[0], ele[1], ele[2])
        ele_geometry.click()

    def get_geometry_win(self, driver):
        ele = online.geometry_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def click_geometry_item(self, driver):
        """ 点击  几何图形项"""
        ele = online.geometry_item
        ele_items = self.get_geometry_win(driver).find_elements_by_class_name(ele[2])
        n = len(ele_items)  # 18
        ele_item = ele_items[random.randint(1, n-1)]
        ele_item.click()
        time.sleep(2)

    def click_geometry_item_smoke(self, driver):
        """ 点击  几何图形项"""
        ele = online.geometry_item
        ele_items = self.get_geometry_win(driver).find_elements_by_class_name(ele[2])
        ele_item = ele_items[0]
        ele_item.click()
        time.sleep(2)

    def click_geometry_win_close(self, driver):
        ele = online.geometry_win_close
        ele_close = self.get_geometry_win(driver).find_element_by_class_name(ele[2])
        ele_close.click()
        time.sleep(2)


# 投屏工具-------hk
    def click_touping(self, driver):
        """ 点击--工具箱列表的 投屏工具"""
        ele = online.touping_icon
        ele_touping = find_element(driver, ele[0], ele[1], ele[2])
        ele_touping.click()

    def get_touping_win(self, driver):
        ele = online.touping_select_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def get_touping_classsin_win(self, driver):
        ele = online.touping_classin_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def get_touping_apple_win(self, driver):
        ele = online.touping_apple_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def click_classIn_touping(self, driver):
        """点击classIn投屏"""
        ele = online.touping_classIn_btn
        ele_close = self.get_touping_win(driver).find_elements_by_class_name(ele[2])[0]
        ele_close.click()

    def click_apple_touping(self, driver):
        """点击苹果投屏"""
        ele = online.touping_apple_btn
        ele_close = self.get_touping_win(driver).find_elements_by_class_name(ele[2])[1]
        ele_close.click()

    def click_sound_local_btn(self, driver):
        """点击本地播放声音"""
        ele = online.sound_local_btn
        sound_local = find_element(driver, ele[0], ele[1], ele[2])
        sound_local.click()

    def click_sound_share_btn(self, driver):
        """点击共享声音"""
        ele = online.sound_share_btn
        sound_share = find_element(driver, ele[0], ele[1], ele[2])
        sound_share.click()

    def click_classin_win_close(self, driver):
        """关闭classin 投屏 窗口"""
        ele = online.touping_win_close
        ele_close = self.get_touping_classsin_win(driver).find_elements_by_class_name(ele[2])[2]
        ele_close.click()

    def click_apple_win_close(self, driver):
        """关闭apple 投屏 窗口"""
        ele = online.touping_win_close
        ele_close = self.get_touping_apple_win(driver).find_elements_by_class_name(ele[2])[2]
        ele_close.click()

# 随机选人
    def click_xuanren(self, driver):
        """ 点击--工具箱列表的 随机选人"""
        ele = online.xuanren_icon
        ele_xuanren = find_element(driver, ele[0], ele[1], ele[2])
        ele_xuanren.click()

    def get_xuanren_win(self, driver):
        ele = online.xuanren_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def choose_stu(self, driver):
        """选择学生下拉框"""
        ele_choose = online.choose_stu_btn
        choose = find_element(driver, ele_choose[0], ele_choose[1], ele_choose[2])
        choose.click()

    def click_all_stu(self, driver):
        """选择 全部学生"""
        ele = online.all_stu_btn
        all_stu = find_element(driver, ele[0], ele[1], ele[2])
        all_stu.click()

    def click_online_stu(self, driver):
        """选择 在线学生"""
        ele = online.online_stu_btn
        online_stu = find_element(driver, ele[0], ele[1], ele[2])
        online_stu.click()

    def click_start_xuanren(self, driver):
        """点击开始选人按钮"""
        ele = online.xuanren_start_btn
        ele_start_xuanren = find_element(driver, ele[0], ele[1], ele[2])
        ele_start_xuanren.click()

    def click_xuanren_win_close(self, driver):
        """关闭 随机选人 窗口"""
        ele = online.xuanren_win_close
        ele_close = self.get_xuanren_win(driver).find_element_by_class_name(ele[2])
        ele_close.click()

# 协作
    def click_xiezuo(self, driver):
        """ 点击--工具箱列表的 协作"""
        ele = online.xiezuo_icon
        ele_xiezuo = find_element(driver, ele[0], ele[1], ele[2])
        ele_xiezuo.click()

    def get_xiezuo_win(self, driver):
        ele = online.xiezuo_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def get_wenben_win(self, driver):
        ele = online.wenben_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def get_wendang_win(self, driver):
        ele = online.wendang_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def click_wenben(self, driver):
        ele = online.wenben_btn
        ele_wenben = self.get_xiezuo_win(driver).find_elements_by_class_name(ele[2])[0]
        ele_wenben.click()

    def click_wendang(self, driver):
        ele = online.wenben_btn
        ele_wenben = self.get_xiezuo_win(driver).find_elements_by_class_name(ele[2])[1]
        ele_wenben.click()

    def input_wenben(self, driver):
        """输入文本内容"""
        ele = online.wenben_context_btn
        ele_wenben = find_element(driver, ele[0], ele[1], ele[2])
        ele_wenben.send_keys("文本内容")

    def wenben_save_local(self, driver):
        """保存至本地"""
        ele_save = online.save_btn
        save = find_element(driver, ele_save[0], ele_save[1], ele_save[2])
        save.click()
        ele_save_local = online.save_local_btn
        save_local = find_element(driver, ele_save_local[0], ele_save_local[1], ele_save_local[2])
        save_local.click()
        ele_confirm = online.confirm_btn
        confirm = find_element(driver, ele_confirm[0], ele_confirm[1], ele_confirm[2])
        confirm.click()

    def input_wendang(self, driver):
        """输入文档内容"""
        ele = online.wendang_context_btn
        ele_wendang = find_element(driver, ele[0], ele[1], ele[2])
        ele_wendang.send_keys("文档内容")

    def click_wenben_win_close(self, driver):
        """关闭 文本 窗口"""
        ele = online.xuanren_win_close
        ele_close = self.get_wenben_win(driver).find_elements_by_class_name(ele[2])[-1]
        ele_close.click()

    def click_wendang_win_close(self, driver):
        """关闭 文本 窗口"""
        ele = online.xuanren_win_close
        ele_close = self.get_wendang_win(driver).find_elements_by_class_name(ele[2])[-1]
        ele_close.click()

# 奖励排行榜
    def click_reward_rank(self, driver):
        """ 点击--工具箱列表的 奖励排行榜"""
        ele = online.reward_rank_icon
        ele_rank = find_element(driver, ele[0], ele[1], ele[2])
        ele_rank.click()

    def get_rank_win(self, driver):
        ele = online.rank_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def click_rank_win_close(self, driver):
        ele = online.rank_win_close
        ele_close = self.get_rank_win(driver).find_element_by_class_name(ele[2])
        ele_close.click()

# 辅助摄像头
    def click_assist_camera(self, driver):
        """ 点击--工具箱列表的 辅助摄像头"""
        ele = online.assist_camera_icon
        ele_rank = find_element(driver, ele[0], ele[1], ele[2])
        ele_rank.click()

    def get_camera_win(self, driver):
        ele = online.camera_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def click_camera_win_close(self, driver):
        ele = online.camera_win_close
        ele_close = self.get_camera_win(driver).find_elements_by_class_name(ele[2])[0]
        ele_close.click()

# 围棋小黑板
    def click_go(self, driver):
        """ 点击--工具箱列表的 围棋小黑板"""
        self.scroll_toolbox_down(driver)
        ele = online.go_icon
        ele_go = find_element(driver, ele[0], ele[1], ele[2])
        ele_go.click()

    def get_go_win(self, driver):
        ele = online.go_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def select_lushu(self, driver):
        ele = online.lushu_btn
        ele_lushu = self.get_go_win(driver).find_elements_by_class_name(ele[2])[3]
        ele_lushu.click()

    def select_color(self, driver):
        ele = online.color_select_btn
        ele_color = self.get_go_win(driver).find_elements_by_class_name(ele[2])[6]
        ele_color.click()

    def get_board_win(self, driver):
        ele = online.board_win
        ele_win = find_element(driver, ele[0], ele[1], ele[2])
        return ele_win

    def click_board(self, driver):
        ele = online.board_ele
        ele_board = self.get_board_win(driver).find_element_by_class_name(ele[2])
        ele_board.click()

    def click_send(self, driver):
        ele = online.push_btn
        ele_send = self.get_board_win(driver).find_elements_by_class_name(ele[2])[-1]
        ele_send.click()

    def click_board_win_close(self, driver):
        ele = online.tool_btn
        ele_close = self.get_board_win(driver).find_elements_by_class_name(ele[2])[0]
        ele_close.click()

# 头部bar
    def get_titlebar(self, driver):
        """ 获取 在线教室 头部bat"""
        ele = online.titleBar
        ele_titlebar = find_element(driver, ele[0], ele[1], ele[2])
        return ele_titlebar

    def get_titlebar_left(self, driver):
        """ 获取 在线教室 头部bat  左侧部分"""
        ele = online.leftBar
        ele_left = self.get_titlebar(driver).find_element_by_class_name(ele[2])
        return ele_left

    def get_fps_ele(self, driver):
        ele = online.fps_value
        ele_fps = find_element(driver, ele[0], ele[1], ele[2])[3]
        return ele_fps

    def get_fps(self, driver):
        """ 获取 fps 内容"""
        ele = self.get_fps_ele(driver)
        text = ele.get_attribute('Name')
        print(text)
        return text


# 抢答器
    def click_responder_icon(self, driver):
        ele = online.Responder_icon
        ele_icon =  find_element(driver, ele[0], ele[1], ele[2])
        ele_icon.click()

    def click_response_start(self, driver):
        ele =  online.Responder_start
        ele_start = find_element(driver, ele[0], ele[1], ele[2])
        ele_start.click()

    def click_response_restart(self, driver):
        ele =  online.Responder_btnagain
        ele_restart = find_element(driver, ele[0], ele[1], ele[2])
        ele_restart.click()

    def click_response_close(self, driver):
        ele =  online.Responder_btnclose
        ele_close = find_element(driver, ele[0], ele[1], ele[2])
        ele_close.click()




###########学生端操作
class StuOnlineClassRoomPage(object):
    """工具--举手上台"""
    def click_handup_icon(self, driver):
        """点击举手上台icon"""
        ele = online.StuHandUp
        ele_handup = find_element(driver, ele[0], ele[1], ele[2])
        ele_handup.click()
