# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 读取csv内容
"""


# 读取csv文件内容
def read_data(file_path):
    file = file_path
    with open(file) as f:
        content = f.readlines()
    data_len = len(content)
    data = []
    for i in range(data_len):
        data.append( content[i].split("\n")[0]) # 读取每一行数据，组成一个list
    # print(data)
    return data

# path = 'D:/PC-STORY\csv\cpu_1660290475.csv'
# read_data(path)

