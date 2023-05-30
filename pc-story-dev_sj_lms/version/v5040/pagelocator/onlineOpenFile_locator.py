# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""

# 定位教室
ClassroomPage = ('ClassroomPage', 'ClassName', 'ClassroomPage')

# 定位右侧操作栏
ToolbarWrapper = ('ToolbarWrapper', 'ClassName', 'ToolbarWrapper')

# 定位‘云盘’
Tool_YunPan = ('云盘icon', 'ClassNames', 'ButtonInVerticalToolBar')

# H5--定位‘文档’
WenDang = ('文档', 'XPath', "//div[span='文档']")

# 清空黑板内容的提示框--打开edb文件后有这个提示
EeoMessageBox = ('清空黑板内容的提示框', 'ClassName', 'EeoMessageBox')
EeoMessageBox_Yes = ('清空黑板内容的提示框--是', 'ClassNames', 'QPushButton')
EeoMessageBox_No = ('清空黑板内容的提示框--否', 'ClassNames', 'QPushButton')


# PPTX课件，关闭
H5PptWidget = ('PPTX课件整体', 'ClassNames', 'H5PptWidget')
H5PptWidget_title = ('PPTX课件-title部分', 'ClassNames', 'QWidget')
H5PptWidget_close_btn = ('PPTX课件-关闭btn', 'ClassNames', 'QToolButton')


# CSV\XLSX 课件，关闭
ExcelShowWidget = ('CSV、XLSX课件整体', 'ClassNames', 'ExcelShowWidget')
ExcelShowWidget_title = ('PPTX课件-title部分', 'ClassNames', 'QWidget')
ExcelShowWidget_close_btn = ('PPTX课件-关闭btn', 'ClassNames', 'QToolButton')


# doc\docx\epub\pdf 课件，关闭
QtPdfShowWidget = ('doc、docx、epub、pdf 课件整体', 'ClassNames', 'QtPdfShowWidget')
QtPdfShowWidget_title = ('doc、docx、epub、pdf 课件-title部分', 'ClassNames', 'QWidget')
QtPdfShowWidget_close_btn = ('doc、docx、epub、pdf 课件-关闭btn', 'ClassNames', 'QToolButton')


# eda、pgn、sgf 课件，关闭
EdaWidget = ('eda、pgn、sgf 课件整体', 'ClassNames', 'EdaWidget')
EdaWidget_title = ('eda、pgn、sgf 课件-title部分', 'ClassNames', 'QWidget')
EdaWidget_close_btn = ('eda、pgn、sgf 课件-关闭btn', 'ClassNames', 'QToolButton')


# mp3 课件，关闭
QtAVAudioShowWidget = ('mp3 课件整体', 'ClassNames', 'QtAVAudioShowWidget')
QtAVAudioShowWidget_title = ('mp3 课件-title部分', 'ClassNames', 'QWidget')
QtAVAudioShowWidget_close_btn = ('mp3 课件-关闭btn', 'ClassNames', 'QToolButton')


# mp4 课件，关闭
QtAVVideoShowWidget = ('mp4 课件整体', 'ClassNames', 'QtAVVideoShowWidget')
QtAVVideoShowWidget_title = ('mp4 课件-title部分', 'ClassNames', 'QWidget')
QtAVVideoShowWidget_close_btn = ('mp4 课件-关闭btn', 'ClassNames', 'QToolButton')


# txt 课件，关闭
CodeEditorWidget = ('txt 课件整体', 'ClassNames', 'CodeEditorWidget')
CodeEditorWidget_title = ('txt 课件-title部分', 'ClassNames', 'QWidget')
CodeEditorWidget_close_btn = ('txt 课件-关闭btn', 'ClassNames', 'QToolButton')


# 视频类文件的相关操作
mp4_start = ('视频文件的开始/暂停按钮', 'XPath', "(((((//*[@ClassName='QWidget'])[1])/*[@ClassName='QWidget'])[3])/*[@ClassName='QToolButton'])[1]")
mp4_slider = ('视频文件进度条', 'XPath', "((((//*[@ClassName='QWidget'])[1])/*[@ClassName='QWidget'])[3])/*[@ClassName='QSlider']")
mp4_loop_btn = ('视频文件循环btn', 'XPath', "(((((//*[@ClassName='QWidget'])[1])/*[@ClassName='QWidget'])[3])/*[@ClassName='QToolButton'])[2]")
mp4_close = ('视频文件关闭btn', 'XPath', "(((((//*[@ClassName='QWidget'])[1])/*[@ClassName='QWidget'])[1])/*[@ClassName='QToolButton'])[3]")

# 音频类操作
mp3_start = ('音频文件的开始/暂停按钮', 'XPath', "((((//*[@ClassName='QWidget'])[1])/*[@ClassName='QWidget'])[2])/*[@ClassName='QWidget']/*[@ClassName='QWidget']/*[@ClassName='QToolButton']")
mp3_slider = ('音频文件进度条', 'XPath', "((((//*[@ClassName='QWidget'])[1])/*[@ClassName='QWidget'])[2])/*[@ClassName='QWidget']/*[@ClassName='QSlider']")

# pdf类操作
pdf_sync = ('pdf 同步滚动', 'Name', '同步滚动')
pdf_scroll = ('pdf 滚动条', 'XPath', "((//*[@ClassName='QWidget']/*[@ClassName='PdfControlForm']/*[@ClassName='QStackedWidget'])[1]/*[@ClassName='QWidget']/*[@ClassName='QScrollArea']/*[@ClassName='QWidget'])[2]/*[@ClassName='QScrollBar']")
pdf_page = ('pdf page', 'XPath', "((//*[@ClassName='QWidget']/*[@ClassName='PdfControlForm']/*[@ClassName='QStackedWidget'])[1]/*[@ClassName='QWidget']/*[@ClassName='QScrollArea']/*[@ClassName='QWidget'])[1]")
pdf_previous_page =  ('pdf 上一页', 'XPath', "(((//*[@ClassName='QWidget']/*[@ClassName='PdfControlForm']/*[@ClassName='QStackedWidget'])[2]/*[@ClassName='QWidget']/*[@ClassName='QWidget']/*[@ClassName='QWidget'])[2]/*[@ClassName='QToolButton'])[1]")
pdf_next_page = ('pdf 下一页', 'XPath', "(((//*[@ClassName='QWidget']/*[@ClassName='PdfControlForm']/*[@ClassName='QStackedWidget'])[2]/*[@ClassName='QWidget']/*[@ClassName='QWidget']/*[@ClassName='QWidget'])[2]/*[@ClassName='QToolButton'])[2]")

# ppt类操作
ppt_previous_page = ('ppt 上一页', 'XPath', "((//*[@ClassName='QWidget']/*[@ClassName='H5PptContentForm']/*[@ClassName='QStackedWidget']/*[@ClassName='QWidget']/*[@ClassName='QWidget']/*[@ClassName='QWidget'])[2]/*[@ClassName='QToolButton'])[1]")
ppt_next_page = ('ppt 下一页', 'XPath', "((//*[@ClassName='QWidget']/*[@ClassName='H5PptContentForm']/*[@ClassName='QStackedWidget']/*[@ClassName='QWidget']/*[@ClassName='QWidget']/*[@ClassName='QWidget'])[2]/*[@ClassName='QToolButton'])[3]")
ppt_middle = ('ppt 下一页', 'XPath', "((//*[@ClassName='QWidget']/*[@ClassName='H5PptContentForm']/*[@ClassName='QStackedWidget']/*[@ClassName='QWidget']/*[@ClassName='QWidget']/*[@ClassName='QWidget'])[2]/*[@ClassName='QToolButton'])[2]")