# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from handler.yamlHandler import get_data
from handler.eleHandler import find_element
import time


class TestYPRoot:
    # 进入云盘
    def test_1_yproot(self, get_driver):
        case  = get_data('yunpan.yaml')[0]
        # 获取元素 '云盘'
        ele_yunpan = find_element(get_driver, 'ele云盘', 'Name', case['ele_name_云盘'])
        ele_yunpan.click()

    # 创建文件夹
    def test_2_create_folder(self, get_driver, get_web_driver):
        case  = get_data('yunpan.yaml')[0]

        ele_create = find_element(get_web_driver, '新建', 'XPath', "//div[@class='eeo-client-btn primary mr-2']")
        ele_create.click()

        ele_folder = find_element(get_web_driver, '文件夹', 'XPaths', case['ele_XPaths_文件夹'])
        ele_folder[0].click()

        # ele_folder_name = web_find_element('输入文件夹名称', 'XPaths', element['ele_XPaths_输入文件夹名称'])
        # ele_folder_name[0].click()

        name = case['folder_name'].split('_')[0] + '_' + str(int(time.time()))
        # ele_folder_name[0].send_keys(name)

        js = "function getcurTime() {var Digital=new Date(); var hours=Digital.getHours(); var minutes=Digital.getMinutes();  var seconds=Digital.getSeconds();  " \
             "folder=\"" + name + "\";   return folder;}" \
             "var inputelements=document.getElementsByTagName(\"input\");" \
             "inputelements[0].value=getcurTime();" \
             "inputelements[0].name=getcurTime();" \
             "inputelements[0].text=getcurTime();" \
             "inputelements[0].innerText=getcurTime();" \
             "inputelements[0].dispatchEvent(new Event('input'));"
        get_web_driver.execute_script(js)

        ele_yes = find_element(get_web_driver, '确认', 'XPaths', case['ele_XPaths_确认'])
        ele_yes[0].click()