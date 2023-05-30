# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@file: 自动从git获取源码，未新旧文件对比做准备
@describe：
"""


import os
import sys
from git.repo import Repo
from git.repo.fun import is_git_dir
from lang_ts import common
import logging
import time
from lang_ts.common import Log


file_path = os.path.join(common.project_path) + '\log\getTS' + '_' + str(int(time.time())) + ".log"
logger = Log(file_path=file_path, level=logging.INFO, format= '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def move_to_backup():
    """
    将前版本的ts文件，备份到old_lan下，2个版本做对比
    若用本地自己备份的文件，则不需要运行这个方法
    """
    current_os = sys.platform   # 获取当前操作系统
    # print(current_os)
    if current_os == 'win32':
        try:
            move_str = 'move ' + (common.origin_ts_path) + '\lang\lan\* ' + common.old_ts_path # 移动文件夹 更改文件夹名称
            # D:\lang\lang\lan\* D:\lang\lan_old
            logger.info("移动文件夹cmd：{}".format(move_str))
            os.system(move_str)
        except Exception as msg:
            logger.error(msg)
    else:
        logger.info("暂未适配除Windows外的其他系统！")


def clean_folder():
    current_os = sys.platform  # 获取当前操作系统
    # print(current_os)
    if current_os == 'win32':
        try:
            del_str = 'rd /s /q  D:\lang'
            logger.info("删除多余文件：{}".format(del_str))
            os.system(del_str)
        except Exception as msg:
            logger.error(msg)
    else:
        logger.info("暂未适配除Windows外的其他系统！")


class GitRepository(object):
    """
    git仓库管理
    """

    def __init__(self, local_path, repo_url, branch='master'):
        self.local_path = local_path
        self.repo_url = repo_url
        self.repo = None
        self.initial(repo_url, branch)

    def initial(self, repo_url, branch):
        """
        初始化git仓库
        :param repo_url:
        :param branch:
        :return:
        """
        if not os.path.exists(self.local_path):
            os.makedirs(self.local_path)

        git_local_path = os.path.join(self.local_path, '.git')
        if not is_git_dir(git_local_path):
            self.repo = Repo.clone_from(repo_url, to_path=self.local_path, branch=branch)
        else:
            self.repo = Repo(self.local_path)

    # def pull(self):
    #     """
    #     从线上拉最新代码
    #     :return:
    #     """
    #     self.repo.git.pull()
    #
    # def branches(self):
    #     """
    #     获取所有分支
    #     :return:
    #     """
    #     branches = self.repo.remote().refs
    #     return [item.remote_head for item in branches if item.remote_head not in ['HEAD', ]]
    #
    # def commits(self):
    #     """
    #     获取所有提交记录
    #     :return:
    #     """
    #     commit_log = self.repo.git.log('--pretty={"commit":"%h","author":"%an","summary":"%s","date":"%cd"}',
    #                                    max_count=50,
    #                                    date='format:%Y-%m-%d %H:%M')
    #     log_list = commit_log.split("\n")
    #     print(log_list)
    #     return [eval(item) for item in log_list]
    #
    # def tags(self):
    #     """
    #     获取所有tag
    #     :return:
    #     """
    #     return [tag.name for tag in self.repo.tags]
    #
    # def change_to_branch(self, branch):
    #     """
    #     切换分值
    #     :param branch:
    #     :return:
    #     """
    #     self.repo.git.checkout(branch)
    #
    # def change_to_commit(self, branch, commit):
    #     """
    #     切换commit
    #     :param branch:
    #     :param commit:
    #     :return:
    #     """
    #     self.change_to_branch(branch=branch)
    #     self.repo.git.reset('--hard', commit)
    #
    # def change_to_tag(self, tag):
    #     """
    #     切换tag
    #     :param tag:
    #     :return:
    #     """
    #     self.repo.git.checkout(tag)

# #  以下，单独运行本脚本
# if __name__ == '__main__':
#     move_to_backup()
#     clean_folder()
#     local_path = common.origin_ts_path
#     repo = GitRepository(local_path, 'https://gl.eeo.im/classin/lang.git')  # git clone