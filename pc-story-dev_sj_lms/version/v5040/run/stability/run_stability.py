# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File:  稳定性测试，运行集合
        包括：1. 班群--课程--创建: 课堂、录播课、作业、测验、讨论、学习资料、单元主题； 公共复用方法； 查看学生成绩
                编辑: 课堂、录播课、作业、测验、讨论、学习资料
            2. 在线教室，教室内各功能遍历
"""

from version.v5040.run.stability.run_class_course import run_course_activity
from version.v5040.run.stability.run_online_classroom_stability import run_online_classroom


if __name__ == '__main__':
    while True:
        run_course_activity()
        run_online_classroom()