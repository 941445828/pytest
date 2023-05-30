# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File: 作业-批阅-留痕验证
"""
import pytest
from config import story_conf
from config.updateConf import UpdateConfig

if __name__ == "__main__":
    UpdateConfig().get_app_version(app=story_conf.APP_URL)
    UpdateConfig().get_login(name=story_conf.LOGIN_USER_NAME, pw=story_conf.LOGIN_PASS_WORD)
    UpdateConfig().get_classname(classname=story_conf.CLASSNAME)
    pytest.main(['-vs',
                 '../../testcase/test_Login.py',
                 '../../testcase/story/homework/test_HomeworkReviewAll.py'
                 ])
