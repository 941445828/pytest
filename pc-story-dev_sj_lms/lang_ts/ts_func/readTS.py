# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 解析多语言ts文件，遍历出节点的’translation‘ text为空  以及attrib是unfinished的
@describe：多语言的source都是英文的，原则上如果翻译后的translation为空，则会去拿source用来显示。
            如果语言版本不是en的，显示成en
"""
import os
import time
import logging
import xml.etree.ElementTree as ET
from lang_ts.common import Log
from lang_ts import common

readTs_logger = Log(file_path=common.project_path + '/log/readTS' + '_' + str(int(time.time())) + ".log", level=logging.INFO, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
zh_file = common.origin_ts_path + '\\lang\\lan\\zh_classin.ts'


# 解析ts文件
# 获取从git拿到本地的ts文件名称、路径
def get_files():
    expect_files_name = os.listdir(common.origin_ts_path + '\lang\lan') # 获取路径下的文件夹和文件名称（不包括子文件、子文件夹）
    # print(expect_files_name)
    expect_files_url = []
    for i in range(len(expect_files_name)):
        expect_files_url.append(common.origin_ts_path + '\\lang\\lan\\' + (expect_files_name[i]))
    # print(expect_files_name, expect_files_url)
    try:
        expect_files_name.sort()
        expect_files_url.sort()
        common.response_files_name.sort()
        assert expect_files_name == common.response_files_name  # 校验从git上拿到的文件和实际所需的文件 名称是否一直，目的在于确认文件不少
    except Exception as msg:
        readTs_logger.error("获取到本地的git文件数量不对！{}".format(msg))
        readTs_logger.error("expect_files_name: {}".format(expect_files_name))
        readTs_logger.error("response_files_name: {}".format(common.response_files_name))
    else:
        return expect_files_name, expect_files_url
expect_files_name = get_files()[0]
expect_files_url = get_files()[1]

def zh_search():  # 查询D:\lang\lang\lan\zh_classin.ts文件里，translation为空的node
    zh_node_none = []
    tree = ET.parse(zh_file)
    root = tree.getroot()
    context = root[0]
    readTs_logger.info("检测文件：{}".format(zh_file))
    for child in context:
        for node in child.iter('translation'):
            if node.text is None:
                zh_node_none.append(child.attrib)
                readTs_logger.info("translation的text显示为空的ID：{}".format(child.attrib))
            if node.attrib == {'type': 'unfinished'}:
                readTs_logger.info("translation的attrib显示为unfinished的ID：{}, {} ".format(child.attrib, node.attrib))
    return zh_node_none   # zh文件中，translation为空的

zh_none_list = zh_search()


def get_content():
    file_count = len(expect_files_name)    # 共几个ts文件
    readTs_logger.info("共获取ts文件{}个".format(file_count))
    for n in range(file_count):
        file_url = expect_files_url[n]  # ts文件路径
        if file_url != zh_file:  # 文件非zh，运行
            readTs_logger.info("检测文件：{}".format(file_url))
            # print("检测文件：{}".format(file_url))
            if file_url != common.origin_ts_path + '\lang\lan' + '\en_classin.ts':  # 文件非en，运行
                try:
                    tree = ET.parse(file_url)
                    root = tree.getroot()
                    context = root[0]
                    # mes = list(context)     # context.getchildren()方法不支持了，改成 list(context)
                    for child in context:
                        # logging.info(child.tag, child.attrib)
                        for node in child.iter('translation'):
                            if node.text is None:
                                if child.attrib not in zh_none_list:
                                    readTs_logger.info("translation的text显示为空的ID：{}".format(child.attrib))
                            if node.attrib == {'type': 'unfinished'}:
                                readTs_logger.info("translation的attrib显示为unfinished的ID：{}, {} ".format(child.attrib, node.attrib))
                except Exception as e:
                    readTs_logger.error("解析文件{}报错！".format(file_url))
            else:
                readTs_logger.info("文件：{} 不需要校验！！！".format(file_url))
                continue

# #  以下，单独运行本脚本
# if __name__ == '__main__':
#     get_content()