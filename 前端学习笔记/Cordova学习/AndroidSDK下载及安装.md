 

### 一、下载：

Android SDK包下载

*   官网下载：[Download Android SDK - free - latest version](http://android-sdk.en.softonic.com/download "Download Android SDK - free - latest version")
*   网盘下载：[Android SDK 百度网盘下载地址链接](http://tools.android-studio.org/index.php/sdk "Android SDK 百度网盘下载地址链接")
*   下载地址https://www.androiddevtools.cn/

### 二、安装Android SDK Tools

双击运行已下载的.exe安装包，

![](https://img-blog.csdnimg.cn/7d0865ca864f45e59f6c908919208caa.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6JCn5rC06Zuo5a-S,size_20,color_FFFFFF,t_70,g_se,x_16)

![](https://img-blog.csdnimg.cn/80bc182055f24078ac4228ca52c73264.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6JCn5rC06Zuo5a-S,size_17,color_FFFFFF,t_70,g_se,x_16)

自动检测JDK的安装环境

![](https://img-blog.csdnimg.cn/1d3ee9f80a9d478284d80386db6d12be.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6JCn5rC06Zuo5a-S,size_17,color_FFFFFF,t_70,g_se,x_16)

 ![](https://img-blog.csdnimg.cn/b7faac2b033a4eb8953625f799099b30.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6JCn5rC06Zuo5a-S,size_17,color_FFFFFF,t_70,g_se,x_16)

 ![](https://img-blog.csdnimg.cn/648f66cac83442ee8b858de97096928d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6JCn5rC06Zuo5a-S,size_17,color_FFFFFF,t_70,g_se,x_16)

 注意：安装路径应避免选择中文或特殊字符路径

![](https://img-blog.csdnimg.cn/461169b825504cfa9fb15dd0e4f7b1e7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6JCn5rC06Zuo5a-S,size_17,color_FFFFFF,t_70,g_se,x_16)

###  三、下载安装Android SDK

Android SDK Tools安装后，启动SDK Manager.exe：

![](https://img-blog.csdnimg.cn/326fb506fdf144c19eaab5d1e3983458.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6JCn5rC06Zuo5a-S,size_20,color_FFFFFF,t_70,g_se,x_16)

#### Tools目录：

Android SDK Manager Packages Tools

**Android SDK Tools**（必须，只需下载一个版本，一般选最新版本）：基础工具包，版本号带rc字样的是预览版。

**Android SDK Platform-tools**（必须，只需下载一个版本，一般选最新版本）：从Android2.3开始划出此目录，存放公开开发工具，比如[adb](https://so.csdn.net/so/search?q=adb&spm=1001.2101.3001.7020)、sqlite3等，被划分到了这里。

**Android SDK Build-tools**（必须，可以安装多个版本）：[Android项目](https://so.csdn.net/so/search?q=Android%E9%A1%B9%E7%9B%AE&spm=1001.2101.3001.7020)构建工具。

\*\*Android xxx（API xx）\*\*目录（可选的各平台开发工具）：

*   Documentation for AndroidSdk（可选）：安卓开发者官网的一些离线文档，不过下载下来代开也很慢，后面会提供另外一个离线版。
*   **SDK Platform**（必须）：对应平台的开发工具，需要在哪个版本的平台下开发就下载哪个。
*   Samples for SDK（可选，此项在高版本tools中已不提供，需要在IDE里通过Import Sample引入，当然也可以下载离线版）：内置的安卓示例程序，推荐安装。
*   Sources for Android SDK（可选）：安卓API的源代码，推荐安装。 -ARM/Intel xxxx Image（可选）：各个以Image结尾的东西是支持响应平台的模拟器，我们就把它想象成一个刷机包吧。（使用真机调试或使用其它模拟器的话不需要安装）

**Extras目录**（可选的扩展）：

*   Android Support Repository（可选）：主要是方便在gradle中使用Android Support Libraries，因为Google并没有把这些库发布到maven center或者jcenter去，而是使用了Google自己的maven仓库。
*   Intel x86 Emulator Accelerator(HAXM installer)(可选)：windows平台的Intel x86模拟器加速工具，配合Intel x86 atom/atom\_64 System Image使用可以加快模拟器的运行速度。

####  下载安装**Android SDK Tools工具**![](https://img-blog.csdnimg.cn/c1c3cc216996493d971f44c9eb2114f8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6JCn5rC06Zuo5a-S,size_20,color_FFFFFF,t_70,g_se,x_16)

 ![](https://img-blog.csdnimg.cn/b9065c9f4bd849c3a3a65fa1b7596fb9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6JCn5rC06Zuo5a-S,size_20,color_FFFFFF,t_70,g_se,x_16)

 ![](https://img-blog.csdnimg.cn/02cfb1042e3747b481d5e061938f700e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6JCn5rC06Zuo5a-S,size_20,color_FFFFFF,t_70,g_se,x_16)

![](https://img-blog.csdnimg.cn/cbc877095f804939b69fb01cc19f2448.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6JCn5rC06Zuo5a-S,size_20,color_FFFFFF,t_70,g_se,x_16)

 点击下载

![](https://img-blog.csdnimg.cn/3583dc87b8914dd79fd61bc997f1a910.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6JCn5rC06Zuo5a-S,size_20,color_FFFFFF,t_70,g_se,x_16)

 确认文件下载

![](https://img-blog.csdnimg.cn/6380726816e245a7bd5b39f838159c4f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6JCn5rC06Zuo5a-S,size_20,color_FFFFFF,t_70,g_se,x_16)

![](https://img-blog.csdnimg.cn/2748de217ca844b890949ee30e573b10.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6JCn5rC06Zuo5a-S,size_20,color_FFFFFF,t_70,g_se,x_16)

下载安装完成后，配置AndroidSDK的环境变量

###  三、环境变量配置

1、添加系统变量，变量名：ANDROID\_HOME，变量值为：SDK安装路径（如下：）

![](https://img-blog.csdnimg.cn/64404cff5bfb4437a9d1aded8190818e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6JCn5rC06Zuo5a-S,size_20,color_FFFFFF,t_70,g_se,x_16)

 添加Path路径：

1）添加 Android新版API 安装路径（在SDK安装目录下）

2）添加 tools安装路径（在SDK安装目录下）

3）添加platform-tools 安装路径（在SDK安装目录下）

![](https://img-blog.csdnimg.cn/d89912061ee74923aeab3085a991f4fa.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6JCn5rC06Zuo5a-S,size_20,color_FFFFFF,t_70,g_se,x_16)

 安装完成

本文转自 <https://blog.csdn.net/DaisyCold/article/details/122602714>，如有侵权，请联系删除。