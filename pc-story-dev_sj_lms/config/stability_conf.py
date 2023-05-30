# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: PC稳定性  相关使用配置
"""


# update-1
"""APP版本号"""
APP_URL = "D:\\classin-win7-2023-05-22_06-40-22-git-4fef4d087-v5.0.3.536\\ClassIn.exe"

# update-2
"""登录用户名和密码"""
LOGIN_USER_NAME = '12112160089'
LOGIN_PASS_WORD = 'e123456'

# update-3
"""是否获取FPS值，填写Y/N，Y=需要获取FPS，N=不需要"""
IS_USE_FPS = 'N'

# update-4
"""将课节创建在此课程下"""
CLASSNAME = 'STABILITY'

# 使用云盘下的文件夹
YUNPANFLODER = '课件'

# 功能：复用其他班级课程
CLASSFORCOPY = '班级-复用使用'

# WebDriver版本   注：2023/5/10后的版本，一般都是103
WEBDRIVER_VERSION = 103

# 在线教室打开的文件列表-稳定性用
files = ['csv.csv', 'doc.doc', 'docx.docx', 'eda.eda', 'edb.edb', 'epub.epub', 'mp3.mp3', 'mp4.mp4', 'pdf.pdf', 'pgn.pgn', 'ppt.ppt', 'pptx.pptx', 'sgf.sgf', 'txt.txt', 'xlsx.xlsx']

# 在线教室，各功能执行次数
online_loop = 6