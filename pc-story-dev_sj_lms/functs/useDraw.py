# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:  给场景性能输入，执行绘图
"""

from config.perf_conf import cpu_png_name, mem_png_name, fps_png_name
from config import perf_conf
from functs.drawPic import draw_chart
from config import *


def use_draw():
    # 绘图
    search_key_cpu = 'cpu_' + perf_conf.story_name      # 根据场景名称搜索
    search_key_mem = 'mem_' + perf_conf.story_name
    search_key_fps = 'fps_' + perf_conf.story_name
    draw_chart(PROJECT_DIR + '\\csv\\', search_key_cpu, cpu_png_name)      # 自定义图片名字
    draw_chart(PROJECT_DIR + '\\csv\\', search_key_mem, mem_png_name)      # 自定义图片名字
    draw_chart(PROJECT_DIR + '\\csv\\', search_key_fps, fps_png_name)


use_draw()