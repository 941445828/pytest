#### lang_ts说明：

##### 一、 创建文件夹 D:\lang  （用于存放git clone 后的文件）

##### 二、 创建文件夹 D:\lan_old （用于存放旧版本ts 文件）

##### 三、 创建文件夹 D:\PC， 在文件夹PC下，使用git bash here

##### 四、 脚本及使用说明：

    1. getTS.py: 
        从git获取源码， 步骤：
        a. 将 D:\lang\lang\lan\ 下的所有文件，移动到 D:\lan_old\ 下
        (若对比文件试用本地自己备份的文件，则不需要运行方法move_to_backup())
        b. 将 D:\lang\ 下的其他文件删除
        c. 切换目录到 D:\lang\ 下， git clone https://gl.eeo.im/classin/lang.git 
       
    2. readTS.py：
        解析各个ts文件，遍历出节点的’translation‘ text为空以及attrib是unfinished的节点
        （无需解析en_classin.ts文件里的空值及unfinished）
        
    3. compare.py：
        文件对比，输出增、删、更新的节点