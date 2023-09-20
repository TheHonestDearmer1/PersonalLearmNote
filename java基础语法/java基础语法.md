# java开发环境的搭建

[![万维广告联盟](https://cdn.wwads.cn/images/placeholder/130x100.png)](https://wwads.cn/)

[万维广告是一个高品质的垂直广告网络联盟，一键购买此流量资源的广告位](https://wwads.cn/)[![img]()广告](https://wwads.cn/?utm_source=property-0&utm_medium=footer)



## [#](https://gaoziman.gitee.io/blogs/pages/882008/#前言)前言

> Java以前自学过一写，现在工作了，时间太久有一些知识都遗忘了，今天开始就更新Java了，想着把之前的Java基础知识捡起来；从最基础的开始，打好Java基础，便于以后复习。也欢迎大家跟我一起复习。

**话不多说，先看一张图**

![JavaSE](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301544817.png)

## [#](https://gaoziman.gitee.io/blogs/pages/882008/#计算机概述-了解)计算机概述（了解）

计算机是一种现代化的电子设备，它能够接受、存储、处理和输出数据。计算机由**硬件**和**软件**两部分组成，硬件包括**中央处理器（CPU）、内存、硬盘、显示器、键盘、鼠标**等部件，软件则包括**系统软件**和**应用软件**。计算机可以进行各种操作，如文字处理、图形设计、音视频播放、游戏等，并且可以通过网络连接进行通信和数据交换。计算机技术的发展对人类社会的影响非常深远，它已经成为现代化社会中不可或缺的一部分。

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#硬件)硬件

硬件是计算机系统的物理部分，主要包括以下组件：

1. 中央处理器（CPU）：负责处理计算机的指令和数据，是计算机的核心部件。 （比如：1+2=3，1,2,3数据存储在内存中，3这个结果是CPU算出来的。）

![image.png](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292233902.png)

1. 内存：用于存储计算机正在运行的程序和数据，是计算机的临时存储器。

![image.png](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292233528.png)

1. 硬盘：用于存储计算机的操作系统、程序和数据，是计算机的永久存储器。

![image.png](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292233971.png)

1. 显示器：用于显示计算机处理的图像和文字。
2. 键盘和鼠标：用于输入指令和数据。
3. 主板：连接计算机各个硬件组件的中心部件。

![image.png](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292233310.png)

1. 电源：提供电能给计算机各个部件。

还有其他硬件组件，如声卡、网卡、显卡、光驱、散热器等。这些硬件组件共同工作，使计算机能够完成各种任务。

计算机性能主要由以下几个部件决定：

1. 中央处理器（CPU）：CPU 是计算机的核心部件，它决定着计算机的计算能力。CPU 的主要指标包括频率、核心数、缓存大小等。它负责执行计算机的指令和处理数据。CPU 从内存中读取指令和数据，并通过其内部的逻辑电路进行计算和处理，最终将结果再存储回内存。
2. 内存：内存是计算机的临时存储器，越大的内存能够存储更多的程序和数据，从而提高计算机的运行速度。
3. 硬盘：硬盘是计算机的永久存储器，它能够存储大量的数据和程序。硬盘的读写速度和容量大小都会影响计算机的性能。
4. 显卡：显卡是计算机的图形处理器，它能够加速计算机的图形处理和显示速度。
5. 主板：主板是计算机各个硬件组件的中心部件，它能够影响计算机的稳定性和性能。
6. 散热器：散热器是计算机的散热部件，它能够保证计算机在高负载运行时不会过热而导致性能下降或者损坏。

这些部件共同工作，决定着计算机的性能和稳定性。

## [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1-1-计算机语言概述)1.1 计算机语言概述

```
Java是一种计算机编程语言。
```

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1、计算机语言是什么)1、计算机语言是什么

所谓计算机编程语言，就是人们可以使用编程语言对计算机下达命令，让计算机完成人们需要的功能。

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_2、计算机语言发展)2、计算机语言发展

- 第一代：机器语言
  - 1946年2月14日，世界上第一台计算机ENAC诞生，使用的是最原始的穿孔卡片。这种卡片上使用的语言是只有专家才能理解的语言，它是用二进制代码表示的语言，与人类语言差别极大，这种语言就称为机器语言。机器语言是第一代计算机语言。这种语言本质上是计算机能识别的唯一语言，人类很难理解。以后的语言就是在这个的基础上简化而来。虽然后来发展的语言能让人类直接理解但最终送入计算机的还是这种机器语言。
- 第二代：汇编语言
  - 计算机语言发展到第二代，出现了汇编语言。汇编语言用助记符代替了操作码，用地址符号或标号代替地址码。这样就用符号代替了机器语言的二进制码。汇编语言也称为符号语言。汇编语言是面向机器的，能直接与存储器、接口电路打交道，也能申请中断，因此汇编语言程序能直接管理和控制硬件设备。程序设计人员必须对计算机有相当深入的了解，才能使用汇编语言编制程序。汇编语言缺乏通用性，程序不易移植。不同计算机的汇编语言之间是不能通用的，因为它们各自都有适合于自己机型特点的汇编语言。但是，掌握了一种计算机的汇编语言，有助于学习其他计算机的汇编语言。比起机器语言，汇编大大进步了。尽管还是复杂，用起来容易出错，但在计算机语言发展史上是机器语言向更高级的语言进化的桥梁。
- 第三代：高级语言
  - 当计算机语言发展到第三代时，就进入了“面向人类”的高级语言。高级语言是一种接近于人们使用习惯的程序设计语言。它允许用英文写计算程序，程序中的符号和算式也与日常用的数学式子差不多。高级语言发展于20世纪50年代中叶到70年代，流行的高级语言已经开始固化在计算机内存里了，比如 Basic语言。现在，计算机语言仍然在不断的发展，种类也相当多，比如 FORTRAN语言， COBOL语言，C语言，C++，C#， PASCAL，Java，Python等等。高级语言接近于自然语言和数学语言，容易为人们掌握；独立于机器，有一定的通用性；计算机不能直接识别和执行用高级语言编写的程序，需要使用编译器或者解释器，转换为机器语言才能被识别和执行；用高级语言编写的程序大大提高了编写效率。

![image-20211218092630678](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292139600.png)

![image-20211218092541075](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292139618.png)

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_3、计算机语言分类)3、计算机语言分类

![image-20211218091234964](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292139609.png)

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_4、计算机语言排行榜)4、计算机语言排行榜

TIOBE排行榜是根据互联网上有经验的程序员、课程和第三方厂商的数量，并使用搜索引擎（如Google、Bing、Yahoo!）以及Wikipedia、Amazon、YouTube和Baidu等统计出的排名数据。

![image-20211216101948388](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292139622.png)

```
计算机语言走势
```

![image-20211218142330176](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292139634.png)

## [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1-2-java语言概述)1.2 Java语言概述

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1、java语言发展历史)1、Java语言发展历史

Java诞生于SUN（Stanford University Network），09年SUN被Oracle（甲骨文）收购。

Java之父是詹姆斯.高斯林(James Gosling)。

![image-20210727085728848](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292142628.png)

1996年发布JDK1.0版。

目前最新的版本是Java17。我们学习的Java8。

将Java取名的是Sun公司的马克 奥颇门（Mark Opperman）。马克 奥颇门是在一家咖啡店与同事品尝咖啡时得到灵感的。Java是印度尼西亚爪哇岛的英文名称，因盛产咖啡而闻名。国外的许多咖啡店用Java来命名或宣传，以彰显其咖啡的品质。Java语言中的许多库类名称，多与咖啡有关，如JavaBeans（咖啡豆）、NetBeans（网络豆）以及ObjectBeans （对象豆）等等。Java使Sun市值大升，一度超过2千亿美元。所有的网络巨头公司为之一振，IBM、HP、微软为Java配置了专门的开发团队，全球几百万软件工程师眷顾于Java，着迷于Java。1982年 Sun公司成立。1986年 Sun公司上市。1995年 Sun公司推出著名的Java编程语言。Sun公司的位置非常像微机争霸战中的苹果公司。它有自己成套的硬件和操作系统，但是它缺乏应用软件。2001年 “9.11”以前，Sun公司市值超过1000亿美元；此后，互联网泡沫破裂，硬件需求大幅减少，它的市值在一个月之内跌幅超过90%。SUN公司的成长用了20年，而衰落只用了1年！

|   发行版本    |  发行时间  |                             备注                             |
| :-----------: | :--------: | :----------------------------------------------------------: |
|     Java      | 1995.05.23 |     Sun公司在Sun world会议上正式发布Java和HotJava浏览器      |
|   Java 1.0    | 1996.01.23 |             Sun公司发布了Java的第一个开发工具包              |
|   Java 1.1    | 1997.02.19 |                                                              |
|   Java 1.2    | 1998.12.08 |    拆分成：J2SE（标准版）、J2EE（企业版）、J2ME（小型版）    |
|   Java 1.3    | 2000.05.08 |                                                              |
|    Java1.4    | 2004.02.06 |                                                              |
| **Java 5.0**  | 2004.09.30 | ①版本号从1.4直接更新至5.0；②平台更名为JavaSE、JavaEE、JavaME |
|   Java 6.0    | 2006.12.11 |               2009.04.20 Oracle宣布收购SUN公司               |
|   Java 7.0    | 2011.07.02 |                                                              |
| **Java 8.0**  | 2014.03.18 |                                                              |
|   Java 9.0    | 2017.09.22 |    ①每半年更新一次；②Java 9.0开始不再支持windows 32位系统    |
|   Java 10.0   | 2018.03.21 |                                                              |
| **Java 11.0** | 2018.09.25 |           JDK安装包取消独立JRE安装包，长期支持版本           |
|   Java 12.0   | 2019.03.19 |                                                              |
|   Java 13.0   | 2019.9.18  |                                                              |
|   Java 14.0   | 2020.3.17  |                                                              |
|   Java 15.0   |   2020.9   |                                                              |
|   Java16.0    |   2021.3   |                                                              |
| **Java17.0**  |   2021.9   |                      最新的长期支持版本                      |

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_2、java是最好的语言吗)2、Java是最好的语言吗？

![image-20211217093810302](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292142620.png)

不是，因为在每个领域都有更合适的编程语言。

- C 语言无疑是现代计算机软件编程语言的王者，几乎所有的操作系统都是 C 语言写成的。C语言是面向过程的编程语言。
- C++ 是面向对象的 C 语言，一直在不断的改进。为了与C兼容，C++被迫做出了很多重大的设计妥协，结果导致语言过分华丽，过分复杂。为了与C兼容，C++并没有采用自动内存管理的策略，从而丧失了修正C最严重问题的机会。另外C++的OO设计耦合度过高，导致组件之间出现很厚的粘合层，并且带来了严重的可维护性问题。C++的应用主要集中在GUI（图形化界面）、游戏和多媒体工具包方面，其他地方很少用到。
- C#是.NET开发平台的主语言。.NET开发平台包括虚拟机CLR、公共类库以及编译工具等开发环境，它是Java语言强有力的竞争对手。但是.NET环境只有Windows有。
- Visual Basic主要用于图形化界面程序的设计，目前也是基于.NET平台。
- JavaScript 是能运行在浏览器中的语言，丰富的前端界面离不开 Javascript 的功劳。近年来的 Node.js 又在后端占有一席之地。
- Python 用于系统管理，并通过高性能预编译的库，提供 API 来进行科学计算，文本处理等，是 Linux 必选的解释性语言。Python的应用方向主要是数据分析、人工智能和机器学习、网络爬虫、自动化测试、web开发、科学计算和统计等。Python的优势是语法简洁清晰，也具有丰富和强大的类库。但是Python更像是胶水语言，它通常用于将其他语言（尤其是C/C++）制作的各种模块轻松的联结在一起。而且Python的运行效率非常低。
- PHP是一种通用开源脚本语言。PHP是在服务器端执行的脚本语言。PHP独特的语法混合了C、Java、Perl以及 PHP 自创的语法。利于学习，使用广泛，主要适用于Web开发领域。LAMP（Linux+Apache+MySQL+PHP）免费套装让很多创业公司可以实现快速低成本的搭建公司网站。虽然 PHP语言使用简单，但是一直有安全漏洞问题要解决。多线程支持不好，性能低下，代码不规范等问题。行业领跑者们从着眼未来考虑，在大数据、物联网、人工智能等方面的广泛应用前景下，对待PHP的重视程度就逐渐下降了。
- Ruby 强于 DSL（领域特定语言），程序员可以定义丰富的语义来充分表达自己的思想。
- Erlang 就是为分布式计算设计的，能保证在大规模并发访问的情况下，保持强壮和稳定性。
- Go 语言内置了并发能力，可以编译成本地代码。当前新的网络相关项目，很大比例是由 Go 语言编写的，如 Docker、Kubernetes 等。
- 函数式编程有 Lisp，编写 iOS 程序有 Swift/Objective-C。
- R的思想是：它可以提供一些集成的统计工具，但更大量的是它提供各种数学计算、统计计算的函数，从而使使用者能灵活机动的进行数据分析，甚至创造出符合需要的新的统计计算方法
- SQL 是用于访问和处理关系型数据库的标准语言， 这类数据库包括：MySQL，Oracle, SQL Server, DB2, PostgreSQL，Sybase, Access 等等

一句话概括，**能留在排行榜之上的语言，都是好的语言，在其所在的领域能做到最好。**

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_3、java语言的特点)3、Java语言的特点

（1）**优点**

- 简单性
  - 在Java语言当中真正操作内存的是：JVM（Java虚拟机）；所有的java程序都是运行在Java虚拟机当中的；而Java虚拟机执行过程中再去操作内存。
  - 对于C或者C++来说程序员都是可以直接通过指针操作内存的。C或者C++更灵活，可以直接程序员操作内存。
  - Java语言屏蔽了指针概念，程序员不能直接操作指针，或者说程序员不能直接操作内存。
  - Java语言底层是C++，所以JVM是用C++语言写好的一个虚拟的电脑。
  - 

- **面向对象：**Java语言支持封装、继承、多态，面向对象编程，让程序更好达到`高内聚`，`低耦合`的标准。
- **支持分布式：**Java语言支持Internet应用的开发，在基本的Java应用编程接口中有一个网络应用编程接口（java net），它提供了用于网络应用编程的类库，包括URL、URLConnection、Socket、ServerSocket等。Java的RMI（远程方法激活）机制也是开发分布式应用的重要手段。
- **健壮型：**Java的强类型机制、异常处理、垃圾的自动收集等是Java程序健壮性的重要保证。对指针的丢弃是Java的明智选择。
  - 主要是因为Java中有一种机制：**自动垃圾回收机制（GC机制）**
  - Java语言是健壮的，相对于C语言来说。
  - Java不容易导致内存的泄漏；C++或者C语言使用不当时很容易导致内存泄漏。JVM负责调度GC机制，程序员不需要干涉。
- **安全性高：**Java通常被用在网络环境中，为此，Java提供了一个安全机制以防恶意代码的攻击。如：安全防范机制（类ClassLoader），如分配不同的名字空间以防替代本地的同名类、字节代码检查。
- **跨平台性：**Java程序（后缀为java的文件）在Java平台上被编译为体系结构中立的字节码格式（后缀为class的文件），然后可以在实现这个Java平台的任何系统中运行。
  - Java语言只要编写/编译一次，可以做到到处运行。 一次编写，到处运行（平台改变了，程序不需要改）
  - 同一份程序通过java虚拟机(JVM)就可以和不同的操作系统进行交互
  - JVM相当于屏蔽了操作系统之间的差距；JVM是在安装JDK的时候自带JVM，所以JDK也有不同版本：windows版的JDK，Linux版本的JDK

（2）**缺点**

- 语法过于复杂，严谨，对程序员的约束比较多，与python和php等相比入门相对较难。但是一旦学会了，就业岗位需求量大，而且薪资待遇节节攀升。
- 一般适用于大型网站开发，整个架构会比较重，对于初创公司开发和维护人员的成本比较高（即薪资高），选择用Java语言开发网站或应用系统的需要一定的经济实力。

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_4、java生态圈)4、Java生态圈

根据2020年IDC（Internet Data Center互联网数据中心）的最新报告《Java迎来25岁》，超过900万的开发人员代表全球69%的全职开发人员使用Java——比其他任何语言都多。

**Java是目前应用最为广泛的软件开发平台之一。**随着Java以及Java社区的不断壮大，Java 也早已不再是简简单单的一门计算机语言了，它更是一个平台、一种文化、一个社区。

**作为一个平台，**Java虚拟机扮演着举足轻重的作用。除了 Java语言，任何一种能够被编译成字节码的计算机语言都属于Java这个平台。Groovy、Scala、 JRuby、Kotlin等都是Java平台的一部分，它们依赖于Java虚拟机，同时，Java平台也因为它们变得更加丰富多彩。

**作为一种文化，**Java几乎成为了 “开源”的代名词。在Java程序中，有着数不清的开源软件和框架。如Tomcat、Struts, Hibernate, Spring,MyBatis等。就连JDK和JVM自身也有不少开源的实现，如OpenJDK、Apache Harmony。可以说，“共享”的精神在Java世界里体现得淋漓尽致。

**作为一个社区，**Java拥有全世界最多的技术拥护者和开源社区支持，有数不清的论坛和资料。从桌面应用软件、嵌入式开发到企业级应用、后台服务器、中间件，都可以看到Java的身影。其应用形式之复杂、参与人数之众多也令人咋舌。可以说，Java社区已经俨然成为了一个良好而庞大的生态系统。**其实这才是Java最大的优势和财富。**

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_5、java技术体系平台)5、Java技术体系平台

- JavaSE（Java Platform, Standard Edition标准版）：允许您在桌面和服务器上开发和部署Java应用程序。Java提供了丰富的用户界面、性能、多功能性、可移植性和当今应用程序所需的安全性。
- JavaEE（Java Platform, Enterprise Edition企业版）：是为开发企业环境下的应用程序提供的一套解决方案，主要针对于Web应用程序开发。
- JavaME（Java Platform, Micro Edition 小型版）：为互联网上的嵌入式和移动设备上运行的应用提供了一个健壮、灵活的环境：微控制器、传感器、网关、移动电话、个人数字助理（PDA）、电视机顶盒、打印机等等。JavaME包括灵活的用户界面、健壮的安全性、内置的网络协议，以及支持动态下载的网络和离线应用程序。基于JavaME的应用程序在许多设备上都是可移植的，但是利用了每个设备的本机功能。
  - Java Embedded: 用于解锁物联网的智能设备的价值： 通过远程市场更新和刷新功能延长产品生命周期和价值； 利用Java的可伸缩性、健壮性、可移植性和全套功能，提高生产效率，降低成本，缩短上市时间； 在边缘启用快速数据功能；
  - Java Card：使安全元件（如智能卡和其他防篡改安全芯片）能够承载采用Java技术的应用程序。Java card提供了一个安全的、可互操作的执行平台，它可以在一个资源受限的设备上存储和更新多个应用程序，同时保持最高的认证级别和与标准的兼容性。
  - Java TV：是一种基于JavaME的技术，它为开发在tv和机顶盒设备上运行的java应用程序提供了一个性能良好、安全且易于实现的解决方案。使用Java TV运行时，开发人员可以轻松创建应用程序，例如电子节目指南（EPG）、视频点播（VOD）客户端、游戏和教育应用程序、用于访问Internet数据的应用程序（例如天气、新闻播报器、社交网络）以及大多数蓝光光盘标题上的用户界面和奖金内容。

![image-20211217114313652](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292142639.png)

![image-20230529214333941](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292143997.png)

## [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1-3-java语言跨平台原理-理解)1.3 Java语言跨平台原理（理解）

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1、java语言跨平台原理)1、Java语言跨平台原理

很多时候，我们写的程序可能要在多个操作系统运行，这个时候就要求我们的程序需要在尽可能不改动的情况下完实现这个目标。不同的语言实现跨平台的方式不同。Java语言实现跨平台是建立在“虚拟机”基础之上的。

在Java出现之前，最为流行的编程语言是C和C++。如果我们想要在一台使用x86_64指令集的CPU的机器（如个人PC）上运行一个C语言程序，就需要编写一个将C语言翻译成x86_64汇编语言的编译器。如果想要在一台使用arm指令集的CPU的机器（如苹果手机）上，运行一个C语言程序，同样需要编写一个将C语言翻译成arm汇编语言的编译器。这样严重影响了C程序的跨平台性，因为针对特定的指令集开发编译器是一个难度非常大的工作。

![image-20210625083023734](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292144771.png)

那么Java是如何解决这个问题的呢？Java设计了一套简洁的虚拟指令集，也就是字节码。如果我们想要在一台机器上运行Java程序，只需要将Java程序编译成字节码就可以了。编写一个将Java程序翻译成Java字节码的编译器，比起编写一个将Java程序翻译成x86_64指令集的编译器来说，要简单得多。可是这里产生了一个问题，难道我们的机器可以直接执行字节码这样的虚拟指令集吗？当然是不能的。我们需要针对不同的指令集，开发对应的字节码解释器。这个工作同样比较简单。

![image-20210625083051577](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292144785.png)

Java虚拟机（JVM，Java Virtual Machine）是由软件技术模拟出计算机运行的一个虚拟的计算机，它负责解释执行字节码指令集。也就是说，只要一台机器可以运行Java的虚拟机，那么就能运行Java语言编写的程序。而不同的平台，需要安装不同的Java虚拟机程序。那么我们编写完Java程序之后，需要先将.java的源文件编译为.class的字节码文件，然后在Java虚拟机中来执行这些字节码文件。

![image-20210625083140531](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292144782.png)

Java虚拟机的设计不仅仅解决了Java程序跨平台的问题，同时解决了很多语言的跨平台问题。

![image-20210625083156633](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292144792.png)

- .NET（C#，VB等语言）也有虚拟机，也能实现跨平台，但是只能在Windows操作系统下安装.NET环境。
- C++不受虚拟机的限制，但是需要用不同平台的编译器重新编译一次。需要编写n个版本的编译器。
- Java虚拟机可以配置在MacOS，Windows（PC操作系统）,Linux等上，但是不能配置在WP（Windows Phone），IOS（移动操作系统）上，只能配置在android（移动操作系统）。Java程序可以实现一次编译处处运行。

![image-20211217111217831](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292144798.png)

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_2、jvm、jre、jdk的关系)2、JVM、JRE、JDK的关系

- **JVM**（Java Virtual Machine ）：Java虚拟机，是运行所有Java程序的假想计算机，是Java程序的运行环境之一，也是Java 最具吸引力的特性之一。我们编写的Java代码，都运行在**JVM** 之上。
- **JRE ** (Java Runtime Environment) ：是Java程序的运行时环境，包含`JVM` 和运行时所需要的`核心类库`。
- **JDK** (Java Development's Kit)：是Java程序开发工具包，包含`JRE` 和开发人员使用的工具。

我们想要运行一个已有的Java程序，那么只需安装`JRE` 即可。

我们想要开发一个全新的Java程序，那么必须安装`JDK` ，其内部包含`JRE`。

![img](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292144805.jpg)

![1561383524152](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292144143.png)

## [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1-4-常用dos命令总结)1.4 常用dos命令总结

> 对于dos命令，它不像Linux命令那样被我们频繁的使用，这就造成我们很容易遗忘；其实很多的dos命令和Linux命令是相通的；今天就先带大家重拾常用的dos命令；面对零基础的同学进行详解！

> 1、怎么打开DOS命令窗口 ⭐️win键 + r （组合键）：可以打开“运行”窗口 ⭐️在运行窗口文本框中输入: cmd，然后回车
>
> 2、什么是DOS命令呢？ ⭐️在DOS命令窗口中才可以输入并执行DOS命令。 ⭐️在最初的windows计算机中没有图形界面的，只有DOS命令窗口。也就是说通过执行DOS命令窗口可以完全完成文件的新建、编辑、保存、删除等一系列操作。
>
> 3、默认情况下DOS命令窗口打开之后，定位的位置是哪里？ ⭐️C:\Users\shark-gao>这是我电脑默认的当前路径
>
> 4、切换盘符？ ⭐️直接输入盘符就行： c: 回车 d: 回车 ⭐️当切换到D盘根下了，那么当前路径就是：D:>，当前路径是当前所在的位置。
>
> 5、mkdir(md) abc（创建文件夹）创建一个目录，起名abc；和Linux是一样的
>
> 6、创建文本文件：echo 123 > 111.txt；就可以把123内容追加到111.txt中，并会创建这个文本文件；Linux特有echo追加内容的功能
>
> 7、删除目录：用rmdir(rd)，例如rmdir abc就会删除abc目录
>
> ```
>   ⭐️对于rmdir建议大家记全称，不然容易和Linux的删除目录rmdir(rm)搞混
> ```
>
> 8、del命令，删除一个或者多个文本文件 ⭐️删除test.c文件：del test.c ⭐️删除所有.c结尾的文本文件，支持模糊匹配:del *.c
>
> 9、dir 查看当前目录下的文件和目录 ⭐️比如：dir/b > list.xls就可以把当前目录下的文件名字追加到excel表格当中10、切换目录？（非常重要，必须掌握） ⭐️使用cd命令来完成目录的切换：cd是什么含义？change directory（改变目录） ⭐️cd命令怎么用，语法格式是什么？ cd 路径 ⭐️路径在windows系统上包括：相对路径和绝对路径。 ⭐️什么是相对路径呢？ 一定要注意，从路径形式上来看，相对路径是一定不会以盘符开始的。 相对路径：相对路径一定是相对于当前所在“位置”而言的。 相对路径是相对于当前而言，从当前所在的位置作为起点。 死记：相对路径一定是从当前位置作为起点开始找。 ⭐️什么是绝对路径呢？ 在windows操作系统中凡是路径起点是盘符的都是绝对路径， 例如：C:\Users\shark-gao> ⭐️注意： cd .. 回到上级路径。 cd \ 直接回到根路径。 . 一个点，代表当前路径。
>
> 11、cls 清屏
>
> 12、exit 退出DOS命令窗口。
>
> 13、怎么查看本机的IP地址？ ⭐️什么是IP地址？有什么用呢？ ⭐️A计算机在网络当中要想定位到（连接到）B计算机，那么必须要先知道B计算机的IP地址，IP地址也可以看做计算机在同一个网络当中的身份证号（唯一标识）。IP地址就相当于电话号码是一个意思。 ⭐️ipconfig（ip地址的配置信息）注意Linux下的是ifconfig。 ⭐️ipconfig /all 该命令后面添加一个/all参数可以查看更详细的网络信息 这个详细信息中包括网卡 的物理地址(Mac地址)，例如：70-8B-CD-A7-BA-25
>
> 14、怎么查看两台计算机是否可以正常通信？ ping命令 ⭐️语法格式：ping IP地址或者ping 域名 ⭐️例如：ping 61.135.169.121或者ping www.baidu.com，一般默认ping四次终止。 Linux不加参数会一直ping下去，ctrl+c终止。
> ⭐️在一个DOS命令窗口中如果有一个命令一直在执行，想强行终止怎么办？ ⭐️例如：ping www.baidu.com -t，加上-t参数，就会一直ping下去，一直ping的目的可以查看网络是否稳定。 http://www.baidu.com 可以打开百度（这种方式比较方便，域名更容易记忆） http://61.135.169.121 也可以打开百度 域名底层最终还是会被解析成IP地址的形式。还是ctrl+c终止！

## [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1-5-开发环境搭建-掌握)1.5 开发环境搭建（掌握）

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1、jdk的下载)1、JDK的下载

- 下载网址：www.oracle.com

- 下载步骤：

  - 登录Oracle公司官网，www.oracle.com，如图所示：在底部选择Developers开发者

    ![1572254490435](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292151028.png)

  - 在**Developers**页面中间的技术分类部分，选择`Java`，单击进入，如图所示：

    ![image-20211019110551338](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292151034.png)

    展示的是最新Java版本，例如Java17。单击Download Java，然后选择具体的版本下载。

    ![image-20211019110843394](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292151038.png)

  - 选择Download Java按钮后

![image-20211019111110242](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292151042.png)

![image-20211019111150970](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292151048.png)

![image-20211019111209831](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292151061.png)

选择**Accept License Agreement**，

![image-20211019111252989](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292151570.png)

注册或登录后下载

![image-20211019111922387](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292151589.png)

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_2、jdk的安装)2、JDK的安装

- 安装步骤：

  - 双击`jdk-8u202-windows-x64.exe`文件，并单击`下一步`，如图所示：

    ![img](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292151620.jpg)

  - 取消独立JRE的安装，单击`公共JRE前的下拉列表`，选择`此功能将不可用`如图所示：

    ![img](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292151642.jpg)

  - 修改安装路径，单击更改，如图所示：

    ![img](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292151666.jpg)

  - 将安装路径修改为`D:\develop\Java\jdk1.8.0_202\`，并单击确定，如图所示：

    ![img](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292151691.jpg)

  - 单击下一步，如图所示：

    ![img](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292151069.jpg)

  - 稍后几秒，安装完成，如图所示：

    ![img](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292151086.jpg)

  - 目录结构，如图所示：

    ![image-20230529215458318](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292154381.png)

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_3、配置环境变量)3、配置环境变量

为什么配置path？

希望在命令行使用javac.exe等工具时，任意目录下都可以找到这个工具所在的目录。

例如：我们在C:\Users\shark-gao目录下使用java命令，结果如下：

![image-20230529215711755](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292157800.png)

我们在JDK的安装目录的bin目录下使用java命令，结果如下：

![image-20230529215736225](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292157283.png)

我们不可能每次使用 `java.exe`，`javac.exe`等工具的时候都进入到`JDK`的安装目录下，太麻烦了。我们希望在任意目录下都可以使用JDK的bin目录的开发工具，因此我们需要告诉操作系统去哪里找这些开发工具，这就需要配置path环境变量。

#### [#](https://gaoziman.gitee.io/blogs/pages/882008/#方案-配置环境变量)方案：配置环境变量

- 步骤：

  - 找到桌面上的此电脑(笔者是Win11系统)，单击鼠标`右键`，选择`属性`，如图所示：

    ![image-20230529220005798](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292200915.png)

  - 在`高级`选项卡，单击`环境变量`，如图所示：

    ![image-20230529220134604](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292201656.png)

  - 点击新建 `JAVA_HOME`这个环境变量

    ![image-20230529220239527](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292202577.png)

  - 在`系统变量`中，选中`Path` 环境变量，`双击`或者`点击编辑` ,如图所示：

    ![image-20230529220356289](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292203342.png)

  - 首先点击新建一个，输入 `%JAVA_HOME%\bin`，将变量引入全局

    ![image-20230529220437327](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292204382.png)

  - 环境变量配置完成，**重新开启**DOS命令行，在任意目录下输入`javac` 命令，运行成功。

    ![image-20230529220631237](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292206320.png)

## [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1-6-入门程序helloworld-掌握)1.6 入门程序HelloWorld（掌握）

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1-6-1-helloworld案例)1.6.1 HelloWorld案例

#### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1、程序开发步骤说明)1、程序开发步骤说明

JDK安装完毕，可以开发我们第一个Java程序了。

Java程序开发三步骤：**编写**、**编译**、**运行**。

![开发步骤](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292213143.jpg)

#### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_2、编写java源程序保存-java源文件)2、编写Java源程序保存.java源文件

1. 在`E:\exer_code\Java2023\chapter01_JavaGrammar\src\main\java` 目录下新建文本文件，完整的文件名修改为`HelloWorld.java`，其中文件名为`HelloWorld`，后缀名必须为`.java`。
2. 用记事本等文本编辑器打开（笔者这里使用记事本是为了让大家熟悉一个Java程序从编译到运行的过程，后面会使用IDEA进行开发）
3. 在文件中输入如下代码，并且`保存`：

```java
public class HelloWorld {
  	public static void main(String[] args) {
    	System.out.println("Hello world!");
  	}
}
```

> 友情提示：
>
> 每个字母和符号必须与示例代码一模一样。

第一个`HelloWord` 源程序就编写完成了，但是这个文件是程序员编写的，JVM是看不懂的，也就不能运行，因此我们必须将编写好的`Java源文件` 编译成JVM可以看懂的`字节码文件` ，也就是`.class`文件。

#### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_3、编译java源文件生成-class字节码文件)3、编译Java源文件生成.class字节码文件

在DOS命令行中，**进入**`E:\exer_code\Java2023\chapter01_JavaGrammar\src\main\java`**目录**，使用`javac` 命令进行编译。

方式一：使用文件资源管理器打开`E:\exer_code\Java2023\chapter01_JavaGrammar\src\main\java`**目录**，然后在地址栏输入cmd。

![image-20230529221802557](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292218623.png)

命令：

```java
javac Java源文件名.后缀名
```

举例：

```java
javac HelloWorld.java
```

![image-20230529221919778](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292219852.png)

编译成功后，命令行没有任何提示。打开`E:\exer_code\Java2023\chapter01_JavaGrammar`目录，发现产生了一个新的文件 `HelloWorld.class`，该文件就是编译后的文件，是Java的可运行文件，称为**字节码文件**，有了字节码文件，就可以运行程序了。

> Java源文件的编译工具`javac.exe`

#### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_4、运行java程序)4、运行Java程序

在DOS命令行中，在字节码文件目录下，使用`java` 命令进行运行。

命令：

```java
java 主类名字
```

主类是指包含main方法的类，main方法是Java程序的入口：

```java
public static void main(String[] args){
    
}
```

举例：

```text
java HelloWorld
```

> 友情提示：
>
> java HelloWord 不要写 不要写 不要写 .class
>
> `如果有包名的话一定加上包名`，否则会显示找不到主类

![image-20230529222543061](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292225123.png)

> Java字节码文件的运行工具：java.exe

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1-6-2-helloworld案例常见错误)1.6.2 HelloWorld案例常见错误

- 单词拼写问题
- 正确：class 错误：Class
- 正确：String 错误：string
- 正确：System 错误：system
- 正确：main 错误：mian
- Java语言是一门严格区分大小写的语言
- 标点符号使用问题
- 不能用中文符号，英文半角的标点符号（正确）
- 括号问题，成对出现

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1-6-3-java程序的结构与格式)1.6.3 Java程序的结构与格式

结构：

```markdown
类{
    方法{
        语句;
    }
}
```

格式：

（1）每一级缩进一个Tab键

（2）{} 的左半部分在行尾，右半部分单独一行，与和它成对的"{"的行首对齐

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1-6-4-public-class与class的区别-掌握)1.6.4 public class与class的区别（掌握）

1. 一个java源文件中可以定义多个class
2. 一个class会编译生成一个class文件
3. public的类可以没有，有的话，只能有一个，并且public的类名要和源文件名保持一致
4. 任何一个class中都可以有main方法，但对于一个软件来说，一般入口只有一个

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1-6-5-编写java程序时应该注意的问题)1.6.5 编写Java程序时应该注意的问题

#### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1、字符编码问题)1、字符编码问题

当cmd命令行窗口的字符编码与.java源文件的字符编码不一致，如何解决？

![image-20230529222753386](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292227438.png)

解决方案：

```
在使用javac命令式，可以指定源文件的字符编码
javac -encoding utf-8 HelloWorld.java
```

#### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_2、大小写问题)2、大小写问题

（1）源文件名：

```markdown
在Windows操作系统中.java的源文件名不区分大小写，我们建议大家养成区分大小写的习惯。
```

（2）字节码文件名与类名

```markdown
严格区分大小写
```

（3）代码中

```markdown
严格区分大小写
```

#### [#](https://gaoziman.gitee.io/blogs/pages/882008/#_3、源文件名与类名一致问题)3、源文件名与类名一致问题？

（1）源文件名是否必须与类名一致？`public`呢？

```markdown
如果这个类不是public，那么源文件名可以和类名不一致。但是不便于代码维护。

如果这个类是public，那么要求源文件名必须与类名一致。否则编译报错。

我们建议大家，不管是否是public，都与源文件名保持一致，而且一个源文件尽量只写一个类，目的是为了好维护。
```

（2）一个源文件中是否可以有多个类？`public`呢？

```markdown
一个源文件中可以有多个类，编译后会生成多个.class字节码文件。

但是一个源文件只能有一个public的类。
```

（3）main方法必须在`public`的类中吗？

```markdown
不是。

但是后面写代码时，基本上main方法（主方法）习惯上都在public类中。
```

## [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1-7-本章练习题)1.7 本章练习题

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#打印你的个人信息)打印你的个人信息

包括：姓名，年龄，性别，家庭住址，联系电话等

![image.png](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292231284.png)

```java
public class PersonalInfo {
    public static void main(String[] args) {
        System.out.println("姓名：张三");
        System.out.println("年龄：25");
        System.out.println("性别：男");
        System.out.println("家庭住址：北京市海淀区");
        System.out.println("联系电话：13888888888");
    }
}
```

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#打印一个菱形)打印一个菱形

![image.png](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292231288.png)

```java
public class Diamond {
    public static void main(String[] args) {
        System.out.println("    *    ");
        System.out.println("   ***   ");
        System.out.println("  *****  ");
        System.out.println(" ******* ");
        System.out.println("*********");
        System.out.println(" ******* ");
        System.out.println("  *****  ");
        System.out.println("   ***   ");
        System.out.println("    *    ");
    }
}
```

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#打印商品列表)打印商品列表

![image.png](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305292231317.png)

```java
public class ProductList {
    public static void main(String[] args) {
        System.out.println("Product\t\tPrice\tStock");
        System.out.println("Apple\t\t3.5\t10");
        System.out.println("Banana\t\t2.5\t20");
        System.out.println("Orange\t\t4.0\t15");
        System.out.println("Watermelon\t5.0\t5");
        System.out.println("Grape\t\t6.0\t8");
    }
}
```

## [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1-8-本章面试题)1.8 本章面试题

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#你认为java是解释型语言还是编译型语言)你认为Java是解释型语言还是编译型语言？

Java既不是纯解释型语言，也不是纯编译型语言，而是一种混合型语言。Java源代码首先会被编译成字节码文件，字节码文件不是针对特定的硬件和操作系统而编译的，而是针对Java虚拟机（JVM）而编译的。字节码文件在运行时由JVM解释执行，JVM会将字节码文件转换为机器码并执行，这样就可以实现跨平台性，使得Java程序可以在任何安装了JVM的计算机上运行。因此，Java是一种混合型语言，它既具备编译型语言的高效性，又具备解释型语言的跨平台性。

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#java是如何做到跨平台的-请说出你的理解)Java是如何做到跨平台的，请说出你的理解？

Java是一种基于虚拟机的编程语言，它的跨平台性是通过Java虚拟机（JVM）实现的。Java程序在编译时会被编译成字节码，而不是直接编译成机器语言。这些字节码可以在任何支持Java虚拟机的平台上运行，包括Windows、Mac、Linux等操作系统。 Java虚拟机是一个抽象的计算机，它提供了一个独立于硬件平台的运行环境。当Java程序在不同的操作系统上运行时，JVM会将字节码解释成机器码，从而实现跨平台运行。这种机制保证了Java程序在不同平台上的一致性和可移植性。 总的来说，Java的跨平台性是通过将程序编译成字节码，再由Java虚拟机解释执行实现的。这种机制使得Java程序可以在不同平台上运行，无需重新编译。

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#请解释一下java中的类路径是什么)请解释一下Java中的类路径是什么？

Java中的类路径（Classpath）是指JVM在搜索类文件（.class文件）时所使用的路径。在Java中，当需要加载一个类时，JVM会按照一定的顺序在类路径中查找该类的字节码文件。如果找到了该文件，则会加载该类并创建相应的对象。 类路径可以由多个路径组成，路径之间用分号（Windows系统）或者冒号（Unix/Linux系统）分隔。在Java中，类路径可以分为系统类路径和用户类路径。 系统类路径是JVM默认的类路径，它包含了Java运行环境中的核心类库和扩展类库。系统类路径可以通过系统属性"java.class.path"来获得。 用户类路径是用户自定义的类路径，它包含了用户自己编写的类文件和第三方库文件。用户类路径可以通过"-classpath"或"-cp"选项指定，也可以通过设置系统环境变量CLASSPATH来指定。 通常情况下，Java程序的类文件都位于用户类路径中，而核心类库和扩展类库位于系统类路径中。在编写Java程序时，需要根据实际情况配置类路径，以确保程序能够正常运行。

### [#](https://gaoziman.gitee.io/blogs/pages/882008/#java字节码是机器码吗)Java字节码是机器码吗？

Java字节码不是机器码。Java源代码在编译时会被编译成Java字节码（.class文件），而不是直接编译成机器码。Java字节码是一种中间代码，它是一种平台无关的二进制代码，可以在任何支持Java虚拟机（JVM）的平台上运行。 Java字节码是由Java编译器生成的一种二进制文件，它包含了Java源代码编译后的中间代码，而不是机器码。Java字节码可以被JVM解释执行，JVM会将字节码解释成机器码，从而实现跨平台运行。 Java字节码的优点是可以在不同平台上运行，而不需要重新编译。这种机制使得Java程序具有很强的可移植性和跨平台性。但是，由于Java字节码需要被JVM解释执行，因此Java程序的执行速度相对较慢。

## [#](https://gaoziman.gitee.io/blogs/pages/882008/#_1-9-本章总结)1.9 本章总结

1. 计算机的核心硬件是什么？各自有什么用？
2. 软件分为哪两类？
3. 你知道哪些系统软件？
4. 你知道哪些应用软件？
5. 计算机语言发展的大体趋势是怎样的？
6. Java之父的名字是？logo是？
7. Java中被长期支持的稳定版本是？
8. Java语言的三大分支？
9. Java中非常重要的两个特性是？
10. 能够简单的描述出Java的加载与执行的过程。
11. 能够独立的编写第一个Java程序，从安装JDK，到配置环境变量，到编写，到编译，到最终的运行。
12. 能够完全理解PATH环境变量
13. 能够完全理解CLASSPATH环境变量
14. Java注释的三种写法？
15. 了解javadoc命令
16. 一个文件中可以定义多个class，一个class会生成一个class文件
17. public的类可以没有，但如果有，只能有一个，并且和源文件名一致
18. 任何一个class中都可以有main方法，但对于一个软件来说，一般入口只有一个

# Java基础语法

[![万维广告联盟](https://cdn.wwads.cn/images/placeholder/130x100.png)](https://wwads.cn/)

[万维广告是一个高品质的垂直广告网络联盟，一键购买此流量资源的广告位](https://wwads.cn/)[![img]()广告](https://wwads.cn/?utm_source=property-0&utm_medium=footer)



## [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#前言)前言

> Java以前自学过一写，现在工作了，时间太久有一些知识都遗忘了，今天开始就更新Java了，想着把之前的Java基础知识捡起来；从最基础的开始，打好Java基础，便于以后复习。也欢迎大家跟我一起复习。

## 1.0所有基础语法

```java
// 这是一个Java程序的入口点，main方法
public class JavaDemo {
    public static void main(String[] args) {
        // 这是一个变量的声明和赋值，变量是用来存储数据的
        int x = 10; // int是整数类型
        double y = 3.14; // double是双精度浮点数类型
        String z = "Hello"; // String是字符串类型

        // 这是一个输出语句，用来在控制台打印数据
        System.out.println("x = " + x); // +号可以用来连接字符串和其他类型的数据
        System.out.println("y = " + y);
        System.out.println("z = " + z);

        // 这是一个算术运算符的示例，用来进行数学计算
        int a = x + 5; // 加法
        int b = x - 5; // 减法
        int c = x * 5; // 乘法
        int d = x / 5; // 除法
        int e = x % 5; // 取余

        // 这是一个关系运算符的示例，用来比较两个值的大小关系，返回一个布尔值（true或false）
        boolean f = x > y; // 大于
        boolean g = x < y; // 小于
        boolean h = x == y; // 等于
        boolean i = x != y; // 不等于

        // 这是一个逻辑运算符的示例，用来组合多个布尔值，返回一个布尔值
        boolean j = f && g; // 与，表示两个条件都为true时才为true
        boolean k = f || g; // 或，表示两个条件有一个为true时就为true
        boolean l = !f; // 非，表示取反

        // 这是一个if-else语句的示例，用来根据条件执行不同的分支
        if (x > 0) { // 如果x大于0，则执行这个分支
            System.out.println("x is positive");
        } else { // 否则执行这个分支
            System.out.println("x is negative or zero");
        }

        // 这是一个switch语句的示例，用来根据变量的值执行不同的分支
        switch (x) {
            case 1: // 如果x等于1，则执行这个分支，并跳出switch语句
                System.out.println("x is one");
                break;
            case 2: // 如果x等于2，则执行这个分支，并跳出switch语句
                System.out.println("x is two");
                break;
            default: // 如果x不等于1或2，则执行这个分支，并跳出switch语句
                System.out.println("x is neither one nor two");
                break;
        }

        // 这是一个for循环语句的示例，用来重复执行一段代码多次
        for (int n = 1; n <= 10; n++) { // n是循环变量，从1开始，每次增加1，直到大于10为止
            System.out.println("n = " + n); // 每次循环都打印n的值
        }

        // 这是一个while循环语句的示例，用来重复执行一段代码直到条件不满足为止
        int m = 1; // m是循环变量，初始值为1
        while (m <= 10) { // 当m小于等于10时，继续循环
            System.out.println("m = " + m); // 每次循环都打印m的值
            m++; // 每次循环都让m增加1
        }

        // 这是一个do-while循环语句的示例，用来重复执行一段代码直到条件不满足为止，至少执行一次
        int p = 1; // p是循环变量，初始值为1
        do {
            System.out.println("p = " + p); // 每次循环都打印p的值
            p++; // 每次循环都让p增加1
        } while (p <= 10); // 当p小于等于10时，继续循环

        // 这是一个数组的声明和初始化，数组是用来存储多个同类型数据的集合
        int[] arr = {1, 2, 3, 4, 5}; // arr是一个整数类型的数组，有5个元素，分别是1, 2, 3, 4, 5

        // 这是一个遍历数组的示例，用来访问数组中的每个元素
        for (int q = 0; q < arr.length; q++) { // q是数组的索引，从0开始，每次增加1，直到小于数组的长度为止
            System.out.println("arr[" + q + "] = " + arr[q]); // 每次循环都打印数组中对应索引的元素
        }

        // 这是一个方法的定义，方法是用来封装一段具有特定功能的代码，可以被其他地方调用
        public static int add(int a, int b) { // add是方法的名字，int a和int b是方法的参数，int是方法的返回类型
            int sum = a + b; // sum是方法内部的局部变量，用来存储两个参数的和
            return sum; // return语句用来返回方法的结果
        }

        // 这是一个方法的调用，用来执行方法中的代码，并得到返回值
        int r = add(3, 4); // r是一个变量，用来接收add方法返回的结果，3和4是传递给add方法的实际参数
        System.out.println("r = " + r); // 打印r的值

        // 这是一个类的定义，类是用来描述一种事物的属性和行为的模板
        public class Person { // Person是类的名字
            // 这些是类的属性，用来描述类的特征
            String name; // name是一个字符串类型的属性，表示人的名字
            int age; // age是一个整数类型的属性，表示人的年龄

            // 这是类的构造方法，用来创建类的实例（对象）
            public Person(String name, int age) { // 构造方法和类名相同，有两个参数name和age
                this.name = name; // this关键字表示当前对象，this.name表示当前对象的name属性，name表示传入的参数name
                this.age = age; // this.age表示当前对象的age属性，age表示传入的参数age
            }

            // 这些是类的方法，用来描述类的行为
            public void sayHello() { // sayHello是一个无参无返回值的方法，用来打拟人说话
                System.out.println("Hello, my name is " + name + ", I am " + age + " years old."); // 打印人的名字和年龄
            }

            public void growUp() { // growUp是一个无参无返回值的方法，用来模拟人长大一岁
                age++; // 让人的年龄增加1
                System.out.println(name + " is now " + age + " years old."); // 打印人现在的年龄
            }
        }

        // 这是一个创建类对象并使用其属性和方法的示例
        Person s = new Person("Tom", 18); // s是一个Person类型的对象，使用Person类的构造方法创建，并传入名字和年龄作为参数
        s.sayHello();
```



## [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-1-注释-annotation-掌握)1.1 注释（annotation）（掌握）

- **注释**：就是对代码的解释和说明。其目的是让人们能够更加轻松地了解代码。为代码添加注释，是十分必须要的，它不影响程序的编译和运行。

- Java中有`单行注释`、`多行注释`和`文档注释`

  - 单行注释以 `//`开头，以`换行`结束，格式如下：

    ```java
    // 注释内容
    ```

  - 多行注释以 `/*`开头，以`*/`结束，格式如下：

    ```java
    /*
    	注释内容
     */
    ```

  - 文档注释以`/**`开头，以`*/`结束，Java特有的注释，结合

    ```java
    /**
    	注释内容
     */
    ```

```java
//单行注释
/*
多行注释
*/
/**
文档注释演示
@author gaoziman
*/
public class Comments{
    
	/**
	Java程序的入口
	@param String[] args main方法的命令参数
	*/
    public static void main(String[] args){
        System.out.println("hello");
    }
}
```

常见的几个注释：

- @author 标明开发该类模块的作者，多个作者之间使用,分割

- @version 标明该类模块的版本
- @see 参考转向，也就是相关主题
- @since 从哪个版本开始增加的
- @param 对方法中某参数的说明，如果没有参数就不能写（后面再学）
- @return 对方法返回值的说明，如果方法的返回值类型是void就不能写（后面再学）
- @throws/@exception 对方法可能抛出的异常进行说明 ，如果方法没有用throws显式抛出的异常就不能写（后面再学）

其中 @param @return 和 @exception 这三个标记都是只用于方法的。

- @param的格式要求：@param 形参名 形参类型 形参说明
- @return 的格式要求：@return 返回值类型 返回值说明
- @exception 的格式要求：@exception 异常类型 异常说明
- @param和@exception可以并列多个

使用javadoc工具可以基于文档注释生成API文档。

```text
用法: javadoc [options] [packagenames] [sourcefiles] [@files]
```

例如：

```java
javadoc -author -d doc Comments.java
```

![image-20230530190521100](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301905236.png)

![image-20230530190536183](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301905299.png)

![image-20230530190548742](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301905881.png)

## [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-2-标识符-identifier-掌握)1.2 标识符( identifier)（掌握）

简单的说，凡是**程序员自己命名**的部分都可以称为`标识符`。

即给`类、变量、方法、包`等命名的字符序列，称为`标识符`。

Java中合法的标识符需要满足以下要求：

1. 标识符可以由字母、数字、下划线(_)和美元符号($)组成，不能含有其他符号。（java支持全球所有语言，所以这里的 字母 指的是任何一个国家的语言都可以）
2. 标识符不能以数字开头。
3. 标识符不能是Java中的关键字，如public、class、void等。
4. 标识符是区分大小写的，即Foo和foo是两个不同的标识符。
5. 标识符的长度没有限制，但是Java建议使用有意义的、简短的标识符。

```
标识符的命名规范（建议遵守的软性规则，否则容易被鄙视和淘汰）
```

- 见名知意

- 类名、接口名等：每个单词的首字母都大写，形式：XxxYyyZzz，

  例如：HelloWorld，String，System等

- 变量、方法名等：从第二个单词开始首字母大写，其余字母小写，形式：xxxYyyZzz，

  例如：age,name,bookName,main

- 包名等：每一个单词都小写，单词之间使用点.分割，形式：xxx.yyy.zzz，

  例如：java.lang

- 常量名等：每一个单词都大写，单词之间使用下划线_分割，形式：XXX_YYY_ZZZ，

  例如：MAX_VALUE,PI

> 例如，以下是合法的标识符：
>
> 1. name
> 2. _name
> 3. $name
> 4. name123
> 5. Name
> 6. MyClassName
>
> 而以下是不合法的标识符：
>
> 1. 123name（以数字开头）
> 2. public（关键字）
> 3. my-name（中间包含横线）
> 4. MyClassName!（包含非法字符）

## [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-3-关键字-keyword-掌握)1.3 关键字（keyword）（掌握）

**关键字**：是指在程序中，Java已经定义好的单词，具有特殊含义。

Java关键字是Java编程语言中预定义的具有特殊含义的保留字，这些保留字不能被用作标识符或变量名，而是在语法中有特定的用法和限制。Java关键字的作用是控制程序的逻辑和结构，这些关键字通常用于声明变量、定义类、控制程序流程、实现面向对象编程等。

Java关键字的种类有很多，包括基本数据类型关键字（如int、double、boolean等）、控制流程关键字（如if、for、while等）、访问权限关键字（如public、private、protected等）、类和对象关键字（如class、new、extends、super等）、异常处理关键字（如try、catch、finally等）等。不同的关键字有不同的作用和用法，程序员需要根据具体的需求选择合适的关键字来编写代码。

Java关键字的使用规则也有一些限制，例如关键字不能作为变量名、方法名等标识符的名称，也不能在不同的上下文中使用不同的含义。因此，在编写Java代码时，程序员需要遵守Java关键字的使用规则，以保证程序的正确性和可读性。

- HelloWorld案例中，出现的关键字有 `public` 、`class` 、 `static` 、 `void` 等，这些单词已经被Java定义好
- 关键字的特点：全部都是`小写字母`。
- 关键字比较多，不需要死记硬背，学到哪里记到哪里即可。

![1555209180504](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904108.png)

> **关键字一共50个，其中const和goto是保留字。**

> **true,false,null看起来像关键字，但从技术角度，它们是特殊的布尔值和空值。**

## [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-4-字面量-理解)1.4 字面量(理解)

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#什么是字面量)什么是字面量

Java中，字面量指的是在程序中直接使用的数据，字面量是Java中最基本的表达式，不需要进行计算或转换，直接使用即可。

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#java中都有哪些字面量)Java中都有哪些字面量

- 整数型：10、-5、0、100
- 浮点型：3.14、-0.5、1.0
- 布尔型：true、false
- 字符型：'a'、'b'、'c'、'1'、'2'、'国'
- 字符串型："Hello"、"World"、"Java"、"你好呀"

## [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-5-初识数据类型-data-type-掌握)1.5 初识数据类型(data type)（掌握）

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#java数据类型概述)Java数据类型概述

Java的数据类型分为两大类：

- 基本数据类型
  - 整数类型：包括**byte**、**short**、**int**和**long**四种类型，用于表示整数。
  - 浮点类型：包括**float**和**double**两种类型，用于表示带小数点的数值。
  - 布尔类型：**boolean**类型，只有true和false两个值，用于表示逻辑值。
  - 字符类型：**char**类型，用于表示单个字符，它是基于Unicode编码的。
- 引用数据类型
  - 类、接口、数组、枚举等。（或者你也可以这样记：除了8种基本数据类型之外，其他都是引用数据类型，**包括String**。）

![image-20210628142322228](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904105.png)

**现阶段重点研究基本数据类型，以后再说引用数据类型。**

下面详细介绍一下每种类型的特点和使用方法：

1. 整数类型：

- byte类型：占用1个字节，范围是-128到127，常用于存储小整数。 (byte类型的1：00000001)
- short类型：占用2个字节，范围是-32768到32767，常用于存储中等大小的整数。 (short类型的1：00000000 00000001)
- int类型：占用4个字节，范围是-2147483648到2147483647，是Java中最常用的整数类型。
- long类型：占用8个字节，范围是-9223372036854775808到9223372036854775807，用于存储极大或极小的整数。

**为什么设计出这么多整数？目的是合适的数据选择合适的类型，可以节省空间，但实际开发中不必斤斤计较，大部分采用int。另外，如果数据过大，超过了long，可以使用BigInteger，它就不是基本数据类型了，属于引用数据类型。后面再说。**

1. 浮点类型：

- float类型：占用4个字节，范围是1.4E-45到3.4028235E38，精度为7位小数，常用于科学计算和工程计算。
- double类型：占用8个字节，范围是4.9E-324到1.7976931348623157E308，精度为15位小数，是Java中最常用的浮点类型。 （**如果超出了double，可以使用BigDecimal，同样它也是一种引用数据类型。**）

1. 布尔类型：

- boolean类型：只有两个值，true和false，用于表示逻辑值，例如判断语句、循环语句等。

1. 字符类型：

- char类型：占用2个字节，用于表示单个字符，例如'A'、'B'、'C'等，也可以表示Unicode编码中的任意字符。

这是一个直观的列表：

| 数据类型 | 占用字节数 | 取值范围                          | 具体取值范围                               | 默认值   |
| -------- | ---------- | --------------------------------- | ------------------------------------------ | -------- |
| byte     | 1          | -2^7 ~ 2^7-1                      | -128 ~ 127                                 | 0        |
| short    | 2          | -2^15 ~ 2^15-1                    | -32768 ~ 32767                             | 0        |
| int      | 4          | -2^31 ~ 2^31-1                    | -2147483648 ~ 2147483647                   | 0        |
| long     | 8          | -2^63 ~ 2^63-1                    | -9223372036854775808 ~ 9223372036854775807 | 0L       |
| float    | 4          | 1.4E-45 ~ 3.4028235E38            | 1.4E-45 ~ 3.4028235E38                     | 0.0f     |
| double   | 8          | 4.9E-324 ~ 1.7976931348623157E308 | 4.9E-324 ~ 1.7976931348623157E308          | 0.0d     |
| boolean  | 1          | true / false                      | true / false                               | false    |
| char     | 2          | 0 ~ 2^16-1                        | 0 ~ 65535                                  | '\u0000' |

关于默认值：Java语言中变量必须先声明，再赋值，才能使用。对于局部变量来说必须手动赋值，而对于成员变量来说，如果没有手动赋值，系统会自动赋默认值。例如：

```java
public class DefaultValue {
    // 成员变量有系统默认值
    static int i;
    public static void main(String[] args){
        System.out.println(i); // 0
        // 成员变量没有系统默认值
        int k;
        System.out.println(k); // 编译报错
    }
}
```

注意：对于引用数据类型来说，默认值null，例如：

```java
public class DefaultValue {
    static String name;
    public static void main(String[] args){
        // String是引用数据类型。
        System.out.println(name); // null
    }
}
```

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#整数型详解)整数型详解

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#整数型字面量的四种表示形式)整数型字面量的四种表示形式

Java中整数型字面量有以下四种表示形式：

1. 十进制表示法：以数字0-9组成的常数，默认为十进制表示法。

   > 例如：int a = 10;

2. 二进制表示法：以0b或0B开头的常数，由0和1组合而成。

   > 例如：int b = 0b101;

3. 八进制表示法：以0开头的常数，由数字0-7组成。

   > 例如：int c = 012;

4. 十六进制表示法：以0x或0X开头的常数，由0-9和A-F（大小写均可）组成。

   > 例如：int d = 0x1F;

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#整数型字面量默认当做int处理)整数型字面量默认当做int处理

Java中整数型字面量默认被当做int类型来处理，**如果要表示long类型的整数，需要在字面量后面加上'L'或'l'标记**。例如，下面是表示int和long类型整数的字面量的示例：

```java
int x = 10; // 10是一个int类型的字面量
long y = 10L; // 10L是一个long类型的字面量
```

需要注意的是，大小写字母'L'和'l'的使用没有区别，但是容易被误解为数字1，因此建议使用大写字母。 请看以下代码有什么问题吗？

```java
long z = 2147483648;
```

编译报错，原因是2147483648被当做int类型处理，而该数字本身已经超出了int最大值，如何修改？

```java
long z = 2147483648L;
```

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#自动类型转换)自动类型转换

**自动转换**：

- 将`取值范围小的类型`自动提升为`取值范围大的类型` 。

基本数据类型的转换规则如图所示：

![img](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301944538.jpg)

![未命名文件.jpg](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301937852.jpeg)

在Java中，对于基本数据类型来说，小容量是可以直接赋值给大容量的，这被称为自动类型转换。对于数字类型来说大小关系为：byte < short < int < long < float < double。

当把存储范围小的值（常量值、变量的值、表达式计算的结果值）赋值给了存储范围大的变量时。

```java
int i = 'A';//char自动升级为int，其实就是把字符的编码值赋值给i变量了
double d = 10;//int自动升级为double

byte b = 127; //右边的整数常量值必须在-128~127范围内
//byte bigB = 130;//错误，右边的整数常量值超过byte范围
long num = 1234567; //右边的整数常量值如果在int范围呢，编译和运行都可以通过，这里涉及到数据类型转换
long bigNum = 12345678912L;//右边的整数常量值如果超过int范围，必须加L，否则编译不通过
```

（2）当存储范围小的数据类型与存储范围大的数据类型一起混合运算时，会按照其中最大的类型运算。

```java
int i = 1;
byte b = 1;
double d = 1.0;

double sum = i + b + d;//混合运算，升级为double
```

（3）当byte,short,char数据类型进行算术运算时，按照int类型处理。

```text
byte b1 = 1;
byte b2 = 2;
byte b3 = b1 + b2;//编译报错，b1 + b2自动升级为int

char c1 = '0';
char c2 = 'A';
System.out.println(c1 + c2);//113 
需要注意的是，自动类型转换只适用于基本数据类型之间的转换。
```

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#强制类型转换)强制类型转换

强制类型转换：Java中大容量是无法直接转换成小容量的。因为这种操作**可能**会导致精度损失，所以这种行为交给了程序员来决定，当然这种后果自然是程序员自己去承担。因此在代码中需要程序员自己亲手加上强制类型转换符，程序才能编译通过。 以下程序编译器就会报错：

```java
int num = 10L;
```

解决方案两个：要么把L去掉，要么使用强制类型转换符，例如：

```java
int num = (int)10L;
```

这样编译器就能编译通过了。

> 强制类型转换时，底层二进制是如何变化的？**原则：砍掉左侧多余的二进制**。例如以上程序的二进制变化是这样的： long类型的10对应的二进制：00000000 00000000 00000000 00000000 00000000 00000000 00000000 00001010 强制转换为int类型的10是这样的：00000000 00000000 00000000 00001010
>
> 因此，强制类型转换时，精度可能会损失，也可能不会损失，这要看具体的数据是否真正的超出了强转后的类型的取值范围。如下图：水可能溢出，也可能不会溢出，这要看真实存放的水有多少！！！

![未命名文件 (1).jpg](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301937847.jpeg)

如果你理解了强制类型转换，那么下面这个程序的执行结果可以推算出来吗？

```java
byte b = (byte)150;
```

> int类型的150的补码（150是正数：原码反码补码一样）：00000000 00000000 00000000 10010110 强转砍掉前三个多出的字节，结果是：10010110（这个是最终存储在计算机中的，注意：存储在计算机中的是补码） 将以上补码10010110推算出原码：11101010（结果是：-106） 因此int类型的150强转为byte类型之后，结果是-106

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#当整数字面量没有超出byte的范围)当整数字面量没有超出byte的范围

在Java中有这样一个规定，当整数型字面量没有超出byte的范围：可以直接赋值给byte类型的变量。

```java
byte b = 127; // 这是允许的
```

很显然，这是一种编译优化。同时也是为了方便程序员写代码。 如果超出了范围，例如：

```java
byte b = 128; // 编译报错
```

这样就会报错，需要做强制类型转换，例如：

```java
byte b = (byte)128;
```

它的执行结果你知道吗？可以尝试推算一下，最终结果是：-128 **在整数类型中，除了byte有这个待遇之外，short同样也是支持的。也就是说：如果整数型字面量没有超出short取值范围时，也是支持直接赋值的。**

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#两个int类型做运算)两个int类型做运算

两个int类型的数据做运算，最终的结果还是int类型：

```java
int a = 10;
int b = 3;
int c = a / b; 
System.out.println(c); // 3
```

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#多种数据类型混合运算)多种数据类型混合运算

在Java中，多种数据类型混合运算时，各自先转换成容量最大的类型，再做运算。

```java
byte a = 100;
int b = 200;
long c = 300L;
long d = a + b + c;
```

你可以测试一下，如果d变量是int类型则编译器会报错。

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#编译器的小心思)编译器的小心思

以下程序编译通过：

```java
byte x = 10 / 3;
```

为什么编译通过？这种情况下都是字面量的时候，编译器可以在编译阶段得出结果是3，而3没有超出byte取值范围。可以直接赋值。 以下程序编译报错：

```java
int a = 10;
int b = 3;
byte x = a / b;
```

为什么编译失败？这种a和b都是变量的情况下，编译器是无法在编译阶段得出结果的，编译器只能检测到结果是int类型。int类型不能直接赋值给byte类型变量。 怎么解决？要么把x变量声明为int类型，要么强制类型转换，例如：

```java
int a = 10;
int b = 3;
byte x = (byte)(a / b);
```

这里需要注意的是：注意小括号的添加，如果不添加小括号，例如：

```java
int a = 10;
int b = 3;
byte x = (byte)a / b;
```

这样还是编译报错，因为只是将a强转为byte了，b还是int。byte和int混合运算，结果还是int类型。

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#浮点型详解)浮点型详解

浮点型类型包括：

- 单精度（float）：4字节（32位）
- 双精度（double）：8字节（64位），精度较高，实际开发中double用的多。

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#浮点型字面量默认被当做double)浮点型字面量默认被当做double

Java中，浮点型字面量默认被当做double类型，如果要当做float类型，需要在数字后面添加 F 或 f。

```java
float f = 3.0; // 编译报错
```

报错原因是：3.0默认被当做double类型，大容量无法直接赋值给小容量。如何修改：

```java
float f = 3.0F;
```

另外，可以通过以下程序的输出结果看到，double精度高于float：

```java
double d = 1.5656856894;
System.out.println(d);

float f = 1.5656856894F;
System.out.println(f);
```

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#浮点型数据两种表示形式)浮点型数据两种表示形式

第一种形式：十进制

```java
double x = 1.23;
double y = 0.23;
double z = .23;
```

第二种形式：科学计数法

```java
double x = 0.123E2; // 0.123 * 10的平方
double y = 123.34E-2; // 123.34 / 10的平方
```

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#浮点型数据存储原理)浮点型数据存储原理

以单精度float为例： ![image.png](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301937835.png)

> 符号位：0表示整数。1表示负数。 指数位：比如小数0.123E30，其中30就是指数。表示0.123 * 10的30次幂。所以也有把指数位叫做偏移量的。最大偏移量127。 尾数位：浮点数的小数部分的有效数字。例如：0.00123，那么尾数位存储123对应的二进制。

**从浮点型数据存储原理上可以看到，二进制中的指数位决定了数字呈指数级增大。因此float虽然是4个字节，但却可以表示比long更大的数值。因此float容量比long的容量大。**

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#使用浮点数的注意事项)使用浮点数的注意事项

计算机的二进制位有限，现实世界中有无限循环的数字，例如3.333333333333333333..........，因此计算机这种有限资源去存储无限数据是不可能的，所以浮点型数据在底层真实存储的时候都是采用近似值的方式存储的。尾数位越多精度越高。 实际上包括0.1这样简单的数字，浮点型数据也是无法精确存储的。(想了解更多，请查看相关文献) 这样就会有一个问题，请看以下程序：

```java
double x = 6.9;
double y = 3.0;
double z = x / y;
System.out.println(z);
```

它的执行结果是：2.3000000000000003 并不是2.3 因此一旦有浮点型数据参与运算得出的结果，一定不要使用“==”与其它数字进行“相等比较”。例如，以下代码就存在问题：

```java
double x = 6.9;
double y = 3.0;
double z = x / y;
if(z == 2.3){
    System.out.println("相等");
}
```

执行发现并没有输出：相等。 原因是判断条件有问题。 如果确实需要进行比较，可以将代码修改为如下：

```java
double x = 6.9;
double y = 3.0;
double z = x / y;
if(z - 2.3 < 0.000001){
    System.out.println("相等");
}
```

也就是说，如果这两个数字之间的差小于0.000001，我就认为是相等的。 因此：如果有浮点型数据参与运算得出了结果，不要拿着这个结果和另一个数据进行“==”相等比较。

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#字符型详解)字符型详解

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#字符型详解-2)字符型详解

char：字符型，占用2个字节。取值范围0~65535。和short（-32768~32767）所表示的个数相同。但char可以表示更大的整数。 字符型字面量采用单引号括起来，例如：'a'、'A'、'0'、'国' 等。 字符型字面量只能是单个字符，不能是多个字符。 Java中char类型可以存储一个汉字。

```java
char c1 = 'A';
char c2 = 'a';
char c3 = '0';
char c4 = '国';
char c5 = '¥';

// 编译报错
//char c6 = 'ab';
```

再看下面程序：

```java
char x = '';
```

编译报错。由于单引号中没有任何字符，因此无法给 c 赋值，所以会导致编译报错，提示无效的字符字面量。 如果要赋给 c 一个空的字符，可以使用转义字符 '\u0000' 来表示。如下所示：

```java
char c = '\u0000'; // 赋给 c 一个空字符
```

**注意：空字符与空格字符完全是两码事。**

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#转义字符)转义字符

Java 中的转义字符是一些在字符串中具有特殊含义的字符序列，它们以反斜线（\）开始。以下是 Java 中的一些常用转义字符：

- \t: 表示制表符，相当于按下 Tab 键
- \n: 表示换行符
- \r: 表示回车符
- ": 表示双引号（"）
- ': 表示单引号（'）
- \: 表示反斜线（\）本身

这些转义序列可以用于不同的 Java 数据类型，如字符串、字符等。在 Java 编程中，转义字符可以帮助我们在字符串中表示一些特殊的字符，例如制表符、换行符、引号等。例如，下面的代码演示了如何使用转义字符来创建包含制表符和换行符的字符串：

```java
String str = "Hello\tworld\nHow are you?";
System.out.println(str);
```

这个例子中，\t 和 \n 分别表示字符串中的制表符和换行符。输出结果是：

```text
Hello   world
How are you?
```

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#字符编码的理解)字符编码的理解

字符编码（Character encoding）是计算机系统中使用的一种将字符集中的字符转换为二进制数据的方式，从而方便计算机的存储和传输。在计算机内部，所有的信息都是以二进制形式存储和处理的，因此字符编码是将字符和二进制数据之间的转换方式。每一个字符在计算机中都有其对应的二进制代码。不同的字符编码可以采用不同的编码方式将字符映射到二进制代码，最终这些二进制代码被存储在计算机内部。 在早期计算机系统中，字符编码主要采用的是 ASCII 编码，采用1个字节编码。最多可以表示256个字符。（实际上ASCII码表只用了128个。） 以下是ASCII码表：

| 十进制 | 字符 | 十进制 | 字符  | 十进制 | 字符  | 十进制 | 字符  |
| ------ | ---- | ------ | ----- | ------ | ----- | ------ | ----- |
| 0      | NUL  | 32     | SPACE | 64     | @     | 96     | `     |
| 1      | SOH  | 33     | !     | **65** | **A** | **97** | **a** |
| 2      | STX  | 34     | "     | 66     | B     | 98     | b     |
| 3      | ETX  | 35     | #     | 67     | C     | 99     | c     |
| 4      | EOT  | 36     | $     | 68     | D     | 100    | d     |
| 5      | ENQ  | 37     | %     | 69     | E     | 101    | e     |
| 6      | ACK  | 38     | &     | 70     | F     | 102    | f     |
| 7      | BEL  | 39     | '     | 71     | G     | 103    | g     |
| 8      | BS   | 40     | (     | 72     | H     | 104    | h     |
| 9      | HT   | 41     | )     | 73     | I     | 105    | i     |
| 10     | LF   | 42     | *     | 74     | J     | 106    | j     |
| 11     | VT   | 43     | +     | 75     | K     | 107    | k     |
| 12     | FF   | 44     | ,     | 76     | L     | 108    | l     |
| 13     | CR   | 45     | -     | 77     | M     | 109    | m     |
| 14     | SO   | 46     | .     | 78     | N     | 110    | n     |
| 15     | SI   | 47     | /     | 79     | O     | 111    | o     |
| 16     | DLE  | **48** | **0** | 80     | P     | 112    | p     |
| 17     | DC1  | 49     | 1     | 81     | Q     | 113    | q     |
| 18     | DC2  | 50     | 2     | 82     | R     | 114    | r     |
| 19     | DC3  | 51     | 3     | 83     | S     | 115    | s     |
| 20     | DC4  | 52     | 4     | 84     | T     | 116    | t     |
| 21     | NAK  | 53     | 5     | 85     | U     | 117    | u     |
| 22     | SYN  | 54     | 6     | 86     | V     | 118    | v     |
| 23     | ETB  | 55     | 7     | 87     | W     | 119    | w     |
| 24     | CAN  | 56     | 8     | 88     | X     | 120    | x     |
| 25     | EM   | 57     | 9     | 89     | Y     | 121    | y     |
| 26     | SUB  | 58     | :     | 90     | Z     | 122    | z     |
| 27     | ESC  | 59     | ;     | 91     | [     | 123    | {     |
| 28     | FS   | 60     | <     | 92     | \|124 |        |       |
| 29     | GS   | 61     | =     | 93     | ]     | 125    | }     |
| 30     | RS   | 62     | >     | 94     | ^     | 126    | ~     |
| 31     | US   | 63     | ?     | 95     | _     | 127    | DEL   |

作为程序员，我们应当记住以下几个常用字符的ASCII码：

- a 对应ASCII码 97（b是98，以此类推）
- A 对应ASCII码 65（B是66，以此类推）
- 0 对应ASCII码 48（1是49，以此类推） **什么是解码？什么是编码？乱码是如何产生的？**

在计算机系统中，解码（Decoding）和编码（Encoding）是两个常用的概念，分别表示将二进制数据转换为字符和将字符转换为二进制数据。 编码是将字符转换为二进制数据的过程。解码是将二进制数据转换为字符的过程。例如：

- 'a' ---------按照ASCII码表**编码**-----------> 01100001
- 01100001 --------按照ASCII码表**解码**------------> 'a'

乱码是指在字符编码和解码的过程中，由于编码和解码所采用的字符集不一致，或者编码和解码所采用的字符集不支持某些字符，导致最终显示的字符与原始字符不一致。为了避免乱码的问题，我们需要统一使用一个字符集，并且在进行字符编码和解码时要保持一致。

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#常见的字符编码)常见的字符编码

常见的字符编码方式如下：

1. ASCII 编码（American Standard Code for Information Interchange：美国信息交换标准编码）：采用1个字节编码，包括字母、数字、符号和控制字符等。
2. Latin-1编码（ISO 8859-1），采用1个字节编码。该编码方式是为了表示欧洲语言（如荷兰语、西班牙语、法语、德语等）中的字符而设计的，共支持 256 个字符。
3. ANSI 编码（American National Standards Institute：美国国家标准协会）：采用1个字节编码，支持英文、拉丁文等字符。
4. Unicode 编码：可表示所有语言的字符。采用了十六进制表示，占用 2 个字节或 4 个字节，最多可表示超过一百万个字符。 （使用这种方式是有点浪费空间的，例如英文字符'a'其实采用一个字节存储就够了。）
5. UTF-8 编码（Unicode Transformation Format，8-bit）：基于 Unicode 编码的**可变长度字符编码**，能够支持多语言和国际化的需求，使用 1~4 个字节来表示一个字符，是目前 Web 开发中最常用的字符编码方式。 （一个英文字母1个字节，一个汉字3个字节。）
6. UTF-16 编码：基于 Unicode 编码的可变长度字符编码，使用 2 或 4 个字节来表示一个字符，应用于很多较早的系统和编程语言中。 （一个英文字母2个字节。一个汉字4个字节。）
7. UTF-32编码：基于Unicode编码的固定长度字符编码，其特点是每个字符占用4个字节。
8. GB2312 编码（小）：是中国国家标准的简体中文字符集，使用 2 个字节来表示一个汉字，是 GBK 编码的前身。
9. GBK 编码（Guo Biao Ku）（中）：是针对中文设计的一个汉字编码方式，使用 2 个字节来表示一个汉字，能够表示中国内地的所有汉字。
10. GB18030编码（大）：是中国国家标准GB 18030-2005《信息技术 中文编码字符集》中规定的字符集编码方案，用于取代GB2312和GBK编码。
11. Big5 编码（大五码）：是台湾地区的繁体中文字符集，使用 2 个字节来表示一个汉字，适用于使用繁体中文的应用场景。

每种编码方式都有其特点和适用场景。在进行软件开发、网站开发和数据存储时，需要根据实际情况选择适合的编码方式。

注意：Java语言中的字符char和字符串String，都是采用Unicode编码。

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#unicode码表)Unicode码表

Unicode码表示的一部分：

| 十六进制码 | 字符 | 名称          | 符号                     |
| ---------- | ---- | ------------- | ------------------------ |
| U+0020     |      | 空格          | (space)                  |
| U+0021     | !    | 感叹号        | (exclamation mark)       |
| U+0022     | "    | 双引号        | (quotation mark)         |
| U+0023     | #    | 井号          | (number sign)            |
| U+0024     | $    | 美元          | (dollar sign)            |
| U+0025     | %    | 百分号        | (percent sign)           |
| U+0026     | &    | 和号          | (ampersand)              |
| U+0027     | '    | 单引号        | (apostrophe)             |
| U+0028     | (    | 左括号        | (left parenthesis)       |
| U+0029     | )    | 右括号        | (right parenthesis)      |
| U+002A     | *    | 星号          | (asterisk)               |
| U+002B     | +    | 加号          | (plus sign)              |
| U+002C     | ,    | 逗号          | (comma)                  |
| U+002D     | -    | 减号          | (hyphen,-minus sign)     |
| U+002E     | .    | 句点          | (full stop,period)       |
| U+002F     | /    | 斜杠          | (slash,forward slash)    |
| U+0030     | 0    | 零            | (digit zero)             |
| U+0031     | 1    | 一            | (digit one)              |
| U+0032     | 2    | 二            | (digit two)              |
| U+0033     | 3    | 三            | (digit three)            |
| U+0034     | 4    | 四            | (digit four)             |
| U+0035     | 5    | 五            | (digit five)             |
| U+0036     | 6    | 六            | (digit six)              |
| U+0037     | 7    | 七            | (digit seven)            |
| U+0038     | 8    | 八            | (digit eight)            |
| U+0039     | 9    | 九            | (digit nine)             |
| U+003A     | :    | 冒号          | (colon)                  |
| U+003B     | ;    | 分号          | (semicolon)              |
| U+003C     | <    | 小于号        | (less than sign)         |
| U+003D     | =    | 等于号        | (equals sign)            |
| U+003E     | >    | 大于号        | (greater than sign)      |
| U+003F     | ?    | 问号          | (question mark)          |
| U+0040     | @    | 艾特符号      | (commercial at)          |
| U+0041     | A    | 拉丁大写字母A | (Latin capital letter A) |
| U+0042     | B    | 拉丁大写字母B | (Latin capital letter B) |
| U+0043     | C    | 拉丁大写字母C | (Latin capital letter C) |
| U+0044     | D    | 拉丁大写字母D | (Latin capital letter D) |
| U+0045     | E    | 拉丁大写字母E | (Latin capital letter E) |
| U+0046     | F    | 拉丁大写字母F | (Latin capital letter F) |
| U+0047     | G    | 拉丁大写字母G | (Latin capital letter G) |

在Java程序中也可以使用Unicode码来指定char变量的值：

```java
char c = '\u0041';
```

输出结果是：A

网络上也有很多在线转码工具，例如：[http://www.jsons.cn/unicode/(opens new window)](http://www.jsons.cn/unicode/)

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#char参与的运算)char参与的运算

Java中允许将一个整数赋值给char类型变量，但这个整数会被当做ASCII码值来处理，例如：

```java
char c = 97;
System.out.println(c);
```

会将97当做ASCII码值，该码值转换char类型是字符'a'，所以输出结果是：a 但需要特别注意的是，这个码值有要求，不能超出char的取值范围。如果是这样的，编译会报错：

```java
// 编译报错
char c = 65536;
```

所以结合之间的byte和short，可以有这样一个结论（记住）：只要没有超出byte short char的取值范围，是可以直接赋值给byte short char类型变量的。例如：

```java
byte b = 1;
short s = 1;
char c = 1;
```

再看以下程序输出结果：

```java
System.out.println('a' + 1);
```

输出结果是：98。这是因为1是int类型，所以'a'会被转换为int类型。 再看以下程序输出结果：

```java
char c = 'a' + 1;
System.out.println(c);
```

输出结果是：b。这是因为c的类型是char类型。 再看以下程序输出结果：

```java
byte b = 1;
short s = 1;
char c = 1;
short num = b + s + c;
```

编译报错：第4行的等号右边是int类型，int类型无法赋值给short类型的变量。 这里有一个结论需要记住：byte short char混合运算时，各自会先转换成int再做运算。

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#布尔型详解)布尔型详解

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#关于布尔型的值)关于布尔型的值

Java中的布尔型，关键字：boolean 只有两个值：true、false。没有1和0这一说。 true表示真，false表示假。

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#布尔值通常使用在哪)布尔值通常使用在哪

Java中的布尔值（boolean）通常用于表示一些逻辑上的真假值，并在程序中进行逻辑控制。以下是布尔值在Java中常用的场景：

1. 条件语句，if和while等语句中需要进行条件判断时，通常使用布尔类型的变量作为条件表达式，根据条件的真假情况执行不同的代码逻辑。
2. 逻辑运算，布尔值是逻辑运算的基础，Java中的逻辑运算符有：与（&&）、或（||）、非（!）等，常用于对布尔值的运算和操作。
3. 方法返回值，可以将布尔值作为方法的返回值，表示某种条件是否满足。
4. 开关标记，布尔变量在程序中常用于开关标记的判断和设置，例如，当某个功能开启或关闭时，我们可以用布尔类型的变量来表示。

综上所述，Java中的布尔值在程序中有很多用途，可以在很多场景下提供非常便利的逻辑控制和判断能力。

下面是一个使用布尔值的简单案例：

```java
boolean gender = true;
if(gender){
    System.out.println("男");
}else{
    System.out.println("女");
}
```

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#基本数据类型转换规则总结)基本数据类型转换规则总结

1. 八种基本数据类型，除布尔型之外，其它类型都可以互相转换。
2. 小容量转换为大容量，叫做自动类型转换，容量从小到大的排序为：
   1. byte < short(char) < int < long < float < double
   2. 注意char比short可以表示更大的整数
3. 大容量转换为小容量，叫做强制类型转换，需要加强制类型转换符才能编译通过，运行时可能损失精度，也可能不会损失。
4. 整数字面量如果没有超出byte short char的取值范围，可以直接赋值给byte short char类型的变量。
5. byte short char混合运算，各自先转换为int再做运算。
6. 多种类型混合运算，各自先转换成容量最大的类型，再做运算。

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#变量和数据类型的作业题)变量和数据类型的作业题

1. 请定义合理的变量用来存储个人信息（姓名、年龄、性别、联系电话），并编写程序定义这些变量，给变量赋值，并打印输出。输出效果如下：

   姓名 年龄 性别 联系电话 张三 20 男 12545457585 李四 30 女 15622525855

2. 有两个变量 a 和 b，a 变量中存储的数据100，b 变量中存储的数据200，请编写程序交换两个变量中的数据。让a变量存储200，让b变量存储100。并且计算两个int类型数据的和，要求最终输出 200+100=300的效果。

3. 请分析以下程序中哪些是可以编译通过的，哪些是报错的

   ```java
   short s = 100;
   s = s - 99;
   
   byte b = 100;
   b = b + 1;
   
   char c = 'a'
   int i = 20;
   float f = .3F;
   double d = c + i + f;
   
   byte b = 11;
   short s = 22;
   short x = b + s;
   ```

## [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-6-常量值-constant-掌握)1.6 常量值（constant）（掌握）

- **常量值：在程序执行的过程中，其值不可以发生改变**

- 常量值的分类：

  |     类型     |          举例           |
  | :----------: | :---------------------: |
  |  整数常量值  | 12，-23, 1567844444557L |
  |  浮点常量值  |      12.34F，12.34      |
  |  字符常量值  |     ‘a’，'0'，‘高’      |
  |  布尔常量值  |       true，false       |
  | 字符串常量值 |      ”HelloWorld“       |

- 整数常量值，超过int范围的必须加L或l（小写L）
- 小数常量值，无论多少，不加F，就是double类型。要表示float类型，必须加F或f
- char常量值，必须使用单引号
- String字符串常量值，必须使用双引号

```java
public class ConstantDemo {
	public static void main(String[] args) {		
		//输出整数常量值
		System.out.println(12);
		System.out.println(-23);
        System.out.println(2352654566L);
		
		//输出小数常量值
        System.out.println(12.34F);
		System.out.println(12.34);
		
		//输出字符常量值
		System.out.println('a');
		System.out.println('0');
        System.out.println('尚');
		
		//输出布尔常量值
		System.out.println(true);
		System.out.println(false);
        
        //输出字符串常量值
		System.out.println("HelloWorld");
	}
}
```

## [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-7-变量-variable-掌握)1.7 变量（variable）（掌握）

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-7-1-什么是变量)1.7.1 什么是变量

![image-20230530191821409](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301918533.png)

变量可以看做是一个盒子，这个盒子可以存储数据。本质上，变量是内存当中的一块空间，这块空间有三要素（变量的三要素）：

- 要素一：数据类型（决定了空间大小）。例如有一种数据类型叫做整数型：int
- 要素二：名字（只要是合法的标识符就行）。例如：age（年龄）
- 要素三：值（盒子中具体存储的数据）。例如：20

例如以下代码则表示声明了一个整数类型的变量age，值为20

```java
int age = 20;
```

以及以下代码则表示声明了一个字符串类型的变量name，值为"jack"

```java
String name = "jack";
```

数据类型后面小节会详细讲解。目前只需要知道int代表整数类型，String代表字符串类型即可。 另外，变量的“变”体现在哪里呢？体现在变量这个盒子中的数据是可以改变的。例如，通过“=”赋值运算符，可以改变盒子中存储的数据：

```java
age = 30;
```

这个操作用专业术语表达叫做：给变量重新赋值。 重新赋值时也是有要求的，值的类型要和变量的类型一致，不然就会报错，例如：

```java
age = "30";
```

报错信息如下： ![image.png](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301918842.png)

> 编译器找到等号右边的数据，发现是String类型，然后发现age这个盒子只能存储int类型，类型不匹配，表示这种int盒子不能存放String类型的数据。

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-7-2-变量的作用)1.7.2 变量的作用

有这样一个需求：请用你当前所学知识，分别计算100和111、222、666、888、999的和，你该怎么编写代码？

```java
System.out.println(100 + 111);
System.out.println(100 + 222);
System.out.println(100 + 666);
System.out.println(100 + 888);
System.out.println(100 + 999);
```

现在需求变化了，要求计算234和111、222、666、888、999的和，你需要将以上代码中所有的100全部进行修改：

```java
System.out.println(234 + 111);
System.out.println(234 + 222);
System.out.println(234 + 666);
System.out.println(234 + 888);
System.out.println(234 + 999);
```

修改了5个位置，如果求和的数据更多，那么修改的位置也会更多，显然：可维护性太差。怎么解决？使用变量可以解决。

```java
int num = 100;
System.out.println(num + 111);
System.out.println(num + 222);
System.out.println(num + 666);
System.out.println(num + 888);
System.out.println(num + 999);
```

如果需求变化了，只需要修改一个位置即可：

```java
int num = 234;
System.out.println(num + 111);
System.out.println(num + 222);
System.out.println(num + 666);
System.out.println(num + 888);
System.out.println(num + 999);
```

通过以上内容的学习，可以得知，**变量的存在，可以让程序更加易维护**。

再比如，又有这样一个需求：现在有三个圆，半径分别是10cm，20cm，30cm，π取值3.14，请分别计算他们的面积，如果不使用变量，程序是这样的：

```java
System.out.println(3.14 * 10 * 10); // 314
System.out.println(3.14 * 20 * 20); // 1256
System.out.println(3.14 * 30 * 30); // 2826
```

上面程序存在的最大问题就是：可读性太差。使用变量可以提高程序的可读性：

```java
double π = 3.14;
int r1 = 10;
int r2 = 20;
int r3 = 30;
System.out.println(π * r1 * r1);
System.out.println(π * r2 * r2);
System.out.println(π * r3 * r3);
因此变量的出现可以提高程序的可读性。
```

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-7-3-变量的声明)1.7.3 变量的声明

```java
数据类型  变量名;
例如：
//存储一个整数类型的年龄
int age; 

//存储一个小数类型的体重
double weight;

//存储一个单字符类型的性别 
char gender;

//存储一个布尔类型的婚姻状态
boolean marry;

//存储一个字符串类型的姓名
String name;

//声明多个同类型的变量
int a,b,c; //表示a,b,c三个变量都是int类型。
```

> 注意：变量的数据类型可以是基本数据类型，也可以是引用数据类型。

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-7-4-变量的赋值)1.7.4 变量的赋值

给变量赋值，就是把“值”存到该变量代表的内存空间中。

1、变量赋值的语法格式

```java
变量名 = 值;
```

- 给变量赋值，变量名必须在=左边，值必须在=右边
- 给变量赋的值类型必须与变量声明的类型一致或兼容（<=）

2、可以使用合适类型的常量值给变量赋值

```java
int age = 18;
double weight = 44.4;
char gender = '女';
boolean marry = true;
String name = "Cisyam";
```

> **long类型：如果赋值的常量整数超过int范围，那么需要在数字后面加L。**
>
> **float类型：如果赋值为常量小数，那么需要在小数后面加F。**
>
> **char类型：使用单引号''**
>
> **String类型：使用双引号""**

3、可以使用其他变量或者表达式给变量赋值

```java
int m = 1;
int n = m;
        
int x = 1;
int y = 2;
int z = 2 * x + y;
```

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-7-5-变量值的输出)1.7.5 变量值的输出

```java
//输出变量的值
System.out.println(age);

//输出变量的值
System.out.println("年龄：" + age);
System.out.println("age：" + age);
System.out.println("name" + name + ",age = " + age + "，gender = " + gender + ",weight = " + weight + ",marry = " + marry);
```

> 如果()中有多项内容，那么必须使用 + 连接起来
>
> 如果某些内容想要原样输出，就用""引起来，而要输出变量中的内容，则不要把变量名用""引起来

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-7-6-变量可以反复赋值)1.7.6 变量可以反复赋值

- 变量的第一次赋值称为初始化；
- 变量的再赋值称为修改变量的值；

```java
//先声明，后初始化
char gender;
gender = '女';

//声明的同时初始化
int age = 18;
System.out.println("age = " + age);///age = 18

//给变量重新赋值，修改age变量的值
age = 19;
System.out.println("age = " + age);//age = 19
```

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-7-7-变量的三要素)1.7.7 变量的三要素

1、数据类型

- 变量的数据类型决定了在内存中开辟多大空间
- 变量的数据类型也决定了该变量可以存什么值

2、变量名

- 见名知意非常重要

3、值

- 基本数据类型的变量：存储数据值
- 引用数据类型的变量：存储地址值，即对象的首地址。例如：String类型的变量存储的是字符串对象的首地址（关于对象后面章节再详细讲解）

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-7-8-变量的使用应该注意什么)1.7.8 变量的使用应该注意什么？

1、先声明后使用

```java
int age;
System.out.println(age); // 报错，原因是变量age没有赋值
```

> 如果没有声明，会报“找不到符号”错误

2、在使用之前必须初始化

> 如果没有初始化，会报“未初始化”错误

3、变量有作用域

> 如果超过作用域，也会报“找不到符号”错误

4、在同一个作用域中不能重名

5、变量值的类型必须与变量声明的类型一致或兼容（<=）

```java
一致：一样
int age = 18;  18是int类型的常量值，age也是int类型

    
兼容：可以装的下，=右边的值要 小于等于 =左边的变量类型
long bigNum =18; 18是int类型的常量值，bigNum是long类型
int < long

int age = 18L; 错误  18L是long类型的常量值，age是int类型
long > int
```

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-7-9-变量的作用域)1.7.9 变量的作用域

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#什么是变量作用域)什么是变量作用域

作用域就是变量的有效范围。变量的作用域是怎样的呢？用一句大白话就可以概括了：出了大括号就不认识了。

```java
public class MyClass {
    static int e = 100;
    public static void main(String[] args){
        int i = 100;
        System.out.println(i);
        for(int k = 0; k < 10; i++){
            int f = 100;
        }
        // 这里是无法访问f变量的
        System.out.println(f);

        // 这里是可以访问e的
        System.out.println(e);
    }
    public static void m(){
        // 这里无法访问main方法中的i
        System.out.println(i);
    }
}
```

![image-20230530192428689](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301924884.png)

作用域的不同主要是因为声明在不同位置的变量具有不同的`生命周期`。所谓的生命周期是：**从内存开辟到内存释放**。

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#java的就近原则)Java的就近原则

```java
public class MyClass {
    
    static int num = 10;
    
    public static void main(String[] args){
        int num = 200;
        // 输出结果是200，这就是就近原则。
        System.out.println(num);
    }
    
}
```

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-7-10-变量的分类)1.7.10 变量的分类

Java中的变量可以按照作用域的不同划分为以下几类：

> 1. 局部变量：定义在方法、语句块、形式参数中的变量。
> 2. 成员变量：定义在类中，但在方法之外的变量。
>    1. 静态变量：使用static关键字定义的变量。
>    2. 实例变量：没有使用static关键字定义的变量。

## [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-8-最终变量-常量-final)1.8 最终变量/常量（final）

最终变量习惯上也称为`常量`，因为它是通过在声明变量的数据类型前面加`final`的方式实现的，所以叫最终变量。加`final`修饰后，这个变量的值就不能修改了，一开始赋值多少，就是多少，所以此时的变量名通常称为常量名。常量名通常所有字母都大写，每一个单词之间使用下划线分割，从命名上和变量名区分开来。

这样做的好处，就是可以见名知意，便于维护。

```java
public class FinalVariableDemo {
	public static void main(String[] args){
        //定义常量
        final int FULL_MARK = 100;//满分
       // FULL_MARK = 150;//错误，final修饰的变量，是常量，不能重新赋值
        
        //输出常量值
        System.out.println("满分：" + FULL_MARK);
        
        //小王的成绩比满分少1分
        int wang = FULL_MARK - 1;
        //小尚得了满分
        int shang = FULL_MARK;
        //小刘得了一半分
        int liu = FULL_MARK/2;
        
        //输出变量值
        System.out.println("小王成绩：" + wang);
        System.out.println("小李成绩：" + shang);
        System.out.println("小刘成绩：" + liu);
	}
}
```

## [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-9-计算机如何存储数据)1.9 计算机如何存储数据

> 计算机世界中只有二进制。那么在计算机中存储和运算的所有数据都要转为二进制。包括数字、字符、图片、声音、视频等。

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-9-1-进制-了解)1.9.1 进制（了解）

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1、进制的分类)1、进制的分类

1. 十进制：

   - 数字组成：0-9
   - 进位规则：逢十进一

2. 二进制：

   - 数字组成：0-1
   - 进位规则：逢二进一

   > 十进制的256，二进制：100000000，为了缩短二进制的表示，又要贴近二进制，在程序中引入八进制和十六进制

3. 八进制：很少使用

   - 数字组成：0-7
   - 进位规则：逢八进一

   > 与二进制换算规则：每三位二进制是一位八进制值

4. 十六进制

   - 数字组成：0-9，a-f
   - 进位规则：逢十六进一

> 与二进制换算规则：每四位二进制是一位十六进制值

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_2、进制的换算)2、进制的换算

| 十进制 | 二进制 | 八进制 | 十六进制 |
| ------ | ------ | ------ | -------- |
| 0      | 0      | 0      | 0        |
| 1      | 1      | 1      | 1        |
| 2      | 10     | 2      | 2        |
| 3      | 11     | 3      | 3        |
| 4      | 100    | 4      | 4        |
| 5      | 101    | 5      | 5        |
| 6      | 110    | 6      | 6        |
| 7      | 111    | 7      | 7        |
| 8      | 1000   | 10     | 8        |
| 9      | 1001   | 11     | 9        |
| 10     | 1010   | 12     | a或A     |
| 11     | 1011   | 13     | b或B     |
| 12     | 1100   | 14     | c或C     |
| 13     | 1101   | 15     | d或D     |
| 14     | 1110   | 16     | e或E     |
| 15     | 1111   | 17     | f或F     |
| 16     | 10000  | 20     | 10       |

- **十进制数据转成二进制数据：**使用除以2倒取余数的方式 ![img](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904125.jpg)

- **二进制数据转成十进制数据：**

  从右边开始依次是2的0次，2的1次，2的2次。。。。

  ![img](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904620.jpg)

- 二进制数据转八进制数据

   从右边开始，三位一组

  ![img](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904645.png)

- 二进制数据转十六进制数据

   从右边开始，四位一组

  ![img](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904665.png)

##### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#十进制转换为二进制)十进制转换为二进制

要将一个十进制数转换为二进制数，可以使用以下步骤：

1. 将十进制数除以2，得到商和余数。
2. 将余数记录下来，然后将商作为新的十进制数，重复步骤1，直到商为0为止。
3. 将记录的余数从下往上排列，得到的就是对应的二进制数。

例如，将十进制数27转换为二进制数： 27 ÷ 2 = 13 ... 1 13 ÷ 2 = 6 ... 1 6 ÷ 2 = 3 ... 0 3 ÷ 2 = 1 ... 1 1 ÷ 2 = 0 ... 1 所以27的二进制数为11011。

##### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#二进制转换为十进制)二进制转换为十进制

将二进制数每一位权值找出来，然后每个权值与对应二进制位相乘，最后将它们相加，即可得到十进制数。

什么是权值？ 在二进制中，权值指的是每个位所代表的数值大小，即二进制中每个位的位置所代表的数值大小。例如，在二进制数1101中，最高位的权值为8，次高位的权值为4，第三位的权值为2，最低位的权值为1。

例如，二进制数1101转换为十进制数的计算过程如下： 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 0 + 1 = 13 因此，二进制数1101转换为十进制数为13。

##### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#练习一下)练习一下

将以下十进制的数字转换为二进制：

- 243：11110011
- 165
- 89

将以下二进制的数字转换为十进制：

- 101010
- 111100
- 011001

##### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#十进制转换为八进制)十进制转换为八进制

将十进制数除以8，直到商为0，然后将每次的余数从下往上排列即为该十进制数的八进制表示。 例如，将十进制数27转换为八进制： 27 ÷ 8 = 3 … 3 3 ÷ 8 = 0 … 3 所以27的八进制表示为33。

##### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#八进制转换为十进制)八进制转换为十进制

八进制转换为十进制的方法如下：

1. 将八进制数的每一位按权展开，权值分别为8的0次方、8的1次方、8的2次方，以此类推。
2. 将每一位的值乘以对应的权值，然后将所有结果相加。

例如，将八进制数 346 转换为十进制数： 3×8^2 + 4×8^1 + 6×8^0 = 3×64 + 4×8 + 6×1 = 198 因此，八进制数 346 转换为十进制数为 198。

##### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#十进制转换为十六进制)十进制转换为十六进制

1. 首先将十进制数除以16，得到商和余数。
2. 将余数转换为对应的十六进制数，如果余数小于10，则直接写下来，否则用A、B、C、D、E、F表示10、11、12、13、14、15。
3. 将商作为新的十进制数，重复步骤1和2，直到商为0为止。
4. 将每一步得到的十六进制数倒序排列，即为最终的十六进制数。

例如，将十进制数255转换为十六进制数：

1. 255 ÷ 16 = 15 余 15
2. 余数15对应的十六进制数为F，所以最后一位为F。
3. 15 ÷ 16 = 0 余 15
4. 余数15对应的十六进制数为F，所以第二位为F。
5. 最终的十六进制数为FF。

##### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#十六进制转换为十进制)十六进制转换为十进制

将十六进制转换为十进制的方法是将每一位的十六进制数值乘以对应的权值，再将各位的结果相加。 例如，将十六进制数ABCD转换为十进制数：

1. 将A、B、C、D分别转换为对应的十进制数值，即10、11、12、13。
2. 根据十六进制的权值规则，从右往左依次乘以16的0次方、1次方、2次方、3次方，即1、16、256、4096。
3. 将各位的乘积相加，即：13×1 + 12×16 + 11×256 + 10×4096 = 43981。
4. 所以，十六进制数ABCD转换为十进制数为43981。

另一种简便的方法是，将十六进制数中的每一位转换为4位的二进制数，再将这些二进制数转换为十进制数，最后将各位的结果相加。

##### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#二进制转换为十六进制)二进制转换为十六进制

二进制转换为十六进制的方法如下：

1. 将二进制数从右往左每四位一组，不足四位则在左侧补0，得到若干个四位二进制数。
2. 将每个四位二进制数转换为对应的十六进制数，可以使用下表进行转换：

| 二进制数 | 十六进制数 |
| -------- | ---------- |
| 0000     | 0          |
| 0001     | 1          |
| 0010     | 2          |
| 0011     | 3          |
| 0100     | 4          |
| 0101     | 5          |
| 0110     | 6          |
| 0111     | 7          |
| 1000     | 8          |
| 1001     | 9          |
| 1010     | A          |
| 1011     | B          |
| 1100     | C          |
| 1101     | D          |
| 1110     | E          |
| 1111     | F          |

1. 将每个四位二进制数对应的十六进制数按照从左往右的顺序排列，得到最终的十六进制数。

例如，将二进制数1101011010111011转换为十六进制数：

1. 从右往左每四位一组，得到1101 0110 1011 1011。
2. 将每个四位二进制数转换为对应的十六进制数，得到D 6 B B。
3. 将每个四位二进制数对应的十六进制数按照从左往右的顺序排列，得到最终的十六进制数：D6BB。

##### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#十六进制转换为二进制)十六进制转换为二进制

将每个十六进制数位转换为四位二进制数即可。 例如：将十六进制数 AF 转换为二进制数。 A 对应的二进制数为 1010，F 对应的二进制数为 1111，因此 AF 对应的二进制数为 10101111

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_3、在代码中如何表示四种进制的常量值)3、在代码中如何表示四种进制的常量值

请分别用四种类型的进制来表示10，并输出它的结果：（了解）

- 十进制：正常表示

  System.out.println(10);

- 二进制：0b或0B开头

  System.out.println(0B10);

- 八进制：0开头

  System.out.println(010);

- 十六进制：0x或0X开头

  System.out.println(0X10);

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-9-2-计算机存储单位-掌握)1.9.2 计算机存储单位（掌握）

- **字节（Byte）：**是计算机信息技术用于计量存储容量的一种计量单位，一字节等于八位。
- **位（bit）：**是数据存储的最小单位。也就是二进制。二进制数系统中，每个0或1就是一个位，叫做bit（比特），其中8 bit 就称为一个字节(Byte)。
- **转换关系：**
  - 8 bit = 1 Byte
  - 1024 Byte = 1 KB
  - 1024 KB = 1 MB
  - 1024 MB = 1 GB
  - 1024 GB = 1 TB

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-9-3-java的基本数据类型的存储范围-掌握)1.9.3 Java的基本数据类型的存储范围（掌握）

![img](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904683.jpg)

> float：单精度浮点型，占内存：4个字节，精度：科学记数法的小数点后6~7位
>
> double：双精度浮点型，占内存：8个字节，精度：科学记数法的小数点后15~16位

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-9-4-计算机如何表示数据-理解)1.9.4 计算机如何表示数据（理解）

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1、如何表示boolean类型的值)1、如何表示boolean类型的值

`true`底层使用`1`表示。

`false`底层使用`0`表示。

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_2、如何表示整数)2、如何表示整数？

##### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#原码反码补码)原码反码补码

原码、反码和补码都是计算机二进制的表示方式。在这三种编码方式中，原码是最简单的，也是最直接的表示方式；反码可以解决原码在计算过程中的问题；补码可以解决反码在计算过程中的问题。 **计算机在底层是采用补码形式表示数据的。** 在二进制当中，最高位表示符号位，0表示正数，1表示负数。

> *规定：正数的补码与反码、原码一样，称为三码合一；*
>
>  **负数的补码与反码、原码不一样：**
>
>  负数的原码：把十进制 转为二进制，然后最高位设置为1
>
>  负数的反码：在原码的基础上，最高位不变，其余位取反（0变1,1变0）
>
>  负数的补码：反码+1
>
> ```
> 例如：byte类型（1个字节，8位）
> ```
>
> 25 ==> 原码 0001 1001 ==> 反码 0001 1001 -->补码 0001 1001
>
> -25 ==>原码 1001 1001 ==> 反码1110 0110 ==>补码 1110 011
>
> ```
> 正数的原码反码补码
> ```
>
> 正数的原码、反码和补码都是相同的。 例如，一个十进制数+5的二进制原码为00000101，反码为00000101，补码为00000101。 原码：将正数的二进制表示直接写下来，最高位为0。 反码：正数的反码就是其原码本身。 补码：正数的补码也就是其原码本身。
>
> ```
> 127的原码反码补码
> ```
>
> 127的原码为01111111，其反码和补码均与原码相同。
>
> ```
> 负数的原码反码补码
> ```
>
> **负数的原码运算规则：将绝对值转换为二进制后，最高位改为1。** -5的原码：10000101 -5的反码：11111010（原则是：以原码作为参考，符号位不变，其他位取反。） -5的补码：11111011（原则是：以反码作为参考，符号位不变，加1）
>
> ```
> -128的原码反码补码
> ```
>
> -128的原码为10000000，其反码为11111111，补码为10000000。注意，对于-128这个特殊的数，它的补码和原码相同。

```java
整数：
正数：25   00000000 00000000 000000000 00011001（原码）
正数：25   00000000 00000000 000000000 00011001（反码）
正数：25   00000000 00000000 000000000 00011001（补码）

负数：-25  10000000 00000000 000000000 00011001（原码）
负数：-25  11111111 11111111 111111111 11100110（反码）
负数：-25  11111111 11111111 111111111 11100111（补码）
```

##### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#计算机底层为什么采用补码)计算机底层为什么采用补码

算机采用补码形式进行数值计算的原因有以下几点：

1. 可以简化电路设计：采用补码形式可以将加减法运算转化为相同的操作，从而简化电路设计。
2. 解决了0的正负问题：在原码中，0有两个表示，+0和-0，这样会导致计算结果不唯一，而在补码中，0只有一种表示，即全0，可以避免这个问题。
3. 解决了负数溢出问题：在原码中，负数的表示范围比正数少1，这样在进行减法运算时容易出现负数溢出的情况，而在补码中，负数的表示范围与正数相同，可以避免负数溢出的问题。
4. 方便计算机进行运算：补码形式可以方便计算机进行加减法运算，而且可以使用相同的电路进行运算，从而提高了计算机的运算效率。

> 下面是一个简单的数据演示： 假设我们要计算-3+2的结果，使用原码进行计算： -3的原码为10000011，2的原码为00000010，进行加法运算得到的结果为10000101，转换成十进制为-5，这个结果是错误的。 使用补码进行计算： -3的补码为11111101，2的补码为00000010，进行加法运算得到的结果为11111111，转换成十进制为-1，这个结果是正确的。

##### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#一个字节可以存储的整数范围是多少)一个字节可以存储的整数范围是多少？

```java
1个字节：8位

0000 0001  ~  0111 111 ==> 1~127

1000 0001 ~ 1111 1111 ==> -127 ~ -1

0000 0000 ==>0

1000 0000 ==> -128（特殊规定）=-127-1
```

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_3、如何表示小数)3、如何表示小数？

了解小数如何存储是为了理解如下问题：

- 为什么float（4个字节）比long（8个字节）的存储范围大？
- 为什么float和double不精确？
- 为什么double（8个字节）比float（4个字节）精度范围大？

因为float、double底层也是二进制，先把小数转为二进制，然后把二进制表示为科学记数法，然后只保存：

①符号位②指数位（需要移位）③尾数位

```java
float：符号位（1位），指数位（8位，偏移127），尾数位（23位）
double：符号位（1位），指数位（11位，偏移1023），尾数为（52位）
float指数-126~+127
double指数-1022~+1023

float类型
小数：8.25 1000.01
           1.00001（科学计数法）
		   符号位0，指数位3+127（偏移量）=130->10000010，尾数00001
		   0 10000010 00001000000000000000000  原码
		   0 10000010 00001000000000000000000  反码
		   0 10000010 00001000000000000000000  补码
		   
小数：-8.25 -1000.01（原码）
		   1 10000010 00001000000000000000000  原码
		   1 01111101 11110111111111111111111  反码
		   1 01111101 11111000000000000000000  补码
		     
double类型：
小数：8.25 1000.01
           1.00001（科学计数法）
		   符号位0，指数位3+1023（偏移量）=1026->10000000010，尾数00001
		   0 10000000010  0000 10000000 00000000 00000000 00000000 00000000 00000000 原码
		   0 10000000010  0000 10000000 00000000 00000000 00000000 00000000 00000000 反码
		   0 10000000010  0000 10000000 00000000 00000000 00000000 00000000 00000000 补码
		   
double类型：
小数：-8.25 -1000.01（原码）
           1.00001（科学计数法）
		   符号位0，指数位3+1023（偏移量）=1026->10000000010，尾数00001
		   1 10000000010  0000 10000000 00000000 00000000 00000000 00000000 00000000 原码
		   1 01111111101  1111 01111111 11111111 11111111 11111111 11111111 11111111 反码
		   1 01111111101  1111 10000000 00000000 00000000 00000000 00000000 00000000 补码
		   
为什么float类型指数位偏移127，double类型指数位偏移1023。
因为指数+3，偏移127就是130		   
因为指数-3，偏移127就是124
130>124，比较大小比较方便。
```

![image-20211217160508390](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904706.png)

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_4、java程序中如何表示和处理单个字符)4、Java程序中如何表示和处理单个字符？

（1）使用单引号将单个字符引起来：例如：'A'，'0'，'尚'

```java
char c = '尚';//使用单引号
String s = '尚';//错误的，哪怕是一个字符，也要使用双引号
		
char kongChar = '';//错误，单引号中有且只能有一个字符
String kongStr = "";//可以，双引号中可以没有其他字符，表示是空字符串
```

（2）特殊的转义字符

```java
\n：换行
\r：回车
\t：Tab键
\\：\
\"："
\'：'
\b：删除键Backspace
public class TestEscapeCharacter {
    public static void main(String[] args){
        System.out.println("hello\tjava");
        System.out.println("hello\rjava");
        System.out.println("hello\njava");
        System.out.println("hello\\world");
        System.out.println("\"hello\"");
        char shuang = '"';
        System.out.println(shuang + "hello" + shuang);
        System.out.println("'hello'");
        char dan ='\'';
        System.out.println(dan + "hello" + dan);
    }
}
public class TestTab {
    public static void main(String[] args){
        System.out.println("hello\tworld\tjava.");
        System.out.println("chailinyan\tis\tbeautiful.");
        System.out.println("姓名\t基本工资\t年龄");
        System.out.println("张三\t10000.0\t23");
    }
}
```

（3）用十进制的0~65535之间的Unicode编码值，表示一个字符

在JVM内存中，一个字符占2个字节，Java使用Unicode字符集来表示每一个字符，即每一个字符对应一个唯一的Unicode编码值。char类型的数值参与算术运算或比较大小时，都是用编码值进行计算的。

| 字符 | Unicode编码值 |
| ---- | ------------- |
| '0'  | 48            |
| '1'  | 49            |
| 'A'  | 65            |
| 'B'  | 66            |
| 'a'  | 97            |
| 'b'  | 98            |
| '尚' | 23578         |

```java
char c1 = 23578;
System.out.println(c1);//尚

char c2 = 97;
System.out.println(c2);//a

//如何查看某个字符的Unicode编码？
//将一个字符赋值给int类型的变量即可
int codeOfA = 'A';
System.out.println(codeOfA);

int codeOfShang = '尚';
System.out.println(codeOfShang);

int codeOfTab = '\t';
System.out.println(codeOfTab);
```

（4）\u字符的Unicode编码值的十六进制型

例如：'\u5c1a'代表'尚'

```java
char c = '\u0041'; //十进制Unicode值65，对应十六进制是41，但是\u后面必须写4位
char c = '\u5c1a'; //十进制Unicode值23578，对应十六进制是5c1a
```

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_5、一个字符到底占几个字节)5、一个字符到底占几个字节？

在JVM内存中，一个字符占2个字节，Java使用Unicode字符集来表示每一个字符，即每一个字符对应一个唯一的Unicode编码值。char类型的数值参与算术运算或比较大小时，都是用编码值进行计算的。

在文件中保存或网络中传输时文本数据时，和环境编码有关。如果环境编码选择ISO8859-1（又名Latin），那么一个字符占一个字节；如果环境编码选择GBK，那么一个字符占1个或2个字节；如果环境编码选择UTF-8，那么一个字符占1-4个字节。（后面讲String类时再详细讲解）

## [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-10-运算符-operator-和标点符号-separators-掌握)1.10 运算符（Operator）和标点符号（Separators）（掌握）

在Java中，一共有38个运算符。

![image-20210701164724830](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904086.png)

运算符的分类：

- 按照功能分：算术运算符、赋值运算符、比较运算符、逻辑运算、条件运算符、Lambda运算符

|        分类         |                        运算符                        |
| :-----------------: | :--------------------------------------------------: |
|  算术运算符（7个）  |                +、-、*、/、%、++、--                 |
| 赋值运算符（12个）  | =、+=、-=、*=、/=、%=、>>=、<<=、>>>=、&=、\|=、^=等 |
|  关系运算符（6个）  |                 >、>=、<、<=、==、!=                 |
|  逻辑运算符（6个）  |                &、\|、^、!、&&、\|\|                 |
|  条件运算符（2个）  |               (条件表达式)?结果1:结果2               |
|   位运算符（7个）   |               &、\|、^、~、<<、>>、>>>               |
| Lambda运算符（1个） |                     ->（后面学）                     |

- 按照操作数个数分：一元运算符（单目运算符）、二元运算符（双目运算符）、三元运算符 （三目运算符）

|           分类            |                  运算符                  |
| :-----------------------: | :--------------------------------------: |
| 一元运算符（单目运算符）  |    正号（+）、负号（-）、++、--、!、~    |
| 二元运算符（双目运算符）  | 除了一元和三元运算符剩下的都是二元运算符 |
| 三元运算符 （三目运算符） |         (条件表达式)?结果1:结果2         |

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-10-1-算术运算符)1.10.1 算术运算符

|  算术运算符  |            符号解释             |
| :----------: | :-----------------------------: |
|     `+`      | 加法运算，字符串连接运算，正号  |
|     `-`      |         减法运算，负号          |
|     `*`      |            乘法运算             |
|     `/`      | 除法运算，整数/整数结果还是整数 |
|     `%`      | 求余运算，余数的符号只看被除数  |
| `++` 、 `--` |          自增自减运算           |

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1、加减乘除模)1、加减乘除模

```java
public class OperatorDemo01 {
	public static void main(String[] args) {
		int a = 3;
		int b = 4;
		
		System.out.println(a + b);// 7
		System.out.println(a - b);// -1
		System.out.println(a * b);// 12
		System.out.println(a / b);// 计算机结果是0，为什么不是0.75呢？
		System.out.println(a % b);// 3
        
        System.out.println(5%2);//1
		System.out.println(5%-2);//1
		System.out.println(-5%2);//-1
		System.out.println(-5%-2);//-1		
		//商*除数 + 余数 = 被除数
		//5%-2  ==>商是-2，余数时1    (-2)*(-2)+1 = 5
		//-5%2  ==>商是-2，余数是-1   (-2)*2+(-1) = -4-1=-5
	}
}
```

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_2、-号的两种用法)2、“+”号的两种用法

- 第一种：对于`+`两边都是数值的话，`+`就是加法的意思
- 第二种：对于`+`两边至少有一边是字符串得话，`+`就是拼接的意思

```java
public class OperatorDemo02 {
	public static void main(String[] args) {
		// 字符串类型的变量基本使用
		// 数据类型 变量名称 = 数据值;
		String str1 = "Hello";
		System.out.println(str1); // Hello
		
		System.out.println("Hello" + "World"); // HelloWorld
		
		String str2 = "Java";
		// String + int --> String
		System.out.println(str2 + 520); // Java520
		// String + int + int
		// String		+ int
		// String
		System.out.println(str2 + 5 + 20); // Java520
	}
}
```

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_3、自加自减运算)3、自加自减运算

**理解：**`++` **运算，变量自己的值加1**。反之，`--` 运算，变量自己的值减少1，用法与`++` 一致。

1、单独使用

- 变量在单独运算的时候，变量`前++`和变量`后++`，变量的是一样的；
- 变量`前++` ：例如 `++a` 。
- 变量`后++` ：例如 `a++` 。

```java
public class OperatorDemo3 {
	public static void main(String[] args) {
		// 定义一个int类型的变量a
		int a = 3;
		//++a;
		a++;
        // 无论是变量前++还是变量后++，结果都是4
		System.out.println(a);
	}
}
```

2、复合使用

- 和`其他变量放在一起使用`或者和`输出语句放在一起使用`，`前++`和`后++`就产生了不同。

- 变量`前++` ：变量先自身加1，然后再取值。
- 变量`后++` ：变量先取值，然后再自身加1。

```java
public class OperatorDemo03 {
	public static void main(String[] args) {
		// 其他变量放在一起使用
		int x = 3;
		//int y = ++x; // y的值是4，x的值是4，
		int y = x++; // y的值是3，x的值是4
		
		System.out.println(x);
		System.out.println(y);
		System.out.println("==========");
        
		// 和输出语句一起
		int z = 5;
		//System.out.println(++z);// 输出结果是6，z的值也是6
		System.out.println(z++);// 输出结果是5，z的值是6
		System.out.println(z);
        
        int a = 1;
        a = a++;//(1)先取a的值“1”放操作数栈(2)a再自增,a=2(3)再把操作数栈中的"1"赋值给a,a=1

        int i = 1;
        int j = i++ + ++i * i++;
        /*
        从左往右加载
        (1)先算i++
        ①取i的值“1”放操作数栈
        ②i再自增 i=2
        （2）再算++i
        ①i先自增 i=3
        ②再取i的值“3”放操作数栈
        （3）再算i++
        ①取i的值“3”放操作数栈
        ②i再自增 i=4
        （4）先算乘法
        用操作数栈中3 * 3 = 9，并把9压会操作数栈
        （5）再算求和
        用操作数栈中的 1 + 9 = 10
        （6）最后算赋值
        j = 10
        */
	} 
}
```

- 小结：
  - **++在前，先自加，后使用；**
  - **++在后，先使用，后自加。**

- 分析

```java
public class TestIncrementOperator1{
	public static void main(String[] args){
		int i = 1;
		i++;
		++i;
	}
}
```

![image-20211217171149646](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904200.png)

```java
public class TestIncrementOperator2{
	public static void main(String[] args){
		int i = 1;
		i = i++;
	}
}
```

![image-20211217171321005](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904221.png)

```java
public class TestIncrementOperator3{
	public static void main(String[] args){
		int i = 1;
		i = ++i;
	}
}
```

![image-20211217171420955](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904241.png)

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-10-2-关系运算符-比较运算符)1.10.2 关系运算符/比较运算符

| 关系运算符 |                           符号解释                           |
| :--------: | :----------------------------------------------------------: |
|    `<`     |  比较符号左边的数据是否小于右边的数据，如果小于结果是true。  |
|    `>`     |  比较符号左边的数据是否大于右边的数据，如果大于结果是true。  |
|    `<=`    | 比较符号左边的数据是否小于或者等于右边的数据，如果大于结果是false。 |
|    `>=`    | 比较符号左边的数据是否大于或者等于右边的数据，如果小于结果是false。 |
|    `==`    |          比较符号两边数据是否相等，相等结果是true。          |
|   `！=`    |     不等于符号 ，如果符号两边的数据不相等，结果是true。      |

- 比较运算符，是两个数据之间进行比较的运算，运算结果一定是boolean值`true`或者`false` 。
- 其中>,<,>=,<=不支持boolean，String类型，==和!=支持boolean和String。

```java
public class OperatorDemo05 {
	public static void main(String[] args) {
		int a = 3;
		int b = 4;

		System.out.println(a < b); // true
		System.out.println(a > b); // false
		System.out.println(a <= b); // true
		System.out.println(a >= b); // false
		System.out.println(a == b); // false
		System.out.println(a != b); // true
	}
}
```

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-10-3-逻辑运算符)1.10.3 逻辑运算符

- 逻辑运算符，是用来连接两个布尔类型值的运算符（`!`除外），运算结果也是boolean值`true`或者`false`

| 逻辑运算符 |   符号解释   |               符号特点               |
| :--------: | :----------: | :----------------------------------: |
|    `&`     |    与，且    |          有`false`则`false`          |
|    `|`     |      或      |           有`true`则`true`           |
|    `^`     |     异或     |     相同为`false`，不同为`true`      |
|    `!`     |      非      | 非`false`则`true`，非`true`则`false` |
|    `&&`    | 双与，短路与 |      左边为false，则右边就不看       |
|    `||`    | 双或，短路或 |       左边为true，则右边就不看       |

&&和&区别，||和|区别：

- **

  ```
  &&
  ```

  和

  ```
  &
  ```

  **区别：

  - `&&`和`&`结果一样，`&&`有短路效果，左边为false，右边不执行；`&`左边无论是什么，右边都会执行。

- **

  ```
  ||
  ```

  和

  ```
  |
  ```

  **区别：

  - `||`和`|`结果一样，`||`有短路效果，左边为true，右边不执行；`|`左边无论是什么，右边都会执行。

```java
public class OperatorDemo06 {
	public static void main(String[] args) {
		int a = 3;
		int b = 4;
		int c = 5;

		// & 与，且；有false则false
		System.out.println((a > b) & (a > c)); 
		System.out.println((a > b) & (a < c)); 
		System.out.println((a < b) & (a > c)); 
		System.out.println((a < b) & (a < c)); 
		System.out.println("===============");
		// | 或；有true则true
		System.out.println((a > b) | (a > c)); 
		System.out.println((a > b) | (a < c)); 
		System.out.println((a < b) | (a > c));
		System.out.println((a < b) | (a < c));
		System.out.println("===============");
		// ^ 异或；相同为false，不同为true
		System.out.println((a > b) ^ (a > c));
		System.out.println((a > b) ^ (a < c)); 
		System.out.println((a < b) ^ (a > c)); 
		System.out.println((a < b) ^ (a < c)); 
		System.out.println("===============");
		// ! 非；非false则true，非true则false
		System.out.println(!false);
		System.out.println(!true);
        
        //&和&&的区别
        System.out.println((a > b) & (a++ > c)); 
        System.out.println("a = " + a);
        System.out.println((a > b) && (a++ > c)); 
        System.out.println("a = " + a);
        System.out.println((a == b) && (a++ > c)); 
        System.out.println("a = " + a);
        
        //|和||的区别
        System.out.println((a > b) | (a++ > c)); 
        System.out.println("a = " + a);
        System.out.println((a > b) || (a++ > c)); 
        System.out.println("a = " + a);
        System.out.println((a == b) || (a++ > c)); 
        System.out.println("a = " + a);
	}
}
/*
3、逻辑运算符
逻辑与：&
	true & true 结果是true
	true & false 结果是false
	false & true 结果是false
	false & false 结果是false
	
	只有两个边都是true，结果才为true。

逻辑或：|
	true | true 结果是true
	true | false 结果是true
	false | true 结果是true
	false | false 结果是false
	
	只要有一边是true，结果就为true。
	
逻辑非：!
	!true  变为false
	!false 变为true
	
逻辑异或：^
	true | true 结果是false
	true | false 结果是true
	false | true 结果是true
	false | false 结果是false
	
	只有两边不一样，一个是true，一个是false，结果才为true。
	
短路与：&&
	true && true 结果是true
	true && false 结果是false
	false && ? 结果是false
	false && ? 结果是false
	
	只有两个边都是true，结果才为true。
	但是它如果左边已经是false，右边不看。这样的好处就是可以提高效率。

	
短路或：||
	true || ？ 结果是true
	true || ？ 结果是true
	false || true 结果是true
	false || false 结果是false
	
	只要有一边是true，结果就为true。
	但是它如果左边已经是true，右边就不看了。这样的好处就是可以提高效率。

特殊：
（1）逻辑运算符的操作数必须是boolean值
（2）逻辑运算符的结果也是boolean值

*/
public class LogicOperator{
	public static void main(String[] args){
		/*
		表示条件，成绩必须在[0,100]之间
		成绩是int类型变量score
		*/
		int score = 56;
		
		//System.out.println(0<=score<=100);
		/*
		LogicOperator.java:23: 错误: 二元运算符 '<=' 的操作数类型错误
                System.out.println(0<=score<=100);
                                           ^
		  第一个类型:  boolean    0<=score的结果 true
		  第二个类型: int
		  
		  true <= 100？不对的
		1 个错误*/
		
		System.out.println(0<=score  & score<=100);
		
	}
}
```

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-10-4-条件运算符)1.10.4 条件运算符

- 条件运算符格式：

```java
条件表达式？结果1：结果2
```

- 条件运算符计算方式：
  - 条件判断的结果是true，条件运算符整体结果为结果1，赋值给变量。
  - 判断条件的结果是false，条件运算符整体结果为结果2，赋值给变量。

```java
public static void main(String[] args) {
    int i = (1==2 ? 100 : 200);
    System.out.println(i);//200
    int j = (3<=4 ? 500 : 600);
    System.out.println(j);//500
}
public class ConditionOperator{
	public static void main(String[] args){
		//判断两个变量a,b谁大，把大的变量赋值给max
		int a = 2;
		int b = 2;
		int max = a >= b ? a : b;
		//如果a>=b成立，就取a的值赋给max，否则取b的值赋给max
		System.out.println(max);
		
		boolean marry = false;
		System.out.println(marry ? "已婚" : "未婚"  );
	}
}
```

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-10-5-位运算符)1.10.5 位运算符

| 位运算符 |                    符号解释                    |
| :------: | :--------------------------------------------: |
|   `&`    |        按位与，当两位相同时为1时才返回1        |
|   `|`    |         按位或，只要有一位为1即可返回1         |
|   `~`    | 按位非，将操作数的每个位（包括符号位）全部取反 |
|   `^`    |    按位异或。当两位相同时返回0，不同时返回1    |
|   `<<`   |                   左移运算符                   |
|   `>>`   |                   右移运算符                   |
|  `>>>`   |                无符号右移运算符                |

- 位运算符的运算过程都是基于补码运算，但是看结果，我们得换成原码，再换成十进制看结果
- 从二进制到十进制都是基于原码
- 正数的原码反码补码都一样，负数原码反码补码不一样
- byte,short,char在计算时按照int类型处理

> 如何区分&,|,^是逻辑运算符还是位运算符？
>
> 如果操作数是boolean类型，就是逻辑运算符，如果操作数是整数，那么就位运算符。

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-左移)（1）左移：<<

 运算规则：左移几位就相当于乘以2的几次方

 **注意：**当左移的位数n超过该数据类型的总位数时，相当于左移（n-总位数）位

 byte,short,char在计算时按照int类型处理

```java
3<<4  类似于  3*2的4次= 3*16 = 48
```

![image-20200225113651675](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904262.png)

```java
-3<<4  类似于  -3*2的4次= -3*16 = -48
```

![image-20200225114707524](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904315.png)

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_2-右移)（2）右移：>>

快速运算：类似于除以2的n次，如果不能整除，**向下取整**

```java
69>>4  类似于  69/2的4次 = 69/16 =4
```

![image-20200225115636844](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904616.png)

```text
-69>>4  类似于  -69/2的4次 = -69/16 = -5
```

![image-20200225120112188](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904645.png)

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_3-无符号右移)（3）无符号右移：>>>

运算规则：往右移动后，左边空出来的位直接补0，不看符号位

正数：和右移一样

负数：右边移出去几位，左边补几个0，结果变为正数

```text
69>>>4  类似于  69/2的4次 = 69/16 =4
```

![image-20200225121104734](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904674.png)

```text
-69>>>4   结果：268435451
```

![image-20200225121244290](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904703.png)

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_4-按位与)（4）按位与：&

运算规则：对应位都是1才为1

>  1 & 1 结果为1
>
>  1 & 0 结果为0
>
>  0 & 1 结果为0
>
>  0 & 0 结果为0

```text
9&7 = 1
```

![image-20200225122440953](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904757.png)

```text
-9&7 = 7
```

![image-20200225122221616](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904856.png)

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_5-按位或)（5）按位或：|

运算规则：对应位只要有1即为1

>  1 | 1 结果为1
>
>  1 | 0 结果为1
>
>  0 | 1 结果为1
>
>  0 & 0 结果为0

```text
9|7  结果： 15
```

![image-20200225122758851](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904001.png)

```text
-9|7 结果： -9
```

![image-20200225123409130](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904027.png)

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_6-按位异或)（6）按位异或：^

 运算规则：对应位一个为1一个为0，才为1

>  1 ^ 1 结果为0
>
>  1 ^ 0 结果为1
>
>  0 ^ 1 结果为1
>
>  0 ^ 0 结果为0

```text
9^7  结果为14
```

![image-20200225123445305](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904100.png)

```text
-9^7 结果为-16
```

![image-20200225133145727](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904132.png)

#### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_7-按位取反)（7）按位取反：~

运算规则：~0就是1

>  ~1就是0

```java
~9  结果：-10
```

![image-20200225124112662](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904158.png)

```java
~-9  结果：8
```

![image-20200225124156862](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904298.png)

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-10-6-赋值运算符)1.10.6 赋值运算符

| 运算符 |                           符号解释                           |
| :----: | :----------------------------------------------------------: |
|   =    |      将右边的常量值/变量值/表达式的值，赋值给左边的变量      |
|   +=   | 将左边变量的值和右边的常量值/变量值/表达式的值进行相加，最后将结果赋值给左边的变量 |
|   -=   | 将左边变量的值和右边的常量值/变量值/表达式的值进行相减，最后将结果赋值给左边的变量 |
|   *=   | 将左边变量的值和右边的常量值/变量值/表达式的值进行相乘，最后将结果赋值给左边的变量 |
|   /=   | 将左边变量的值和右边的常量值/变量值/表达式的值进行相除，最后将结果赋值给左边的变量 |
|   %=   | 将左边变量的值和右边的常量值/变量值/表达式的值进行相模，最后将结果赋值给左边的变量 |
|  <<=   | 将左边变量的值左移右边常量/变量值/表达式的值的相应位，最后将结果赋值给左边的变量 |
|  >>=   | 将左边变量的值右移右边常量/变量值/表达式的值的相应位，最后将结果赋值给左边的变量 |
|  >>>=  | 将左边变量的值无符号右移右边常量/变量值/表达式的值的相应位，最后将结果赋值给左边的变量 |
|   &=   | 将左边变量的值和右边的常量值/变量值/表达式的值进行按位与，最后将结果赋值给左边的变量 |
|  \|=   | 将左边变量的值和右边的常量值/变量值/表达式的值进行按位或，最后将结果赋值给左边的变量 |
|   ^=   | 将左边变量的值和右边的常量值/变量值/表达式的值进行按位异或，最后将结果赋值给左边的变量 |

```java
public class OperatorDemo04 {
	public static void main(String[] args) {
		int a = 3;
		int b = 4;
        int c = a + b;        
        
		b += a;// 相当于 b = b + a ; 
		System.out.println(a); // 3
		System.out.println(b); // 7	
        System.out.println(c); //7
		
		short s = 3;
		// s = s + 4; 代码编译报错，因为将int类型的结果赋值给short类型的变量s时，可能损失精度
		s += 4; // 代码没有报错
        //因为在得到int类型的结果后，JVM自动完成一步强制类型转换，将int类型强转成short
		System.out.println(s);
        
        int j = 1;
		j += ++j * j++;//相当于  j = j + (++j * j++);
		System.out.println(j);//5
        
        int m = 1;
        m <<= 2;
        System.out.println(m);
	}
}
```

- 扩展赋值运算符在**将最后的结果赋值给左边的变量前，多做了一步强制类型转换**。
- 注意：所有的赋值运算符的=左边一定是一个变量

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-10-7-运算符优先级)1.10.7 运算符优先级

![1553858424335](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904423.png)

提示说明：

（1）表达式不要太复杂

（2）先算的使用()

> 口诀：
>
> 单目运算排第一；
>
> 乘除余二加减三；
>
> 移位四，关系五；
>
> 等和不等排第六；
>
> 位与、异或和位或；
>
> 短路与和短路或；
>
> 依次从七到十一；
>
> 条件排在第十二；
>
> 赋值一定是最后；

### [#](https://gaoziman.gitee.io/blogs/pages/7263a2/#_1-10-8-标点符号)1.10.8 标点符号

在Java中一共有12个标点符号。（后面再一一学习）

![image-20210701170438577](https://gaoziman.oss-cn-hangzhou.aliyuncs.com/img/202305301904447.png)

- 小括号 () 用于强制类型转换、表示优先运算表达式、方法参数列表
- 大括号 {} 用于数组元素列表、类体、方法体、复合语句代码块边界符
- 中括号 [] 用于数组
- 分号; 用于结束语句
- 逗号,用于多个赋值表达式的分隔符和方法参数列表分隔符
- 英文句号.用于成员访问和包目录结构分隔符
- 英文省略号...用于可变参数
- @用于注解
- 双冒号::用于方法引用

```
各个标点符号的使用在后续章节中一一揭晓。
```