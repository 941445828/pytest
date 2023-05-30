# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File:
"""
from selenium.webdriver import ActionChains
from version.v5040.pagelocator import lmsCourse_locator as LMS
from handler.eleHandler import find_element
import time
from handler.yamlHandler import get_data, YamlMethod


class LmsPage:
# 新建课堂
    def click_H5_create(self, driver):
        ele = LMS.H5_Create
        ele_create = find_element(driver, ele[0], ele[1], ele[2])
        ele_create.click()
        time.sleep(1)

    def click_ketang(self, driver): # 通过单元下下创建
        ele = LMS.KeTang
        ele_ketang = find_element(driver, ele[0], ele[1], ele[2])
        ele_ketang.click()

    def click_pulish_ketang(self, driver):
        ele = LMS.Publish
        ele_pulish = find_element(driver, ele[0], ele[1], ele[2])
        ele_pulish.click()
        time.sleep(10)

    def move_to_unit(self, driver):
        ele = LMS.UnitItem
        ele_name = ele[2]
        ele_name = ele_name.split("'")
        case = get_data('baseConf.yaml')[0]
        ele_name = ele_name[0] + "'" + case['UnitName'] + "'"+ ele_name[2]
        ele_item = find_element(driver, ele[0], ele[1], ele_name)
        ele_item.click()

    def click_add_btn(self, driver):
        ele = LMS.AddBtn
        ele_btn = find_element(driver, ele[0], ele[1], ele[2])
        ele_btn.click()

    def click_ketang_new(self, driver): # 通过【新建】btn下创建
        ele = LMS.KeTangNew
        ele_ketang = find_element(driver, ele[0], ele[1], ele[2])
        ele_ketang.click()

    def click_online_mode(self, driver):
        ele = LMS.TeachMode
        ele_online = find_element(driver, ele[0], ele[1], ele[2])
        ele_online[0].click

    def get_page_down(self, driver):
        ele = LMS.QScrollBarKeTang
        ele_bar = find_element(driver, ele[0], ele[1], ele[2])
        ActionChains(driver).drag_and_drop_by_offset(ele_bar[0], 0, 300).perform()

    def click_wisdom_mode(self, driver):
        ele = LMS.TeachMode
        ele_online = find_element(driver, ele[0], ele[1], ele[2])
        ele_online[0].click

    def click_luke_room(self, driver):
        ele = LMS.LukeClassRoom
        ele_room = find_element(driver, ele[0], ele[1], ele[2])
        ele_room.click()

    def click_luke_onsite(self, driver):
        ele = LMS.LuKeOnSite
        ele_site = find_element(driver, ele[0], ele[1], ele[2])
        ele_site.click()

    def click_page_zhibo(self, driver):
        ele = LMS.PageZhiBo
        ele_zhibo = find_element(driver, ele[0], ele[1], ele[2])
        ele_zhibo.click()

    def click_page_huifang(self, driver):
        ele = LMS.PageHuiFang
        ele_huifang = find_element(driver, ele[0], ele[1], ele[2])
        ele_huifang.click()

# 新建活动点击发布btn--公用
    def click_publish_btn(self, driver):
        ele = LMS.PublishBtn
        ele_pub = find_element(driver, ele[0], ele[1], ele[2])
        ele_pub.click()
        time.sleep(2)

# 新建录播课
    def click_luboke(self, driver):
        ele = LMS.Luboke
        ele_luboke = find_element(driver, ele[0], ele[1], ele[2])
        ele_luboke.click()

    def enter_luboke_name(self, driver):
        ele = LMS.LubokeName
        ele_name = find_element(driver, ele[0], ele[1], ele[2])
        ele_name.click()
        ele_name.send_keys("zjw_luboke")

    def click_yunpan(self, driver):
        ele = LMS.Choose_Yunpan
        ele_yunpan = find_element(driver, ele[0], ele[1], ele[2])
        ele_yunpan.click()

    def choose_folder(self, driver, folder):
        ele_xpath = "//span[text()='" + folder + "' ]//..//..//div"
        ele = ('选择云盘中的文件夹', 'XPath', ele_xpath)
        ele_folder = find_element(driver, ele[0], ele[1], ele[2])
        ele_folder.click()

    def choose_file(self, driver):
        ele = LMS.File_Yunpan
        ele_file = find_element(driver, ele[0], ele[1], ele[2])
        ele_file[0].click()

    def click_btn_ensure(self, driver):
        ele = LMS.LubokeEnsure
        ele_yes = find_element(driver, ele[0], ele[1], ele[2])
        ele_yes.click()


# 新建作业
    def click_homework(self, driver):
        ele = LMS.Homework
        ele_hw = find_element(driver, ele[0], ele[1], ele[2])
        ele_hw.click()

    def enter_hw_name(self, driver):
        ele = LMS.HW_Name
        ele_name = find_element(driver, ele[0], ele[1], ele[2])
        ele_name.click()
        ele_name.send_keys("zjw_homework_lms")

    def enter_hw_content(self, driver):
        ele = LMS.HW_Content
        ele_name = find_element(driver, ele[0], ele[1], ele[2])
        ele_name.click()
        ele_name.send_keys("zjw_homework_lms_content")


# 新建测验
    def click_exam(self, driver):
        ele = LMS.Exam
        ele_exam = find_element(driver, ele[0], ele[1], ele[2])
        ele_exam.click()

    def click_select_item(self, driver):
        ele = LMS.ExamItem
        ele_sec = find_element(driver, ele[0], ele[1], ele[2])
        time.sleep(2)
        ele_sec.click()

    def click_select_set(self, driver):
        ele = LMS.ExamSet
        ele_sec = find_element(driver, ele[0], ele[1], ele[2])
        ele_sec.click()

    def enter_exam_title(self, driver):
        ele = LMS.ExamTitle
        ele_title = find_element(driver, ele[0], ele[1], ele[2])
        ele_title.click()
        ele_title.send_keys("zjw_exam")

    def click_exam_publish(self, driver):
        ele = LMS.ExamPublish
        ele_pub = find_element(driver, ele[0], ele[1], ele[2])
        time.sleep(5)
        ele_pub.click()
        time.sleep(5)


# 新建讨论
    def click_discuss(self, driver):
        ele = LMS.Discuss
        ele_discuss = find_element(driver, ele[0], ele[1], ele[2])
        ele_discuss.click()

    def enter_dis_title(self, driver):
        ele = LMS.DisTitle
        ele_title = find_element(driver, ele[0], ele[1], ele[2])
        ele_title.click()
        ele_title.send_keys("zjw_discuss")

    def enter_dis_content(self, driver):
        ele = LMS.DisContent
        ele_content = find_element(driver, ele[0], ele[1], ele[2])
        ele_content.click()
        ele_content.send_keys("zjw_discuss_content")


# 新建学习资料
    def click_learning(self, driver):
        ele = LMS.Learning
        ele_learn = find_element(driver, ele[0], ele[1], ele[2])
        ele_learn.click()

    def enter_learn_title(self, driver):
        ele = LMS.LearningTitle
        ele_title = find_element(driver, ele[0], ele[1], ele[2])
        ele_title.click()
        ele_title.send_keys("zjw_learning_materials")

    def enter_learn_content(self, driver):
        ele = LMS.LearningContent
        ele_content = find_element(driver, ele[0], ele[1], ele[2])
        ele_content.click()
        ele_content.send_keys("zjw_learning_materials_content")


# 新建单元主题
    def click_unit(self, driver):
        ele = LMS.UnitTopic
        ele_unit = find_element(driver, ele[0], ele[1], ele[2])
        ele_unit.click()

    def enter_unit_title(self, driver):
        ele = LMS.UnitTitle
        ele_title = find_element(driver, ele[0], ele[1], ele[2])
        ele_title.click()
        unit_title = "zjw_unit_topic_title_" + str(int(time.time()))
        # 将单元名称，存入
        case = get_data('baseConf.yaml')[0]
        case['UnitName'] = unit_title
        YamlMethod(get_data('baseConf.yaml')[1]).yaml_write(case)
        # 键入单元名称
        ele_title.send_keys(unit_title)


    def enter_unit_content(self, driver):
        ele = LMS.UnitContent
        ele_content = find_element(driver, ele[0], ele[1], ele[2])
        ele_content.click()
        ele_content.send_keys("zjw_unit_topic_content")


# 复用其他班级课程
    def click_copy(self, driver):
        ele = LMS.Copy
        ele_copy = find_element(driver, ele[0], ele[1], ele[2])
        ele_copy.click()

    def choose_class(self, driver, classname):
        ele = '//span[text()="'+ classname +'"]'
        ele_choose = driver.find_element_by_xpath(ele)
        ele_choose.click()

    def choose_unit(self, driver):
        ele = LMS.CopyUnit
        ele_choose = find_element(driver, ele[0], ele[1], ele[2])
        ele_choose.click()

    def click_Continue(self, driver):
        ele = LMS.CopyContinue
        ele_go = find_element(driver, ele[0], ele[1], ele[2])
        ele_go.click()

    def click_sure(self, driver):
        ele = LMS.CopySure
        ele_yes = find_element(driver, ele[0], ele[1], ele[2])
        ele_yes.click()
        time.sleep(5)


#  切换到‘成绩’tab，查看成绩
    def click_study_activity(self, driver):
        ele = LMS.StudyActivity
        ele_tab = find_element(driver, ele[0], ele[1], ele[2])
        ele_tab.click()

    def click_student(self, driver):
        ele = LMS.sut_list
        ele_student = find_element(driver, ele[0], ele[1], ele[2])
        ele_student.click()

    def click_score_page_closed(self, driver):
        eles = self.get_autotestlms(driver)
        eles[0].click()


# 搜索，点击放大镜logo
    def click_search_logo(self, driver):
        ele = LMS.SearchLogo
        ele_logo = find_element(driver, ele[0], ele[1], ele[2])
        ele_logo.click()

    def enter_search_content(self, driver, content, num):
        # 性能测试-sleep 5s； 稳定性测试-sleep 20s
        ele = LMS.SearchText
        ele_text = find_element(driver, ele[0], ele[1], ele[2])
        ele_text.click()
        ele_text.send_keys(content)
        time.sleep(num)

    def enter_search_content_del(self, driver):
        ele = LMS.SearchDel
        ele_del = find_element(driver, ele[0], ele[1], ele[2])
        ele_del.click()


# 编辑  公用方法
    def get_autotestlms(self, driver):
        ele = LMS.AutoTestLMS
        ele_auto = find_element(driver, ele[0], ele[1], ele[2])
        return ele_auto

    def click_activities_item(self, driver):
        ele = LMS.EditItem
        ele_item = find_element(driver, ele[0], ele[1], ele[2])
        ele_item.click()

    def click_edit_btn(self, driver):
        ele = LMS.EditBtn
        ele_logo = find_element(driver, ele[0], ele[1], ele[2])
        ele_logo.click()

    def click_edit_allow_check(self, driver):
        ele = LMS.EditAllowCheck
        ele_allow =  find_element(driver, ele[0], ele[1], ele[2])
        ele_allow.click()

    def click_edit_ensure_native(self, driver):
        ele = LMS.EditEnsureNative
        ele_ensure = find_element(driver, ele[0], ele[1], ele[2])
        ele_ensure.click()

    def click_edit_ensure_web(self, driver):
        ele = LMS.EditEnsureH5
        ele_ensure = find_element(driver, ele[0], ele[1], ele[2])
        ele_ensure.click()


# 编辑 课堂
    def click_ketang_edit_enter(self, driver):
        eles = self.get_autotestlms(driver)
        eles[0].click()

    def click_ketang_page_closed(self, driver):
        eles = self.get_autotestlms(driver)
        eles[1].click()


# 编辑 录播课
    def click_luboke_edit_enter(self, driver):
        eles = self.get_autotestlms(driver)
        eles[0].click()

    def click_luboke_page_closed(self, driver):
        eles = self.get_autotestlms(driver)
        eles[1].click()


# 编辑 作业
    def click_hw_edit_enter(self, driver):
        eles = self.get_autotestlms(driver)
        eles[1].click()

    def click_hw_page_closed(self, driver):
        eles = self.get_autotestlms(driver)
        eles[2].click()


# 编辑 测验
    def click_exam_edit_enter(self, driver):
        eles = self.get_autotestlms(driver)
        eles[0].click()

    def click_exam_page_closed(self, driver):
        eles = self.get_autotestlms(driver)
        eles[1].click()

    def click_exam_edit_ensure(self, driver):
        eles = self.get_autotestlms(driver)
        eles[0].click()


# 编辑 讨论
    def click_discuss_edit_enter(self, driver):
        eles = self.get_autotestlms(driver)
        eles[0].click()

    def click_discuss_page_closed(self, driver):
        eles = self.get_autotestlms(driver)
        eles[1].click()


# 编辑 学习资料
    def click_learning_edit_enter(self, driver):
        eles = self.get_autotestlms(driver)
        eles[0].click()

    def click_learning_page_closed(self, driver):
        eles = self.get_autotestlms(driver)
        eles[1].click()


# LmsPage().fun_2()


########################### 以下，是学生端操作
# 搜索，点击放大镜logo
class StuLmsPage:
    def stu_click_search_logo(self, driver):
        ele = LMS.StuSearchLogo
        ele_logo = find_element(driver, ele[0], ele[1], ele[2])
        ele_logo.click()