#安装完成Ubuntu20.04之后要做的事：基础配置、界面美化、异常处理、常用软件的安装与常用命令


#### 文章目录
- - <ul><li>- - - - - - - - - - - - - - - - - - - - - - 


**最近换了电脑，重装了双系统，在安装了Ubuntu20.04系统之后，要做的基础配置、界面美化、异常处理与常用软件的安装，此博文方便我自己重裝系統之後快速使用**

## 一、换源

Ubuntu系统自带的源都是国外的网址，国内用户在使用的时候下载比较慢甚至无法获取，在安装各种库或软件时会深受其折磨！解决方案是直接替换成国内的镜像源（建议使用第二种或第三种）

### 1.1 通过软件更新

打开软件更新

![https://img-blog.csdnimg.cn/fae3724e93544d2099d6ec85164aae0d.png#pic_center](https://img-blog.csdnimg.cn/fae3724e93544d2099d6ec85164aae0d.png#pic_center)

选择Download from-&gt;Other，找到China，选择源。关闭界面等待自动更新源

### 1.2 通过修改源文件

（1）备份源文件：

>  
 sudo cp /etc/apt/sources.list /etc/apt/sources.list.old 


（2）打开文件：

>  
 sudo gedit /etc/apt/sources.list 


（3）换源：推荐清华或者阿里云的源（根据自己的网去尝试，选择最快的一个）：，选择Ubuntu版本（查看ubuntu版本命令：`cat /etc/issue`）并复制源内容，覆盖`sources.list`文件原来的内容：

![https://img-blog.csdnimg.cn/b1ab9fcd4b9a4ab0a2f19329d0597ffa.png#pic_center](https://img-blog.csdnimg.cn/b1ab9fcd4b9a4ab0a2f19329d0597ffa.png#pic_center)

（4）换过源之后要更新：

>  
 sudo apt-get update 


### 1.3 使用鱼香ROS一键换源

```
wget http://fishros.com/install -O fishros &amp;&amp; . fishros

```

![https://img-blog.csdnimg.cn/86ba97f1a9ba4177927de8fa8b411318.png#pic_center](https://img-blog.csdnimg.cn/86ba97f1a9ba4177927de8fa8b411318.png#pic_center) 选择5一件安装，安装完记得更新：

>  
 sudo apt-get update 


## 二、安裝显卡驱动

參考
- 找到合适自己电脑显卡的驱动，打开终端输入命令：
```
ubuntu-drivers devices

```

显示电脑上可用的nvidia驱动，只需要安装推荐的版本即可（后面有`recommend`字样）

![https://img-blog.csdnimg.cn/fbbb6953be594c90b6824cf34fcfb827.png#pic_center](https://img-blog.csdnimg.cn/fbbb6953be594c90b6824cf34fcfb827.png#pic_center)
- 打开电脑里的软件和更新app
![https://img-blog.csdnimg.cn/63fe91cd11a84ff5b7d692fe59e8879b.png](https://img-blog.csdnimg.cn/63fe91cd11a84ff5b7d692fe59e8879b.png)

来到附加驱动这个页面，选择刚刚看到的`recommand`的驱动，点击应用更改，等待安装完成。 也可以手动安装：

```
sudo apt-get install nvidia-driver-470

```

然后重启电脑，打开终端，输入命令

```
nvidia-smi

```

出现下面图中显示則安裝成功：

![https://img-blog.csdnimg.cn/defb6feaa7e04aaca1a3a5722f41d3b9.png#pic_center](https://img-blog.csdnimg.cn/defb6feaa7e04aaca1a3a5722f41d3b9.png#pic_center)

### 2.1 解决显卡驱动安装的错误

我的笔记本（惠普暗影精灵8）安装时遇到一些麻烦与解决办法，如果你的电脑同时有核显和独显，请先切换成独显！ （1）安装系统后进不了界面，只有一个光标 在启动选项界面的ubuntu选项下按e，移动光标将`quiet splash $vt.....`修改为

```
quiet splash nomodeset

```

然后按照下方提示启动系统。这只是临时办法，需要进入系统彻底解决

（2）进入界面后无法调节亮度（极暗），没有WIFI选项 连接网线，安装intel提供的20.04补丁包，会安装内核`5.14.0-1059-oem`，安装完成后直接重启，WIFI ，亮度调节，intel lris xe 核显都会正常，进入系统也没有问题了

```
sudo apt-get install linux-oem-20.04

```

（3）安装显卡驱动后进不了界面，只有一个光标，首先确定是不是显卡驱动导致的 Ctrl+Alt+F1，没有反应说明是，一般是显卡和内核不匹配导致的 Ctrl+Alt+F2，进入命令行，登陆，然后卸载显卡驱动

```
sudo apt-get remove --purge nvidia*
sudo apt-get autoremove

```

重新安装其他版本的显卡驱动 按照上面方法安装显卡驱动，一般情况下`recommand`是和内核匹配的，但是可能安装了`5.14.0-1059-oem`，`recommand`并不对，我是显示`520 recommand`，但是安装`470`才没问题

（4）如果不小心更新了内核，导致显卡和内核不匹配，删除内核方法为 从旧版本内核的恢复模式进入系统，首先查询当前使用的内核版本，别删错了

```
uname -a

```

查询系统中装了多少内核

```
dpkg --get-selections|grep linux

```

![https://img-blog.csdnimg.cn/aa6c4c0b6f69479a82d1a72c71dd71d4.png#pic_center](https://img-blog.csdnimg.cn/aa6c4c0b6f69479a82d1a72c71dd71d4.png#pic_center)

删除不需要的内核，后面内容从上图复制

```
sudo apt-get purge linux-image-*.*.*-**
sudo apt-get purge linux-headers-*.*.*-**

```

删除后再次执行

```
dpkg --get-selections|grep linux

```

查看内核是否都删除，有的内核后面会显示是`deinstall` ，表示已经卸载但未删除，清理：

```
sudo dpkg -P linux-***-*.*.*-**-***

```

## 三、安裝中文输入法

### 3.1 安装

打开`language support`，第一次进入时可能会提醒你安装一些语言，同意并输入密码等待安装完成即可，默认的输入法是`IBus`： ![https://img-blog.csdnimg.cn/c5a69722efec4585b6086c4ddf2ded78.png](https://img-blog.csdnimg.cn/c5a69722efec4585b6086c4ddf2ded78.png) 选择`Install/Remove Languages`，找到中文简体勾选并应用： ![https://img-blog.csdnimg.cn/366d8d4f4c81482d857f9de704cf578c.png](https://img-blog.csdnimg.cn/366d8d4f4c81482d857f9de704cf578c.png) 打开设置找到`Region&amp;Language`，点击+添加输入法： ![https://img-blog.csdnimg.cn/f7c55e6c5c5f4a2b994c58b975aec798.png](https://img-blog.csdnimg.cn/f7c55e6c5c5f4a2b994c58b975aec798.png) 点击Chinese，选择智能拼音添加（如果没有重启电脑就可以），输入法切换快捷键是win+space，而切换语言是shift ![https://img-blog.csdnimg.cn/3edafeda80884dd2a32909189f67019b.png](https://img-blog.csdnimg.cn/3edafeda80884dd2a32909189f67019b.png) ![https://img-blog.csdnimg.cn/577b717b98b4466784047296e85dc9a2.png](https://img-blog.csdnimg.cn/577b717b98b4466784047296e85dc9a2.png)

### 3.2 解决键盘短暂失灵和延迟的问题

在我的系统里，出现了键盘突然失灵、输入延迟，但是鼠标是正常的问题，要等几分钟才好，通过了解到，是因为ibus拼音输入法的问题，重启一下ibus就行，并参考他写了个脚本，点击就可重启ibus
- restart_key.sh（随便放在哪里，然后打开终端赋予它运行权限：`sudo chmod 777 restart_key.sh`）
```
#!/bin/bash
ibus restart
exit 0

```
- ibus_hsy.desktop，其中几个路径修改为自己的，右击 “ibus_hsy.desktop”，属性， 权限勾选“允许文件作为程序执行”
```
[Desktop Entry]
Name=重启键盘
Name[zh_CN]=重启键盘
Exec = gnome-terminal -e "bash -c '/home/zard/bin/restart_key.sh;$SHELL'" 
Path = /home/zard/
Icon= /home/zard/bin/海洋之歌.jpg
Terminal=true
Type=Applicatio

```

这里我没有像作者一样放在桌面，因为在打开很多界面的情况下去桌面点击比较麻烦，我选择放在左侧任务栏。但是`ibus_hsy.desktop`不是安装的，所以不能将它加入桌面侧边的任务栏，而通过软件中心安装的软件就有图标，并能加入到启动器上，这是因为它们有一个desktop配置文件的缘故。这些配置文件在`/usr/share/applications`这个文件夹下面，因此我们将`ibus_hsy.desktop`复制到此文件夹下：

```
sudo cp -r ibus_hsy.desktop /usr/share/applications

```

然后就能在软件中心找到它了，在左下角软件列表中将其添加到任务栏：

![https://img-blog.csdnimg.cn/0039e79898294b8ebb72657abdc6bdf3.png#pic_center](https://img-blog.csdnimg.cn/0039e79898294b8ebb72657abdc6bdf3.png#pic_center)

## 四、双系统时间同步

windows使用当地时间，ubuntu使用UTC时间，两者相差8h的时间。首先安装时间同步工具：

```
sudo apt install ntpdate

```

使用工具通过互联网同步时间：

```
sudo ntpdate time.windows.com

```

设置ubuntu使用当地时间：

```
sudo hwclock --localtime --systohc

```

## 五、修改双系统启动顺序以及美化grub界面

### 5.1 修改双系统启动顺序

```
sudo gedit /etc/default/grub

```

將

```
GRUB_DEFAULT=0 # 修改爲要启动的系統序号（从0開始）
GRUB_TIMEOUT_STYLE=hidden
GRUB_TIMEOUT=10 # 等待时间，单位是秒

```

更新`grub`：

```
sudo update-grub

```

### 5.2 grup引导界面美化

法一：在github上下载相关的美化主题。

```
git clone https://github.com/vinceliuice/grub2-themes.git

```

进入grub2-themes目录文件安装

```
cd grub2-themes
sudo ./install.sh

```

按照提示选择主题、颜色和分辨率即可完成安装 ![https://img-blog.csdnimg.cn/525d24b2e445401999ac992ed0960deb.png#pic_center](https://img-blog.csdnimg.cn/525d24b2e445401999ac992ed0960deb.png#pic_center) 法二：去这个地址：，下载主题，下载解压完成后，执行命令：

```
sudo chmod a+x install.sh
./install.sh

```

我安装的`Vimix-1080p`效果如下

![https://img-blog.csdnimg.cn/4ff69459ce894753b7d9c2c1cc745da2.jpeg#pic_center](https://img-blog.csdnimg.cn/4ff69459ce894753b7d9c2c1cc745da2.jpeg#pic_center)

## 六、系统卡死的处理办法

无论Ubuntu出现什么状况**卡死机千万不能强制关机**！！！！因为这个时候强制关机大多数情况下是无法再次进入系统的（亲身体验）。这里有安全重启的办法：
1. 同时按住 `Ctrl` 和 `Alt` 键，按住不要放（一直不要松）1. 按一下 `SysRq` 键（有的键盘是`PrtSc`）1. 依次按下 `R, E, I , S , U , B` 键
这些步骤做完后，系统就会安全重启

## 七、主题美化

为了完全抛弃Windows，更舒服地使用Ubuntu，不得不美化一下系统界面。参考这篇，安装Tweaks，通过Tweaks切换下载的主题，图标等等

```
sudo apt install gnome-tweak-tool
# 安装 gnome 扩展模块，配合 tweak 来实现美化。
sudo apt-get install gnome-shell-extensions

```

![https://img-blog.csdnimg.cn/4abfd8bb3ecd4559996ec07251e4ac56.png#pic_center](https://img-blog.csdnimg.cn/4abfd8bb3ecd4559996ec07251e4ac56.png#pic_center) 重启gnome：按Alt+F2进入命令窗口，输入r，并回车。点击extensions选项，把User themes打开（若无法打开先重启电脑）。

![https://img-blog.csdnimg.cn/d19f5d07869e4acc9937bf31707d8f93.png#pic_center](https://img-blog.csdnimg.cn/d19f5d07869e4acc9937bf31707d8f93.png#pic_center)

下载主题网站，可以选择各种主题、壁纸、鼠标样式、Dock样式、图标主题，将下载好的主题文件解压放到路径：`/usr/share/themes`，图标文件放到`/usr/share/icons`，如：

```
sudo cp -r Mojave-light-solid /usr/share/themes
sudo cp -r WhiteSur-Light /usr/share/themes
sudo cp -r McMojave-circle /usr/share/icons
sudo cp -r macOSCursor /usr/share/icons

```

下面是我最终的效果

![https://img-blog.csdnimg.cn/3890afda1e284da7b74dd728574b7b62.png#pic_center](https://img-blog.csdnimg.cn/3890afda1e284da7b74dd728574b7b62.png#pic_center)

![https://img-blog.csdnimg.cn/419af70b1632429a8e05451f54549849.png#pic_center](https://img-blog.csdnimg.cn/419af70b1632429a8e05451f54549849.png#pic_center)

![https://img-blog.csdnimg.cn/182bc59a41084380a73a4d37a013c083.png#pic_center](https://img-blog.csdnimg.cn/182bc59a41084380a73a4d37a013c083.png#pic_center) 如果要卸载某个主题，cd进目录直接删除文件夹就行（sudo） 更多自定义内容等待你去探索吧

## 八、自动挂载Windows盘

打开系统挂载文件

```
sudo gedit /etc/fstab

```

查看查看ubuntu的分区情况、复制目标分区的UUID：

```
sudo blkid

```

![https://img-blog.csdnimg.cn/3df720a559054eab9ee82b2e27295ad2.png#pic_center](https://img-blog.csdnimg.cn/3df720a559054eab9ee82b2e27295ad2.png#pic_center)

例如我要挂载windows下的两个盘，名称分别为Data和SLAMData，复制他们两个的UUID，在`/etc/fstab`中添加两句（UUID，挂载位置-zard是我的用户名，挂载磁盘类型：linux分区一般为ext4，windows分区一般为ntfs，挂载参数：一般为defaults`后来没有权限修改文件夹，这里又改成了rw-读写`，以及是否进行开机的磁盘检查）：

```
UUID=74D2389FD238678E /media/zard/Data  ntfs     defaults       0       2
UUID=B0121BFB121BC56E /media/zard/SLAMData  ntfs     defaults       0       2

```

![https://img-blog.csdnimg.cn/ad6c42d7bb2b4424b747e5f92d34da31.png#pic_center](https://img-blog.csdnimg.cn/ad6c42d7bb2b4424b747e5f92d34da31.png#pic_center)

添加完之后重启就会自动挂载这两个盘

## 九、设置录屏时间无限制

```
gsettings set org.gnome.settings-daemon.plugins.media-keys max-screencast-length 0

```

录屏快捷键：

>  
 CTRL+ALT+SHIFT+R #开始录屏 CTRL+ALT+SHIFT+R #结束录屏 


## 十、设置新建文件模板

默认情况下，Ubuntu 右键没有新建文档选项。要在右键添加新建文件，需要使用到 `home` 中的`Templates`（模板）文件夹。该文件夹专门用来存放右键的新建文件模板的。在此文件夾下打開終端，新建文件：

```
touch Text.txt

```

之後右鍵就可以新建文本文檔。 由于常用CMake，我设置了一个`CMakeLists.txt`模板，这样就可以随时新建一个带参考内容的`CMakeLists.txt`

```
cmake_minimum_required(VERSION 3.10)
project(ProjectName VERSION 1.0)

# SET(CMAKE_BUILD_TYPE Release/Debug)
# MESSAGE("-- Build type: " ${CMAKE_BUILD_TYPE})

# set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Werror -std=c++14")
# MESSAGE("-- cmake build mode: " ${CMAKE_C_FLAGS})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Werror -std=c++14")
MESSAGE("-- cmake build mode: " ${CMAKE_CXX_FLAGS})

# MESSAGE([SEND_ERROR | STATUS | FATAL_ERROR] "message to display"...)

# Find package----------------------------------------
# find_package(thirdparty REQUIRED)
# Include directories---------------------------------
# include_directories(
	#{PROJECT_SOURCE_DIR}/include
	#${thirdparty_INCLUDE_DIRS}
#)

# Find sources----------------------------------------
# file(GLOB LIBHELLO_SRC "{PROJECT_SOURCE_DIR}/src/*.cpp")
# file(GLOB SOURCES "{PROJECT_SOURCE_DIR}/Examples/src/*.cpp")

# Add_library-----------------------------------------
# set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/lib)
# add_library(hello SHARED ${LIBHELLO_SRC})
# target_link_libraries(hello ${thirdparty_LIBRARIES})

# add_library(hello_static STATIC ${LIBHELLO_SRC}) 
# target_link_libraries(hello_static ${Pangolin_LIBRARIES})
# set_target_properties(hello_static PROPERTIES OUTPUT_NAME "hello")

# install library-------------------------------------
# install(TARGETS hello hello_static
#	LIBRARY DESTINATION lib
#	ARCHIVE DESTINATION lib)
# install(FILES ../include/hello.h DESTINATION include/hello)

# Add executable--------------------------------------
# set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
# add_executable(CMake ${SOURCES})
# target_link_libraries(CMake ${hello_LIBS})

# Add subdirectory------------------------------------
# add_subdirectory(directory)

```

## 十一、卸载系统软件

系统预装了一些无用或者用处很少的软件（安装系统时选择最小安装就不会预装），执行下面这行命令可以删除它们（游戏为例）：

```
sudo apt-get --purge remove gnome-mahjongg gnome-mines aisleriot gnome-sudoku

```

根据个人习惯自行决定删除軟件：

```
remmina	远程桌面
libreoffice	办公软件
thunderbird	邮件客户端
totem	视频播放
rhythmbox	音乐播放器
*empathy	即时通讯软件
*brasero	光盘刻录软件
simple-scan	文档扫描仪
gnome-mahjongg	对对碰游戏
aisleriot	接龙游戏
gnome-mines	扫雷
cheese	茄子(拍照)
transmission-common	bt下载
*gnome-orca	屏幕阅读器
gnome-sudoku	数独

```

## 十二、系统备份与恢复

Linux秉承一切皆文件的思想，系统备份就相当于把整个/（根目录）所有文件打包压缩保存。备份前先切换到root用户，避免权限问题，然后切换到 /（根目录）

```
sudo su
cd /
tar -cvpzf /media/zard/Elements\ SE/UbuntuBackup/ubuntu_backup@`date +%Y-%m-%d`.tar.gz --exclude=/proc --exclude=/tmp --exclude=/boot --exclude=/home --exclude=/lost+found --exclude=/media --exclude=/mnt --exclude=/run /

```

提示错误：`tar: Exiting with failure status due to previous errors`，忽略即可，其中：
- `/media/zard/Elements\ SE/UbuntuBackup/ubuntu_backup@`date +%Y-%m-%d`.tar.gz`：保存路径，`date +%Y-%m+%d`shell命令用于获取当前时间，注明时间戳- `--exclude=` ： 排除指定目录，不进行备份。如果没有把/home或者/boot目录单独分一个区，一定不要加–exclude=/home或–exclude=/boot参数。- `-z` 用gzip压缩备份文档，减小空间
可单独备份/home和/boot

```
tar -cvpzf /media/zard/Elements\ SE/UbuntuBackup/ubuntu_backup_boot@`date +%Y-%m-%d`.tar.gz /boot
tar -cvpzf /media/zard/Elements\ SE/UbuntuBackup/ubuntu_backup_home@`date +%Y-%m-%d`.tar.gz /home

```

恢复（只写了能进入终端的情况）：

```
sudo su
cd /
rm -fr /* #删除整个文件系统
tar -xvpzf /media/zard/Elements\ SE/UbuntuBackup/ubuntu_backup@2023-04-23.tar.gz -C /
tar -xvpzf /media/zard/Elements\ SE/UbuntuBackup/ubuntu_backup_boot@2023-04-23.tar.gz -C /
tar -xvpzf /media/zard/Elements\ SE/UbuntuBackup/ubuntu_backup_home@2023-04-23.tar.gz -C /
# 还原系统后一定要把之前没有备份的目录手动创建，不然重启系统是有问题的
mkdir proc tmp lost+found media mnt run

```

要想移植到其他系统，要保证Ubuntu版本以及内核一致 查看Ubuntu发行版本：

```
lsb_release -a

```

查看Linux内核以及位数

```
uname -a

```

![https://img-blog.csdnimg.cn/b3420a49ed22421b844568779c5003a2.png#pic_center](https://img-blog.csdnimg.cn/b3420a49ed22421b844568779c5003a2.png#pic_center)

## 十三、清理日志以及无用包

在/var/log/journal/垃圾日志文件占用比较大，可以通过如下命令来清除

```
journalctl --disk-usage        # 检查日志大小
sudo journalctl --vacuum-time=1w    # 只保留一周的日志
sudo journalctl --vacuum-size=500M    # 只保留500MB的日志

```

清理升级缓存以及无用包

```
sudo apt-get autoclean                # 删除旧版本软件缓存
sudo apt-get clean                    # 删除系统内所有软件缓存
sudo apt-get autoremove             # 删除系统不再使用的孤立软件

```

## 十四、apt-get 命令的使用：安装、更新、卸载软件包

（1）安装 软件包

```
apt-get install PackageName // 普通安装
apt-get install PackageName=VersionName // 安装指定包的指定版
apt-get --reinstall install PackageName // 重新安装
apt-get build-dep PackageName // 安装源码包所需要的编译环境
apt-get -f install // 修复依赖关系
apt-get source PackageName // 下载软件包的源码
# 例如安装一些工具：sudo apt-get install g++ gcc gdb make cmake vim

```

（2）卸载 软件包

```
apt-get remove PackageName // 删除软件包, 保留配置文件
apt-get --purge remove PackageName // 删除软件包, 同时删除配置文件
apt-get purge PackageName // 删除软件包, 同时删除配置文件
apt-get autoremove PackageName // 删除软件包, 同时删除为满足依赖而自动安装且不再使用的软件包
apt-get --purge autoremove PackageName // 删除软件包, 删除配置文件,删除不再使用的依赖包
apt-get clean &amp;&amp; apt-get autoclean // 清除 已下载的软件包 和 旧软件包

```

（3）更新 软件包

```
apt-get update // 更新安装源（Source）
apt-get upgrade // 更新已安装的软件包
apt-get dist-upgrade //更新已安装的软件包（识别并处理依赖关系的改变）

```

（4）查询 软件包

```
dpkg -l // 列出已安装的所有软件包
apt-cache search PackageName // 搜索软件包
apt-cache show PackageName // 获取软件包的相关信息, 如说明、大小、版本等
apt-cache depends PackageName // 查看该软件包需要哪些依赖
apt-cache rdepends PackageName // 查看该软件包被哪些包依
apt-get check // 检查是否有损坏的依赖

```

## 十五、find和grep搜索命令

### 15.1 find根据文件名搜索

```
# find 搜索的路径 -name 要搜索的文件名
# find 搜索的路径 -name name.* 或 *.type
find ./Desktop/ORB_SLAM2/Examples/TimeMatch -name *.cpp
find ./Desktop/ORB_SLAM2/Examples/TimeMatch -name main.*

```

### 15.2 grep根据文件内容搜索

```
# grep "搜索的内容" 搜索的路径/文件 参数
grep "include" ./Desktop/ORB_SLAM2/Examples/TimeMatch/main.cpp
# 搜索目录
grep "include" ./Desktop/ORB_SLAM2/Examples/TimeMatch/ -r
# 显示行号
grep "include" ./Desktop/ORB_SLAM2/Examples/TimeMatch/ -nr

```

## 十六、Ubuntu常用命令

```
# Ctrl+Alt+T 打开新的终端
# Ctrl+shift+T 打开新的终端Tab
# Ctrl+shift+n 打开新的同目录的终端

clear # 清屏
clear --help # cmd --help:查看Linux命令的帮助，例如
sudo clear # 以管理员权限运行命令：sudo
history # 查看终端输入的所有历史命令

# 根目录：/，家目录：/home/zrad, ~
# cd ~ 回家，cd 打开文件夹
cd ~
cd Desktop
cd ..  # 返回上一级

pwd # 查看当前路径

# mkdir *** 创建文件夹
mkdir test_sh
cd /home/zard/test_sh
mkdir test test2
# 创建多级文件夹
mkdir -p test2/test3/test4

# 将文本写进tmp文件（覆盖）
echo "Ctrl+Alt+T 打开终端" &gt; tmp
# 将文本写进tmp文件（追加）
echo "Ctrl+shift+T分开终端" &gt;&gt; tmp

cd test
# touch ****.*** 创建文件（如果存在只会更新创建时间）
touch test1.txt
mkdir test

ls  # ls 查看当前目录下所有文件及文件夹
ls -l # ls -l 查看当前目录下所有文件及文件夹并显示详细信息（字节为单位）
ls -a  # ls -a 查看当前目录下所有文件及文件夹(包括隐藏的)
ls -lh # ls -lh 查看当前目录下所有文件及文件夹并显示详细信息(单位kMGT)
# ll==ls -laf
ll
ls -lah
# ls ***:罗列路径下的所有文件及文件夹
ls /home/zard/test_sh

# tree：显示当前文件树结构 sudo apt-get install tree
tree

echo "rm **.**:移除文件"
echo "rm -r ***:移除文件夹"
echo "rm -f *** -r:移除文件夹及其下的所有文件"

cd /home/zard/test_sh/test/
touch test2.txt
echo "mv **.**/*** ***:移动文件夹/文件至***"
mv /home/zard/test_sh/test2 /home/zard/test_sh/test/test
mv /home/zard/test_sh/test/test2.txt /home/zard/test_sh/test/test

echo "cp **.**/*** ***:复制----------------"
cp /home/zard/test_sh/test2 /home/zard/test_sh/test/test -r
cp /home/zard/test_sh/test/test1.txt /home/zard/test_sh/test/test

# 压缩/解压缩文件
mkdir testcom
touch testcom testcom2
cd testcom &amp;&amp; touch testcom testcom2
cd ..
tree
# c代表压缩，z代表使用gzip，v代表显示压缩日志，f代表指定压缩包名称，后面是要压缩的文件夹及文件
tar czvf all.tar.gz testcom testcom2 tmp
rm -f testcom testcom2 tmp -r
# x代表解压缩
tar xzvf all.tar.gz
# 解压缩到目录
mkdir all
tar xzvf all.tar.gz -C all
tree

# zip格式
# 安装压缩工具 sudo apt-get install zip uzip
zip -r all2 testcom testcom2 tmp
unzip all2
mkdir all3
unzip all2 -d all3

```

## 十七、常用软件的安装

### 17.1 安裝与卸载微信

deepin是国产的linux系统，支持qq、微信等众多windows软件。在ubuntu上添加deepin的环境就可以安装和使用qq和微信了(QQ界面有点拉，这里还是不要装了，下面有更好的) （1）添加仓库：

```
wget -O- https://deepin-wine.i-m.dev/setup.sh | sh

```

（2）安装微信

```
sudo apt install com.qq.weixin.deepin

```

（3）卸载微信，如果要卸载dpkg安装的应用，通过`sudo dpkg -l`查看已经安装的软件，并找到自己的安装的软件名。可以通过`grep`进行字符过滤

```
dpkg -l | grep weixin
sudo apt-get remove com.qq.weixin.deepin:i386

```

![https://img-blog.csdnimg.cn/085c400c4d38444cbc05bae090651cfc.png#pic_center](https://img-blog.csdnimg.cn/085c400c4d38444cbc05bae090651cfc.png#pic_center)

`dpkg -l | grep weixin`搜不到就换成`dpkg -l | grep wechat`

删除WeChat 自动生成的记录文档

```
cd Documents 
sudo rm -r WeChat\ Files

```

（4）卸载wine

```
dpkg -l | grep wine
sudo apt remove deepin-wine-helper:i386 deepin-wine6-stable deepin-wine6-stable-amd64 deepin-wine6-stable-i386:i386

```

![https://img-blog.csdnimg.cn/7935618de2424ef9ac0c806afb5fa5bb.png#pic_center](https://img-blog.csdnimg.cn/7935618de2424ef9ac0c806afb5fa5bb.png#pic_center)

### 17.2 安裝与卸载QQ

最近发现官方更新了Linux版QQ，界面相比之前有质的飞跃，推荐安装，直接去官网下载安装包：，然后安装：

```
sudo dpkg -i linuxqq_3.1.1-11223_amd64.deb

```

![https://img-blog.csdnimg.cn/25c62a311fa54ebeb9db405bfe3dcd67.png#pic_center](https://img-blog.csdnimg.cn/25c62a311fa54ebeb9db405bfe3dcd67.png#pic_center)

通过`sudo dpkg -l`查找：

```
sudo dpkg -l | grep qq

```

![https://img-blog.csdnimg.cn/5356706ac25a4d82ad2a9a15262c45de.png#pic_center](https://img-blog.csdnimg.cn/5356706ac25a4d82ad2a9a15262c45de.png#pic_center)

然后卸载：

```
sudo dpkg -r linuxqq

```

### 17.3 安装Chrome浏览器并加入apt更新

```
sudo apt-get install wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install libappindicator1 libindicator7
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get -f install

```

![https://img-blog.csdnimg.cn/f0accb8239544c558c806717aacfcba0.png#pic_center](https://img-blog.csdnimg.cn/f0accb8239544c558c806717aacfcba0.png#pic_center)

### 17.4 安裝VScode

（1）下载安装包 进入VSCode官网 ，下载`Linux x64.deb`版本 ![https://img-blog.csdnimg.cn/2af9928b6e3448118310719c6a6a3a54.png](https://img-blog.csdnimg.cn/2af9928b6e3448118310719c6a6a3a54.png) （2）双击安装包安装： ![https://img-blog.csdnimg.cn/1d48018c8063491ba511f23cc42ee024.png](https://img-blog.csdnimg.cn/1d48018c8063491ba511f23cc42ee024.png)

（3）安装插件

我常用的插件

```
python、 C/C++、 CMake、 ROS、 Chinese、 
GBKtoUTF8、 vscode-icons、 vscode-pdf、 URDF、
Prettier-Code formatter、 vscode-drawio

```

![https://img-blog.csdnimg.cn/80e7e3f2af0941d5ae25f60257a748f7.png](https://img-blog.csdnimg.cn/80e7e3f2af0941d5ae25f60257a748f7.png)

（4）减小Ipch缓存： `Ipch`：这些文件是Visual Studio用来保存预编译版的头文件和Intellisense用的。如果删除后，重新加载项目会重建这些文件，但VSCode中设定范围后就不会产生超过这个数的缓存大小。

```
/home/用户名/.cache/vscode-cpptools/ipch

```

ipch文件内包含缓存的预编译头文件（PCH），vscode使用的时间越长，那么这个文件夹内的缓存就越多，最终会造成较大的内存占用。当我们不用来运行很大的文件时，只是利用它来敲代码，用不到预编译头文件时可以关闭这个功能。 在VSCode菜单栏中 `文件-&gt;首选项-&gt;设置`，然后搜索`C_Cpp.intelliSenseCacheSize`,修改其默认值5120为512

### 17.5 安装代码对比工具Meld

安装：

```
sudo apt-get install meld

```

选择两个文件夹，蓝色会显示代码改动，双击文件会显示具体哪里有改动： ![https://img-blog.csdnimg.cn/9e38c26a41d94141a97d0b71446e5d4d.png#pic_center](https://img-blog.csdnimg.cn/9e38c26a41d94141a97d0b71446e5d4d.png#pic_center)![https://img-blog.csdnimg.cn/aa8f25901e8b4d4185e3797bf4c9f5ce.png#pic_center](https://img-blog.csdnimg.cn/aa8f25901e8b4d4185e3797bf4c9f5ce.png#pic_center)

### 17.6 安裝WPS

（1）打开官网，选择Linux版本（Deb格式For X64）：

![https://img-blog.csdnimg.cn/da950bfa66a344c6a848c4000a0a0a50.png#pic_center](https://img-blog.csdnimg.cn/da950bfa66a344c6a848c4000a0a0a50.png#pic_center)

（2）安装安装包：

```
sudo dpkg -i wps-office_11.1.0.10702_amd64.deb

```

（3）安装完成后会在桌面会自动生成 `wps-office-prometheus.desktop`启动器文件，给`wps-office-prometheus.desktop`文件赋予执行权限：

```
sudo chmod +x wps-office-prometheus.desktop

```

（4）右击桌面`wps-office-prometheus.desktop`文件，点击选择允许运行，生成WPS启动快捷方式图标 （5）安装windows字体：选择windows的C盘文件：`C:/windows/fonts`，复制到linux系统盘中，进入`fonts`文件夹中，打开终端，输入：

```
sudo cp * /usr/share/fonts

```

### 17.7 安装PDF阅读器Foxit Reader

虽然安装了wps，但是Linux的wps无法对PDF进行标注等编辑操作，因此我们安装实用的福昕DPF阅读器 （1）在下载安装文件，点击下载网页会自动获取系统适合的安装包

![https://img-blog.csdnimg.cn/82ed19725d4e4ce198eb489dc5341633.png#pic_center](https://img-blog.csdnimg.cn/82ed19725d4e4ce198eb489dc5341633.png#pic_center)

（2）解压文件后运行安装文件（Tab补自己的，不要手打，不要复制我的），选择安装路径之后一路确认：

```
./FoxitReader.enu.setup.2.4.5.0727\(rb70e8df\).x64.run

```

![https://img-blog.csdnimg.cn/df8891faabf8422d8c3373825205dbe5.png#pic_center](https://img-blog.csdnimg.cn/df8891faabf8422d8c3373825205dbe5.png#pic_center)

（3）安装后如果是英文，在help中切换语言并重启，接下来就可以愉快的使用了

![https://img-blog.csdnimg.cn/745e640d06ab4d3fac76649bf2e6458e.png#pic_center](https://img-blog.csdnimg.cn/745e640d06ab4d3fac76649bf2e6458e.png#pic_center)

（4）**注意**，可能会遇到打开pdf文件之后把系统卡死的情况，尤其是学位论文和书籍这种大的PDF，这时候使用上面的方法重启系统，千万不要强制关机。重启之后，到 `~/opt/foxitsoftware/foxitreader/fxplugins` 目录下删除 libupdater.so：

```
cd  ~/opt/foxitsoftware/foxitreader/fxplugins 
sudo rm libupdater.so

```

删除后就不会再出现卡死的问题了

（5）可以卸载默认PDF阅读器Evince，它对中文支持不太好，界面也令人很不爽

```
sudo apt-get remove evince

```

### 17.8 安裝视频播放器smplayer

ubuntu自带的视频播放器只能播放一种格式，这里安装smplayer，解码比较强，类似于Potplayer

```
sudo add-apt-repository ppa:rvm/smplayer 
sudo apt-get update 
sudo apt-get install smplayer smplayer-themes smplayer-skins

```

常用的快捷键: `space`：暂停播放和开始播放 `]`：加速播放 `[`：减速播放 `-&gt;`：快进 `&lt;-`：快退

### 17.9 安装文献管理软件Zotero

（1）从官网下载安装Zotero官网地址： （2）解压生成了Zotero_linux-x86_64这个文件夹，包含了zotero软件的所有的文件 （3）创建zotero软件安装目录

```
sudo mkdir /opt/zotero

```

（4）复制解压的文件到/opt/zotero目录下

```
sudo mv Zotero_linux-x86_64/* /opt/zotero/

```

（5）更新zotero的桌面位置

```
cd /opt/zotero
sudo ./set_launcher_icon

```

（6）创造软连接到应用程序桌面

```
ln -s /opt/zotero/zotero.desktop ~/.local/share/applications/zotero.desktop

```

（7）接下来就能找到这个软件并使用啦！ ![https://img-blog.csdnimg.cn/27d1f9fd389442509d33961089da6530.png#pic_center](https://img-blog.csdnimg.cn/27d1f9fd389442509d33961089da6530.png#pic_center) （8）安装翻译插件 下载地址：，点右侧release下载`*.xpi`文件，然后打开Zotero中 “`Tools -&gt; Add-ons`”，选择 `Install add-on from file…`，选择`.xpi`插件安装完成。当阅读外文文献时，选中内容自动翻译。支持谷歌、有道、百度、Deepl等： ![https://img-blog.csdnimg.cn/9befe7b034b54e6095cf756d0aa1a3a6.png#pic_center](https://img-blog.csdnimg.cn/9befe7b034b54e6095cf756d0aa1a3a6.png#pic_center) （9）添加新的引用样式（中国标准GB/T 7714-2015） 首先下载，再选择“编辑——首选项”，弹出“Zotero首选项框”，点击+号添加引文格式： ![https://img-blog.csdnimg.cn/2bab77a2c41147abab9d1665ed289e56.png#pic_center](https://img-blog.csdnimg.cn/2bab77a2c41147abab9d1665ed289e56.png#pic_center)

### 17.10 安装有道云笔记

官网然后安装：

```
sudo dpkg -i *.deb

```

![https://img-blog.csdnimg.cn/0cf199fb51b34ede991ee9d70b1989c0.png#pic_center](https://img-blog.csdnimg.cn/0cf199fb51b34ede991ee9d70b1989c0.png#pic_center)

### 17.11 安装远程控制软件ToDesk

进入下载deb文件，然后安装：

```
sudo dpkg -i todesk-v4.3.1.0-amd64.deb

```

![https://img-blog.csdnimg.cn/349bd115e886456eadd15eeee5affa3c.png#pic_center](https://img-blog.csdnimg.cn/349bd115e886456eadd15eeee5affa3c.png#pic_center)

### 17.12 安装画图软件Kolourpaintr和录屏软件Kazam

打开Ubuntu自带的软件商店（software），左上角搜索Kolourpaint： ![https://img-blog.csdnimg.cn/94f765c2c01c4925af98c4b40d65c7fd.png#pic_center](https://img-blog.csdnimg.cn/94f765c2c01c4925af98c4b40d65c7fd.png#pic_center)

注： 如果报错：报错“unable to install typora: status-code=409 kind=snap-change-conflict，参考： 如果软件商店没了，重新安装：

```
sudo apt-get install gnome-software

```

同样地，Kazam： ![https://img-blog.csdnimg.cn/166557e3d3fe474b8333b7f27e6dea70.png#pic_center](https://img-blog.csdnimg.cn/166557e3d3fe474b8333b7f27e6dea70.png#pic_center) 可以设置录屏范围和准备时间（秒），按Capture开始录制 ![https://img-blog.csdnimg.cn/38323e58d45f497b988a3264e51b021f.png#pic_center](https://img-blog.csdnimg.cn/38323e58d45f497b988a3264e51b021f.png#pic_center)

打开左上角file-&gt;preferences设置帧率和输出位置： ![https://img-blog.csdnimg.cn/780a1b379c88481c9c709016916ac28e.png#pic_center](https://img-blog.csdnimg.cn/780a1b379c88481c9c709016916ac28e.png#pic_center)

### 17.13 安装Github桌面版

使用鱼香ROS一键安装

```
wget http://fishros.com/install -O fishros &amp;&amp; . fishros

```

选择2自动安装： ![https://img-blog.csdnimg.cn/1dbc864f42244b71a00012167a26e3a1.png#pic_center](https://img-blog.csdnimg.cn/1dbc864f42244b71a00012167a26e3a1.png#pic_center) ![https://img-blog.csdnimg.cn/a12d181b7be24c2db2b742188252aba9.png#pic_center](https://img-blog.csdnimg.cn/a12d181b7be24c2db2b742188252aba9.png#pic_center)
