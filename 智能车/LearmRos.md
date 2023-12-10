# 使用Ubuntu


之后所有的内容都是基于虚拟机软件 VMware WorkStation Pro 16 与Ubuntu 20.04.1。  
我使用默认设置安装（虚拟机上安装Ubuntu教程这里省略，可以参考网上~）。  
Ubuntu操作系统是ROS的部署平台，所以熟悉一下这个基本常用命令。

### 1 设置中勾上使用开源软件并选择源

右上角下拉菜单选择“设置”→“关于”→“软件更新”  
前面四个打勾，并在“下载自”处选择“其他站点”选择合适的下载源，我选择了阿里云的服务器。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/e5f2e966cf7e4ba9bd1577dc161a9f99.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)点击系统界面的左下角可浏览软件列表，左边的公文包图标可打开软件中心管理安装软件，类似应用市场。

### 2 打开终端

类似Windows系统的命令提示符cmd。  
快捷键：Ctrl+Alt+T  
![在这里插入图片描述](https://img-blog.csdnimg.cn/ed9d515e929845d2b2d0a04ed94ed2a9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 3 显示目前文件目录：`pwd`

见上图  
Ubuntu系统只有一个盘，当前用户的资料存储在 根目录/home/用户名 下。

### 4 进入指定目录：`cd`

进入子目录：`cd 目录名`  
进入上一级目录`cd ..`  
![在这里插入图片描述](https://img-blog.csdnimg.cn/0b48cb8212a14597899992c800f4cc93.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 当前目录下打开文件夹（图形界面）

`open .`

### 5 文件夹操作

创建新文件夹 `mkdir 文件夹名`  
查看当前目录下所有文件 `ls`  
![在这里插入图片描述](https://img-blog.csdnimg.cn/6df4262210d44b9785b6423fd4936bee.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)



### 6 文件操作

创建新文件（类似创建空txt，打开可编辑）`touch 文件名`  
移动文件 `mv 文件名 /目标目录`。例：`mv test_file /home/ck`  
拷贝文件 `cp test_file 目标目录(/文件名)`。例：`cp test_file test_folder/test_file2`  
删除文件 `rm 文件名`  
删除文件夹 `rm -r 目录名`  
![在这里插入图片描述](https://img-blog.csdnimg.cn/76548226bf914c269f627b02b039383b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 7 指令使用帮助：`指令名 --help`

例：`cd --help`

### 8 以超级用户权限执行一些操作 `sudo`

例：安装、更新软件，如更新当前系统软件列表：`sudo apt-get update`

### 9 查看进程并关闭进程

查看全部进程信息：

    ps -aux


根据关键字查看具体的某个进程：

    ps -aux | grep 进程关键字


杀死进程：

    sudo kill 进程号(PID)


接着将是ROS的安装教程~

图摘自：B站【古月居】古月·ROS入门21讲

# What is ROS

![在这里插入图片描述](https://img-blog.csdnimg.cn/98335b5b86194b6c99228a759508892d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

*   ROS：Robot Operating System
*   包括了四个part：通信机制、开发工具、应用功能、生态系统
*   这种模式旨在提高机器人研发中的软件复用率

### 2 节点(Node) 与 节点管理器(Node Master)

![在这里插入图片描述](https://img-blog.csdnimg.cn/4e176d3440984762b9c3a67364daacb5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 3 通信模式之一——Topic模式

![在这里插入图片描述](https://img-blog.csdnimg.cn/4967afb3119c4a77823ace638eaf7c6d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

*   Message：定义数据的类型，具有一定的数据结构定义
*   单向的
*   数据的管道称为Topic（话题）
*   使用 发布&订阅 模型，右下图显示了Camera Node是发布者，图像处理节点和图像显示节点是订阅者。
*   话题的消息的接口使用 .msg 文件定义

### 4 通信模式之二——Service模式

![在这里插入图片描述](https://img-blog.csdnimg.cn/6486084570f84bd68fb5217515b3208b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

*   C/S模型
*   带有反馈的机制
*   双向的
*   如左下图，图像处理节点向Camera节点发出请求（比如上调图像分辨率），Camera节点上调分辨率后向图像处理节点发出反馈。
*   服务的数据内容可用 .srv 定义

### 5 两者对比

![在这里插入图片描述](https://img-blog.csdnimg.cn/7a30f08c96bc4e70a7214cc3ba439fd6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 6 参数(Parameter)

![在这里插入图片描述](https://img-blog.csdnimg.cn/aab061200b4246dcb85c75a9ae4dac1e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

*   参数是一个“字典”
*   存储在ROS Master服务器，节点可以对参数存储、检索、更新（如图）
*   适合静态存储、非二进制

### 7 文件系统

![在这里插入图片描述](https://img-blog.csdnimg.cn/82d41bfd7e0d49b983ded5a5291735d5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

*   文件系统代表了代码的结构。

([fin](https://so.csdn.net/so/search?q=fin&spm=1001.2101.3001.7020))

## 打开小海龟程序  

终端，启动ROS Master：

    roscore


终端2，启动小海龟仿真器：  
（输入`rosrun turtlesim`，敲两下`Tab`健可查看该命令下有哪些功能）

    rosrun turtlesim turtlesim_node


终端3，启动海龟控制节点：

    rosrun turtlesim turtle_teleop_key


![在这里插入图片描述](https://img-blog.csdnimg.cn/08404969ffd74d37873fc8b9bffad873.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 2 查看系统中的计算图：rqt\_graph

新建终端窗口：

    rqt_graph


可展示系统中运行的计算图：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/f5baccf923974d9c8b07eb8837eabdee.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)可以清晰地了解系统节点间通信的部分信息。  
teleop\_turtle节点（键盘控制节点）通过cmd\_vel（topic）向turtlesim节点（海归仿真器节点）发出消息，使得小海龟移动。

### 3 rosnode

#### 显示节点列表：rosnode list

![在这里插入图片描述](https://img-blog.csdnimg.cn/531a85e1fe014457ba8a1c723546c7a9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)可以看到有3个节点。

#### 查看节点信息：rosnode info

查看节点的具体信息：`rosnode info /节点名`  
我们查看海龟仿真器节点/turtlesim的信息：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/fd8666b15d154c89bf05f50da3f826b8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
可以看到海龟仿真器节点/turtlesim自己有一些发布和订阅，也有一些服务。

### 4 rostopic

#### 显示topic列表：rostopic list

![在这里插入图片描述](https://img-blog.csdnimg.cn/9883c9621c5a42e4b91762887acf9347.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 手动发布数据给topic

我们来手动发布数据给topic来控制海龟移动，使用`rostopic pub`  
上图我们看到小海龟是通过/cmd\_vel这个topic进行发布信息而移动的，这次我们通过手动publish数据给这个topic来控制小海龟移动。  
格式：`rostopic pub (参数) 话题名 消息数据结构 “具体数据”`  
例，我们输入：（我们可以使用Tab键让我们自动填充数据，使用方向键←→移动到指定位置修改数据，比如我们把x的0.0改成了1.0）

    rostopic pub /turtle1/cmd_vel geometry_msgs/Twist "linear:
      x: 1.0
      y: 0.0
      z: 0.0
    angular:
      x: 0.0
      y: 0.0
      z: 0.0"


小海龟沿着正前方向移动了1单位，我们再使用参数`-r 5`移动5次，小海龟就撞上了南墙。  
Ctrl+C就可以终止。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/c4677424712e4d73b9867f9205348324.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 5 rosmsg

#### 查看消息数据结构

上例我们使用了**消息数据结构**定义了一个消息传给topic，我们可以查看有哪些消息数据结构。  
查看消息数据结构使用：rosmsg show …  
在输入过程中，我们可以勤使用Tab键查看或填充内容。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/5bd07a3acc3a4e0cb32a2b77ebe50c5b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)我们可以看到geometry\_msgs/Twist数据结构的内容。

### 6 使用服务通信方式：rosservice

上例我们使用了向topic传msg来控制节点，这次我们试试第二种通信方式service。

#### 查看服务列表：rosservice list

![在这里插入图片描述](https://img-blog.csdnimg.cn/4a21ed9d28ec4eb184a7c1223c060d23.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 手动通过服务来进行操作

这次我们通过人工产生服务（service）来诞生一只新海龟，使用rosservice call /spawn …  
在服务列表中，有个/spawn服务，可以产生一只新的海龟。  
格式：`rosservice call (参数) 服务名 “具体数据”`  
![在这里插入图片描述](https://img-blog.csdnimg.cn/bec967eaa31348ec99077de94e7b964e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
这时我们再输入`rostopic list`，可以看到turtle2已经在topic里了。

### 7 话题记录和复现：rosbag

试想我们尝试让海龟以我们指定的路径移动了一回，我们想要把它 记录下来，拷贝到自己的实验室再复现出来，我们就可以使用话题记录功能。  
常用命令：`rosbag record -a -O 文件名`  
比如我们使用之前打开的键盘操作器让海龟移动一圈并记录下来：  
（1）打开新终端输入`rosbag record -a -O cmd_record`  
这样就开始记录了：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/13f9ea006b2641eebed9cfb05de7f840.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)（2）移动一下：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/d65cd6f9cf374c1db1852b70bd2237f4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)到记录界面按Ctrl+C停止：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/ca1fcfd010a246b9bec6ea82192612ef.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)文件就记录在了这里：![在这里插入图片描述](https://img-blog.csdnimg.cn/2ff6f212c85d46959c8f30bfab1ca38f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
（3）接下去关闭所有打开的ros节点  
重新开启roscore，开启海龟节点rosrun turtlesim turtlesim\_node  
这时我们输入 `rosbag play cmd_record`就可以复现之前的移动啦！  
![在这里插入图片描述](https://img-blog.csdnimg.cn/b90fa322ecc84e1baf3cf109614b9a39.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

 ### 1 What is Workspace(工作空间)

**工作空间**（Workspace）：存放工程开发相关文件的文件夹。类似一个IDE（例如Pycharm）新建一个工程，就是一个工作空间。包含4个文件夹：

*   src：**代码空间**（Source Space）：放置功能包代码
*   build：**编译空间**（Build Space）：编译过程中产生的中间文件，不用过多关注
*   devel：**开发空间**（Development Space）：放置编译生成的可执行文件、库、脚本
*   install：**安装空间**（Install Space）：存放可执行文件，与上面有一定重复  
    例图：  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/cee788aa31e5411eaa1a46589ff64cc5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

# 创建工作空间

#### 创建

    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws/src
    catkin_init_workspace


我们先创建一个src文件夹，然后进入该文件夹  
第3行`catkin_init_workspace`意为将当前文件夹变为工作空间，使其拥有工作空间的属性  
注：“~/”意为当前用户名目录；“-p”意为递归创建目录，即直接创建多级目录。  
src文件夹即代码空间，不能自行用别的名称代替  
![在这里插入图片描述](https://img-blog.csdnimg.cn/c0ddeba08a534e42951589498f14babf.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)可以看到创建了这么一个txt文件，说明创建工作空间成功。

#### 编译空代码的工作空间

要编译工作空间，先要回到工作空间的根目录。

    cd ~/catkin_ws
    catkin_make


第二行`catkin_make`为编译指令，将src里的源码都进行编译。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/a5beed1f46eb4bdbacdd3bf1f7a4ca73.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)可以看到生成了build和devel两个新文件夹，devel存放了编译完成的内容。  
这里没有生成install文件夹，要生成install文件夹，输入`catkin_make install`：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/04e2af2c3ef94b2e8ff3c27da461e3b5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)install中生成了可执行文件。  
这样一个空的工作空间创建好了，并且空的代码空间（功能包）编译完成。

### 3 创建功能包

**功能包**是放置ROS源码的最小单元。  
上面我们创建了一个空的工作空间，src文件夹里面没写东西，现在我们创建一个自己的功能包。  
注意同一工作空间下，不允许存在同名功能包；不同工作空间下，允许存在同名功能包。

#### 创建

指令格式：`catkin_create_pkg <package_name> [depend1] [depend2] [depend3]`  
<package\_name>为包名  
\[depend\]为依赖，即指明编译的时候需要ROS中的其他功能包，如需要调用python、C++库，就要指明rospy、roscpp。  
我们创建功能包：

    cd ~/catkin_ws/src
    catkin_create_pkg test_pkg std_msgs rospy roscpp


![在这里插入图片描述](https://img-blog.csdnimg.cn/7ffd4fd7d2d246a08b7180892ad1ed43.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
创建成功，我们可以打开文件夹见到我们的目录结构(上图)。

#### 编译新的功能包

回到工作空间根目录，再编译一下。

    cd ~/catkin_ws
    catkin_make


![在这里插入图片描述](https://img-blog.csdnimg.cn/4d6f1dfb55a540cb843112934982b4bb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 4 设置和检查环境变量

#### 设置

编译完功能包后，为了运行，先设置环境变量，以便系统找到我们的工作空间和功能包。

    source ~/catkin_ws/devel/setup.bash


#### 检查

    echo $ROS_PACKAGE_PATH


echo为打开环境变量，通过 ROS\_PACKAGE\_PATH 查找所有ros功能包的路径。  
前面source了 devel/setup.bash ，现在就会包含这个路径：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/cff1429ccf74450f84d305159394e556.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_16,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 5 功能包中的两个重要文件

#### package.xml

使用xml语言描述功能包相关的信息：  
（后面的课会用到）  
![在这里插入图片描述](https://img-blog.csdnimg.cn/d884d9ac35794a579f07db1c359bbfd7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)![在这里插入图片描述](https://img-blog.csdnimg.cn/029f3fdec0bf4baa8f9fc24bb04fa7e4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### CMakeLists.txt

描述功能包里的编译规则，使用CMake语法。  
（后面的课会越来越多的用到）  
![在这里插入图片描述](https://img-blog.csdnimg.cn/2cadfe0590c54691880c82aca7a7b1b5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

 

基于B站ROS公开课：【古月居】古月·ROS入门21讲  
基于Ubuntu 20.04.1、Noetic版本  
修正错误，并详述Python版本部署  

#### 目录（本节基于P10）

*   *   [1 模型图](#1__10)
    *   [2 创建功能包](#2__20)
    *   [3 创建Publisher代码（以C++为例）](#3_PublisherC_28)
    *   [4 编译代码（以C++为例）](#4_C_46)
    *   *   [配置Publisher代码编译规则](#Publisher_48)
        *   [执行编译](#_61)
        *   [source 一下 setup.bash](#source__setupbash_68)
        *   [运行](#_72)
    *   [5 创建Publisher代码（以Python为例）](#5_PublisherPython_90)
    *   *   [查看内置Python版本](#Python_96)
        *   [创建Python代码](#Python_104)
    *   [6 编译代码（以Python为例）](#6_Python_122)
    *   *   [配置代码编译规则](#_124)
        *   [执行编译](#_130)
        *   [source 一下 setup.bash](#source__setupbash_137)
        *   [运行](#_141)

前面提到的通信模式之一的Topic模式，其使用“发布订阅”的方式来通信。  
我们之前是通过命令行或键盘操控的形式让海龟动起来的，这次我们直接编译一个程序来控制它。  
本节通过创建一个发布者Publisher来控制海龟。  
我们先看要实现的这个小程序的图。  
(部分图摘自：b站【古月居】古月·ROS入门21讲)

# 发布者Publisher的编程实现

图中，我们使用ROS Master管理节点。  
有两个主要节点：  
**Publisher**，名为Turtle Velocity（即海龟的速度）  
**Subscriber**，即海龟仿真器节点 /turtlesim  
Publisher(Turtle Velocity)，发布Message（即海龟的速度信息，以geometry\_msgs::Twist的数据结构，包括线速度和角速度），通过Topic（/turtle1/cmd\_vel）总线管道，将数据传输给Subscriber。Subscriber订阅得到的速度信息，来控制海龟发生运动。

“/turtle1/cmd\_vel”这个topic是海归仿真器节点/turtlesim下自带的topic，可直接拿来用。

![在这里插入图片描述](https://img-blog.csdnimg.cn/9307be79c1994e2994014f62c00fbb17.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 2 创建功能包

我们之前已经创建了工作空间了，这次我们在src文件夹创建一个新的功能包learning topic

    cd ~/catkin_ws/src
    catkin_create_pkg learning_topic roscpp rospy std_msgs geometry_msgs turtlesim


![在这里插入图片描述](https://img-blog.csdnimg.cn/188ffaaaa305474eab138355b1fea086.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 3 创建Publisher代码（以C++为例）

**关于如何实现一个Publisher：**

*   初始化ROS节点
*   向ROS Master注册节点信息，包括发布的话题名和话题中的消息类型
*   创建消息数据
*   按照一定的频率循环发布消息

先以C++为例（后面会讲Python的情形），我们这次需要在src里创建C++的代码文件以输入代码。源码见下。  

**节点名不能重复**

（源码地址：https://github.com/guyuehome/ros\_21\_tutorials/blob/master/learning\_topic/src/velocity\_publisher.cpp）  
我用红字标上了代码讲解。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/322067f1f67b4c809aaa501432f88aff.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

```c++
#include<ros/ros.h>
#include<geometry_msgs/Twist.h>
using namespace std;

int main(int argc,char **argv){
    //ros节点初始化
     ros::init(argc,argv,"velocity_publisher");
     //创建节点句柄
     ros::NodeHandle n;
     //创建一个publisher,发布名为velocity_publisher
     ros::Publisher turtle_vel_pub = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel",10);
     //设置循环的频率
     ros::Rate loop_rate(10);//ros::ok()
     
     int count = 0;

     while(ros::ok()){
        //初始化geometry_msgs::Twist类型的消息
         geometry_msgs::Twist vel_msg;
         vel_msg.linear.x = 0.5;
         vel_msg.angular.z = 0.2;

         //发布消息
        turtle_vel_pub.publish(vel_msg);
        ROS_INFO("Publish turtle velocity command[%0.2f m/s %0.2f rad/s]",vel_msg.linear.x,vel_msg.angular.z);


        loop_rate.sleep();
}
 return 0;
}
```

将这个cpp文件创建在src文件夹下：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/01a9587f7b824c7aa7eba371d931a9fe.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### VSC设置

#### 设置插入模式

vscode的文本编辑器继承了linux上vim的功能。用vscode打开源文件后，可能默认的模式是一般模式，这种模式下是不能输入字符的，对于用惯了windows的人来说是非常不习惯的。如何将默认的模式更改为插入模式呢。File-Preferences-Settings，搜索vim.startInInsertMode，在Start in Insert mode前面打上勾。

#### 设置包能够正确被读取

如图所示![在这里插入图片描述](https://img-blog.csdnimg.cn/ba883f91f1b44126a061aef5ff3e052a.png)

找到ros的include文件
---------------

如图，我的ros的include文件位置是

    /opt/ros/noetic/include

路径大概都差不多，我的ros版本是noetic，所以其他版本的ros的路径可能是换成其他版本的名称  
记住这个路径  
![在这里插入图片描述](https://img-blog.csdnimg.cn/bf5805cc7e504ff1a660a2c705d432ee.png)

左键点击小灯泡，再点击编辑“include”设置  
![在这里插入图片描述](https://img-blog.csdnimg.cn/daff2c16beca4ef5abc11bc0c0c547b0.png)

将你ros的include文件的路径填到包含路径中去，注意在路径最后加上/\*\*表示递归搜索。即

    /opt/ros/noetic/include/**


![在这里插入图片描述](https://img-blog.csdnimg.cn/6a1416cdd11248929aad449bdf9f9e2c.png)  
返回到你的cpp文件，就会发现问题解决。(至少我是解决了)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/49e9679bfde248b0a29e17feb279cf48.png)  
编写一个publisher程序并检验  
![在这里插入图片描述](https://img-blog.csdnimg.cn/d5211a77f2b741e58a75f4292a5209cd.png)  
点击init类并摁F12  
![在这里插入图片描述](https://img-blog.csdnimg.cn/2d9ae69245cf4b97a4389c06a2448783.png)  
成功！

注意
--

不要让CMake config 你的工作环境，可能会失效（我点了config后，这个方法就失效了）

### 4 编译代码（以C++为例）

有了代码，接下来编译。

#### 配置Publisher代码编译规则

首先需要配置CMakeLists.txt中的编译规则：

*   设置需要编译的代码和生成的可执行文件
*   设置链接库

将下列代码拷贝至CMakeLists.txt中：

    add_executable(velocity_publisher src/velocity_publisher.cpp)
    target_link_libraries(velocity_publisher ${catkin_LIBRARIES})

拷贝到下图这个位置（代码的作用见图）：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/ab6c4885c9614629b9c487843afc4ec7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 执行编译

回到工作空间目录，执行编译.

    cd ~/catkin_ws
    catkin_make


![在这里插入图片描述](https://img-blog.csdnimg.cn/e7bc2480d1ac4ae791578d2fe6eefefc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### source 一下 setup.bash

我们之后每次运行这个程序都需要source一下devel/setup.bash，我们不妨将  
`source devel/setup.bash`放入环境变量.bashrc中。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/77f22cbfc15846f3be26c458f3555749.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 运行

打开终端，分别运行：

    roscore


    rosrun turtlesim turtlesim_node


    rosrun learning_topic velocity_publisher

![在这里插入图片描述](https://img-blog.csdnimg.cn/4bcf47be4e4d488ca2bbe5b7fd2ea0d0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
海龟就按照我们之前代码中设定的线速度和角速度画圆啦！

我们编译好的程序是放在devel/lib目录下的：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/954fba05219543069dff48b1b3f980f7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)



### 5 创建Publisher代码（以Python为例）

下面我们详述Python的实现方法。  
Python的步骤中，在“配置编译规则”和“编译并执行”这俩步骤有些不同，前面都一样。

#### 查看内置Python版本

Ubuntu20.04内置了Python3.8，可见 /usr/bin 目录下：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/1cbf9aef27a04878b6879f2ea703d443.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)我们在终端使用`python3`命令可调用python，比如查看版本号：

    python3 --version


![在这里插入图片描述](https://img-blog.csdnimg.cn/1aa7a8671eec48f7a7243e4a2fa1cbf3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 创建Python代码

python代码文件是放在功能包文件夹下的scripts目录下的，我们需要新建一个scripts文件夹。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/aeeffa601d7c4b75963e71eb3dd3c7d3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)复述一下**实现Publisher的方法：**

*   初始化ROS节点
*   向ROS Master注册节点信息，包括发布的话题名和话题中的消息类型
*   创建消息数据
*   按照一定的频率循环发布消息

我们把我们的Python版的代码拷贝到目录下。  
（源码地址：https://github.com/guyuehome/ros\_21\_tutorials/blob/master/learning\_topic/scripts/velocity\_publisher.py）  
（注意：第31行 `rospy.loginfo("Publsh turtle velocity command[%0.2f m/s, %0.2f rad/s]",`原作者因为用Tab导致对齐失败，手动用4个空格对齐一下）  
我用红字标上了代码讲解。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/db3214ab077d4990b419cd6b60f42da3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

右击文件→属性，打开执行权限：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/0797b662626f4016a186863f1688327c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 6 编译代码（以Python为例）

有了代码，接下来编译。

#### 配置代码编译规则

在新的Noetic版本的ROS中，需要配置这一步，貌似之前的版本不需要配置。

我们配置一下CMakeLists.txt中的编译规则：  
将文件中的catkin\_install\_python这段取消注释，并将默认的my\_python\_script改成velocity\_publisher.py  
![在这里插入图片描述](https://img-blog.csdnimg.cn/5db291d3ba7b4879af32d2f89e070757.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 执行编译

回到工作空间目录，执行编译.

    cd ~/catkin_ws
    catkin_make


![在这里插入图片描述](https://img-blog.csdnimg.cn/f85236f7db5f43b8aa18bcb6aacdbccf.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### source 一下 setup.bash

如前所述，需要将`source devel/setup.bash`放入环境变量.bashrc中(.bashrc在主目录中，是隐藏文件)。  
我们前面C++的时候这句话已经放进去了。

#### 运行

打开终端，分别运行：

    roscore


    rosrun turtlesim turtlesim_node


    rosrun learning_topic velocity_publisher.py

python直接执行功能包下的这个py文件就行了。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/02478225ce3e4b688d4842eec5b87a1f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)小海龟一样跑起来啦~

本节通过创建一个订阅者Subscriber来控制海龟。  
我们先看要实现的这个小程序的图。  
(部分图摘自：b站【古月居】古月·ROS入门21讲)

# 订阅者**Subscriber**的编程实现

ROS Master管理两个主要节点：  
**Publisher**，海龟[仿真器](https://so.csdn.net/so/search?q=%E4%BB%BF%E7%9C%9F%E5%99%A8&spm=1001.2101.3001.7020)/turtlesim  
**Subscriber**，名为Pose Listener  
这次海龟仿真器turtlesim为Publisher，发布Message（传输的是动作信息，以数据结构 turtlesim::Pose发布），通过[Topic](https://so.csdn.net/so/search?q=Topic&spm=1001.2101.3001.7020)（/turtle1/pose）的管道，将数据传输给Subscriber。Subscriber订阅得到的数据，获得Pose信息。

“/turtle1/pose”这个topic是海归仿真器节点/turtlesim下自带的topic，直接拿来用。

![在这里插入图片描述](https://img-blog.csdnimg.cn/57eb6dfc28b74ab58af87d9d0d34b4f6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 2 创建功能包

我们之前已经创建了工作空间和功能包learning topic了。  
直接上代码。

### 3 创建Subscriber代码（C++）

**如何实现一个Subscriber：**

*   初始化ROS节点
*   订阅需要的话题
*   循环等待话题消息，接收到消息后进入回调函数
*   在回调函数中完成消息处理

（源码：https://github.com/guyuehome/ros\_21\_tutorials/blob/master/learning\_topic/src/pose\_subscriber.cpp）  
我用红字标上了代码讲解。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/5fc16bd4b8504996bdafec02f50084ec.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

```c++
/**
 * 该例程将订阅/turtle1/pose话题，消息类型turtlesim::Pose
 */
 
#include <ros/ros.h>
#include "turtlesim/Pose.h"

// 接收到订阅的消息后，会进入消息回调函数
void poseCallback(const turtlesim::Pose::ConstPtr& msg)
{
    // 将接收到的消息打印出来
    ROS_INFO("Turtle pose: x:%0.6f, y:%0.6f", msg->x, msg->y);
}

int main(int argc, char **argv)
{
    // 初始化ROS节点
    ros::init(argc, argv, "pose_subscriber");

    // 创建节点句柄
    ros::NodeHandle n;

    // 创建一个Subscriber，订阅名为/turtle1/pose的topic，注册回调函数poseCallback
    ros::Subscriber pose_sub = n.subscribe("/turtle1/pose", 10, poseCallback);

    // 循环等待回调函数
    ros::spin();

    return 0;
}
```



### 4 编译代码（C++）

有了代码，接下来编译。

#### 配置代码编译规则

配置CMakeLists.txt中的编译规则：

*   设置需要编译的代码和生成的可执行文件
*   设置链接库

将下列代码拷贝至CMakeLists.txt中：  
直接加到之前那两行下面即可

    add_executable(pose_subscriber src/pose_subscriber.cpp)
    target_link_libraries(pose_subscriber ${catkin_LIBRARIES})


![在这里插入图片描述](https://img-blog.csdnimg.cn/18bba97c85ee4a93b3f601bf8de2eba3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 执行编译

回到工作空间目录，执行编译.

    cd ~/catkin_ws
    catkin_make


![在这里插入图片描述](https://img-blog.csdnimg.cn/899cbf92e3f74078895d8e681a5f0fd6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### source 一下 setup.bash

将`source devel/setup.bash`放入环境变量.bashrc中，之前已完成。

#### 运行

打开终端，分别运行：

    roscore


    rosrun turtlesim turtlesim_node


    rosrun learning_topic pose_subscriber


![在这里插入图片描述](https://img-blog.csdnimg.cn/14c12d3690e148aab1db223fed752ea2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)这时海龟的位置就会一直被pose\_subscriber监听，现在因为海龟没动，所以x、y的坐标值是不会变的。  
我们让海龟动起来，再建立一个之前用过的键盘控制节点：

    rosrun turtlesim turtle_teleop_key


控制它移动，坐标就发生实时变化啦！  
![在这里插入图片描述](https://img-blog.csdnimg.cn/1537beab9eb14ba2b1f49adb68ce5b97.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 5 Python实现

（源码：https://github.com/guyuehome/ros\_21\_tutorials/blob/master/learning\_topic/scripts/pose\_subscriber.py）

#### 创建Python代码

源码拷贝到scripts下。  
我用红字标上了代码讲解。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/f8a7f843bf034a21bbe0986fee8b18cb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

右击文件→属性，打开执行权限。

#### 配置代码编译规则

配置一下CMakeLists.txt中的编译规则：  
之前已将文件中的catkin\_install\_python这段取消注释，并将默认的my\_python\_script改成了velocity\_publisher.py  
这次再加上一个关于pose\_subscriber.py的catkin\_install\_python方法：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/d860786eaa5947d48845e68967323227.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 编译代码

回到工作空间目录，执行编译.

    cd ~/catkin_ws
    catkin_make


#### source 一下 setup.bash

略过。

#### 运行

打开终端，分别运行：

    roscore


    rosrun turtlesim turtlesim_node


    rosrun learning_topic pose_subscriber.py


    rosrun turtlesim turtle_teleop_key


控制它移动，成功！  
![在这里插入图片描述](https://img-blog.csdnimg.cn/b940b93d249e4cf4a3b20e230bca2cfd.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 试着查看一下系统当前的[计算图](https://so.csdn.net/so/search?q=%E8%AE%A1%E7%AE%97%E5%9B%BE&spm=1001.2101.3001.7020)

再打开一个终端，输入：

    rqt_graph


调到所有活动active节点/话题视图，可看到3个节点：  
键盘控制器节点/teleop\_turtle 通过 /turtle/cmd\_vel 传速度msg给海归仿真器节点/turtlesim，  
/turtlesim 通过 /turtle/pose 传位置msg给subscriber节点。  
/turtle/cmd\_vel 和 /turtle/pose 两个topic都在turtle1海龟下面，因为海龟自身会发布速度和位置的msg给这两个topic  
![在这里插入图片描述](https://img-blog.csdnimg.cn/796f3101b24648e3a8965463e6f80207.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

# 话题消息的定义与使用

之前两节使用了Topic模型，我们先使用了Twist类型（geometry\_msgs.msg库下的Twist类）的Message作为输入指令进行发布，接着使用了Pose类型（Turtlesim.msg库下的Pose类）的Message作为订阅消息进行接收。  
我们可以使用`rosmsg show ...`来查看这俩的数据结构，可以看出包含了哪些信息：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/9badb390b7754a46a6cfd7f3450ceb44.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_12,color_FFFFFF,t_70,g_se,x_16#pic_center)

以上的**Message**消息都是预定义好的，当我们需要自定义消息该怎么做呢？  
(部分图摘自：b站【古月居】古月·ROS入门21讲)

### 模型图

这节我们自定义一个消息类型“Person”，并完成发布订阅整个过程，Publisher进行发布个人信息，Subscriber来接收个人信息。Topic定义名为“person\_info”。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/3f3200515ffa4190ab8e261f52f3b065.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 自定义话题消息

#### 定义msg文件

我们通过自定义msg文件来自定义话题消息。  
我们定义msg文件名为：_Person.msg_

1.  在learning\_topic的功能包根目录下，新建文件夹 msg  
    并创建新文件 Person.msg，创建方法为使用`touch`命令在当前目录输入：

    touch Person.msg
    

![在这里插入图片描述](https://img-blog.csdnimg.cn/914c9c502d344189a10ecb36b35b6d26.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)注意Person的"P"要大写。

2.  我们把下面代码复制进Person.msg

    string name
    uint8 sex
    uint8 age
    
    uint8 unknown = 0
    uint8 male = 1
    uint8 female = 2

msg文件定义使用自己的一套语言规则。  
定义好msg数据接口后，就可以根据这个定义用C++或Python编译。

#### 在package.xml中添加功能包依赖

添加动态生成程序的功能包依赖。  
打开package.xml文件，将下面代码拷到文件指定位置：

    <build_depend>message_generation</build_depend>
    <exec_depend>message_runtime</exec_depend>


build\_depend为编译依赖，这里依赖的是一个会动态产生message的功能包  
exer\_depend为执行依赖，这里依赖的是一个动态runtime运行的功能包

![在这里插入图片描述](https://img-blog.csdnimg.cn/6c15f82874944a2f81fa79b90287ccad.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 在CMakeLists.txt中添加编译选项

1.  因为在package.xml添加了功能包编译依赖，在CMakeList.txt里的find\_package中也要加上对应的部分；
2.  需要将定义的Person.msg作为消息接口，针对它做编译；
3.  需要指明编译这个消息接口需要哪些ROS已有的包；  
    有了这两个配置才可将定义的msg编译成不同的程序文件
4.  因为在package.xml添加了功能包执行依赖，在CMakeList.txt里的catkin\_package中也要加上对应的部分；

代码，复制到图示位置：

    find_package( ...... message_generation)
    
    add_message_files(FILES Person.msg)
    generate_messages(DEPENDENCIES std_msgs)
    
    catkin_package( ...... message_runtime)


![在这里插入图片描述](https://img-blog.csdnimg.cn/d04b106e87f64473b544cb4c4e98625e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)![在这里插入图片描述](https://img-blog.csdnimg.cn/98f7affd23a840a8afcc3053b4f618ea.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)![在这里插入图片描述](https://img-blog.csdnimg.cn/affb3d2ab7a94c899ec021b5a37412b5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 编译生成C++头文件或Python库

以上完成后，到工作空间根目录，编译：

    catkin_make


![在这里插入图片描述](https://img-blog.csdnimg.cn/4b1187ce7fba4970aaf72e4593b3585d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
编译完成后，我们可以在 devel/include/learning\_topic/ 下找到这个C++的头文件：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/67e1b808bc2d460cae3e850fbf36673d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
也可以在 devel/lib/python3/dist-packages/learning\_topic/msg 下找到Python的包：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/9aea40a8f620424dbd1d7f28d47995e5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
接下来我们就可以通过编写程序来调用生成的.h或.py了！

### 3 创建代码并编译运行（C++）

#### 创建代码

我们创建一个Publisher代码和一个Subscriber代码，通过程序调用生成的.h。  
(源码：https://github.com/guyuehome/ros\_21\_tutorials/tree/master/learning\_topic/src)  
我用红字标上了代码讲解。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/8041893ee87a4f7eb174da8a15c0ddb2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  

```c++
#include <ros/ros.h>
#include "learning_topic/Person.h"

int main(int argc, char **argv)
{
    // ROS节点初始化
    ros::init(argc, argv, "person_publisher");

    // 创建节点句柄
    ros::NodeHandle n;

    // 创建一个Publisher，发布名为/person_info的topic，消息类型为learning_topic::Person，队列长度10
    ros::Publisher person_info_pub = n.advertise<learning_topic::Person>("/person_info", 10);

    // 设置循环的频率
    ros::Rate loop_rate(1);

    int count = 0;
    while (ros::ok())
    {
        // 初始化learning_topic::Person类型的消息
    	learning_topic::Person person_msg;
		person_msg.name = "Tom";
		person_msg.age  = 18;
		person_msg.sex  = learning_topic::Person::male;

        // 发布消息
		person_info_pub.publish(person_msg);

       	ROS_INFO("Publish Person Info: name:%s  age:%d  sex:%d", 
				  person_msg.name.c_str(), person_msg.age, person_msg.sex);

        // 按照循环频率延时
        loop_rate.sleep();
    }

    return 0;
}

```

![在这里插入图片描述](https://img-blog.csdnimg.cn/fc54686fab014003b3348b1031c636ca.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

```c++
#include <ros/ros.h>
#include "learning_topic/Person.h"

// 接收到订阅的消息后，会进入消息回调函数
void personInfoCallback(const learning_topic::Person::ConstPtr& msg)
{
    // 将接收到的消息打印出来
    ROS_INFO("Subcribe Person Info: name:%s  age:%d  sex:%d", 
			 msg->name.c_str(), msg->age, msg->sex);
}

int main(int argc, char **argv)
{
    // 初始化ROS节点
    ros::init(argc, argv, "person_subscriber");

    // 创建节点句柄
    ros::NodeHandle n;

    // 创建一个Subscriber，订阅名为/person_info的topic，注册回调函数personInfoCallback
    ros::Subscriber person_info_sub = n.subscribe("/person_info", 10, personInfoCallback);

    // 循环等待回调函数
    ros::spin();

    return 0;
}

```

在代码中我们调用了自己编译好的头文件，并使用了定义的Person类和属性。

将代码拷贝到src文件夹下。

#### 编译

先配置CMakeLists.txt编译规则，复习一下规则：

*   设置需要编译的代码和生成的可执行文件；
*   设置链接库；
*   **添加依赖项**。

将下面代码拷贝到指定位置：

    add_executable(person_publisher src/person_publisher.cpp)
    target_link_libraries(person_publisher ${catkin_LIBRARIES})
    add_dependencies(person_publisher ${PROJECT_NAME}_generate_messages_cpp)
    
    add_executable(person_subscriber src/person_subscriber.cpp)
    target_link_libraries(person_subscriber ${catkin_LIBRARIES})
    add_dependencies(person_subscriber ${PROJECT_NAME}_generate_messages_cpp)


这里新增了一个添加依赖项，因为代码涉及到动态生成，我们需要将可执行文件与动态生成的程序产生依赖关系。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/341cb195f23146379b948909667d777b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

然后编译：

    cd ~/catkin_ws
    catkin_make


![在这里插入图片描述](https://img-blog.csdnimg.cn/4faa03bd647c45578070e219a0a266a4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 运行

默认已经source，接着运行。

    roscore


    rosrun learning_topic person_subscriber


    rosrun learning_topic person_publisher

可以看到运行成功，subscriber接收到了publisher的person信息：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/794cd5e1f14044f88acbde91b1743b93.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)可以看到计算图：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/5a6d53de11ae4306a7bc165d4cce65f6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
如果我们将roscore关掉，可以看到subscriber和publisher依然在接发。roscore代表了ROS Master，它帮助subscriber和publisher建立通信连接，连接建立后退出舞台也没什么问题了。  
但是关闭ROS Master就不能管理这个连接了。同时也无法看到rqt\_graph。  
![关闭roscore后依然保持通信](https://img-blog.csdnimg.cn/c8f240dcf3d74a9187cd4d36af1a14a2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 4 创建代码并编译运行（Python）

#### 创建代码

我们创建一个Publisher代码和一个Subscriber代码，通过程序调用生成的.py。  
(源码：https://github.com/guyuehome/ros\_21\_tutorials/tree/master/learning\_topic/scripts)

作者的person\_publisher.py代码有两个问题：

1.  这里函数名“velocity\_publisher”取的有点问题，和之前小节的重名了。不过不影响运行。
2.  【重要】拷贝进去后会发现while循环里的rospy那行没和其他行对齐，若不更正会导致后面运行的时候报对齐错误。建议全部改成8个空格对齐。参考下图修正。

![在这里插入图片描述](https://img-blog.csdnimg.cn/10ab2486e22546979287a0f3093b5b65.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

person\_subscriber.py无误  
![在这里插入图片描述](https://img-blog.csdnimg.cn/27ff5c59c2834d92976d13214db2fb45.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

在代码中我们调用了自己编译好的python库（编译指ROS将之前写好的Person.msg文件用我们的规则编译成python库），并使用了定义的Person类和属性。

将代码拷贝到src文件夹下。  
右击py文件→属性，打开执行权限。

#### 编译

配置CMakeLists.txt编译规则，注意和C++的区别：  
我们只要加上一个关于person\_publisher.py和person\_subscriber.py的catkin\_install\_python方法：  
下面代码写到指定位置：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/6b42e2a1cba74d4fbc500ed47f56061a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

然后编译

    cd ~/catkin_ws
    catkin_make


#### 运行

默认已经source，接着运行。

    roscore


    rosrun learning_topic person_subscriber.py


    rosrun learning_topic person_publisher.py

同样可以运行成功，subscriber接收到了publisher的person信息！  
没看C++部分的同学可以看看上面C++部分运行中关于rqt\_graph计算图和关闭ROS Master对连接影响的描述。 

基于B站ROS公开课：【古月居】古月·ROS入门21讲  
基于Ubuntu 20.04.1、Noetic版本  
修正错误，并详述Python版本部署

# 客户端Client的编程实现

这节来到通信模式之二的Service模式，其使用“ **客户端/服务器(C/S)模型**”的方式来通信。  
是一种带有反馈的同步通信机制。  
之前我们曾通过命令行工具 `rosservice call /spawn ...`生成一只新的海龟。这次通过程序的形式发布服务请求，使客户端在海龟仿真器生成一只新的小海龟。  
我们先看要实现的这个小程序的图。  
(部分图摘自：b站【古月居】古月·ROS入门21讲)

### 1 模型图

Sever端是海龟仿真器/turtlesim，Client端是待实现的程序，其作为Response的节点，并产生Request的请求，发给Server端。Server端收到Request请求后产生一只海龟，回馈一个Response给Client海龟产生是否成功。Service的名称为/spawn，中间传输消息的数据结构为turtlesim::Spawn。  
ROS Master负责管理节点。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/77dcfe3f14784ee9873514e561a3eb43.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 2 创建功能包

这次我们创建新的功能包 learning\_service

    cd ~/catkin_ws/src
    catkin_create_pkg learning_service roscpp rospy std_msgs geometry_msgs turtlesim


![在这里插入图片描述](https://img-blog.csdnimg.cn/07ff85acf61e4b39b673586edfa5ce90.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 3 创建代码并编译运行（C++）

#### 如何实现一个客户端Client

*   初始化ROS
*   创建一个Client实例
*   发布服务请求数据
*   等待Server处理之后的应答结果

#### 创建客户端Client代码

（源码：https://github.com/guyuehome/ros\_21\_tutorials/tree/master/learning\_service/src）  
将源码turtle\_spawn.cpp拷贝到src文件夹下。我用红字标上了代码讲解。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/805ddc62b46f492c9460980fff9e93f8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 编译

先配置CMakeLists.txt编译规则：

*   设置需要编译的代码和生成的可执行文件；
*   设置链接库；

    add_executable(turtle_spawn src/turtle_spawn.cpp)
    target_link_libraries(turtle_spawn ${catkin_LIBRARIES})

拷贝到CMakeLists.txt对应位置。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/64490ebcaea84d46a3a5578b90300c52.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
然后编译：

    cd ~/catkin_ws
    catkin_make


编译成功，在 devel/lib/learning\_service 下生成库  
![在这里插入图片描述](https://img-blog.csdnimg.cn/2c7344c21c154a998e61ad2b8f61ab6d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 运行

默认已经source，接着运行。

    roscore


    rosrun turtlesim turtlesim_node


    rosrun learning_service turtle_spawn


成功生成第二只海龟！  
![在这里插入图片描述](https://img-blog.csdnimg.cn/65740145af2e44818c0512b51eda9def.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 4 创建代码并编译运行（Python）

#### 如何实现一个客户端Client

*   初始化ROS
*   创建一个Client实例
*   发布服务请求数据
*   等待Server处理之后的应答结果

#### 创建客户端Client代码

（源码：https://github.com/guyuehome/ros\_21\_tutorials/tree/master/learning\_service/scripts）  
将源码turtle\_spawn.py拷贝到新建的scripts文件夹下。我用红字标上了代码讲解。  
可以看到Python不需要C++中的另一个call阻塞型函数来等待服务器的反馈，而是建立ServiceProxy机制，直接add\_turtle传入参数创建请求数据，赋为response以返回它的name。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/35b44e2c228d4204b2632f2953526b76.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)【注意】这里是Python2代码，接着需要如下图修改成Python3：

1.  两个print语句后面的内容用括号括起来
2.  except 后面的逗号 , 改成 as

![在这里插入图片描述](https://img-blog.csdnimg.cn/15091a9130e749c1b6d6491daa4f6b26.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

右击py文件→属性，打开执行权限。

#### 编译

配置CMakeLists.txt编译规则，注意和C++的区别：  
我们只要加上一个关于turtle\_spawn.py的catkin\_install\_python方法：  
下面代码写到指定位置：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/54d2697cc42c4a1483668808bf06f74a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
然后编译：

    cd ~/catkin_ws
    catkin_make


编译成功，在 devel/lib/learning\_service 下生成py调用库。

#### 运行

默认已经source，接着运行。

    roscore


    rosrun turtlesim turtlesim_node


    rosrun learning_service turtle_spawn.py


成功！  
![在这里插入图片描述](https://img-blog.csdnimg.cn/a9960319a3ad4bd5a7667e0f9cdbf9e4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#  服务端Server的编程实现

上一讲学习了基于Service模式的客户端Client的编程实现。  
这节来实现另一例基于Service模式的程序，来学习服务端Service的编程实现。  
我们先看模型图。  
(部分图摘自：b站【古月居】古月·ROS入门21讲)

### 1 模型图

Server端本身是进行模拟海龟运动的命令端，它的实现是通过给海龟发送速度（Twist）的指令，来控制海龟运动（本身通过Topic实现）。  
Client端相当于海龟运动的开关，其发布Request来控制Server端。  
通过自定义名为 /turtle\_command 的Service实现，中间传输消息的数据类型为std\_srvs::Trigger（一种针对服务标准std\_srvs下的数据定义）来通信。Trigger意为触发，通过Trigger信号来触发Server端的运动指令。  
Server端接收这个Trigger信号后，可控制其是否要给海龟发送Twist指令，同时给Client发送Response反馈告诉它海龟的运动状态。  
ROS Master负责管理节点。

所以本例既有Server端自己的Topic模式控制海龟运动，又有S/C之间的Service模式，包含两种通信模式的实现。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/b03d2f23b00543559f581d2ef9bcff5a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 2 创建功能包

本节还是使用上节创建的 learning\_service 包来进行代码存放和编译。

### 3 创建代码并编译运行（C++）

#### 如何实现一个服务器端Server

*   初始化ROS
*   创建一个Server实例
*   循环等待服务请求，进入回调函数
*   在回调函数中完成服务功能的处理，并反馈应答数据

#### 创建服务端Server代码

（源码：https://github.com/guyuehome/ros\_21\_tutorials/tree/master/learning\_service/src）  
将源码turtle\_command\_server.cpp拷贝到src文件夹下。我用红字标上了代码讲解。  
(下面代码有一处错误，27行后补上一个分号;)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/364844e0d06c4e83b1ce633671b90846.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

其中在回调函数中给Client端的反馈数据res是与Trigger相对应的，我们可以查看一下Trigger的数据结构。可以使用`rossrv`指令查看service中的数据类型：

    rossrv show std_srvs/Trigger


![在这里插入图片描述](https://img-blog.csdnimg.cn/143689fd908c4540937dae1b67cc2eaf.png#pic_center)

#### 编译

先配置[CMakeLists](https://so.csdn.net/so/search?q=CMakeLists&spm=1001.2101.3001.7020).txt编译规则：

*   设置需要编译的代码和生成的可执行文件；
*   设置链接库；

    add_executable(turtle_command_server src/turtle_command_server.cpp)
    target_link_libraries(turtle_command_server ${catkin_LIBRARIES})
    

拷贝到CMakeLists.txt对应位置。

然后编译：

    cd ~/catkin_ws
    catkin_make


#### 运行

默认已经source，接着运行。

    roscore


    rosrun turtlesim turtlesim_node


    rosrun learning_service turtle_command_server


服务端启动。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/3d8bc172fb174994be05441c07293752.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
接着我们使用`rosservice call ...`请求海龟动起来，再打开一个终端。  
（输入完 /turtle\_command 后敲个空格再用Tab键可自动填充空指令内容）

    rosservice call /turtle_command "{}"


给到一个空内容的指令后，可以看到海龟动起来了。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/e7650e877fc943d2a725396bf581ec06.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
再输入一遍`rosservice call /turtle_command "{}"`海龟就会停下来。

### 4 创建代码并编译运行（Python）

#### 如何实现一个服务器端Server

*   初始化ROS
*   创建一个Server实例
*   循环等待服务请求，进入回调函数
*   在回调函数中完成服务功能的处理，并反馈应答数据

#### 创建服务端Server代码

（源码：https://github.com/guyuehome/ros\_21\_tutorials/tree/master/learning\_service/scripts）  
将源码turtle\_command\_server.py拷贝到src文件夹下。

注意在C++里我们使用了spinOnce来查看一次队列，判断是否有消息入队；在Python中没有这个功能，因此这里使用了多线程思路。  
我用红字标上了代码讲解。绿字是Python3的修改点。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/79451a80ecdd40db8515b54462193c98.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)在代码36行解释中，回调函数中给Client端的反馈数据是与Trigger相对应的，我们可以查看一下Trigger的数据结构。可以使用`rossrv`指令查看service中的数据类型：

    rossrv show std_srvs/Trigger


![在这里插入图片描述](https://img-blog.csdnimg.cn/143689fd908c4540937dae1b67cc2eaf.png#pic_center)  
最后右击py文件→属性，打开执行权限。

#### 编译

配置CMakeLists.txt编译规则：  
加上一个关于turtle\_command\_server.py的catkin\_install\_python方法，写到指定位置。

然后编译：

    cd ~/catkin_ws
    catkin_make


#### 运行

默认已经source，接着运行。

    roscore


    rosrun turtlesim turtlesim_node


    rosrun learning_service turtle_command_server.py


服务端启动。

接着我们使用`rosservice call ...`请求海龟动起来，再打开一个终端。  
（输入完 /turtle\_command 后敲个空格再用Tab键可自动填充空指令内容）

    rosservice call /turtle_command "{}"


![在这里插入图片描述](https://img-blog.csdnimg.cn/0b49b083cbc0471d9c00d55f326bfeda.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
再输入一遍`rosservice call /turtle_command "{}"`海龟就会停下来。

### 5 再看服务数据srv

在代码中，回调函数中给Client端的反馈数据是与Trigger相对应的，这个对应是指与它的response部分对应。  
我们可以再查看一下Trigger的数据结构：

    rossrv show std_srvs/Trigger

![在这里插入图片描述](https://img-blog.csdnimg.cn/143689fd908c4540937dae1b67cc2eaf.png#pic_center)  
我们可以看到在定义srv的数据结构时，有一块三个连续破折号“- - -”。  
这指的是破折号上方是定义Request部分，下方是定义Response部分。  
在Trigger中，没有Request部分，即一个空内容的Request，这也解释了我们不需要在让海龟运动时给 /turtle\_command 传内容，直接传个空值 “{}” 就可以了（`rosservice call /turtle_command "{}"`）。  
这部分为下一节做铺垫，下一节将讲自定义服务数据srv。

# 服务数据(srv)的定义与使用

前面讲了两个Service模式的例子，分别用到了两种服务数据：turtlesim/Spawn和std_srvs/Trigger。  
我们可以使用 `rossrv show ...`来查看数据结构：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/b5afa64c889b40978bb4a4157b5e991f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_12,color_FFFFFF,t_70,g_se,x_16#pic_center)

我们可以看到Spawn中的Request部分含坐标信息、朝向角和名称，Response部分含名称。  
Trigger中Request部分为空，Response部分含成功Flag、消息内容。

与之前topic种的msg类似，我们也可以用相似的语法自定义服务数据srv  
这节我们来自己定义服务数据来满足个性化的需求。  
(部分图摘自：b站【古月居】古月·ROS入门21讲)

### 1 模型图

在第8节我们讲解了话题消息msg的定义与使用，在第8节的例子中我们曾自定义了一个消息类型“Person”以发布个人信息，Publisher发布个人信息，Subscriber接收个人信息。这个例子中，Publisher会不断地发信息，Subscriber不停地接数据，一开动就停不下来了，也是topic模式的缺陷。  
本节我们使用Service模式用自定义的服务数据srv来实现，我们希望Request一次才发一次信息来显示。

如图，Client发布显示某个人的信息的Request，通过自定义的服务数据“Person”（learning::Person）来发出去。  
Server端收到Request，显示这个人的具体信息，同时发Response向Client反馈显示结果。  
ROS Master负责管理节点。

![在这里插入图片描述](https://img-blog.csdnimg.cn/6225bb4b3aa74ffabf96c769a5d449b3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 2 创建功能包

本节还是使用上节创建的 learning\_service 包来进行代码存放和编译。

### 3 自定义服务数据

#### 定义srv文件

我们通过自定义srv文件来自定义服务数据。与之前自定义话题数据msg类似。  
我们定义srv文件名为：_Person.srv_

1.  在learning\_topic的功能包根目录下，新建文件夹 srv  
    并创建新文件 Person.srv，创建方法为使用`touch`命令在当前目录输入：

    touch Person.srv
    

![在这里插入图片描述](https://img-blog.csdnimg.cn/439f03132dda498984d9590548c1fc26.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

注意Person的"P"要大写。

2.  我们把下面代码复制进Person.srv

    string name
    uint8 sex
    uint8 age
    
    uint8 unknown = 0
    uint8 male = 1
    
    uint8 female = 2
    
    ---
    
    string result

与之前Person.msg不同的是，多了破折号下面这个Response结果，上面的是Request内容。  
定义好srv数据接口后，就可以根据这个定义用C++或Python编译。

#### 在package.xml中添加功能包依赖

添加动态生成程序的功能包依赖。  
打开package.xml文件，将下面代码拷到文件指定位置：

    <build_depend>message_generation</build_depend>
    <exec_depend>message_runtime</exec_depend>


build\_depend为编译依赖，这里依赖的是一个会动态产生message的功能包  
exer\_depend为执行依赖，这里依赖的是一个动态runtime运行的功能包  
![在这里插入图片描述](https://img-blog.csdnimg.cn/9b4ae51012b44c36bf32839faa621880.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 在[CMakeLists](https://so.csdn.net/so/search?q=CMakeLists&spm=1001.2101.3001.7020).txt中添加编译选项

为什么要添加编译选项：

1.  因为在package.xml添加了功能包编译依赖，在CMakeList.txt里的find\_package中也要加上对应的部分；
2.  需要将定义的Person.srv作为消息接口，针对它做编译；
3.  需要指明编译这个消息接口需要哪些ROS已有的包；  
    有了这两个配置才可将定义的srv编译成不同的程序文件
4.  因为在package.xml添加了功能包执行依赖，在CMakeList.txt里的catkin\_package中也要加上对应的部分；

代码，复制到图示位置：

    find_package( ...... message_generation)
    
    add_service_files(FILES Person.srv)
    generate_messages(DEPENDENCIES std_msgs)
    
    catkin_package( ...... message_runtime)


![在这里插入图片描述](https://img-blog.csdnimg.cn/54f4edf1c16d4990bb35e495f1cb2e25.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)![在这里插入图片描述](https://img-blog.csdnimg.cn/8d39a9c559ff442d8183898b97db989a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

![在这里插入图片描述](https://img-blog.csdnimg.cn/153c19e40de540b783ebfb45ae1db892.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 编译生成语言相关文件

以上完成后，到工作空间根目录，编译：

    catkin_make


编译完成后，我们可以在 devel/include/learning\_topic/ 下找到这个C++的头文件；  
也可以在 devel/lib/python3/dist-packages/learning\_topic/mrv 下找到Python的包。

### 4 创建代码并编译运行（C++）

#### 创建代码

我们创建一个Client代码和一个Server代码，通过程序调用生成的头文件。  
(源码：https://github.com/guyuehome/ros\_21\_tutorials/tree/master/learning\_service/src)  
用红字标示了自己的注解笔记。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/9e6bc85f4d504fefa072e63bbb75f2d2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)![在这里插入图片描述](https://img-blog.csdnimg.cn/551d80ae8bb14ca48561e4b075270d91.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
在代码中我们调用了自己编译好的头文件，使用了自定义的Person类和属性。  
将代码拷贝到src文件夹下。

#### 编译

先配置CMakeLists.txt编译规则，复习一下规则：

*   设置需要编译的代码和生成的可执行文件；
*   设置链接库；
*   添加依赖项。

将下面代码拷贝到指定位置：

    add_executable(person_server src/person_server.cpp)
    target_link_libraries(person_server ${catkin_LIBRARIES})
    add_dependencies(person_server ${PROJECT_NAME}_gencpp)
    
    add_executable(person_client src/person_client.cpp)
    target_link_libraries(person_client ${catkin_LIBRARIES})
    add_dependencies(person_client ${PROJECT_NAME}_gencpp)

第三项是添加依赖项，因为代码涉及到动态生成，我们需要将可执行文件与动态生成的程序产生依赖关系。  
注：这里添加的依赖项用到的是gencpp包，是一个C++用的ROS message 和 service 生成器，以依赖动态生成的cpp文件。

![在这里插入图片描述](https://img-blog.csdnimg.cn/71d7ad1c18a24a6cae9bb4f82f7f488f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

然后编译：

    cd ~/catkin_ws
    catkin_make


#### 运行

默认已经source，接着运行。

    roscore


    rosrun learning_service person_server


    rosrun learning_service person_client


可以看到运行Server后，启动Client会发一次人物信息，在Server端看到，看到后反馈给Client确认后终止这次发送行为。  
先运行Client的话则会一直等待Server端接收，直到Server端启动接收到信息。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/7f6e8d8a83bd46c09a5103d37887c481.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 5 创建代码并编译运行（Python）

#### 创建代码

我们创建一个Client代码和一个Server代码，通过程序调用自己编译的py库。  
(源码：https://github.com/guyuehome/ros\_21\_tutorials/tree/master/learning\_service/scripts)  
用红字标示了自己的注解笔记。绿字是Python3的修正。

![在这里插入图片描述](https://img-blog.csdnimg.cn/f8cd11b3590f480b81725cbf59e2aa7e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)![在这里插入图片描述](https://img-blog.csdnimg.cn/506b5dc440644b9f849fe2e7f202ee34.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
将代码拷贝到scripts文件夹下。  
右击py文件→属性，打开执行权限。

#### 编译

配置CMakeLists.txt编译规则  
加上一个关于person\_server.py和person\_client.py的catkin\_install\_python方法：  
下面代码写到指定位置

![在这里插入图片描述](https://img-blog.csdnimg.cn/4991967f5e42470e9a672f6f50171e0a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
然后编译

    cd ~/catkin_ws
    catkin_make


#### 运行

默认已经source，接着运行。

    roscore


    rosrun learning_topic person_server.py


    rosrun learning_topic person_client.py

可以看到运行Server后，启动Client会发一次人物信息，在Server端看到，看到后反馈给Client确认后终止这次发送行为。  
先运行Client的话则会一直等待Server端接收，直到Server端启动接收到信息。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/c97be96d24854eab9049cf4f231ef9c2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

# 参数的使用与编程方法

至此我们学习了ROS中的两种核心通信机制：Topic（话题）模式 和 Service（服务）模式。  
Topic中的Publisher、Subscriber，Service中的Client、Server，消息类型msg、srv以及它们的自定义数据类型。  
这次讲讲参数的使用。  
(部分图摘自：b站【古月居】古月·ROS入门21讲)

### 1 概念图

在ROS Master中，存在一个参数服务器（Parameter Server），它是一个**全局字典**，即一个全局变量的存储空间，用来保存各个节点的配置参数。各个节点都可以对参数进行全局访问。

![在这里插入图片描述](https://img-blog.csdnimg.cn/7cd43cafcb684806b283c30d8ce7e1e6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
我们来看看参数服务器的使用方法。

### 2 创建功能包

本节建立一个新的功能包，命名为 learning\_parameter。在src下创建。

    cd ~/catkin_ws/src
    catkin_create_pkg learning_parameter roscpp rospy std_srvs


### 3 参数命令行的使用(rosparam)

rosparam命令可以完成参数相关的大部分功能。

在ROS中，参数文件常以YAML文件的格式保存，形式如下：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/1b3f0c79101340e396181f9549f4a366.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)常用 rosparam 命令用法：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/aedca38406e444e2a82ec53fe9ece653.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_18,color_FFFFFF,t_70,g_se,x_16#pic_center)  
我们打开海龟仿真节点来试一下。

    roscore


    rosrun turtlesim turtlesim_node


#### 显示参数列表

    rosparam list


![在这里插入图片描述](https://img-blog.csdnimg.cn/de7a2afc8c604f25b57c2a158507a883.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

观察一下这些参数，可以看到：  
/turtlesim/background\_b  
/turtlesim/background\_g  
/turtlesim/background\_r  
分别代表了小海龟的背景RGB颜色，目前是蓝色。  
/rosdistro 为ros的版本代号  
/roslaunch/uris/host\_ck\_vpc\_\_35381  
/rosversion 当前ros的版本  
/run\_id 进程的id号

#### 显示某个参数值

例：

    rosparam get /turtlesim/background_b


![在这里插入图片描述](https://img-blog.csdnimg.cn/3d5f5964c04a4889986b51d1aac371be.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 设定某个参数值

例：

    rosparam set /turtlesim/background_b 100


把/turtlesim/background\_b的值改成100，再get一下可以看到已经改成了255

![在这里插入图片描述](https://img-blog.csdnimg.cn/fb6a846a27504bdaa719c3b9afbbba4d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
但是，海龟的背景颜色还没变。我们需要发送一个clear的空内容服务请求：

    rosservice call /clear "{}"


可以看到背景以及改过来了。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/2ff3c8712b5a47c3a3fdd4410d3b4214.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 保存参数到文件

例：

    rosparam dump param.yaml


将参数导出，保存为param.yaml文件。  
默认保存位置为当前工作空间根目录下，我们可以打开看看：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/8af9680a5b9b4377982887ec9f91582e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 从文件读取参数

我们可以直接在这个yaml文件里修改参数，然后导回去。  
比如背景色改成 255，255，255（白色）  
![在这里插入图片描述](https://img-blog.csdnimg.cn/a77cc6759b884799b647dffd9ed2eb95.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
导回去：

    rosparam load param.yaml


clear一下，背景就变白色了。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/e6345f4d22634bacb43bb64ffca537cb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 删除参数

例：

    rosparam delete /turtlesim/background_b


就可以删掉指定的参数。  
删掉后可以用`rosparam set ...`设回来。

### 4 使用程序来使用参数（C++）

这次我们使用程序来获取和设置参数。  
如何获取/设置参数：

*   get函数获取参数
*   set函数设置参数

#### 创建代码

（源码：https://github.com/guyuehome/ros\_21\_tutorials/tree/master/learning\_parameter/src）  
![在这里插入图片描述](https://img-blog.csdnimg.cn/8049bbeadfb84157b3830b2fbbf39ec5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)注意这段代码需要修改一下以满足我们当前Noetic版本ROS的要求，背景色的三个参数名前面都要带 /turtlesim，因为Noetic中背景色的参数名称就是这样。修改：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/63e7a45ed3ae49c5ad4bdf0ed2d025a4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

完成后将代码拷贝到src文件夹下。

#### 编译

先配置CMakeLists.txt编译规则，规则：

*   设置需要编译的代码和生成的可执行文件；
*   设置链接库

将下面代码拷贝到指定位置：

    add_executable(parameter_config src/parameter_config.cpp)
    target_link_libraries(parameter_config ${catkin_LIBRARIES})


然后编译：

    cd ~/catkin_ws
    catkin_make


#### 运行

默认已经source，接着运行。

    roscore


    rosrun turtlesim turtlesim_node


    rosrun learning_parameter parameter_config


可以看到背景从蓝色变成了白色。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/f44bf0a116b841d3bac93c3f657a5700.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 5 使用程序来使用参数（Python）

这次我们使用程序来获取和设置参数。  
如何获取/设置参数：

*   get函数获取参数
*   set函数设置参数

#### 创建代码

（源码：https://github.com/guyuehome/ros\_21\_tutorials/tree/master/learning\_parameter/scripts）  
注意Python3代码格式的修改（绿字）。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/b9bd286def6544e491acdf50abf37412.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
注意服务名前面补上 /turtlesim，因为Noetic中背景色的参数名称就是这样。

![在这里插入图片描述](https://img-blog.csdnimg.cn/5587dfc4659344a8a9262ac56b55fb06.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_18,color_FFFFFF,t_70,g_se,x_16#pic_center)

将代码拷贝到新建的scripts文件夹下。  
右击py文件→属性，打开执行权限。

#### 编译

配置CMakeLists.txt编译规则  
加上一个关于parameter\_config.py的catkin\_install\_python方法：  
下面代码写到指定位置

![在这里插入图片描述](https://img-blog.csdnimg.cn/56359a414e684390ac9ddea9fb360488.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
然后编译：

    cd ~/catkin_ws
    catkin_make


#### 运行

默认已经source，接着运行。

    roscore


    rosrun turtlesim turtlesim_node


    rosrun learning_parameter parameter_config.py


可以看到背景从蓝色变成了白色。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/3a2abbaa68a64678bb19c40ac3575416.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#  ROS中的坐标管理系统

本节学习ROS中的坐标管理系统。  
(部分图摘自：b站【古月居】古月·ROS入门21讲)

### 1 机器人中的坐标变换

机器人运动学的核心，描述任意两个坐标系之中任意两个向量之间的变换，可以用一个4×4的**变换矩阵**（Transformation Matrices）来描述它的平移和旋转变化。  
变换矩阵中有包括**旋转矩阵**（Rotation Matrix）的信息和位置移动（Translation）的信息。  
相关教程推荐B站的机器人学入门课程：台大机器人学之运动学——林沛群。一步步手动进行矩阵的推导计算，非常易懂，超级推荐。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/de0647851d3a42f09f607607fb24ad7b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 2 TF功能包

一个机器人中，可以有很多坐标系，我们需要去描述任意两个坐标系之间的关系，涉及到大量的矩阵运算。我们可以用ROS中的TF(Transform)功能包来解决问题。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/566c30e0e5e7407fb78e1c6381851dcc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_15,color_FFFFFF,t_70,g_se,x_16#pic_center)

TF功能包的特点：默认能记录10秒内机器人所有坐标系之间的位置关系。

能具体了解什么信息呢？举个栗子：

*   5秒钟之前，机器人头部坐标系相对于全局坐标系的关系是什么样的？
*   机器人夹取的物体相对于机器人中心坐标系的位置在哪里？
*   机器人中心坐标系相对于全局坐标系的位置在哪里？

#### TF坐标变换如何实现？

实现机制：

*   广播TF变换
*   监听TF变换

这有别于之前topic和service的机制。广播和监听的具体实现会在下一节讲解。  
在ROS Master启动后，启动TF后，会在后台维护一个名为“TF树（TF Tree）”的数据结构。所有的坐标系都是通过树形结构保存在这个树结构当中，当有结点想查询某两个坐标系之间的关系的话，直接可以查询这个TF Tree来得到。

#### TF的一个小案例

![在这里插入图片描述](https://img-blog.csdnimg.cn/74a7c952f6864a1991056c6b570f9b69.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
比如这辆带激光雷达的车，车体是以base\_link为坐标系的，激光雷达是以base\_laser为坐标系的，可以看到base\_laser是base\_link向x轴平移了0.1m，向z轴平移了0.2m，y轴没有平移。  
当base\_laser测到离墙面的距离为0.3m，即向量(0.3,0,0)时，就可以根据图下方的TF tree进行坐标系之间的数据变换的运算，从而算出base\_link的相对与测距点的相对向量(0.4,0,0.2)。

### 3 小程序：小海龟跟随实验

我们通过一个小程序来实现一个小海龟跟随另一个小海龟，并通过可视化的方法以理解坐标系的变换。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/899af48c36a4428d8c28049daca42643.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_11,color_FFFFFF,t_70,g_se,x_16#pic_center)  

在这个小程序中，我们控制一只海龟移动，另一只会实时跟随我们直到重合。  
在noetic版本的ROS中，预装了这个小程序，不过直接运行可能会报错。

自带：

```
sudo apt-get install ros-melodic-turtle-tf
```

报错的原因可能是[Python解释器](https://so.csdn.net/so/search?q=Python%E8%A7%A3%E9%87%8A%E5%99%A8&spm=1001.2101.3001.7020)的指向问题。我们先打开终端输入：

    cd /usr/bin/
    sudo rm -r python
    sudo cp python3 python

（第二行 rm -r 找不到文件的忽略即可）  
/usr/bin/下没有名为python文件，我们将python3指向python就行了（个人理解）。

#### 打开小程序

接着我们正式打开小程序：

    roslaunch turtle_tf turtle_tf_demo.launch


这里直接使用的roslauch，会在后面小节讲到。  
打开后就会有两只海龟，我们直接用键盘操作一只海龟前进，另一只会跟过来。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/dcdb4bda8dd84b9e9162c8385401f6bf.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 查看当前的TF树

我们来查看当前的TF tree，查看一下坐标系之间的关系。  
输入：

    rosrun tf view_frames


BUT，noetic直接运行可能会报错，无法生成pdf文件：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/310125d01d71474d9273fce55fc59eee.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
我们先打开它指向的那个view\_frames文件的修改权限：

    sudo chmod a+w /opt/ros/noetic/lib/tf/view_frames


然后打开，88行后加上这句`vstr = str(vstr)`：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/a9751749e37247669f708b4697aecba6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
再运行：

    rosrun tf view_frames


可在用户文件夹下生成一个pdf文件：  
可以看到有3个坐标系，除了两个海龟自身的坐标系，还有个world坐标系。  
这颗TF树展示了当前的坐标间的位置关系，**turtle1和turtle2是相对world坐标系变化的**。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/316ca90957364a8bb769e2e78ba39afc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 坐标相对位置关系可视化1（tf\_echo）

比如我们想看两个海龟的相对变换关系，直接输入：

    rosrun tf tf_echo turtle1 turtle2


![在这里插入图片描述](https://img-blog.csdnimg.cn/5c46bec9a5cf4b4f978f5f76dfb6d8b8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)我们接着操控海龟1移动，相对关系就发生了变化：

![在这里插入图片描述](https://img-blog.csdnimg.cn/26e93075fcc74153a1d65f2d8f7332c8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)这里包含了Translation和Rotation的信息。  
Translation表示了相对位移的信息（是一个3×1的向量）。  
Rotation表示了旋转矩阵的信息（一个3×3的矩阵，但自由度为3），它又有两种表示方式：  
1.RPY表示法(pitch俯仰角、yaw偏航角、roll翻滚角)  
2.四元数法(Quaternion)  
都可以表示旋转矩阵的信息，这些概念理解建议学习前面提到的机器人运动学基础。

Rotation和Translation合起来可以构成变换矩阵(4×4，见本节第一部分的图)。  
我这里再放一幅Rotation和Translation包含所有的变换信息的图方便理解。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/41c8f3c343984b25ad212f2debc66e31.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 坐标相对位置关系可视化2（[rviz](https://so.csdn.net/so/search?q=rviz&spm=1001.2101.3001.7020)）

rviz工具会在后面详述，先体验一下，输入：

    rosrun rviz rviz -d `rospack find turtle_tf` /rviz/turtle_rviz.rviz


打开rviz界面。  
上面Fixed Frame选 world。Add选添加TF，可以看到3个坐标系了。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/d72d28e1088d43a8b5276235125e299e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
控制海龟运动，坐标系发生改变，然后坐标系turtle2原点会靠近turtle1原点：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/ec342d5413b84fd1ad3ab7845d41470b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
下图中左边变换矩阵的运算，其实就是坐标移动的本质。两个坐标系相对于world坐标系的变换的乘积可以求得两个坐标系相对的变换关系。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/4777d9dba1ee4b5291ef2eb3a248e114.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#  tf坐标系广播与监听的编程实现

上节学习了坐标管理系统tf的简介和理论，这节讲解TF坐标变换的实现机制 **广播**与 **监听**的编程实现。  
(部分图摘自：b站【古月居】古月·ROS入门21讲)

### 1 创建功能包

创建的 learning\_tf 包来进行代码存放和编译。

    cd ~/catkin_ws/src
    catkin_create_pkg learning_tf roscpp rospy tf turtlesim


### 2 创建代码并编译运行（C++）

**如何实现一个TF广播器**：

*   定义TF广播器（TransformBroadcaster）
*   创建坐标变换值
*   发布坐标变换（sendTransform）

**如何实现一个TF监听器**：

*   定义TF监听器（TransformListener）
*   查找坐标变换（waitForTransform、lookupTransform）

#### 创建代码

(源码：https://github.com/guyuehome/ros\_21\_tutorials/tree/master/learning\_tf/src)  
用红字标示了自己的注解笔记。

turtle\_tf\_broadcaster.cpp ：根据实现的步骤，我们想要通过TF广播任意两个坐标系之间的位置关系，需要建立一个广播器，然后创建坐标的变换值，将这个变换矩阵的信息广播出去(插入TF tree)。  
注意下面main函数时我们需要传入参数，参数从终端命令行输入（输入的参数包括节点名称 和 turtle\_name），下面运行部分会解释一下传入的参数的方法。这样我们从终端传参可以重复跑两遍这个C++程序分别对应turtle1和turtle2的广播器。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/123a8475efaf4ba28794fa02e7071b59.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
坐标关系插入TF tree后，树会自动运算变换矩阵，后面我们就可以用监听器调用了。  
turtle\_tf\_listener.cpp：根据步骤，从tf中获取任意两个坐标之间的位置关系(通过waitfor和lookup)，然后命令turtle2向turtle1以定义的速度(Twist)移动。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/b9fa7b284dcc4f01b95b4480b80a638a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
将代码拷贝到src文件夹下。

#### 编译

先配置CMakeLists.txt编译规则：

*   设置需要编译的代码和生成的可执行文件；
*   设置链接库；

将下面代码拷贝到指定位置：

    add_executable(turtle_tf_broadcaster src/turtle_tf_broadcaster.cpp)
    target_link_libraries(turtle_tf_broadcaster ${catkin_LIBRARIES})
    
    add_executable(turtle_tf_listener src/turtle_tf_listener.cpp)
    target_link_libraries(turtle_tf_listener ${catkin_LIBRARIES})


![在这里插入图片描述](https://img-blog.csdnimg.cn/c3350933996e4550bf2022b4e3010b4c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
然后编译：

    cd ~/catkin_ws
    catkin_make


#### 运行

默认已经source，接着分别在每个终端运行。

    roscore


    rosrun turtlesim turtlesim_node


注：  
我们下面直接在命令行传入参数。  
第1个参数：我们在turtle\_tf\_broadcaster.cpp定义节点时使用了"my\_tf\_broadcaster"的名字，我们使用`__name:=`传入新的名字取代"my\_tf\_broadcaster"，这样避免名字重复（因为ROS中节点名字不能重复），这样就可以重复跑程序了。  
第2个参数是turtle名称 turtle1 和 turtle2。

    rosrun learning_tf turtle_tf_broadcaster __name:=turtle1_tf_broadcaster /turtle1


    rosrun learning_tf turtle_tf_broadcaster __name:=turtle2_tf_broadcaster /turtle2


    rosrun learning_tf turtle_tf_listener


上面完成后就会有一个海龟生成并跑向中间的第1只海龟。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/71bb965cbcda4fb894b97b7a953f8ef5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

    rosrun turtlesim turtle_teleop_key


我们用键盘控制海龟，同样可以让第2只海龟追着我们跑。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/349593713e414f44a87d72022ad31c92.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 2 创建代码并编译运行（Python）

**如何实现一个TF广播器**：

*   定义TF广播器（TransformBroadcaster）
*   创建坐标变换值
*   发布坐标变换（sendTransform）

**如何实现一个TF监听器**：

*   定义TF监听器（TransformListener）
*   查找坐标变换（lookupTransform）

#### 创建代码

(源码：https://github.com/guyuehome/ros\_21\_tutorials/tree/master/learning\_tf/scripts)  
用红字标示了自己的注解笔记。

turtle\_tf\_broadcaster.py ：根据实现的步骤，我们想要通过TF广播任意两个坐标系之间的位置关系，需要建立一个广播器，然后创建坐标的变换值，将这个变换矩阵的信息广播出去(插入TF tree)。  
注意下面main函数中，我们的turtlename是一个通过终端传入的参数，下面运行部分会解释一下传入的参数的方法。这样我们从终端传参可以重复跑两遍这个python程序分别对应turtle1和turtle2的广播器。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/730fd74e646a498bbceabf0fafa65fbd.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
坐标关系插入TF tree后，树会自动运算变换矩阵，后面我们就可以用监听器调用了。  
turtle\_tf\_listener.py：根据步骤，从tf中获取任意两个坐标之间的位置关系，然后命令turtle2向turtle1以定义的速度(Twist)移动。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/c5f51c1e0e2e4d6fac740befe8c301b0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
将代码拷贝到新建的scripts文件夹下。  
右击py文件→属性，打开执行权限。

#### 编译

先配置CMakeLists.txt编译规则：  
加上一个关于turtle\_tf\_broadcaster.py和turtle\_tf\_listener.py的catkin\_install\_python方法：  
将下面代码写到指定位置：

![在这里插入图片描述](https://img-blog.csdnimg.cn/326718fa8b1d42cb8cb94bacb04ad64b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
然后编译

    cd ~/catkin_ws
    catkin_make


#### 运行

默认已经source，接着运行。

    roscore


    rosrun turtlesim turtlesim_node


注：  
我们下面直接在命令行传入参数。  
第1个参数：我们在turtle\_tf\_broadcaster.py定义节点时使用了"turtle\_tf\_broadcaster"的名字，我们使用`__name:=`传入新的名字取代"my\_tf\_broadcaster"，这样避免名字重复（因为ROS中节点名字不能重复），这样就可以重复跑程序了。  
第2个参数是turtle名称 turtle1 和 turtle2。

    rosrun learning_tf turtle_tf_broadcaster.py __name:=turtle1_tf_broadcaster _turtle:=turtle1


    rosrun learning_tf turtle_tf_broadcaster.py __name:=turtle2_tf_broadcaster _turtle:=turtle2


    rosrun learning_tf turtle_tf_listener.py


注：显示“ the rosdep view is empty: call ‘sudo rosdep init’ and ‘rosdep update’ ”的话不用介意。  
上面完成后就会有一个海龟生成并跑向中间的第1只海龟。

    rosrun turtlesim turtle_teleop_key

我们用键盘控制海龟，同样可以让第2只海龟追着我们跑。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/df868e2523514f2396f22b0a97fc1e11.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

# launch启动文件的使用方法

在之前的学习中，比如上一讲TF坐标广播和监听，启动程序非常麻烦，一共启动了6个终端窗口，并且涉及到终端向ROS的参数传递。  
**launch启动文件**将解决这个问题，帮助我们快速部署、整合并启动程序。  
(部分图摘自：b站【古月居】古月·ROS入门21讲)

### 1 [launch文件](https://so.csdn.net/so/search?q=launch%E6%96%87%E4%BB%B6&spm=1001.2101.3001.7020)结构

*   由XML语言写的，可实现多个节点的配置和启动。
*   不再需要打开多个终端用多个rosrun命令来启动不同的节点了
*   可自动启动ROS Master  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/f0170ee5e34f415d93722cd064dcde86.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 2 launch文件语法

#### 根元素

注：name为节点名称，会取代程序中初始化节点 init 时赋予的名字。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/b40b24082fca46798de1266eee4c5c70.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)其他：  
output：控制某个节点node把日志信息打印到终端。  
respawn：节点奔溃后是否重启  
required：节点是否为必须节点，即改节点奔溃后须终止其他节点  
ns：自定义的命名空间，在自定义的命名空间中运行节点  
args：输入参数用

#### 参数设置

param：【在ROS参数服务器中】处理一个参数  
rosparam：【在ROS参数服务器中】处理多个参数  
arg：【不存在于ROS的参数服务器中】仅在launch文件中出现，可作为node运行时传的参数，如之前在终端输入指令时传的参数。

![在这里插入图片描述](https://img-blog.csdnimg.cn/19ebe5c0515d4eeeb010e738e3067058.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### 重映射、嵌套

注意嵌套include之后，调用另一个launch文件，便会启动该文件内的所有内容。![在这里插入图片描述](https://img-blog.csdnimg.cn/8ca1928ac4d44558a2c23167a6e986d7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)更多标签参见：http://wiki.ros.org/[roslaunch](https://so.csdn.net/so/search?q=roslaunch&spm=1001.2101.3001.7020)/XML

### 3 示例

演示一些launch文件的实例。

需要先创建个新的功能包 learning\_launch，包本身不需要添加别的依赖。

    cd ~/catkin_ws/src
    catkin_create_pkg learning_launch


可以在learning\_launch下新建一个launch文件夹，来存放launch文件。  
（源文件：https://github.com/guyuehome/ros\_21\_tutorials/tree/master/learning\_launch/launch）  
可以把源文件中的几个launch文件拷贝到launch文件夹下。

打开launch文件后，文本编辑器的菜单下选择“查看”→“高亮模式”，选择XML可方便查看代码。  
下面看一些示例。

#### simple.launch

![在这里插入图片描述](https://img-blog.csdnimg.cn/4c88aa1600cd4b71a503410c678082cd.png#pic_center)  
本例对之前的learning\_topic功能包下的发布和订阅节点的程序进行了整合，设定了node的name，并选择将日志信息打印到终端。

我们试着启动该launch文件，先编译一下然后输入`roslaunch 包名 文件名`启动：

    cd ~/catkin_ws
    catkin_make
    roslaunch learning_launch simple.launch


我们可以看到启动launch后，发布和订阅的日志同时打印到了终端。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/2d09f64c462f45d2925faf8c77d26200.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### turtlesim\_parameter\_config.launch

![在这里插入图片描述](https://img-blog.csdnimg.cn/1e4e5c9fd179471596b08d2a91172181.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
本例是对参数的一些操作。  
注：源文件的lauch文件因为Tab键的关系又没有对齐，自己可以手动按每4个空格对齐代码。

将源码中的config文件夹下的param.yaml拷贝到目标目录：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/0268fcc0450d4678a3e0618e3512577a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)然后启动（前面编译过一次不用再编译了）：

    roslaunch learning_launch turtlesim_parameter_config.launch


然后打开新终端，我们访问一下新设置的参数：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/dc82e57095dc4d37bf697fb969a2e43e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

我们可以看到 /turtle\_name1 参数是写在node节点 turtlesim\_node 下的，因此该参数有 turtlesim\_node的命名空间，参数全名叫： /turtlesim\_node/turtle\_name1。  
同理load的参数也带有当前节点名的命名空间，并且这个yaml文件自身建了个group命名空间。  
而 /turtle\_number 参数是写在外面的，因此参数就叫： /turtle\_number 。

#### start\_tf\_demo\_c++.launch

这个例子把上一节的tf坐标广播与监听的一系列命令行整合在了一起。也不用在命令行中传参数了。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/c8b54ddaeac84a239df1213d4a31987b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
启动（前面编译过一次不用再编译）：

    roslaunch learning_launch start_tf_demo_c++.launch


![在这里插入图片描述](https://img-blog.csdnimg.cn/7101a4bfd8964f01944f12eb409c273a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### start\_tf\_demo\_py.launch

同上，就是根据python的源代码的写法，传参的时候手动定义了一个节点下的参数：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/f88cd85a33fe4080b23aa9fa6bbe0f8a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)运行效果同上。

#### turtlesim\_remap.launch

使用include，调用另一个launch文件simple.launch，可启动该文件内的所有内容。  
并将topic名改动。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/1d0fafc323b34f3f8ac207b3592787c2.png#pic_center)  
启动（前面编译过一次不用再编译）：

    roslaunch learning_launch turtlesim_remap.launch


![在这里插入图片描述](https://img-blog.csdnimg.cn/94a82cf9ccc44d7fb5199171c7a2e514.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)我们输入`rostopic list`可以看到话题名已经改成了/cmd\_vel  
我们可以向新话题名/cmd\_vel发布一个新的速度指令，海龟应该就会动起来（效果略^^）！

# 常用可视化工具的使用

这节是最后一节，介绍一些常用可视化工具的使用。  
在课的一开始曾经介绍过ROS的其中一个可视化工具，计算图可视化指令——rqt\_graph。  
这期将介绍其他的可视化工具，包括**Qt工具箱**、前面接触到的**Rviz**等。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/f46881ae95394739bba415a2e8c5f093.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
(部分图摘自：b站【古月居】古月·ROS入门21讲)

### 日志输出工具——rqt\_console

我们启动海龟键盘控制节点，打开日志输出工具。

    roscore


    rosrun turtlesim turtlesim_node


    rosrun turtlesim turtle_teleop_key


    rqt_console


再让海龟撞上南墙，日志输出工具就会把日志信息都显示出来。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/57414b4c3d8a485baf3858b5a664df5e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 绘制数据曲线——rqt\_plot

前面已经打开了海龟控制的相关节点。  
我们打开数据绘图工具rqt\_plot。

    rqt_plot


在输入框中输入左斜杠`/`可以看到自动填充项，我们选择 /turtle1/pose 按回车，就会显示位置信息的实时情况。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/f203b699968b4ca89255e1fbaaa03509.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
我们移动小海龟，曲线就会发生变化。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/478f0a7dcf30497691dec44026e14274.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

可以按暂停停止记录，可以使用放大镜来放大缩小曲线：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/949ce234854d4523af4d163d554753c4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 图像渲染工具——rqt\_image\_view

可相机的图像数据的插件，可简单查看图像摄像头的图像。

    rqt_image_view


![在这里插入图片描述](https://img-blog.csdnimg.cn/fb7163eaa1624dc8b0828a7111dd7c20.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_17,color_FFFFFF,t_70,g_se,x_16#pic_center)

### [图形界面](https://so.csdn.net/so/search?q=%E5%9B%BE%E5%BD%A2%E7%95%8C%E9%9D%A2&spm=1001.2101.3001.7020)总接口——rqt

我们直接输入[rqt](https://so.csdn.net/so/search?q=rqt&spm=1001.2101.3001.7020)可以打开图形界面总接口  
我们可以在Plugin菜单下面打开各种图形界面的小工具，分块显示在下方。  
前面介绍的这些Qt工具包都可以在这里找到。

    rqt


![在这里插入图片描述](https://img-blog.csdnimg.cn/3e449fe588294335987bcc0c983ab4f7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### Rviz

我们在前面曾使用过Rviz来显示空间坐标系的相对位置。  
Rviz不仅可以显示坐标系，还可以可视化各种各样的东西（包括导航、点云、运动规划等），是一个综合的数据可视化平台。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/c6c33a6bb285446cbb4db866919333da.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/8248be124334408d8a32d3d40adacb64.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/e61c0f2ee9c144ddbd9e70ea94321da0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
我们打开Rviz：

    rosrun rviz rviz


举个栗子：  
我们Add一个Image项，就可以通过设置Topic名（比如是摄像头Topic）来获取图像信息了。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/3ad8f02d017b40149e007b38bd58f5bf.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### Gazebo

仿真平台简介  
![在这里插入图片描述](https://img-blog.csdnimg.cn/2ea6dbbbc7bd4cd48c743571bc2e3a3e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/3ad731b8f3fd4d17a5f58938855f2a3f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAdGFrZWRhY2hpYQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 最喜欢的一句话

ROS是一个工具，也是一种生活方式，但他并不完美，也不是机器人开发的全部。  
ROS is thus more of a way of life for robot programmers than simply an operating system.

Let’s keep learning！  
（ROS入门学习笔记完结）