# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""

import yaml
from config import *
from handler.logHandler import logger


class YamlMethod:
    def __init__(self, file):
        self.file = file

    def yaml_read(self):
        with open(self.file, 'r+', encoding='utf8') as file:
            data_read = yaml.load(file, Loader=yaml.FullLoader)
        file.close()
        return data_read

    def yaml_write(self, edit):
        with open(self.file, 'w+', encoding='utf8') as file:
            yaml.dump(edit, file, allow_unicode=True)
        file.close()


def get_data(yaml_file_name):
    # print(config.ROOT_URL)
    file_path = PROJECT_DIR + '\\data\\' + yaml_file_name
    # print(file_path)
    yaml_data = YamlMethod(file_path).yaml_read()
    if len(yaml_data) <= 0:
        logger.error('yaml文件：{} 不存在或是空文档'.format(file_path))
    return yaml_data, file_path    # return2个参数,是个元组,第一个参数是读取后的数据，第二个参数url地址

# get_data('login.yaml')
