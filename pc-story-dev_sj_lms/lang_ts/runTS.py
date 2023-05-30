# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from lang_ts.ts_func import readTS, getTS, compare
from lang_ts import common

if __name__ == '__main__':
    # 更新git文件:
    getTS.move_to_backup() # 若用本地自己备份的文件，则不需要运行这个方法
    getTS.clean_folder()
    local_path = common.origin_ts_path
    repo = getTS.GitRepository(local_path, common.repo_git)  #  git clone

    # 查找value空&unfinished的元素
    readTS.get_content() #

    # 对比新旧文件不同
    compare.compare()

