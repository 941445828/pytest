# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: PC  性能测试  相关使用配置
"""
from config.utils import timeStamp


# update-1
"""APP版本号"""
APP_URL = "D:\\classin-win7-2023-05-22_06-40-22-git-4fef4d087-v5.0.3.536\\ClassIn.exe"

# update-2
"""登录用户名和密码"""
LOGIN_USER_NAME = '12112160080'
LOGIN_PASS_WORD = 'e123456'

# update-3
"""将课节创建在此课程下"""
CLASSNAME = 'PERF_TEST'

# update-4
"""是否获取FPS值，填写Y/N，Y=需要获取FPS，N=不需要"""
IS_USE_FPS = 'Y'

"""测试服务器名称"""
server = 'win10'

# WebDriver版本   注：2023/5/10后的版本，一般都是103
WEBDRIVER_VERSION = 103

# 场景名称描述
story_name = '录课模式'

# APP版本号
pc_version = APP_URL.split("\\")[1]

# 性能数据保存--csv文件名称定义
cpu_csv_name = 'cpu_' + story_name + '_' + pc_version + '_' + server + '_' + timeStamp()
mem_csv_name = 'mem_' + story_name + '_' + pc_version + '_' + server + '_' + timeStamp()
fps_csv_name = 'fps_' + story_name + '_' + pc_version + '_' + server + '_' + timeStamp()

# 绘图生成文件名称配置
cpu_png_name = 'cpu_' + story_name + '_' + '_' + server + '_' + timeStamp()
mem_png_name = 'mem_' + story_name + '_' + '_' + server + '_' + timeStamp()
fps_png_name = 'fps_' + story_name + '_' + '_' + server + '_' + timeStamp()

# 打开的文件列表
open_files_setting = ['mp3.mp3', 'pgn.pgn', 'pptx.pptx', 'sgf.sgf', 'eda.eda', 'mp4.mp4']
# open_files_setting = ['声与热.edb', '别董大带声音的ppt.pptx',  '觉醒.flv', '凯叔声律启蒙.mp3', '内部推荐操作指南.pdf', '计数器.edlink']

# 性能收集过程中，使用得打开指定类型文件
target_file = ['.pdf', '.mp4', '.ppt']