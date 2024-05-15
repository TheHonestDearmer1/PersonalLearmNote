# Maven - 概述

[Apache Maven POM - Maven中文手册 (17bigdata.com)](http://www.17bigdata.com/book/maven/MAVENZhongWenShouCe/APACHEMAVENPOM.html)

[Maven使用教程（IDEA版）_idea maven-CSDN博客](https://blog.csdn.net/m0_66734853/article/details/124560037)

## Maven 是什么？

Maven 是一个项目管理和整合工具。Maven 为开发者提供了一套完整的构建生命周期框架。开发团队几乎不用花多少时间就能够自动完成工程的基础构建配置，因为 Maven 使用了一个标准的目录结构和一个默认的构建生命周期。

在有多个开发团队环境的情况下，Maven 能够在很短的时间内使得每项工作都按照标准进行。因为大部分的工程配置操作都非常简单并且可复用，在创建报告、检查、构建和测试自动配置时，Maven 可以让开发者的工作变得更简单。

Maven 能够帮助开发者完成以下工作：

- 构建
- 文档生成
- 报告
- 依赖
- SCMs
- 发布
- 分发
- 邮件列表

总的来说，Maven 简化了工程的构建过程，并对其标准化。它无缝衔接了编译、发布、文档生成、团队合作和其他任务。Maven 提高了重用性，负责了大部分构建相关的任务。

## Maven 的历史

Maven 最初是在 Jakarta Turbine 项目中为了简化构建过程而设计的。项目中有几个子工程，每个工程包含稍有不同的 ANT 文件。JAR 文件使用 CVS 管理。

[Apache](http://www.17bigdata.com/book/apache2.2/index.html) 小组随后开发了 Maven，能够同时构建多个工程、发布工程信息、部署工程、在几个工程中共享 JAR 文件，并且协助团队合作。

## Maven 的目标

Maven 的主要目的是为开发者提供

- 一个可复用、可维护、更易理解的工程综合模型
- 与这个模型交互的插件或者工具

Maven 工程结构和内容被定义在一个 xml 文件中 － pom.xml，是 Project Object Model (POM) 的简称，此文件是整个 Maven 系统的基础组件。详细内容请参考 Maven POM 部分。

## 约定优于配置

Maven 使用约定而不是配置，意味着**开发者不需要再自己创建构建过程**。

开发者不需要再关心每一个配置细节。Maven 为工程提供了合理的默认行为。当创建 Maven 工程时，Maven 会创建默认的工程结构。开发者只需要合理的放置文件，而在 pom.xml 中不再需要定义任何配置。

举例说明，下面的表格展示了工程源码文件、资源文件的默认配置，和其他一些配置。假定 `${basedir}` 表示工程目录：

| 配置项             | 默认值                        |
| :----------------- | :---------------------------- |
| source code        | ${basedir}/src/main/java      |
| resources          | ${basedir}/src/main/resources |
| Tests              | ${basedir}/src/test           |
| Complied byte code | ${basedir}/target             |
| distributable JAR  | ${basedir}/target/classes     |

为了构建工程，Maven 为开发者提供了选项来配置生命周期目标和工程依赖（依赖于 Maven 的插件扩展功能和默认的约定）。**大部分的工程管理和构建相关的任务**是由 Maven 插件完成的。

开发人员不需要了解每个插件是如何工作的，就能够构建任何给定的 Maven 工程。详细内容请参考 Maven 插件部分。

# Maven - 环境配置

Maven 是一个基于 Java 的工具，所以要做的第一件事情就是安装 JDK。

## 系统要求

| 项目     | 要求                                                         |
| :------- | :----------------------------------------------------------- |
| JDK      | Maven 3.3 要求 JDK 1.7 或以上 Maven 3.2 要求 JDK 1.6 或以上 Maven 3.0/3.1 要求 JDK 1.5 或以上 |
| 内存     | 没有最低要求                                                 |
| 磁盘     | Maven 自身安装需要大约 10 MB 空间。除此之外，额外的磁盘空间将用于你的本地 Maven 仓库。你本地仓库的大小取决于使用情况，但预期至少 500 MB |
| 操作系统 | 没有最低要求                                                 |

## 步骤 1：检查 Java 安装

现在打开控制台，执行下面的 `java` 命令。

| 操作系统 | 任务           | 命令                              |
| :------- | :------------- | :-------------------------------- |
| Windows  | 打开命令控制台 | `c:\> java -version`              |
| Linux    | 打开命令终端   | `$ java -version`                 |
| Mac      | 打开终端       | `machine:~ joseph$ java -version` |

我们来验证一下所有平台上的输出：

| 操作系统 | 输出                                                         |
| :------- | :----------------------------------------------------------- |
| Windows  | java version "1.6.0_21" Java(TM) SE Runtime Environment (build 1.6.0_21-b07) Java HotSpot(TM) Client VM (build 17.0-b17, mixed mode, sharing) |
| Linux    | java version "1.6.0_21" Java(TM) SE Runtime Environment (build 1.6.0_21-b07) Java HotSpot(TM) Client VM (build 17.0-b17, mixed mode, sharing) |
| Mac      | java version "1.6.0_21" Java(TM) SE Runtime Environment (build 1.6.0_21-b07) Java HotSpot(TM)64-Bit Server VM (build 17.0-b17, mixed mode, sharing) |

如果你没有安装 Java，从以下网址安装 Java 软件开发套件（SDK）：**[Http](https://www.dba.cn/tutorial-id4113.html)://www.oracle.com/technetwork/java/javase/downloads/index.[HTML](http://www.17bigdata.com/book/html/index.html)**。我们假定你安装的 Java 版本为1.6.0_21。

## 步骤 2：设置 Java 环境

设置 `JAVA_HOME` 环境变量，并指向你机器上的 Java 安装目录。例如：

| 操作系统 | 输出                                                         |
| :------- | :----------------------------------------------------------- |
| Windows  | Set the environment variable JAVA_HOME to C:\Program Files\Java\jdk1.6.0_21 |
| Linux    | `export JAVA_HOME=/usr/local/java-current`                   |
| Mac      | `export JAVA_HOME=/Library/Java/Home`                        |

将 Java 编译器地址添加到系统路径中。

| 操作系统 | 输出                                                         |
| :------- | :----------------------------------------------------------- |
| Windows  | 将字符串“;C:\Program Files\Java\jdk1.6.0_21\bin”添加到系统变量“Path”的末尾 |
| Linux    | export PATH=$PATH:$JAVA_HOME/bin/                            |
| Mac      | not required                                                 |

使用上面提到的 **java -version** 命令验证 Java 安装。

## 步骤 3：下载 Maven 文件

从以下网址下载 Maven 3.2.5：**http://maven.[Apache](http://www.17bigdata.com/book/apache2.2/index.html).org/download.html**

[Maven的安装与配置_maven安装-CSDN博客](https://blog.csdn.net/pan_junbiao/article/details/104264644)

apache-maven-3.9.5-bin 要下载bin结尾的文件

## 步骤 4：解压 Maven 文件

解压文件到你想要的位置来安装 Maven 3.2.5，你会得到 apache-maven-3.2.5 子目录。

| 操作系统 | 位置 (根据你的安装位置而定)                                  |
| :------- | :----------------------------------------------------------- |
| Windows  | `C:\Program Files\Apache Software foundation\apache-maven-3.2.5` |
| Linux    | `/usr/local/apache-maven`                                    |
| Mac      | `/usr/local/apache-maven`                                    |

## 步骤 5：设置 Maven 环境变量

添加 M2_HOME、M2、MAVEN_OPTS 到环境变量中。

| 操作系统 | 输出                                                         |
| :------- | :----------------------------------------------------------- |
| Windows  | 使用系统属性设置环境变量。 M2_HOME=C:\Program Files\Apache Software Foundation\apache-maven-3.2.5 M2=%M2_HOME%\bin MAVEN_OPTS=-Xms256m -Xmx512m |
| Linux    | 打开命令终端设置环境变量。 export M2_HOME=/usr/local/apache-maven/apache-maven-3.2.5 export M2=$M2_HOME/bin export MAVEN_OPTS=-Xms256m -Xmx512m |
| Mac      | 打开命令终端设置环境变量。 export M2_HOME=/usr/local/apache-maven/apache-maven-3.2.5 export M2=$M2_HOME/bin export MAVEN_OPTS=-Xms256m -Xmx512m |

## 步骤 6：添加 Maven bin 目录到系统路径中

现在添加 M2 变量到系统“Path”变量中

| 操作系统 | 输出                                    |
| :------- | :-------------------------------------- |
| Windows  | 添加字符串 “;%M2%” 到系统“Path”变量末尾 |
| Linux    | export PATH=$M2:$PATH                   |
| Mac      | export PATH=$M2:$PATH                   |

## 步骤 7：验证 Maven 安装

现在打开控制台，执行以下 **mvn** 命令。

| 操作系统 | 输出           | 命令                              |
| :------- | :------------- | :-------------------------------- |
| Windows  | 打开命令控制台 | `c:\> mvn --version`              |
| Linux    | 打开命令终端   | `$ mvn --version`                 |
| Mac      | 打开终端       | `machine:~ joseph$ mvn --version` |

最后，验证以上命令的输出，应该是像下面这样：

| 操作系统 | 输出                                                         |
| :------- | :----------------------------------------------------------- |
| Windows  | Apache Maven 3.2.5 (r801777; 2009-08-07 00:46:01+0530) Java version: 1.6.0_21 Java home: C:\Program Files\Java\jdk1.6.0_21\jre |
| Linux    | Apache Maven 3.2.5 (r801777; 2009-08-07 00:46:01+0530) Java version: 1.6.0_21 Java home: C:\Program Files\Java\jdk1.6.0_21\jre |
| Mac      | Apache Maven 3.2.5 (r801777; 2009-08-07 00:46:01+0530) Java version: 1.6.0_21 Java home: C:\Program Files\Java\jdk1.6.0_21\jre |

恭喜！你完成了所有的设置，开始使用 Apache Maven 吧。

# Maven - POM

POM 代表工程对象模型。它是使用 Maven 工作时的基本组建，是一个 xml 文件。它被放在工程根目录下，文件命名为 pom.xml。

POM 包含了关于工程和各种配置细节的信息，Maven 使用这些信息构建工程。

POM 也包含了目标和插件。当执行一个任务或者目标时，Maven 会查找当前目录下的 POM，从其中读取所需要的配置信息，然后执行目标。能够在 POM 中设置的一些配置如下：

- project dependencies
- plugins
- goals
- build profiles
- project version
- developers
- mailing list

在创建 POM 之前，我们首先确定工程组（groupId），及其名称（artifactId）和版本，在仓库中这些属性是工程的唯一标识。

## POM 举例

```
<project xmlns="http://maven.apache.org/POM/4.0.0"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
   http://maven.apache.org/xsd/maven-4.0.0.xsd">
   <modelVersion>4.0.0</modelVersion>

   <groupId>com.companyname.project-group</groupId>
   <artifactId>project</artifactId>
   <version>1.0</version>

</project>
```

需要说明的是每个工程应该只有一个 POM 文件。

- 所有的 POM 文件需要 **project** 元素和三个必须的字段：**groupId, artifactId,version**。
- 在仓库中的工程标识为 **groupId:artifactId:version**
- POM.xml 的根元素是 **project**，它有三个主要的子节点：

| 节点       | 描述                                                         |
| :--------- | :----------------------------------------------------------- |
| groupId    | 这是工程组的标识。它在一个组织或者项目中通常是唯一的。例如，一个银行组织 com.company.bank 拥有所有的和银行相关的项目。 |
| artifactId | 这是工程的标识。它通常是工程的名称。例如，消费者银行。groupId 和 artifactId 一起定义了 artifact 在仓库中的位置。 |
| version    | 这是工程的版本号。在 artifact 的仓库中，它用来区分不同的版本。例如： com.company.bank:consumer-banking:1.0 com.company.bank:consumer-banking:1.1. |

## Super POM

所有的 POM 都继承自一个父 POM（无论是否显式定义了这个父 POM）。父 POM 也被称作 **Super POM**，它包含了一些可以被继承的默认设置。

Maven 使用 effective pom（Super pom 加上工程自己的配置）来执行相关的目标，它帮助开发者在 pom.xml 中做尽可能少的配置，当然这些配置可以被方便的重写。

查看 Super POM 默认配置的一个简单方法是执行以下命令：**mvn help:effective-pom**

在你的电脑上的任意目录下创建一个 pom.xml 文件，使用上面提到的示例 pom 中的内容。

在下面的例子中，我们在 `C:\MVN\project` 目录中创建了一个 pom.xml 文件。

现在打开命令控制台，到 pom.xml 所在的目录下执行以下 **mvn** 命令。

```
C:\MVN\project>mvn help:effective-pom
```

Maven 将会开始处理并显示 effective-pom。

```
[INFO] Scanning for projects...
[INFO] Searching repository for plugin with prefix: 'help'.
[INFO] ------------------------------------------------------------------------
[INFO] Building Unnamed - com.companyname.project-group:project-name:jar:1.0
[INFO]    task-segment: [help:effective-pom] (aggregator-style)
[INFO] ------------------------------------------------------------------------
[INFO] [help:effective-pom {execution: default-cli}]
[INFO]

.....

[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESSFUL
[INFO] ------------------------------------------------------------------------
[INFO] Total time: < 1 second
[INFO] Finished at: Thu Jul 05 11:41:51 IST 2012
[INFO] Final Memory: 6M/15M
[INFO] ------------------------------------------------------------------------
```

Effective POM 的结果就像在控制台中显示的一样，经过继承、插值之后，使配置生效。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- ================================================================= -->
<!--                                                                   -->
<!-- Generated by Maven Help Plugin on 2012-07-05T11:41:51             -->
<!-- See: Http://maven.Apache.org/plugins/maven-help-plugin/           -->
<!--                                                                   -->
<!-- ================================================================= -->

<!-- ================================================================= -->
<!--                                                                   -->
<!-- Effective POM for project                                         -->
<!-- 'com.companyname.project-group:project-name:jar:1.0'              -->
<!--                                                                   -->
<!-- ================================================================= -->

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/
2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 h
ttp://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.companyname.project-group</groupId>
  <artifactId>project</artifactId>
  <version>1.0</version>
  <build>
    <sourceDirectory>C:\MVN\project\src\main\java</sourceDirectory>
    <scriptSourceDirectory>src/main/scripts</scriptSourceDirectory>
    <testSourceDirectory>C:\MVN\project\src\test\java</testSourceDirectory>
    <outputDirectory>C:\MVN\project\target\classes</outputDirectory>
    <testOutputDirectory>C:\MVN\project\target\test-classes</testOutputDirectory>
    <resources>
      <resource>
        <mergeId>resource-0</mergeId>
        <directory>C:\MVN\project\src\main\resources</directory>
      </resource>
    </resources>
    <testResources>
      <testResource>
        <mergeId>resource-1</mergeId>
        <directory>C:\MVN\project\src\test\resources</directory>
      </testResource>
    </testResources>
    <directory>C:\MVN\project\target</directory>
    <finalName>project-1.0</finalName>
    <pluginManagement>
      <plugins>
        <plugin>
          <artifactId>maven-antrun-plugin</artifactId>
          <version>1.3</version>
        </plugin>
        <plugin>
          <artifactId>maven-assembly-plugin</artifactId>
          <version>2.2-beta-2</version>
        </plugin>
        <plugin>
          <artifactId>maven-clean-plugin</artifactId>
          <version>2.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-compiler-plugin</artifactId>
          <version>2.0.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-dependency-plugin</artifactId>
          <version>2.0</version>
        </plugin>
        <plugin>
          <artifactId>maven-deploy-plugin</artifactId>
          <version>2.4</version>
        </plugin>
        <plugin>
          <artifactId>maven-ear-plugin</artifactId>
          <version>2.3.1</version>
        </plugin>
        <plugin>
          <artifactId>maven-ejb-plugin</artifactId>
          <version>2.1</version>
        </plugin>
        <plugin>
          <artifactId>maven-install-plugin</artifactId>
          <version>2.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-jar-plugin</artifactId>
          <version>2.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-javadoc-plugin</artifactId>
          <version>2.5</version>
        </plugin>
        <plugin>
          <artifactId>maven-plugin-plugin</artifactId>
          <version>2.4.3</version>
        </plugin>
        <plugin>
          <artifactId>maven-rar-plugin</artifactId>
          <version>2.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-release-plugin</artifactId>
          <version>2.0-beta-8</version>
        </plugin>
        <plugin>
          <artifactId>maven-resources-plugin</artifactId>
          <version>2.3</version>
        </plugin>
        <plugin>
          <artifactId>maven-site-plugin</artifactId>
          <version>2.0-beta-7</version>
        </plugin>
        <plugin>
          <artifactId>maven-source-plugin</artifactId>
          <version>2.0.4</version>
        </plugin>
        <plugin>
          <artifactId>maven-surefire-plugin</artifactId>
          <version>2.4.3</version>
        </plugin>
        <plugin>
          <artifactId>maven-war-plugin</artifactId>
          <version>2.1-alpha-2</version>
        </plugin>
      </plugins>
    </pluginManagement>
    <plugins>
      <plugin>
        <artifactId>maven-help-plugin</artifactId>
        <version>2.1.1</version>
      </plugin>
    </plugins>
  </build>
  <repositories>
    <repository>
      <snapshots>
        <enabled>false</enabled>
      </snapshots>
      <id>central</id>
      <name>Maven Repository Switchboard</name>
      <url>http://repo1.maven.org/maven2</url>
    </repository>
  </repositories>
  <pluginRepositories>
    <pluginRepository>
      <releases>
        <updatePolicy>never</updatePolicy>
      </releases>
      <snapshots>
        <enabled>false</enabled>
      </snapshots>
      <id>central</id>
      <name>Maven Plugin Repository</name>
      <url>http://repo1.maven.org/maven2</url>
    </pluginRepository>
  </pluginRepositories>
  <reporting>
    <outputDirectory>C:\MVN\project\target/site</outputDirectory>
  </reporting>
</project>
```

在上面的 pom.xml 中，你可以看到 Maven 在执行目标时需要用到的默认工程源码目录结构、输出目录、需要的插件、仓库和报表目录。

Maven 的 pom.xml 文件也不需要手工编写。

Maven 提供了大量的原型插件来创建工程，包括工程结构和 pom.xml。

详细内容请参考 **Maven - 插件** 和 **Maven - 创建工程** 部分的内容。

# 依赖没有自动下载

**如果依赖没有自动下载**就在项目中执行命令，就会自动下载依赖：

```cmd
mvn dependency:resolve
```

