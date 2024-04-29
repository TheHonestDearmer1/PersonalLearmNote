 

*   **操作前确认当前linux用户是管理员，并且安装有Docker。**
    
*   **启动docker**
    
    ```
     systemctl   start   docker
    ```
    
*   **拉取镜像**
    
    ```
    docker pull mysql:8.0.22
    ```
    
*   **查看镜像是否拉取成功**
    
    ```
    docker images
    ```
    
*   **创建mysql容器** #注意\\前一定加空格
    
    ```linux
    docker run \           
    --restart=always \     #这个参数是mysql在docker启动的时候，也会跟着自动启动
    --name mysql8.0 \      #这个参数是mysql容器的名字
    -p 3306:3306 \         #这个参数是端口号映射
    -v 自己的文件夹路径:/var/lib/mysql \ #路径举例：/root/mysql/data 自己创建的存储mysql数据的文件
    -e MYSQL_ROOT_PASSWORD=root \     #这个参数是是设置用户名为root  密码为root
    -d mysql:8.0.22                   #-d参数是后台运行    
    ```
    
    为什么上边要手动创建自己的路径？我们先来看如果不指定一个自己的路径，那么mysql自动生成的路径是啥样的。
    
    复制这个：
    
    ```
    docker run --restart=always --name mysql8.0 -p 3306:3306 -v /var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456   -d mysql:8.0.20 
    ```
    
    
    
*   查看未指定数据存储路径的mysql容器的自动数据卷挂载
    

```bash
docker  inspect  容器名           #我这里容器名是mysql8.0
```

mysql容器会自动创建匿名卷

![image-20240118190952408](https://img-blog.csdnimg.cn/img_convert/a2c9705e0ff8decd3739c09da35d87b3.png)

可以看到这个默认的路径太复杂了，而这个文件很重要，我们数据库存储的信息都在这个文件内，我们经常要用到这个文件。所以在创建mysql的时候给他更改路径，方便后续我们去找到这个文件。也便于mysql的版本更替。

容器创建完成后，进入容器内部的命令终端

```
 docker exec -it mysql8.0 bash     #mysql8.0是mysql容器的名字。
```

```
mysql -uroot -proot             //-u用户   -p密码   登录  
```

//登录mysql -u和用户名root之间不要有空格

```

use mysql；                 //切换到mysql库（mysql库是默认的系统库） 这里的命令的分号一定不能少

select host, user, authentication_string, plugin from user;  查询权限，是否允许外部主机访问

update user set host='%' where user='root';   //设置允许外部主机访问

FLUSH PRIVILEGES;    //刷新设置
```

如果你是从windows上用mysql图形化工具连接linux上的[mysql数据库](https://so.csdn.net/so/search?q=mysql%E6%95%B0%E6%8D%AE%E5%BA%93&spm=1001.2101.3001.7020)，那么host下要是%才行。

![image-20240120141934772](https://img-blog.csdnimg.cn/img_convert/d52d8fefbd59cd541d6917e28ed20e6b.png)

这里的caching\_sha2\_password会导致Windows的图形化工具在连接mysql时报下面的问题

![image-20240120114703520](https://img-blog.csdnimg.cn/img_convert/19844950ae537cc136860e2820daad7d.png)

**解决方法**

```

##更改root用户加密方式

#更改本地主机
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password by '你的密码';

#新建的用户默认也会是caching\_sha2\_password 所以在写代码的时候也要改
#更改所有主机
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '你的密码';
//刷新设置
FLUSH PRIVILEGES;
```

运行结果  
![](https://img-blog.csdnimg.cn/img_convert/8250719d2ad199e2549024557dae208b.png)

**更改后连接成功** #若不行那就重启下Windows下的mysql的图形化管理工具

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[云原生入门技能树](https://edu.csdn.net/skill/cloud_native/cloud_native-3eb56d157f784765b43f6f2ef0f28aac?utm_source=csdn_ai_skill_tree_blog)[容器(docker)](https://edu.csdn.net/skill/cloud_native/cloud_native-3eb56d157f784765b43f6f2ef0f28aac?utm_source=csdn_ai_skill_tree_blog)[安装docker](https://edu.csdn.net/skill/cloud_native/cloud_native-3eb56d157f784765b43f6f2ef0f28aac?utm_source=csdn_ai_skill_tree_blog)18115 人正在系统学习中

本文转自 <https://blog.csdn.net/m0_73450879/article/details/135715427>，如有侵权，请联系删除。