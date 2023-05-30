# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File:
"""
from selenium.webdriver import ActionChains
from config.common import lang_setting
from handler.yamlHandler import get_data, YamlMethod
from handler.logHandler import logger
import time, configparser, allure
from handler.getWinHandler import get_win
from version.v5000.pageobject.setting_page import BasicSettingChangeLanguagePage
from handler.eleHandler import find_element


class TestTS(object):
    # 校验--获取元素"设置"的text
    @allure.severity('critical')
    @allure.title('校验文字')
    @allure.description("测试：文字”设置“在切换到各个语种时显示是否正确")
    def test_1_assert(self, get_driver):
        response_setting_content =  BasicSettingChangeLanguagePage().get_setting_text(get_driver)
        logger.info('获取当前定位到的结果文字是：{}'.format(response_setting_content))
        lang = self.get_lang()
        # 校验：{语种：翻译}
        expect_setting = lang_setting.get(lang)[1]
        logger.info("期望当前显示的文字是: {}".format(expect_setting))
        allure.attach('{}'.format(lang), '语言')
        allure.attach('{}'.format(response_setting_content), '定位元素获取值')
        allure.attach('{}'.format(expect_setting), '期望值')
        try:
            assert response_setting_content == expect_setting
            logger.info('response：{}， expect：{} 一样!'.format(response_setting_content, expect_setting))
        except AssertionError as msg:
            logger.error('response：{}， expect：{} 不一样'.format(response_setting_content, expect_setting))
            allure.attach('{}'.format("False"), "校验结果：失败")
        else:
            allure.attach('{}'.format("True"), "校验结果：成功")


    def test_2_set(self, get_driver):
        # 更新yaml数据
        content = YamlMethod(get_data('setting.yaml')[1]).yaml_read()
        # print(content)
        content['ele_name_语言选择'] = self.get_next()
        YamlMethod(get_data('setting.yaml')[1]).yaml_write(content)
        case = get_data('setting.yaml')[0]
        # logger.info("set--用例 {}：".format(case))

        # 点击设置
        BasicSettingChangeLanguagePage().click_setting(get_driver)

        # 产生了新窗口，切换窗口
        get_win(get_driver, 0)
        time.sleep(2)

        # 点击系统设置
        BasicSettingChangeLanguagePage().click_os_setting(get_driver)

        # 产生了新窗口，切换窗口
        get_win(get_driver, 0)
        time.sleep(2)

        # 点击基本设置
        BasicSettingChangeLanguagePage().click_basic_setting(get_driver)

        # 点击更改语言选择框
        BasicSettingChangeLanguagePage().click_lang_dropmenu(get_driver)
        if YamlMethod(get_data('setting.yaml')[1]).yaml_read()['ele_name_语言选择'] == '简体中文':
            # 点击语言
            choose_language = find_element(get_driver, '语言选择', 'Name', case['ele_name_语言选择'])
            choose_language.click()
        else:
            ActionChains(get_driver).context_click().perform()
            BasicSettingChangeLanguagePage().sendKeys_lang_dropmenu(get_driver)

        # 查找元素--弹窗选择， 点击否(逻辑说明:点击是之后会重新启动，窗口关掉了)
        BasicSettingChangeLanguagePage().click_choose_no(get_driver)

        # 关闭设置页面
        close = get_driver.find_element_by_accessibility_id(case['ele_id_closewindows'])
        close.click()
        time.sleep(2)

    def test_3_switch_win(self, get_driver):
        get_win(get_driver, -1)
        time.sleep(2)

    # 获取当前语种
    def get_lang(self):
        config = configparser.ConfigParser()
        path = r'C:\Users\Administrator\AppData\Roaming\ClassIn\settings.ini'
        config.read(path)
        lang = config.get('General', 'lang')
        print('获取当前语言: {}'.format(lang))
        return lang


    # 获取下一个语种
    def get_next(self):
        lang = self.get_lang()
        yuyan = None
        for i in range(len(lang_setting)):
            if list(lang_setting.keys())[i] == lang and lang != 'pt':
                yuyan = list(lang_setting.values())[i + 1][2]
            elif list(lang_setting.keys())[i] == lang and lang == 'pt':
                yuyan = list(lang_setting.values())[0][2]
        print("下一个即将运行的语种是：{}".format(yuyan))
        return yuyan