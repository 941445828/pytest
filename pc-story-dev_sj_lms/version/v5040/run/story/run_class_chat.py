# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 场景描述: 班级内，发布5000条聊天数据
"""
import pytest
from config import story_conf
from config.updateConf import UpdateConfig


def start_chat():
    UpdateConfig().get_app_version(app=story_conf.APP_URL)
    UpdateConfig().get_login(name=story_conf.LOGIN_USER_NAME, pw=story_conf.LOGIN_PASS_WORD)
    UpdateConfig().get_classname(classname=story_conf.CLASSNAME)

    pytest.main(['-vsq',
                 '../../testcase/test_Login.py',
                 '../../testcase/test_CreateClass.py::TestUseTargetClass',
                 '../../testcase/story/class/test_Send_Chat.py::TestClassSendChat'
    ])


start_chat()