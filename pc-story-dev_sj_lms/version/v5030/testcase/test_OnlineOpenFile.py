# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from version.v5030.pageobject.onlineOpenFile_page import OnlineOpenFilePage
from handler.yamlHandler import get_data
import allure
from config import perf_conf
from version.v5030 import *
from config import *
from config import stability_conf
import random
from handler.logHandler import logger
from handler.yamlHandler import YamlMethod
from version.v5030.pageobject.onlineOpenFile_page import MP4Operation, PDFOperation, PPTOperation


@allure.feature("教室")
@allure.story("测试--使用云盘")
class TestUseYunPanPerf:
    @allure.title('云盘')
    @allure.description("点击云盘")
    def test_click_yunpan(self, get_driver, get_function_name):
        OnlineOpenFilePage().get_ClassroomPage(get_driver)
        OnlineOpenFilePage().get_ToolbarWrapper(get_driver)
        OnlineOpenFilePage().click_yunpan(get_driver)


@allure.feature("教室")
@allure.story("测试--使用文档")
class TestUseWenDangPerf:
    @allure.title('文档')
    @allure.description("点击文档")
    def test_click_wendang(self, get_web_driver, get_function_name):
        get_new_page_special(get_web_driver, "inspector")
        OnlineOpenFilePage().click_wendang(get_web_driver)


@allure.feature("教室")
@allure.story("测试--使用文件夹")
class TestUseTargetFolderPerf:
    @allure.title('文件夹')
    @allure.description("列表视图下，点击文件夹")
    def test_click_target_folder(self, get_web_driver, get_function_name):
        case = get_data('class.yaml')[0]
        OnlineOpenFilePage().click_target_folder(get_web_driver, case['folder_name'])


@allure.feature("教室")
@allure.story("测试--使用文件夹")
class TestUseTargetFolderGrid:
    @allure.title('文件夹')
    @allure.description("网格视图下，点击文件夹")
    def test_click_target_folder_grid(self, get_web_driver, get_function_name):
        case = get_data('class.yaml')[0]
        OnlineOpenFilePage().click_target_folder_grid(get_web_driver, case['folder_name'])


@allure.feature("教室")
@allure.story("测试--使用课件")
class TestOpenFile:
    @allure.title('课件')
    @allure.description("网格视图下，随机点击课件")
    def test_open_files_random_grid(self, get_web_driver, get_driver, get_function_name):
            """打开文件--随机打开一个课件"""
            files = []
            for i in range(stability_conf.online_loop):
                files_list = stability_conf.files
                file = random.choice(files_list)
                file_kind = file.split('.')[1]
                try:
                    logger.info('next step: online classroom open files : {}'.format(file))
                    OnlineOpenFilePage().click_file_grid(get_web_driver, file)
                except Exception as e:
                    logger.error(e)
                else:
                    if file_kind == 'edb':
                        OnlineOpenFilePage().click_clear_blackbord_yes(get_driver)
                        time.sleep(1)
                    if file_kind not in files:
                        files.append(file_kind)
                    continue
                time.sleep(2)
            logger.info("打开的课件是： {}".format(files))
            # 将file_kind存入yaml
            content = get_data('tmp.yaml')[0]
            content['file_kind'] = files
            YamlMethod(get_data('tmp.yaml')[1]).yaml_write(content)
            return files


@allure.feature("教室")
@allure.story("测试--使用课件")
class TestUseTargetFilePerf:
    @allure.title('课件')
    @allure.description("点击pdf课件")
    def test_choose_pdf_file(self, get_web_driver, get_function_name):
        # 点击pdf
        OnlineOpenFilePage().click_target_file_grid(get_web_driver, file_kind='.pdf')
        time.sleep(time_sleep[2] * 6)

    @allure.title('课件')
    @allure.description("点击mp4课件")
    def test_choose_mp4_file(self, get_web_driver, get_function_name):
        # 点击mp4
        OnlineOpenFilePage().click_target_file_grid(get_web_driver, file_kind='.mp4')
        time.sleep(time_sleep[2] * 6)

    @allure.title('课件')
    @allure.description("点击ppt课件")
    def test_choose_ppt_file(self, get_web_driver, get_function_name):
        # 点击ppt
        OnlineOpenFilePage().click_target_file_grid(get_web_driver, file_kind='.ppt')
        time.sleep(time_sleep[2] * 6)


@allure.feature("教室")
@allure.story("测试--使用课件")
class TestMP4PlayPerf:
    @allure.title('课件')
    @allure.description("使用mp4课件")
    def test_use_mp4(self, get_driver, get_function_name):
        MP4Operation().use_mp4(get_driver)

    @allure.title('课件')
    @allure.description("mp4课件点击开始播放")
    def test_start_mp4(self, get_driver, get_function_name):
        MP4Operation().start_mp4(get_driver)
        time.sleep(time_sleep[2] * 6)

    @allure.title('课件')
    @allure.description("mp4课件调整进度条")
    def test_mp4_slider(self, get_driver, get_function_name):
        MP4Operation().click_mp4_slider(get_driver)
        time.sleep(time_sleep[2] * 6)

    @allure.title('课件')
    @allure.description("mp4课件点击循环")
    def test_mp4_loop(self, get_driver, get_function_name):
        MP4Operation().loop_mp4(get_driver)
        time.sleep(time_sleep[2] * 2)


@allure.feature("教室")
@allure.story("测试--使用课件")
class TestPDFOperationPerf:
    @allure.title('课件')
    @allure.description("点击pdf课件")
    def test_use_pdf(self, get_driver, get_function_name):
        PDFOperation().use_pdf(get_driver)

    # @allure.title('课件')
    # @allure.description("pdf课节点击同步滚动")
    # def test_pdf_sync(self, get_driver, get_function_name):
    #     """课节本身默认开启同步滚动"""
    #     PDFOperation().pdf_click_sync(get_driver)
    #     time.sleep(time_sleep[2] * 6)

    @allure.title('课件')
    @allure.description("pdf课件使用pagedown")
    def test_pdf_page_down(self, get_driver, get_function_name):
        PDFOperation().pdf_page_down(get_driver)
        time.sleep(time_sleep[2] * 6)

    @allure.title('课件')
    @allure.description("pdf课件点击下一页")
    def test_pdf_next_page(self, get_driver, get_function_name):
        PDFOperation().pdf_next_page(get_driver)
        time.sleep(time_sleep[2] * 6)

    @allure.title('课件')
    @allure.description("pdf课件点击上一页")
    def test_pdf_prev_page(self, get_driver, get_function_name):
        PDFOperation().pdf_previous_page(get_driver)
        time.sleep(time_sleep[2] * 6)


@allure.feature("教室")
@allure.story("测试--使用课件")
class TestPPTOperationPerf:
    def test_use_ppt(self, get_driver, get_function_name):
        PPTOperation().use_ppt(get_driver)

    @allure.title('课件')
    @allure.description("ppt课件点击下一页")
    def test_ppt_next_page(self, get_driver, get_function_name):
        PPTOperation().ppt_next_page(get_driver)
        time.sleep(time_sleep[2] * 6)

    @allure.title('课件')
    @allure.description("ppt课件点击上一页")
    def test_pdf_prev_page(self, get_driver, get_function_name):
        PPTOperation().ppt_previous_page(get_driver)
        time.sleep(time_sleep[2] * 6)


@allure.feature("教室")
@allure.story("测试--在线教室打开课件")
class TestOpenFiles(object):
    def test_open(self, get_driver):

        OnlineOpenFilePage().get_ClassroomPage(get_driver)

        OnlineOpenFilePage().get_ToolbarWrapper(get_driver)

        OnlineOpenFilePage().click_yunpan(get_driver)

    def test_use_wendang(self, get_web_driver):
        get_new_page_special(get_web_driver, "inspector")
        OnlineOpenFilePage().click_wendang(get_web_driver)

    def test_open_file(self, get_web_driver):
        case = get_data('class.yaml')[0]
        # 点击文件夹
        OnlineOpenFilePage().click_folder(get_web_driver, case['folder_name'])
        # 点击要打开的课件

        files_list = perf_conf.open_files_setting
        print('open:')
        for i in range(len(files_list)):
            print(files_list[i])
            OnlineOpenFilePage().click_file(get_web_driver, files_list[i])
            time.sleep(60)
        time.sleep(90)


class TestOpenFilesClassIn(object):
    def test_open(self, get_driver):

        OnlineOpenFilePage().get_ClassroomPage(get_driver)

        OnlineOpenFilePage().get_ToolbarWrapper(get_driver)

        OnlineOpenFilePage().click_yunpan(get_driver)

    def test_use_wendang(self, get_web_driver):
        OnlineOpenFilePage().click_wendang(get_web_driver)

    def test_open_file(self, get_web_driver):
        case = get_data('class.yaml')[0]
        # 点击文件夹
        OnlineOpenFilePage().click_folder(get_web_driver, case['folder_name'])
        # 点击要打开的课件

        files_list = perf_conf.open_files_setting
        print('open:')
        for i in range(len(files_list)):
            print(files_list[i])
            OnlineOpenFilePage().click_file(get_web_driver, files_list[i])
            time.sleep(60)
        time.sleep(90)





