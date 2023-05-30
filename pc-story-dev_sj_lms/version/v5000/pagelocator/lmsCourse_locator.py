# coding = utf-8
"""
@Author: zjw
@Create on:
@Modify on:
@File: LMS版本，班级-课程
"""


# 公用[新建]按钮
H5_Create = ('课程tab下的【新建】', 'XPath', '//span[text()= "新建"]')
PublishBtn = ('活动发布btn', 'XPath', '//span[text()="发布"]')  # 单元主题、录播课、作业、讨论、学习资料。测验不一样

# 新建课堂相关
KeTang = ('课堂', 'XPath', '(//div[text()="课堂"])[2]')
UnitItem =  ('单元主题item', 'XPath', '(//div[@aria-describedby="rbd-hidden-text-0-hidden-text-0"])[last()]')
Publish = ('发布课堂', 'Name', '发布')
# AddBtn = ('添加+', 'XPath', '//div[@aria-describedby="rbd-hidden-text-0-hidden-text-0"][last()]/div/div/div/div/div/div/div/div[2]/div[1]')
AddBtn = ('添加+', 'XPath', '(//div[@aria-describedby="rbd-hidden-text-0-hidden-text-0"][last()]/div/div/div/div/div/div/div/div[2]/div[2]/div)[1]')
KeTangCreateBody = ('新建课堂的设置表单', 'ClassName', 'LmsCreateCourseWidget')
KeTangNew = ('课堂', 'XPath', '(//div[text()="课堂"])[1]')
QScrollArea = ('新建课堂页面左侧', 'ClassName', 'QScrollArea')
EeoWebView = ('新建课堂页面右侧', 'ClassName', 'EeoWebView')
KeTangAddName = ('新建课堂填写课堂名称', 'ClassName', 'EeoCustomLineEditWithTip')
TeachMode = ('教学模式', 'ClassNames', 'QRadioButton')  # 0是在线模式，1是智慧教室，
LukeClassRoom = ('录制教室', 'Name', '录制教室')
LuKeOnSite = ('录制现场', 'Name', '录制现场')
PageZhiBo = ('网页直播', 'Name', '网页直播')
PageHuiFang = ('网页回放', 'Name', '网页回放')
QScrollBarKeTang=('新建课堂页面的滚动条', 'ClassNames','QScrollBar')


# 新建录播课相关
Luboke = ('录播课', 'XPath', '//div[text()="录播课"]')
LubokeName = ('输入录播课名称', 'XPath', '//input[@placeholder="请填写录播课标题（50字以内）"]')
Choose_Yunpan = ('点击云盘选择', 'XPath', '//div[@title="从云盘选择"]')
File_Yunpan = ('选择云盘的视频', 'XPaths','//i[@class="eeo-icon-uncheckbox"][1]')
LubokeEnsure = ('选择云盘的视频确定', 'XPath','//span[text()="确定"]')
# LubokePublish = ('发布录播课', 'XPath','//button[@title="发布"]')


# 新建作业相关
Homework = ('作业', 'XPath', '//div[text()="作业"]')
HW_Name = ('输入作业名称', 'XPath', '//input[@placeholder="请填写作业标题（50字以内）"]')
HW_Content = ('输入作业内容', 'XPath','//div[@aria-placeholder="请填写作业内容"]')
# HW_Publish = ('作业的发布btn', 'XPath','//span[text()="发布"]')


# 新建测验相关
Exam = ('测验', 'XPath', '//div[text()="测验"]')
ExamItem = ('全选本页', 'XPath','//span[text()="全选本页"]')
ExamSet = ('组卷和设置', 'XPath','//span[contains(text(),"下一步：组卷和设置")]')
ExamTitle = ('标题', 'XPath','//input[@placeholder="请输入试卷标题（必填）"]')
ExamPublish = ('测验的发布btn', 'XPath', '//span[text()=" 发布 "]')


# 新建讨论相关
Discuss = ('讨论', 'XPath', '//div[text()="讨论"]')
DisTitle = ('讨论标题', 'XPath', '//input[@placeholder="请填写讨论标题（50字以内）"]')
DisContent = ('讨论内容', 'XPath','//div[@aria-placeholder="请填写讨论内容"]')
# DisPublish = ('讨论的发布btn', 'XPath','//span[contains(text(),"发布")]')


# 新建学习资料相关
Learning = ('学习资料', 'XPath', '//div[text()="学习资料"]')
LearningTitle = ('学习资料标题', 'XPath', '//input[@placeholder="请填写资料标题（50字以内）"]')
LearningContent = ('学习资料内容', 'XPath','//div[@aria-placeholder="请填写资料内容"]')
# LearningPublish =('学习资料的发布btn', 'XPath','//span[text()="发布"]')


# 新建单元主题
UnitTopic = ('单元主题', 'XPath','//div[text()="单元主题"]')
UnitTitle = ('单元主题主题', 'XPath','//input[@placeholder="请填写单元主题名称(50字以内)"]')
UnitContent = ('单元主题内容', 'XPath','//textarea[@placeholder="请填写单元介绍，包括学习目标、资源与建议等。"]')
# UnitPublish = ('单元主题的发布btn', 'XPath','//span[text()="发布"]')


# 复用其他班级课程
Copy = ('复用其他班级课程', 'XPath','//span[text()= "复用其他班级课程"]')
# CopyClass = ('选择复制班级', 'XPath','//span[text()="班级-复用使用"]')
CopyUnit = ('选择单元', 'XPath','(//input[@class="ant-checkbox-input"])[1]')
CopyContinue = ('继续', 'XPath', '//button[@class="ant-btn ant-btn-primary false auto-test-lms"]')
CopySure = ('确定', 'XPath','//span[text()="确定"]')


#  查看‘成绩’tab
StudyActivity = ('学习活动', 'XPath', '//div[text()="学习活动"]')
sut_list =('学生score列表的第一个人', 'XPath', '(//div[@class="flex items-center px-4 cursor-pointer"])[1]')


# 课程下 搜索
SearchLogo = ('搜索 放大镜logo', 'XPath', '(//img[@class="text-gray-400 auto-test-lms rounded"])[1]')
SearchText = ('搜索框', 'XPath', '//input[@placeholder="搜索学习活动"]')
SearchDel = ('清除搜索框内容X', 'XPath', '//div[@class="flex w-5 h-5 justify-center content-center cursor-pointer items-center auto-test-lms"]')


# 编辑相关公共元素
EditItem =  ('活动搜索结果list，取最后一个进行编辑', 'XPath', '(//div[@class="truncate"])[last()]')
# EditEnter = ('编辑入口logo ...', 'XPath', '(//img[@class="cursor-pointer auto-test-lms"])[last()]')  # 作业编辑入口class同名的存在2个
EditBtn = ('点击...里的编辑', 'XPath', '//span[text()="编辑"]')
EditEnsureNative=('编辑确定btn-原生', 'Name', '确定')
EditEnsureH5=('编辑确定btn-web', 'XPath', '//button[@title="确定"]')  # 作业、讨论、录播课、学习资料(测验的另取其他)
# PageClosed = ('页面关闭’X‘', 'XPath', '//span[@class="anticon auto-test-lms"]')  # 活动详情页面，学生成绩详情页面
"""
对活动详情页面添加标识的元素的说明：详情页面元素上添加了标识auto-test-lms
1. 添加标识的元素包括编辑入口'...'  和  页面关闭‘X’ 等。
2. 元素AutoTestLMS获取后是个list
作业--分享取数组下标0，编辑入口取数组下标1，页面关闭‘x’取数组下标2
课堂&测验&学习资料&讨论--编辑入口取数组下标0，页面关闭‘x’取数组下标1
录播课--编辑入口取数组下标0，页面关闭‘x’取数组下标1； 另有下标3和4定位在其他位置
学生成绩--页面关闭‘x’取数据下标0
测验编辑页面的【确定】--取数组下标0
"""
AutoTestLMS = ('各活动详情页面加标识的元素', 'XPaths', '//*[contains(@class, "auto-test-lms")]')



# 编辑 课堂 相关
EditAllowCheck = ('编辑-公开学习报告和评分', 'XPath', '//button[@id="isAllowCheck"]')


# 编辑 测验 相关
# EditEnsureExamH5=('测验编辑确定btn-web', 'XPath', '(//span[contains(text(),"确定")])[2]')





# # 课程下 搜索
# # SearchLogo = ('搜索 放大镜logo', 'XPath', '//img[@src="/client/lms/static/search.e9e807c5.svg"]')
# # SearchLogo = ('搜索 放大镜logo', 'XPath', '//img[@src="/client/lms/static/search.9e37d02a.svg"]')
# # SearchLogo = ('搜索 放大镜logo', 'XPaths', '//span[@class="relative p-1 cursor-pointer hover:bg-gray-50 active:bg-gray-500"]')
# SearchLogo = ('搜索 放大镜logo', 'XPaths', '(//img[@class="text-gray-400 auto-test-lms rounded"])[1]')
# SearchText = ('搜索框', 'XPath', '//input[@placeholder="搜索学习活动"]')
# # SearchDel = ('清除搜索框内容X', 'XPath', '//span[@class="ant-input-suffix"]')
# # SearchDel = ('清除搜索框内容X', 'XPath', '//img[@class="text-gray-400"]')
# # SearchDel = ('清除搜索框内容X', 'XPath', '//div[@class="font-pf-regular noBoxShadow"]/span/span[2]/div')
#
# SearchDel = ('清除搜索框内容X', 'XPath', '//div[@class="flex w-5 h-5 justify-center content-center cursor-pointer items-center auto-test-lms"]')
#
# # 编辑相关公共元素
# # EditEnter = ('课堂编辑入口logo ...', 'XPath', '//img[@src="/client/lms/static/more_operation.087297d5.svg"]')
# # EditEnter = ('课堂编辑入口logo ...', 'XPath', '//img[@src="/client/lms/static/moreW.de9a965b.svg"]')
# # EditEnter = ('课堂编辑入口logo ...', 'XPaths', '//img[@src="/client/lms/static/moreW.de9a965b.svg"]')
#                                               # "//img[@class='ant-dropdown-trigger cursor-pointer mt-0.5']"
# # EditEnter = ('编辑入口logo ...', 'XPath', '//div[@class="ml-2 items-center text-center hover:bg-gray-300"][2]')
# # EditEnter = ('编辑入口logo ...', 'XPath', '(//div[@class="flex items-center"]/div/div)[2]')
# EditItem =  ('活动搜索结果list，取最后一个进行编辑', 'XPath', '(//div[@class="truncate"])[last()]')
#
# EditEnter = ('编辑入口logo ...', 'XPath', '(//img[@class="cursor-pointer auto-test-lms"])[last()]')  # 作业编辑入口class同名的存在2个
# EditBtn = ('点击...里的编辑', 'XPath', '//span[text()="编辑"]')
# EditEnsureNative=('编辑确定btn-原生', 'Name', '确定')
# EditEnsureH5=('编辑确定btn-web', 'XPath', '//span[text()="确定"]')
# # EditClosed = ("活动详情页面的关闭'X'", 'XPath', '(//div[@class="w-full h-6 align-middle"])')  # 12.19 关闭可以用统一的元素了
# PageClosed = ('页面关闭’X‘', 'XPath', '//span[@class="anticon auto-test-lms"]')  # 活动详情页面，学生成绩详情页面
#
#
# # 编辑 课堂 相关
# # KeTangItem =  ('课堂list，取第一个', 'XPath', '(//div[@class="border-b border-gray-1100 cursor-pointer  w-full items-center flex py-3 px-5"])[1]')
# # KeTangItem =  ('课堂list，取最后一个', 'XPath', '(//div[@class="truncate"])[last()]')
# # //span[text()='LMS稳定性测试']
# EditAllowCheck = ('编辑-公开学习报告和评分', 'XPath', '//button[@id="isAllowCheck"]')
# # KeTangEditClosed = ('编辑课堂-课堂页面的关闭', 'XPath', '(//div[@class="w-6 h-6 align-middle"])[3]')
# # KeTangEditClosed = ('编辑课堂-课堂页面的关闭', 'XPath', '(//div[@class="w-6 h-6 align-middle"])[2]')
#
#
# #  编辑 录播课 相关
# # LubokeItem =  ('录播课list，取第一个', 'XPath', '(//div[@class="border-b border-gray-1100 cursor-pointer  w-full items-center flex py-3 px-5"])[1]')
# # LubokeItem =  ('录播课list，取第一个', 'XPath', '(//div[@class="rounded-b-lg border-b border-gray-f5 cursor-pointer  w-full items-center flex py-3 px-5"])[1]')
# # LubokeItem =  ('录播课list，取最后一个', 'XPath', '(//div[@class="truncate"])[last()]')
# # LubokeEditClosed = ('编辑录播课-录播课页面的关闭', 'XPath', '(//div[@class="w-6 h-6 align-middle"])[2]')
#
#
# # 编辑 作业 相关
# # HWItem =  ('作业list，取第一个', 'XPath', '(//div[@class="border-b border-gray-1100 cursor-pointer  w-full items-center flex py-3 px-5"])[1]')
# # HWItem =  ('作业list，取第一个', 'XPath', '(//div[@class="rounded-b-lg border-b border-gray-f5 cursor-pointer  w-full items-center flex py-3 px-5"])[1]')
# # HWItem =  ('作业list，取最后一个', 'XPath', '(//div[@class="truncate"])[last()]')
# # HWEditEnter = ('作业编辑入口logo ...', 'XPath', '//div[@class="ml-2 items-center text-center hover:bg-gray-300"][3]')
# HWEditEnter = ('作业编辑入口logo ...', 'XPath', '//div[@class="ml-0.5 items-center text-center hover:bg-gray-300"][3]')
# # HWEditClosed = ('编辑作业-页面的关闭', 'XPath', "//div[@class='ml-2 items-center text-center icon-close-hover']")
#
# # 编辑 测验 相关
# # ExamEditItem =  ('测验list，取第一个', 'XPath', '(//div[@class="border-b border-gray-1100 cursor-pointer  w-full items-center flex py-3 px-5"])[1]')
# # ExamEditItem =  ('测验list，取第一个', 'XPath', '(//div[@class="rounded-b-lg border-b border-gray-f5 cursor-pointer  w-full items-center flex py-3 px-5"])[1]')
# # ExamEditItem =  ('测验list，取最后一个', 'XPath', '(//div[@class="truncate"])[last()]')
# # ExamEditBtn = ('测验点击...里的编辑', 'XPath', '//span[text()="编辑活动"]')
# ExamEditBtn = ('测验点击...里的编辑', 'XPath', '//span[text()="编辑"]')
# EditEnsureExamH5=('测验编辑确定btn-web', 'XPaths', '//span[contains(text(),"确定")]')
# # ExamEditClosed = ('编辑测验-测验页面的关闭', 'XPath', '(//div[@class="w-6 h-6 align-middle"])[3]')
# # ExamEditClosed = ('编辑测验-测验页面的关闭', 'XPath', '(//div[@class="w-6 h-6 align-middle"])[2]')
#
# # 编辑 讨论 相关
# # DiscussEditItem =  ('讨论list，取第一个', 'XPath', '(//div[@class="border-b border-gray-1100 cursor-pointer  w-full items-center flex py-3 px-5"])[1]')
# # DiscussEditItem =  ('讨论list，取第一个', 'XPath', '(//div[@class="rounded-b-lg border-b border-gray-f5 cursor-pointer  w-full items-center flex py-3 px-5"])[1]')
# # DiscussEditItem =  ('讨论list，取最后一个', 'XPath', '(//div[@class="truncate"])[last()]')
# # DiscussEditClosed = ('编辑讨论-讨论页面的关闭', 'XPath', '(//div[@class="w-6 h-6 align-middle"])[3]')
# # DiscussEditClosed = ('编辑讨论-讨论页面的关闭', 'XPath', '(//div[@class="w-6 h-6 align-middle"])[1]')
# # DiscussEditClosed = ('编辑讨论-讨论页面的关闭', 'XPath', '(//div[@class="w-6 h-6 align-middle"])[2]')
# # DiscussEditClosed = ('编辑讨论-讨论页面的关闭', 'XPath', '(//div[@class="w-full h-6 align-middle"])')
#
# # 编辑 学习资料 相关
# # LearningEditItem =  ('学习资料list，取第一个', 'XPath', '(//div[@class="border-b border-gray-1100 cursor-pointer  w-full items-center flex py-3 px-5"])[1]')
# # LearningEditItem =  ('学习资料list，取第一个', 'XPath', '(//div[@class="rounded-b-lg border-b border-gray-f5 cursor-pointer  w-full items-center flex py-3 px-5"])[1]')
# # LearningEditItem =  ('学习资料list，取最后一个', 'XPath', '(//div[@class="truncate"])[last()]')
# # LearingEditClosed = ('编辑学习资料-学习资料页面的关闭', 'XPath', '(//div[@class="w-6 h-6 align-middle"])[2]')












# Achievement=('成绩', 'Names', '成绩')
# Luboke_Pulish = ('发布录播课', 'Xpath','//span[text()="发布"]//..//..//button[2]')
# Recording_Classroom_KeTang=('录制教室', 'ClassNames','ToggleButton')
# QScrollBar_KeTang=('滚动条', 'ClassNames','QScrollBar')
# Name_Ketang=('课堂名称', 'ClassNames','QScrollBar')
# Ensure=('确定', 'Name', '确定')
# Close=('关闭', 'ClassNames','QToolButton')
# Score=('成绩', 'Name', '成绩')
# Course=('课程', 'Name', '课程')
# Kecheng=('课程', 'Names', '课程')
# New_Create = ('新建', 'ClassNames', 'EeoTabButton')