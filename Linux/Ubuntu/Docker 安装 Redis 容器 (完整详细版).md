 

> [Docker 安装 (完整详细版)](https://blog.csdn.net/BThinker/article/details/123358697 "Docker 安装 (完整详细版)")
> 
> [Docker 日常命令大全(完整详细版)](https://blog.csdn.net/BThinker/article/details/123355362 "Docker 日常命令大全(完整详细版)")

#### 1、获取Redis镜像 

> Docker如果想安装软件 , 必须先到 Docker 镜像仓库下载镜像。 
> 
> [Docker 镜像仓库](https://hub.docker.com/_/redis?tab=tags "Docker 镜像仓库")

![](https://img-blog.csdnimg.cn/a7eff82490c149729c2c4b26d3fed586.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAVG91Y2gm,size_20,color_FFFFFF,t_70,g_se,x_16)​

#### 2、下载Redis镜像

| 命令 | 描述 |
| --- | --- |
| docker pull redis | 下载最新版Redis镜像 (其实此命令就等同于 : docker pull redis:latest ) |
| docker pull redis:xxx | 下载指定版本的Redis镜像 (xxx指具体版本号) |

![](https://img-blog.csdnimg.cn/0808658eda074e84b7b9b222e47eeffc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAVG91Y2gm,size_20,color_FFFFFF,t_70,g_se,x_16)

>  检查当前所有Docker下载的镜像

```undefined
docker images
```

![](https://img-blog.csdnimg.cn/3413ab83bec64ff4823571cf63e60d0c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAVG91Y2gm,size_20,color_FFFFFF,t_70,g_se,x_16)

####  3、创建Redis配置文件

> 启动前需要先创建Redis外部挂载的配置文件 （ /home/redis/conf/redis.conf ）  
> 之所以要先创建 , 是因为Redis本身容器只存在 /etc/redis 目录 , 本身就不创建 redis.conf 文件  
> 当服务器和容器都不存在 redis.conf 文件时, 执行启动命令的时候 docker 会将 redis.conf 作为目录创建 , 这并不是我们想要的结果 。

```cobol
## 创建目录mkdir -p /home/redis/conf## 创建文件touch /home/redis/conf/redis.conf
```

![](https://img-blog.csdnimg.cn/7b335dcfb0944505a71bf135d7611157.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAVG91Y2gm,size_20,color_FFFFFF,t_70,g_se,x_16)

#### 4、创建Redis容器并启动

> Docker 创建 Redis 容器命令

```cobol
docker run \-d \--name redis \-p 6379:6379 \--restart unless-stopped \-v /home/redis/data:/data \-v /home/redis/conf/redis.conf:/etc/redis/redis.conf \redis-server /etc/redis/redis.conf \redis:bullseye  
```

| 命令 | 描述 |
| --- | --- |
| –name redis | 启动容器的名字 |
| \-d  |  后台运行 |
| \-p 6379:6379  |  将容器的 6379(后面那个) 端口映射到主机的 6379(前面那个) 端口 |
| –restart unless-stopped | 容器重启策略 |
| \-v /home/redis/data:/data | 将Redis储存文件夹挂在到主机 |
| \-v /home/redis/conf/redis.conf:/etc/redis/redis.conf  | 将配置文件夹挂在到主机 |
| \-d redis:bullseye | 启动哪个版本的 Redis (本地镜像的版本) |
| redis-server /etc/redis/redis.conf  | Redis 容器中设置 redis-server 每次启动读取 /etc/redis/redis.conf 这个配置为准 |
| \--appendonly yes | 在Redis容器启动redis-server服务器并打开Redis持久化配置 |
| \\  | shell 命令换行 |

>     注意 : 命令中所有 冒号 前面的是主机配置 , 冒号 后面的是redis容器配置 。  
> –restart unless-stopped : 在docker重启时重启当前容器。但不包含docker重启时已停止的容器。

```cobol
# 本次执行命令：docker run --name redis -p 6379:6379 \-v /home/redis/data:/data \-v /home/redis/conf/redis.conf:/etc/redis/redis.conf \-d redis:bullseye redis-server /etc/redis/redis.conf 
```

5、查看Redis是否运行

```perl
### 查看Docker运行中的容器docker ps docker ps | grep redis
```

![](https://img-blog.csdnimg.cn/72945154265b41078dc1d601cbcf79fa.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAVG91Y2gm,size_20,color_FFFFFF,t_70,g_se,x_16)

> Docker日志查看

```undefined
docker logs redis
```

![](https://img-blog.csdnimg.cn/98b048d4ed2f47dd9803b562ef3e131b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAVG91Y2gm,size_20,color_FFFFFF,t_70,g_se,x_16)

>  报错：chown: changing ownership of '.': Permission denied，权限不足！[请跳转！！！](https://baocl.blog.csdn.net/article/details/115701152 "请跳转！！！")

#### 6、进入Redis容器

```bash
### 通过 Docker 命令进入 Redis 容器内部docker exec -it redis /bin/bashdocker exec -it redis bash### 进入 Redis 控制台redis-cli### 添加一个变量为 key 为 name , value 为 bella 的内容> set name bella### 查看 key 为 name 的 value 值> get name  ### 或者也可以直接通过Docker Redis 命令进入Redis控制台 (上面两个命令的结合)docker exec -it redis redis-cli
```

![](https://img-blog.csdnimg.cn/1e0fd15dcafa427b92ab1184a5c52951.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAVG91Y2gm,size_20,color_FFFFFF,t_70,g_se,x_16)

####  7、退出容器

```php
exit
```

#### 8、Redis 配置文件修改

> 修改 /home/redis/conf/redis.conf

| 命令 | 功能 |
| --- | --- |
| appendonly yes |  启动Redis持久化功能 (默认 no , 所有信息都存储在内存 \[重启丢失\] 。 设置为 yes , 将存储在硬盘 \[重启还在\]) |
| protected-mode no |  关闭protected-mode模式，此时外部网络可以直接访问 (docker貌似自动开启了) |
| bind 0.0.0.0 | 设置所有IP都可以访问 (docker貌似自动开启了) |
| requirepass 密码 |  设置密码 |

####  9、进入有密码的Redis控制台

> 如果你设置了密码,需要通过如下命令进入Redis控制台 

    ![](https://img-blog.csdnimg.cn/4eab973d495041bb88853d0c08a5e47d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAVG91Y2gm,size_20,color_FFFFFF,t_70,g_se,x_16)

```cobol
## 进入Redis容器docker exec -it redis /bin/bash ## 通过密码进入Redis控制台redis-cli -h 127.0.0.1 -p 6379 -a 123456
```

![](https://img-blog.csdnimg.cn/1dd6a665f9484755a650ac824956a85f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAVG91Y2gm,size_20,color_FFFFFF,t_70,g_se,x_16)  
    
      
 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[云原生入门技能树](https://edu.csdn.net/skill/cloud_native/cloud_native-3eb56d157f784765b43f6f2ef0f28aac?utm_source=csdn_ai_skill_tree_blog)[容器(docker)](https://edu.csdn.net/skill/cloud_native/cloud_native-3eb56d157f784765b43f6f2ef0f28aac?utm_source=csdn_ai_skill_tree_blog)[安装docker](https://edu.csdn.net/skill/cloud_native/cloud_native-3eb56d157f784765b43f6f2ef0f28aac?utm_source=csdn_ai_skill_tree_blog)18113 人正在系统学习中

本文转自 <https://blog.csdn.net/BThinker/article/details/123374236>，如有侵权，请联系删除。