# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
import pytest


if __name__ == '__main__':
    pytest.main(['-vs',
                 # '../../testcase/test_Login.py',
                 '../../testcase/test_CreateClass.py::TestUseTargetClass',
                 '../../testcase/test_CreateClass.py::TestChangeCourseTab',
                 '../../testcase/test_AddOnlineCourse.py::TestEnterClassRoom',  #  进入教室内
                 '../../testcase/perf/test_GetFPS.py'
                 ])
