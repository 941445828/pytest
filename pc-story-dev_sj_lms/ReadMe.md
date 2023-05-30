##### 一、概述
    本项目从获取UI元素入手，对ClassIn.exe进行性能、稳定性、场景等方面的测试

##### 二、环境搭建:
    
    1. python3.6 【为适用其他脚本功能，最好安装版本3.6】
       如下，可下载python3.6.5
       https://www.python.org/ftp/python/3.6.5/python-3.6.5-amd64.exe
    
    2. 安装 WinAPPDriver：
       使用版本：WindowsApplicationDriver-1.2.99
       下载地址：https://github.com/microsoft/WinAppDriver/releases
       注： 运行脚本前，先启动WinAppDriver.exe
       
       2.1. 下载
[![zB6d8e.png](https://s1.ax1x.com/2022/12/02/zB6d8e.png)](https://imgse.com/i/zB6d8e)
        
       2.2. 安装【可以通过点击option，更换安装路径】
[![zBcPIK.png](https://s1.ax1x.com/2022/12/02/zBcPIK.png)](https://imgse.com/i/zBcPIK)

       2.3. 安装后，在所安装选路径找到WinAppDriver.exe 并点击启动
[![zBc3Rg.png](https://s1.ax1x.com/2022/12/02/zBc3Rg.png)](https://imgse.com/i/zBc3Rg)
       
       
    3. 配置Windows，开启开发者模式：
       3.1 在Windows设置中，搜索“开发者设置”：
   [![zE8kp6.png](https://s1.ax1x.com/2022/11/15/zE8kp6.png)](https://imgse.com/i/zE8kp6)
       
       3.2 模式选择打开：
   [![zEeZIU.png](https://s1.ax1x.com/2022/11/15/zEeZIU.png)](https://imgse.com/i/zEeZIU)
      
    4. 安装依赖  
       使用命令： pip3 install -r ./requirements.txt
       安装pyHook：
       D:\PC-STORY>pip3.6 install tools\pyHook-1.5.1-cp36-cp36m-win_amd64.whl
       
    
##### 三、【重要】配置说明：
    1. 稳定性相关
    
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

    2. 性能相关
        待完善
        
    3. 场景相关
        待完善
        
##### 四、运行说明：
    1. 下载ClassIn版本
        \\10.0.0.100\build\classin\lms-portable-log\win7，取测试包
        
    2. 更改测试包的配置：
       解压后的文件夹下文件EEOServerProxy.ini里：更新 LB_SERVER=lb15.eeo.im
       
    3. 启动WinAppDriver.exe
    
    4. 运行脚本： 详细说明见五
       
       
##### 五、 脚本实现
    1. 稳定性相关
        1.1 课程下，各活动操作：
            新建：课堂、录播课、作业、测验、讨论、学习资料、单元主题
            操作：复用其他班级课程、查看学生成绩
            编辑：课堂、录播课、作业、测验、讨论、学习资料
            运行脚本： run/stability/run_class_course.py
            
        1.2 在线教室内，各功能定向遍历操作
            运行脚本：run/stability/run_online_classroom_stability.py
            
        稳定性相关脚本，汇总运行：run/stability/run_stability.py
        
    2. 性能相关：
        2.1 场景一，收集CPU/MEM使用情况数据：
            登录APP--创建班级--创建课节（在线&录课模式）--进入教室--打开一个课件--课件打开后在教室内停留60s--退出教室--退出APP
            运行脚本： run/perf/run_online_luke_openfile.py
            将获取的cpu/mem数据绘图： functs/useDraw.py 
          
        2.2 场景二,
            登录APP--创建班级--创建课节（在线&非录课模式）--进入教室--打开一个课件--课件打开后在教室内停留60s--退出教室--退出APP
            运行脚本： run/perf/run_online_noluke_openfile.py
            将获取的cpu/mem数据绘图： functs/useDraw.py
        
    3. 场景相关：
        3.1 登录--切换多语言，验证”设置“显示的是否是对应语言的内容
            运行脚本：run/story/run_ts.py
            
        3.2 数据构造： 班级内，发布5000条聊天数据
            运行脚本： run/story/run_class_chat.py
            
        3.3 老师批阅作业，验证留痕正确性
            运行脚本： run/story/run_hw_review.py
                  
##### 六、其他说明：
    1. WinAppDriver 支持Win10及以上的系统
    2. 开发自动化case，需要安装Visual Studio， 使用inspect.exe 识别UI元素