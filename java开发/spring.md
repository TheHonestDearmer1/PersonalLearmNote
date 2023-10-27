## 课程介绍

对于一门新技术，我们需要从`为什么要学`、`学什么`以及`怎么学`这三个方向入手来学习。那对于Spring来说:

### 为什么要学?

- 从使用和占有率看
  - Spring在市场的占有率与使用率高
  - Spring在企业的技术选型命中率高
  - 所以说,Spring技术是JavaEE开发必备技能，企业开发技术选型命中率 > 90%
    **说明**:对于未使用Spring的项目一般都是些比较老的项目，大多都处于维护阶段。
- 从专业角度看
  - 随着时代发展，软件规模与功能都呈几何式增长，开发难度也在不断递增，该如何解决?
    - Spring可以简化开发，降低企业级开发的复杂性，使开发变得更简单快捷
  - 随着项目规模与功能的增长,遇到的问题就会增多，为了解决问题会引入更多的框架，这些框架如何协调工作?
    - Spring可以框架整合，高效整合其他技术，提高企业级应用开发与运行效率
- 综上所述，Spring是一款非常优秀而且功能强大的框架，不仅要学，而且还要学好。

### 学什么?

从上面的介绍中，我们可以看到Spring框架主要的优势是在`简化开发`和`框架整合`上，至于如何实现就是我们要学习Spring框架的主要内容:

- 简化开发

  : Spring框架中提供了两个大的核心技术，分别是:

  - IOC
  - AOP
    - 事务处理

- Spring的简化操作都是基于这两块内容,所以这也是Spring学习中最为重要的两个知识点。

- 事务处理属于Spring中AOP的具体应用，可以简化项目中的事务管理，也是Spring技术中的一大亮点。

- 框架整合

  : Spring在框架整合这块已经做到了极致，它可以整合市面上几乎所有主流框架，比如:

  - MyBatis
  - MyBatis-plus
  - Struts
  - Struts2
  - Hibernate
  - ……

- 这些框架中，我们目前只学习了MyBatis，所以在Spring框架的学习中，主要是学习如何整合MyBatis。

- 综上所述

  ，对于Spring的学习，主要学习四块内容:

  1. IOC
  2. 整合Mybatis(IOC的具体应用)
  3. AOP
  4. 声明式事务(AOP的具体应用)

### 怎么学?

- 学习Spring框架设计思想
  - 对于Spring来说，它能迅速占领全球市场，不只是说它的某个功能比较强大，更重要是在它的`思想`上。
- 学习基础操作，思考操作与思想间的联系
  - 掌握了Spring的设计思想，然后就需要通过一些基础操作来思考操作与思想之间的关联关系
- 学习案例，熟练应用操作的同时，体会思想
  - 会了基础操作后，就需要通过大量案例来熟练掌握框架的具体应用，加深对设计思想的理解。
- 介绍完`为什么要学`、`学什么`和`怎么学`Spring框架后，我们需要重点掌握的是:
  - Spring很优秀，需要认真重点的学习
  - Spring的学习主线是IOC、AOP、声明式事务和整合MyBais
- 接下来，咱们就开始进入Spring框架的学习。

## Spring相关概念

### 初识Spring

#### Spring家族

- 官网：[https://spring.io](https://spring.io/)， 从官网我们可以大概了解到：
  - Spring能做什么:用以开发web、微服务以及分布式系统等,光这三块就已经占了JavaEE开发的九成多。
  - Spring并不是单一的一个技术，而是一个大家族，可以从官网的`Projects`中查看其包含的所有技术。
- Spring发展到今天已经形成了一种开发的生态圈,Spring提供了若干个项目,每个项目用于完成特定的功能。
  - Spring已形成了完整的生态圈，也就是说我们可以完全使用Spring技术完成整个项目的构建、设计与开发。
  - Spring有若干个项目，可以根据需要自行选择，把这些个项目组合起来，起了一个名称叫Spring全家桶，如下图所示

[![](img/630c26bd16f2c2beb1e9ef1e.jpg)](https://pic.imgdb.cn/item/630c26bd16f2c2beb1e9ef1e.jpg)

**说明:**

图中的图标都代表什么含义，可以进入 https://spring.io/projects 网站进行对比查看。
这些技术并不是所有的都需要学习，额外需要重点关注`Spring Framework`、`SpringBoot`和`SpringCloud`:

- Spring Framework：Spring框架，是Spring中最早最核心的技术，也是所有其他技术的基础。
- SpringBoot：Spring是来简化开发，而SpringBoot是来帮助Spring在简化的基础上能更快速进行开发。
- SpringCloud：这个是用来做分布式之微服务架构的相关开发。

除了上面的这三个技术外，还有很多其他的技术，也比较流行，如SpringData，SpringSecurity等，这些都可以被应用在我们的项目中。我们这里所学习的Spring其实指的是Spring Framework。

#### Spring发展史

接下来我们介绍下Spring Framework这个技术是如何来的呢?

[![](img/630c28bf16f2c2beb1eb2f6a.jpg)](https://pic.imgdb.cn/item/630c28bf16f2c2beb1eb2f6a.jpg)

- IBM(IT公司-国际商业机器公司)在1997年提出了EJB思想,早期的JAVAEE开发大都基于该思想。
- Rod Johnson(Java和J2EE开发领域的专家)在2002年出版的`Expert One-on-One J2EE Design and Development`,书中有阐述在开发中使用EJB该如何做。
- Rod Johnson在2004年出版的`Expert One-on-One J2EE Development without EJB`,书中提出了比EJB思想更高效的实现方案，并且在同年将方案进行了具体的落地实现，这个实现就是Spring1.0。
- 随着时间推移，版本不断更新维护，目前最新的是Spring5
  - Spring1.0是纯配置文件开发
  - Spring2.0为了简化开发引入了注解开发，此时是配置文件加注解的开发方式
  - Spring3.0已经可以进行纯注解开发，使开发效率大幅提升，我们的课程会以注解开发为主
  - Spring4.0根据JDK的版本升级对个别API进行了调整
  - Spring5.0已经全面支持JDK8，所以学习期间最好用JDK8版本
- 本节介绍了Spring家族与Spring的发展史，需要我们重点掌握的是:
  - Spring其实是Spring家族中的Spring Framework
  - Spring Framework是Spring家族中其他框架的底层基础，学好Spring可以为其他Spring框架的学习打好基础

### Spring系统架构

#### 系统架构图

- Spring Framework是Spring生态圈中最基础的项目，是其他项目的根基。
- Spring Framework的发展也经历了很多版本的变更，每个版本都有相应的调整
  [![](img/630c2c6e16f2c2beb1ee0194.jpg)](https://pic.imgdb.cn/item/630c2c6e16f2c2beb1ee0194.jpg)
- Spring Framework的5版本目前没有最新的架构图，而最新的是4版本，所以接下来主要研究的是4的架构图
  [![](img/630c2c8616f2c2beb1ee158e.jpg)](https://pic.imgdb.cn/item/630c2c8616f2c2beb1ee158e.jpg)

1. 核心层
   - Core Container：核心容器，这个模块是Spring最核心的模块，其他的都需要依赖该模块
2. AOP层
   - **AOP(Aspect Oriented Programming)**：**面向切面编程**，它依赖核心层容器，目的是在不改变原有代码的前提下对其进行功能增强
   - Aspects：AOP是思想，Aspects是对AOP思想的具体实现
3. 数据层
   - Data Access：数据访问，Spring全家桶中有对数据访问的具体实现技术
   - Data Integration：数据集成，Spring支持整合其他的数据层解决方案，比如Mybatis
   - Transactions：事务，Spring中事务管理是Spring AOP的一个具体实现，也是后期学习的重点内容
4. Web层
   - 这一层的内容将在SpringMVC框架具体学习
5. Test层
   - **Spring主要整合了Junit来完成单元测试和集成测试**

#### 课程学习路线

- 介绍完Spring的体系结构后，从中我们可以得出对于Spring的学习主要包含四部分内容，分别是:
  1. Spring的IOC/DI
  2. Spring的AOP
  3. AOP的具体应用,事务管理
  4. IOC/DI的具体应用,整合Mybatis

[![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://pic.imgdb.cn/item/630c2daf16f2c2beb1eefe53.jpg)

### Spring核心概念

在Spring核心概念这部分内容中主要包含`IOC/DI`、`IOC容器`和`Bean`,那么问题就来了，这些都是什么呢?

#### 目前项目中的问题

要想解答这个问题，就需要先分析下目前咱们代码在编写过程中遇到的问题

1. 业务层需要调用数据层的方法，就需要在业务层new数据层的对象
2. 如果数据层的实现类发生变化，那么业务层的代码也需要跟着改变，发生变更后，都需要进行编译打包和重部署
3. 所以，现在代码在编写的过程中存在的问题是：耦合度偏高

针对这个问题，该如何解决呢?

- 业务层实现
- 数据层实现

```java
JAVA
public class BookServlet extends BookServlet {
    //这个地方是写死了的
    private BookDao bookDao = new BookDaoImpl();

    public void save() {
        bookDao.save();
    }
}
```



我们就想，如果不new对象，只声明一下，不就可以降低依赖了吗，但是又会引入新的问题，去掉以后程序能运行吗?

- 答案显然是不行的，因为bookDao没有赋值为Null，强行运行就会出空指针异常。
  所以现在的问题就是，业务层不想new对象，运行的时候又需要这个对象，该咋办呢?
- 针对这个问题，Spring就提出了一个解决方案:
  - 使用对象时，在程序中不要主动使用new产生对象，转换为由外部提供对象
  - 这种实现思就是Spring的一个核心概念

#### IOC、IOC容器、Bean、DI(理解)

1. **IOC(Inversion of Control)控制反转**
   - 那什么是控制反转呢？
     - 使用对象时，**由主动new产生对象转换为由`外部`提供对象**，此过程中对象创建控制权由程序转移到外部，此思想称为控制反转。
     - 业务层要用数据层的类对象，以前是自己`new`的
     - 现在自己不new了，交给`别人[外部]`来创建对象
     - `别人[外部]`就**反转控制了数据层对象的创建权**
     - 这种思想就是控制反转
     - 别人[外部]指的是什么呢?继续往下看
   - **Spring和IOC之间的关系是什么呢?**
     - Spring技术对IOC思想进行了实现
     - Spring提供了一个容器，称为`IOC容器`，用来充当IOC思想中的"外部"
     - IOC思想中的`别人[外部]`指的就是Spring的IOC容器
   - IOC容器的作用以及内部存放的是什么?
     - **IOC容器**负责对象的创建、初始化等一系列工作，其中包含了数据层和业务层的类对象
     - **被创建或被管理的对象在IOC容器中统称为Bean**
     - IOC容器中放的就是一个个的Bean对象
   - 当IOC容器中创建好service和dao对象后，程序能正确执行么?
     - 不行，因为service运行需要依赖dao对象
     - IOC容器中虽然有service和dao对象
     - 但是service对象和dao对象没有任何关系
     - 需要把dao对象交给service,也就是说要绑定service和dao对象之间的关系
     - 像这种在容器中建立对象与对象之间的绑定关系就要用到DI(Dependency Injection)依赖注入.
2. **DI(Dependency Injection)依赖注入**
   - 什么是依赖注入呢?
     - 在容器中建立bean与bean之间的依赖关系的整个过程，称为依赖注入
       - 业务层要用数据层的类对象，以前是自己`new`的
       - 现在自己不new了，靠`别人[外部其实指的就是IOC容器]`来给注入进来
       - 这种思想就是依赖注入
   - IOC容器中哪些bean之间要建立依赖关系呢?
     - 这个需要程序员根据业务需求提前建立好关系，如业务层需要依赖数据层，service就要和dao建立依赖关系
   - 介绍完Spring的IOC和DI的概念后，我们会发现这两个概念的最终目标就是:充分解耦，具体实现靠:
     - 使用IOC容器管理bean（IOC)
     - 在IOC容器内将有依赖关系的bean进行关系绑定（DI）
     - 最终结果为:使用对象时不仅可以直接从IOC容器中获取，并且获取到的bean已经绑定了所有的依赖关系.

#### 形象理解(控制反转，依赖注入)

- 从前有个人叫小明，小明有三大爱好，逛知乎，打游戏，抢红包

```java
JAVA
class Ming extends Person
{
    private String name;
    private int age;

    void read(){
        //逛知乎
    }

    void play(){
        //打游戏
    }

    void grab(){
        //抢红包
    }

}
```

- 但是小明作为一个人类，无法仅靠自己就完成上述功能，他必须`依赖`一部手机，所以他买了一台iPhone6

```java

class iPhone6 extends Iphone
{
    void read(String name) {
        System.out.println(name + "打开了知乎然后编了一个故事");
    }

    void play(String name) {
        System.out.println(name + "打开了Apex并开始白给");
    }

    void grab(String name) {
        System.out.println(name + "开始抢红包却只抢不发");
    }
}
```

- 小明很珍惜自己买的新手机，每天把它牢牢控制在手心,于是小明变成了这样

```java
JAVA
class Ming extends Person {
    private String name;
    private int age;

    public Ming(String name, int age) {
        this.name = name;
        this.age = age;
    }

    void read() {
        //逛知乎
        new iPhone6().read(name);
    }

    void play() {
        //打游戏
        new iPhone6().play(name);
    }

    void grab() {
        //抢红包
        new iPhone6().grab(name);
    }
}
```

- 今天是周六，小明不用上班，于是他起床，并依次逛起了知乎，打起了游戏，并抢了个红包。

```java
JAVA
Ming ming = new Ming("小明", 18);  //小明起床
ming.read();
ming.play();
ming.grab();
```

- 这个时候，我们可以在命令行里看到输出如下

> 小明打开了知乎然后编了一个故事
> 小明打开了Apex并开始白给
> 小明开始抢红包却只抢不发

- 这一天，小明过得很充实，他觉得自己是世界上最幸福的人。
- 但随着时间的推移，手机越来越卡顿，电池寿命也越来越短，到了冬天还会冻关机了，小明很难过，他意识到他需要换一部手机了
- 为了获得更好的使用体验，小明一咬牙一跺脚，买了一台iPhone14 Pro Max，但他现在遇到了一个问题，他之前太过依赖那台iPhone6了，他们已经深深的耦合在一起了，如果要换手机，他必须要拿螺丝刀改造自己，将自己体内所有方法中的iPhone6换成iPhone14

```java
class Ming extends Person {
    private String name;
    private int age;

    public Ming(String name, int age) {
        this.name = name;
        this.age = age;
    }

    void read() {
        //逛知乎
        new iPhone14().read(name);
    }

    void play() {
        //打游戏
        new iPhone14().play(name);
    }

    void grab() {
        //抢红包
        new iPhone14().grab(name);
    }
}
```

- 虽然过程很辛苦，但小明觉得自己是值得的。随后在晚高峰挤地铁的时候，小明的手机被偷了。为了应急，小明只好重新使用那部刚刚被遗弃的iphone6，但是一想到那漫长的改造过程，小明的心里就说不出的委屈
- 他觉得自己过于依赖手机了，为什么每次手机出什么问题他都要去改造他自己，这不仅仅是过度耦合，简直是本末倒置，他向天空大喊，我不要再控制我的手机了。
- 天空中的造物主，也就是作为程序员的我，听到了他的呐喊，我告诉他，你不用再控制你的手机了，交给我来管理，把控制权交给我。这就叫做控制反转。
- 小明听到了我的话，他既高兴，又有一点害怕，他跪下来磕了几个头，虔诚地说到：“原来您就是传说中的造物主。我听到您刚刚说了 **`控制反转`** 四个字，就是把手机的控制权从我的手里交给你，但这只是您的想法，是一种思想罢了，要用什么办法才能实现控制反转，又可以让我继续使用手机呢？”
- “呵“，身为造物主的我在表现完不屑以后，扔下了四个大字，“依赖注入！”
- 接下来，伟大的我开始对小明进行惨无人道的改造

```java
class Ming extends Person {
    private String name;
    private int age;
    private Phone phone;

    public Ming(String name, int age, Phone phone) {
        this.name = name;
        this.age = age;
        this.phone = phone;
    }

    void read() {
        //逛知乎
        this.phone.read(name);
    }

    void play() {
        //打游戏
        this.phone.play(name);
    }

    void grab() {
        //抢红包
        this.phone.grab(name);
    }
}
```

- 随后我们来模拟小明的一天

```java
Phont phone = new Iphone14();   //创建一个iphone14的实例
if(phone.isBroken() == true){   //如果iphone14不可用，则使用旧版手机
    phone = new Iphone6();
}
Ming ming = new Ming("小明",18,phone);    //小明不用关心是什么手机，他只要玩就行了。
ming.read();
ming.play();
ming.grab();
```

- 我们先看一下iphone14 是否可以使用，如果不可以使用，则直接换成iphone6,然后唤醒小明，并把手机塞到他的手里，换句话说，把他所依赖的手机直接注入到他的身上，他不需要关心自己拿的是什么手机，他只要直接使用就可以了。
- 这就是`依赖注入`。
- 随后小明的生活开始变得简单了起来，而他把省出来的时间都用来写笔记了，他在笔记本上这样写到

我曾经有很强的控制欲，过度依赖于我的手机，导致我和手机之间耦合程度太高，只要手机出现一点点问题，我都要改造我自己，这实在是既浪费时间又容易出问题。自从我把控制权交给了造物主，他每天在唤醒我以前，就已经替我选好了手机，我只要按照平时一样玩手机就可以了，根本不用关心是什么手机。即便手机出了问题，也可以由造物主直接搞定，不需要再改造我自己了，我现在买了七部手机，都交给了造物主，每天换一部，美滋滋！
我也从其中获得了这样的感悟： 如果一个类A 的功能实现需要借助于类B，那么就称类B是类A的依赖，如果在类A的内部去实例化类B，那么两者之间会出现较高的耦合，一旦类B出现了问题，类A也需要进行改造，如果这样的情况较多，每个类之间都有很多依赖，那么就会出现牵一发而动全身的情况，程序会极难维护，并且很容易出现问题。**要解决这个问题，就要把A类对B类的控制权抽离出来，交给一个第三方去做，把控制权反转给第三方，就称作控制反转**（IOC Inversion Of Control）。控制反转是一种思想，是能够解决问题的一种可能的结果，而依赖注入（Dependency Injection）就是其最典型的实现方法。由第三方（我们称作IOC容器）来控制依赖，把他通过构造函数、属性或者工厂模式等方法，注入到类A内，这样就极大程度的对类A和类B进行了解耦。

原文出自知乎的一篇文章，这里稍微进行了些许改动



[![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://files.codelife.cc/website/zhihu.svg)

浅谈控制反转与依赖注入--胡小国

https://zhuanlan.zhihu.com/p/33492169

#### 核心概念小结

重点要理解`什么是IOC/DI思想`、`什么是IOC容器`和`什么是Bean`：

1. 什么IOC/DI思想?

- IOC:控制反转，**控制反转的是对象的创建权**
- DI:依赖注入，**绑定对象与对象之间的依赖关系**

1. 什么是IOC容器?

- Spring创建了一个容器用来存放所创建的对象，这个容器就叫IOC容器

1. 什么是Bean?

- 容器中所存放的一个个对象就叫Bean或Bean对象

## Spring入门案例

介绍完Spring的核心概念后，接下来我们得思考一个问题就是，Spring到底是如何来实现IOC和DI的，那接下来就通过一些简单的入门案例，来演示下具体实现过程:

### IOC入门案例

对于入门案例，我们得先`分析思路`然后再`代码实现`

#### 入门案例思路分析

1. Spring是使用容器来管理bean对象的，那么管什么?

- 主要管理项目中所使用到的类对象，比如(Service和Dao)

1. 如何将被管理的对象告知IOC容器?

- 使用配置文件

1. 被管理的对象交给IOC容器，要想从容器中获取对象，就先得思考如何获取到IOC容器?

- Spring框架提供相应的接口

1. IOC容器得到后，如何从容器中获取bean?

- 调用Spring框架提供对应接口中的方法

1. 使用Spring导入哪些坐标?

- 用别人的东西，就需要在pom.xml添加对应的依赖

#### 入门案例代码实现

- 需求分析:将BookServiceImpl和BookDaoImpl交给Spring管理，并从容器中获取对应的bean对象进行方法调用。

1. 创建Maven的java项目
   这个没啥好说的
2. pom.xml添加Spring的依赖jar包

```XML
<dependency>
  <groupId>org.springframework</groupId>
  <artifactId>spring-context</artifactId>
  <version>5.2.10.RELEASE</version>
</dependency>
```

1. **创建BookDao，BookDaoImpl，BookService和BookServiceImpl四个类**

- BookDao
- BookDaoImpl
- BookService
- BookServiceImpl

```JAVA
ublic interface BookDao {
    public void save();
}
```



1. resources下添加spring配置文件

右键 -> 新建 -> XML配置文件 -> Spring配置

1. 在配置文件中完成bean的配置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
      <!--
      bean标签标示配置bean
      id属性标示给bean起名字
      class属性表示给bean定义类型，
      得是具体的实现类而不是接口，要靠这个造对象的
      -->
    <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl"/>
    <bean id="bookService" class="com.blog.service.impl.BookServiceImpl"/>
</beans>
```

注意事项：bean定义时id属性在同一个上下文中(配置文件)不能重复

1. **获取IOC容器**
   使用Spring提供的接口完成IOC容器的创建，创建App类，编写main方法

```java
public class App {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");

    }
}
```

1. **从容器中获取对象进行方法调用**
   使用getBean(String name)方法，其name参数就是我们在bean配置的id，通过这个id来造对象

```java
public class App {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        BookService bookService = (BookService) context.getBean("bookService");
        bookService.save();
    }
}
```

1. 运行程序
   测试结果如下

> book service save …
> book dao save …

至此，Spring的IOC入门案例已经完成，但是在`BookServiceImpl`的类中依然存在`BookDaoImpl`对象的new操作，它们之间的耦合度还是比较高，这块该如何解决，就需要用到下面的`DI(依赖注入)`。

### DI入门案例

对于DI的入门案例，我们依然先`分析思路`然后再`代码实现`

#### 入门案例思路分析

1. 要想实现依赖注入，必须要基于IOC管理Bean

- DI的入门案例要依赖于前面的IOC入门案例

1. Service中使用new形式创建的Dao对象是否保留？

- 不保留，这样才能解耦合，最终要使用IOC容器中的bean对象

1. Service中需要的Dao对象如何进入到Service中？

- 在Service中提供一个方法（例如提供一个set方法），让Spring的IOC容器可以通过该方法传入bean对象，也就达到了不是自己new，而是外部提供

1. Service与Dao之间的关系如何描述？

- 使用配置文件

#### 入门案例代码实现

需求：基于IOC入门案例，在BookServiceImpl类中删除new对象的方式，使用Spring的DI完成Dao层的注入

1. 删除业务层中使用new的方式创建的dao对象

```
JAVA
public class BookServiceImpl implements BookService {
    //private BookDao bookDao = new BookDaoImpl();
    private BookDao bookDao;
    public void save() {
        System.out.println("book service save ...");
        bookDao.save();
    }
}
```

1. 在业务层提供BookDao的setter方法
   我们在set方法中加一条输出语句，看看是否被调用了

```
JAVA
public class BookServiceImpl implements BookService {
    private BookDao bookDao;

    public void save() {
        System.out.println("book service save ...");
        bookDao.save();
    }

    public void setBookDao(BookDao bookDao) {
        this.bookDao = bookDao;
        System.out.println("set方法被调用啦");
    }
}
```

1. 在配置文件中添加依赖注入的配置

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl"/>

    <!--主要变化在这里-->
    <bean id="bookService" class="com.blog.service.impl.BookServiceImpl">
        <!--配置server与dao的关系-->
        <!--
            property标签表示配置当前bean的属性
            name属性表示配置哪一个具体的属性(这里是配置bookService的bookDao属性)
            ref属性表示参照哪一个bean(参照当前配置文件中的bookDao)
        -->
        <property name="bookDao" ref="bookDao"></property>
    </bean>
</beans>
```

- 注意:配置中的两个bookDao的含义是不一样的
  - name="bookDao"中`bookDao`的作用是让Spring的IOC容器在获取到名称后，将首字母大写，前面加set找对应的`setBookDao()`方法进行对象注入
  - ref="bookDao"中`bookDao`的作用是让Spring能在IOC容器中找到id为`bookDao`的Bean对象给`bookService`进行注入

[![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://pic.imgdb.cn/item/630d5f3d16f2c2beb1abd707.jpg)
\4. 运行程序调用方法
测试结果如下

> set方法被调用啦
> book service save …
> book dao save …

## IOC相关内容

通过前面两个案例，我们已经学习了`bean如何定义配置`，`DI如何定义配置`以及`容器对象如何获取`的内容，接下来主要是把这三块内容展开进行详细的讲解，深入的学习下这三部分的内容，首先是bean基础配置。

### bean基础配置

对于bean的配置中，主要会讲解`bean基础配置`,`bean的别名配置`,`bean的作用范围配置`(重点),这三部分内容

#### bean的基础配置–id与class

对于bean的基础配置，在前面的案例中已经使用过:

```
XML
<bean id="" class=""/>
```

其中，bean标签的功能、使用方式以及id和class属性的作用，我们通过一张图来描述下
[![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://pic.imgdb.cn/item/630d676b16f2c2beb1afa402.jpg)

#### bean的name属性

我们可以在bean标签中配置name属性，来充当别名，下面我们来演示

1. 配置别名
   打开spring的配置文件`applicationContext.xml`

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl"/>
    <!--name:为bean指定别名，别名可以有多个，使用逗号，分号，空格进行分隔-->
    <bean id="bookService" name="service1 service2 service3" class="com.blog.service.impl.BookServiceImpl">
        <property name="bookDao" ref="bookDao"></property>
    </bean>
</beans>
```

1. 根据名称容器中获取bean对象

```
JAVA
public class App {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        //此处根据bean标签的id属性和name属性的任意一个值来获取bean对象
        BookService bookService = (BookService) context.getBean("service2");
        bookService.save();
    }
}
```

1. 运行程序
   测试结果如下：

> set方法被调用啦
> book service save …
> book dao save …

注意事项：

- bean依赖注入的ref属性指定bean，必须在容器中存在，而ref的值也可以是name里的别名，不过还是建议用id值来注入
- 如果我们在调用getBean(String name)方法时，传入了一个不存在该名称的bean对象，则会报错`NoSuchBeanDefinitionException`，此时我们要检查一下是哪边写错了（例如bean的id和name都没有service100，而getBean的参数却写了service100）

#### bean作用范围scope配置

关于bean的作用范围是bean属性配置的一个重点内容。
bean的scope有两个取值：

- singleton：单例（默认）
- prototype：非单例

\######## 验证IOC容器中对象是否为单例

- 验证思路：我们只需要对同一个bean创建两个对象，然后打印二者的地址值，看看是否一致
- 代码实现

```
JAVA
public class App {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        //我这里使用了别名，其实还是同一个bean
        BookService bookService2 = (BookService) context.getBean("service2");
        BookService bookService3 = (BookService) context.getBean("service3");
        System.out.println(bookService2);
        System.out.println(bookService3);
    }
}
```

- 输出结果如下，地址值一致，确实是单例的

> com.blog.service.impl.BookServiceImpl@25bbe1b6
> com.blog.service.impl.BookServiceImpl@25bbe1b6

- 那如果我想创建出来非单例的bean对象，该如何实现呢?
  - 配置bean的scope属性为prototype

\######## 配置bean为非单例
在Spring配置文件中，配置scope属性来实现bean的非单例创建

- 在Spring的配置文件中，修改`<bean>`的scope属性

```
XML
<bean id="bookService" name="service1 service2 service3" class="com.blog.service.impl.BookServiceImpl" scope="prototype">
    <property name="bookDao" ref="bookDao"></property>
</bean>
```

- 运行程序
  输出结果如下，地址值不一致

> com.blog.service.impl.BookServiceImpl@25bbe1b6
> com.blog.service.impl.BookServiceImpl@5702b3b1

\######## scope使用后续思考
介绍完`scope`属性以后，我们来思考几个问题:

- 为什么bean默认为单例?
  - bean为单例的意思是在Spring的IOC容器中只会有该类的一个对象
  - bean对象只有一个就避免了对象的频繁创建与销毁，达到了bean对象的复用，性能高
- bean在容器中是单例的，会不会产生线程安全问题?
  - 如果对象是有状态对象，即该对象有成员变量可以用来存储数据的，
  - 因为所有请求线程共用一个bean对象，所以会存在线程安全问题。
  - 如果对象是无状态对象，即该对象没有成员变量没有进行数据存储的，
  - 因方法中的局部变量在方法调用完成后会被销毁，所以不会存在线程安全问题。
- 哪些bean对象适合交给容器进行管理?
  - 表现层对象（controller）
  - 业务层对象（service）
  - 数据层对象（dao）
  - 工具对象（util）
- 哪些bean对象不适合交给容器进行管理?
  - 封装实例的域对象（domain，pojo），因为会引发线程安全问题，所以不适合。

### bean实例化

- 对象已经能交给Spring的IOC容器来创建了，但是容器是如何来创建对象的呢?

  - 就需要研究下

    ```
    bean的实例化过程
    ```

    ，在这块内容中主要解决两部分内容，分别是

    - bean是如何创建的
    - 实例化bean的三种方式，`构造方法`,`静态工厂`和`实例工厂`

- 在讲解这三种创建方式之前，我们需要先确认一件事:

  - bean本质上就是对象，对象在new的时候会使用构造方法完成，那创建bean也是使用构造方法完成的。
    - 基于这个知识点出发，我们来验证spring中bean的三种创建方式，

#### 构造方法实例化

- 在之前的BookDaoImpl类中添加一个无参构造函数，并打印一句话，方便观察结果。

```
JAVA
public class BookDaoImpl implements BookDao {
    public void save() {
        System.out.println("book dao save ...");
    }

    public BookDaoImpl() {
        System.out.println("book dao constructor is running ...");
    }
}
```

- 运行程序
  输出结果如下

> book dao constructor is running …
> com.blog.service.impl.BookServiceImpl@25bbe1b6

- 接下来我们将构造器私有化继续测试

```
JAVA
public class BookDaoImpl implements BookDao {
    public void save() {
        System.out.println("book dao save ...");
    }

    private BookDaoImpl() {
        System.out.println("book dao constructor is running ...");
    }
}
```

- 运行程序，能执行成功，说明内部走的依然是构造函数，能访问到类中的私有构造方法，显而易见Spring底层用的是反射

> book dao constructor is running …
> com.blog.service.impl.BookServiceImpl@25bbe1b6

- 我们在构造函数中添加一个参数试试

```
JAVA
public class BookDaoImpl implements BookDao {
    public void save() {
        System.out.println("book dao save ...");
    }

    public BookDaoImpl(int i) {
        System.out.println("book dao constructor is running ...");
    }
}
```

- 运行程序，程序会报错`NoSuchMethodException`，说明Spring底层使用的是类的无参构造方法。
- 完事儿之后记得将空参构造器还原回去，把其中的输出语句也删了，方便我们进行下一步的测试

#### 静态工厂实例化

- 创建一个工厂类BookDaoFactory并提供一个静态方法

```
JAVA
//静态工厂创建对象
public class BookDaoFactory {
    public static BookDao getBookDaoImpl(){
        return new BookDaoImpl();
    }
}
```

- 修改App运行类，在类中通过工厂获取对象

```
JAVA
public class App {
    public static void main(String[] args) {
        //通过静态工厂创建对象
        BookDao bookDao = BookDaoFactory.getBookDaoImpl();
        bookDao.save();
    }
}
```

- 运行后，可以查看到结果

> book dao save …

- 那我们如何将这种方式交给Spring来管理呢？
- 这就要用到Spring中的静态工厂实例化的知识了，具体实现步骤为:

1. 在spring的配置文件`application.properties`修改bookDao的bean

```
XML
<bean id="bookDao" class="com.blog.factory.BookDaoFactory" factory-method="getBookDaoImpl"/>
```

class:工厂类的类全名
factory-mehod:具体工厂类中创建对象的方法名
\2. 在App运行类，使用从IOC容器中获取bean的方法进行运行测试

```
JAVA
public class App {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        BookDao bookDao = (BookDao) context.getBean("bookDao");
        bookDao.save();
    }
}
```

1. 运行后，结果如下，与我们自己直接new对象没太大区别，而且还麻烦了，那这种方式的意义是什么呢？

> book dao save …

1. 解惑
   在工厂的静态方法中，我们除了new对象还可以做其他的一些业务操作，而之前new对象的方式就无法添加其他的业务内容

```
JAVA
public class BookDaoFactory {
    public static BookDao getBookDaoImpl() {
        System.out.println("book dao factory setup ...");//模拟必要的业务操作
        //这里还可以加一大堆业务逻辑
        return new BookDaoImpl();
    }
} 
```

介绍完静态工厂实例化后，这种方式一般是用来兼容早期的一些老系统，所以`了解为主`。

#### 实例工厂与FactoryBean

\######## 实例工厂实例化
接下来继续来研究Spring的第三种bean的创建方式`实例工厂实例化`

- 修改工厂类`BookDaoFactory`的get方法，注意此处和静态工厂的工厂类不一样的地方是方法`不是静态方法`

```
JAVA
public class BookDaoFactory {
    //唯一的区别就是去掉的static
    public BookDao getBookDaoImpl() {
        System.out.println("book dao factory setup ...");//模拟必要的业务操作
        //这里还可以加一大堆业务逻辑
        return new BookDaoImpl();
    }
}
```

- 修改App运行类，在类中通过工厂获取对象，由于不是静态方法了，所以我们需要先创建实例工厂对象，然后再用实例工厂对象调用方法

```
JAVA
public class App {
    public static void main(String[] args) {
        //创建实例工厂对象
        BookDaoFactory bookDaoFactory = new BookDaoFactory();
        //通过实例工厂对象创建对象
        BookDao bookDao = bookDaoFactory.getBookDaoImpl();
        bookDao.save();
    }
}
```

- 运行结果如下

> book dao factory setup … 这个是模拟业务逻辑的输出，无视掉就行
> book dao save …

- 那么对于上面这种实例工厂的方式如何交给Spring管理呢?

1. 在spring配置文件中修改bookDao的bean

```
XML
<bean id="bookDaoFactory" class="com.blog.factory.BookDaoFactory"/>
<bean id="bookDao" factory-bean="bookDaoFactory" factory-method="getBookDaoImpl"/>
```

实例化工厂运行的顺序是:

- 创建实例化工厂对象,对应的是第一行配置
- 调用对象中的方法来创建bean，对应的是第二行配置
  - factory-bean:工厂的实例对象
  - factory-method:工厂对象中的具体创建对象的方法名

1. 在App运行类，使用从IOC容器中获取bean的方法进行运行测试

```
JAVA
public class App {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        BookDao bookDao = (BookDao) context.getBean("bookDao");
        bookDao.save();
    }
}
```

1. 运行后，可以查看到结果

> book dao factory setup …
> book dao save …

实例工厂实例化的方式就已经介绍完了，配置的过程还是比较复杂，要写两行配置，而且这两行还是高耦合的，所以Spring为了简化这种配置方式就提供了一种叫`FactoryBean`的方式来简化开发。

\######## FactoryBean

具体的使用步骤为：

1. 创建一个`BookDaoFactoryBean`类，实现`FactoryBean`接口，重写接口方法

```
JAVA
public class BookDaoFactoryBean implements FactoryBean<BookDao> {

    public BookDao getObject() throws Exception {
        return new BookDaoImpl();
    }

    public Class<?> getObjectType() {
        return BookDao.class;
    }
}
```

1. 在Spring的配置文件中修改bookDao的bean

```
XML
<bean id="bookDao" class="com.blog.factory.BookDaoFactoryBean"></bean>
```

1. App运行类不用做任何修改，直接运行，结果如下

> book dao save …

这种方式在Spring去整合其他框架的时候会被用到，所以这种方式需要我们理解掌握。

- 查看源码会发现，FactoryBean接口其实会有三个方法，分别是

```
JAVA
T getObject() throws Exception;

Class<?> getObjectType();

default boolean isSingleton() {
    return true;
}
```

- 方法一:getObject()，被重写后，在方法中进行对象的创建并返回
- 方法二:getObjectType(),被重写后，主要返回的是被创建类的Class对象
- 方法三:没有被重写，因为它已经给了默认值，从方法名中可以看出其作用是设置对象是否为单例，默认true，这里就不加以验证了

#### bean实例化小结

- bean是如何创建的呢?

  - 通过构造方法

- Spring的IOC实例化对象的三种方式分别是:

  - 构造方法(常用)
  - 静态工厂(了解)
  - 实例工厂(了解)
    - FactoryBean(实用)
      这些方式中，重点掌握`构造方法`和`FactoryBean`即可。

  需要注意的一点是，构造方法在类中默认会提供，但是如果重写了构造方法，默认的就会消失，在使用的过程中需要注意，如果需要重写构造方法，最好把默认的构造方法也重写下。

### bean的生命周期

关于bean的相关知识还有最后一个是`bean的生命周期`，对于生命周期，我们主要围绕着`bean生命周期控制`来讲解

- 首先理解下什么是生命周期?
  - 从创建到消亡的完整过程,例如人从出生到死亡的整个过程就是一个生命周期。
- bean生命周期是什么?
  - bean对象从创建到销毁的整体过程。
- bean生命周期控制是什么?
  - 在bean创建后到销毁前做一些事情。
- 现在我们面临的问题是如何在bean的创建之后和销毁之前把我们需要添加的内容添加进去。

#### 生命周期设置

具体的控制有两个阶段:

- bean创建之后，想要添加内容，比如用来初始化需要用到资源
- bean销毁之前，想要添加内容，比如用来释放用到的资源

1. 添加初始化和销毁方法
   针对这两个阶段，我们在BookDaoImpl类中分别添加两个方法，方法名随便取

```
JAVA
public class BookDaoImpl implements BookDao {
    public void save() {
        System.out.println("book dao save ...");
    }

    public void init() {
        System.out.println("init ... ");
    }

    public void destroy() {
        System.out.println("destroy ... ");
    }
}
```

1. 配置生命周期
   修改bookDao的配置

```
XML
<bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl" init-method="init" destroy-method="destroy"></bean>
```

1. 运行程序
   输出结果如下

> init …
> book dao save …

从结果中可以看出，init方法执行了，但是destroy方法却未执行，这是为什么呢?

- Spring的IOC容器是运行在JVM中
- 运行main方法后,JVM启动,Spring加载配置文件生成IOC容器,从容器获取bean对象，然后调方法执行
- main方法执行完后，JVM退出，这个时候IOC容器中的bean还没有来得及销毁就已经结束了
- 所以没有调用对应的destroy方法

知道了出现问题的原因，具体该如何解决呢?继续往下看

#### close关闭容器

- ApplicationContext中没有close方法，它的子类中有close方法
- 所以需要将ApplicationContext更换成ClassPathXmlApplicationContext，然后调用close方法就好啦

```
JAVA
public class App {
    public static void main(String[] args) {
        //ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        BookDao bookDao = (BookDao) context.getBean("bookDao");
        bookDao.save();
        context.close();
    }
}
```

- 运行程序，输出如下，可以看到destroy正常输出

> init …
> book dao save …
> destroy …

#### 注册钩子关闭容器

- 在容器未关闭之前，提前设置好回调函数，让JVM在退出之前回调此函数来关闭容器
- 调用context的registerShutdownHook()方法

```
JAVA
public class App {
    public static void main(String[] args) {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        BookDao bookDao = (BookDao) context.getBean("bookDao");
        bookDao.save();
        context.registerShutdownHook();
    }
}
```

注意：registerShutdownHook在ApplicationContext中也没有

- 运行后，查询打印结果

> init …
> book dao save …
> destroy …

- 那两种方式介绍完后，close和registerShutdownHook选哪个?

  - 相同点:这两种都能用来关闭容器

  - 不同点:close()是在调用的时候关闭，registerShutdownHook()是在JVM退出前调用关闭。

    - 那么registerShutdownHook()方法可以在任意位置调用，下面的代码中将其放在了第二行，仍能正常输出，但要是将其换成close()方法，则会报错`BeanFactory not initialized or already closed`，这里就是already closed

    ```
    JAVA
    public class App {
        public static void main(String[] args) {
            ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
            context.registerShutdownHook();
            BookDao bookDao = (BookDao) context.getBean("bookDao");
            bookDao.save();
        }
    }
    ```

- 开发中到底用哪个呢？

  - 答案是两个都不用
  - 分析上面的实现过程，会发现添加初始化和销毁方法，即需要编码也需要配置，实现起来步骤比较多也比较乱。
  - Spring给我们提供了两个接口来完成生命周期的控制，好处是可以不用再进行配置`init-method`和`destroy-method`

- 接下来在BookServiceImpl完成这两个接口的使用

  - 修改BookServiceImpl类，添加两个接口`InitializingBean`， `DisposableBean`并实现接口中的两个方法`afterPropertiesSet`和`destroy`

```
JAVA
public class BookServiceImpl implements BookService, InitializingBean, DisposableBean {
    private BookDao bookDao;

    public void save() {
        System.out.println("book service save ...");
        bookDao.save();
    }

    public void setBookDao(BookDao bookDao) {
        System.out.println("set ... ");
        this.bookDao = bookDao;
    }

    public void destroy() throws Exception {
        System.out.println("service destroy ... ");
    }

    public void afterPropertiesSet() throws Exception {
        System.out.println("service init ... ");
    }
}
```

- BookServiceImpl的bean配置如下

```
XML
<bean id="bookService" class="com.blog.service.impl.BookServiceImpl">
    <property name="bookDao" ref="bookDao"></property>
</bean>
```

- 重新运行App类，输出结果如下

> init …
> service init …
> book dao save …
> service destroy …
> destroy …

- 小细节

  - 对于InitializingBean接口中的afterPropertiesSet方法，翻译过来为`属性设置之后`。

  - 对于BookServiceImpl来说，bookDao是它的一个属性

  - setBookDao方法是Spring的IOC容器为其注入属性的方法

  - 思考:afterPropertiesSet和setBookDao谁先执行?

    - 从方法名分析，猜想应该是setBookDao方法先执行
    - 验证思路，在setBookDao方法中添加一局输出语句，看看谁先输出

    ```
    JAVA
    public void setBookDao(BookDao bookDao) {
        System.out.println("set ... ");
        this.bookDao = bookDao;
    }
    ```

    - 重新运行，结果如下，`service init`在`set`之后，符合我们的预期

    > init …
    > set …
    > service init …
    > book dao save …
    > service destroy …
    > destroy …

可能存在的疑问：明明我们没调用bookService，但为什么上面的输出结果中有service呢？
解惑：所有IOC容器中的bean的初始化和销毁都会运行，所以service也会运行

#### bean生命周期小结

1. 关于Spring中对bean生命周期控制提供了两种方式:

- 在配置文件中的bean标签中添加`init-method`和`destroy-method`属性
- 类实现`InitializingBean`与`DisposableBean`接口

1. 对于bean的生命周期控制在bean的整个生命周期中所处的位置如下

- 初始化容器
  - 1.创建对象(内存分配)
  - 2.执行构造方法
  - 3.执行属性注入(set操作)（`set ...`）
  - 4.执行bean初始化方法（`service init ...`）
- 使用bean
  - 执行业务操作（`book dao save ...`）
- 关闭/销毁容器
  - 执行bean销毁方法（`service destroy ...`）

1. 关闭容器的两种方式:

- ConfigurableApplicationContext是ApplicationContext的子类，子类才有下面两种方法
  - close()方法
  - registerShutdownHook()方法

## DI相关内容

上面我们已经完成了bean相关操作的讲解，接下来就进入第二个大的模块`DI依赖注入`。

我们先来思考

- 向一个类中传递数据的方式有几种?

  - 普通方法(set方法)
  - 构造方法

- 依赖注入描述了在容器中建立bean与bean之间的依赖关系的过程，如果bean运行需要的是数字或字符串呢?

  - 引用类型
  - 简单类型(基本数据类型与String)

- Spring就是基于上面这些知识点，为我们提供了两种注入方式，分别是:

  - ```
    setter注入
    ```

    - 简单类型
    - 引用类型

  - ```
    构造器注入
    ```

    - 简单类型
    - 引用类型

### setter注入

- 对于setter方式注入引用类型的方式之前已经学习过，快速回顾下:
- 在bean中定义引用类型属性，并提供可访问的set方法

```
JAVA
public class BookServiceImpl implements BookService {
    private BookDao bookDao;
    public void setBookDao(BookDao bookDao) {
        this.bookDao = bookDao;
    }
}
```

- 配置中使用property标签ref属性注入引用类型对象

```
XML
<bean id="bookService" class="com.blog.service.impl.BookServiceImpl">
    <property name="bookDao" ref="bookDao"></property>
</bean>
```

- 我们再来回顾一下配置中的两个bookDao的含义

配置中的两个bookDao的含义是不一样的

- name="bookDao"中bookDao的作用是让Spring的IOC容器在获取到名称后，将首字母大写，前面加set找对应的setBookDao()方法进行对象注入
- ref="bookDao"中bookDao的作用是让Spring能在IOC容器中找到id为bookDao的Bean对象给bookService进行注入

#### 环境准备

- 先来做一些准备工作，我们在dao包下新建一个UserDao接口

```
JAVA
public interface UserDao {
    public void save();
}
```

- 然后新建一个UserDaoImpl类实现UserDao接口

```
JAVA
public class UserDaoImpl implements UserDao {
    public void save() {
        System.out.println("user dao save ...");
    }
}
```

- 然后修改我们之前的BookDao等类

- BookDao
- BookDaoImpl
- BookService
- BookServiceImpl

```
JAVA
public interface BookDao {
    public void save();
}
```



- 配置文件如下

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl"></bean>

    <bean id="bookService" class="com.blog.service.impl.BookServiceImpl">
        <property name="bookDao" ref="bookDao"></property>
    </bean>
</beans>
```

- 修改App运行类，加载Spring的IOC容器，并从中获取对应的bean对象

```
JAVA
public class App {
    public static void main(String[] args) {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        BookService bookService = (BookService) context.getBean("bookService");
        bookService.save();
    }
}
```

#### 注入引用数据类型

需求:在bookServiceImpl对象中注入userDao

1. 在BookServiceImpl中声明userDao属性
2. 为userDao属性提供setter方法
3. 在配置文件中使用property标签注入

- `步骤一：`声明userDao属性并提供setter方法

```
JAVA
public class BookServiceImpl implements BookService {
    private BookDao bookDao;
    //声明属性
    private UserDao userDao;
    //提供setter
    public void setUserDao(UserDao userDao) {
        this.userDao = userDao;
    }

    public void setBookDao(BookDao bookDao) {
        this.bookDao = bookDao;
    }

    public void save() {
        System.out.println("book service save ...");
        bookDao.save();
        userDao.save();
    }
}
```

- `步骤二：`在配置文件中注入配置
  在applicationContext.xml配置文件中使用property标签注入

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl"></bean>
    <bean id="userDao" class="com.blog.dao.impl.UserDaoImpl"></bean>

    <bean id="bookService" class="com.blog.service.impl.BookServiceImpl">
        <property name="bookDao" ref="bookDao"></property>
        <property name="userDao" ref="userDao"></property>
    </bean>
</beans>
```

- `步骤三：`运行程序，结果如下，userDao已经成功注入。

> book service save …
> book dao save …
> user dao save …

#### 注入简单数据类型

需求：给BookDaoImpl注入一些简单数据类型的数据
参考引用数据类型的注入，我们可以推出具体的步骤为:

1. 在BookDaoImpl类中声明对应的简单数据类型的属性
2. 为这些属性提供对应的setter方法
3. 在applicationContext.xml中配置

**思考:**

- 引用类型使用的是`<property name="" ref=""/>`,简单数据类型还是使用ref吗?
- ref是指向Spring的IOC容器中的另一个bean对象的，对于简单数据类型，没有对应的bean对象，该如何配置呢?使用value来配置`<property name="" value=""/>`
- `步骤一：`声明属性并提供setter方法
  这里举例就用`String dataBaseName`和`int connectionCount`这两个属性，同时在save()方法的输出语句中加上这两个属性

```
JAVA
public class BookDaoImpl implements BookDao {
    private String dataBaseName;
    private int connectionCount;

    public void setDataBaseName(String dataBaseName) {
        this.dataBaseName = dataBaseName;
    }

    public void setConnectionCount(int connectionCount) {
        this.connectionCount = connectionCount;
    }

    public void save() {
        System.out.println("book dao save ..." + dataBaseName + "," + connectionCount);
    }
}
```

- `步骤二：`在配置文件中进行注入配置
  在applicationContext.xml配置文件中使用property标签注入

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl">
        <property name="dataBaseName" value="mysql"></property>
        <property name="connectionCount" value="100"></property>
    </bean>
    <bean id="userDao" class="com.blog.dao.impl.UserDaoImpl"></bean>

    <bean id="bookService" class="com.blog.service.impl.BookServiceImpl">
        <property name="bookDao" ref="bookDao"></property>
        <property name="userDao" ref="userDao"></property>
    </bean>
</beans>
```

value:后面跟的是简单数据类型，对于参数类型，Spring在注入的时候会自动转换，但是不能写一个错误的类型，例如`connectionCount`是`int`类型，你却给他传一个`abc`，这样的话，spring在将`abc`转换成int类型的时候就会报错。

- `步骤三：`运行程序，查看输出，两个简单数据类型也成功注入

> book service save …
> book dao save …mysql,100
> user dao save …

- 那么对于setter注入方式的基本使用就已经介绍完了
  - 对于引用数据类型使用的是`<property name="" ref=""/>`
  - 对于简单数据类型使用的是`<property name="" value=""/>`

### 构造器注入

#### 环境准备

- 修改BookDao、BookDaoImpl、UserDao、UserDaoImpl、BookService和BookServiceImpl类

- BookDao
- BookDaoImpl
- UserDao
- UserDaoImpl
- BookService
- BookServiceImpl

```
JAVA
public interface BookDao {
    public void save();
}
```



- 配置文件

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl"/>
    <bean id="bookService" class="com.blog.service.impl.BookServiceImpl">
        <property name="bookDao" ref="bookDao"/>
    </bean>
</beans>
```

- 运行类

```
JAVA
public class App {
    public static void main( String[] args ) {
        ApplicationContext ctx = new ClassPathXmlApplicationContext("applicationContext.xml");
        BookService bookService = (BookService) ctx.getBean("bookService");
        bookService.save();
    }
}
```

#### 构造器注入引用数据类型

接下来，在上面这个环境中来完成构造器注入的学习:

需求：将BookServiceImpl类中的bookDao修改成使用构造器的方式注入。

1. 将bookDao的setter方法删除掉
2. 添加带有bookDao参数的构造方法
3. 在applicationContext.xml中配置

- `步骤一：`删除setter方法并提供构造方法
  在BookServiceImpl类中将bookDao的setter方法删除掉,并添加带有bookDao参数的构造方法

```
JAVA
public class BookServiceImpl implements BookService{
    private BookDao bookDao;

    public BookServiceImpl(BookDao bookDao) {
        this.bookDao = bookDao;
    }

    public void save() {
        System.out.println("book service save ...");
        bookDao.save();
    }
}
```

- `步骤二：`配置文件中进行配置构造方式注入
  在applicationContext.xml中配置

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl"/>
    <bean id="bookService" class="com.blog.service.impl.BookServiceImpl">
        <constructor-arg name="bookDao" ref="bookDao"/>
    </bean>
</beans>
```

说明：在标签`<constructor-arg>`中

- name属性对应的值为构造函数中方法`形参的参数名`，必须要保持一致。
- ref属性指向的是spring的IOC容器中其他bean对象。

- `步骤三：`运行程序
  运行App类，查看结果，说明bookDao已经成功注入。

> book service save …
> book dao save …

#### 构造器注入多个引用数据类型

需求：在BookServiceImpl使用构造函数注入多个引用数据类型，比如userDao

1. 声明userDao属性
2. 生成一个带有bookDao和userDao参数的构造函数
3. 在applicationContext.xml中配置注入

- `步骤一：`提供多个属性的构造函数
  在BookServiceImpl声明userDao并提供多个参数的构造函数，save方法中记得调用userDao.save()

```
JAVA
public class BookServiceImpl implements BookService {
    private BookDao bookDao;
    private UserDao userDao;

    public BookServiceImpl(BookDao bookDao, UserDao userDao) {
        this.bookDao = bookDao;
        this.userDao = userDao;
    }

    public void save() {
        System.out.println("book service save ...");
        bookDao.save();
        userDao.save();
    }
}
```

- `步骤二：`在配置文件中配置多参数注入

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="userDao" class="com.blog.dao.impl.UserDaoImpl"/>
    <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl"/>
    <bean id="bookService" class="com.blog.service.impl.BookServiceImpl">
        <constructor-arg name="bookDao" ref="bookDao"/>
        <constructor-arg name="userDao" ref="userDao"/>
    </bean>
</beans>
```

- `步骤三：`运行程序
  结果中出现了userDao的输出，说明userDao成功注入

> book service save …
> book dao save …
> user dao save …

#### 构造器注入多个简单数据类型

需求:在BookDaoImpl中，使用构造函数注入databaseName和connectionNum两个参数。
参考引用数据类型的注入，我们可以推出具体的步骤为:

1. 提供一个包含这两个参数的构造方法
2. 在applicationContext.xml中进行注入配置

- `步骤一：`添加多个简单属性并提供构造方法
  修改BookDaoImpl类，添加构造方法，同时在save()方法中输出这两个属性

```
JAVA
public class BookDaoImpl implements BookDao {

    private String databaseName;
    private int connectionNum;

    public BookDaoImpl(String databaseName, int connectionNum) {
        this.databaseName = databaseName;
        this.connectionNum = connectionNum;
    }

    public void save() {
        System.out.println("book dao save ..." + databaseName + "," + connectionNum);
    }
}
```

- `步骤二：`配置完成多个属性构造器注入

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="userDao" class="com.blog.dao.impl.UserDaoImpl"/>
    <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl">
        <constructor-arg name="databaseName" value="mysql"></constructor-arg>
        <constructor-arg name="connectionNum" value="100"></constructor-arg>
    </bean>
    <bean id="bookService" class="com.blog.service.impl.BookServiceImpl">
        <constructor-arg name="bookDao" ref="bookDao"/>
        <constructor-arg name="userDao" ref="userDao"/>
    </bean>
</beans>
```

- `步骤三：`运行程序

> book service save …
> book dao save …mysql,9421
> user dao save …

#### 目前存在的问题

- `<constructor-arg>`标签内的name，必须与构造函数中的参数名一致，这两块存在紧耦合。
- 那么我们怎么解决这个问题呢？
- 在解决这个问题之前，需要提前说明的是，这个参数名发生变化的情况并不多，所以上面的还是比较主流的配置方式，下面介绍的，我们以了解为主。
- 方式一：删除name属性，添加type属性，按照类型注入
  - 这种方式可以解决构造函数形参名发生变化带来的耦合问题
  - 但是如果构造方法参数中有类型相同的参数，这种方式就不太好实现了

```
XML
<bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl">
    <constructor-arg type="java.lang.String" value="mysql"></constructor-arg>
    <constructor-arg type="int" value="9421"></constructor-arg>
</bean>
```

- 方式二：删除type属性，添加index属性，按照索引下标注入，下标从0开始
  - 这种方式可以解决参数类型重复问题
  - 但是如果构造方法参数顺序发生变化后，这种方式又带来了耦合问题

```
XML
<bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl">
    <constructor-arg index="0" value="mysql"></constructor-arg>
    <constructor-arg index="1" value="9421"></constructor-arg>
</bean>
```

介绍完两种参数的注入方式，具体我们该如何选择呢?

1. 强制依赖使用构造器进行，使用setter注入有概率不进行注入导致null对象出现
   - 强制依赖指对象在创建的过程中必须要注入指定的参数
2. 可选依赖使用setter注入进行，灵活性强
   - 可选依赖指对象在创建过程中注入的参数可有可无
3. Spring框架倡导使用构造器，第三方框架内部大多数采用构造器注入的形式进行数据初始化，相对严谨
4. 如果有必要可以两者同时使用，使用构造器注入完成强制依赖的注入，使用setter注入完成可选依赖的注入
5. 实际开发过程中还要根据实际情况分析，如果受控对象没有提供setter方法就必须使用构造器注入
6. 自己开发的模块推荐使用setter注入

#### 小结

这部分主要讲解的是Spring的依赖注入的实现方式:

- setter注入

  - 简单数据类型

    ```
    XML
    <bean ...>
        <property name="" value=""/>
    </bean>
    ```

  - 引用数据类型

    ```
    XML
    <bean ...>
        <property name="" ref=""/>
    </bean>
    ```

- 构造器注入

  - 简单数据类型

    ```
    XML
    <bean ...>
        <constructor-arg name="" index="" type="" value=""/>
    </bean>
    ```

  - 引用数据类型

    ```
    XML
    <bean ...>
        <constructor-arg name="" index="" type="" ref=""/>
    </bean>
    ```

- 依赖注入的方式选择上

  - 建议使用setter注入
  - 第三方技术根据情况选择

### 自动配置

前面花了大量的时间把Spring的注入去学习了下，总结起来就两个字`麻烦`。

- 问:麻烦在哪?
  - 答:配置文件的编写配置上。
- 问:有更简单方式么?
  - 答:有，自动配置

所以什么是自动配置以及如何实现自动配置，就是接下来要学习的内容

#### 什么是依赖自动装配？

IOC容器根据bean所依赖的资源在容器中`自动查找并注入`到bean中的过程称为自动装配

#### 自动装配方式有哪些？

- 按类型（常用）
- 按名称
- 按构造方法
- 不启用自动装配

#### 环境准备

- 修改BookDao、BookDaoImpl、BookService和BookServiceImpl类

- BookDao
- BookDaoImpl
- BookService
- BookServiceImpl

```
JAVA
public interface BookDao {
    public void save();
}
```



- 配置文件

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl"/>
    <bean id="bookService" class="com.blog.service.impl.BookServiceImpl">
        <property name="bookDao" ref="bookDao"/>
    </bean>
</beans>
```

- App运行类

```
JAVA
public class App {
    public static void main( String[] args ) {
        ApplicationContext ctx = new ClassPathXmlApplicationContext("applicationContext.xml");
        BookService bookService = (BookService) ctx.getBean("bookService");
        bookService.save();
    }
}
```

#### 完成自动装配的配置

自动装配只需要修改applicationContext.xml配置文件即可:

1. 将`<property>`标签删除
2. 在`<bean>`标签中添加autowire属性

- 首先来实现按照类型注入的配置

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<!--    <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl"/>-->
<!--    既然是按类型注入了，那么id写不写都无所谓了-->
    <bean class="com.blog.dao.impl.BookDaoImpl"/>
    <bean id="bookService" class="com.blog.service.impl.BookServiceImpl" autowire="byType"/>
</beans>
```

- 运行程序，结果如下，说明已经成功注入了

> book service save …
> book dao save …

注意事项：

- 需要注入属性的类中对应属性的`setter`方法不能省略
- 被注入的对象必须要被Spring的IOC容器管理
- 按照类型在Spring的IOC容器中如果找到多个对象，会报`NoUniqueBeanDefinitionException`

- 当一个类型在IOC中有多个对象，还想要注入成功，这个时候就需要按照名称注入，配置方式如下

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <!--这里就有两个同一类型的bean，但是id不一样-->
    <bean id="bookDao1" class="com.blog.dao.impl.BookDaoImpl"/>
    <bean id="bookDao2" class="com.blog.dao.impl.BookDaoImpl"/>
    <bean class="com.blog.dao.impl.BookDaoImpl"/>
    <bean id="bookService" class="com.blog.service.impl.BookServiceImpl" autowire="byName"/>
</beans>
```

- 同时修改BookServiceImpl类汇总的`setBookDao`方法，将其重命名为`setBookDao1`

```
JAVA
public class BookServiceImpl implements BookService{
    private BookDao bookDao;

    public void setBookDao1(BookDao bookDao) {
        this.bookDao = bookDao;
    }

    public void save() {
        System.out.println("book service save ...");
        bookDao.save();
    }
}
```

- 运行程序，结果如下，说明已经成功注入了

> book service save …
> book dao save …

- 疑惑：为什么刚刚修改的是setBookDao的方法名，而不是将bookDao属性修改为bookDao1呢？按照名称注入中的名称指的是什么?
- 解惑：
  - 因为bookDao是private修饰的，外部类无法直接访问
  - 所以外部类只能通过属性的set方法进行访问
  - 对外部类来说，setBookDao方法名，去掉set后首字母小写是其属性名
    - 为什么是去掉set首字母小写?
    - 这个规则是set方法生成的`默认规则`，set方法的生成是把属性名首字母大写前面加set形成的方法名
  - 所以按照名称注入，其实是和对应的set方法有关，但是如果按照标准起名称，属性名和set对应的名是一致的

#### 小结

- 如果按照名称去找对应的bean对象，找不到则注入Null
- 当某一个类型在IOC容器中有多个对象，按照名称注入只找其指定名称对应的bean对象，不会报错
- 两种方式介绍完后，以后用的更多的是`按照类型`注入。
- 最后对于依赖注入，需要注意一些其他的配置特征:
  1. 自动装配用于引用类型依赖注入，不能对简单类型进行操作
  2. 使用按类型装配时（byType）必须保障容器中相同类型的bean唯一，推荐使用
  3. 使用按名称装配时（byName）必须保障容器中具有指定名称的bean，因变量名与配置耦合，不推荐使用
  4. 自动装配优先级低于setter注入与构造器注入，同时出现时自动装配配置失效

### 集合注入

前面我们已经能完成引入数据类型和简单数据类型的注入，但是还有一种数据类型`集合`，集合中既可以装简单数据类型也可以装引用数据类型，对于集合，在Spring中该如何注入呢?

先来回顾下，常见的集合类型有哪些?

- 数组
- List
- Set
- Map
- Properties

针对不同的集合类型，该如何实现注入呢?接着往下看

#### 环境准备

- 修改BookDaoImpl类

- BookDao
- BookDaoImpl

```
JAVA
public interface BookDao {
    public void save();
}
```



- 修改配置文件

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl"/>
</beans>
```

- 修改App运行时类

```
JAVA
public class App {
    public static void main( String[] args ) {
        ApplicationContext ctx = new ClassPathXmlApplicationContext("applicationContext.xml");
        BookDao bookDao = (BookDao) ctx.getBean("bookDao");
        bookDao.save();
    }
}
```

- 准备工作完毕，接下来，在上面这个环境中来完成`集合注入`的学习，下面所有的配置方式，都是在bookDao的bean标签中使用`<property>`进行注入

#### 注入数组类型

```
XML
<property name="array">
    <array>
        <value>100</value>
        <value>200</value>
        <value>300</value>
    </array>
</property>
```

#### 注入List类型

```
XML
<property name="list">
    <list>
        <value>张三</value>
        <value>ABC</value>
        <value>123</value>
    </list>
</property>
```

#### 注入Set类型

```
XML
<property name="set">
    <set>
        <value>100</value>
        <value>200</value>
        <value>ABC</value>
        <value>ABC</value>
    </set>
</property>
```

#### 注入Map类型

```xml

<property name="map">
    <map>
        <entry key="探路者" value="马文"/>
        <entry key="次元游记兵" value="恶灵"/>
        <entry key="易位窃贼" value="罗芭"/>
    </map>
</property>
```

#### 注入Properties类型

```
XML
<property name="properties">
    <props>
        <prop key="暴雷">沃尔特·菲茨罗伊</prop>
        <prop key="寻血猎犬">布洛特·亨德尔</prop>
        <prop key="命脉">阿杰·切</prop>
    </props>
</property>
```

配置完成之后，运行查看结果

> book dao save …
> 遍历数组:[100, 200, 300]
> 遍历List[张三, ABC, 123]
> 遍历Set[100, 200, ABC]
> 遍历Map{探路者=马文, 次元游记兵=恶灵, 易位窃贼=罗芭}
> 遍历Properties{命脉=阿杰·切, 寻血猎犬=布洛特·亨德尔, 暴雷=沃尔特·菲茨罗伊}

说明：

- property标签表示setter方式注入，构造方式注入constructor-arg标签内部也可以写`<array>`、`<list>`、`<set>`、`<map>`、`<props>`标签
- List的底层也是通过数组实现的，所以`<list>`和`<array>`标签是可以混用
- 集合中要添加引用类型，只需要把`<value>`标签改成`<ref>`标签，这种方式用的比较少

## IOC/DI配置管理第三方bean

前面所讲的知识点都是基于我们自己写的类，现在如果有需求让我们去管理第三方jar包中的类，该如何管理?

### 案例:数据源对象管理

本次案例将使用之前学过的数据源`Druid`来配置学习下

#### 环境准备

1. 创建一个Maven项目
2. 在pom.xml添加依赖

```
XML
<dependencies>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>5.2.10.RELEASE</version>
    </dependency>
</dependencies>
```

1. resources下添加spring的配置文件applicationContext.xml

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

</beans>
```

1. 编写一个运行类App

```
JAVA
public class App {
    public static void main(String[] args) {
        ApplicationContext ctx = new ClassPathXmlApplicationContext("applicationContext.xml");
    }
}
```

#### 思路分析

在上述环境下，我们来对数据源进行配置管理，先来分析下思路

需求：使用Spring的IOC容器来管理Druid连接池对象

1. 使用第三方的技术，需要在pom.xml添加依赖
2. 在配置文件中将`第三方的类`制作成一个bean，让IOC容器进行管理
3. 数据库连接需要基础的四要素`驱动`、`连接`、`用户名`和`密码`，`如何注入`到对应的bean中
4. 从IOC容器中获取对应的bean对象，将其打印到控制台查看结果

思考:

- 第三方的类指的是什么?
- 如何注入数据库连接四要素?

#### 实现Druid管理

带着这两个问题，把下面的案例实现下

- `步骤一：`导入druid依赖

```
XML
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid</artifactId>
    <version>1.1.16</version>
</dependency>
```

- `步骤二：`配置第三方bean
  那么到底是使用setter注入还是构造器注入呢？
  这个就需要我们来看看第三方类给我们提供了什么
  通过查看源码，我们发现`DruidDataSource`只给我们提供了两个构造器如下

```
JAVA
public DruidDataSource()

public DruidDataSource(boolean fairLock) 
```

显然这两个构造器不能满足我们的需求，因为我们需要注入数据库连接的四要素，构造器的参数中没有提供
那么我们继续来看看给我们提供了什么setter方法

```
JAVA
public void setUsername(String username) {
    if (!StringUtils.equals(this.username, username)) {
        if (this.inited) {
            throw new UnsupportedOperationException();
        } else {
            this.username = username;
        }
    }
}

public void setPassword(String password) {
    if (!StringUtils.equals(this.password, password)) {
        if (this.inited) {
            LOG.info("password changed");
        }

        this.password = password;
    }
}

···
```

通过查看源码，我们发现已经给我们提供了许多的setter方法，其中包括了连接四要素，所以这里我们需要使用setter注入
在applicationContext.xml配置文件中添加`DruidDataSource`的配置

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
            http://www.springframework.org/schema/beans
            http://www.springframework.org/schema/beans/spring-beans.xsd">
    <!--管理DruidDataSource对象-->
    <bean class="com.alibaba.druid.pool.DruidDataSource">
        <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
        <property name="url" value="jdbc:mysql://localhost:13306/spring_db"/>
        <property name="username" value="root"/>
        <property name="password" value="yourPassword"/>
    </bean>
</beans>
```

- `步骤三：`从IOC容器中获取对应的bean对象

```
JAVA
public class App {
    public static void main(String[] args) {
       ApplicationContext ctx = new ClassPathXmlApplicationContext("applicationContext.xml");
       DruidDataSource dataSource = context.getBean(DruidDataSource.class);
       System.out.println(dataSource);
    }
}
```

- `步骤四：`运行程序
  打印如下结果: 说明第三方bean对象已经被spring的IOC容器进行管理

> {
> CreateTime:“2022-09-01 10:15:19”,
> ActiveCount:0,
> PoolingCount:0,
> CreateCount:0,
> DestroyCount:0,
> CloseCount:0,
> ConnectCount:0,
> Connections:[
> ]
> }

做完案例后，我们来解答一下上面的思考

- 第三方的类指的是什么?
  - `DruidDataSource`
- 如何注入数据库连接四要素?
  - `setter注入`

### 加载properties文件

刚刚我们完成了druid数据源的配置，但其中包含了一些问题，我们来分析一下：

- 这两个数据源中都用到了一些固定的常量（如数据库连接四要素），把这些值加载到Spring的配置文件中，不利于后期的维护
- 那我们现在就需要将这些值提取到一个外部的properties配置文件中，在之前我们也是这样做的
- 那么如何在Spring框架中读取配置文件来进行配置，就是我们接下来要解决的问题

#### 第三方bean属性优化

需求:将数据库连接四要素提取到properties配置文件，spring来加载配置信息并使用这些信息来完成属性注入。

1. 在resources下创建一个jdbc.properties(文件的名称可以任意)
2. 将数据库连接四要素配置到配置文件中
3. 在Spring的配置文件中加载properties文件
4. 使用加载到的值实现属性注入

- `步骤一：`准备properties配置文件
  resources下创建一个jdbc.properties文件,并添加对应的属性键值对

```
PROPERTIES
jdbc.driverClass=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/spring_db
jdbc.username=root
jdbc.password=password
```

- `步骤二：`开启`context`命名空间
  在applicationContext.xml中开`context`命名空间

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="
            http://www.springframework.org/schema/beans
            http://www.springframework.org/schema/beans/spring-beans.xsd
            http://www.springframework.org/schema/context
            http://www.springframework.org/schema/context/spring-context.xsd
        ">
</beans>
```

- `步骤三：`加载properties配置文件
  在配置文件中使用`context`命名空间下的标签来加载properties配置文件

```
XML
<context:property-placeholder location="jdbc.properties"/>
```

- `步骤四：`完成属性注入
  使用`${key}`来读取properties配置文件中的内容并完成属性注入

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="
            http://www.springframework.org/schema/beans
            http://www.springframework.org/schema/beans/spring-beans.xsd
            http://www.springframework.org/schema/context
            http://www.springframework.org/schema/context/spring-context.xsd
        ">
    <context:property-placeholder location="jdbc.properties"/>
    <bean id="dataSource" class="com.alibaba.druid.pool.DruidDataSource">
        <property name="driverClassName" value="${jdbc.driverClass}"/>
        <property name="url" value="${jdbc.url}"/>
        <property name="username" value="${jdbc.username}"/>
        <property name="password" value="${jdbc.password}"/>
    </bean>
</beans>
```

至此，读取外部properties配置文件中的内容就已经完成。

#### 读取单个属性

对于上面的案例，我们看不出实际的效果，那我们试着读取properties中的属性，然后输出在控制台看看

需求：从properties配置文件中读取key为name的值，并将其注入到BookDao中并在save方法中进行打印。

1. 在项目中添加BookDao和BookDaoImpl类
2. 为BookDaoImpl添加一个name属性并提供setter方法
3. 在jdbc.properties中添加数据注入到bookDao中打印方便查询结果
4. 在applicationContext.xml添加配置完成配置文件加载、属性注入(${key})

- `步骤一：`在项目中添对应的类
  BookDao和BookDaoImpl类，并在BookDaoImpl类中添加`name`属性与setter方法

```
JAVA
public class BookDaoImpl implements BookDao {
    private String name;

    public void setName(String name) {
        this.name = name;
    }

    public void save() {
        System.out.println("book dao save ..." + name);
    }
}
```

- `步骤二：`完成配置文件的读取与注入
  在applicationContext.xml添加配置，`bean的配置管理`、`读取外部properties`、`依赖注入`:

```
XML
<bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl">
    <property name="name" value="${jdbc.url}"/>
</bean>
```

- `步骤三：`运行程序
  在App类中，从IOC容器中获取bookDao对象，调用方法，查看值是否已经被获取到并打印控制台

```
JAVA
public class App {
    public static void main(String[] args) {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        BookDao bookDao = (BookDao) context.getBean("bookDao");
        bookDao.save();
    }
}
```

运行结果如下，说明已经成功获取到了值

> book dao save …jdbc:mysql://localhost:13306/spring_db

- `注意事项`
  至此，读取properties配置文件中的内容就已经完成，但是在使用的时候，有些注意事项:

- 问题一：键值对的key为

  ```
  username
  ```

  引发的问题

  - 在properties中配置键值对的时候，如果key设置为`username`

  ```
  PROPERTIES
  username=root
  ```

  - 在applicationContext.xml注入该属性

  ```
  XML
  <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl">
      <property name="name" value="${username}"/>
  </bean>
  ```

  - 运行后，在控制台打印的不是`root`，而是自己电脑的用户名

  > book dao save …Kyle

  - 出现问题的原因是`<context:property-placeholder/>`标签会加载系统的环境变量，而且环境变量的值会被优先加载，下面的代码可以输出系统环境变量

  ```
  JAVA
  public static void main(String[] args) throws Exception{
      Map<String, String> env = System.getenv();
      System.out.println(env);
  }
  ```

  打印出来的结果中会有一个USERNAME=XXX[自己电脑的用户名称]

  - 解决方案，将system-properties-mode设置为NEVER，表示不加载系统环境变量，这样就可以解决上面的问题了，当然还有一个解决方案就是避免使用`username`作为属性的`key`。

  ```
  XML
  <context:property-placeholder location="jdbc.properties" system-properties-mode="NEVER"/>
  ```

- 问题二：当有多个properties配置文件需要被加载，该如何配置?

  - 修改applicationContext.xml

  ```
  XML
  <!--方式一 -->
  <context:property-placeholder location="jdbc.properties,jdbc2.properties" system-properties-mode="NEVER"/>
  <!--方式二-->
  <context:property-placeholder location="*.properties" system-properties-mode="NEVER"/>
  <!--方式三 -->
  <context:property-placeholder location="classpath:*.properties" system-properties-mode="NEVER"/>
  <!--方式四-->
  <context:property-placeholder location="classpath*:*.properties" system-properties-mode="NEVER"/>
  ```

  - 说明：
    - 方式一：可以实现，如果配置文件多的话，每个都需要配置
    - 方式二：`*.properties`代表所有以properties结尾的文件都会被加载，可以解决方式一的问题，但是不标准
    - 方式三：标准的写法，`classpath:`代表的是从根路径下开始查找，但是只能查询当前项目的根路径
    - 方式四：不仅可以加载当前项目还可以加载当前项目所依赖的所有项目的根路径下的properties配置文件

#### 小结

- 如何开启`context`命名空间

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="
            http://www.springframework.org/schema/beans
            http://www.springframework.org/schema/beans/spring-beans.xsd
            http://www.springframework.org/schema/context
            http://www.springframework.org/schema/context/spring-context.xsd
        ">
```

- 如何加载properties配置文件

```
XML
<context:property-placeholder location="" system-properties-mode="NEVER"/>
```

- 如何在applicationContext.xml引入properties配置文件中的值
  - `${key}`

## 核心容器

前面已经完成bean与依赖注入的相关知识学习，接下来我们主要学习的是IOC容器中的`核心容器`。

这里所说的核心容器，我们可以把它简单的理解为`ApplicationContext`，前面虽然已经用到过，但是并没有系统的学习，接下来我们从以下几个问题入手来学习下容器的相关知识:

- 如何创建容器?
- 创建好容器后，如何从容器中获取bean对象?
- 容器类的层次结构是什么?
- BeanFactory是什么?

### 环境准备

- 创建一个Maven项目
- pom.xml添加Spring的依赖

```
XML
<dependencies>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>5.2.10.RELEASE</version>
    </dependency>
</dependencies>
```

- resources下添加applicationContext.xml

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
            http://www.springframework.org/schema/beans
            http://www.springframework.org/schema/beans/spring-beans.xsd
        ">
    <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl"/>
</beans>
```

- 添加BookDao和BookDaoImpl类

- BookDao
- BookDaoImpl

```
JAVA
public interface BookDao {
    public void save();
}
```



- 创建运行类App

```
JAVA
public class App {
    public static void main(String[] args) {
        ApplicationContext ctx = new ClassPathXmlApplicationContext("applicationContext.xml");
        BookDao bookDao = (BookDao) ctx.getBean("bookDao");
        bookDao.save();
    }
}
```

### 容器

#### 容器的创建方式

- 案例中创建`ApplicationContext`的方式如下
- 这种方式翻译为：类路径下的XML配置文件

```
JAVA
ApplicationContext ctx = new ClassPathXmlApplicationContext("applicationContext.xml");
```

- 除了上面这种方式，Spring还提供了另外一种创建方式
- 这种方式翻译为：文件系统下的XML配置文件，路径需要写绝对路径
- 这种方式虽能实现，但是当项目的位置发生变化后，代码也需要跟着改，耦合度高，不推荐使用。

```
JAVA
ApplicationContext ctx = new FileSystemXmlApplicationContext("D:\xxx/xxx\applicationContext.xml");
```

#### 获取bean的三种方式

- 方式一，就是我们之前用的方式
- 这种方式存在的问题是每次获取的时候都需要进行类型转换，有没有更简单的方式呢?

```
JAVA
BookDao bookDao = (BookDao) ctx.getBean("bookDao");
```

- 方式二
  这种方式可以解决类型强转问题，但是参数又多加了一个，相对来说没有简化多少。

```
JAVA
BookDao bookDao = ctx.getBean("bookDao"，BookDao.class);
```

- 方式三
- 这种方式就类似我们之前所学习依赖注入中的按类型注入。必须要确保IOC容器中该类型对应的bean对象只能有一个。

```
JAVA
BookDao bookDao = ctx.getBean(BookDao.class);
```

#### BeanFactory的使用

容器的最上级的父接口为`BeanFactory`
使用`BeanFactory`也可以创建IOC容器

```
JAVA
public class AppForBeanFactory {
    public static void main(String[] args) {
        Resource resources = new ClassPathResource("applicationContext.xml");
        BeanFactory bf = new XmlBeanFactory(resources);
        BookDao bookDao = bf.getBean(BookDao.class);
        bookDao.save();
    }
}
```

为了更好的看出`BeanFactory`和`ApplicationContext`之间的区别，在BookDaoImpl添加如下构造函数

```
JAVA
public class BookDaoImpl implements BookDao {
    public BookDaoImpl() {
        System.out.println("constructor");
    }
    public void save() {
        System.out.println("book dao save ..." );
    }
}
```

如果不去获取bean对象，打印会发现：

- BeanFactory是延迟加载，只有在获取bean对象的时候才会去创建
- ApplicationContext是立即加载，容器加载的时候就会创建bean对象
- ApplicationContext要想成为延迟加载，只需要将lazy-init设为true

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
            http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl"  lazy-init="true"/>
</beans>
```

### 核心容器总结

#### 容器相关

- BeanFactory是IoC容器的顶层接口，初始化BeanFactory对象时，加载的bean延迟加载
- ApplicationContext接口是Spring容器的核心接口，初始化时bean立即加载
- ApplicationContext接口提供基础的bean操作相关方法，通过其他接口扩展其功能
- ApplicationContext接口常用初始化类
  - ClassPathXmlApplicationContext(常用)
  - FileSystemXmlApplicationContext

#### bean相关

[![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://pic.imgdb.cn/item/631070e616f2c2beb1536517.jpg)

#### 依赖注入相关

[![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://pic.imgdb.cn/item/631070f716f2c2beb1536fa3.jpg)

## IOC/DI注解开发

Spring的IOC/DI对应的配置开发就已经讲解完成，但是使用起来相对来说还是比较复杂的，复杂的地方在`配置文件`。
Spring到底是如何简化代码开发的呢?
要想真正简化开发，就需要用到Spring的注解开发，Spring对注解支持的版本历程:

- 2.0版开始支持注解
- 2.5版注解功能趋于完善
- 3.0版支持纯注解开发

关于注解开发，这里会讲解两块内容`注解开发定义bean`和`纯注解开发`。
注解开发定义bean用的是2.5版提供的注解，纯注解开发用的是3.0版提供的注解。

### 环境准备

- 创建一个Maven项目
- pom.xml添加Spring的依赖

```
XML
<dependencies>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>5.2.10.RELEASE</version>
    </dependency>
</dependencies>
```

- resources下添加applicationContext.xml

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="
            http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl"/>
</beans>
```

- 添加BookDao、BookDaoImpl、BookService、BookServiceImpl类

- BookDao
- BookDaoImpl
- BookService
- BookServiceImpl

```
JAVA
public interface BookDao {
    public void save();
}
```



- 创建运行类App

```
JAVA
public class App {
    public static void main(String[] args) {
        ApplicationContext ctx = new ClassPathXmlApplicationContext("applicationContext.xml");
        BookDao bookDao = (BookDao) ctx.getBean("bookDao");
        bookDao.save();
    }
}
```

### 注解开发定义bean

- `步骤一：`删除原有的XML配置
  将配置文件中的bean标签删除掉

```
XML
<bean id="bookDao" class="com.blog.dao.impl.BookDaoImpl"/>
```

- `步骤二：`在Dao上添加注解
  在BookDaoImpl类上添加`@Component`注解

```
JAVA
@Component("bookDao")
public class BookDaoImpl implements BookDao {
    public void save() {
        System.out.println("book dao save ...");
    }
}
```

注意：@Component注解不可以添加在接口上，因为接口是无法创建对象的。

- `步骤三：`配置Spring的注解包扫描
  为了让Spring框架能够扫描到写在类上的注解，需要在配置文件上进行包扫描

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="
            http://www.springframework.org/schema/beans
            http://www.springframework.org/schema/beans/spring-beans.xsd
            http://www.springframework.org/schema/context
            http://www.springframework.org/schema/context/spring-context.xsd
        ">
    <context:component-scan base-package="com.blog"/>
</beans>
```

- 说明：component-scan
  - component:组件,Spring将管理的bean视作自己的一个组件
  - scan:扫描
    base-package指定Spring框架扫描的包路径，它会扫描指定包及其子包中的所有类上的注解。
  - 包路径越多`如:com.blog.dao.impl`，扫描的范围越小速度越快
  - 包路径越少`如:com.blog`,扫描的范围越大速度越慢
  - 一般扫描到项目的组织名称即Maven的groupId下`如:com.blog`即可。
- `步骤四：`运行程序

> book dao save …

- `步骤五：`Service上添加注解
  在BookServiceImpl类上也添加`@Component`交给Spring框架管理

```
JAVA
@Component
public class BookServiceImpl implements BookService {
    public void save() {
        System.out.println("book service save ...");
    }
}
```

- `步骤六：`运行程序
  在App类中，从IOC容器中获取BookServiceImpl对应的bean对象

```
JAVA
public class App {
    public static void main(String[] args) {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        //按照名称获取bean
        BookDao bookDao = (BookDao) context.getBean("bookDao");
        //按照类型获取bean
        BookService bookService = context.getBean(BookService.class);
        bookDao.save();
        bookService.save();
    }
}
```

结果如下

> book dao save …
> book service save …

**说明:**

- BookServiceImpl类没有起名称，所以在App中是按照类型来获取bean对象
- `@Component`注解如果不起名称，会有一个默认值就是`当前类名首字母小写`，所以也可以按照名称获取，如

```
JAVA
BookService bookService = (BookService) context.getBean("bookServiceImpl");
```

对于@Component注解，还衍生出了其他三个注解`@Controller`、`@Service`、`@Repository`
通过查看源码会发现：这三个注解和@Component注解的作用是一样的，为什么要衍生出这三个呢?
这是方便我们后期在编写类的时候能很好的区分出这个类是属于`表现层`、`业务层`还是`数据层`的类。

### 纯注解开发模式

上面已经可以使用注解来配置bean,但是依然有用到配置文件，在配置文件中对包进行了扫描，Spring在3.0版已经支持纯注解开发，使用Java类替代配置文件，开启了Spring快速开发赛道，那么具体如何实现?

#### 思路分析

实现思路为：

- 将配置文件applicationContext.xml删掉，用类来替换

#### 实现步骤

- `步骤一：`创建配置类
  创建一个配置类SpringConfig

```
JAVA
public class SpringConfig {
}
```

- `步骤二：`标识该类为配置类
  在配置类上面加一个`@Configuration`注解，将其标识为一个配置类，用于替换掉`applicationContext.XML`

```
JAVA
@Configuration
public class SpringConfig {
}
```

- `步骤三：`用注解替换包扫描配置
  在配置类上添加包扫描注解`@ComponentScan`替换`<context:component-scan base-package=""/>`

```
JAVA
@Configuration
@ComponentScan("com.blog")
public class SpringConfig {
}
```

- `步骤四：`创建运行类并执行
  创建一个新的运行类`AppForAnnotation`

```
JAVA
public class AppForAnnotation {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfig.class);
        BookDao bookDao = (BookDao) context.getBean("bookDao");
        bookDao.save();
        BookService bookService = context.getBean(BookService.class);
        bookService.save();
    }
}
```

运行AppForAnnotation,可以看到两个对象依然被获取成功

> book dao save …
> book service save …

至此，纯注解开发的方式就已经完成了，主要内容包括：

- Java类替换Spring核心配置文件

  - `@Configuration`注解用于设定当前类为配置类
  - `@ComponentScan`注解用于设定扫描路径，此注解只能添加一次，多个数据请用数组格式

  ```
  JAVA
  @ComponentScan({com.blog.service","com.blog.dao"})
  ```

- 读取Spring核心配置文件初始化容器对象切换为读取Java配置类初始化容器对象

```
JAVA
AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfig.class);
```

- 知识点：`@Configuration`

| 名称 |       @Configuration        |
| :--: | :-------------------------: |
| 类型 |           类注解            |
| 位置 |         类定义上方          |
| 作用 |   设置该类为spring配置类    |
| 属性 | value（默认）：定义bean的id |

- 知识点：`@ComponentScan`

| 名称 |                      @ComponentScan                      |
| :--: | :------------------------------------------------------: |
| 类型 |                          类注解                          |
| 位置 |                        类定义上方                        |
| 作用 | 设置spring配置类扫描路径，用于加载使用注解格式定义的bean |
| 属性 |     value（默认）：扫描路径，此路径可以逐层向下扫描      |

#### 小结

这部分要重点掌握的是使用注解完成Spring的bean管理，需要掌握的内容为:

- 记住`@Component`、`@Controller`、`@Service`、`@Repository`这四个注解
- applicationContext.xml中`<context:component-san/>`的作用是指定扫描包路径，注解为`@ComponentScan`
- `@Configuration`标识该类为配置类，使用类替换`applicationContext.xml`文件
- `ClassPathXmlApplicationContext`是加载XML配置文件
- `AnnotationConfigApplicationContext`是加载配置类

### 注解开发bean的作用范围和生命周期

使用注解已经完成了bean的管理，接下来按照前面所学习的内容，将通过配置实现的内容都换成对应的注解实现，包含两部分内容:`bean作用范围(scope)`和`bean生命周期(init和destroy)`。

#### bean的作用范围

- 修改`AppForAnnotation`类，并运行查看结果

```
JAVA
public class AppForAnnotation {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfig.class);
        BookDao bookDao1 = (BookDao) context.getBean("bookDao");
        BookDao bookDao2 = (BookDao) context.getBean("bookDao");
        System.out.println(bookDao1);
        System.out.println(bookDao2);
    }
}
```

- 结果如下，说明默认情况下bean是单例

> com.blog.dao.impl.BookDaoImpl@77e4c80f
> com.blog.dao.impl.BookDaoImpl@77e4c80f

- 要想将BookDaoImpl变成非单例，只需要在其类上添加`@scope`注解

```
JAVA
@Component("bookDao")
@Scope("prototype")
public class BookDaoImpl implements BookDao {
    public void save() {
        System.out.println("book dao save ...");
    }
}
```

- 再次运行程序，查看结果，输出的两个地址值不一致，说明已经成功变为非单例的了

> com.blog.dao.impl.BookDaoImpl@176d53b2
> com.blog.dao.impl.BookDaoImpl@971d0d8

知识点：`@scope`

| 名称 |                            @Scope                            |
| :--: | :----------------------------------------------------------: |
| 类型 |                            类注解                            |
| 位置 |                          类定义上方                          |
| 作用 | 设置该类创建对象的作用范围，可用于设置创建出的bean是否为单例对象 |
| 属性 | value（默认）：定义bean作用范围，默认值singleton（单例），可选值prototype（非单例） |

#### bean的生命周期

- 在BookDaoImpl中添加两个方法，`init`和`destroy`，方法名可以任意，再添加一个构造方法

```
JAVA
@Component("bookDao")
public class BookDaoImpl implements BookDao {
    
    public BookDaoImpl() {
        System.out.println("construct ... ");
    }

    public void save() {
        System.out.println("book dao save ...");
    }

    public void init() {
        System.out.println("init ... ");
    }

    public void destroy() {
        System.out.println("destroy ... ");
    }
}
```

- 如何对方法进行标识，哪个是初始化方法，哪个是销毁方法?
  只需要在对应的方法上添加`@PostConstruct`和`@PreDestroy`注解即可。

```
JAVA
@Component("bookDao")
public class BookDaoImpl implements BookDao {

    public BookDaoImpl() {
        System.out.println("construct ... ");
    }

    public void save() {
        System.out.println("book dao save ...");
    }

    @PostConstruct  // 在构造方法之后执行，替换 init-method
    public void init() {
        System.out.println("init ... ");
    }

    @PreDestroy // 在销毁方法之前执行,替换 destroy-method
    public void destroy() {
        System.out.println("destroy ... ");
    }
}
```

- 要想看到两个方法执行，需要注意的是`destroy`只有在容器关闭的时候，才会执行，所以需要修改App的类

```
JAVA
public class AppForAnnotation {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfig.class);
        BookDao bookDao = (BookDao) context.getBean("bookDao");
        System.out.println(bookDao);
        context.registerShutdownHook();//关闭容器
    }
}
```

- 运行AppForAnnotation类查看打印结果，证明init和destroy方法都被执行了，且init确实是在构造方法后执行的。

> construct …
> init …
> com.blog.dao.impl.BookDaoImpl@971d0d8
> destroy …

注意：JDK8版本以上，如果找不到`@PostConstruct`和`@PreDestroy`注解，需要导入下面的jar包

```
XML
<dependency>
  <groupId>javax.annotation</groupId>
  <artifactId>javax.annotation-api</artifactId>
  <version>1.3.2</version>
</dependency>
```

找不到的原因是，从JDK9以后jdk中的javax.annotation包被移除了，这两个注解刚好就在这个包中。

知识点`@PostConstruct`

| 名称 |     @PostConstruct     |
| :--: | :--------------------: |
| 类型 |        方法注解        |
| 位置 |         方法上         |
| 作用 | 设置该方法为初始化方法 |
| 属性 |           无           |

知识点`PreDestroy`

| 名称 |     @PreDestroy      |
| :--: | :------------------: |
| 类型 |       方法注解       |
| 位置 |        方法上        |
| 作用 | 设置该方法为销毁方法 |
| 属性 |          无          |

#### 小结

配置文件中的bean标签中的
`id`对应`@Component("")`，`@Controller("")`，`@Service("")`，`@Repository("")`
`scope`对应`@scope()`
`init-method`对应`@PostConstruct`
`destroy-method`对应`@PreDestroy`

### 注解开发依赖注入

Spring为了使用注解简化开发，并没有提供`构造函数注入`、`setter注入`对应的注解，只提供了自动装配的注解实现。

#### 环境准备

- 创建一个Maven项目

- pom.xml添加Spring的依赖

  ```
  XML
  <dependencies>
      <dependency>
          <groupId>org.springframework</groupId>
          <artifactId>spring-context</artifactId>
          <version>5.2.10.RELEASE</version>
      </dependency>
  </dependencies>
  ```

- 添加一个配置类`SpringConfig`

```
JAVA
@Configuration
@ComponentScan("com.blog")
public class SpringConfig {
}
```

- 添加BookDao、BookDaoImpl、BookService、BookServiceImpl类

- BookDao
- BookDaoImpl
- BookService
- BookServiceImpl

```
JAVA
public interface BookDao {
    public void save();
}
```



- 创建运行类AppForAnnotation

```
JAVA
public class App {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext(SpringConfig.class);
        BookService bookService = ctx.getBean(BookService.class);
        bookService.save();
    }
}
```

- 环境准备好后，直接运行App类会有问题，因为还没有提供配置注入BookDao的，所以bookDao对象为Null,调用其save方法就会报`控指针异常`。

#### 注解实现按照类型注入

对于这个问题使用注解该如何解决?

- 在BookServiceImpl类的bookDao属性上添加`@Autowired`注解

```
JAVA
@Service
public class BookServiceImpl implements BookService {
    @Autowired
    private BookDao bookDao;

//    public void setBookDao(BookDao bookDao) {
//        this.bookDao = bookDao;
//    }

    public void save() {
        System.out.println("book service save ...");
        bookDao.save();
    }
}
```

**注意:**

- `@Autowired`可以写在属性上，也可也写在setter方法上，最简单的处理方式是`写在属性上并将setter方法删除掉`
- 为什么setter方法可以删除呢?
  - 自动装配基于反射设计创建对象并通过`暴力反射`为私有属性进行设值
  - 普通反射只能获取public修饰的内容
  - 暴力反射除了获取public修饰的内容还可以获取private修改的内容
  - 所以此处无需提供setter方法

- `@Autowired`是按照类型注入，那么对应BookDao接口如果有多个实现类，比如添加BookDaoImpl2

```
JAVA
@Repository
public class BookDaoImpl2 implements BookDao {
    public void save() {
        System.out.println("book dao save ...2");
    }
}
```

这个时候再次运行App，就会报错`NoUniqueBeanDefinitionException`
此时，按照类型注入就无法区分到底注入哪个对象，解决方案:`按照名称注入`

- 先给两个Dao类分别起个名称

```
JAVA
@Repository("bookDao")
public class BookDaoImpl implements BookDao {
    public void save() {
        System.out.println("book dao save ..." );
    }
}
@Repository("bookDao2")
public class BookDaoImpl2 implements BookDao {
    public void save() {
        System.out.println("book dao save ...2" );
    }
}
```

此时就可以注入成功，但是得思考个问题:

- @Autowired是按照类型注入的，给BookDao的两个实现起了名称，它还是有两个bean对象，为什么不报错?
- @Autowired默认按照类型自动装配，如果IOC容器中同类的Bean找到多个，就按照变量名和Bean的名称匹配。因为变量名叫`bookDao`而容器中也有一个`booDao`，所以可以成功注入。
- 那下面这种情况可以成功注入吗

```
JAVA
@Repository("bookDao1")
public class BookDaoImpl implements BookDao {
    public void save() {
        System.out.println("book dao save ..." );
    }
}
@Repository("bookDao2")
public class BookDaoImpl2 implements BookDao {
    public void save() {
        System.out.println("book dao save ...2" );
    }
}
```

还是不行的，因为按照类型会找到多个bean对象，此时会按照`bookDao`名称去找，因为IOC容器只有名称叫`bookDao1`和`bookDao2`，所以找不到，会报`NoUniqueBeanDefinitionException`

#### 注解实现按照名称注入

当根据类型在容器中找到多个bean,注入参数的属性名又和容器中bean的名称不一致，这个时候该如何解决，就需要使用到`@Qualifier`来指定注入哪个名称的bean对象。`@Qualifier`注解后的值就是需要注入的bean的名称。

```
JAVA
@Service
public class BookServiceImpl implements BookService {
    @Autowired
    @Qualifier("bookDao1")
    private BookDao bookDao;
    
    public void save() {
        System.out.println("book service save ...");
        bookDao.save();
    }
}
```

注意:@Qualifier不能独立使用，必须和@Autowired一起使用

#### 简单数据类型注入

- 引用类型看完，简单类型注入就比较容易懂了。简单类型注入的是基本数据类型或者字符串类型，下面在`BookDaoImpl`类中添加一个`name`属性，用其进行简单类型注入

```
JAVA
@Repository
public class BookDaoImpl implements BookDao {
    private String name;
    public void save() {
        System.out.println("book dao save ..." + name);
    }
}
```

- 数据类型换了，对应的注解也要跟着换，这次使用`@Value`注解，将值写入注解的参数中就行了

```
JAVA
@Repository
public class BookDaoImpl implements BookDao {
    @Value("Stephen")
    private String name;
    public void save() {
        System.out.println("book dao save ..." + name);
    }
}
```

注意数据格式要匹配，如将"abc"注入给int值，这样程序就会报错。
介绍完后，会有一种感觉就是这个注解好像没什么用，跟直接赋值是一个效果，还没有直接赋值简单，所以这个注解存在的意义是什么?继续往下看

#### 注解读取properties配置文件

`@Value`一般会被用在从properties配置文件中读取内容进行使用，具体如何实现?

- `步骤一：`在resource下准备一个properties文件

```
PROPERTIES
name=Stephen
```

- `步骤二：`使用注解加载properties配置文件
  在配置类上添加`@PropertySource`注解

```
JAVA
@Configuration
@ComponentScan("com.blog")
@PropertySource("jdbc.properties")
public class SpringConfig {
}
```

- `步骤三：`使用@Value读取配置文件中的内容

```
JAVA
@Repository
public class BookDaoImpl implements BookDao {
    @Value("${name}")
    private String name;
    public void save() {
        System.out.println("book dao save ..." + name);
    }
}
```

- `步骤四：`运行程序
  运行App类，查看运行结果，说明配置文件中的内容已经被加载

> book service save …
> book dao save …Stephen

**注意:**

- 如果读取的properties配置文件有多个，可以使用`@PropertySource`的属性来指定多个

```
JAVA
@PropertySource({"jdbc.properties","xxx.properties"})
```

- `@PropertySource`注解属性中不支持使用通配符`*`,运行会报错

```
JAVA
@PropertySource({"*.properties"})
```

- `@PropertySource`注解属性中可以把`classpath:`加上,代表从当前项目的根路径找文件

```
JAVA
@PropertySource({"classpath:jdbc.properties"})
```

知识点1：`@Autowired`

| 名称 |                          @Autowired                          |
| :--: | :----------------------------------------------------------: |
| 类型 |     属性注解 或 方法注解（了解） 或 方法形参注解（了解）     |
| 位置 | 属性定义上方 或 标准set方法上方 或 类set方法上方 或 方法形参前面 |
| 作用 |                     为引用类型属性设置值                     |
| 属性 |        required：true/false，定义该属性是否允许为null        |

知识点2：`@Qualifier`

| 名称 |                    @Qualifier                    |
| :--: | :----------------------------------------------: |
| 类型 |           属性注解 或 方法注解（了解）           |
| 位置 | 属性定义上方 或 标准set方法上方 或 类set方法上方 |
| 作用 |          为引用类型属性指定注入的beanId          |
| 属性 |         value（默认）：设置注入的beanId          |

知识点3：`@Value`

| 名称 |                      @Value                      |
| :--: | :----------------------------------------------: |
| 类型 |           属性注解 或 方法注解（了解）           |
| 位置 | 属性定义上方 或 标准set方法上方 或 类set方法上方 |
| 作用 |     为 基本数据类型 或 字符串类型 属性设置值     |
| 属性 |          value（默认）：要注入的属性值           |

知识点4：`@PropertySource`

| 名称 |                       @PropertySource                        |
| :--: | :----------------------------------------------------------: |
| 类型 |                            类注解                            |
| 位置 |                          类定义上方                          |
| 作用 |                 加载properties文件中的属性值                 |
| 属性 | value（默认）：设置加载的properties文件对应的文件名或文件名组成的数组 |

## IOC/DI注解开发管理第三方bean

前面定义bean的时候都是在自己开发的类上面写个注解就完成了，但如果是第三方的类，这些类都是在jar包中，我们没有办法在类上面添加注解，这个时候该怎么办?

遇到上述问题，我们就需要有一种更加灵活的方式来定义bean,这种方式不能在原始代码上面书写注解，一样能定义bean,这就用到了一个全新的注解`@Bean`。

### 环境准备

学习`@Bean`注解之前，我们先来准备一个环境

- 创建一个Maven项目
- 在pom.xml中添加Spring依赖

```
XML
<dependencies>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>5.2.10.RELEASE</version>
    </dependency>
</dependencies>
```

- 添加一个配置类`SpringConfig`

```
JAVA
@Configuration
public class SpringConfig {
}
```

- 添加BookDao、BookDaoImpl类

```
JAVA
public interface BookDao {
    public void save();
}
@Repository
public class BookDaoImpl implements BookDao {
    public void save() {
        System.out.println("book dao save ..." );
    }
}
```

- 创建运行类App

```
JAVA
public class App {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext(SpringConfig.class);
    }
}
```

### 注解开发管理第三方bean

在上述环境中完成对`Druid`数据源的管理，具体的实现步骤为

- `步骤一：`导入对应的jar包

```
XML
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid</artifactId>
    <version>1.1.16</version>
</dependency>
```

- `步骤二：`在配置类中添加一个方法
  注意该方法的返回值就是要创建的Bean对象类型

```
JAVA
@Configuration
public class SpringConfig {
    public DataSource dataSource() {
        DruidDataSource dataSource = new DruidDataSource();
        dataSource.setDriverClassName("com.mysql.jdbc.Driver");
        dataSource.setUrl("jdbc:mysql://localhost:13306/spring_db");
        dataSource.setUsername("root");
        dataSource.setPassword("PASSWORD");
        return dataSource;
    }
}
```

- `步骤三：`在方法上添加`@Bean`注解
  `@Bean`注解的作用是将方法的返回值作为一个Spring管理的bean对象

```
JAVA
@Configuration
public class SpringConfig {
    @Bean
    public DataSource dataSource() {
        DruidDataSource dataSource = new DruidDataSource();
        dataSource.setDriverClassName("com.mysql.jdbc.Driver");
        dataSource.setUrl("jdbc:mysql://localhost:13306/spring_db");
        dataSource.setUsername("root");
        dataSource.setPassword("PASSWORD");
        return dataSource;
    }
}
```

- `步骤四：`从IOC容器中获取对象并打印

```
JAVA
public class App {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext(SpringConfig.class);
        DataSource dataSource = ctx.getBean(DataSource.class);
        System.out.println(dataSource);
    }
}
```

输出如下

> {
> CreateTime:“2022-09-02 10:36:33”,
> ActiveCount:0,
> PoolingCount:0,
> CreateCount:0,
> DestroyCount:0,
> CloseCount:0,
> ConnectCount:0,
> Connections:[
> ]
> }

- 至此使用`@Bean`来管理第三方bean的案例就已经完成。
- 如果有多个bean要被Spring管理，直接在配置类中多写几个方法，方法上添加@Bean注解即可。

### 引入外部配置类

如果把所有的第三方bean都配置到Spring的配置类`SpringConfig`中，虽然可以，但是不利于代码阅读和分类管理，所有我们就想能不能按照类别将这些bean配置到不同的配置类中?

那么对于数据源的bean，我们可以把它的配置单独放倒一个`JdbcConfig`类中

```
JAVA
public class JdbcConfig {
    @Bean
    public DataSource dataSource() {
        DruidDataSource dataSource = new DruidDataSource();
        dataSource.setDriverClassName("com.mysql.jdbc.Driver");
        dataSource.setUrl("jdbc:mysql://localhost:13306/spring_db");
        dataSource.setUsername("root");
        dataSource.setPassword("PASSWORD");
        return dataSource;
    }
}
```

那现在又有了一个新问题，这个配置类如何能被Spring配置类加载到，并创建DataSource对象在IOC容器中?

针对这个问题，有两个解决方案，接着往下看

#### 使用包扫描引入

- `步骤一：`在Spring的配置类上添加包扫描
  注意要将JdbcConfig类放在包扫描的地址下

```
JAVA
@Configuration
@ComponentScan("com.blog.config")
public class SpringConfig {
}
```

- `步骤二：`在JdbcConfig上添加`@Configuration`注解
  JdbcConfig类要放入到`com.blog.config`包下，需要被Spring的配置类扫描到即可

```
JAVA
@Configuration
public class JdbcConfig {
    @Bean
    public DataSource dataSource(){
        DruidDataSource ds = new DruidDataSource();
        ds.setDriverClassName("com.mysql.jdbc.Driver");
        ds.setUrl("jdbc:mysql://localhost:3306/spring_db");
        ds.setUsername("root");
        ds.setPassword("root");
        return ds;
    }
}
```

- `步骤三：`运行程序
  仍然可以获取到bean对象并输出到控制台

> {
> CreateTime:“2022-09-02 10:52:50”,
> ActiveCount:0,
> PoolingCount:0,
> CreateCount:0,
> DestroyCount:0,
> CloseCount:0,
> ConnectCount:0,
> Connections:[
> ]
> }

这种方式虽然能够扫描到，但是不能很快的知晓都引入了哪些配置类(因为把包下的所有配置类都扫描了)，所有这种方式不推荐使用。

#### 使用@Import引入

方案一实现起来有点小复杂，Spring早就想到了这一点，于是又给我们提供了第二种方案。
这种方案可以不用加`@Configuration`注解，但是必须在Spring配置类上使用`@Import`注解手动引入需要加载的配置类

- `步骤一：`去除JdbcConfig类上的注解

```
JAVA
public class JdbcConfig {
    @Bean
    public DataSource dataSource() {
        DruidDataSource dataSource = new DruidDataSource();
        dataSource.setDriverClassName("com.mysql.jdbc.Driver");
        dataSource.setUrl("jdbc:mysql://localhost:13306/spring_db");
        dataSource.setUsername("root");
        dataSource.setPassword("PASSWORD");
        return dataSource;
    }
}
```

- `步骤二：`在Spring配置类中引入

```
JAVA
@Configuration
@Import(JdbcConfig.class)
public class SpringConfig {
}
```

**注意:**

- 扫描注解可以移除
- @Import参数需要的是一个数组，可以引入多个配置类。
- @Import注解在配置类中只能写一次

- `步骤三：`运行程序
  依然能获取到bean对象并打印控制台

> {
> CreateTime:“2022-09-02 11:02:12”,
> ActiveCount:0,
> PoolingCount:0,
> CreateCount:0,
> DestroyCount:0,
> CloseCount:0,
> ConnectCount:0,
> Connections:[
> ]
> }

知识点1：`@Bean`

| 名称 |                 @Bean                  |
| :--: | :------------------------------------: |
| 类型 |                方法注解                |
| 位置 |              方法定义上方              |
| 作用 | 设置该方法的返回值作为spring管理的bean |
| 属性 |      value（默认）：定义bean的id       |

知识点2：`@Import`

| 名称 |                           @Import                            |
| :--: | :----------------------------------------------------------: |
| 类型 |                            类注解                            |
| 位置 |                          类定义上方                          |
| 作用 |                          导入配置类                          |
| 属性 | value（默认）：定义导入的配置类类名， 当配置类有多个时使用数组格式一次性导入多个配置类 |

### 注解开发实现为第三方bean注入资源

在使用@Bean创建bean对象的时候，如果方法在创建的过程中需要其他资源该怎么办?

这些资源会有两大类，分别是`简单数据类型` 和`引用数据类型`。

#### 简单数据类型

对于下面代码关于数据库的四要素不应该写死在代码中，应该是从properties配置文件中读取。如何来优化下面的代码?

```
JAVA
public class JdbcConfig {
    @Bean
    public DataSource dataSource() {
        DruidDataSource dataSource = new DruidDataSource();
        dataSource.setDriverClassName("com.mysql.jdbc.Driver");
        dataSource.setUrl("jdbc:mysql://localhost:13306/spring_db");
        dataSource.setUsername("root");
        dataSource.setPassword("PASSWORD");
        return dataSource;
    }
}
```

- `步骤一：`提供对应的四个属性

```
JAVA
public class JdbcConfig {

    private String driver;
    private String url;
    private String username;
    private String password;

    @Bean
    public DataSource dataSource() {
        DruidDataSource dataSource = new DruidDataSource();
        dataSource.setDriverClassName(driver);
        dataSource.setUrl(url);
        dataSource.setUsername(username);
        dataSource.setPassword(password);
        return dataSource;
    }
}
```

- `步骤二：`使用`@Value`注解

```
JAVA
public class JdbcConfig {
    @Value("com.mysql.jdbc.Driver")
    private String driver;
    @Value("jdbc:mysql://localhost:13306/spring_db")
    private String url;
    @Value("root")
    private String username;
    @Value("PASSWORD")
    private String password;

    @Bean
    public DataSource dataSource() {
        DruidDataSource dataSource = new DruidDataSource();
        dataSource.setDriverClassName(driver);
        dataSource.setUrl(url);
        dataSource.setUsername(username);
        dataSource.setPassword(password);
        return dataSource;
    }
}
```

- 扩展
  现在的数据库连接四要素还是写在代码中，需要做的是将这些内容提取到jdbc.properties配置文件，在上面我们已经实现过了，这里再来复习一遍

1. resources目录下添加jdbc.properties
2. 配置文件中提供四个键值对分别是数据库的四要素

```
PROPERTIES
jdbc.driver=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/spring_db
jdbc.username=root
jdbc.password=PASSWORD.
```

1. 使用@PropertySource加载jdbc.properties配置文件
2. 修改@Value注解属性的值，将其修改为`${key}`，key就是键值对中的键的值

```
JAVA
@PropertySource("jdbc.properties")
public class JdbcConfig {
    @Value("${jdbc.driver}")
    private String driver;
    @Value("${jdbc.url}")
    private String url;
    @Value("${jdbc.username}")
    private String username;
    @Value("${jdbc.password}")
    private String password;

    @Bean
    public DataSource dataSource() {
        DruidDataSource dataSource = new DruidDataSource();
        dataSource.setDriverClassName(driver);
        dataSource.setUrl(url);
        dataSource.setUsername(username);
        dataSource.setPassword(password);
        return dataSource;
    }
}
```

输出结果如下

> {
> CreateTime:“2022-09-02 11:13:45”,
> ActiveCount:0,
> PoolingCount:0,
> CreateCount:0,
> DestroyCount:0,
> CloseCount:0,
> ConnectCount:0,
> Connections:[
> ]
> }

#### 引用数据类型

假设在构建DataSource对象的时候，需要用到BookDao对象，该如何把BookDao对象注入进方法内让其使用呢?

- `步骤一：`在SpringConfig中扫描BookDao
  扫描的目的是让Spring能管理到BookDao，也就是要让IOC容器中有一个BookDao对象

```
JAVA
@Configuration
@ComponentScan("com.blog.dao")
@Import(JdbcConfig.class)
public class SpringConfig {
}
```

- `步骤二：`在JdbcConfig类的方法上添加参数
  引用类型注入只需要为bean定义方法设置形参即可，容器会`根据类型`自动装配对象。

```
JAVA
@Bean
public DataSource dataSource(BookDao bookDao) {
    bookDao.save();
    DruidDataSource dataSource = new DruidDataSource();
    dataSource.setDriverClassName(driver);
    dataSource.setUrl(url);
    dataSource.setUsername(username);
    dataSource.setPassword(password);
    return dataSource;
}
```

- `步骤三：`运行程序
  结果如下，说明bookDao已经成功注入

> book dao save …
> {
> CreateTime:“2022-09-02 11:29:54”,
> ActiveCount:0,
> PoolingCount:0,
> CreateCount:0,
> DestroyCount:0,
> CloseCount:0,
> ConnectCount:0,
> Connections:[
> ]
> }

## 注解开发总结

[![](img/6311791f16f2c2beb1cd19b1.jpg)](https://pic.imgdb.cn/item/6311791f16f2c2beb1cd19b1.jpg)

## Spring整合

### Spring整合MyBatis

#### 环境准备

在准备环境的同时，我们也来回顾一下MyBatis开发的相关内容

- `步骤一：`准备数据库表
  MyBatis是用来操作数据库表的，所以我们先来创建库和表

```
SQL
create database spring_db character set utf8;
use spring_db;
create table tbl_account(
    id int primary key auto_increment,
    name varchar(35),
    money double
);

INSERT INTO tbl_account(`name`,money) VALUES
('Tom',2800),
('Jerry',3000),
('Jhon',3100);
```

- `步骤二：`创建项目导入依赖

```
XML
<dependencies>
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>5.1.46</version>
    </dependency>
    <dependency>
        <groupId>org.mybatis</groupId>
        <artifactId>mybatis</artifactId>
        <version>3.5.6</version>
    </dependency>
    <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>druid</artifactId>
        <version>1.1.16</version>
    </dependency>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>5.2.10.RELEASE</version>
    </dependency>
</dependencies>
```

- `步骤三：`根据表创建模型类

```
JAVA
public class Account {
    private Integer id;
    private String name;
    private Double money;

    public Account() {
    }

    public Account(Integer id, String name, double money) {
        this.id = id;
        this.name = name;
        this.money = money;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getMoney() {
        return money;
    }

    public void setMoney(double money) {
        this.money = money;
    }

    @Override
    public String toString() {
        return "Account{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", money=" + money +
                '}';
    }
}
```

- `步骤四：`创建Dao接口（在之前是Mapper接口，且要配置一个对应的xml文件，不过这里没涉及到复杂的sql语句，所以没配置xml文件，采用注解开发）

```
JAVA
public interface AccountDao {

    @Insert("insert into tbl_account(name, money) VALUES (#{name}, #{money})")
    void save(Account account);

    @Delete("delete from tbl_account where id = #{id}")
    void delete(Integer id);

    @Update("update tbl_account set `name` = #{name}, money = #{money}")
    void update(Account account);

    @Select("select * from tbl_account")
    List<Account> findAll();

    @Select("select * from tbl_account where id = #{id}")
    Account findById(Integer id);
}
```

- `步骤五：`创建Service接口和实现类

- AccountService
- AccountServiceImpl

```
JAVA
public interface AccountService {
    void save(Account account);

    void delete(Integer id);

    void update(Account account);

    List<Account> findAll();

    Account findById(Integer id);
}
```



- `步骤六：`添加jdbc.properties文件

```
PROPERTIES
jdbc.driver=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/spring_db
jdbc.username=root
jdbc.password=PASSWORD.
```

- `步骤七：`添加Mybatis核心配置文件

```
XML
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <!--读取外部properties配置文件-->
    <properties resource="jdbc.properties"></properties>
    <!--别名扫描的包路径-->
    <typeAliases>
        <package name="com.blog.domain"/>
    </typeAliases>
    <!--数据源-->
    <environments default="mysql">
        <environment id="mysql">
            <transactionManager type="JDBC"></transactionManager>
            <dataSource type="POOLED">
                <property name="driver" value="${jdbc.driver}"></property>
                <property name="url" value="${jdbc.url}"></property>
                <property name="username" value="${jdbc.username}"></property>
                <property name="password" value="${jdbc.password}"></property>
            </dataSource>
        </environment>
    </environments>
    <!--映射文件扫描包路径-->
    <mappers>
        <package name="com.blog.dao"></package>
    </mappers>
</configuration>
```

- `步骤八：`编写应用程序

```
JAVA
public class App {
    public static void main(String[] args) throws IOException {
        // 1. 创建SqlSessionFactoryBuilder对象
        SqlSessionFactoryBuilder sqlSessionFactoryBuilder = new SqlSessionFactoryBuilder();
        // 2. 加载mybatis-config.xml配置文件
        InputStream inputStream = Resources.getResourceAsStream("mybatis-config.xml");
        // 3. 创建SqlSessionFactory对象
        SqlSessionFactory factory = sqlSessionFactoryBuilder.build(inputStream);
        // 4. 获取SqlSession
        SqlSession sqlSession = factory.openSession();
        // 5. 获取mapper
        AccountDao mapper = sqlSession.getMapper(AccountDao.class);
        //6. 执行方法进行查询
        Account account = mapper.findById(2);
        System.out.println(account);
        //7. 释放资源
        sqlSession.close();
    }
}
```

- `步骤九：`运行程序，结果如下

> Account{id=2, name=‘Jerry’, money=3000.0}

#### 思路分析

Mybatis的基础环境我们已经准备好了，接下来就得分析下在上述的内容中，哪些对象可以交给Spring来管理?

- Mybatis程序核心对象分析
  从图中可以获取到，真正需要交给Spring管理的是SqlSessionFactory
  [![](img/6313ff4416f2c2beb1bf13f0.jpg)](https://pic.imgdb.cn/item/6313ff4416f2c2beb1bf13f0.jpg)
- 整合Mybatis，就是将Mybatis用到的内容交给Spring管理，分析下配置文件
  [![](img/6313ff5116f2c2beb1bf1ee5.jpg)](https://pic.imgdb.cn/item/6313ff5116f2c2beb1bf1ee5.jpg)

说明:

- 第一部分读取外部properties配置文件，Spring有提供具体的解决方案`@PropertySource`,需要交给Spring
- 第二部分起别名包扫描，为SqlSessionFactory服务的，需要交给Spring
- 第三部分主要用于做连接池，Spring之前我们已经整合了Druid连接池，这块也需要交给Spring
- 前面三部分一起都是为了创建SqlSession对象用的，那么用Spring管理SqlSession对象吗?回忆下SqlSession是由SqlSessionFactory创建出来的，所以只需要将SqlSessionFactory交给Spring管理即可。
- 第四部分是Mapper接口和映射文件[如果使用注解就没有该映射文件]，这个是在获取到SqlSession以后执行具体操作的时候用，所以它和SqlSessionFactory创建的时机都不在同一个时间，可能需要单独管理。

#### 整合步骤

前面我们已经分析了Spring与Mybatis的整合，大体需要做两件事，

- 第一件事是：Spring要管理MyBatis中的SqlSessionFactory
- 第二件事是：Spring要管理Mapper接口的扫描

那我们下面就开始来整合

- `步骤一：`项目中导入整合需要的jar包

```
XML
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis-spring</artifactId>
    <version>1.3.0</version>
</dependency>
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-jdbc</artifactId>
    <version>5.2.10.RELEASE</version>
</dependency>
```

- `步骤二：`创建Spring的主配置类

```
JAVA
//配置类注解
@Configuration
//包扫描，主要扫描的是项目中的AccountServiceImpl类
@ComponentScan("com.blog")
public class SpringConfig {
}
```

- `步骤三：`创建数据源的配置类
  在配置类中完成数据源的创建

```
JAVA
public class JdbcConfig {
    @Value("${jdbc.driver}")
    private String driver;
    @Value("${jdbc.url}")
    private String url;
    @Value("${jdbc.username}")
    private String username;
    @Value("${jdbc.password}")
    private String password;

    @Bean
    public DataSource dataSource() {
        DruidDataSource dataSource = new DruidDataSource();
        dataSource.setDriverClassName(driver);
        dataSource.setUrl(url);
        dataSource.setUsername(username);
        dataSource.setPassword(password);
        return dataSource;
    }
}
```

- `步骤四：`主配置类中读properties并引入数据源配置类

```
JAVA
@Configuration
@ComponentScan("com.blog")
@PropertySource("jdbc.properties")
@Import(JdbcConfig.class)
public class SpringConfig {
}
```

- `步骤五：`创建Mybatis配置类并配置SqlSessionFactory

```
JAVA
public class MyBatisConfig {

    @Bean
    public SqlSessionFactoryBean sqlSessionFactory(DataSource dataSource) {
        //定义bean，SqlSessionFactoryBean，用于产生SqlSessionFactory对象
        SqlSessionFactoryBean sqlSessionFactory = new SqlSessionFactoryBean();
        //设置模型类的别名扫描
        sqlSessionFactory.setTypeAliasesPackage("com.blog.domain");
        //设置数据源
        sqlSessionFactory.setDataSource(dataSource);
        return sqlSessionFactory;
    }
    //定义bean，返回MapperScannerConfigurer对象
    @Bean
    public MapperScannerConfigurer mapperScannerConfigurer() {
        MapperScannerConfigurer msc = new MapperScannerConfigurer();
        msc.setBasePackage("com.blog.dao");
        return msc;
    }
}
```

说明：

- 使用SqlSessionFactoryBean封装SqlSessionFactory需要的环境信息
  [![](img/6314160016f2c2beb1d5ae4f.jpg)](https://pic.imgdb.cn/item/6314160016f2c2beb1d5ae4f.jpg)
- SqlSessionFactoryBean是前面我们讲解FactoryBean的一个子类，在该类中将SqlSessionFactory的创建进行了封装，简化对象的创建，我们只需要将其需要的内容设置即可。
- 方法中有一个参数为dataSource,当前Spring容器中已经创建了Druid数据源，类型刚好是DataSource类型，此时在初始化SqlSessionFactoryBean这个对象的时候，发现需要使用DataSource对象，而容器中刚好有这么一个对象，就自动加载了DruidDataSource对象。
- `sqlSessionFactory.setTypeAliasesPackage("com.blog.domain");`，替换掉配置文件中的

```
XML
<typeAliases>
    <package name="com.blog.domain"/>
</typeAliases>
```

- `sqlSessionFactory.setDataSource(dataSource);`，替换掉配置文件中的

```
XML
<environments default="mysql">
    <environment id="mysql">
        <transactionManager type="JDBC"></transactionManager>
        <dataSource type="POOLED">
            <property name="driver" value="${jdbc.driver}"></property>
            <property name="url" value="${jdbc.url}"></property>
            <property name="username" value="${jdbc.username}"></property>
            <property name="password" value="${jdbc.password}"></property>
        </dataSource>
    </environment>
</environments>
```

- 使用MapperScannerConfigurer加载Dao接口，创建代理对象保存到IOC容器中
  [![](img/631416a116f2c2beb1d64489.jpg)](https://pic.imgdb.cn/item/631416a116f2c2beb1d64489.jpg)
- 这个MapperScannerConfigurer对象也是MyBatis提供的专用于整合的jar包中的类，用来处理原始配置文件中的mappers相关配置，加载数据层的Mapper接口类
- MapperScannerConfigurer有一个核心属性basePackage，就是用来设置所扫描的包路径

- `步骤六：`主配置类中引入Mybatis配置类

```
JAVA
@Configuration
@ComponentScan("com.blog")
@PropertySource("jdbc.properties")
@Import({JdbcConfig.class, MyBatisConfig.class})
public class SpringConfig {
}
```

- `步骤七：`编写运行类
  在运行类中，从IOC容器中获取Service对象，调用方法获取结果

```
JAVA
public class App {
    public static void main(String[] args) throws IOException {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfig.class);
        AccountService accountService = context.getBean(AccountService.class);
        Account account = accountService.findById(1);
        System.out.println(account);
    }
}
```

- `步骤八：`运行程序

> Account{id=1, name=‘Tom’, money=2800.0}

至此，Spring与Mybatis的整合就已经完成了，其中主要用到的两个类分别是:

- SqlSessionFactoryBean
- MapperScannerConfigurer

### Spring整合JUnit

- `步骤一：`引入依赖

```
XML
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>5.2.10.RELEASE</version>
</dependency>
```

- `步骤二：`编写测试类

```
JAVA
//设置类运行器
@RunWith(SpringJUnit4ClassRunner.class)
//设置Spring环境对应的配置类
@ContextConfiguration(classes = {SpringConfig.class})//加载配置类
public class AccountServiceTest {
    //支持自动装配注入bean
    @Autowired
    private AccountService accountService;

    @Test
    public void test(){
        Account account = accountService.findById(1);
        System.out.println(account);
    }

    @Test
    public void selectAll(){
        List<Account> accounts = accountService.findAll();
        System.out.println(accounts);
    }
}
```

**注意:**

- 单元测试，如果测试的是注解配置类，则使用`@ContextConfiguration(classes = 配置类.class)`
- 单元测试，如果测试的是配置文件，则使用`@ContextConfiguration(locations={配置文件名,...})`
- Junit运行后是基于Spring环境运行的，所以Spring提供了一个专用的类运行器，这个务必要设置，这个类运行器就在Spring的测试专用包中提供的，导入的坐标就是这个东西`SpringJUnit4ClassRunner`
- 上面两个配置都是固定格式，当需要测试哪个bean时，使用自动装配加载对应的对象，下面的工作就和以前做Junit单元测试完全一样了

知识点1：`@RunWith`

| 名称 |             @RunWith              |
| :--: | :-------------------------------: |
| 类型 |            测试类注解             |
| 位置 |          测试类定义上方           |
| 作用 |          设置JUnit运行器          |
| 属性 | value（默认）：运行所使用的运行期 |

知识点2：`@ContextConfiguration`

| 名称 |                    @ContextConfiguration                     |
| :--: | :----------------------------------------------------------: |
| 类型 |                          测试类注解                          |
| 位置 |                        测试类定义上方                        |
| 作用 |                设置JUnit加载的Spring核心配置                 |
| 属性 | classes：核心配置类，可以使用数组的格式设定加载多个配置类 locations:配置文件，可以使用数组的格式设定加载多个配置文件名称 |

## AOP简介

前面我们在介绍Spring的时候说过，Spring有两个核心的概念，一个是`IOC/DI`，一个是`AOP`。

前面已经对`IOC/DI`进行了系统的学习，接下来要学习它的另一个核心内容，就是`AOP`。

`AOP是在不改原有代码的前提下对其进行增强`。

那现在我们围绕这句话，主要学习两方面内容`AOP核心概念`,`AOP作用`

### 什么是AOP?

- AOP(Aspect Oriented Programming)面向切面编程，是一种编程范式，指导开发者如何组织程序结构
  - OOP(Object Oriented Programming)面向对象编程

我们都知道OOP是一种编程思想，那么AOP也是一种编程思想，编程思想主要的内容就是指导程序员该如何编写程序，所以它们两个是不同的`编程范式`。

### AOP作用

- 作用:在不惊动原始设计的基础上为其进行功能增强

### AOP核心概念

为了能更好的理解AOP的相关概念，我们准备了一个环境，整个环境的内容我们暂时可以不用关注，最主要的类为:`BookDaoImpl`

```
JAVA
@Repository
public class BookDaoImpl implements BookDao {
    public void save() {
        //记录程序当前执行执行（开始时间）
        Long startTime = System.currentTimeMillis();
        //业务执行万次
        for (int i = 0;i<10000;i++) {
            System.out.println("book dao save ...");
        }
        //记录程序当前执行时间（结束时间）
        Long endTime = System.currentTimeMillis();
        //计算时间差
        Long totalTime = endTime-startTime;
        //输出信息
        System.out.println("执行万次消耗时间：" + totalTime + "ms");
    }
    public void update(){
        System.out.println("book dao update ...");
    }
    public void delete(){
        System.out.println("book dao delete ...");
    }
    public void select(){
        System.out.println("book dao select ...");
    }
}
```

代码的内容很简单，就是测试一下万次执行的耗时
当在App类中从容器中获取bookDao对象后，分别执行其`save`,`delete`,`update`和`select`方法后会有如下的打印结果

- save
- delete
- update
- select

book dao save …
book dao save …
book dao save …
book dao save …
book dao save …
book dao save …
执行万次消耗时间:79ms



疑问

- 对于计算万次执行消耗的时间只有save方法有，为什么delete和update方法也会有呢?
- delete和update方法有，那什么select方法为什么又没有呢?

这个案例中其实就使用了Spring的AOP，在不惊动(改动)原有设计(代码)的前提下，想给谁添加额外功能就给谁添加。这个也就是Spring的理念：

- 无入侵式/无侵入式

说了这么多，Spring到底是如何实现的呢?
[![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://pic.imgdb.cn/item/63155fb516f2c2beb109d12c.jpg)

1. 前面一直在强调，Spring的AOP是对一个类的方法在不进行任何修改的前提下实现增强。对于上面的案例中BookServiceImpl中有`save`,`update`,`delete`和`select`方法,这些方法我们给起了一个名字叫`连接点`
2. 在BookServiceImpl的四个方法中，`update`和`delete`只有打印没有计算万次执行消耗时间，但是在运行的时候已经有该功能，那也就是说`update`和`delete`方法都已经被增强，所以对于需要增强的方法我们给起了一个名字叫`切入点`
3. 执行BookServiceImpl的update和delete方法的时候都被添加了一个计算万次执行消耗时间的功能，将这个功能抽取到一个方法中，换句话说就是存放共性功能的方法，我们给起了个名字叫`通知`
4. 通知是要增强的内容，会有多个，切入点是需要被增强的方法，也会有多个，那哪个切入点需要添加哪个通知，就需要提前将它们之间的关系描述清楚，那么对于通知和切入点之间的关系描述，我们给起了个名字叫`切面`
5. 通知是一个方法，方法不能独立存在需要被写在一个类中，这个类我们也给起了个名字叫`通知类`

至此AOP中的核心概念就已经介绍完了，总结下:

- 连接点(JoinPoint)：程序执行过程中的任意位置，粒度为执行方法、抛出异常、设置变量等
  - 在SpringAOP中，理解为方法的执行
- 切入点(Pointcut):匹配连接点的式子
  - 在SpringAOP中，一个切入点可以描述一个具体方法，也可也匹配多个方法
    - 一个具体的方法:如com.blog.dao包下的BookDao接口中的无形参无返回值的save方法
    - 匹配多个方法:所有的save方法/所有的get开头的方法/所有以Dao结尾的接口中的任意方法/所有带有一个参数的方法
  - 连接点范围要比切入点范围大，是切入点的方法也一定是连接点，但是是连接点的方法就不一定要被增强，所以可能不是切入点。
- 通知(Advice):在切入点处执行的操作，也就是共性功能
  - 在SpringAOP中，功能最终以方法的形式呈现
- 通知类：定义通知的类
- 切面(Aspect):描述通知与切入点的对应关系。

### 小结

这部分需要掌握的内容是

- 什么是AOP?
- AOP的作用是什么?
- AOP中核心概念分别指的是什么?
  - 连接点
  - 切入点
  - 通知
  - 通知类
  - 切面

## AOP入门案例

### 需求分析

案例设定：测算接口执行效率，但是这个案例稍微复杂了点，我们对其进行简化。
简化设定：在方法执行前输出当前系统时间。
那现在我们使用SpringAOP的注解方式完成在方法执行的前打印出当前系统时间。

### 思路分析

1. 导入坐标
2. 制作连接点（原始操作，Dao接口及实现类）
3. 制作共性功能（通知类和通知）
4. 定义切入点
5. 绑定切入点和通知的关系（切面）

### 环境准备

- 创建一个Maven项目
- pom.xml添加Spring依赖

```
XML
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>5.2.10.RELEASE</version>
</dependency>
```

- 添加BookDao和BookDaoImpl类

- BookDao
- BookDaoImpl

```
JAVA
public interface BookDao {
    public void save();
    public void update();
}
```



- 创建Spring的配置类

```
JAVA
@Configuration
@ComponentScan("com.blog")
public class SpringConfig {
}
```

- 编写App运行类

```
JAVA
public class App {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfig.class);
        BookDao bookDao = context.getBean(BookDao.class);
        bookDao.update();
    }
}
```

**说明:**

- 目前打印save方法的时候，因为方法中有打印系统时间，所以运行的时候是可以看到系统时间
- 对于update方法来说，就没有该功能
- 我们要使用SpringAOP的方式在不改变update方法的前提下让其具有打印系统时间的功能。

### AOP实现步骤

- `步骤一：`添加依赖

```
XML
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.4</version>
</dependency>
```

因为`spring-context`中已经导入了`spring-aop`,所以不需要再单独导入`spring-aop`
导入AspectJ的jar包,AspectJ是AOP思想的一个具体实现，Spring有自己的AOP实现，但是相比于AspectJ来说比较麻烦，所以我们直接采用Spring整合ApsectJ的方式进行AOP开发。

- `步骤二：`定义接口和实现类
  准备环境的时候我们已经完成了
- `步骤三：`定义通知类和通知
  通知就是将共性功能抽取出来后形成的方法，共性功能指的就是当前系统时间的打印。
  类名和方法名没有要求，可以任意。

```
JAVA
public class MyAdvice {
    public void method(){
        System.out.println(System.currentTimeMillis());
    }
}
```

- `步骤四：`定义切入点
  BookDaoImpl中有两个方法，分别是update()和save()，我们要增强的是update方法，那么该如何定义呢？

```
JAVA
public class MyAdvice {
    @Pointcut("execution(void com.blog.dao.impl.BookDaoImpl.update())")
    private void pt() {
    }

    public void method() {
        System.out.println(System.currentTimeMillis());
    }
}
```

**说明:**

- 切入点定义依托一个不具有实际意义的方法进行，即无参数、无返回值、方法体无实际逻辑。
- execution及后面编写的内容，之后我们会专门去学习。

- `步骤五：`制作切面
  切面是用来描述通知和切入点之间的关系，如何进行关系的绑定?

```
JAVA
public class MyAdvice {

    @Pointcut("execution(void com.blog.dao.BookDao.update())")
    private void pt(){}
    
    @Before("pt()")
    public void method(){
        System.out.println(System.currentTimeMillis());
    }
}
```

绑定切入点与通知关系，并指定通知添加到原始连接点的具体执行`位置`

**说明:**`@Before`翻译过来是之前，也就是说通知会在切入点方法执行之前执行，除此之前还有其他四种类型，后面会讲。
那这里就会在执行update()之前，来执行我们的method()，输出当前毫秒值

- `步骤六：`将通知类配给容器并标识其为切面类

```
JAVA
@Component
@Aspect
public class MyAdvice {

    @Pointcut("execution(void com.blog.dao.impl.BookDaoImpl.update())")
    private void pt() {
    }

    @Before("pt()")
    public void method() {
        System.out.println(System.currentTimeMillis());
    }
}
```

- `步骤七：`开启注解格式AOP功能
  使用`@EnableAspectJAutoProxy`注解

```
JAVA
@Configuration
@ComponentScan("com.blog")
@EnableAspectJAutoProxy
public class SpringConfig {
}
```

- `步骤八：`运行程序
  这次我们再来调用update()

```
JAVA
public class App {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfig.class);
        BookDao bookDao = context.getBean(BookDao.class);
        bookDao.update();
    }
}
```

控制台成功输出了当前毫秒值

> 1662367945787
> book dao update …

知识点1：`@EnableAspectJAutoProxy`

| 名称 | @EnableAspectJAutoProxy |
| :--: | :---------------------: |
| 类型 |       配置类注解        |
| 位置 |     配置类定义上方      |
| 作用 |   开启注解格式AOP功能   |

知识点2：`@Aspect`

| 名称 |        @Aspect        |
| :--: | :-------------------: |
| 类型 |        类注解         |
| 位置 |    切面类定义上方     |
| 作用 | 设置当前类为AOP切面类 |

知识点3：`@Pointcut`

| 名称 |          @Pointcut          |
| :--: | :-------------------------: |
| 类型 |          方法注解           |
| 位置 |     切入点方法定义上方      |
| 作用 |       设置切入点方法        |
| 属性 | value（默认）：切入点表达式 |

知识点4：`@Before`

| 名称 |                           @Before                            |
| :--: | :----------------------------------------------------------: |
| 类型 |                           方法注解                           |
| 位置 |                       通知方法定义上方                       |
| 作用 | 设置当前通知方法与切入点之间的绑定关系，当前通知方法在原始切入点方法前运行 |

## AOP工作流程

AOP的入门案例已经完成，对于刚才案例的执行过程，我们就得来分析分析，这一节我们主要讲解两个知识点:`AOP工作流程`和`AOP核心概念`。其中核心概念是对前面核心概念的补充。

### AOP工作流程

由于AOP是基于Spring容器管理的bean做的增强，所以整个工作过程需要从Spring加载bean说起

- 流程一：

  Spring容器启动

  - 容器启动就需要去加载bean,哪些类需要被加载呢?
  - 需要被增强的类，如:BookServiceImpl
  - 通知类，如:MyAdvice
  - 注意此时bean对象还没有创建成功

- 流程二：读取所有切面配置中的切入点

```
JAVA
@Component
@Aspect
public class MyAdvice {
    @Pointcut("execution(void com.blog.dao.impl.BookDaoImpl.update())")
    private void ptx() {
    }

    @Pointcut("execution(void com.blog.dao.impl.BookDaoImpl.update())")
    private void pt() {
    }


    @Before("pt()")
    public void method() {
        System.out.println(System.currentTimeMillis());
    }
}
```

上面这个例子中有两个切入点的配置，但是第一个`ptx()`并没有被使用，所以不会被读取。

- 流程三：

  初始化bean，判定bean对应的类中的方法是否匹配到任意切入点

  - 注意第一步在容器启动的时候，bean对象还没有被创建成功。
  - 要被实例化bean对象的类中的方法和切入点进行匹配

[![](img/6315bf8416f2c2beb16ede79.jpg)](https://pic.imgdb.cn/item/6315bf8416f2c2beb16ede79.jpg)

- 匹配失败，创建原始对象，如`UserDao`

  - 匹配失败说明不需要增强，直接调用原始对象的方法即可。

- 匹配成功，创建原始对象（`目标对象`）的`代理`对象，如:`BookDao`

  - 匹配成功说明需要对其进行增强
  - 对哪个类做增强，这个类对应的对象就叫做目标对象
  - 因为要对目标对象进行功能增强，而采用的技术是动态代理，所以会为其创建一个代理对象
  - 最终运行的是代理对象的方法，在该方法中会对原始方法进行功能增强

- 流程四：

  获取bean执行方法

  - 获取的bean是原始对象时，调用方法并执行，完成操作
  - 获取的bean是代理对象时，根据代理对象的运行模式运行原始方法与增强的内容，完成操作

- 下面我们来验证一下容器中是否为代理对象

  - 如果目标对象中的方法`会被增强`，那么容器中将存入的是目标对象的`代理对象`
  - 如果目标对象中的方法`不被增强`，那么容器中将存入的是目标`对象本身`

- `步骤一：`修改App运行类，获取类的类型并输出

```
JAVA
public class App {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfig.class);
        BookDao bookDao = context.getBean(BookDao.class);
        System.out.println(bookDao);
        System.out.println(bookDao.getClass());
    }
}
```

- `步骤二：`修改MyAdvice类，改为不增强
  将定义的切入点改为`updatexxx`，而BookDaoImpl类中不存在该方法，所以BookDao中的update方法在执行的时候，就不会被增强
  所以此时容器中的对象应该是目标对象本身。

```
JAVA
@Component
@Aspect
public class MyAdvice {
    @Pointcut("execution(void com.blog.dao.impl.BookDaoImpl.updatexxx())")
    private void pt() {
    }

    @Before("pt()")
    public void method() {
        System.out.println(System.currentTimeMillis());
    }
}
```

- `步骤三：`运行程序
  输出结果如下，确实是目标对象本身，符合我们的预期

> com.blog.dao.impl.BookDaoImpl@bcec361
> class com.blog.dao.impl.BookDaoImpl

- `步骤四：`修改MyAdvice类，改为增强
  将定义的切入点改为`update`，那么BookDao中的update方法在执行的时候，就会被增强
  所以容器中的对象应该是目标对象的代理对象

```
JAVA
@Component
@Aspect
public class MyAdvice {
    @Pointcut("execution(void com.blog.dao.impl.BookDaoImpl.update())")
    private void pt() {
    }

    @Before("pt()")
    public void method() {
        System.out.println(System.currentTimeMillis());
    }
}
```

- `步骤五：`运行程序
  结果如下

> com.blog.dao.impl.BookDaoImpl@3d34d211
> class com.sun.proxy.$Proxy19

至此对于刚才的结论，我们就得到了验证，这块我们需要注意的是:
不能直接打印对象，从上面两次结果中可以看出，直接打印对象走的是对象的toString方法，不管是不是代理对象，打印的结果都是一样的，原因是内部对toString方法进行了重写。

### AOP核心概念

在上面介绍AOP的工作流程中，我们提到了两个核心概念，分别是:

- 目标对象(Target)：原始功能去掉共性功能对应的类产生的对象，这种对象是无法直接完成最终工作的
- 代理(Proxy)：目标对象无法直接完成工作，需要对其进行功能回填，通过原始对象的代理对象实现

上面这两个概念比较抽象，简单来说

目标对象就是要增强的类`如:BookServiceImpl类`对应的对象，也叫原始对象，不能说它不能运行，只能说它在运行的过程中对于要增强的内容是缺失的。

SpringAOP是在不改变原有设计(代码)的前提下对其进行增强的，它的底层采用的是代理模式实现的，所以要对原始对象进行增强，就需要对原始对象创建代理对象，在代理对象中的方法把通知`如:MyAdvice中的method方法`内容加进去，就实现了增强，这就是我们所说的代理(Proxy)。

### 小结

这部分我们需要掌握的内容有：

- 能说出AOP的工作流程
- AOP的核心概念
  - 目标对象、连接点、切入点
  - 通知类、通知
  - 切面
  - 代理
- SpringAOP的本质或者可以说底层实现是通过`代理模式`。

## AOP配置管理

### AOP切入点表达式

前面我们已经接触过了切入点表达式，下面我们来具体学习一下

```
JAVA
@Pointcut("execution(void com.blog.dao.impl.BookDaoImpl.update())")
```

对于AOP中切入点表达式，我们总共会学习三个内容，分别是`语法格式`、`通配符`和`书写技巧`。

#### 语法格式

首先我们先要明确两个概念:

- 切入点:要进行增强的方法
- 切入点表达式:要进行增强的方法的描述方式

对于切入点的描述，我们其实是有两中方式的，先来看下前面的例子
由于BookDaoImpl类实现了BookDao接口，那么有如下两种方式来描述

- 描述方式一：执行com.blog.dao包下的BookDao接口中的无参数update方法

```
JAVA
execution(void com.blog.dao.BookDao.update())
```

- 描述方式二：执行com.blog.dao.impl包下的BookDaoImpl类中的无参数update方法

```
JAVA
execution(void com.blog.dao.impl.BookDaoImpl.update())
```

因为调用接口方法的时候最终运行的还是其实现类的方法，所以上面两种描述方式都是可以的。

对于切入点表达式的语法为:

- 切入点表达式标准格式：动作关键字(访问修饰符 返回值 包名.类/接口名.方法名(参数) 异常名）
  对于这个格式，我们不需要硬记，通过一个例子，理解它:

```
JAVA
execution(public User com.blog.service.UserService.findById(int))
```

- execution：动作关键字，描述切入点的行为动作，例如execution表示执行到指定切入点
- public:访问修饰符,还可以是public，private等，可以省略
- User：返回值，写返回值类型
- com.blog.service：包名，多级包使用点连接
- UserService:类/接口名称
- findById：方法名
- int:参数，直接写参数的类型，多个类型用逗号隔开
- 异常名：方法定义中抛出指定异常，可以省略

切入点表达式就是要找到需要增强的方法，所以它就是对一个具体方法的描述，但是方法的定义会有很多，所以如果每一个方法对应一个切入点表达式，想想这块就会觉得将来编写起来会比较麻烦，有没有更简单的方式呢?

- 使用通配符

#### 通配符

我们使用通配符描述切入点，主要的目的就是简化之前的配置，具体都有哪些通配符可以使用?

- `*`:单个独立的任意符号，可以独立出现，也可以作为前缀或者后缀的匹配符出现
  匹配com.blog包下的任意包中的UserService类或接口中所有find开头的带有一个参数的方法

```
JAVA
execution（public * com.blog.*.UserService.find*(*))
```

- `..`：多个连续的任意符号，可以独立出现，常用于简化包名与参数的书写
  匹配com包下的任意包中的UserService类或接口中所有名称为findById的方法

```
JAVA
execution（public User com..UserService.findById(..))
```

- `+`：专用于匹配子类类型
  这个使用率较低，描述子类的，`*Service+`，表示所有以Service结尾的接口的子类

```
JAVA
execution(* *..*Service+.*(..))
```

下面我们来具体分析一下各种用法

- 匹配接口，能匹配到

```
JAVA
execution(void com.blog.dao.BookDao.update())
```

- 匹配实现类，能匹配到

```
JAVA
execution(void com.blog.dao.impl.BookDaoImpl.update())
```

- 返回值任意，能匹配到

```
JAVA
execution(* com.blog.dao.impl.BookDaoImpl.update())
```

- 返回值任意，但是update方法必须要有一个参数，无法匹配，要想匹配需要在update接口和实现类添加参数

```
JAVA
execution(* com.blog.dao.impl.BookDaoImpl.update(*))
```

- 返回值为void,com包下的任意包三层包下的任意类的update方法，匹配到的是实现类，能匹配

```
JAVA
execution(void com.*.*.*.*.update())
```

- 返回值为void,com包下的任意两层包下的任意类的update方法，匹配到的是接口，能匹配

```
JAVA
execution(void com.*.*.*.update())
```

- 返回值为void，方法名是update的任意包下的任意类，能匹配

```
JAVA
execution(void *..update())
```

- 匹配项目中任意类的任意方法，能匹配，但是不建议使用这种方式，影响范围广

```
JAVA
execution(* *..*(..))
```

- 匹配项目中任意包任意类下只要以u开头的方法，update方法能满足，能匹配

```
JAVA
execution(* *..u*(..))
```

- 匹配项目中任意包任意类下只要以e结尾的方法，update和save方法能满足，能匹配

```
JAVA
execution(* *..*e(..))
```

- 返回值为void，com包下的任意包任意类任意方法，能匹配，*代表的是方法

```
JAVA
execution(void com..*())
```

- 将项目中所有业务层方法的以find开头的方法匹配

```
JAVA
execution(* com.blog.*.*Service.find*(..))
```

- 将项目中所有业务层方法的以save开头的方法匹配

```
JAVA
execution(* com.blog.*.*Service.save*(..))
```

#### 书写技巧

对于切入点表达式的编写其实是很灵活的，那么在编写的时候，有没有什么好的技巧让我们用用:

- 所有代码按照标准规范开发，否则以下技巧全部失效
- 描述切入点通常`描述接口`，而不描述实现类,如果描述到实现类，就出现紧耦合了
- 访问控制修饰符针对接口开发均采用public描述（`可省略访问控制修饰符描述`）
- 返回值类型对于增删改类使用精准类型加速匹配，对于查询类使用`*`通配快速描述
- `包名`书写尽量不使用`..`匹配，效率过低，常用`*`做单个包描述匹配，或精准匹配
- `接口名/类名`书写名称与模块相关的采用`*`匹配，例如UserService书写成`*Service`，绑定业务层接口名
- 方法名书写以`动词`进行`精准匹配`，名词采用`*`匹配，例如`getById`书写成`getBy*`，`selectAll`书写成`selectAll`
- 参数规则较为复杂，根据业务方法灵活调整
- 通常`不使用异常`作为`匹配`规则

### AOP通知类型

前面的案例中，有涉及到如下内容

```
JAVA
@Before("pt()")
```

它所代表的含义是将`通知`添加到`切入点`方法执行的`前面`。
除了这个注解外，还有没有其他的注解，换个问题就是除了可以在前面加，能不能在其他的地方加?

#### 类型介绍

我们先来回顾下AOP通知:

- AOP通知描述了抽取的共性功能，根据共性功能抽取的位置不同，最终运行代码时要将其加入到合理的位置

那么具体可以将通知添加到哪里呢？一共提供了5种通知类型

- 前置通知
- 后置通知
- `环绕通知(重点)`
- 返回后通知(了解)
- 抛出异常后通知(了解)

为了更好的理解这几种通知类型，我们来看一张图

[![](img/6315d94816f2c2beb18bafb7.jpg)](https://pic.imgdb.cn/item/6315d94816f2c2beb18bafb7.jpg)

1. 前置通知，追加功能到方法执行前,类似于在代码1或者代码2添加内容
2. 后置通知,追加功能到方法执行后,不管方法执行的过程中有没有抛出异常都会执行，类似于在代码5添加内容
3. 返回后通知,追加功能到方法执行后，只有方法正常执行结束后才进行,类似于在代码3添加内容，如果方法执行抛出异常，返回后通知将不会被添加
4. 抛出异常后通知,追加功能到方法抛出异常后，只有方法执行出异常才进行,类似于在代码4添加内容，只有方法抛出异常后才会被添加
5. 环绕通知,环绕通知功能比较强大，它可以追加功能到方法执行的前后，这也是比较常用的方式，它可以实现其他四种通知类型的功能，具体是如何实现的，需要我们往下学习。

#### 环境准备

- 创建一个Maven项目
- pom.xml添加Spring依赖

```
XML
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>5.2.10.RELEASE</version>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.4</version>
</dependency>
```

- 添加BookDao和BookDaoImpl类

- BookDao
- BookDaoImpl

```
JAVA
public interface BookDao {
    public void update();

    public int select();
}
```



- 创建Spring的配置类

```
JAVA
@Configuration
@ComponentScan("com.blog")
@EnableAspectJAutoProxy
public class SpringConfig {
}
```

- 创建通知类

```
JAVA
@Component
@Aspect
public class MyAdvice {
    @Pointcut("execution(void com.blog.dao.BookDao.update())")
    private void pt() {
    }

    public void before() {
        System.out.println("before advice ...");
    }

    public void after(){
        System.out.println("after advice ...");
    }

    public void around(){
        System.out.println("around before advice ...");
        System.out.println("around after advice ...");
    }

    public void afterReturning(){
        System.out.println("afterReturning advice ...");
    }

    public void afterThrowing(){
        System.out.println("afterThrowing advice ...");
    }
}
```

- 编写App运行类

```
JAVA
public class App {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfig.class);
        BookDao bookDao = context.getBean(BookDao.class);
        bookDao.update();
    }
}
```

#### 通知类型的使用

- 前置通知

修改MyAdvice，在before方法上添加`@Before`注解

```
JAVA
@Component
@Aspect
public class MyAdvice {
    @Pointcut("execution(void com.blog.dao.BookDao.update())")
    private void pt() {
    }

    @Before("pt()")
    public void before() {
        System.out.println("before advice ...");
    }
}
```

运行程序，输出如下

> before advice …
> book dao update …

- 后置通知

```
JAVA
@Component
@Aspect
public class MyAdvice {
    @Pointcut("execution(void com.blog.dao.BookDao.update())")
    private void pt() {
    }

    @Before("pt()")
    public void before() {
        System.out.println("before advice ...");
    }

    @After("pt()")
    public void after(){
        System.out.println("after advice ...");
    }
}
```

运行程序，输出如下

> before advice …
> book dao update …
> after advice …

- 环绕通知
  - 基本使用

```
JAVA
@Component
@Aspect
public class MyAdvice {
    @Pointcut("execution(void com.blog.dao.BookDao.update())")
    private void pt() {
    }

    @Around("pt()")
    public void around(){
        System.out.println("around before advice ...");
        System.out.println("around after advice ...");
    }
}
```

运行程序，输出如下

> around before advice …
> around after advice …

运行结果中，通知的内容打印出来，但是原始方法的内容却没有被执行。

因为环绕通知需要在原始方法的前后进行增强，所以环绕通知就必须要能对原始操作进行调用，具体如何实现?

- 在方法参数中添加`ProceedingJoinPoint`，同时在需要的位置使用`proceed()`调用原始操作

```
JAVA
@Component
@Aspect
public class MyAdvice {
    @Pointcut("execution(void com.blog.dao.BookDao.update())")
    private void pt() {
    }

    @Around("pt()")
    public void around(ProceedingJoinPoint pjp) throws Throwable {
        System.out.println("around before advice ...");
        //表示对原始操作的调用
        pjp.proceed();
        System.out.println("around after advice ...");
    }
}
```

运行程序，输出如下

> around before advice …
> book dao update …
> around after advice …

- 注意事项

  - 当原始方法中有返回值时

    - 修改MyAdvice,对BookDao中的select方法添加环绕通知

    ```
    JAVA
    @Component
    @Aspect
    public class MyAdvice {
        @Pointcut("execution(int com.blog.dao.BookDao.select())")
        private void pt() {
        }
    
        @Around("pt()")
        public void around(ProceedingJoinPoint pjp) throws Throwable {
            System.out.println("around before advice ...");
            pjp.proceed();
            System.out.println("around after advice ...");
        }
    }
    ```

    - 修改App类，调用select方法

    ```
    JAVA
    public class App {
        public static void main(String[] args) {
            AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfig.class);
            BookDao bookDao = context.getBean(BookDao.class);
            int select = bookDao.select();
            System.out.println(select);
        }
    }
    ```

    - 运行程序，报错

    > org.springframework.aop.AopInvocationException: Null return value from advice does not match primitive return type for: …
    > 错误大概的意思是:`空的返回不匹配原始方法的int返回`

    - void就是返回Null
    - 原始方法的返回值是BookDao下的select方法

- 所以如果我们使用环绕通知的话，要根据原始方法的返回值来设置环绕通知的返回值，具体解决方案为:

```
JAVA
@Component
@Aspect
public class MyAdvice {
    @Pointcut("execution(int com.blog.dao.BookDao.select())")
    private void pt() {
    }

    @Around("pt()")
    public Object around(ProceedingJoinPoint pjp) throws Throwable {
        System.out.println("around before advice ...");
        Object res = pjp.proceed();
        System.out.println("around after advice ...");
        return res;
    }
}
```

- 运行程序，结果如下

> around before advice …
> book dao select …
> around after advice …
> 100

说明:

- 为什么返回的是Object而不是int的主要原因是Object类型更通用。
- 在环绕通知中是可以对原始方法返回值就行修改的。例如上面的例子，可以改为`return res+666;`，最终的输出结果也会变为766

- 返回后通知

```
JAVA
@Component
@Aspect
public class MyAdvice {
    @Pointcut("execution(int com.blog.dao.BookDao.select())")
    private void pt() {
    }

    @AfterReturning("pt()")
    public void afterReturning() {
        System.out.println("afterReturning advice ...");
    }
}
```

运行程序，结果如下

> book dao select …
> afterReturning advice …
> 100

注意：
返回后通知是需要在原始方法`select`正常执行后才会被执行，如果`select()`方法执行的过程中出现了异常，那么返回后通知是不会被执行。后置通知是不管原始方法有没有抛出异常都会被执行。
现在我们在select()方法中加一个异常

```
JAVA
public int select() {
    System.out.println("book dao select ...");
    int a = 1 / 0;
    return 100;
}
```

运行程序，输出如下，没有输出`afterReturning advice ...`

> book dao select …
> Exception in thread “main” java.lang.ArithmeticException: / by zero
> …

我们再换成后置输出，运行程序，结果如下，输出了`after advice ...`
输出如下

> book dao select …
> after advice …
> Exception in thread “main” java.lang.ArithmeticException: / by zero
> …

- 异常后通知

```
JAVA
@Component
@Aspect
public class MyAdvice {
    @Pointcut("execution(int com.blog.dao.BookDao.select())")
    private void pt() {
    }

    @AfterThrowing("pt()")
    public void afterThrowing() {
        System.out.println("afterThrowing advice ...");
    }
}
```

运行程序，输出如下

> book dao select …
> afterThrowing advice …
> Exception in thread “main” java.lang.ArithmeticException: / by zero
> …

学习完这5种通知类型，我们来思考下环绕通知是如何实现其他通知类型的功能的?

因为环绕通知是可以控制原始方法执行的，所以我们把增强的代码写在调用原始方法的不同位置就可以实现不同的通知类型的功能，如

[![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://pic.imgdb.cn/item/6316050116f2c2beb1be2656.jpg)

#### 通知类型总结

知识点1：`@After`

| 名称 |                            @After                            |
| :--: | :----------------------------------------------------------: |
| 类型 |                           方法注解                           |
| 位置 |                       通知方法定义上方                       |
| 作用 | 设置当前通知方法与切入点之间的绑定关系，当前通知方法在原始切入点方法后运行 |

知识点2：`@AfterReturning`

| 名称 |                       @AfterReturning                        |
| :--: | :----------------------------------------------------------: |
| 类型 |                           方法注解                           |
| 位置 |                       通知方法定义上方                       |
| 作用 | 设置当前通知方法与切入点之间绑定关系，当前通知方法在原始切入点方法正常执行完毕后执行 |

知识点3：`@AfterThrowing`

| 名称 |                        @AfterThrowing                        |
| :--: | :----------------------------------------------------------: |
| 类型 |                           方法注解                           |
| 位置 |                       通知方法定义上方                       |
| 作用 | 设置当前通知方法与切入点之间绑定关系，当前通知方法在原始切入点方法运行抛出异常后执行 |

知识点4：`@Around`

| 名称 |                           @Around                            |
| :--: | :----------------------------------------------------------: |
| 类型 |                           方法注解                           |
| 位置 |                       通知方法定义上方                       |
| 作用 | 设置当前通知方法与切入点之间的绑定关系，当前通知方法在原始切入点方法前后运行 |

知识点5：`@Before`

| 名称 |                           @Before                            |
| :--: | :----------------------------------------------------------: |
| 类型 |                           方法注解                           |
| 位置 |                       通知方法定义上方                       |
| 作用 | 设置当前通知方法与切入点之间的绑定关系，当前通知方法在原始切入点方法前运行 |

环绕通知注意事项

1. 环绕通知必须依赖形参ProceedingJoinPoint才能实现对原始方法的调用，进而实现原始方法调用前后同时添加通知
2. 通知中如果未使用ProceedingJoinPoint对原始方法进行调用将跳过原始方法的执行
3. 对原始方法的调用可以不接收返回值，通知方法设置成void即可，如果接收返回值，最好设定为Object类型
4. 原始方法的返回值如果是void类型，通知方法的返回值类型可以设置成void,也可以设置成Object
5. 由于无法预知原始方法运行后是否会抛出异常，因此环绕通知方法必须要处理Throwable异常

介绍完这么多种通知类型，具体该选哪一种呢?

我们可以通过一些案例加深下对通知类型的学习。

### 业务层接口执行效率

#### 需求分析

这个需求也比较简单，前面我们在介绍AOP的时候已经演示过:

- 需求:任意业务层接口执行均可显示其执行效率（执行时长）
  这个案例的目的是查看每个业务层执行的时间，这样就可以监控出哪个业务比较耗时，将其查找出来方便优化。

具体实现的思路:

1. 开始执行方法之前记录一个时间
2. 执行方法
3. 执行完方法之后记录一个时间
4. 用后一个时间减去前一个时间的差值，就是我们需要的结果。

所以要在方法执行的前后添加业务，经过分析我们将采用`环绕通知`。
**说明:**原始方法如果只执行一次，时间太快，两个时间差可能为0，所以我们要执行万次来计算时间差。

#### 环境准备

- 创建一个Maven项目
- pom.xml添加Spring依赖

```
XML
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>5.2.10.RELEASE</version>
</dependency>
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-jdbc</artifactId>
    <version>5.2.10.RELEASE</version>
</dependency>
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>5.2.10.RELEASE</version>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.4</version>
</dependency>
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.46</version>
</dependency>
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid</artifactId>
    <version>1.1.16</version>
</dependency>
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.5.6</version>
</dependency>
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis-spring</artifactId>
    <version>1.3.0</version>
</dependency>
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
    <scope>test</scope>
</dependency>
```

- 创建数据库与表

```
SQL
create database spring_db character set utf8;
use spring_db;
create table tbl_account(
    id int primary key auto_increment,
    name varchar(35),
    money double
);

INSERT INTO tbl_account(`name`,money) VALUES
('Tom',2800),
('Jerry',3000),
('Jhon',3100);
```

- 添加AccountService、AccountServiceImpl、AccountDao与Account类

- Account
- AccountDao
- AccountService
- AccountServiceImpl

```
JAVA
public class Account {
    private Integer id;
    private String name;
    private Double money;

    public Account() {
    }

    public Account(Integer id, String name, double money) {
        this.id = id;
        this.name = name;
        this.money = money;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getMoney() {
        return money;
    }

    public void setMoney(double money) {
        this.money = money;
    }

    @Override
    public String toString() {
        return "Account{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", money=" + money +
                '}';
    }
}
```

- resources下提供一个jdbc.properties

```
PROPERTIES
jdbc.driver=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/spring_db?useSSL=false
jdbc.username=root
jdbc.password=poassword.
```

- 创建相关配置类

- SpringConfig
- JdbcConfig
- MyBatisConfig
- AccountServiceImpl

```
JAVA
@Configuration
@ComponentScan("com.blog")
@PropertySource("jdbc.properties")
@Import({JdbcConfig.class, MyBatisConfig.class})
public class SpringConfig {
}
```



- 编写Spring整合Junit的测试类

```
JAVA
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = SpringConfig.class)
public class AccountServiceTestCase {
    @Autowired
    private AccountService accountService;

    @Test
    public void testFindById(){
        Account account = accountService.findById(2);
    }

    @Test
    public void testFindAll(){
        List<Account> accountList = accountService.findAll();
    }
}
```

#### 功能开发

- `步骤一：`开启SpringAOP的注解功能
  在Spring的主配置文件SpringConfig类中添加注解

```
JAVA
@EnableAspectJAutoProxy
```

- `步骤二：`创建AOP的通知类

- 该类要被Spring管理，需要添加`@Component`
- 要标识该类是一个AOP的切面类，需要添加`@Aspect`
- 配置切入点表达式，需要添加一个方法，并添加`@Pointcut`

```
JAVA
@Component
@Aspect
public class ProjectAdvice {
    @Pointcut("execution(* com.blog.service.*Service.*(..))")
    public void servicePt() {
    }

    public void runSpeed() {

    }
}
```

- `步骤三：`添加环绕通知
  在runSpeed()方法上添加@Around

```
JAVA
@Component
@Aspect
public class ProjectAdvice {
    @Pointcut("execution(* com.blog.service.*Service.*(..))")
    public void servicePt() {
    }

    @Around("servicePt()")
    public Object runSpeed(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {

        Object res = proceedingJoinPoint.proceed();
        return res;
    }
}
```

- `步骤四：`完成核心业务，记录万次执行的时间

```
JAVA
@Component
@Aspect
public class ProjectAdvice {
    @Pointcut("execution(* com.blog.service.*Service.*(..))")
    public void servicePt() {
    }

    @Around("servicePt()")
    public void runSpeed(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        for (int i = 0; i < 10000; i++) {
            proceedingJoinPoint.proceed();
        }
        long end = System.currentTimeMillis();
        System.out.println("业务层接口万次执行时间: " + (end - start) + "ms");
    }
}
```

- `步骤五：`运行单元测试类
  运行结果如下

> 业务层接口万次执行时间: 2312ms
> 业务层接口万次执行时间: 1578ms

- `步骤六：` 程序优化
  目前还存在一个问题，当我们一次执行多个方法时，控制台输出的都是`业务层接口万次执行时间: XXXms`
  我们无法得知具体哪个方法的耗时，那么该如何优化呢？
  ProceedingJoinPoint中有一个getSignature()方法来获取签名，然后调用`getDeclaringTypeName`可以获取类名，`getName()`可以获取方法名

```
JAVA
@Around("servicePt()")
public void runSpeed(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
    Signature signature = proceedingJoinPoint.getSignature();
    String typeName = signature.getDeclaringTypeName();
    String methodName = signature.getName();
    long start = System.currentTimeMillis();
    for (int i = 0; i < 10000; i++) {
        proceedingJoinPoint.proceed();
    }
    long end = System.currentTimeMillis();
    System.out.println("万次执行 " + typeName + "." + methodName + " 耗时" + (end - start) + "ms");
}
```

再次运行程序，结果如下

> 万次执行 com.blog.service.AccountService.findAll 耗时2086ms
> 万次执行 com.blog.service.AccountService.findById 耗时1365ms

说明
当前测试的接口执行效率仅仅是一个理论值，并不是一次完整的执行过程。
这块只是通过该案例把AOP的使用进行了学习，具体的实际值是有很多因素共同决定的。

### AOP通知获取数据

目前我们写AOP仅仅是在原始方法前后追加一些操作，接下来我们要说说AOP中数据相关的内容，我们将从`获取参数`、`获取返回值`和`获取异常`三个方面来研究切入点的相关信息。
前面我们介绍通知类型的时候总共讲了五种，那么对于这五种类型都会有参数，返回值和异常吗?
我们先来逐一分析下:

- 获取切入点方法的参数，所有的通知类型都可以获取参数
  - JoinPoint：适用于前置、后置、返回后、抛出异常后通知
  - ProceedingJoinPoint：适用于环绕通知
- 获取切入点方法返回值，前置和抛出异常后通知是没有返回值，后置通知可有可无，所以不做研究
  - 返回后通知
  - 环绕通知
- 获取切入点方法运行异常信息，前置和返回后通知是不会有，后置通知可有可无，所以不做研究
  - 抛出异常后通知
  - 环绕通知

#### 环境准备

- 创建一个maven项目
- 添加Spring依赖

```
XML
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>5.2.10.RELEASE</version>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.4</version>
</dependency>
```

- 添加BookDao和BookDaoImpl类

- BookDao
- BookDaoImpl

```
JAVA
public interface BookDao {
    String findName(int id);
}
```



- 创建Spring配置类

```
JAVA
@Configuration
@ComponentScan("com.blog")
@EnableAspectJAutoProxy
public class SpringConfig {
}
```

- 编写通知类

```
JAVA
@Component
@Aspect
public class MyAdvice {

    @Pointcut("execution(* com.blog.dao.BookDao.findName(..))")
    public void pt(){}

    @Before("pt()")
    public void before(){
        System.out.println("before advice ...");
    }

    @After("pt()")
    public void after(){
        System.out.println("after advice ...");
    }

    @Around("pt()")
    public Object around(ProceedingJoinPoint pjp) throws Throwable {
        Object res = pjp.proceed();
        return res;
    }

    @AfterReturning("pt()")
    public void afterReturning(){
        System.out.println("afterReturning advice ...");
    }

    @AfterThrowing("pt()")
    public void afterThrowing(){
        System.out.println("afterThrowing advice ...");
    }
}
```

- 编写App运行类

```
JAVA
public class App {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfig.class);
        BookDao bookDao = context.getBean(BookDao.class);
        String name = bookDao.findName(9527);
        System.out.println(name);
    }
}
```

#### 获取参数

- `非环绕通知获取方式`
  在方法上添加JoinPoint，通过JoinPoint来获取参数

```
JAVA
@Component
@Aspect
public class MyAdvice {

    @Pointcut("execution(* com.blog.dao.BookDao.findName(..))")
    public void pt(){}

    @Before("pt()")
    public void before(JoinPoint joinPoint){
        Object[] args = joinPoint.getArgs();
        System.out.println(Arrays.toString(args));
        System.out.println("before advice ...");
    }
}
```

运行App类，可以获取如下内容，说明参数9527已经被获取

> [9527]
> before advice …
> id:9527
> TestName

- **思考:方法的参数只有一个，为什么获取的是一个数组?**
  - 因为参数的个数是不固定的，所以使用数组更通配些。
  - 如果将参数改成两个会是什么效果呢?
- 修改BookDao和BookDaoImpl类

- BookDao
- BookDaoImpl

```
JAVA
public interface BookDao {
    String findName(int id, String name) {
}
```



- 修改App类，调用方法传入多个参数

```
JAVA
public class App {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfig.class);
        BookDao bookDao = context.getBean(BookDao.class);
        String name = bookDao.findName(9527,"Tony");
        System.out.println(name);
    }
}
```

输出结果如下，两个参数都已经被获取到

> [9527, Tony]
> before advice …
> id:9527
> TestName

- `环绕通知获取方式`
  环绕通知使用的是ProceedingJoinPoint，因为ProceedingJoinPoint是JoinPoint类的子类，所以对于ProceedingJoinPoint类中应该也会有对应的`getArgs()`方法，我们去验证下

```
JAVA
@Component
@Aspect
public class MyAdvice {

    @Pointcut("execution(* com.blog.dao.BookDao.findName(..))")
    public void pt(){}

    @Around("pt()")
    public Object around(ProceedingJoinPoint pjp) throws Throwable {
        Object[] args = pjp.getArgs();
        System.out.println(Arrays.toString(args));
        Object res = pjp.proceed();
        return res;
    }
}
```

运行App后查看运行结果，说明ProceedingJoinPoint也是可以通过getArgs()获取参数

> [9527, Tony]
> id:9527
> TestName

```
注意:
```

- pjp.proceed()方法是有两个构造方法，分别是:
  - proceed()
  - proceed(Object[] object)
- 调用无参数的proceed，当原始方法有参数，会在调用的过程中自动传入参数
- 所以调用这两个方法的任意一个都可以完成功能
- 但是当需要修改原始方法的参数时，就只能采用带有参数的方法,如下

```
JAVA
@Component
@Aspect
public class MyAdvice {

    @Pointcut("execution(* com.blog.dao.BookDao.findName(..))")
    public void pt(){}

    @Around("pt()")
    public Object around(ProceedingJoinPoint pjp) throws Throwable {
        Object[] args = pjp.getArgs();
        System.out.println(Arrays.toString(args));
        args[0] = 9421;
        Object res = pjp.proceed(args);
        return res;
    }
}
```

运行程序，输出结果如下

> [9527, Tony]
> id:9421
> TestName

有了这个特性后，我们就可以在环绕通知中对原始方法的参数进行拦截过滤，避免由于参数的问题导致程序无法正确运行，还可以根据参数来给予不同的权限，提高代码的健壮性。

#### 获取返回值

对于返回值，只有返回后`AfterReturing`和环绕`Around`这两个通知类型可以获取，具体如何获取?

- 环绕通知获取返回值

```
JAVA
@Component
@Aspect
public class MyAdvice {

    @Pointcut("execution(* com.blog.dao.BookDao.findName(..))")
    public void pt(){}

    @Around("pt()")
    public Object around(ProceedingJoinPoint pjp) throws Throwable {
        Object[] args = pjp.getArgs();
        System.out.println(Arrays.toString(args));
        args[0] = 9421;
        Object res = pjp.proceed(args);
        return res;
    }
}
```

上述代码中，`res`就是方法的返回值，我们是可以直接获取，不但可以获取，如果需要还可以进行修改。

- 返回后通知获取返回值

```
JAVA
@Component
@Aspect
public class MyAdvice {

    @Pointcut("execution(* com.blog.dao.BookDao.findName(..))")
    public void pt(){}

    @AfterReturning(value = "pt()", returning = "res")
    public void afterReturning(Object res){
        System.out.println("afterReturning advice ..." + res);
    }
}
```

运行程序，输出如下，成功获取了返回值

> id:9527
> afterReturning advice …TestName
> TestName

几点注意:

1. 参数名的问题
   赋给returning的值，必须与Object类型参数名一致，上面的代码中均为`res`
2. afterReturning方法参数类型的问题
   参数类型可以写成String，但是为了能匹配更多的参数类型，建议写成Object类型
3. afterReturning方法参数的顺序问题
   如果存在JoinPoint参数，则必须将其放在第一位，否则运行将报错

```
JAVA
public void afterReturning(JoinPoint jp,Object res)
```

#### 获取异常

对于获取抛出的异常，只有抛出异常后`AfterThrowing`和环绕`Around`这两个通知类型可以获取，具体如何获取?

- `环绕通知获取异常`
  这块比较简单，以前我们是抛出异常，现在只需要将异常捕获，就可以获取到原始方法的异常信息了

```
JAVA
@Component
@Aspect
public class MyAdvice {

    @Pointcut("execution(* com.blog.dao.BookDao.findName(..))")
    public void pt(){}

    @Around("pt()")
    public Object around(ProceedingJoinPoint pjp) {
        Object[] args = pjp.getArgs();
        System.out.println(Arrays.toString(args));
        args[0] = 9421;
        Object res = null;
        try {
            res = pjp.proceed(args);
        } catch (Throwable e) {
            throw new RuntimeException(e);
        }
        return res;
    }
}
```

在catch方法中就可以获取到异常，至于获取到异常以后该如何处理，这个就和你的业务需求有关了。

- `抛出异常后通知获取异常`

```
JAVA
@Component
@Aspect
public class MyAdvice {

    @Pointcut("execution(* com.blog.dao.BookDao.findName(..))")
    public void pt() {
    }

    @AfterThrowing(value = "pt()", throwing = "throwable")
    public void afterThrowing(Throwable throwable) {
        System.out.println("afterThrowing advice ..." + throwable);
    }
}
```

那现在我们只需要让原始方法抛一个异常来看看效果

```
JAVA
@Repository
public class BookDaoImpl implements BookDao {
    public String findName(int id, String name) {
        System.out.println("id:" + id);
        int a = 1 / 0;
        return "TestName";
    }
}
```

运行程序，输出如下，成功输出了异常

> [9527, Tony]
> id:9421
> afterThrowing advice …java.lang.ArithmeticException: / by zero
> Exception in thread “main” java.lang.RuntimeException: java.lang.ArithmeticException: / by zero
> …

至此，AOP通知如何获取数据就已经讲解完了，数据中包含`参数`、`返回值`、`异常(了解)`。

### 百度网盘密码数据兼容处理

#### 需求分析

需求：对百度网盘分享链接输入密码时尾部多输入的空格做兼容处理。
问题描述：

- 当我们从别人发给我们的内容中复制提取码的时候，有时候会多复制到一些空格，直接粘贴到百度的提取码输入框
- 但是百度那边记录的提取码是没有空格的
- 这个时候如果不做处理，直接对比的话，就会引发提取码不一致，导致无法访问百度盘上的内容
- 所以多输入一个空格可能会导致项目的功能无法正常使用。
- 此时我们就想能不能将输入的参数先帮用户去掉空格再操作呢?
  - 答案是可以的，我们只需要在业务方法执行之前对所有的输入参数进行格式处理——trim()
- 那要对所有的参数都需要去除空格么?
  - 也没有必要，一般只需要针对字符串处理即可。

- 以后涉及到需要去除前后空格的业务可能会有很多，这个去空格的代码是每个业务都写么?
  - 可以考虑使用AOP来统一处理。
- AOP有五种通知类型，该使用哪种呢?
  - 我们的需求是将原始方法的参数处理后在参与原始方法的调用，能做这件事的就只有环绕通知。

#### 环境准备

- 创建一个Maven项目
- pom.xml添加Spring依赖

```
XML
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>5.2.10.RELEASE</version>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.4</version>
</dependency>
```

- 添加ResourcesDao和ResourcesDaoImpl，ResourcesService，ResourcesServiceImpl类

- ResourcesDao
- ResourcesDaoImpl
- ResourcesService
- ResourcesServiceImpl

```
JAVA
public interface ResourceDao {
    boolean readResource(String url,String password);
}
```



- 创建Spring配置类

```
JAVA
@Configuration
@ComponentScan("com.blog")
public class SpringConfig {
}
```

- 编写App运行类

```
JAVA
public class App {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfig.class);
        ResourceService service = context.getBean(ResourceService.class);
        boolean flag = service.openURL("https://pan.baidu.com/xx", "root");
        System.out.println(flag);
    }
}
```

现在项目的效果是，当输入密码为"root"控制台打印为true,如果密码改为"root "控制台打印的是false
需求是使用AOP将参数进行统一处理，不管输入的密码`root`前后包含多少个空格，最终控制台打印的都是true。

#### 具体实现

- `步骤一：`开启SpringAOP的注解功能

```
JAVA
@Configuration
@ComponentScan("com.blog")
@EnableAspectJAutoProxy
public class SpringConfig {
}
```

- `步骤二：`编写通知类

```
JAVA
@Component
@Aspect
public class MyAdvice {
    @Pointcut("execution(* com.blog.service.*Service.*(..))")
    public void pt(){}

    @Around("pt()")
    public Object around(ProceedingJoinPoint pjp) throws Throwable {
        Object[] args = pjp.getArgs();
        for (int i = 0; i < args.length; i++) {
            if ((String.class).equals(args[i].getClass())){
                args[i] = args[i].toString().trim();
            }
        }
        Object res = pjp.proceed(args);
        return res;
    }
}
```

- `步骤三：`运行程序
  不管密码`root`前后是否加空格，最终控制台打印的都是true

## AOP总结

### AOP核心概念

- 概念：AOP(Aspect Oriented Programming)面向切面编程，一种编程范式
- 作用：在不惊动原始设计的基础上为方法进行功能`增强`
- 核心概念
  - 代理（Proxy）：SpringAOP的核心本质是采用`代理模式`实现的
  - 连接点（JoinPoint）：在SpringAOP中，理解为任意方法的执行
  - 切入点（Pointcut）：匹配连接点的式子，也是具有共性功能的方法描述
  - 通知（Advice）：若干个方法的共性功能，在切入点处执行，最终体现为一个方法
  - 切面（Aspect）：描述通知与切入点的对应关系
  - 目标对象（Target）：被代理的原始对象成为目标对象

### 切入点表达式

- 切入点表达式标准格式：动作关键字(访问修饰符 返回值 包名.类/接口名.方法名（参数）异常名)

```
JAVA
execution(* com.itheima.service.*Service.*(..))
```

- 切入点表达式描述通配符：
  - 作用：用于快速描述，范围描述
  - `*`：匹配任意符号（常用）
  - `..` ：匹配多个连续的任意符号（常用）
  - `+`：匹配子类类型
- 切入点表达式书写技巧
  1. 按`标准规范`开发
  2. 查询操作的返回值建议使用`*`匹配
  3. 减少使用`..`的形式描述包，效率低
  4. `对接口进行描述`，使用`*`表示模块名，例如UserService的匹配描述为`*Service`
  5. 方法名书写保留动词，例如get，使用`*`表示名词，例如getById匹配描述为getBy`*`
  6. 参数根据实际情况灵活调整

### 五种通知类型

- 前置通知
- 后置通知
- 环绕通知（重点）
  - 环绕通知依赖形参ProceedingJoinPoint才能实现对原始方法的调用
  - 环绕通知可以隔离原始方法的调用执行
  - 环绕通知返回值设置为Object类型
  - 环绕通知中可以对原始方法调用过程中出现的异常进行处理
- 返回后通知
- 抛出异常后通知

### 通知中获取参数

- 获取切入点方法的参数，所有的通知类型都可以获取参数
  - JoinPoint：适用于前置、后置、返回后、抛出异常后通知
  - ProceedingJoinPoint：适用于环绕通知
- 获取切入点方法返回值，前置和抛出异常后通知是没有返回值，后置通知可有可无，所以不做研究
  - 返回后通知
  - 环绕通知
- 获取切入点方法运行异常信息，前置和返回后通知是不会有，后置通知可有可无，所以不做研究
  - 抛出异常后通知
  - 环绕通知

## AOP事务管理

### Spring事务简介

#### 相关概念

相关概念

- 事务作用：在数据层保障一系列的数据库操作同成功同失败
- Spring事务作用：在数据层或业务层保障一系列的数据库操作同成功同失败

数据层有事务我们可以理解，为什么业务层也需要处理事务呢？举个简单的例子

- 转账业务会有两次数据层的调用，一次是加钱一次是减钱
- 把事务放在数据层，加钱和减钱就有两个事务
- 没办法保证加钱和减钱同时成功或者同时失败
- 这个时候就需要将事务放在业务层进行处理。

Spring为了管理事务，提供了一个平台事务管理器`PlatformTransactionManager`

```
JAVA
public interface PlatformTransactionManager extends TransactionManager {
    TransactionStatus getTransaction(@Nullable TransactionDefinition var1) throws TransactionException;

    void commit(TransactionStatus var1) throws TransactionException;

    void rollback(TransactionStatus var1) throws TransactionException;
}
```

commit是用来提交事务，rollback是用来回滚事务。

PlatformTransactionManager只是一个接口，Spring还为其提供了一个具体的实现:

```
JAVA
public class DataSourceTransactionManager extends AbstractPlatformTransactionManager implements ResourceTransactionManager, InitializingBean {
    @Nullable
    private DataSource dataSource;
    private boolean enforceReadOnly;
···
···

}
```

从名称上可以看出，我们只需要给它一个DataSource对象，它就可以帮你去在业务层管理事务。其内部采用的是JDBC的事务。所以说如果你持久层采用的是JDBC相关的技术，就可以采用这个事务管理器来管理你的事务。而Mybatis内部采用的就是JDBC的事务，所以后期我们Spring整合Mybatis就采用的这个`DataSourceTransactionManager`事务管理器。

#### 转账案例–需求分析

接下来通过一个案例来学习下Spring是如何来管理事务的。

先来分析下需求:

- 需求: 实现任意两个账户间转账操作
- 需求微缩: A账户减钱，B账户加钱

为了实现上述的业务需求，我们可以按照下面步骤来实现下:

1. 数据层提供基础操作，指定账户减钱（outMoney），指定账户加钱（inMoney）
2. 业务层提供转账操作（transfer），调用减钱与加钱的操作
3. 提供2个账号和操作金额执行转账操作
4. 基于Spring整合MyBatis环境搭建上述操作

#### 转账案例–环境搭建

- `步骤一：`准备数据表
  Tom和Jerry初始金额都是1000

```
SQL
CREATE DATABASE spring_db CHARACTER SET utf8;
USE spring_db;
CREATE TABLE tbl_account(
    id INT PRIMARY KEY AUTO_INCREMENT,
    NAME VARCHAR(35),
    money DOUBLE
);
INSERT INTO tbl_account(`name`,money) VALUES('Tom',1000),('Jerry',1000);
```

- `步骤二：`创建项目导入jar包

```
XML
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>5.2.10.RELEASE</version>
</dependency>
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid</artifactId>
    <version>1.1.16</version>
</dependency>

<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.5.6</version>
</dependency>

<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.46</version>
</dependency>

<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-jdbc</artifactId>
    <version>5.2.10.RELEASE</version>
</dependency>

<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis-spring</artifactId>
    <version>1.3.0</version>
</dependency>

<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>5.2.10.RELEASE</version>
</dependency>
```

- `步骤三：`根据表创建模型类

```
JAVA
public class Account {
    private Integer id;
    private String name;
    private Double money;

    public Account() {
    }

    public Account(Integer id, String name, Double money) {
        this.id = id;
        this.name = name;
        this.money = money;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Double getMoney() {
        return money;
    }

    public void setMoney(Double money) {
        this.money = money;
    }

    @Override
    public String toString() {
        return "Account{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", money=" + money +
                '}';
    }
}
```

- `步骤四：`创建Dao接口

```
JAVA
public interface AccountDao {

    @Update("update tbl_account set money = money + #{money} where name = #{name}")
    void inMoney(@Param("name") String name,@Param("money") Double money);

    @Update("update tbl_account set money = money - #{money} where name = #{name}")
    void outMoney(@Param("name") String name, @Param("money") Double money);
}
```

- `步骤五：`创建Service接口和实现类

- AccountService
- AccountServiceImpl

```
JAVA
public interface AccountService {
    /**
     * 转账操作
     * @param out 转出方
     * @param in 转入方
     * @param money 金额
     */
    public void transfer(String out,String in,Double money);
}
```



- `步骤六：`添加jdbc.properties文件

```
PROPERTIES
jdbc.driver=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/spring_db?useSSL=false
jdbc.username=root
jdbc.password=poassword.
```

- `步骤七：`创建JdbcConfig配置类

```
JAVA
public class JdbcConfig {
    @Value("${jdbc.driver}")
    private String driver;
    @Value("${jdbc.url}")
    private String url;
    @Value("${jdbc.username}")
    private String username;
    @Value("${jdbc.password}")
    private String password;

    @Bean
    public DataSource dataSource() {
        DruidDataSource dataSource = new DruidDataSource();
        dataSource.setDriverClassName(driver);
        dataSource.setUrl(url);
        dataSource.setUsername(username);
        dataSource.setPassword(password);
        return dataSource;
    }
}
```

- `步骤八：`创建MybatisConfig配置类

```
JAVA
public class MyBatisConfig {

    @Bean
    public SqlSessionFactoryBean sqlSessionFactoryBean(DataSource dataSource){
        SqlSessionFactoryBean factory = new SqlSessionFactoryBean();
        factory.setTypeAliasesPackage("com.blog.domain");
        factory.setDataSource(dataSource);
        return factory;
    }

    @Bean
    public MapperScannerConfigurer mapperScannerConfigurer(){
        MapperScannerConfigurer msc = new MapperScannerConfigurer();
        msc.setBasePackage("com.blog.dao");
        return msc;
    }
}
```

- `步骤九:`创建SpringConfig配置类

```
JAVA
@Configuration
@ComponentScan("com.blog")
@PropertySource("jdbc.properties")
@Import({JdbcConfig.class, MyBatisConfig.class})
public class SpringConfig {
}
```

- `步骤十：`编写测试类

```
JAVA
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = SpringConfig.class)
public class AccountServiceTest {
    @Autowired
    private AccountService accountService;

    @Test
    public void testTransfer() {
        accountService.transfer("Tom", "Jerry", 100D);
    }
}
```

#### 事务管理

上述环境，运行单元测试类，会执行转账操作，`Tom`的账户会减少100，`Jerry`的账户会加100。

这是正常情况下的运行结果，但是如果在转账的过程中出现了异常，如

```
JAVA
@Service
public class AccountServiceImpl implements AccountService {
    @Autowired
    protected AccountDao accountDao;

    public void transfer(String out, String in, Double money) {
        accountDao.outMoney(out, money);
        int a = 1 / 0;
        accountDao.inMoney(in, money);
    }
}
```

这个时候就模拟了转账过程中出现异常的情况，此时进行转账，`Tom`的账户会减少100，而`Jerry`的账户却不会增加100
那我们来分析一下刚才的结果

- 程序正常执行时，账户金额A减B加，没有问题
- 程序出现异常后，转账失败，但是异常之前操作成功，异常之后操作失败，整体业务失败

当程序出问题后，我们需要让事务进行回滚，而且这个事务应该是加在业务层上，而Spring的事务管理就是用来解决这类问题的。

Spring事务管理具体的实现步骤如下

- `步骤一：`在需要被事务管理的方法上添加`@Transactional`注解

```
JAVA
@Service
public class AccountServiceImpl implements AccountService {
    @Autowired
    protected AccountDao accountDao;

    @Transactional
    public void transfer(String out, String in, Double money) {
        accountDao.outMoney(out, money);
        int a = 1 / 0;
        accountDao.inMoney(in, money);
    }
}
```

注意:`@Transactional`可以写在接口类上、接口方法上、实现类上和实现类方法上

- 写在接口类上，该接口的所有实现类的所有方法都会有事务
- 写在接口方法上，该接口的所有实现类的该方法都会有事务
- 写在实现类上，该类中的所有方法都会有事务
- 写在实现类方法上，该方法上有事务
- `建议写在实现类或实现类的方法上`

- `步骤二：`在JdbcConfig类中配置事务管理器

```
JAVA
public class JdbcConfig {
    @Value("${jdbc.driver}")
    private String driver;
    @Value("${jdbc.url}")
    private String url;
    @Value("${jdbc.username}")
    private String username;
    @Value("${jdbc.password}")
    private String password;

    @Bean
    public DataSource dataSource() {
        DruidDataSource dataSource = new DruidDataSource();
        dataSource.setDriverClassName(driver);
        dataSource.setUrl(url);
        dataSource.setUsername(username);
        dataSource.setPassword(password);
        return dataSource;
    }

    //配置事务管理器，mybatis使用的是jdbc事务
    @Bean
    public PlatformTransactionManager platformTransactionManager(DataSource dataSource){
        DataSourceTransactionManager transactionManager = new DataSourceTransactionManager();
        transactionManager.setDataSource(dataSource);
        return transactionManager;
    }
}
```

注意：事务管理器要根据使用技术进行选择，Mybatis框架使用的是JDBC事务，可以直接使用`DataSourceTransactionManager`

- `步骤三：`开启事务注解`@EnableTransactionManagement`

```
JAVA
@Configuration
@ComponentScan("com.blog")
@PropertySource("jdbc.properties")
@EnableTransactionManagement
@Import({JdbcConfig.class, MyBatisConfig.class})
public class SpringConfig {
}
```

- `步骤四：`运行测试类
  运行程序之后，我们去数据库查看Tom和Jerry的金额，发现没有变化
  那么说明在转换的业务出现错误后，事务就可以控制回滚，保证数据的正确性。

知识点1：`@EnableTransactionManagement`

| 名称 |      @EnableTransactionManagement      |
| :--: | :------------------------------------: |
| 类型 |               配置类注解               |
| 位置 |             配置类定义上方             |
| 作用 | 设置当前Spring环境中开启注解式事务支持 |

知识点2：`@Transactional`

| 名称 |                        @Transactional                        |
| :--: | :----------------------------------------------------------: |
| 类型 |                   接口注解 类注解 方法注解                   |
| 位置 |         业务层接口上方 业务层实现类上方 业务方法上方         |
| 作用 | 为当前业务层方法添加事务（如果设置在类或接口上方则类或接口中所有方法均添加事务） |

### Spring事务角色

这部分我们重点要理解两个概念，分别是`事务管理员`和`事务协调员`。

当未开启Spring事务之前
[![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://pic.imgdb.cn/item/63180cda16f2c2beb1974dc0.jpg)

- AccountDao的outMoney因为是修改操作，会开启一个事务T1
- AccountDao的inMoney因为是修改操作，会开启一个事务T2
- AccountService的transfer没有事务，
  - 运行过程中如果没有抛出异常，则T1和T2都正常提交，数据正确
  - 如果在两个方法中间抛出异常，T1因为执行成功提交事务，T2因为抛异常不会被执行
  - 就会导致数据出现错误

当开启Spring的事务管理后
[![](img/63180d1a16f2c2beb197868a.jpg)](https://pic.imgdb.cn/item/63180d1a16f2c2beb197868a.jpg)

- transfer上添加了@Transactional注解，在该方法上就会有一个事务T
- AccountDao的outMoney方法的事务T1加入到transfer的事务T中
- AccountDao的inMoney方法的事务T2加入到transfer的事务T中
- 这样就保证他们在同一个事务中，当业务层中出现异常，整个事务就会回滚，保证数据的准确性。

通过上面例子的分析，我们就可以得到如下概念:

- 事务管理员：发起事务方，在Spring中通常指代业务层开启事务的方法
- 事务协调员：加入事务方，在Spring中通常指代数据层方法，也可以是业务层方法

注意：目前的事务管理是基于`DataSourceTransactionManager`和`SqlSessionFactoryBean`使用的是同一个数据源。

### Spring事务属性

这部分我们主要学习三部分内容`事务配置`、`转账业务追加日志`、`事务传播行为`。

#### 事务配置

|          属性          |            作用            |                  示例                   |
| :--------------------: | :------------------------: | :-------------------------------------: |
|        readOnly        |     设置是否为只读事务     |        readOnly = true 只读事务         |
|        timeout         |      设置事务超时时间      |         timeout = -1(永不超时)          |
|      rollbackFor       |  设置事务回滚异常(class)   |  rollbackFor{NullPointException.class}  |
|  rollbackForClassName  | 设置事务回滚异常（String)  |            同上格式为字符串             |
|     noRollbackFor      | 设置事务不回滚异常(class)  | noRollbackFor{NullPointExceptior.class} |
| noRollbackForClassName | 设置事务不回滚异常(String) |            同上格式为字符串             |
|       isolation        |      设置事务隔离级别      |     isolation = Isolation. DEFAULT      |
|      propagation       |      设置事务传播行为      |                    …                    |

上面这些属性都可以在`@Transactional`注解的参数上进行设置。

- readOnly：true只读事务，false读写事务，增删改要设为false,查询设为true。

- timeout:设置超时时间单位秒，在多长时间之内事务没有提交成功就自动回滚，-1表示不设置超时时间。

- rollbackFor:当出现指定异常进行事务回滚

- noRollbackFor:当出现指定异常不进行事务回滚

  - 思考:出现异常事务会自动回滚，这个是我们之前就已经知道的

  - noRollbackFor是设定对于指定的异常不回滚，这个好理解

  - rollbackFor是指定回滚异常，对于异常事务不应该都回滚么，为什么还要指定?

    - 事实上Spring的事务只会对`Error异常`和`RuntimeException异常`及其子类进行事务回顾，其他的异常类型是不会回滚的，如下面的代码就不会回滚

    ```
    JAVA
    @Service
    public class AccountServiceImpl implements AccountService {
        @Autowired
        protected AccountDao accountDao;
    
        @Transactional
        public void transfer(String out, String in, Double money) throws IOException {
            accountDao.outMoney(out, money);
            if (true) throw new IOException();
            accountDao.inMoney(in, money);
        }
    }
    ```

    所以当我们运行程序之后，Tom会少100块钱，而Jerry不会多100块钱，这100块钱就凭空消失了

    - 此时就可以使用rollbackFor属性来设置出现IOException异常不回滚

    ```
    JAVA
    @Service
    public class AccountServiceImpl implements AccountService {
        @Autowired
        protected AccountDao accountDao;
    
        @Transactional(rollbackFor = {IOException.class})
        public void transfer(String out, String in, Double money) throws IOException {
            accountDao.outMoney(out, money);
            if (true) throw new IOException();
            accountDao.inMoney(in, money);
        }
    }
    ```

    - rollbackForClassName等同于rollbackFor,只不过属性为异常的类全名字符串
    - noRollbackForClassName等同于noRollbackFor，只不过属性为异常的类全名字符串
    - isolation设置事务的隔离级别
      - DEFAULT :默认隔离级别, 会采用数据库的隔离级别
      - READ_UNCOMMITTED : 读未提交
      - READ_COMMITTED : 读已提交
      - REPEATABLE_READ : 重复读取
      - SERIALIZABLE: 串行化

介绍完上述属性后，还有最后一个事务的传播行为，为了讲解该属性的设置，我们需要完成下面的案例。

#### 转账业务追加日志案例

\######## 需求分析

- 在前面的转账案例的基础上添加新的需求，完成转账后记录日志。
  - 需求：实现任意两个账户间转账操作，并对每次转账操作在数据库进行留痕
  - 需求微缩：A账户减钱，B账户加钱，数据库记录日志

- 基于上述的业务需求，我们来分析下该如何实现：
  1. 基于转账操作案例添加日志模块，实现数据库中记录日志
  2. 业务层转账操作（transfer），调用减钱、加钱与记录日志功能

- 需要注意一点就是，我们这个案例的预期效果为:
  - `无论转账操作是否成功，均进行转账操作的日志留痕`

\######## 环境准备

- `步骤一：`创建日志表

```
SQL
create table tbl_log(
   id int primary key auto_increment,
   info varchar(255),
   createDate datetime
)
```

- `步骤二：`添加LogDao接口

```
JAVA
public interface LogDao {

    @Insert("insert into tbl_log(info, createDate) VALUES (#{info},now())")
    void log(String info);
}
```

- `步骤三：`添加LogService接口和实现类

- LogService
- LogServiceImpl

```
JAVA
public interface LogService {
    void log(String out, String in, Double money);
}
```



- `步骤四：`在转账的业务中添加记录日志

```
JAVA
@Service
public class AccountServiceImpl implements AccountService {
    @Autowired
    protected AccountDao accountDao;
    @Autowired
    protected LogService logService;

    @Transactional(rollbackFor = {IOException.class})
    public void transfer(String out, String in, Double money) throws IOException {
        try {
            accountDao.outMoney(out, money);
            accountDao.inMoney(in, money);
        } finally {
            logService.log(out, in, money);
        }
    }
}
```

- ```
  步骤五：
  ```

  运行程序

  - 当程序正常运行，tbl_account表中转账成功，tbl_log表中日志记录成功
  - 当转账业务之间出现异常(int i =1 / 0),转账失败，tbl_account成功回滚，但是tbl_log表未添加数据，说明也回滚了
  - 这个结果和我们想要的不一样，什么原因?该如何解决?
    - 失败原因：日志的记录与转账操作隶属同一个事务，同成功同失败（同回滚）
    - 解决方案：继续往下看
    - 预期效果：无论转账操作是否成功，日志必须保留

#### 事务传播行为

[![](img/6318177d16f2c2beb1a2274f.jpg)](https://pic.imgdb.cn/item/6318177d16f2c2beb1a2274f.jpg)

对于上述案例的分析:

- log方法、inMoney方法和outMoney方法都属于增删改，分别有事务T1,T2,T3
- transfer因为加了`@Transactional`注解，也开启了事务T
- 前面我们讲过Spring事务会把T1,T2,T3都加入到事务T中
- 所以当转账失败后，`所有的事务都回滚`，导致日志没有记录下来
- 这和我们的需求不符，这个时候我们就想能不能让log方法单独是一个事务呢?

要想解决这个问题，就需要用到事务传播行为，所谓的事务传播行为指的是:

- 事务传播行为：事务协调员对事务管理员所携带事务的处理态度。
  - 具体如何解决，就需要用到之前我们没有说的`propagation属性`。

- 修改logService改变事务的传播行为

```
JAVA
@Service
public class LogServiceImpl implements LogService {
    @Autowired
    private LogDao logDao;

    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void log(String out, String in, Double money) {
        logDao.log(out + "向" + in + "转账" + money + "元");
    }
}
```

运行后，就能实现我们想要的结果，不管转账是否成功，都会记录日志。

事务传播行为的可选值

| 传播属性       | 事务管理员                                                   | 事务协调员 |
| -------------- | ------------------------------------------------------------ | ---------- |
| REQUIRED(默认) | 开启T                                                        | 加入T      |
| 无             | 新建T2                                                       |            |
| REQUIRES_NEW   | 开启T                                                        | 新建T2     |
| 无             | 新建T2                                                       |            |
| SUPPORTS       | 开启T                                                        | 加入T      |
| 无             | 无                                                           |            |
| NOT_SUPPORTED  | 开启T                                                        | 无         |
| 无             | 无                                                           |            |
| MANDTORY       | 开启T                                                        | 加入T      |
| 无             | ERROR                                                        |            |
| NEVER          | 开启T                                                        | ERROR      |
| 无             | 无                                                           |            |
| NESTED         | 设置savePoint,一旦事务回滚，事务将回滚到savePoint处，交由客户响应提交/回滚 |            |