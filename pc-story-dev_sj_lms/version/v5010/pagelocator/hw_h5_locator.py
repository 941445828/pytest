# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File:
"""


Search = ('搜索框', 'ClassName', 'EeoSearchLineEdit')


HomeworkTab = ('作业列表', 'Name', '作业')

TeaAccount = ('点击账号', 'XPath','(//span[text()="980账号"])[1]')
StuAccount = ('点击学生', 'XPath','//div[@class="studentMeg"]')
ButtonReview = ('作业重新批阅','XPath','//button[contains(text(),"重新批阅")]')
HomeworkReview = ('批阅作业', 'XPath', "(//div[contains(text(),'去批阅')])[1]")

ViewHomeworkImage=('查看作业图片', 'XPath', "(//img[@class ='image'])[1]")
PicBtnFinish =  ('确定','XPath','//span[text()="确定"]//..//..//div[1]')
HomeworkScore=('作业评分', 'Name','评分')



HomeworkImagesPreview=('添加表情class', 'ClassName','HomeworkImagesPreview')
HomeworkImage=('添加表情', 'ClassNames','QPushButton')
# HomeworkImage=('添加表情', 'XPath','//*[@ClassName="HomeworkImagesPreview"]/*[@ClassName="QWidget"]/*[@ClassName="QPushButton"]')
HomeworkChoiceClass=('某个表情class', 'ClassName','QTableWidget')
HomeworkChoice=('某个表情', 'XPaths',"//*[@FrameworkId='Qt']")

HomeworkText=('添加文字', 'ClassNames','QToolButton')
InputHomeworkText=('添加文字具体内容', 'ClassName','EeoPainter')
HomeworkEnsure=('确定','XPath','//span[text()="确定"]//..//..//div[1]')

HomeworkViewFinish=('作业批阅完成', 'Name','完成')
HomeworkFinish=('作业完成', 'XPath','//button[contains(text(),"完成")]')
homeworkReReview=('作业重新批阅','XPath','//button[contains(text(),"重新批阅")]')

HomeworkClick=('作业点击','XPath','//span[text()="980账号"])[1]')

HomeworkPicNext=('作业下一张', 'Name','下一张')

HomeworkLoop=('图片循环', 'XPath','//div[@class="homework-content-img"]//div[@class="imgContent"]')
HomeworkTitleClick=('点击账号', 'XPath','(//span[text()="980账号"])[1]')

HomeworkStudentClick=('点击学生', 'XPath','(//span[contains(text(),"002学生")]')

ExamClick=('测验', 'Name','测验')

HomeworkReviewFinish = ('作业重新批阅完成','XPath','//button[contains(text(), "完成")]')
HomeworkReviewClosed = ('作业重新批阅关闭','XPath','//div[ @class ="close_btn_dialog pointer"]')