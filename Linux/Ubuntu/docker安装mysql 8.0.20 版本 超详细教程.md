 

[docker](https://so.csdn.net/so/search?q=docker&spm=1001.2101.3001.7020)安装mysql版本8.0.20

第一步 下拉镜像

```bash
docker pull mysql:8.0.20
```

![](https://img-blog.csdnimg.cn/20200502144724949.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTQ1NzYyOTE=,size_16,color_FFFFFF,t_70)

### 第二步 启动镜像

```bash
docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=123456  -d mysql:8.0.20
```

![](https://img-blog.csdnimg.cn/20200502144853961.jpg)

**查看是否启动成功**

```bash
docker ps -a
```

![](https://img-blog.csdnimg.cn/20200502144908897.jpg)

### 第三步 启动成功后，进入容器内部拷贝配置文件，到宿主主机。

```bash
docker cp  mysql:/etc/mysql /mnt/sda1/mysql8.0.20
```

### ![](https://img-blog.csdnimg.cn/20200502144947373.jpg)

**拷贝容器的 /etc/mysql目录到 主机目录/mnt/sda1/mysql8.0.20**

### 第四步 删除mysql容器，重新创建容器

```bash
docker stop mysql
```

**先停止容器**

### ![](https://img-blog.csdnimg.cn/20200502145018720.png)

**再删除容器**

```bash
docker rm mysql
```

### ![](https://img-blog.csdnimg.cn/20200502145032243.png)

### 第五步 启动mysql ，挂载配置文件，数据持久化到宿主主机

**启动脚本 文件名为mysql8.0.20.sh**

```bash
#!/bin/shdocker run \-p 3306:3306 \--name mysql \--privileged=true \--restart unless-stopped \-v /mnt/sda1/mysql8.0.20/mysql:/etc/mysql \-v /mnt/sda1/mysql8.0.20/logs:/logs \-v /mnt/sda1/mysql8.0.20/data:/var/lib/mysql \-v /etc/localtime:/etc/localtime \-e MYSQL_ROOT_PASSWORD=123456 \-d mysql:8.0.20
```

### ![](https://img-blog.csdnimg.cn/20200502145056627.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTQ1NzYyOTE=,size_16,color_FFFFFF,t_70)

**命令解释：**

 -p 端口映射

\--privileged=true  挂载文件权限设置

\--restart unless-stopped  设置 开机后自动重启容器

\-v /mnt/sda1/mysql8.0.20/mysql:/etc/mysql    挂载配置文件

\-v /mnt/sda1/mysql8.0.20/logs:/logs \\      挂载日志

\-v /mnt/sda1/mysql8.0.20/data:/var/lib/mysql \\  挂载数据文件 持久化到主机，

\-v /etc/localtime:/etc/localtime    容器时间与宿主机同步

\-e MYSQL\_ROOT\_PASSWORD=123456    设置密码

\-d  mysql:8.0.20   后台启动,mysql

### 第六步，执行脚本 启动镜像

```bash
sh mysql8.0.20.sh
```

### ![](https://img-blog.csdnimg.cn/20200502145408626.png)

**docker ps -a  查看是否启动成功**

![](https://img-blog.csdnimg.cn/20200502145422575.jpg)

**Navicat 连接mysql 查看版本号**

![](https://img-blog.csdnimg.cn/20200502145459939.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTQ1NzYyOTE=,size_16,color_FFFFFF,t_70)

**大功告成----挂载出来的数据文件以及配置文件**

![](https://img-blog.csdnimg.cn/20200502150024502.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTQ1NzYyOTE=,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/20200502150044339.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTQ1NzYyOTE=,size_16,color_FFFFFF,t_70)

### 恭喜安装成功。

如果要修改  mysql的配置信息，直接 修改挂载出来的配置文件即可。

修改完记得重启

**停止mysql**  

```bash
docker stop mysql
```

**启动 mysql** 

```cpp
docker start mysql
```

文章知识点与官方知识档案匹配，可进一步学习相关知识

[云原生入门技能树](https://edu.csdn.net/skill/cloud_native/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/cloud_native/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/cloud_native/?utm_source=csdn_ai_skill_tree_blog)18112 人正在系统学习中

本文转自 <https://blog.csdn.net/u014576291/article/details/105890286>，如有侵权，请联系删除。