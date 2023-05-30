# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
import xml.etree.ElementTree as ET
from lang_ts import common
import os
import logging
import time
from lang_ts.common import Log


compare_logger = Log(file_path=common.project_path + '/log/compare' + '_' + str(int(time.time())) + ".log", level=logging.INFO, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
new_files_url = []
old_files_url = []
file_name = []
new_files_name = os.listdir(common.origin_ts_path + '\\lang\\lan')  # 获取new文件名称
# print(new_files_name)
old_files_name = os.listdir(common.old_ts_path)     # 获取old文件名称
# print(old_files_name)
count_new = len(new_files_name)     # 获取new文件数量
count_old = len(old_files_name)     # 获取old文件数量
file = {'ar_classin.ts': '阿拉伯语', 'en_classin.ts': '英语', 'es_classin.ts': '西班牙语', 'fr_classin.ts': '法语', 'id_classin.ts': '印尼语', 'ja_classin.ts': '日语',
        'ko_classin.ts': '韩语', 'pt_classin.ts': '葡萄牙语', 'ru_classin.ts': '俄语', 'vi_classin.ts': '越南语', 'zh_classin.ts': '中文简体'}


def get_file():
    """
    获取新、旧文件 绝对路径，并返回
    :return:
    """
    if new_files_name == old_files_name:
        try:
            for x in range(count_new):
                new_files_url.append(common.origin_ts_path + '\lang\lan' + '\\' + new_files_name[x])
                old_files_url.append(common.old_ts_path + '\\' + old_files_name[x])
                file_name.append(new_files_name[x])
            # print(new_files_url)
            # print(old_files_url)
            # print(file_name)
        except Exception as e:
            compare_logger.error(e)
    else:
        compare_logger.error("新旧lan ts文件数量不一致！")
    return new_files_url, old_files_url, file_name     # 返回新、旧文件绝对路径
# get_file()


def get_file_content(file_url):
    """
    获取新、旧文件内容
    :param file_url: ts文件地址
    :return:
    file_content: 数据格式set  {'ID': ['source', 'translation', 'oldsource']}
    list_count: file_content集合长度int
    keys: 集合keys[]
    values: 集合values[]
    """
    # 解析文件1
    file_content = dict()
    tree = ET.ElementTree(file=file_url)
    root = tree.getroot()
    context = root[0]
    len_child = len(list(context))
    for i in range(1, len_child):
        value = []
        id = context[i].attrib.get('id')
        for node_source in context[i].iter('source'):
            source = node_source.text
            # print(source)
            value.append(source)
        for node_translation in context[i].iter('translation'):
            translation = node_translation.text
            # print(translation)
            value.append(translation)
        for node_oldsource in context[i].iter('oldsource'):
            oldsource = node_oldsource.text
            # print(oldsource)
            value.append(oldsource)
        file_content[id] = value
    # print(file_content)
    list_count = len(file_content)
    keys = list(file_content.keys())
    values = list(file_content.values())
    # print(keys)
    # print(values)
    return file_content, list_count, keys, values   # 返回文件内容、集合长度、keys、values
# get_file_content('D:\lang\lang\lan\en_classin.ts')[0]


def compare():
    if count_new == count_old:
        add_key_value = []      # 对比后的新增内容，只在新文件里
        delete_key_value = []   # 对比后删除的内容，只在旧文件里
        update_key_value = []   # 对比后更新的内容，key一致，value更新
        for y in range(count_new):
            file_new_content = get_file_content(get_file()[0][y])[0]    # 新文件--内容
            # print(file_new_content)
            file_old_content = get_file_content(get_file()[1][y])[0]    # 旧文件--内容
            # print(file_old_content)
            file_new_list_count = get_file_content(get_file()[0][y])[1] # 新文件--长度
            # print(file_new_list_count)
            file_old_list_count = get_file_content(get_file()[1][y])[1] # 旧文件--长度
            # print(file_old_list_count)
            file_new_content_keys = get_file_content(get_file()[0][y])[2]   # 新文件--keys
            # print(file_new_content_keys)
            file_old_content_keys = get_file_content(get_file()[1][y])[2]   # 旧文件--keys
            # print(file_old_content_keys)
            file_new_content_values = get_file_content(get_file()[0][y])[3] # 新文件--values
            # print(file_new_content_values)
            file_old_content_values = get_file_content(get_file()[1][y])[3] # 旧文件--values
            # print(file_old_content_values)
            if file_new_content == file_old_content:
                compare_logger.info("{} 新、旧文件内容完全一致！".format(get_file()[0][y]))
            else:
                try:
                    for n in range(file_new_list_count):    # 新增的
                        if file_new_content_keys[n] not in file_old_content_keys:
                            add_key_value.append({file_new_content_keys[n]: file_new_content_values[n]})
                    for o in range(file_old_list_count):    # 删除的
                        if file_old_content_keys[o] not in file_new_content_keys:
                            delete_key_value.append({file_old_content_keys[o]: file_old_content_values[0]})
                    for diff in range(file_new_list_count): # 更新的
                        if file_new_content_keys[diff] in file_old_content_keys and file_new_content.get(file_new_content_keys[diff]) != file_old_content.get(file_new_content_keys[diff]):
                            update_key_value.append({file_new_content_keys[diff]: file_new_content_values[diff]})
                except Exception as e:
                    compare_logger.error(e)
                else:
                    if file_name[y] == ((get_file()[0][y]).split('\\'))[-1]:
                        compare_logger.info("{}: {}".format(file.get(file_name[y]), get_file()[0][y]))
                        compare_logger.info("新增：")
                        compare_logger.info( ', \n'.join(str(add_key_value).split('},')))
                        compare_logger.info("删除：")
                        compare_logger.info( ', \n'.join(str(delete_key_value).split('},')))
                        compare_logger.info("更新：")
                        compare_logger.info( ', \n'.join(str(update_key_value).split('},')))
    else:
        compare_logger.error("新旧lan ts文件数量不一致！")

#  以下，单独运行本脚本
# if __name__ == '__main__':
#     compare()