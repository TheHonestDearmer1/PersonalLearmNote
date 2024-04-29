 

docker在[安装redis](https://so.csdn.net/so/search?q=%E5%AE%89%E8%A3%85redis&spm=1001.2101.3001.7020)后，一般是没法远程使用的(在考虑防火墙和服务器规则的条件下，当然也可能是bind的问题)，这是很让人头疼的事情，因为没有配置redis的密码

方法一

> 在启动容器的时候，就为其配置密码

```bash
# 拉取redis镜像
docker pull redis

# 启动容器的时候，并为其设置密码
docker run -d --name myredis -p 6379:6379 redis --requirepass "123456"
```

方法二

> 在容器启动后，再为其配置密码

```bash
# 拉取redis镜像
docker pull redis

# 启动容器
docker run -d -p 6366:6379 --name redis-test redis

# 查看运行的redis，并记下它的 CONTAINER ID
docker ps 

# 通过容器id，进入redis
docker exec -it CONTAINER_ID /bin/bash

# 运行redis客户端
redis-cli

# 查看redis的密码
config get requirepass

# 设置redis的密码
config set requirepass yourPassword

# 认证
auth yourPassword
```

其他:

> 思路: 修改docker内的redis的配置文件的 requirepass 行信息

```bash
有的人可能认为，通过进入容器内部，然后去修改redis的配置文件（/etc/redis/redis.conf）
实际上<font color=red>docker的redis是没有配置文件的</font>

如果一定需要配置文件，需要先把当前的redis容器给停止掉，然后将redis.conf给挂载上
```

我没有试过！！！，有人做出来，记得给个链接。

  
友情提示:  

> 若在Redis中保存对象，需要标记对象可序列化(版本号)  
>   
>   
> 在不指定序列化的版本号时，系统将自动给其加上一个版本号------>>>带来的结果就是：本次、本机储存的对象，不能被其他主机、重新启动后读取(会出现部分异常和数据有差错)  
>   
>   
> 解决方法:实现Serializable接口，并指定版本号private static final long serialVersionUID = 1936056658480287561L;  
> 一定要保证每个需要序列化类的版本号是不一样的

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Java技能树](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)144464 人正在系统学习中

本文转自 <https://blog.csdn.net/qq_43324779/article/details/123561461>，如有侵权，请联系删除。