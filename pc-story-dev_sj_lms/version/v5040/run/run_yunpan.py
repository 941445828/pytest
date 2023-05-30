# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 场景描述： 登录--云盘--创建文件夹
"""
import pytest
import os


if __name__ == "__main__":
    pytest.main(['-vs', '../testcase/test_Login.py', '../testcase/test_yunpan.py', '--alluredir=../testreport/', '--clean-alluredir'])
    os.system("allure generate ../testreport/ --clean")
