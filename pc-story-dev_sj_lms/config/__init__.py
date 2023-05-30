# # coding = utf-8
import os
import datetime
import time


"""
项目 根目录地址
"""
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(PROJECT_DIR)

"""
webview driver 
"""
WEB_DRIVER_URL =  PROJECT_DIR + '\\tools\\' + '\\chromedriver-84.exe'
WEB_DRIVER_103 =  PROJECT_DIR + '\\tools\\' + '\\chromedriver-103.exe'

# print(WEB_DRIVER_URL)
INSPECT_URL = "127.0.0.1:7777"

"""
日志相关配置
"""
now = str(datetime.datetime.now()).split('.')[0]
LOG_FILE_URL = PROJECT_DIR + '\\testlog\\' + str(datetime.date.today()) + '_' + str(int(time.time())) +  '.log'
LOG_NAME = "ClassIn-PC-STORY"
LOG_SET_LEVEL = "DEBUG"
LOG_FORMAT = '%(asctime)s-%(levelname)s-%(filename)s - %(lineno)d - %(message)s'


# sleep time配置，单位s
time_sleep = [1, 2, 5]