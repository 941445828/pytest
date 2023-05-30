# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 收集cpu\mem
"""
import csv
import time
import psutil
from functs.getPid import get_pid
from config import utils
from handler.logHandler import logger


class Collect:
# 收集mem、cpu
    def collect(self, cpu_file_url, mem_file_url):
        try:
            while True:
                pid = get_pid()
                logger.info('PID={}'.format(pid))
                if pid is not None:
                    p = psutil.Process(int(pid))
                    # cpu
                    cpu_pid = p.cpu_percent(interval=2)
                    cpu_content = ['{}'.format(cpu_pid) + '%', utils.now_time()]
                    with open(cpu_file_url, 'a', newline='')as cup_file:
                        cpu_csv = csv.writer(cup_file)
                        cpu_csv.writerow(cpu_content)
                    logger.info('cpu: {}'.format(cpu_content))
                    # mem
                    mem_pid = p.memory_info().rss
                    mem_pid = round(mem_pid / 1024 / 1024, 2)  # float 保留小数点2位
                    mem_content = ['{}'.format(mem_pid) + 'MB', utils.now_time()]
                    with open(mem_file_url, 'a', newline='')as mem_file:
                        cpu_csv = csv.writer(mem_file)
                        cpu_csv.writerow(mem_content)
                    logger.info('mem: {}'.format(mem_content))
                else:
                    # cpu=0
                    cpu_content = ['0' + '%', utils.now_time()]
                    with open(cpu_file_url, 'a', newline='')as cup_file:
                        cpu_csv = csv.writer(cup_file)
                        cpu_csv.writerow(cpu_content)
                    logger.info('cpu: 0')

                    # mem=0
                    mem_content = ['0' + '%', utils.now_time()]
                    with open(mem_file_url, 'a', newline='')as mem_file:
                        cpu_csv = csv.writer(mem_file)
                        cpu_csv.writerow(mem_content)
                    logger.info('mem: 0')
                    time.sleep(2)
                continue
        except Exception as e:
            logger.error(e)

