 

需求：基于openjdk:8-jdk-alpine镜像，将一个java项目构建为镜像  
实现步骤：

1.  在linux系统检查有无openjdk:8-jdk-alpine镜像

```java
docker images
```

2.  如果没有，需要去镜像仓库拉取镜像，比如[DockerHub](https://hub-stage.docker.com/)  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/c2a4391e57e54133945c5d58abe5ea28.png)  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/00488761029641388693f44c8153f485.png)
3.  复制命令到linux系统控制台

```java
docker pull openjdk:8-jdk-alpine
```

运行成功  
![在这里插入图片描述](https://img-blog.csdnimg.cn/e361376ff2954ba992f3cdeda6f5d518.png)

4.  在linux系统新建一个空目录，然后在目录中新建一个文件，命令为Dockerfile，拷贝java项目的jar包docker-demo.jar到这个目录中  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/edc44d4d5b7d4a54929c2d3765dd0493.png)
5.  编写Dockerfile文件

*   基于openjdk:8-jdk-alpine作为基础镜像
*   将xxx.jar拷贝到镜像中
*   暴露端口
*   编写入口ENTRYPOINT  
    内容如下：

```java
# 基础镜像
FROM openjdk:8-jdk-alpine
# 设定时区
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# 拷贝jar包
COPY docker-demo.jar /tmp/app.jar
#开放端口
EXPOSE 8090
# 入口
ENTRYPOINT ["java", "-jar", "/tmp/app.jar"]
```

6.  进入到当前文件夹目录，然后使用docker build命令构建镜像

```java
docker build -t docker-demo .
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/0da33f17690d48f898d7b07f4ef28fd6.png)  
**\-t**：是给镜像起名，格式依然是repository:tag的格式，不指定tag时，默认为latest；  
**.** :是指定Dockerfile所在目录，如果就在当前目录，则指定为“.”；

7.  此时再用docker images命令可查看构建出来的镜像  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/619d0c0f80094de3a8caf463e56ae662.png)
8.  使用docker run创建容器并运行

```java
docker run -d --name dd -p 8080:8080 docker-demo
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/89ded1760dce4925848642744927a94f.png)  
运行成功！  
10\. 使用[docker](https://so.csdn.net/so/search?q=docker&spm=1001.2101.3001.7020) logs -f \[容器名称\]命令在控制台打印日志

```java
docker logs -f dd
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/f6b4581d696e44ce8345f09d114c0401.png)

10.  在浏览器输入访问地址及接口信息即可访问项目

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Java技能树](https://edu.csdn.net/skill/java/java-20cad95081b4475aaac1c1ebf7af0253?utm_source=csdn_ai_skill_tree_blog)[深入研究容器](https://edu.csdn.net/skill/java/java-20cad95081b4475aaac1c1ebf7af0253?utm_source=csdn_ai_skill_tree_blog)[Collection的功能方法](https://edu.csdn.net/skill/java/java-20cad95081b4475aaac1c1ebf7af0253?utm_source=csdn_ai_skill_tree_blog)144464 人正在系统学习中

本文转自 <https://blog.csdn.net/qq_52121180/article/details/133712422>，如有侵权，请联系删除。

设置自动启动

```bash
sudo docker update mysql --restart=always
```