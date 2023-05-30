# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 方法:绘制图表
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from functs.readCSV import read_data
from config import utils
import os


# 统计，要绘入图的所有文件
def get_files(folder_path, search_file):
    file_list = []
    files = os.listdir(folder_path)
    # print(files)
    for file in files:
        cur_path = os.path.join(folder_path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            get_files(cur_path, search_file)
        else:
            # 判断是否是需要的文件
            if search_file in file:
                file = folder_path + file
                file_list.append(file)
    # print(file_list)
    return file_list


# 绘图
def draw_chart(path, search, png_name):
    files = get_files(path, search)
    files_count = len(files)
    fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
    for i in range(files_count):
        file_url = get_files(path, search)[i]
        x_len = len(read_data(files[i]))
        x = np.arange(1, x_len+1)
        y = []
        file = read_data(files[i])
        # print(file)
        for j in range(len(file)):
            if 'cpu' in search:
                y.append(float(file[j].split(',')[0].rsplit('%')[0]))
            elif 'mem' in search:
                if '%' in file[j].split(',')[0]:
                    y.append(float(file[j].split(',')[0].rsplit('%')[0]))
                else:
                    y.append(float(file[j].split(',')[0].rsplit('MB')[0]))
            elif 'fps' in search:
                print(file[j].split(',')[0])
                y.append(file[j].split(',')[0])

        ax.plot(x, y, label=file_url)
    if 'cpu' in search:
        ax.set_ylabel('cpu使用率 %')
        ax.set_title('CPU使用情况')
    elif 'mem' in search:
        ax.set_ylabel('内存占用量 MB')
        ax.set_title('内存使用情况')
    elif 'fps' in search:
        ax.set_ylabel('FPS值')
        ax.set_title('FPS使用情况')
    matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
    plt.rc('axes', unicode_minus=False)
    ax.set_xlabel('请求次数（2S/次）')
    ax.legend()
    if 'cpu' in search:
        plt.savefig(utils.get_cpu_png_url(png_name))
    elif 'mem' in search:
        plt.savefig(utils.get_mem_png_url(png_name))
    elif 'fps' in search:
        plt.savefig(utils.get_fps_png_url(png_name))
    # plt.show()  # 注销掉之后, 不弹图片
