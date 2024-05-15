 

#### 文章目录

*   *   [一、前言](#_2)
    *   [二、codimd是什么？](#codimd_6)
    *   *   [2.1 源于hackmd的超好用markdown编辑器](#21_hackmdmarkdown_8)
        *   [2.2 codimd的作用](#22_codimd_14)
    *   [三、安装和使用](#_24)
    *   *   [3.1 安装前需要知道的](#31__26)
        *   [3.2 安装步骤](#32__32)
        *   *   [3.2.1 创建数据库](#321__44)
            *   [3.2.2 安装git](#322_git_52)
            *   [3.2.3 安装docker](#323_docker_60)
            *   [3.2.4 安装docker compose](#324_docker_compose_68)
            *   [3.2.5 安装codimd](#325_codimd_74)
            *   [3.2.6 检查是否安装成功](#326__129)
            *   [3.2.7 放行端口](#327__157)
            *   [3.2.8 测试使用](#328__167)
        *   [3.3 开始写作](#33__173)
    *   [四、总结](#_179)
    *   [五、参考资料](#_183)

### 一、前言

最近笔者需要频繁更新和发布文档，因此有了寻找一个在线[markdown](https://www.runoob.com/markdown/md-tutorial.html)文档平台的想法。我最终在作业部落，gitbook，codimd之中选择了codimd，并且将其部署到了自己的服务器以便提高访问速度，因此写下这篇博客记录自己**部署和使用的心得**，供大家参考借鉴。

### 二、codimd是什么？

#### 2.1 源于hackmd的超好用markdown编辑器

hackmd是一款著名的在线协作markdown编辑器产品

CodiMD是HackMD的**免费开源版本**

#### 2.2 codimd的作用

*   在线编辑markdown文档
*   在线发布markdown文档
*   和别人在线协作编辑markdown文档

你可以使用**官方**提供的[codimd服务](https://demo.codimd.org/)

![](https://imgconvert.csdnimg.cn/aHR0cDovL25leHRjbG91ZC5oZWxsb2NoYW9zLmNuL2luZGV4LnBocC9zL2lBbWMyTUtEZWJrY2p5Sy9wcmV2aWV3?x-oss-process=image/format,png)

### 三、安装和使用

#### 3.1 安装前需要知道的

*   安装之后你可以使用的功能和[官方](https://demo.codimd.org/)是一样的
*   安装的好处是，codimd官方的服务器在美国，在国内访问速度慢，部署到自己的服务器可以提高访问速度，也便于自己掌控数据库
*   目前codimd是开放系统，所有人都可以注册和使用你服务器上的codimd服务

#### 3.2 安装步骤

笔者是参考[官方文档](https://hackmd.io/c/codimd-documentation/%2Fs%2Fcodimd-docker-deployment)进行安装的

总共需要以下步骤：

*   在MySQL建立codimd使用的数据库
*   安装git
*   安装docker
*   安装docker-compose
*   安装codimd

##### 3.2.1 创建数据库

笔者使用宝塔面板，因此直接如图添加一个数据库

请注意**允许所有ip访问该数据库**，因为[docker](https://so.csdn.net/so/search?q=docker&spm=1001.2101.3001.7020)容器访问不属于本地ip访问，可以看[详细解释](https://jingsam.github.io/2018/10/16/host-in-docker.html)

![image-20200428231026983](https://imgconvert.csdnimg.cn/aHR0cDovL25leHRjbG91ZC5oZWxsb2NoYW9zLmNuL2luZGV4LnBocC9zL2F6ZmZLYVdORmlpSFI0ay9wcmV2aWV3?x-oss-process=image/format,png)

##### 3.2.2 安装git

笔者直接使用yum进行安装，执行以下指令即可

```
yum install git
```

##### 3.2.3 安装docker

同样使用yum进行安装，执行以下指令即可

```
yum install docker
```

##### 3.2.4 安装docker compose

```
yum install docker-compose
```

##### 3.2.5 安装codimd

```yml
version: "3"
services:
  codimd:
    image: nabo.codimd.dev/hackmdio/hackmd:2.0.1
    environment:
      - CMD_DB_URL=postgres://codimd:change_password@database/codimd
      - CMD_USECDN=false
    ports:
      - "3000:3000"
    volumes:
      - upload-data:/home/hackmd/app/public/uploads
    restart: always
volumes:
  upload-data: {}
```

你需要执行以下步骤完成codimd的安装：

*   在一个目录下创建 `docker-compose.yml`，向其中粘贴以上内容
    
*   修改其中的配置信息
    
*   在该目录下执行`docker-compose up -d`即可完成安装
    

配置信息说明:

```
postgres://codimd:change_password@database/codimd
```

这一行中各个参数的含义分别是：

```
 数据库连接协议://用户名:密码@数据库主机:数据库端口/数据库名
```

我使用的是MySQL，数据库名和用户名都是codimd，因此改成：

```
mysql://codimd:密码@172.18.0.1:3306/codimd
```

这里我的MySQL是在docker的宿主机本地安装的，但是主机ip没有写localhost，因为localhost在docker容器里面会解释成容器本身的ip，这样就连不上安装在宿主机的MySQL，所以我使用：

```
ip addr show docker0
```

查看了宿主机的ip为172.18.0.1，然后使用宿主机ip代替localhost，就达到容器内部访问外部的MySQL数据库的目的，可以看[其他解决方案和详细解释](https://jingsam.github.io/2018/10/16/host-in-docker.html)

##### 3.2.6 检查是否安装成功

安装完成后可以使用`docker ps`命令查看codimd是否已经运行

查看运行日志：执行以下命令

```
docker logs -f -t --tail 行数 容器名
```

通过上面的`docker ps`命令中看到容器名为codimd\_codimd\_1

所以我执行

```
docker logs -f -t --tail 10  codimd_codimd_1
```

看到

```
HTTP Server listening at 0.0.0.0:3000
```

这样的日志就表示安装成功了

##### 3.2.7 放行端口

codimd默认是运行在3000端口的，因此需要防火墙放行

*   防火墙放行3000端口
    
*   阿里云安全组规则放行3000端口
    

你可以使用[端口扫描工具](https://tool.chinaz.com/port)确认端口已经正确放行

##### 3.2.8 测试使用

访问你的服务器主机ip的3000端口，即可看到codimd的主页

![image-20200428232641617](https://imgconvert.csdnimg.cn/aHR0cDovL25leHRjbG91ZC5oZWxsb2NoYW9zLmNuL2luZGV4LnBocC9zL29vRFdFeEZpYVpRZEhvYi9wcmV2aWV3?x-oss-process=image/format,png)

#### 3.3 开始写作

有了codimd之后你就可以在线编辑你的markdown文档了，还可以邀请别人一起编辑

![](https://imgconvert.csdnimg.cn/aHR0cDovL25leHRjbG91ZC5oZWxsb2NoYW9zLmNuL2luZGV4LnBocC9zL2FrTGdmSDVhYWZXWkU2ai9wcmV2aWV3?x-oss-process=image/format,png)

### 四、总结

笔者在整个codimd的安装过程还是比较顺利，使用docker-compose安装十分便捷，主要遇到的问题是第一次安装之后查看日志发现访问不了数据库，后来查了资料才知道docker容器内访问localhost会被解释成docker容器本身的ip而不是常规的127.0.0.1，而且，使用docker容器访问数据库，也不属于本地服务器访问数据库。安装完成之后使用起来还是比较方便的，编辑器的页面比较美观，终于可以摆脱离线编辑文档还要写各种版本号更新记录的日子了。

### 五、参考资料

*   [codimd官方文档](https://hackmd.io/c/codimd-documentation/%2Fs%2Fcodimd-docker-deployment)
*   [Docker容器访问宿主机网络](https://jingsam.github.io/2018/10/16/host-in-docker.html)
*   [hackmd的安装与维护](https://www.zybuluo.com/zhongdao/note/1446729)

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[云原生入门技能树](https://edu.csdn.net/skill/cloud_native/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/cloud_native/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/cloud_native/?utm_source=csdn_ai_skill_tree_blog)16362 人正在系统学习中

本文转自 <https://blog.csdn.net/weixin_43001913/article/details/105870156>，如有侵权，请联系删除。