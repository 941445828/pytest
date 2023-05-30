# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File: 作业重新批阅
"""
from config import *
from skimage.metrics import structural_similarity
import imutils
import cv2
from selenium.webdriver.common.keys import Keys
from version.v5000.pagelocator import hw_h5_locator as Homework
from handler.eleHandler import find_element
import time


class H5Page:
    def click_coursename(self, driver):
        # 点击班级名称
        ele = Homework.Search
        ele_search = find_element(driver, ele[0], ele[1], ele[2])
        # print("ele_search_length",len(ele_search))
        return ele_search

    def click_exam(self, driver):
        # 点击班级名称
        ele = Homework.HomeworkClick
        ele_click_homework = find_element(driver, ele[0], ele[1], ele[2])
        return ele_click_homework

    def click_homework(self, driver):
        # 点击班级名称
        ele = Homework.HomeworkClick
        ele_click_homework = find_element(driver, ele[0], ele[1], ele[2])
        return ele_click_homework


    def click_tea_account(self, driver):
        ele = Homework.TeaAccount
        ele_tea = find_element(driver, ele[0], ele[1], ele[2])
        ele_tea.click()

    def click_stu_account(self, driver):
        ele = Homework.StuAccount
        ele_stu = find_element(driver, ele[0], ele[1], ele[2])
        ele_stu.click()

    def click_btn_review(self, driver):
        ele = Homework.ButtonReview
        ele_btn = find_element(driver, ele[0], ele[1], ele[2])
        ele_btn.click()

    def click_pic(self, driver):
        ele = Homework.ViewHomeworkImage
        ele_pic = find_element(driver, ele[0], ele[1], ele[2])
        ele_pic.click()

    def click_homework_tab(self, driver):
        # 获取元素
        ele = Homework.HomeworkTab
        ele_homework_tab = find_element(driver, ele[0], ele[1], ele[2])
        # print("ele_homework_tab",len(ele_homework_tab))
        ele_homework_tab.click()


    def click_homework_review(self, driver):
        # 获取元素
        ele = Homework.HomeworkReview
        ele_homeworkreview = find_element(driver, ele[0], ele[1], ele[2])
        ele_homeworkreview.click()

    def view_homework_image(self, driver):
        ele = Homework.ViewHomeworkImage
        ele_viewhomeworkimage = find_element(driver, ele[0], ele[1], ele[2])
        ele_viewhomeworkimage.click()

    def click_homework_image_class(self, driver):
        ele = Homework.HomeworkImagesPreview
        ele_imagespreview = find_element(driver, ele[0], ele[1], ele[2])
        # print("len-click_homework_image_class",len(ele_imagespreview))
        print("click_homework_image_class",ele_imagespreview)
        return ele_imagespreview
        # ele_imagespreview.click()

    def click_homework_image(self, driver):
        ele = Homework.HomeworkImage
        ele_clickhomeworkimg = find_element(driver, ele[0], ele[1], ele[2])
        print("ele_clickhomeworkimg",len(ele_clickhomeworkimg))
        return ele_clickhomeworkimg[2]

    def click_homework_choice_image_class(self, driver):
        ele = Homework.HomeworkChoiceClass
        ele_homeworkchoice_class = find_element(driver, ele[0], ele[1], ele[2])
        return ele_homeworkchoice_class


    def click_homework_choice_image(self, driver):
        # ele = Homework.HomeworkChoice
        ele_homeworkchoice1 = self.click_homework_choice_image_class(driver).find_elements_by_xpath("//*[@FrameworkId='Qt']")
        print("ele_homeworkchoice1",len(ele_homeworkchoice1))# 19
        ele_homeworkchoice2 = self.click_homework_choice_image_class(driver).find_elements_by_xpath("//*[@FrameworkId='Qt']")
        # print("ele_homeworkchoice2",len(ele_homeworkchoice2))
        # time.sleep(1)
        ele_homeworkchoice2[7].click()
        time.sleep(1)

    def click_homework_score(self, driver):
        ele = Homework.HomeworkScore
        ele_homeworkscore = find_element(driver, ele[0], ele[1], ele[2])
        # print("ele_viewhomeworkimage",len(ele_viewhomeworkimage))
        return ele_homeworkscore

    def click_homework_text(self, driver):
        ele = Homework.HomeworkText
        ele_homeworktext = find_element(driver, ele[0], ele[1], ele[2])
        print("ele_homeworktext",len(ele_homeworktext))
        ele_homeworktext[7].click()

    def input_homework_text(self, driver,content):
        ele = Homework.InputHomeworkText
        ele_inputhomeworktext = find_element(driver, ele[0], ele[1], ele[2])
        # print("ele_inputhomeworktext",len(ele_inputhomeworktext))
        ele_inputhomeworktext.send_keys(content)
        ele_inputhomeworktext.send_keys(Keys.SPACE)

    def click_homework_shape(self, driver):
        ele = Homework.HomeworkText
        ele_homeworktext = find_element(driver, ele[0], ele[1], ele[2])
        # print("ele_homeworktext",len(ele_homeworktext))
        ele_homeworktext[5].click()

    def input_homework_shape(self, driver):
        ele = Homework.InputHomeworkText
        ele_inputhomeworktext = find_element(driver, ele[0], ele[1], ele[2])
        ele_inputhomeworktext.send_keys("7878")

    def homework_shape(self, driver):
        ele = Homework.InputHomeworkText
        ele_inputhomeworktext = find_element(driver, ele[0], ele[1], ele[2])
        return ele_inputhomeworktext

    def click_eidt_pic_finish(self, driver):
        ele = Homework.PicBtnFinish
        ele_btn = find_element(driver, ele[0], ele[1], ele[2])
        ele_btn.click()

    def click_homework_image_save(self, driver):
        time.sleep(2)
        ele = Homework.HomeworkImage
        ele_clickhomeworkimgsave = find_element(driver, ele[0], ele[1], ele[2])
        return ele_clickhomeworkimgsave[12]

    def click_homework_image_upload(self, driver):
        ele = Homework.HomeworkImage
        ele_clickhomeworkimgupload = find_element(driver, ele[0], ele[1], ele[2])
        return ele_clickhomeworkimgupload[13]

    def click_self_adaptionhomework_image(self, driver):
        ele = Homework.HomeworkImage
        ele_clickadaptionhomework = find_element(driver, ele[0], ele[1], ele[2])
        print("ele_clickadaptionhomework",len(ele_clickadaptionhomework))
        return ele_clickadaptionhomework[8]

    def click_homework_ensure(self, driver):
        time.sleep(8)
        ele = Homework.HomeworkEnsure
        ele_clickhomeworkimgensure= find_element(driver, ele[0], ele[1], ele[2])
        ele_clickhomeworkimgensure.click()

    def click_homework_review_finish(self, driver):
        time.sleep(1)
        ele = Homework.HomeworkImage
        ele_homeworkviewfinish = find_element(driver, ele[0], ele[1], ele[2])
        print("ele_homeworkviewfinish",len(ele_homeworkviewfinish))
        return ele_homeworkviewfinish[17]

    def click_homework_finish(self, driver):
        ele = Homework.HomeworkFinish
        ele_homeworkfinish = find_element(driver, ele[0], ele[1], ele[2])
        ele_homeworkfinish.click()

    def click_homework_re_review(self, driver):
        ele = Homework.homeworkReReview
        ele_homeworkrereview = find_element(driver, ele[0], ele[1], ele[2])
        ele_homeworkrereview.click()

    def click_homework_pic_next(self, driver):
        ele = Homework.HomeworkPicNext
        ele_homeworkpicnext = find_element(driver, ele[0], ele[1], ele[2])
        return ele_homeworkpicnext

    def click_upload_pic(self,num):
        os.system(PROJECT_DIR + '\\tools' + '\\uploadFile.exe %s' %num)
        # os.system("D:\\pc-story\\pagelocator\\uploadFileNew.exe %s" %num)
        time.sleep(2)
    def click_homework_pic_nums_loop(self,driver):
        ele = Homework.HomeworkLoop
        ele_homeworkpicnumsloop = find_element(driver, ele[0], ele[1], ele[2])
        print("ele_homeworkpicnumsloop-len", len(ele_homeworkpicnumsloop))
        ele_homeworkpicnumsloop_num=len(ele_homeworkpicnumsloop)
        return ele_homeworkpicnumsloop_num

    def click_homework_title_click(self, driver):
        ele = Homework.HomeworkTitleClick
        ele_homeworktitleclick = find_element(driver, ele[0], ele[1], ele[2])
        ele_homeworktitleclick.click()

    def click_homework_student_click(self, driver):
        ele = Homework.HomeworkStudentClick
        ele_homeworkstudentclick = find_element(driver, ele[0], ele[1], ele[2])
        ele_homeworkstudentclick.click()


    def get_rootpath(self):
        current_path = os.path.abspath(__file__)
        a = current_path.split('\\')[:-4]
        fat = '/'.join(a)
        return fat

    def click_review_finish(self, driver):
        ele = Homework.HomeworkReviewFinish
        ele_btn = find_element(driver, ele[0], ele[1], ele[2])
        ele_btn.click()

    def click_review_closed(self, driver):
        ele = Homework.HomeworkReviewClosed
        ele_btn = find_element(driver, ele[0], ele[1], ele[2])
        ele_btn.click()

    def judge_the_pic_is_consistent(self):

            list = ['11329722']
            list1 = ['71798047950783review']
            current_path = os.path.abspath(__file__)
            a = current_path.split('\\')[:-3]
            fat = '/'.join(a)
            rootpath = fat
            imageA = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list[0]) + ".jpeg")
            imageB = cv2.imread(rootpath + '/Users/Documents/ClassIn Files/' + str(list1[0]) + ".jpeg")

            # imageA = cv2.imread(os.path.dirname(os.path.dirname(__file__))+ '/pagelocator/1.png')
            #
            # imageB = cv2.imread(os.path.dirname(os.path.dirname(__file__))+ '/pagelocator/3.png')

            # 将他们转换为灰度：

            grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
            grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

            # 计算两个灰度图像之间的结构相似度指数：
            # 不过ssim多用于压缩图片后的失真度比较。。

            (score, diff) = structural_similarity(grayA, grayB, full=True)
            diff = (diff * 255).astype("uint8")
            print("diff", diff)

            # 找到不同点的轮廓以致于我们可以在被标识为“不同”的区域周围放置矩形：

            thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

            # cv2.findContours()函数返回两个值，一个是轮廓本身，还有一个是每条轮廓对应的属性。
            # 其首先返回一个list，list中每个元素都是图像中的一个轮廓

            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            """注意cv版本，下面这一行会出现下列问题：
            OpenCV 3 改为cv2.findContours(...)返回值为image, contours, hierarchy，

            OpenCV 2 cv2.findContours(...)和OpenCV 4 的cv2.findContours(...)返回值为contours, hierarchy。"""

            # 把contour轮廓储存在cnts这个list列表里

            cnts = cnts[1] if imutils.is_cv2() else cnts[0]
            print("cnts", cnts)
            if cnts != ():

                # 找到一系列区域，在区域周围放置矩形：
                """

                cv2.rectangle(imageA,(x,y),(x+w,y+h),(0,0,255),2)  参数解释

                第一个参数：img是原图

                第二个参数：（x，y）是矩阵的左上点坐标

                第三个参数：（x+w，y+h）是矩阵的右下点坐标

                第四个参数：（0,0,255）是画线对应的rgb颜色

                第五个参数：2是所画的线的宽度
            """

                for c in cnts:
                    (x, y, w, h) = cv2.boundingRect(c)
                    cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # 用cv2.imshow 展现最终对比之后的图片， cv2.imwrite 保存最终的结果图片

                cv2.imshow("differ", imageB)
                cv2.imwrite("differ.png", imageB)
                cv2.waitKey(0)
                print("图片不一样")
            else:
                print("图片一样")

