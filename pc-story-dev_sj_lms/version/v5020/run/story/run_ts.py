# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 场景描述: 登录--切换多语言，验证”设置“显示的是否是对应语言的内容
"""
import pytest
import os
from config import story_conf
from config.updateConf import UpdateConfig

# if __name__ == "__main__":
#     for i in range(12):
#         pytest.main(['-vs', '../testcase/test_Login.py', '../testcase/test_ts.py', '../testcase/test_QuitAPP.py', '--alluredir=testreport/', '--clean-alluredir'])
#         os.system("allure generate testreport/ --clean")


def start_ts():
    UpdateConfig().get_app_version(app=story_conf.APP_URL)
    UpdateConfig().get_login(name=story_conf.LOGIN_USER_NAME, pw=story_conf.LOGIN_PASS_WORD)
    UpdateConfig().get_classname(classname=story_conf.CLASSNAME)
    for i in range(12):
        pytest.main(['-vs',
                     '../../testcase/test_Login.py',
                     '../../testcase/test_ts.py',
                     '../../testcase/test_QuitAPP.py',
                     '--alluredir=testreport/',
                     '--clean-alluredir'])


start_ts()