import time
import os


def get_new_page_special(driver, url):
    time.sleep(2)
    # print(get_web_driver.current_window_handle)  # 输出当前窗口句柄， 这句不要了
    handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
    # print(handles)  # 输出句柄集合
    for handle in handles:  # 切换窗口
        driver.switch_to.window(handle)
        time.sleep(3)
        if url in driver.current_url:
            # print(driver.current_url)
            break


# 版本路径
root_dir = os.path.dirname(os.path.abspath(__file__))
# print(root_dir)  #  D:\PC-STORY\version\v5000
