 

#### MongoDB下载安装教程

*   [1、下载](#1_3)
*   [2、安装](#2_7)
*   [3、启动mongoDB](#3mongoDB_42)
*   *   [3.1、在windows的任务管理器中启动mongoDB](#31windowsmongoDB_43)
    *   [3.2、双击mongo.exe，启动mongodb](#32mongoexemongodb_45)
    *   [3.3、在此处输入命令，操作数据库](#33_53)
*   [4、操作mongoDB数据库的一些基础命令](#4mongoDB_55)
*   *   [4.1、数据库操作命令](#41_56)
    *   [4.2、MongoDB操作集合（表）的常用命令](#42MongoDB_78)

1、下载
----

[mongodb官网下载](https://www.mongodb.com/try/download/community)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531163211189.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)

2、安装
----

1、双击下载好的文件  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531163329193.png)  
2、点击next:  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531163341365.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)  
3、接受协议，点击next  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531163422210.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)4、选择complete，完整安装（安装全部组件）  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531163747923.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)

5、修改默认的安装位置  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531163554723.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)6、修改好安装路径，点击next  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531163608404.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)7、选择服务及安装路径  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531163907432.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)  
data目录是数据存储目录，数据库中的数据就存储在这个目录中。log是日志文件的输出目录。

需要在该盘的根目录下新建一个data文件夹（必须要是MongoDB安装盘符的根目录下），在data文件夹下创建db子文件夹（存放数据库文件）、log子文件夹（存放日志文件）。然后再把上面的data目录修改为我们刚才创建的db文件夹的路径。如果不修改data路径，会出现一些问题；log路径改不改都行，影响不大。

启动MongoDB服务服务时，会先检查db目录下是否有所需的文件、文件夹，没有就自动创建，有就从中读取数据，初始化服务器。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531164029650.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)  
8、点击install，进行安装  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531164201740.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)9、正在安装  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531164234463.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)  
10、安装成功，点击finish  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531164313270.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)  
11、打开任务管理器，monogodb已经启动  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531164537950.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)  
12、打开本地看到已经做好了mongodb配置  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531164710427.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)

3、启动mongoDB
-----------

### 3.1、在windows的任务管理器中启动mongoDB

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531170139874.png)

### 3.2、双击mongo.exe，启动mongodb

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531174108282.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)

在浏览器访问：[http://127.0.0.1:27017/](http://127.0.0.1:27017/)出现如下页面证明mongoDb启动成功。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531170121931.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)

### 3.3、在此处输入命令，操作数据库

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210531174559675.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)

4、操作mongoDB数据库的一些基础命令
---------------------

### 4.1、数据库操作命令

一个mongodb中可以建立多个数据库  
常用操作：

```
1、 Help查看命令提示
db.help();
2、 切换/创建数据库
use test
如果数据库不存在，则创建数据库，否则切换到指定数据库
3、 查询所有数据库
show dbs;
4、 删除当前使用数据库
db.dropDatabase();
5、 查看当前使用的数据库
db.getName();
6、 显示当前db状态
db.stats();
7、 当前db版本
db.version();
8、 查看当前db的链接机器地址
db.getMongo〇;
```

### 4.2、MongoDB操作集合（表）的常用命令

[操作MongoDB集合（表）的常用命令](https://blog.csdn.net/qq_46112274/article/details/117422380)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210601115915641.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTEyMjc0,size_16,color_FFFFFF,t_70)

本文转自 <https://blog.csdn.net/qq_46112274/article/details/117420196>，如有侵权，请联系删除。