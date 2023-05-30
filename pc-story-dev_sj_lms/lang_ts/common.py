# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
import logging
import os


# logger
class Log(logging.Logger):
    def __init__(self, name=None, file_path=None, level=None, format=None):
        super(Log, self).__init__(name)
        file = logging.FileHandler(file_path, encoding='utf-8', mode='a')
        file.setLevel(level)
        fmt = logging.Formatter(format)
        file.setFormatter(fmt)
        self.addHandler(file)
# logger = Log(name='readXML', file_path="D:/readXML_"+str(int(time.time()))+".log", level=logging.INFO, format= '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


# 定义
project_path = os.path.abspath(os.path.dirname(__file__))    # 本项目路径
# print(project_path) # D:\PC\lang_ts
repo_git = 'https://gl.eeo.im/classin/lang.git'  # ts远程仓
origin_ts_path = 'D:\lang'   # 从git取到的ts源文件存放地址
# print(origin_ts_path) # D:\lang
old_ts_path = 'D:\lan_old'
# print(old_ts_path)  # D:\lang


# 定义实际需要存在的文件名称
response_files_name = ['ar_classin.ts', 'en_classin.ts', 'es_classin.ts', 'fr_classin.ts', 'id_classin.ts', 'ja_classin.ts', 'ko_classin.ts', 'pt_classin.ts', 'ru_classin.ts', 'vi_classin.ts', 'zh_classin.ts']
