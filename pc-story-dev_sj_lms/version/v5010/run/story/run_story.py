# coding = utf-8

""" 场景测试， 统一运行汇总口"""

from version.v5000.run.story.run_class_chat import start_chat
from version.v5000.run.story.run_ts import start_ts


if __name__ == '__main__':
    start_chat()    # 班级中发布5000条聊天数据
    start_ts()      # 多语言