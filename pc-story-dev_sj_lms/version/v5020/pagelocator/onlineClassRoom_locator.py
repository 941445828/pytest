# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: 在线教室--元素获取
"""


"""区域布局"""
# 教室内整体区域
wholeLocation = ('教室内整体区域', 'ClassName', 'ClassroomPage')



"""头部区域"""
titleBar = ('在线教室头部bar', 'ClassName', 'TitleBar')

# 网络延迟、CPU、FPS
leftBar = ('网络延迟、CPU、FPS', 'ClassName', 'SystemStateLabel')
# FPS
# fps_value = ('FPS值', 'ClassNames', 'QLabel')
fps_value = ('FPS值', 'XPaths', "//*[@ClassName='SystemStateLabel']/*[@ClassName='QLabel']")

# 最小化、最大化、关闭区域
rightBar = ('最小化、最大化、关闭', 'ClassName', 'ToolBarInRoom')
# 最小化button
minimize_button = ('最小化button', 'ClassNames', 'QToolButton')
# 最大化button
maximize_button = ('最大化button', 'ClassNames', 'QToolButton')
# 关闭button
close_button = ('关闭button', 'ClassNames', 'QToolButton')

# 设置--设置虚拟背景
setting_area = ('设置区域', 'XPath', "(((((//*[@ClassName='TitleBar']/*[@ClassName='QWidget'])[2])/*[@ClassName='QToolBar'])[1])/*[@ClassName='ActionContentsWidget'])[1]" )
setting = ('设置', 'Name', '设置')
virtual = ('虚拟背景-item', 'XPath', "(((//*[@ClassName='DeviceSettingWidget']/*[@ClassName='QWidget'])[2])/*[@ClassName='EeoToolButtonInRoom'])[4]")
virtual_backup = ('选择-背景虚化', 'XPath', "(//*[@ClassName='DeviceSettingWidget']/*[@ClassName='QStackedWidget']/*[@ClassName='VirtualCameraWidget']/*[@ClassName='ClassroomVirtualView']/*[@FrameworkId='Qt'])[2]")
setting_close = ('设置窗口-关闭', 'XPath', "((//*[@ClassName='DeviceSettingWidget']/*[@ClassName='QWidget'])[1])/*[@ClassName='QToolButton']")

"""摄像头区域"""
cameraLocation = ('摄像头区域', 'ClassName', 'RegionAWidget')
# 摄像头
camera = ('摄像头tool', 'ClassNames', 'IPlayer')

reward_all = ('奖杯logo，给台上所有学生发奖励', 'ClassName', 'ButtonAwardAll')


"""黑板+工具操作区域"""
mainLocation = ('黑板+工具栏主体区域', 'ClassName', 'EeoPainter')



"""工具栏区域"""
tookLocation = ('工具栏区域', 'ClassName', 'ToolbarInClassroom')
# 点击工具 ButtonInVerticalToolBar 13个
click_icon = ('点击icon', 'ClassNames', 'ButtonInVerticalToolBar')
choose_icon = ('选择&移动icon', 'ClassNames', 'ButtonInVerticalToolBar')
pen_icon = ('画笔icon', 'ClassNames', 'ButtonInVerticalToolBar')
rubber_icon = ('橡皮擦icon', 'ClassNames', 'ButtonInVerticalToolBar')
text_icon = ('文本icon', 'ClassNames', 'ButtonInVerticalToolBar')
cut_icon = ('截图icon', 'ClassNames', 'ButtonInVerticalToolBar')
laser_icon = ('激光笔icon', 'ClassNames', 'ButtonInVerticalToolBar')
yunpan_icon = ('云盘icon', 'ClassNames', 'ButtonInVerticalToolBar')
toolbox_icon = ('工具箱icon', 'ClassNames', 'ButtonInVerticalToolBar')
homework_icon = ('作业icon', 'ClassNames', 'ButtonInVerticalToolBar')
note_icon = ('课堂笔记icon', 'ClassNames', 'ButtonInVerticalToolBar')
chat_icon = ('聊天icon', 'ClassNames', 'ButtonInVerticalToolBar')
roster_icon = ('花名册icon', 'ClassNames', 'ButtonInVerticalToolBar')



# 举手上台区域
handUpLocation = ('举手上台button', 'ClassName', 'TeacherHandupButton')
# 举手复选框
handup_box = ('举手复选框', 'ClassName', 'QCheckBox')



"""画笔区域"""
penLocation = ('画笔工具弹出框', 'ClassName', 'FontBoxForRoom')
# 画笔粗细
pen_sub0 = ('画笔粗度0', 'Name', 'sub0')
pen_sub1 = ('画笔粗度1', 'Name', 'sub1')
pen_sub2 = ('画笔粗度2', 'Name', 'sub2')
pen_sub3 = ('画笔粗度3', 'Name', 'sub3')
# 画笔线条
pen_solid = ('画笔实心线条', 'Name', 'solidline')
pen_dot = ('画笔点状线条', 'Name', 'dotline')
# 画笔样式
pen_curve = ('画笔-曲线', 'Name', 'curve')
pen_line = ('画笔-直线', 'Name', 'line')
pen_ellipse = ('画笔-圆圈', 'Name', 'ellipse')
pen_rectangle = ('画笔-长方形', 'Name', 'rectangle')
# 画笔颜色
pen_color1 = ('画笔-色1', 'Name', 'color1')
pen_color2 = ('画笔-色2', 'Name', 'color2')
pen_color3 = ('画笔-色3', 'Name', 'color3')
pen_color4 = ('画笔-色4', 'Name', 'color4')
pen_color5 = ('画笔-色5', 'Name', 'color5')
pen_color6 = ('画笔-色6', 'Name', 'color6')
pen_color7 = ('画笔-色7', 'Name', 'color7')
pen_color8 = ('画笔-色8', 'Name', 'color8')
pen_color9 = ('画笔-色9', 'Name', 'color9')
pen_color10 = ('画笔-色10', 'Name', 'color10')
pen_color11 = ('画笔-色11', 'Name', 'color11')
pen_color12 = ('画笔-色12', 'Name', 'color12')


"""橡皮擦区域"""
rubberLocation = ('橡皮擦工具弹出框', 'ClassName', 'RubberWidgetInRoom')
# 橡皮擦粗细
rubber_sub0 = ('橡皮擦粗度0', 'Name', 'sub0')
rubber_sub1 = ('橡皮擦粗度1', 'Name', 'sub1')
rubber_sub2 = ('橡皮擦粗度2', 'Name', 'sub2')
# 橡皮擦清屏
rubber_clear_btn = ('橡皮擦清屏刷子btn', 'Name', 'clear')
rubber_clear_prompt = ('橡皮擦清屏提示框', 'ClassName', 'EeoMessageBox')


"""文本工具区域"""
textLocation = ('文本工具弹出框', 'ClassName', 'FontBoxForRoom')
# 文本字号
text_sub0 = ('文本字号0', 'Name', 'sub0')
text_sub1 = ('文本字号1', 'Name', 'sub1')
text_sub2 = ('文本字号2', 'Name', 'sub2')
text_sub3 = ('文本字号3', 'Name', 'sub3')
# 文本颜色
text_color1 = ('文本-色1', 'Name', 'color1')
text_color2 = ('文本-色2', 'Name', 'color2')
text_color3 = ('文本-色3', 'Name', 'color3')
text_color4 = ('文本-色4', 'Name', 'color4')
text_color5 = ('文本-色5', 'Name', 'color5')
text_color6 = ('文本-色6', 'Name', 'color6')
text_color7 = ('文本-色7', 'Name', 'color7')
text_color8 = ('文本-色8', 'Name', 'color8')
text_color9 = ('文本-色9', 'Name', 'color9')
text_color10 = ('文本-色10', 'Name', 'color10')
text_color11 = ('文本-色11', 'Name', 'color11')
text_color12 = ('文本-色12', 'Name', 'color12')



"""截图区域"""
cutLocation = ('截图工具弹出框', 'ClassName', 'ScreenshotMenu')
cut_cut = ("截图-截图选项", 'Name', 'screenshot')


"""激光笔区域"""
laserLocation = ('激光笔工具弹出框', 'ClassName', 'LaserMessageWidget')



"""工具箱区域"""
# 工具箱区域
toolboxLocation = ('工具箱列表区域', 'Name', 'ClassroomToolBox')
# 工具箱加载更多icon
more_icon = ('工具箱加载更多icon', 'ClassNames', 'QToolButton')
# 工具箱 窗口关闭btn
toolbox_win_close = ('工具箱窗口关闭btn', 'ClassNames', 'QToolButton')
"""各个工具"""
# 打开文件
openFile_icon = ('打开文件 icon', 'Name', '打开文件')

# 保存/分享板书
saveEdb_icon = ('保存/分享板书 icon', 'Name', '保存/分享板书')
# 保存和分享板书窗口
save_win = ('保存和分享板书窗口', 'Name', 'Form')
# 保存至本地
save_to_local = ('保存至本地 icon', 'ClassNames', 'EIconTextButton')
save_to_check = ('保存至本地另存信息确认窗口', 'ClassName', 'SaveEdbFileWithCheckRepeat')
save_file_name = ('另存为文件名称', 'ClassName', 'QLineEdit')
save_to_local_url = ('保存至本地地址另存', 'ClassNames', 'QPushButton')
# 保存至云盘
save_to_yunpan = ('保存至云盘 icon', 'ClassNames', 'EIconTextButton')
# 分享至ClassIn icon
share_to_ClassIn = ('分享至ClassIn icon', 'ClassNames', 'EIconTextButton')
# 复制图片
copy_pic = ('复制图片 icon', 'ClassNames', 'EIconTextButton')


# 共享
# shareTool_icon = ('共享工具 icon', 'Name', '共享工具')
shareTool_icon = ('共享工具 icon', 'Name', '屏幕共享')
share_win = ('共享工具 窗口', 'ClassName', 'ShareSelectWidget')
share_win_close_btn = ('共享工具 窗口', 'ClassName', 'QToolButton')
# 桌面共享
share_btn = ('屏幕共享-共享btn', 'Name', '共享')
end_share_btn = ('屏幕共享-结束共享btn', 'Name', '结束共享')
# share_desktop = ('桌面共享', 'ClassNames', 'ToolDescriptionButton')
share_desktop = ('桌面共享', 'ClassNames', 'ScreenDescriptionButton')
share_desktop_sound = ('桌面共享-共享声音' ,'Name', '共享声音')
share_desktop_start = ('桌面共享-开始共享' ,'Name', '开始共享')
share_desktop_close = ('桌面共享-关闭btn', 'ClassNames', 'QToolButton') #7个的最后一个
# 教师屏幕共享
# share_teacher = ('教师屏幕共享', 'ClassNames', 'ToolDescriptionButton')
share_teacher = ('教师屏幕共享', 'ClassNames', 'ScreenDescriptionButton')
share_teacher_close = ('老师屏幕共享-关闭btn', 'ClassNames', 'QToolButton') # 14的最后一个
# 全体学生共享
share_student = ('学生屏幕共享选项', 'ClassNames', 'ScreenDescriptionButton')
share_student_send_btn = ('学生屏幕共享-发送共享请求-btn', 'Name', '发送共享请求')
share_student_title = ('全体学生共享', 'ClassName', 'ToolBarInRoom')
share_student_close = ('全体学生共享-关闭btn', 'ClassNames', 'QToolButton') # 3的最后一个



# 筛子
shaizi_icon = ('骰子 icon', 'Name', '骰子')
shaizi_win_total = ('骰子窗口整体', 'ClassName', 'H5DiceWidget')
shaizi_H5= ('骰子中心h5', 'XPaths', '//div[@class["diceBox"]]')
shaizi_win_close = ('骰子窗口关闭btn', 'ClassName', 'QToolButton' )

# 答题器
datiqi_icon = ('答题器 icon', 'Name', '答题器')
datiqi_win = ('答题器窗口整体', 'ClassName', 'QASelectFrame')
daqiti_win2_title = ('答题器人数窗口title', 'ClassName', 'QATitleBar')
datiqi_win_close = ('答题器窗口关闭btn', 'ClassName', 'QToolButton' )
datiqi_item = ('答题器选项', 'ClassNames', 'QASelectItem')
datiqi_begin_btn = ('答题器开始答题btn', 'Name', '开始答题')
datiqi_edit_btn = ('答题器修改答案btn', 'Name', '修改答案')
datiqi_end_btn = ('答题器结束答题btn', 'Name', '结束答题')

# 小黑板
xiaoheiban_icon = ('小黑板 icon', 'Name', '小黑板')
xiaoheiban_win = ('小黑板 窗口', 'ClassName', 'ScratchSelectorDialog')
xiaoheiban_paint = ('小黑板-画板', 'ClassNames', 'QPushButton')
xiaoheiban_text = ('小黑板-文本', 'ClassNames', 'QPushButton')
xiaoheiban_paint_prepare = ('小黑板-准备阶段-窗口', 'ClassName', 'Standalone::TabBlackboardWidget')
xiaoheiban_share = ('小黑板-画板-分发', 'Name', '分发')
xiaoheiban_back = ('小黑板-画板-收回', 'Name', '收回')
xiaoheiban_reshare = ('小黑板-画板-再次分发', 'Name', '再次分发')
xiaoheiban_painter = ('小黑板-画板-面板编辑部分', 'ClassName', 'EeoPainter')
xiaoheiban_texter = ('小黑板-文本-面板编辑部分', 'ClassName', 'TextWidget')
xiaoheiban_paint_PainterController = ('小黑板-画板-工具tools', 'ClassName', 'PainterController')
xiaoheiban_paint_pen = ('小黑板-画板-工具-画笔', 'ClassNames', 'QPushButton')
xiaoheiban_paint_text = ('小黑板-画板-工具-文本', 'ClassNames', 'QPushButton')
xiaoheiban_prepare_close = ('小黑板-画板-窗口-关闭', 'ClassName', 'QToolButton')


# 计时器
jishiqi_icon = ('计时器 icon', 'Name', '计时器')
jishiqi_win = ('计时器窗口', 'ClassName', 'StopwatchWidget')
jishiqi_begin_btn = ('计时器开始btn', 'Name', '开始')
jishiqi_FloatButtons = ('计时器暂停区域', 'ClassName', 'FloatButtons')
jishiqi_continue_btn = ('计时器继续btn', 'Name', '继续')
jishiqi_reset_btn = ('计时器重置btn', 'Name', '重置')
jishiqi_win_close = ('计时器窗口关闭', 'ClassName', 'QToolButton')

# 定时器
dingshiqi_icon = ('定时器 icon', 'Name', '定时器')
dingshiqi_win = ('定时器窗口', 'ClassName', 'TimerToolWidget')
dingshiqi_begin_btn = ('定时器开始btn', 'Name', '开始')
dingshiqi_edit_btn = ('定时器时间调整上下箭头', 'ClassNames', 'QToolButton')
dingshiqi_win_close = ('定时器窗口关闭', 'ClassNames', 'QToolButton')


# 分组讨论
group_icon = ('分组讨论 icon', 'Name', '分组讨论')
start_group_btn = ('开始分组btn', 'Name', '开始分组')
begin_discuss_btn = ('开始讨论btn', 'Name', '开始讨论')
end_discuss_btn = ('结束讨论btn', 'Name', '结束讨论')
re_group_btn = ('重新分组btn', 'Name', '重新分组')
re_discuss_btn = ('再次讨论btn', 'Name', '再次讨论')
group_win = ('分组讨论窗口', 'ClassName', 'StartGroupWidget')
group_win_close = ('分组讨论窗口关闭', 'ClassNames', 'QToolButton')


# 浏览器
browser_icon = ('浏览器 icon', 'Name', '浏览器')
browser_win = ('浏览器窗口', 'ClassName', 'WebShareWidget')
browser_win_close = ('浏览器窗口关闭', 'ClassNames', 'QToolButton')
browser_url_edit = ('编辑输入网址', 'ClassName', 'WebShareSearchLineEdit')


# 视频墙
video_icon = ('视频墙 icon', 'Name', '视频墙')
wall_win = ('视频墙打开后的窗口', 'ClassNames', 'ShadowWindowContainer')
wall_switch_screen = ('视频墙窗口切换', 'ClassNames', 'QPushButton')
wall_save = ('视频墙窗口-保存', 'ClassNames', 'QPushButton')
wall_save_win = ('视频墙-保存分享-窗口', 'ClassNames', 'ShadowWindowContainer')
save_local = ('保存至本地-by name', 'Name', '保存至本地')
save_yunpan = ('保存至云盘-by name', 'Name', '保存至云盘')
share_classin = ('分享至ClassIn-by name', 'Name', '分享至ClassIn')
copy_picture = ('复制图片-by name', 'Name', '复制图片')
save_win_close = ('视频墙-保存和分享-关闭btn', 'ClassNames', 'QToolButton')
wall_setting = ('视频墙窗口-设置', 'ClassNames', 'QPushButton')
video_site = (('视频墙-摄像头', 'ClassNames', 'VideoItemWidget'))
wall_win_close = ('视频墙窗口-关闭btn', 'ClassNames', 'QPushButton')


# 教学素材库
material_icon = ('教学素材库 icon', 'Name', '教学素材库')
material_win = ('教学素材库 窗口', 'ClassName', 'ShadowWindowContainer')
material_win_close = ('教学素材库-窗口-关闭', 'ClassNames', 'QToolButton')#[1]
material_subject = ('素材分类项目', 'XPaths', "//div[@class='handleFont']")
material_item = ('素材项', 'XPaths', "//div[@class='material-border']")


# 尺规工具
ruler_icon = ('尺规工具 icon', 'Name', '尺规工具')
ruler_win = ('尺规工具 窗口', 'ClassName', 'RulerGaugeToolSelectWidget')
ruler_win_close = ('尺规工具 窗口 关闭', 'ClassName','QToolButton')
ruler_item = ('尺规工具项', 'ClassNames','QPushButton')


# 几何图形
geometry_icon = ('几何图形 icon', 'Name', '几何图形')
geometry_win = ('几何图形 窗口', 'ClassName', 'GeometrySelectWidget')
geometry_win_close = ('几何图形 窗口 关闭', 'ClassName','QToolButton')
geometry_item = ('几何图形项', 'ClassNames','QToolButton')


# 投屏工具---------------hk
touping_icon = ('投屏 icon', 'Name', '投屏工具')
touping_select_win = ('投屏工具主窗口', 'ClassName', 'MirrorSelectWidget')
touping_classIn_btn = ('calssIn投屏', 'ClassName', 'ToolDescriptionButton')
touping_apple_btn = ('苹果投屏', 'ClassName', 'ToolDescriptionButton')
touping_classin_win = ('投屏二级窗口', 'ClassName', 'EeoMirrorWidget')
touping_apple_win = ('投屏二级窗口', 'ClassName', 'MirrorWidget')
sound_local_btn = ('本地播放声音btn', 'Name', '本地播放声音')
sound_share_btn = ('共享声音btn', 'Name', '共享声音')
touping_win_close = ('投屏窗口关闭', 'ClassNames', 'QToolButton')


# 随机选人
xuanren_icon = ('随机选人 icon', 'Name', '随机选人')
xuanren_win = ('随机选人窗口', 'ClassName', 'LotteryWidget')
choose_stu_btn = ('选择学生下拉框', 'ClassName', 'ComboBoxInRoom')
all_stu_btn = ('全部学生btn', 'Name', '全体学生')
online_stu_btn = ('在线学生btn', 'Name', '在线学生')
xuanren_start_btn = ('开始btn', 'ClassName', 'QPushButton')
xuanren_win_close = ('随机选人窗口关闭', 'ClassNames', 'QToolButton')


# 协作
xiezuo_icon = ('协作 icon', 'Name', '协作')
xiezuo_win = ('协作窗口', 'ClassName', 'CollaborationTypeWidget')
wenben_btn = ('文本 btn', 'ClassName', 'DesktopShareSelectButton')
wenben_win = ('文本输入框win', 'ClassName', 'CodeEditorWidget')
wendang_win = ('文档输入框win', 'ClassName', 'DocumentEditorWidget')
wenben_context_btn = ('文本内容输入框', 'ClassName', 'OsrWidgetCpu')
save_btn = ('保存按钮', 'Name', '保存')
save_local_btn = ('保存至本地', 'Name', '保存至本地')
confirm_btn = ('确认按钮', 'Name', '确认')
wendang_btn = ('文本 btn', 'ClassName', 'DesktopShareSelectButton')
wendang_context_btn = ('文档内容输入框', 'ClassName', 'OsrWidgetCpu')
wenben_win_close = ('文本窗口关闭', 'ClassNames', 'QToolButton')

# 奖励排行榜
reward_rank_icon = ('奖励排行榜 icon', 'Name', '奖励排行榜')
rank_win = ('排行榜窗口', 'ClassName', 'RewardListWidget')
rank_win_close = ('排行榜窗口关闭', 'ClassName', 'QToolButton')

# 辅助摄像头
assist_camera_icon = ('辅助摄像头 icon', 'Name', '辅助摄像头')
camera_win = ('辅助摄像头 窗口', 'ClassName', 'TeachingCameraWidget')
camera_win_close = ('辅助摄像头口关闭', 'ClassNames', 'QToolButton')

# 围棋小黑板
go_icon = ('围棋小黑板 icon', 'Name', '围棋小黑板')
go_win = ('围棋小黑板 win', 'ClassName', 'SgfInitDialog')
lushu_btn = ('围棋路数', 'ClassNames', 'QPushButton')
color_select_btn = ('执棋颜色', 'ClassNames', 'QPushButton')
go_win_close = ('围棋窗口关闭', 'ClassName', 'QPushButton')
board_win = ('棋盘 win', 'ClassName', 'Standalone::TabBlackboardWidget')
board_ele = ('出棋', 'ClassName', 'QStackedWidget')
push_btn = ('QPushButton', 'ClassName', 'QPushButton')
tool_btn = ('QToolButton', 'ClassName', 'QToolButton')

"""作业区域"""





"""课堂笔记区域"""
noteLocation = ('课堂笔记区域', 'ClassName', 'LessonNoteWidget')
# 添加笔记button
noteadd_icon = ('添加笔记button', 'ClassName', 'NoteAddBtn')
# 添加笔记文字text
notetext_icon = ('添加笔记文字text', 'ClassNames', 'NoteTextEdit')
# 笔记图片,点击可以查看
notelabel_icon = ('笔记图片', 'ClassName', 'ImageLabel')
# 笔记图片查看--窗口
image_win = ('笔记图片查看--窗口', 'ClassName', 'ImagePreview')
# 笔记图片查看--窗口--最大化
image_win_title_maximize = ('笔记图片查看--窗口--最大化', 'ClassName', 'QPushButton')
# 笔记图片查看--窗口--关闭
image_win_close = ('笔记图片查看--窗口--关闭', 'ClassName', 'QPushButton')
# 笔记图片查看--窗口--编辑文字
image_win_edit_text = ('笔记图片查看--窗口--编辑文字', 'ClassName', 'QTextEdit')
# 笔记图片查看--窗口--tool--1:1\放大\缩小\转向\另存
image_win_edit_tool = ('笔记图片查看--窗口--编辑工具', 'ClassName', 'QPushButton')
# 笔记图片查看--窗口--编辑---暂
note_win_close = ('课堂笔记窗口关闭', 'ClassName', 'QPushButton')




"""聊天区域"""
chatLocation = ('聊天区域', 'ClassName', 'ChatInClassTab')
# 聊天框
chat_widget = ('聊天框整体', 'ClassName', 'ChatInClassSendWidget')
# 聊天框--表情icon
chat_emoji = ('聊天框--表情icon', 'ClassNames', 'EeoHoverButton')
# 聊天框--截图icon
chat_cut = ('聊天框--截图icon', 'ClassNames', 'EeoHoverButton')
# 聊天框--文字编辑
chat_text_edit = ('聊天框--文字编辑', 'ClassName', 'ChatTextEdit')
# 聊天框--发送button
chat_send_btn = ('聊天框--发送button', 'ClassName', 'QPushButton')
# 聊天区域--关闭
chat_win_close = ('聊天区域--关闭', 'ClassNames', 'QToolButton')



"""花名册区域"""
rosterLocation = ('聊天区域', 'ClassName', 'RosterWidget')
# 花名册--窗口--搜索
roster_win_search =  ('花名册--窗口--关闭', 'ClassName', 'RosterSearchEdit')
# 花名册--窗口--关闭
roster_win_close =  ('花名册--窗口--关闭', 'ClassName', 'QToolButton')
# 花名册-班级学生tab
roster_stu_tab = ('花名册--班级学生tab', 'ClassNames', 'RosterTabButton')
# 花名册-班级学生表格
roster_stu_table = ('花名册--班级学生表格', 'ClassNames', 'RosterTableView')
# 花名册-表格-title
roster_table_name = ('花名册--表格-学生姓名', 'Name', '学生姓名')
roster_table_on = ('花名册--表格-上台', 'Name', '上台')
roster_table_empower = ('花名册--表格-授权', 'Name', '授权')
roster_table_silence = ('花名册--表格-禁言', 'Name', '禁言')
roster_table_mike = ('花名册--表格-麦克风', 'Name', '麦克风')
roster_table_camera = ('花名册--表格-摄像头', 'Name', '摄像头')
roster_table_award = ('花名册--表格-奖励', 'Name', '奖励')
roster_table_handup = ('花名册--表格-举手', 'Name', '举手')
roster_table_out = ('花名册--表格-移出', 'Name', '移出')
roster_table_device = ('花名册--表格-设备', 'Name', '设备')
roster_table_teacher = ('花名册--表格-联席教师', 'Name', '联席教师')
# 花名册-班级学生表格-表格项
roster_stu_table_item = ('学生tab表格下的孩子们', 'XPaths', "//*[@ClassName='RosterTableView']/*[@FrameworkId='Qt']")
OutMessageBox = ('花名册移出学生的系统提示', 'ClassName', 'OutMessageBox')
# 花名册-联席教师tab
roster_tea_tab = ('花名册--联席教师tab', 'ClassNames', 'RosterTabButton')
# 花名册-联席教师表格
roster_tea_table = ('花名册--联席教师表格', 'ClassNames', 'RosterTableView')
# 花名册-教师操作功能区域
roster_tea = ('花名册-老师操作区域功能', 'ClassName', 'RosterTeacherWidget')
# 花名册-摄像头复原
roster_tea_camera_reset = ('花名册-老师操作-摄像头复位', 'ClassNames', 'QToolButton')
# 花名册-全体静音/全体取消静音
roster_tea_mute = ('花名册-老师操作-全体静音/全体取消静音', 'ClassNames', 'QToolButton')
# 花名册-全体下台
roster_tea_stu_off = ('花名册-老师操作-全体下台', 'ClassNames', 'QToolButton')
# 花名册-台上学生授权/取消授权
roster_tea_stu_empower = ('花名册-老师操作-全体授权', 'ClassNames', 'QToolButton')
# 花名册-开启轮播
roster_tea_lunbo_open = ('花名册-老师操作-开启轮播', 'Name', '开启')
# 花名册--轮播--人员选择框
roster_lunbo_who = ('花名册--轮播--人员选择框', 'ClassNames', 'ComboBoxInRoom')
# 花名册--轮播--人员选择--所有人
roster_lunbo_all = ('花名册--轮播--人员选择--所有人', 'Name', '所有人')
# 花名册--轮播--人员选择--非禁用
roster_lunbo_part = ('花名册--轮播--人员选择--非禁用', 'Name', '非禁用')
# 花名册--轮播--顺序选择框
roster_lunbo_order = ('花名册--轮播--顺序选择框', 'ClassNames', 'ComboBoxInRoom')
# 花名册--轮播--顺序选择--顺序
roster_lunbo_shunxu = ('花名册--轮播--顺序选择--顺序', 'Name', '顺序')
# 花名册--轮播--顺序选择--随机
roster_lunbo_suiji = ('花名册--轮播--顺序选择--随机', 'Name', '随机')


"""抢答器区域"""
Responder_icon = ('抢答器 icon', 'Name', '抢答器')
Responder_start = ('抢答器-开始', 'Name', 'start')
Responder_btnclose = ('抢答器-关闭', 'Name', 'btnclose')
Responder_btnagain = ('抢答器-重新开始', 'Name', 'btnagain')









#####################学生端，元素获取
# 举手
StuHandUp = ('举手上台button', 'ClassName', 'StudentHandupButton')