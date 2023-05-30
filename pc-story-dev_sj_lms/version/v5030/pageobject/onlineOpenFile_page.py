# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from version.v5030.pagelocator import onlineOpenFile_locator as OpenFile
from handler.eleHandler import find_element
import time
import random


class OnlineOpenFilePage(object):
    def get_ClassroomPage(self, driver):
        ele = OpenFile.ClassroomPage
        ele_page = find_element(driver, ele[0], ele[1], ele[2])
        return ele_page

    def get_ToolbarWrapper(self, driver):
        ele = OpenFile.ToolbarWrapper
        ele_tools_icon = self.get_ClassroomPage(driver).find_element_by_class_name(ele[2])
        time.sleep(1)
        ele_tools_icon.click()
        return ele_tools_icon

    def click_yunpan(self, driver):
        ele = OpenFile.Tool_YunPan
        ele_yunpan = self.get_ToolbarWrapper(driver).find_elements_by_class_name(ele[2])[7]
        time.sleep(1)
        ele_yunpan.click()

    def click_wendang(self, driver):
        ele = OpenFile.WenDang
        ele_wendang = find_element(driver, ele[0], ele[1], ele[2])
        ele_wendang.click()

    def click_folder(self, driver, folder_name):
        """2023.2.10---云盘更新，此xpath找不到文件夹了"""
        ele_xpath = "//div[contains(text(),'" + folder_name +"')]"
        ele_folder = find_element(driver, '文件夹名称', 'XPath', ele_xpath)
        ele_folder.click()

    def click_target_folder(self, driver, folder_name):
        # 列表视图
        ele = "//div/span[contains(text(),'" + folder_name + "')]"
        ele_folder = find_element(driver, '列表视图下，文件夹名称', 'XPath', ele)
        ele_folder.click()

    def click_target_folder_grid(self, driver, folder_name):
        # 网格视图
        ele = "(//*[div='" + folder_name + "'])[last()]"
        ele_folder = find_element(driver, '网格视图下，文件夹名称', 'XPath', ele)
        ele_folder.click()

    def click_file(self, driver, file):
        """列表视图下，点击文件"""
        if file == 'doc.doc' or file == 'docx.docx':
            # ele = "//div[contains(text(),'" + file.split('.')[0] + "')]"  # """2023.2.10---云盘更新，此xpath找不到文件了"""
            ele = "//div[div/span='" + file.split('.')[0] + "']"
            ele_file = find_element(driver, '要打开的文件:' + file, 'XPaths', ele)[1]
        else:
            # ele = "//div[contains(text(),'" + file.split('.')[0] + "')]" """2023.2.10---云盘更新，此xpath找不到文件了"""
            ele = "//div[div/span='" + file.split('.')[0] + "']"
            ele_file = find_element(driver, '要打开的文件:' + file, 'XPath', ele)
        time.sleep(1)
        ele_file.click()

    def click_file_grid(self, driver, file):
        """网格视图下， 点击文件"""
        if file == 'doc.doc' or file == 'docx.docx':
            ele = "//div[text()='" + file.split('.')[0] + "']"
            ele_file = find_element(driver, '要打开的文件:' + file, 'XPaths', ele)[1]
        else:
            ele =  "//div[text()='" + file.split('.')[0] + "']"
            ele_file = find_element(driver, '要打开的文件:' + file, 'XPath', ele)
        time.sleep(1)
        ele_file.click()

    def click_target_file(self, driver, file_kind):
        """ file_kind传参要求如: .pdf .pm4  """
        # "//div[span='.pdf']"
        # (// div[span='.pdf'])[1]  第一个
        ele_xpath = "//div[span='" + file_kind + "']"
        ele_file = find_element(driver, '打开文件类型：' + file_kind, 'XPaths', ele_xpath)
        ele_file[0].click()

    def click_target_file_grid(self, driver, file_kind):
        """ file_kind传参要求如: .pdf .pm4  """
        # "//div[span='.pdf']"
        # (// div[span='.pdf'])[1]  第一个
        ele_xpath = "(//div[text()='" + file_kind + "'])[last()]"
        ele_file = find_element(driver, '打开文件类型：' + file_kind, 'XPaths', ele_xpath)
        ele_file[0].click()

    def get_clear_blackbord(self, driver):
        ele = OpenFile.EeoMessageBox
        ele_box = find_element(driver, ele[0], ele[1], ele[2])
        return ele_box

    def click_clear_blackbord_yes(self, driver):
        ele = OpenFile.EeoMessageBox_Yes
        ele_yes = self.get_clear_blackbord(driver).find_elements_by_class_name(ele[2])[0]
        time.sleep(1)
        ele_yes.click()

    def click_clear_blackbord_no(self, driver):
        ele = OpenFile.EeoMessageBox_No
        ele_no = self.get_clear_blackbord(driver).find_elements_by_class_name(ele[2])[1]
        time.sleep(1)
        ele_no.click()


class OnlineCloseFilePage(object):
    def close_pptx(self, driver):
        ele = OpenFile.H5PptWidget
        ele_whole = find_element(driver, ele[0], ele[1], ele[2])[0]
        ele_whole.click()
        ele_title = OpenFile.H5PptWidget_title
        ele_title_click = ele_whole.find_elements_by_class_name(ele_title[2])[0]
        time.sleep(1)
        ele_title_click.click()
        ele_close_btn = OpenFile.H5PptWidget_close_btn
        ele_close_click = ele_title_click.find_elements_by_class_name(ele_close_btn[2])[2]
        time.sleep(1)
        ele_close_click.click()

    def close_excel(self, driver):
        ele = OpenFile.ExcelShowWidget
        ele_whole =  find_element(driver, ele[0], ele[1], ele[2])[0]
        ele_whole.click()
        ele_title = OpenFile.ExcelShowWidget_title
        ele_title_click = ele_whole.find_elements_by_class_name(ele_title[2])[0]
        time.sleep(1)
        ele_title_click.click()
        ele_close_btn = OpenFile.ExcelShowWidget_close_btn
        ele_close_click = ele_title_click.find_elements_by_class_name(ele_close_btn[2])[2]
        time.sleep(1)
        ele_close_click.click()


    def close_pdf(self, driver):
        ele = OpenFile.QtPdfShowWidget
        ele_whole =  find_element(driver, ele[0], ele[1], ele[2])[0]
        ele_whole.click()
        ele_title = OpenFile.QtPdfShowWidget_title
        ele_title_click = ele_whole.find_elements_by_class_name(ele_title[2])[0]
        time.sleep(1)
        ele_title_click.click()
        ele_close_btn = OpenFile.QtPdfShowWidget_close_btn
        ele_close_click = ele_title_click.find_elements_by_class_name(ele_close_btn[2])[2]
        time.sleep(1)
        ele_close_click.click()

    def close_eda(self, driver):
        ele = OpenFile.EdaWidget
        ele_whole =  find_element(driver, ele[0], ele[1], ele[2])[0]
        ele_whole.click()
        ele_title = OpenFile.EdaWidget_title
        ele_title_click = ele_whole.find_elements_by_class_name(ele_title[2])[0]
        time.sleep(1)
        ele_title_click.click()
        ele_close_btn = OpenFile.EdaWidget_close_btn
        ele_close_click = ele_title_click.find_elements_by_class_name(ele_close_btn[2])[2]
        time.sleep(1)
        ele_close_click.click()

    def close_avaudio(self, driver):
        ele = OpenFile.QtAVAudioShowWidget
        ele_whole =  find_element(driver, ele[0], ele[1], ele[2])[0]
        ele_whole.click()
        ele_title = OpenFile.QtAVAudioShowWidget_title
        ele_title_click = ele_whole.find_elements_by_class_name(ele_title[2])[0]
        time.sleep(1)
        ele_title_click.click()
        ele_close_btn = OpenFile.QtAVAudioShowWidget_close_btn
        ele_close_click = ele_title_click.find_elements_by_class_name(ele_close_btn[2])[2]
        time.sleep(1)
        ele_close_click.click()


    def close_avvideo(self, driver):
        ele = OpenFile.QtAVVideoShowWidget
        ele_whole =  find_element(driver, ele[0], ele[1], ele[2])[0]
        ele_whole.click()
        ele_title = OpenFile.QtAVVideoShowWidget_title
        ele_title_click = ele_whole.find_elements_by_class_name(ele_title[2])[0]
        time.sleep(1)
        ele_title_click.click()
        ele_close_btn = OpenFile.QtAVVideoShowWidget_close_btn
        ele_close_click = ele_title_click.find_elements_by_class_name(ele_close_btn[2])[2]
        time.sleep(1)
        ele_close_click.click()


    def close_codeeditor(self, driver):
        ele = OpenFile.CodeEditorWidget
        ele_whole =  find_element(driver, ele[0], ele[1], ele[2])[0]
        ele_whole.click()
        ele_title = OpenFile.CodeEditorWidget_title
        ele_title_click = ele_whole.find_elements_by_class_name(ele_title[2])[0]
        time.sleep(1)
        ele_title_click.click()
        ele_close_btn = OpenFile.CodeEditorWidget_close_btn
        ele_close_click = ele_title_click.find_elements_by_class_name(ele_close_btn[2])[2]
        time.sleep(1)
        ele_close_click.click()


class MP4Operation:
    def get_mp4s(self, driver):
        # 获取当前教室内打开的所有视频类的文件
        ele = OpenFile.QtAVVideoShowWidget
        ele_mp4s = find_element(driver, ele[0], ele[1], ele[2])
        return ele_mp4s

    def use_mp4(self, driver):
        ele = OpenFile.QtAVVideoShowWidget
        # ele_mp4s = find_element(driver, ele[0], ele[1], ele[2])
        mp4 = random.choice(find_element(driver, ele[0], ele[1], ele[2]))
        mp4.click()
        return mp4

    def start_mp4(self, driver):
        ele = OpenFile.mp4_start
        ele_start = self.use_mp4(driver).find_element_by_xpath(ele[2])
        ele_start.click()

    def click_mp4_slider(self, driver):
        ele = OpenFile.mp4_slider
        ele_slider = self.use_mp4(driver).find_element_by_xpath(ele[2])
        ele_slider.click()

    def stop_mp4(self, driver):
        ele = OpenFile.mp4_start
        ele_start = self.use_mp4(driver).find_element_by_xpath(ele[2])
        ele_start.click()

    def loop_mp4(self, driver):
        ele = OpenFile.mp4_loop_btn
        ele_start = self.use_mp4(driver).find_element_by_xpath(ele[2])
        ele_start.click()


class MP3Operation:
    def get_mp3s(self, driver):
        # 获取当前教室内打开的所有视频类的文件
        ele = OpenFile.QtAVAudioShowWidget
        ele_mp3s = find_element(driver, ele[0], ele[1], ele[2])
        return ele_mp3s

    def use_mp3(self, driver):
        ele = OpenFile.QtAVAudioShowWidget
        # ele_mp4s = find_element(driver, ele[0], ele[1], ele[2])
        mp3 = random.choice(find_element(driver, ele[0], ele[1], ele[2]))
        # print(mp3)
        mp3.click()
        return mp3

    def start_mp3(self, driver):
        ele = OpenFile.mp3_start
        ele_start = self.use_mp3(driver).find_element_by_xpath(ele[2])
        ele_start.click()

    def click_mp3_slider(self, driver):
        ele = OpenFile.mp3_slider
        ele_slider = self.use_mp3(driver).find_element_by_xpath(ele[2])
        ele_slider.click()

    def stop_mp3(self, driver):
        ele = OpenFile.mp3_start
        ele_start = self.use_mp3(driver).find_element_by_xpath(ele[2])
        ele_start.click()


class PDFOperation:
    def get_pdfs(self, driver):
        ele = OpenFile.QtPdfShowWidget
        ele_pdfs = find_element(driver, ele[0], ele[1], ele[2])
        return ele_pdfs

    def use_pdf(self, driver):
        ele = OpenFile.QtPdfShowWidget
        pdf = random.choice(find_element(driver, ele[0], ele[1], ele[2]))
        pdf.click()
        return pdf

    def pdf_click_sync(self, driver): # pdf默认打开‘同步滚动’
        ele = OpenFile.pdf_sync
        ele_sync = self.use_pdf(driver).find_element_by_name(ele[2])
        ele_sync.click()

    def pdf_page_down(self, driver):
        for i in range(5):
            ele = OpenFile.pdf_page
            ele_page = self.use_pdf(driver).find_element_by_xpath(ele[2])
            ele_page.click()
            ActionChains(driver).key_down(Keys.PAGE_DOWN).perform()

    def pdf_use_scroll(self, driver):  # 元素pdf 定位在元素中间位置  不能拖动
        ele = OpenFile.pdf_scroll
        ele_scroll = self.use_pdf(driver).find_element_by_xpath(ele[2])
        # ele_scroll.click()
        ActionChains(driver).drag_and_drop_by_offset(ele_scroll, 0, 30).perform()

    def pdf_previous_page(self, driver):
        for i in range(5):
            ele = OpenFile.pdf_previous_page
            ele_prev_page = self.use_pdf(driver).find_element_by_xpath(ele[2])
            ele_prev_page.click()

    def pdf_next_page(self, driver):
        for i in range(5):
            ele = OpenFile.pdf_next_page
            ele_next_page = self.use_pdf(driver).find_element_by_xpath(ele[2])
            ele_next_page.click()


class PPTOperation:
    def get_ppts(self, driver):
        ele = OpenFile.H5PptWidget
        ele_ppts = find_element(driver, ele[0], ele[1], ele[2])
        return ele_ppts

    def use_ppt(self, driver):
        ele = OpenFile.H5PptWidget
        ppt = random.choice(find_element(driver, ele[0], ele[1], ele[2]))
        ppt.click()
        return ppt

    def ppt_previous_page(self, driver):
        for i in range(5):
            ele = OpenFile.ppt_previous_page
            ele_prev_page = self.use_ppt(driver).find_element_by_xpath(ele[2])
            ele_prev_page.click()

    def ppt_next_page(self, driver):
        for i in range(5):
            ele = OpenFile.ppt_next_page
            ele_next_page = self.use_ppt(driver).find_element_by_xpath(ele[2])
            ele_next_page.click()












"""
edb:    板书，无需关闭课件
png:    无需关闭
csv:    ExcelShowWidget
xlsx：   ExcelShowWidget
doc:    QtPdfShowWidget
docx:   QtPdfShowWidget
epub：  QtPdfShowWidget
pdf:    QtPdfShowWidget
eda:    EdaWidget
pgn:    EdaWidget
sgf：    EdaWidget
mp3：    QtAVAudioShowWidget
mp4：    QtAVVideoShowWidget
pptx：   H5PptWidget
txt：    CodeEditorWidget
"""