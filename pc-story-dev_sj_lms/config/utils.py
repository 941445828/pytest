import time
from config import *
import pyperclip
import pyautogui

"""
获取时间戳
"""
def timeStamp():
    timestamp = str(int(time.time()))
    # print(timestamp)
    return timestamp
# timeStamp()

"""
获取当前时间点
"""
def now_time():
    now = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d_%H:%M:%S')
    # print(now)
    return now
# now_time()

"""
文件地址: 收集cpu mem存放的csv  绘图生成的png
"""
def get_cpu_csv_url(name):
    cpu_file_url = PROJECT_DIR + '\\csv\\' + str(name) + '.csv'
    return cpu_file_url

def get_mem_csv_url(name):
    cpu_file_url = PROJECT_DIR + '\\csv\\' + str(name) + '.csv'
    return cpu_file_url

def get_cpu_png_url(name):
    draw_png_url = PROJECT_DIR + '\\chart\\' + str(name) + '.png'
    return draw_png_url

def get_mem_png_url(name):
    draw_png_url = PROJECT_DIR + '\\chart\\' + str(name) + '.png'
    return draw_png_url

def get_fps_csv_url(name):
    fps_file_url = PROJECT_DIR + '\\csv\\' + str(name) + '.csv'
    return fps_file_url

def get_fps_png_url(name):
    draw_png_url = PROJECT_DIR + '\\chart\\' + str(name) + '.png'
    return draw_png_url


def copy_paste(content):
    """复制粘贴"""
    pyperclip.copy(content)
    pyautogui.hotkey('ctrl', 'v')