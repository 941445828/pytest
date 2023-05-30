#### LMS-课程下，稳定性测试说明

##### 一、测试内容包括：
    1. LMS各活动
        新建：课堂、录播课、作业、测验、讨论、学习资料、单元主题
        操作：复用其他班级课程、查看学生成绩
        编辑：课堂、录播课、作业、测验、讨论、学习资料
        
    2. 在线教室内，各功能定向遍历操作
    
##### 二、环境搭建:
    
    1. python3.6 【为适用其他脚本功能，最好安装版本3.6】
       如下，可下载python3.6.5
       https://www.python.org/ftp/python/3.6.5/python-3.6.5-amd64.exe
    
    2. 安装 WinAPPDriver：
       使用版本：WindowsApplicationDriver-1.2.99
       下载地址：https://github.com/microsoft/WinAppDriver/releases
       
       2.1. 下载
[![zB6d8e.png](https://s1.ax1x.com/2022/12/02/zB6d8e.png)](https://imgse.com/i/zB6d8e)
        
       2.2. 安装【可以通过点击option，更换安装路径】
[![zBcPIK.png](https://s1.ax1x.com/2022/12/02/zBcPIK.png)](https://imgse.com/i/zBcPIK)

       2.3. 安装后，在所安装选路径找到WinAppDriver.exe 并点击启动
[![zBc3Rg.png](https://s1.ax1x.com/2022/12/02/zBc3Rg.png)](https://imgse.com/i/zBc3Rg)
       
       注： 运行脚本前，先启动WinAppDriver.exe
       
    3. 配置Windows，开启开发者模式：
       3.1 在Windows设置中，搜索“开发者设置”：
   [![zE8kp6.png](https://s1.ax1x.com/2022/11/15/zE8kp6.png)](https://imgse.com/i/zE8kp6)
       
       3.2 模式选择打开：
   [![zEeZIU.png](https://s1.ax1x.com/2022/11/15/zEeZIU.png)](https://imgse.com/i/zEeZIU)
      
    4. 安装依赖  
       使用命令： pip3 install -r ./requirements.txt
       安装pyHook：
       D:\PC-STORY>pip3.6 install tools\pyHook-1.5.1-cp36-cp36m-win_amd64.whl
       
    
##### 三、【重要】运行脚本前，配置内容：

    1.1 配置文件，更新 ./config/stability_conf.py
            APP_URL -- ClassIn.exe应用程序路径，确保切到15环境
            LOGIN_USER_NAME、LOGIN_PASS_WORD -- 登录用户名&密码
            CLASSNAME -- 功能运行所需班级(最好置顶，以防首屏找不到)，例如：新建的LMS活动都会放在这个班级下
            YUNPANFLODER -- 功能运行所需云盘下的文件夹，例如：上传视频文件需要，教室内打开课件需要
            CLASSFORCOPY -- 复用其他班级课程需要，最好置顶，以防首屏找不到；被复用的的单元下活动不要太多，以防被复制时超100个，失败
            online_loop -- int，功能循环使用次数
            files -- 云盘文件夹YUNPANFLODER下的课件列表
            
    1.2 其他前置配置需求
        确保所配置的班级CLASSNAME下，至少有两名学生存在(否则分组讨论功能不可用)
        云盘文件夹YUNPANFLODER，需要存在一个视频文件--.mp4、.3g2、.3gp等ClassIN支持的视频格式文件



##### 四、运行：
    
    1. 选择版本：
        框架采用版本分离，在version目录下选择使用版本号
        例如，迭代发版的客户端版本号为v5.0.0.X， 使用目录V5000；
        迭代发版的客户端版本号为v5.0.1.X， 使用目录V5010
        
    2. 下载ClassIn测试版本
        \\10.0.0.100\build\classin\xxxxx，下取要测试包
       
    3. 启动WinAppDriver.exe
    
    4. 运行脚本：
             
       4.1 课程下，各活动操作：
            新建：课堂、录播课、作业、测验、讨论、学习资料、单元主题
            操作：复用其他班级课程、查看学生成绩
            编辑：课堂、录播课、作业、测验、讨论、学习资料
            运行脚本： run/stability/run_class_course.py
            
        4.2 在线教室内，各功能定向遍历操作
            运行脚本：run/stability/run_online_classroom_stability.py
            ***本脚本注意事项***：
            ①：在线教室内工具栏顺序需为：点击、选择、画笔、橡皮擦、文本工具、截图、激光笔、云盘、工具箱、课程、课堂笔记、聊天、花名册， 否则容易报错
            ②：教室内工具箱默认展示两行，需要保证各工具占位顺序如下，否则容易报错。
               默认展示：
               第一行：打开文件、保存/分享板书、屏幕共享、骰子； 第二行：答题器、小黑板、计时器、定时器
               展开更多后展示：
               第三行：投屏工具、抢答器、随机选人、分组讨论； 第四行：协作、奖励排行榜、浏览器、物理实验
               第五行：化学实验、教学素材库、辅助摄像头、VNC； 第六行： 作业、测验、拖拽激光笔、 直播聊天
               第七行：视频墙、 围棋小黑板、尺规工具、几何图形。
            ③： 使用投屏工具功能时，首次使用会有系统弹窗，可以先行人工干预，关闭弹窗
            ④云盘下的元素定位，匹配使用默认的网格视图查找 （列表视图会找不到）
            
       
       稳定性相关脚本，汇总运行：run/stability/run_stability.py
       【注：现开启的是汇总运行脚本。若只运行LMS稳定性脚本，将run/stability/run_class_course.py最下面现注释的2行代码取消注释 后运行即可】
       
       
##### 五、其他说明：
    1. WinAppDriver 支持Win10及以上的系统
    2. 开发自动化case，需要安装Visual Studio， 使用inspect.exe 识别UI元素