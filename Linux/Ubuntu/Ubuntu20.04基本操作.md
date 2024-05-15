#Ubuntu20.04基本操作
## 

## 切换用户

从root切换到普通用户：

```
su 用户名
```

从普通用户切换到root：

```
su root
```



## Ubuntu 20.04 上安装 gcc/g++7.5

默认的 Ubuntu 软件源包含了一个软件包组，名称为 “build-essential”,它包含了 GNU 编辑器集合，GNU 调试器，和其他编译软件所必需的开发库和工具。

以 拥有 sudo 权限用户身份或者 root 身份运行下面的命令：

```
sudo apt update
sudo apt install build-essential
```

这个命令将会安装一系列软件包，包括`gcc`,`g++`,和`make`。

安装如何使用 GNU/Linux开发的手册。

```
sudo apt-get install manpages-dev

```

通过运行下面的命令，打印 GCC 版本，来验证 GCC 编译器是否被成功地安装。

```
gcc --version
```

 默认是9.4.0



## 编译文件小练习

使用vi编辑器

vi是Unix的传统编辑器，现在传承到了Linux下。常听到的vim可以理解为vi的升级版，一般你装了vim，那么你执行vi的时候实际上就是执行了vim。

在终端执行：

```
vi hello-vi-world.c
```

就会进入vi的界面，开始编辑hello-vi-world.c这个文件。

现在还不能编辑，要想进入编辑模式需要按"i"键，按下之后进入插入内容的模式，会看到最下方出现“插入”或"INSERT"的字样。

然后就可以开始编辑了，比如写一个最简单的C程序：

```
#include&lt;stdio.h&gt;
int main(int argc,char*argv[])
{
    printf("welcom my vi world\n");
    return 0;


}
```

现在还内容还没有被写到文件里，如果想要保存则按照如下步骤进行：

1、按Esc键退出编辑模式。

2、输入一个":"冒号键，在左下角出现一个冒号。

3、输入一个"w"键，然后回车。你会看到下方提示已经written，说明保存成功了，这个文件也被自动创建。

如果要退出vi编辑器则把第三步的w换成q回车就退出了。

如果第三步想要保存并且退出，冒号后面写"wq"回车就行了，代表保存然后退出。或者直接写"x"回车也代表保存退出。

Linux下的常用编译器就是gcc系列，C++的是g++。

安装完后我们尝试对上面两个程序分别进行编译，如果要将hello-vi-world.c编译成可执行二进制文件，则执行：

```
gcc -o hello-vi-world hello-vi-world.c -Wall
```

如果没有语法错误就编译好了，我们用ls看一下。

看到一个带"x"权限（可执行权限）的绿色文件（不一定会显示颜色）。下面尝试执行一下试试，执行谁只要在终端上输入要执行的文件的路径名即可，比如输入./hello-vi-world（注意前面一个点），代表执行当前路径下的hello-vi-world文件。

注意这里没有"./"是不行的，点"."代表当前路经，./hello-vi-world代表当前路经下的hello-vi-world文件，如果直接写hello-vi-world，则终端会尝试从默认的一些路经（如/bin, /usr/bin）下查找有没有这个可执行文件，一般情况下找不到当前路经。

<img alt="" src="https://img-blog.csdnimg.cn/aab9286a5c994251b22554fdbd9485b4.png">

 

现在可以自己尝试编译并执行hello-em-world.c

gcc其实有很多很多功能，比如要想预编译hello-em-world.c文件可以执行

```
gcc -E -o hello-em-world.i hello-em-world.c
```

执行成功后就会出现一个hello-em-world.i的文件，可以用less,vi或emacs查看一下它的内容，就是经过预编译后的内容。

如果要进行编译，这里说的编译是纯粹的编译，就是把c代码编译成汇编代码，则可以执行：

```
gcc -S -o hello-em-world.s hello-em-world.i
```

把.i文件写为hello-em-world.c也行，就是跳过手动预编译直接完成预编译和编译两个过程。这时会得到一个hello-em-world.s文件，打开看一下，里面是编译好的使用于当前体系结构的汇编代码。

把汇编代码进行汇编可以执行：

```
gcc -c -o hello-em-world.o hello-em-world.s
```

把.s文件换成.c也行，就是自动完成预编译、编译和汇编三个过程。现在得到一个hello-em-world.o文件，这一个二进制文件，但不是最后的可执行二进制文件，因为它还缺少最后一步连接处理。

最后对.o文件进行连接，我们这里就一个.o文件所以简单，经常是需要有多个.o文件需要连接。连接执行：

```
gcc -o hello-em-world hello-em-world.o
```

如果把最后的.o文件写成.c，那就和最开始我们用hello-vi-world.c编译时示范的那样了。实际上那样是完成了预编译、编译、汇编和连接一连串的过程。

好了，现在执行一个最后的编译结果吧。



<img alt="" height="117" src="https://img-blog.csdnimg.cn/img_convert/2ba32c6211704b73a764136a0046ee59.png" width="798">

gcc可以支持很多平台，刚才示范的是通用PC下的gcc编译，你还可以交叉编译，使用gcc针对ARM或者AVR或者其它平台的版本。这个就自己去研究吧。

想了解更多gcc的只是可以到GNU的网站上去看看其文档。顺带提一下gdb是常用的调式软件，如何使用gdb调式gcc编译出来的程序请自行学习。

 

## ubuntu扫描本地IP

```
ifconfig
```



## ubuntu使用ssh登录

```
sudo apt install openssh-server
```

在电脑端使用ssh命令登录:

最好用的是：

```
ssh oem@sumengxian.local #用户名+主机名.local
```

最后：

```
 ssh oem@192.168.123.115 #用户名+地址
```

