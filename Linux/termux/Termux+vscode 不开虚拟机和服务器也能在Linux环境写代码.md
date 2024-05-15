目录
==

*   为啥要这么折腾
*   需要什么
*   先装Termux
*   Termux还能再装Linux
*   配置SSH
*   vscode也能远程写代码

为啥要这么折腾
=======

最近有门课要在Linux环境上面写代码，虽然电脑上装了一个Ubuntu虚拟机，但是每次写代码都要打开虚拟机，很占用电脑资源，而且有时候需要在虚拟机和本机之间切换，很不优雅。  
偶然间发现Termux也能运行Linux某些命令，虽然Termux和真实Linux还是有差距，但是Termux能安装Linux系统，就很nice。vscode可以安装ssh远程连接插件，只要有Linux服务器，就算在Windows上也能编写Linux代码。  
假如在手机上安装Linux，电脑远程连接就能编写代码，就很棒。

需要什么
====

*   安卓手机及Termux
*   一台电脑及vscode
*   需要电脑和手机在同一个网络下（能ping通即可）

先装Termux
========

[官网下载](https://link.juejin.cn?target=https%3A%2F%2Ftermux.com%2F "https://termux.com/")  
[GitHub下载](https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2Ftermux%2Ftermux-app%2Freleases "https://github.com/termux/termux-app/releases")  
使用可以参考[Termux 高级终端安装使用配置教程 - 画入新雪 - 博客园 (cnblogs.com)](https://link.juejin.cn?target=https%3A%2F%2Fwww.cnblogs.com%2Fcutesnow%2Fp%2F11430833.html "https://www.cnblogs.com/cutesnow/p/11430833.html")

Termux还能再装Linux
===============

*   先安装基础件proot-distro

复制代码

 `pkg install proot-distro` 

*   可以查看proot-distro的使用帮助

bash

复制代码

`proot-distro help`

*   查看可安装的Linux系统

复制代码

`proot-distro list`

![Screenshot_2021-10-17-17-17-44-251_com.termux.jpg](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6d6809ae20e4089801c2182acffed78~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

*   选择一个系统进行安装

vbnet

复制代码

 `proot-distro install <Alias>` 

*   我安装的是ubuntu，所以运行

复制代码

 `proot-distro install ubuntu`

*   登录ubuntu

复制代码

`proot-distro login ubuntu`

配置SSH
=====

*   安装ssh服务端

vbscript

复制代码

`apt-get install openssh-server`

*   手机安装的Linux是root用户，而且默认的22号端口不可用，因此需要修改ssh配置

bash

复制代码

`vim /etc/ssh/sshd_config`

*   添加端口9022（其他未被占用的端口也行） ![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27c0474c7fb34793938fb97b28f7cee8~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)
*   允许root用户登录 ![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4be5204da4824fd283e8b8c0c679d168~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)
*   重启ssh服务器

bash

复制代码

`/etc/init.d/ssh restart`

*   查找ssh进程，如下图，ssh已经成功开启

perl

复制代码

`ps -e | grep ssh`

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82ae4f42303a4538bab764dddd96845e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

*   设置root密码

复制代码

`passwd root`

输入两次，修改成功  
![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b285f8ec0e93467f964d5b1a664f3334~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

*   网络配置 电脑和手机需要在同一个局域网中，电脑和手机连接同一个WiFi或者电脑连接手机热点  
    查看手机IP，wlan0即是手机在局域网内的地址，记住这个IP ![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed53a82088e44c32b6b93de47d4d535c~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)
*   使用Xsell尝试登录
    *   配置Xshell连接信息，配置IP和端口号。 ![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0deb0265f39843c082d0dd616c7fe872~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)
    *   配置用户名密码，这个密码即是前面设置的密码 ![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/879b127cc3134cf8b51f821d202b12bf~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)
    *   成功连接 ![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b77fd7eb4fe4ce991f8ea57f5d68b9f~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

vscode也能远程写代码
=============

配置好SSH便可使用VScode远程连接了。

*   安装插件 ![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1405d51ee90c493699fcaf1e880ac33c~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)
*   配置文件 点击左下角图标![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afe4038cb4714a7cbeeea6b7d8408e87~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)，选择Open SSH Configuration file...，选择第一条路径进行配置。其中Host是别名，随便起一个就行，HostName是IP地址，User是用户名（这里是root），Port是端口。 ![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5aea80717bad4be09dd3af9a380e81bb~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)
*   进行连接，点击左下角图标，选择connect to host，选择刚才设置的主机即可。然后会跳出一个新的窗口，输入密码即可。
*   打开文件夹，再次输入密码，新建文件，即可开始写代码。 ![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3dd2959ccf94857953c97454b6ed419~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp?)

本文转自 <https://juejin.cn/post/7019992544444416037>，如有侵权，请联系删除。