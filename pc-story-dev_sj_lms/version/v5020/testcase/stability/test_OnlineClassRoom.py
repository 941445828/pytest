# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 智慧教室
"""


from version.v5020.pageobject.onlineClassRoom_page import OnlineClassRoomPage, StuOnlineClassRoomPage
from config import *
from config import stability_conf
from version.v5020.pageobject.onlineOpenFile_page import OnlineOpenFilePage, OnlineCloseFilePage
from version.v5020.pageobject.common_page import ChooseFolder, ChooseFile, ClassAppraise, PromptChoose
from handler.yamlHandler import get_data
import random
from handler.logHandler import logger
from handler.yamlHandler import YamlMethod
from handler.getWinHandler import get_win
from config import utils
from version.v5020 import *
import allure


class TestOnlineCamera(object):
    """摄像头"""
    def test_camera(self, get_driver):
        """拖拽摄像头"""
        OnlineClassRoomPage().move_camera(get_driver)

class TestCameraSmoke:
    """ 摄像头-冒烟用例"""
    def test_camera_smoke(self, get_driver):
        """ 移动摄像头到固定位置"""
        OnlineClassRoomPage().move_camera_to_regular(get_driver)


class TestCameraReset:
    def test_camera_reset(self, get_driver):
        """花名册 摄像头 复位"""
        TestRoster().test_open_roster(get_driver)
        OnlineClassRoomPage().click_camera_reset(get_driver)
        TestRoster().test_close_roster(get_driver)


@allure.feature("教室")
@allure.story("测试--发奖励")
class TestTeacherRewardAllPerf:
    @allure.title('发奖励')
    @allure.description("给台上所有同学发奖励")
    def test_click_reward_all(self, get_driver, get_function_name):
        OnlineClassRoomPage().reward_all(get_driver)
        time.sleep(time_sleep[2] * 6)

@allure.feature("教室")
@allure.story("测试--摄像头设置虚拟背景")
class TestSettingCamera:
    @allure.title('虚拟背景')
    @allure.description("获取教室设置区域")
    def test_click_setting_area(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_setting_btn(get_driver)

    @allure.title('虚拟背景')
    @allure.description("点击‘设置’")
    def test_click_setting(self, get_driver, get_function_name):
        get_win(get_driver, 0)
        OnlineClassRoomPage().click_setting(get_driver)

    @allure.title('虚拟背景')
    @allure.description("点击‘虚拟背景’")
    def test_click_virtual_background(self, get_driver, get_function_name):
        get_win(get_driver, 0)
        OnlineClassRoomPage().click_virtual(get_driver)

    @allure.title('虚拟背景')
    @allure.description("选择‘背景虚化’")
    def test_choose_virtual_list_item(self, get_driver):
        OnlineClassRoomPage().click_background_virtual(get_driver)
        time.sleep(5)

    @allure.title('虚拟背景')
    @allure.description("关闭设置窗口")
    def test_close_setting_win(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_setting_win_close(get_driver)
        time.sleep(5)


class TestSleepAfterVirtual:
    def test_sleep(self):
        time.sleep(120)



# class TestOnlineYunPanOpenFile(object):
#     """云盘"""
#     def test_use_yunpan(self, get_driver):
#         """点击云盘"""
#         OnlineOpenFilePage().get_ClassroomPage(get_driver)
#         OnlineOpenFilePage().get_ToolbarWrapper(get_driver)
#         OnlineOpenFilePage().click_yunpan(get_driver)
#
#     def test_changeto_webdriver(self,get_web_driver):
#         get_new_page_special(get_web_driver,"cloud")
#
#     def test_use_wendang(self, get_web_driver):
#         """点击文档"""
#         OnlineOpenFilePage().click_wendang(get_web_driver)
#
#     def test_use_folder(self, get_web_driver):
#         """点击文件夹--课件"""
#         case = get_data('class.yaml')[0]
#         OnlineOpenFilePage().click_target_folder(get_web_driver, case['folder_name'])
#
#     def test_open_files(self, get_web_driver, get_driver):
#         """打开文件--随机打开一个课件"""
#         files = []
#         for i in range(stability_conf.online_loop):
#             files_list = stability_conf.files
#             file = random.choice(files_list)
#             file_kind = file.split('.')[1]
#             try:
#                 logger.info('next step: online classroom open files : {}'.format(file))
#                 OnlineOpenFilePage().click_file(get_web_driver, file)
#             except Exception as e:
#                 logger.error(e)
#             else:
#                 if file_kind == 'edb':
#                     OnlineOpenFilePage().click_clear_blackbord_yes(get_driver)
#                     time.sleep(1)
#                 if file_kind not in files:
#                     files.append(file_kind)
#                 continue
#             time.sleep(2)
#         logger.info("打开的课件是： {}".format(files))
#         # 将file_kind存入yaml
#         content = get_data('tmp.yaml')[0]
#         content['file_kind'] = files
#         YamlMethod(get_data('tmp.yaml')[1]).yaml_write(content)
#         return files

class TestOnlineYunPanOpenFileSmoke:
    """云盘-打开课件--smoke"""
    def test_use_yunpan(self, get_driver):
        """点击云盘"""
        OnlineOpenFilePage().get_ClassroomPage(get_driver)
        OnlineOpenFilePage().get_ToolbarWrapper(get_driver)
        OnlineOpenFilePage().click_yunpan(get_driver)

    def test_use_wendang(self, get_web_driver):
        """点击文档"""
        OnlineOpenFilePage().click_wendang(get_web_driver)

    def test_use_folder(self, get_web_driver):
        """点击文件夹--课件"""
        case = get_data('class.yaml')[0]
        OnlineOpenFilePage().click_folder(get_web_driver, case['folder_name'])

    def test_open_file_smoke(self, get_web_driver, get_driver):
        """打开文件--打开课件--smoke用例"""
        files = []
        file = stability_conf.files[0]
        file_kind = file.split('.')[1]
        try:
            logger.info('smoke case: online classroom open files : {}'.format(file))
            OnlineOpenFilePage().click_file(get_web_driver, file)
        except Exception as e:
            logger.error(e)
        else:
            if file_kind == 'edb':
                OnlineOpenFilePage().click_clear_blackbord_yes(get_driver)
                time.sleep(1)
            if file_kind not in files:
                files.append(file_kind)
        time.sleep(2)
        logger.info("打开的课件是： {}".format(files))
        # 将file_kind存入yaml
        content = get_data('tmp.yaml')[0]
        content['smoke_file_kind'] = files
        YamlMethod(get_data('tmp.yaml')[1]).yaml_write(content)
        return files

class TestOnlineYunPanCloseFile(object):
    def test_getmainlocation(self, get_driver):
        OnlineClassRoomPage().get_mainLotion(get_driver)

    def test_close_file(self, get_driver):
        files =  get_data('tmp.yaml')[0]['file_kind']
        logger.info("从以下文件中，选择要关闭的课件： {}".format(files))
        for i in range(len(files)):
            if 'pptx' in files[i]:
                OnlineCloseFilePage().close_pptx(get_driver)
                logger.info("pptx课件已关闭！")
            elif 'csv' in files[i] or 'xlsx' in files[i]:
                OnlineCloseFilePage().close_excel(get_driver)
                logger.info("csv、xlsx 课件已关闭！")
            elif 'doc' in files[i] or 'docx' in files[i] or 'epub'in files[i] or  'pdf' in files[i]:
                OnlineCloseFilePage().close_pdf(get_driver)
                logger.info("doc、docx、epub、pdf课件已关闭！")
            elif 'eda' in files[i] or 'pgn' in files[i] or 'sgf' in files[i]:
                OnlineCloseFilePage().close_eda(get_driver)
                logger.info("eda、pgn、sgf 课件已关闭！")
            elif 'mp3' in files[i] :
                OnlineCloseFilePage().close_avaudio(get_driver)
                logger.info("mp3 课件已关闭！")
            elif 'mp4' in files[i] :
                OnlineCloseFilePage().close_avvideo(get_driver)
                logger.info("mp4 课件已关闭！")
            elif 'txt' in files[i]:
                OnlineCloseFilePage().close_codeeditor(get_driver)
                logger.info("txt 课件已关闭！")
            elif 'edb' in files[i] or 'png' in files[i]:
                logger.info("edb、png 无关闭！")
            else:
                logger.error("文件类型: {} 需要兼容判断！！！".format(files[i]))


class TestOnlineYunPanCloseFileSmoke(object):
    def test_getmainlocation(self, get_driver):
        OnlineClassRoomPage().get_mainLotion(get_driver)

    def test_close_file(self, get_driver):
        files =  get_data('tmp.yaml')[0]['smoke_file_kind']
        logger.info("从以下文件中，选择要关闭的课件： {}".format(files))
        for i in range(len(files)):
            if 'pptx' in files[i]:
                OnlineCloseFilePage().close_pptx(get_driver)
                logger.info("pptx课件已关闭！")
            elif 'csv' in files[i] or 'xlsx' in files[i]:
                OnlineCloseFilePage().close_excel(get_driver)
                logger.info("csv、xlsx 课件已关闭！")
            elif 'doc' in files[i] or 'docx' in files[i] or 'epub'in files[i] or  'pdf' in files[i]:
                OnlineCloseFilePage().close_pdf(get_driver)
                logger.info("doc、docx、epub、pdf课件已关闭！")
            elif 'eda' in files[i] or 'pgn' in files[i] or 'sgf' in files[i]:
                OnlineCloseFilePage().close_eda(get_driver)
                logger.info("eda、pgn、sgf 课件已关闭！")
            elif 'mp3' in files[i] :
                OnlineCloseFilePage().close_avaudio(get_driver)
                logger.info("mp3 课件已关闭！")
            elif 'mp4' in files[i] :
                OnlineCloseFilePage().close_avvideo(get_driver)
                logger.info("mp4 课件已关闭！")
            elif 'txt' in files[i]:
                OnlineCloseFilePage().close_codeeditor(get_driver)
                logger.info("txt 课件已关闭！")
            elif 'edb' in files[i] or 'png' in files[i]:
                logger.info("edb、png 无关闭！")
            else:
                logger.error("文件类型: {} 需要兼容判断！！！".format(files[i]))


class TestToolChoose:
    """使用工具： 选择&移动"""
    def test_move(self, get_driver):
        """快捷键： 全选、复制、粘贴"""
        OnlineClassRoomPage().use_choose_quick_copy(get_driver)


class TestToolChooseSmoke:
    """使用工具： 选择&移动--smoke用例"""
    def test_move(self, get_driver):
        """快捷键： 全选、复制、粘贴"""
        OnlineClassRoomPage().use_choose_quick_copy_smoke(get_driver)


class TestToolPen:
    """使用工具： 画笔"""
    def test_draw(self, get_driver):
        """画线条"""
        for i in range(stability_conf.online_loop):
            OnlineClassRoomPage().use_pen(get_driver)

class TestToolPenSmoke:
    """使用工具： 画笔--smoke用例"""
    def test_draw_smoke(self, get_driver):
        OnlineClassRoomPage().use_pen_first(get_driver)


@allure.feature("教室")
@allure.story("测试--使用画笔")
class TestToolPenPerf:
    @allure.title('画笔')
    @allure.description("使用画笔，画线条")
    def test_draw(self, get_driver, get_function_name):
        """画线条"""
        for i in range(stability_conf.online_loop):
            OnlineClassRoomPage().use_pen(get_driver)
        time.sleep(time_sleep[2] * 6)


class TestToolCut:
    """ 使用工具： 截图"""
    def test_cut(self, get_driver):
        OnlineClassRoomPage().get_cut_icon(get_driver)
        OnlineClassRoomPage().choose_cut(get_driver)

class TestToolRubber:
    """使用工具： 橡皮擦"""
    def test_use_rubber(self, get_driver):
        for i in range(stability_conf.online_loop):
            OnlineClassRoomPage().use_rubber_icon(get_driver)


class TestToolRubberSmoke:
    """使用工具： 橡皮擦--smoke使用"""
    def test_use_rubber(self, get_driver):
            OnlineClassRoomPage().use_rubber_icon_smoke(get_driver)


@allure.feature("教室")
@allure.story("测试--使用橡皮擦")
class TestToolRubberPerf:
    @allure.title('橡皮擦')
    @allure.description("使用橡皮擦")
    def test_use_rubber(self, get_driver, get_function_name):
        for i in range(stability_conf.online_loop):
            OnlineClassRoomPage().use_rubber_icon(get_driver)
        time.sleep(time_sleep[2] * 6)


class TestRubberClearScreen:
    """使用橡皮擦的清屏"""
    def test_rubber_clear(self, get_driver):
        OnlineClassRoomPage().click_rubber_clear(get_driver)

    def test_clear_ensure(self, get_driver):
        OnlineClassRoomPage().click_clear_promt(get_driver)
        PromptChoose().prompt_choose_yes(get_driver)

@allure.feature("教室")
@allure.story("测试--使用橡皮擦")
class TestRubberClearScreenPerf:
    @allure.title('橡皮擦')
    @allure.description("点击 橡皮擦 清屏icon")
    def test_rubber_clear(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_rubber_clear(get_driver)

    @allure.title('橡皮擦')
    @allure.description("清屏确认")
    def test_clear_ensure(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_clear_promt(get_driver)
        PromptChoose().prompt_choose_yes(get_driver)
        time.sleep(time_sleep[2] * 2)

class TestToolText:
    def test_use_text(self, get_driver):
        for i in range(stability_conf.online_loop):
            OnlineClassRoomPage().use_text(get_driver)
            content = random.choice(get_data('class.yaml')[0]['online_chat_content'])
            utils.copy_paste(content)


class TestToolTextSmoke:
    def test_use_text(self, get_driver):
        OnlineClassRoomPage().use_text_smoke(get_driver)
        content = get_data('class.yaml')[0]['online_chat_content'][0]
        utils.copy_paste(content)


class TestToolNote:
    def test_add_note(self, get_driver):
        OnlineClassRoomPage().click_add_note(get_driver)
        OnlineClassRoomPage().add_note_text(get_driver)
        OnlineClassRoomPage().close_note_win(get_driver)

class TestToolNoteSmoke:
    def test_add_note(self, get_driver):
        OnlineClassRoomPage().click_add_note(get_driver)
        OnlineClassRoomPage().add_note_text_smoke(get_driver)
        OnlineClassRoomPage().close_note_win(get_driver)


class TestToolChat:
    def test_add_chat(self, get_driver):
        """发送聊天内容： 从content list中，随机选一条文字，发送 """
        OnlineClassRoomPage().edit_chat_content(get_driver)
        content = random.choice(get_data('class.yaml')[0]['online_chat_content'])
        utils.copy_paste(content)
        time.sleep(2)
        OnlineClassRoomPage().click_add_chat(get_driver)
        OnlineClassRoomPage().close_chat_win(get_driver)

class TestToolChatSmoke:
    def test_add_chat_smoke(self, get_driver):
        """发送聊天内容： 从content list中，选第一条文字，发送--smoke用例 """
        OnlineClassRoomPage().edit_chat_content(get_driver)
        content = get_data('class.yaml')[0]['online_chat_content'][0]
        utils.copy_paste(content)
        time.sleep(2)
        OnlineClassRoomPage().click_add_chat(get_driver)
        OnlineClassRoomPage().close_chat_win(get_driver)


@allure.feature("教室")
@allure.story("测试--使用聊天")
class TestToolChatTextPerf:
    @allure.title('聊天')
    @allure.description("工具栏上点击聊天icon")
    def test_click_tool_chat(self, get_driver, get_function_name):
        OnlineClassRoomPage().get_chat_icon(get_driver)

    @allure.title('聊天')
    @allure.description("聊天框，点击文字输入框")
    def test_click_chat_text_icon(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_chat_text_icon(get_driver)

    @allure.title('聊天')
    @allure.description("编辑聊天内容")
    def test_add_chat_text(self, get_driver, get_function_name):
        """发送聊天内容： 从content list中，随机选一条文字，发送 """
        content = random.choice(get_data('class.yaml')[0]['online_chat_content'])
        utils.copy_paste(content)
        time.sleep(2)

    @allure.title('聊天')
    @allure.description("发送聊天内容")
    def test_send_chat_text(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_add_chat(get_driver)

    @allure.title('聊天')
    @allure.description("关闭聊天窗口")
    def test_close_chat_win(self, get_driver, get_function_name):
        OnlineClassRoomPage().close_chat_win(get_driver)
        time.sleep(time_sleep[2] * 6)


@allure.feature("教室")
@allure.story("测试--使用聊天")
class TestToolChatSendTextAndCutPerf:
    @allure.title('聊天')
    @allure.description("工具栏上点击聊天icon")
    def test_click_tool_chat(self, get_driver, get_function_name):
        OnlineClassRoomPage().get_chat_icon(get_driver)

    @allure.title('聊天')
    @allure.description("点击聊天的截图功能icon")
    def test_click_chat_cut_icon(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_chat_cut_icon(get_driver)

    @allure.title('聊天')
    @allure.description("编辑聊天截图")
    def test_add_chat_cut(self, get_driver, get_function_name):
        OnlineClassRoomPage().add_chat_cut(get_driver)

    @allure.title('聊天')
    @allure.description("聊天框，点击文字输入框")
    def test_click_chat_text_icon(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_chat_text_icon(get_driver)

    @allure.title('聊天')
    @allure.description("编辑聊天内容")
    def test_add_chat_text(self, get_driver, get_function_name):
        """发送聊天内容： 从content list中，随机选一条文字，发送 """
        content = random.choice(get_data('class.yaml')[0]['online_chat_content'])
        utils.copy_paste(content)
        time.sleep(2)

    @allure.title('聊天')
    @allure.description("点击发送btn")
    def test_send_chat_text(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_add_chat(get_driver)

    @allure.title('聊天')
    @allure.description("关闭聊天窗口")
    def test_close_chat_win(self, get_driver, get_function_name):
        OnlineClassRoomPage().close_chat_win(get_driver)
        time.sleep(time_sleep[2] * 6)


class TestToolHandUp:
    def test_choose_handup(self, get_driver):
        OnlineClassRoomPage().get_handup_icon(get_driver)
        OnlineClassRoomPage().click_handup_box(get_driver)
        time.sleep(5)


@allure.feature("教室")
@allure.story("测试--举手功能")
class TestToolHandUpPerf:
    @allure.title('举手')
    @allure.description("授权举手功能")
    def test_choose_handup(self, get_driver, get_function_name):
        OnlineClassRoomPage().get_handup_icon(get_driver)
        OnlineClassRoomPage().click_handup_box(get_driver)
        time.sleep(time_sleep[2] * 6)


class TestRoster:
    def test_open_roster(self, get_driver):
        """打开 花名册"""
        OnlineClassRoomPage().get_roster_icon(get_driver)
        time.sleep(1)

    def test_click_stu_table(self, get_driver):
        """花名册 班级学生 title各字段排序"""
        OnlineClassRoomPage().click_stu_tab(get_driver)
        OnlineClassRoomPage().click_stu_table_title(get_driver)
        OnlineClassRoomPage().click_stu_table_item(get_driver)

    def test_click_tea_table(self, get_driver):
        """花名册 联席教师 title各自动排序"""
        OnlineClassRoomPage().click_tea_tab(get_driver)
        OnlineClassRoomPage().click_tea_table_title(get_driver)

    def test_close_roster(self, get_driver):
        """关闭 花名册"""
        OnlineClassRoomPage().close_roster_win(get_driver)
        time.sleep(1)

class TestAllStuMute:
    def test_mute(self, get_driver):
        """花名册 全体静音/取消静音"""
        TestRoster().test_open_roster(get_driver)
        OnlineClassRoomPage().click_mute(get_driver)
        time.sleep(5)
        TestRoster().test_close_roster(get_driver)

class TestAllStuEmpower:
    def test_empower(self, get_driver):
        """花名册 全体授权/取消授权"""
        TestRoster().test_open_roster(get_driver)
        OnlineClassRoomPage().click_stu_empower(get_driver)
        time.sleep(5)
        TestRoster().test_close_roster(get_driver)

class TestAllStuLunBo:
    def test_set_lunbo(self, get_driver):
        """花名册 设置轮播"""
        TestRoster().test_open_roster(get_driver)
        OnlineClassRoomPage().click_lunbo_open(get_driver)
        OnlineClassRoomPage().choose_who_lunbo(get_driver)
        OnlineClassRoomPage().choose_order_lunbo(get_driver)
        TestRoster().test_close_roster(get_driver)


@allure.feature("教室")
@allure.story("测试--开启轮播")
class TestAllStuLunBoPerf:
    @allure.title('轮播')
    @allure.description("打开花名册")
    def test_open_roster(self, get_driver, get_function_name):
        TestRoster().test_open_roster(get_driver)

    @allure.title('轮播')
    @allure.description("点击开启轮播")
    def test_click_start_lunbo(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_lunbo_open(get_driver)
        time.sleep(time_sleep[2])

    @allure.title('轮播')
    @allure.description("关闭花名册")
    def test_close_roster(self, get_driver, get_function_name):
        TestRoster().test_close_roster(get_driver)
        time.sleep(time_sleep[2])


class TestLunBoSmoke:
    def test_set_lunbo_smoke(self, get_driver):
        """花名册 设置轮播-勾选开启 """
        TestRoster().test_open_roster(get_driver)
        OnlineClassRoomPage().click_lunbo_open(get_driver)
        TestRoster().test_close_roster(get_driver)


class TestAllStuOff:
    def test_stu_off(self, get_driver):
        """花名册 全体下台"""
        TestRoster().test_open_roster(get_driver)
        OnlineClassRoomPage().click_stu_off(get_driver)
        time.sleep(5)
        TestRoster().test_close_roster(get_driver)


class TestOpenToolBoxList:
    def test_get_totle_list(self, get_driver, more_btn=True):
        """打开工具箱，点击更多，显示全部列表"""
        OnlineClassRoomPage().click_toolbox_icon(get_driver)
        OnlineClassRoomPage().get_toolbox_location(get_driver)
        if more_btn:
            OnlineClassRoomPage().click_more_btn(get_driver)  # 不一定会用到加载更多

class TestCloseToolBoxList:
    def test_list_back(self, get_driver):
        """点击更多，收起工具箱列表"""
        OnlineClassRoomPage().click_more_btn(get_driver)

    def test_close_win(self, get_driver):
        """关闭工具箱，窗口"""
        OnlineClassRoomPage().click_toolbox_close_win(get_driver)


class TestToolBoxOpenFile:
    def test_changeto_native_driver(self, get_driver):
        get_win(get_driver, 0)
        time.sleep(5)

    def test_click_openfile(self, get_driver):
        """点击-打开文件，并从本地打开文件"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_openfile(get_driver)
        file = random.choice(get_data('yunpan.yaml')[0]['local_file'])
        file_url = PROJECT_DIR + '\\file\\' + file
        ChooseFile().use_local_file(get_driver, file_url)


class TestToolBoxOpenFileSmoke:
    def test_click_openfile(self, get_driver):
        """点击-打开文件，并从本地打开固定文件--smoke用例"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_openfile(get_driver)
        file = get_data('yunpan.yaml')[0]['local_file'][0]
        file_url = PROJECT_DIR + '\\file\\' + file
        ChooseFile().use_local_file(get_driver, file_url)

class TestSaveEdb:
    def test_save_to_local(self, get_driver):
        """保存板书至本地"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_save_or_share(get_driver)
        OnlineClassRoomPage().click_save_to_local(get_driver)
        file_name = str(int(time.time()))
        OnlineClassRoomPage().use_file_rename(get_driver)
        utils.copy_paste(file_name)
        time.sleep(1)
        OnlineClassRoomPage().click_save_as_url(get_driver)
        folder_url = PROJECT_DIR + '\\file'
        ChooseFolder().use_local_floder(get_driver, folder_url)
        PromptChoose().prompt_choose_queren(get_driver)
        time.sleep(3)


@allure.feature("教室")
@allure.story("测试--工具箱-保存/分享板书")
class TestSaveEdbPerf:
    @allure.title('保存板书')
    @allure.description("保存板书至本地")
    def test_save_to_local(self, get_driver, get_function_name):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_save_or_share(get_driver)
        OnlineClassRoomPage().click_save_to_local(get_driver)
        file_name = str(int(time.time()))
        OnlineClassRoomPage().use_file_rename(get_driver)
        utils.copy_paste(file_name)
        time.sleep(1)

    @allure.title('保存板书')
    @allure.description("保存板书至本地，选择保存路径")
    def test_choose_save_url(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_save_as_url(get_driver)
        folder_url = PROJECT_DIR + '\\file'
        ChooseFolder().use_local_floder(get_driver, folder_url)

    @allure.title('保存板书')
    @allure.description("保存板书至本地，保存确认")
    def test_save_blackboard_ensure(self, get_driver, get_function_name):
        PromptChoose().prompt_choose_queren(get_driver)
        time.sleep(time_sleep[2] * 6)


class TestShaiZi:
    def test_click_shaizi_tool(self, get_driver):
        """工具箱里点击-骰子"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_shaizi(get_driver)

    def test_changeto_webdriver(self, get_web_driver):
        get_new_page_special(get_web_driver, "e_model_dice")

    def test_use_shaizi(self, get_web_driver):
        """操作骰子"""
        # get_win(get_web_driver, 2)
        # time.sleep(2)
        OnlineClassRoomPage().use_shaiziH5(get_web_driver)

    def test_close_shaizi_win(self, get_driver):
        """关闭骰子窗口"""
        OnlineClassRoomPage().click_shaizi_win_close(get_driver)


class TestShaiZiSmoke:
    def test_click_shaizi_tool(self, get_driver):
        """工具箱里点击-骰子"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_shaizi(get_driver)

    def test_changeto_webdriver(self, get_web_driver):
        get_new_page_special(get_web_driver, "e_model_dice")

    def test_use_shaizi(self, get_web_driver):
        """操作骰子"""
        OnlineClassRoomPage().use_shaiziH5_smoke(get_web_driver)
        # get_win(get_web_driver, 2)
        # time.sleep(2)

    def test_close_shaizi_win(self, get_driver):
        """关闭骰子窗口"""
        OnlineClassRoomPage().click_shaizi_win_close(get_driver)


class TestDaTiQi:
    def test_click_tool(self, get_driver):
        """工具箱里点击-答题器"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_datiqi(get_driver)

    def test_use_datiqi(self, get_driver):
        """步骤： 设置正确答案-开始答题-修改答案-结束答题"""
        OnlineClassRoomPage().choose_answer(get_driver)
        OnlineClassRoomPage().click_begin(get_driver)
        OnlineClassRoomPage().click_edit(get_driver)
        PromptChoose().prompt_choose_sure(get_driver)
        time.sleep(10)
        OnlineClassRoomPage().click_end(get_driver)

    def test_close_win(self, get_driver):
        """关闭答题器窗口"""
        OnlineClassRoomPage().click_datiqi_win_close(get_driver)


class TestDaTiQiSmoke:
    def test_click_tool(self, get_driver):
        """工具箱里点击-答题器"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_datiqi(get_driver)

    def test_use_datiqi(self, get_driver):
        """步骤： 设置正确答案-开始答题-修改答案-结束答题"""
        OnlineClassRoomPage().choose_answer_first(get_driver)
        OnlineClassRoomPage().click_begin(get_driver)
        OnlineClassRoomPage().click_edit_smoke(get_driver)
        PromptChoose().prompt_choose_sure(get_driver)
        time.sleep(10)
        OnlineClassRoomPage().click_end(get_driver)

    def test_close_win(self, get_driver):
        """关闭答题器窗口"""
        OnlineClassRoomPage().click_datiqi_win_close(get_driver)


@allure.feature("教室")
@allure.story("测试--答题器")
class TestAnswerPerf:
    @allure.title('答题器')
    @allure.description("打开工具答题器")
    def test_click_answer_tool(self, get_driver, get_function_name):
        """工具箱里点击-答题器"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_datiqi(get_driver)
        time.sleep(time_sleep[2] * 6)

    @allure.title('答题器')
    @allure.description("答题器--设置正确答案")
    def test_answer_setting(self, get_driver, get_function_name):
        OnlineClassRoomPage().choose_answer(get_driver)
        time.sleep(time_sleep[2] * 6)

    @allure.title('答题器')
    @allure.description("答题器--开始答题")
    def test_answer_start(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_begin(get_driver)
        time.sleep(time_sleep[2] * 12)

    @allure.title('答题器')
    @allure.description("答题器--修改答案")
    def test_answer_edit(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_edit(get_driver)
        PromptChoose().prompt_choose_sure(get_driver)
        time.sleep(time_sleep[2] * 12)

    @allure.title('答题器')
    @allure.description("答题器--结束答题")
    def test_answer_end(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_end(get_driver)
        time.sleep(time_sleep[2] * 12)

    @allure.title('答题器')
    @allure.description("答题器--关闭答题器")
    def test_close_win(self, get_driver, get_function_name):
        """关闭答题器窗口"""
        OnlineClassRoomPage().click_datiqi_win_close(get_driver)
        time.sleep(time_sleep[2] * 6)


class TestJiShiQi:
    def test_jishiqi_tool(self, get_driver):
        """工具箱里点击-计时器"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_jishiqi(get_driver)

    def test_use_jishiqi(self, get_driver):
        """步骤： 开始-暂停-重置-开始-暂停-继续"""
        OnlineClassRoomPage().click_begin_jishiqi(get_driver)
        time.sleep(5)
        OnlineClassRoomPage().click_stop_jishiqi(get_driver)
        time.sleep(5)
        OnlineClassRoomPage().click_reset_jishiqi(get_driver)
        time.sleep(3)
        OnlineClassRoomPage().click_begin_jishiqi(get_driver)
        time.sleep(5)
        OnlineClassRoomPage().click_stop_jishiqi(get_driver)
        time.sleep(5)
        OnlineClassRoomPage().click_continue_jishiqi(get_driver)
        time.sleep(5)

    def test_jishiqi_win_close(self, get_driver):
        OnlineClassRoomPage().click_jishiqi_win_close(get_driver)


class TestDingShiQi:
    def test_dingshiqi_tool(self, get_driver):
        """工具箱里点击-定时器"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_dingshiqi(get_driver)

    def test_use_dingshiqi(self, get_driver):
        """编辑定时器，时长，点击开始"""
        OnlineClassRoomPage().click_dingshiqi_edit(get_driver)
        OnlineClassRoomPage().click_dingshiqi_begin(get_driver)

    def test_dingshiqi_win_close(self, get_driver):
        """关闭 定时器 窗口"""
        OnlineClassRoomPage().click_dingshiqi_win_close(get_driver)


class TestDingShiQiSmoke:
    def test_dingshiqi_smoke(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_dingshiqi(get_driver)
        OnlineClassRoomPage().click_dingshiqi_edit_smoke(get_driver)
        OnlineClassRoomPage().click_dingshiqi_begin(get_driver)
        OnlineClassRoomPage().click_dingshiqi_win_close(get_driver)


class TestShareDeskTop:
    def test_share_open(self, get_driver):
        """共享工具--打开 桌面共享"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_share_icon(get_driver)
        OnlineClassRoomPage().click_share_desktop(get_driver)
        get_win(get_driver, 0)

    # def test_share_sound(self, get_driver):
    #     """共享声音"""
    #     OnlineClassRoomPage().click_share_sound(get_driver)

    # def test_share_start(self, get_driver):
    #     """开始共享"""
    #     OnlineClassRoomPage().click_share_start(get_driver)

    def test_share_start(self, get_driver):
        """开始共享"""
        OnlineClassRoomPage().click_share(get_driver)
        time.sleep(10)
        get_win(get_driver, 1)

    def test_end_share(self, get_driver):
        OnlineClassRoomPage().click_end_share(get_driver)
        get_win(get_driver, 0)

    # def test_share_close(self, get_driver):
    #     """关闭共享"""
    #     OnlineClassRoomPage().click_share_desktop_close(get_driver)
    #     get_win(get_driver, 0)


@allure.feature("教室")
@allure.story("测试--屏幕共享")
class TestShareDeskTopPerf:
    @allure.title('桌面共享')
    @allure.description("点击选择功能桌面共享")
    def test_desk_share_open(self, get_driver, get_function_name):
        """共享工具--打开 桌面共享"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_share_icon(get_driver)
        OnlineClassRoomPage().click_share_desktop(get_driver)
        get_win(get_driver, 0)

    @allure.title('桌面共享')
    @allure.description("点击开始共享")
    def test_desk_share_start(self, get_driver, get_function_name):
        """开始共享"""
        OnlineClassRoomPage().click_share(get_driver)
        time.sleep(5)
        get_win(get_driver, 1)
        time.sleep(time_sleep[2] * 36)

    @allure.title('桌面共享')
    @allure.description("关闭共享")
    def test_desk_end_share(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_end_share(get_driver)
        get_win(get_driver, 0)


class TestShareTeacher:
    def test_share_open(self, get_driver):
        """共享工具--打开 桌面共享"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_share_icon(get_driver)
        OnlineClassRoomPage().click_share_teacher(get_driver)
        get_win(get_driver, 0)

    # def test_share_close(self, get_driver):
    #     """关闭共享"""
    #     OnlineClassRoomPage().click_share_teacher_close(get_driver)
    #     get_win(get_driver, 0)

    def test_share_start(self, get_driver):
        """开始共享"""
        OnlineClassRoomPage().click_share(get_driver)
        time.sleep(10)
        get_win(get_driver, 0)

    def test_end_share(self, get_driver):
        OnlineClassRoomPage().click_end_share(get_driver)
        get_win(get_driver, 0)


@allure.feature("教室")
@allure.story("测试--屏幕共享")
class TestShareTeacherPerf:
    @allure.title('教师屏幕共享')
    @allure.description("点击选择功能教师屏幕共享")
    def test_tea_share_open(self, get_driver, get_function_name):
        """共享工具--打开 桌面共享"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_share_icon(get_driver)
        OnlineClassRoomPage().click_share_teacher(get_driver)
        get_win(get_driver, 0)

    @allure.title('教师屏幕共享')
    @allure.description("点击开始共享")
    def test_tea_share_start(self, get_driver, get_function_name):
        """开始共享"""
        OnlineClassRoomPage().click_share(get_driver)
        time.sleep(5)
        get_win(get_driver, 0)
        time.sleep(time_sleep[2] * 36)

    @allure.title('教师屏幕共享')
    @allure.description("关闭共享")
    def test_tea_end_share(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_end_share(get_driver)
        get_win(get_driver, 0)


@allure.feature("教室")
@allure.story("测试--屏幕共享")
class TestShareStudentPerf:
    @allure.title('学生屏幕共享')
    @allure.description("点击选择功能学生屏幕共享")
    def test_stu_share_open(self, get_driver, get_function_name):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_share_icon(get_driver)
        OnlineClassRoomPage().click_share_student(get_driver)
        get_win(get_driver, 0)

    @allure.title('学生屏幕共享')
    @allure.description("点击开始共享")
    def test_stu_share_start(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_stu_share(get_driver)
        time.sleep(5)
        time.sleep(time_sleep[2] * 36)

    @allure.title('学生屏幕共享')
    @allure.description("关闭共享")
    def test_stu_end_share(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_end_share(get_driver)


class TestPaintUsePen:
    def test_open_paint(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_xiaoheiban_icon(get_driver)
        OnlineClassRoomPage().click_xiaoneiban_paint(get_driver)
    def test_use_paint_pen(self, get_driver):
        for i in range(stability_conf.online_loop):
            OnlineClassRoomPage().use_paint_pen(get_driver)
            time.sleep(2)
    def test_paint_share(self, get_driver):
        OnlineClassRoomPage().click_paint_share(get_driver)
        time.sleep(5)
    def test_paint_back(self, get_driver):
        OnlineClassRoomPage().click_paint_back(get_driver)
        time.sleep(5)
    def test_paint_close_win(self, get_driver):
        OnlineClassRoomPage().click_panit_close(get_driver)
        PromptChoose().prompt_choose_yes(get_driver)
        folder_url = PROJECT_DIR + '\\folder'
        ChooseFolder().use_local_floder(get_driver, folder_url)


class TestPaintUsePenSmoke:
    def test_paint_smoke(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_xiaoheiban_icon(get_driver)
        OnlineClassRoomPage().click_xiaoneiban_paint(get_driver)
        OnlineClassRoomPage().use_paint_pen_smoke(get_driver)
        time.sleep(2)
        OnlineClassRoomPage().click_paint_share(get_driver)
        time.sleep(5)
        OnlineClassRoomPage().click_paint_back(get_driver)
        time.sleep(5)
        OnlineClassRoomPage().click_panit_close(get_driver)
        PromptChoose().prompt_choose_yes(get_driver)
        folder_url = PROJECT_DIR + '\\folder'
        ChooseFolder().use_local_floder(get_driver, folder_url)


class TestPaintUseText:
    def test_open_paint(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_xiaoheiban_icon(get_driver)
        OnlineClassRoomPage().click_xiaoneiban_paint(get_driver)

    def test_use_paint_text(self, get_driver):
        OnlineClassRoomPage().use_paint_text(get_driver)
        content = random.choice(get_data('class.yaml')[0]['online_chat_content'])
        utils.copy_paste(content)
        time.sleep(2)

    def test_paint_share(self, get_driver):
        OnlineClassRoomPage().click_paint_share(get_driver)
        time.sleep(5)

    def test_paint_back(self, get_driver):
        OnlineClassRoomPage().click_paint_back(get_driver)
        time.sleep(5)

    def test_paint_close_win(self, get_driver):
        OnlineClassRoomPage().click_panit_close(get_driver)
        PromptChoose().prompt_choose_yes(get_driver)
        folder_url = PROJECT_DIR + '\\folder'
        ChooseFolder().use_local_floder(get_driver, folder_url)




class TestTextEdit:
    def test_open_text(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_xiaoheiban_icon(get_driver)
        OnlineClassRoomPage().click_xiaoneiban_text(get_driver)

    def test_text_edit(self, get_driver):
        case = get_data('class.yaml')[0]
        content = random.choice(case['online_chat_content'])
        OnlineClassRoomPage().use_text_edit(get_driver)
        utils.copy_paste(content)


    def test_paint_share(self, get_driver):
        OnlineClassRoomPage().click_paint_share(get_driver)
        time.sleep(5)
    def test_paint_back(self, get_driver):
        OnlineClassRoomPage().click_paint_back(get_driver)
        time.sleep(5)
    def test_paint_close_win(self, get_driver):
        OnlineClassRoomPage().click_panit_close(get_driver)
        PromptChoose().prompt_choose_yes(get_driver)
        folder_url = PROJECT_DIR + '\\folder'
        time.sleep(2)
        ChooseFolder().use_local_floder(get_driver, folder_url)


class TestTextEditSmoke:
    def test_text_smoke(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_xiaoheiban_icon(get_driver)
        OnlineClassRoomPage().click_xiaoneiban_text(get_driver)

    def test_text_edit_smoke(self, get_driver):
        case = get_data('class.yaml')[0]
        content = case['online_chat_content'][0]
        OnlineClassRoomPage().use_text_edit(get_driver)
        utils.copy_paste(content)

    def test_paint_share(self, get_driver):
        OnlineClassRoomPage().click_paint_share(get_driver)
        time.sleep(5)
    def test_paint_back(self, get_driver):
        OnlineClassRoomPage().click_paint_back(get_driver)
        time.sleep(5)
    def test_paint_close_win(self, get_driver):
        OnlineClassRoomPage().click_panit_close(get_driver)
        PromptChoose().prompt_choose_yes(get_driver)
        folder_url = PROJECT_DIR + '\\folder'
        time.sleep(2)
        ChooseFolder().use_local_floder(get_driver, folder_url)


class TestGroupDiscuss:
    def test_group(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_group_icon(get_driver)
        OnlineClassRoomPage().click_start_group(get_driver)
        OnlineClassRoomPage().click_begin_discuss(get_driver)
        OnlineClassRoomPage().click_end_discuss(get_driver)
        OnlineClassRoomPage().click_re_group(get_driver)
        OnlineClassRoomPage().click_begin_discuss(get_driver)
        OnlineClassRoomPage().click_end_discuss(get_driver)
        OnlineClassRoomPage().click_re_discuss(get_driver)
        OnlineClassRoomPage().click_end_discuss(get_driver)
        OnlineClassRoomPage().click_group_win_close(get_driver)
        PromptChoose().prompt_choose_yes(get_driver)


class TestBrowser:
    def test_open_browser(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver)
        OnlineClassRoomPage().click_browser_icon(get_driver)

    def test_eidt_url(self, get_driver):
        OnlineClassRoomPage().click_browser_url(get_driver)
        time.sleep(1)
        content = random.choice(get_data('class.yaml')[0]['classroom_browser_url'])
        utils.copy_paste(content)
        time.sleep(2)
        OnlineClassRoomPage().use_key_enter(get_driver)
        time.sleep(5)

    def test_close_browser_win(self, get_driver):
        OnlineClassRoomPage().click_browser_win_close(get_driver)


class TestBrowserSmoke:
    def test_open_browser(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver)
        OnlineClassRoomPage().click_browser_icon(get_driver)

    def test_eidt_url(self, get_driver):
        OnlineClassRoomPage().click_browser_url(get_driver)
        time.sleep(1)
        content = get_data('class.yaml')[0]['classroom_browser_url'][0]
        utils.copy_paste(content)
        time.sleep(2)
        OnlineClassRoomPage().use_key_enter(get_driver)
        time.sleep(5)

    def test_close_browser_win(self, get_driver):
        OnlineClassRoomPage().click_browser_win_close(get_driver)


@allure.feature("教室")
@allure.story("测试--浏览器")
class TestBrowserPerf:
    @allure.title('浏览器')
    @allure.description("浏览器--打开浏览器")
    def test_open_browser_tool(self, get_driver, get_function_name):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_browser_icon(get_driver)
        time.sleep(time_sleep[2] * 6)

    @allure.title('浏览器')
    @allure.description("浏览器--编辑url")
    def test_eidt_url(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_browser_url(get_driver)
        time.sleep(5)
        content = random.choice(get_data('class.yaml')[0]['classroom_browser_url'])
        utils.copy_paste(content)
        time.sleep(5)
        OnlineClassRoomPage().use_key_enter(get_driver)
        time.sleep(time_sleep[2] * 12)

    @allure.title('浏览器')
    @allure.description("浏览器--关闭浏览器")
    def test_close_browser_win(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_browser_win_close(get_driver)
        time.sleep(time_sleep[2] * 12)


class TestVideo:
    # 有扩展屏
    def test_open_video(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_video_icon(get_driver)
        PromptChoose().prompt_choose_open(get_driver)
        time.sleep(2)
        get_win(get_driver, 1)
        time.sleep(5)

    def test_switch_screen(self, get_driver):
        OnlineClassRoomPage().click_switch(get_driver)
        time.sleep(5)

    def test_save_yunpan(self, get_driver):
        OnlineClassRoomPage().click_save(get_driver)
        time.sleep(2)
        OnlineClassRoomPage().click_save_yunpan(get_driver)
        time.sleep(2)
        PromptChoose().prompt_choose_queren(get_driver)
        time.sleep(2)

    def test_close_save(self, get_driver):
        OnlineClassRoomPage().close_save_win(get_driver)

    def test_wall_setting(self, get_driver):
        OnlineClassRoomPage().click_wall_setting(get_driver)
        PromptChoose().prompt_choose_done(get_driver)
        time.sleep(2)

    def test_wall_win_close(self, get_driver):
        OnlineClassRoomPage().click_wall_win_close(get_driver)
        time.sleep(2)
        get_win(get_driver, 0)
        time.sleep(5)


class TestVideoOneScreen:
    # 一块屏幕
    def test_open_video(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_video_icon(get_driver)
        PromptChoose().prompt_choose_open(get_driver)
        time.sleep(2)
        get_win(get_driver, 0)
        time.sleep(5)

    def test_save_yunpan(self, get_driver):
        OnlineClassRoomPage().click_phone_for_one_screen(get_driver)
        time.sleep(2)
        OnlineClassRoomPage().click_save_yunpan(get_driver)
        time.sleep(2)
        PromptChoose().prompt_choose_queren(get_driver)
        time.sleep(2)

    def test_close_save(self, get_driver):
        OnlineClassRoomPage().close_save_win(get_driver)

    def test_wall_setting(self, get_driver):
        OnlineClassRoomPage().click_wall_setting_for_one_screen(get_driver)
        PromptChoose().prompt_choose_done(get_driver)
        time.sleep(2)

    def test_wall_win_close(self, get_driver):
        OnlineClassRoomPage().click_wall_win_close_for_one_screen(get_driver)
        time.sleep(2)
        get_win(get_driver, 0)
        time.sleep(5)


@allure.feature("教室")
@allure.story("测试--视频墙")
class TestVideoOneScreenPerf:
    @allure.title('视频墙')
    @allure.description("打开工具视频墙")
    def test_open_video(self, get_driver, get_function_name):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=True)
        OnlineClassRoomPage().click_video_icon(get_driver)
        PromptChoose().prompt_choose_open(get_driver)
        time.sleep(2)
        get_win(get_driver, 0)
        time.sleep(time_sleep[2] * 36)

    @allure.title('视频墙')
    @allure.description("关闭视频墙")
    def test_wall_win_close(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_wall_win_close_for_one_screen(get_driver)
        time.sleep(2)
        get_win(get_driver, 0)
        time.sleep(5)


class TestMaterial:
    def test_open_material(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_material_icon(get_driver)

    # def test_choose_subject(self, get_web_driver):
    #     OnlineClassRoomPage().click_choose_subject(get_web_driver)
    def test_changeto_webdriver(self, get_web_driver):
        get_new_page_special(get_web_driver, "material")

    def test_choose_item(self, get_web_driver):
        OnlineClassRoomPage().click_material_item(get_web_driver)

    def test_close_win(self, get_driver):
        OnlineClassRoomPage().click_material_win_close(get_driver)


class TestMaterialSmoke:
    def test_open_material(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_material_icon(get_driver)

    def test_choose_item(self, get_web_driver):
        get_win(get_web_driver, 2)
        time.sleep(2)
        OnlineClassRoomPage().click_material_item_smoke(get_web_driver)

    def test_close_win(self, get_driver):
        OnlineClassRoomPage().click_material_win_close(get_driver)


class TestRuler:
    def test_open_ruler(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_ruler_icon(get_driver)
        time.sleep(2)

    #   # 点击后的尺规不能关闭, 影响层级关系, 暂不执行
    # def test_choose_ruler_item(self, get_driver):
    #     OnlineClassRoomPage().click_ruler_item(get_driver)

    def test_ruler_win_close(self, get_driver):
        OnlineClassRoomPage().click_ruler_win_close(get_driver)


class TestGeometry:
    # 几何图形
    def test_open_geometry(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_geometry_icon(get_driver)
        time.sleep(2)

    def test_choose_geometry_item(self, get_driver):
        OnlineClassRoomPage().click_geometry_item(get_driver)

    def test_geometry_win_close(self, get_driver):
        OnlineClassRoomPage().click_geometry_win_close(get_driver)


class TestRulerSmoke:
    def test_open_ruler(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_ruler_icon(get_driver)
        time.sleep(2)

      # 点击后的尺规不能关闭, 影响层级关系, 暂不执行
    def test_choose_ruler_item(self, get_driver):
        OnlineClassRoomPage().click_ruler_item_smoke(get_driver)

    def test_ruler_win_close(self, get_driver):
        OnlineClassRoomPage().click_ruler_win_close(get_driver)


class TestClassOverAppraise:
    def test_yes(self, get_driver, get_function_name):
        time.sleep(2)
        get_win(get_driver, 0)
        time.sleep(2)
        """评价窗口上，直接点击确定"""
        ClassAppraise().appraise_sure(get_driver)
        get_win(get_driver, 0)
        time.sleep(2)


# -----------------hk
class TestTouPing:
    def test_classIn_touping(self, get_driver):
        """classIn投屏"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_touping(get_driver)
        OnlineClassRoomPage().click_classIn_touping(get_driver)
        OnlineClassRoomPage().click_sound_local_btn(get_driver)
        OnlineClassRoomPage().click_sound_share_btn(get_driver)
        OnlineClassRoomPage().click_classin_win_close(get_driver)

    def test_apple_touping(self, get_driver):
        """苹果投屏"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_touping(get_driver)
        OnlineClassRoomPage().click_apple_touping(get_driver)
        OnlineClassRoomPage().click_sound_local_btn(get_driver)
        OnlineClassRoomPage().click_sound_share_btn(get_driver)
        OnlineClassRoomPage().click_apple_win_close(get_driver)


class TestSuiJiXuanRen:
    def test_xuanren_tool(self, get_driver):
        """工具箱中选择 随机选人"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_xuanren(get_driver)

    def test_use_xuanren(self, get_driver):
        """下拉框-选择 全部学生-开始选人， 下拉框-选择 在线学生-开始选人"""
        OnlineClassRoomPage().choose_stu(get_driver)
        OnlineClassRoomPage().click_all_stu(get_driver)
        OnlineClassRoomPage().click_start_xuanren(get_driver)
        time.sleep(2)
        OnlineClassRoomPage().choose_stu(get_driver)
        OnlineClassRoomPage().click_online_stu(get_driver)
        OnlineClassRoomPage().click_start_xuanren(get_driver)
        time.sleep(2)

    def test_xuanren_win_close(self, get_driver):
        """关闭 随机选人 窗口"""
        OnlineClassRoomPage().click_xuanren_win_close(get_driver)


class TestCollaboration:
    def test_wenben(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_xiezuo(get_driver)
        OnlineClassRoomPage().click_wenben(get_driver)
        OnlineClassRoomPage().input_wenben(get_driver)
        OnlineClassRoomPage().wenben_save_local(get_driver)
        OnlineClassRoomPage().click_wenben_win_close(get_driver)

    def test_wendang(self, get_driver):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_xiezuo(get_driver)
        OnlineClassRoomPage().click_wendang(get_driver)
        time.sleep(5)
        OnlineClassRoomPage().input_wendang(get_driver)
        OnlineClassRoomPage().click_wendang_win_close(get_driver)


class TestRewardRank:
    """奖励排行榜"""
    def test_reward_rank_tool(self, get_driver):
        """工具箱里点击-奖励排行榜"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        time.sleep(3)
        OnlineClassRoomPage().click_reward_rank(get_driver)

    def test_rank_win_close(self, get_driver):
        """关闭 奖励排行榜 窗口"""
        OnlineClassRoomPage().click_rank_win_close(get_driver)


class TestAssistCamera:
    """辅助摄像头"""
    def test_assist_camera_tool(self, get_driver):
        """工具箱里点击-辅助摄像头"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        time.sleep(3)
        OnlineClassRoomPage().click_assist_camera(get_driver)

    def test_camera_win_close(self, get_driver):
        """关闭 辅助摄像头 窗口"""
        OnlineClassRoomPage().click_camera_win_close(get_driver)


class TestGo:
    """围棋小黑板"""
    def test_assist_camera_tool(self, get_driver):
        """工具箱里点击-围棋小黑板"""
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_go(get_driver)

    def test_select_lushu(self, get_driver):
        """选择围棋路数"""
        OnlineClassRoomPage().select_lushu(get_driver)

    def test_select_color(self, get_driver):
        """选择围棋路数"""
        OnlineClassRoomPage().select_color(get_driver)

    def test_click_board(self, get_driver):
        """出棋"""
        OnlineClassRoomPage().click_board(get_driver)

    def test_click_send(self, get_driver):
        """分发"""
        OnlineClassRoomPage().click_send(get_driver)

    def test_click_take_back(self, get_driver):
        """收回"""
        time.sleep(3)
        OnlineClassRoomPage().click_send(get_driver)

    def test_click_close(self, get_driver):
        """关闭窗口"""
        OnlineClassRoomPage().click_board_win_close(get_driver)


@allure.feature("教室")
@allure.story("测试--抢答器")
class TestResponderPerf:
    @allure.title('抢答器')
    @allure.description("打开工具抢答器")
    def test_open_responder(self, get_driver, get_function_name):
        TestOpenToolBoxList().test_get_totle_list(get_driver, more_btn=False)
        OnlineClassRoomPage().click_responder_icon(get_driver)
        time.sleep(time_sleep[2] * 6)

    @allure.title('抢答器')
    @allure.description("抢答器--开始抢答")
    def test_start_response(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_response_start(get_driver)
        time.sleep(time_sleep[2] * 36)

    @allure.title('抢答器')
    @allure.description("抢答器--重新抢答")
    def test_restart_response(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_response_restart(get_driver)   # 点击“重新开始”，再点“开始抢答”
        time.sleep(time_sleep[2] * 6)
        OnlineClassRoomPage().click_response_start(get_driver)
        time.sleep(time_sleep[2] * 12)

    @allure.title('抢答器')
    @allure.description("抢答器--关闭抢答器")
    def test_close_response(self, get_driver, get_function_name):
        OnlineClassRoomPage().click_response_close(get_driver)







######################学生端 操作
class TestStuSleep:
    def test_time_sleep_60(self, get_function_name):
        time.sleep(60)

    def test_time_sleep_1500(self, get_function_name):
        time.sleep(1500)


class TestStuClassOverAppraise:
    def test_cancel(self, get_driver, get_function_name):
        time.sleep(2)
        get_win(get_driver, 0)
        time.sleep(2)
        """窗口上，直接点击取消"""
        PromptChoose().prompt_choose_cancel(get_driver)
        get_win(get_driver, 0)
        time.sleep(2)


@allure.feature("教室")
@allure.story("测试--举手功能")
class TestStuHandUp:
    @allure.title('举手')
    @allure.description("授权举手功能")
    def test_choose_handup(self, get_driver, get_function_name):
        StuOnlineClassRoomPage().click_handup_icon(get_driver)


