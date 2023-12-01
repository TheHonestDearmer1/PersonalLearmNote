 

#### Docker-安装[MySQL8](https://so.csdn.net/so/search?q=MySQL8&spm=1001.2101.3001.7020).x，挂载本地数据目录和配置文件

*   [1.拉取镜像](#1_1)
*   [2.创建本地目录](#2_10)
*   [3.编辑配置文件](#3_21)
*   [4.运行容器（注意对应本地路径不要错）](#4_52)
*   [5.常用命令](#5_81)
*   [6.环境变量说明](#6_117)
*   [幕](#_149)

1.拉取镜像
------

> *   搜索镜像、拉取镜像  
>       
>     
> 
> ```shell
> $ docker search mysql
> $ docker pull mysql
> ```

2.创建本地目录
--------

> *   创建本地目录、创建本地配置文件
> *   注：路径都是绝对路径，换成你自己的即可  
>       
>     
> 
> ```shell
> $ mkdir /wyj/mysql8 && \
>  touch /wyj/mysql8/my.cnf
> ```

3.编辑配置文件
--------

> *   vim /wyj/mysql8/my.cnf
> *   复制下面的内容到 /wyj/mysql8/my.cnf
> *   注：路径都是绝对路径，换成你自己的即可  
>       
>     
> 
> ```shell
> [mysql]
> #设置mysql客户端默认字符集
> default-character-set=UTF8MB4
> [mysqld]
> #设置3306端口
> port=3306
> #允许最大连接数
> max_connections=200
> #允许连接失败的次数
> max_connect_errors=10
> #默认使用“mysql_native_password”插件认证
> default_authentication_plugin=mysql_native_password
> #服务端使用的字符集默认为8比特编码的latin1字符集
> character-set-server=UTF8MB4
> #开启查询缓存
> explicit_defaults_for_timestamp=true
> #创建新表时将使用的默认存储引擎
> default-storage-engine=INNODB
> #等待超时时间秒
> wait_timeout=60
> #交互式连接超时时间秒
> interactive-timeout=600
> ```

4.运行容器（注意对应本地路径不要错）
-------------------

> *   运行容器，映射端口为3306,（注意对应本地路径不要错）
> *   注：路径都是绝对路径，换成你自己的即可  
>       
>     
> 
> ```shell
> $ docker run \
>   -d \
>   -p 3306:3306 \
>   -v /wyj/mysql8/data:/var/lib/mysql \
>   -v /wyj/mysql8/my.cnf:/etc/mysql/conf.d/my.cnf \
>   -e MYSQL_ROOT_PASSWORD=1234qwer \
>   --restart=always \
>   --privileged=true \
>   --name mysql8 \
>   mysql
>   
> #列出当前所有正在运行的container
> $ docker ps 
> 
> #备用参数
> #许多配置选项可以作为标志传递给mysqld. 无需cnf灵活地自定义。默认编码和排序规则更改为使用 UTF-8 ( utf8mb4)
>  --character-set-server=utf8mb4 
>  --collation-server=utf8mb4_unicode_ci
> 
> ```

5.常用命令
------

> *   常用命令  
>       
>     
> 
> ```shell
> $ docker ps ：列出当前所有正在运行的container
> 
> $ docker ps -a ：列出所有的container（包含历史，即运行过的container）
> 
> $ docker kill id    ： 杀死容器
> 
> $ docker stop id    ： 停止容器
> 
> $ docker start id   ： 启动容器
> 
> $ docker restart id ： 重启容器
> 
> $ docker rmi -f  <image ID>： 删除一个或多个镜像 image
> 
> $ docker rm -f  id   ：  删除指定 镜像 image
> 
> $ docker rm -f <container...>   ：  删除一个或多个container
> 
> $ docker rm  -f `docker ps -a -q`   ： 删除所有的container
> 
> $ docker rm `docker ps -f "status=exited" -q`  ： 删除停止的容器
> 
> $ docker kill`docker ps -a -q` :停止所有container
> 
> $ docker exec -it ng /bin/bash  ：进入容器
> 
> $ docker cp ng:/etc/nginx/nginx.conf /data/nginx.conf   ：拷贝容器内文件到外部
> 
> ```

6.环境变量说明
--------

> *   启动mysql镜像时，您可以通过在docker run命令行中传递一个或多个环境变量来调整 MySQL 实例的配置。请注意，如果您使用已包含数据库的数据目录启动容器，则以下任何变量都不会产生任何影响：任何预先存在的数据库在容器启动时将始终保持不变。

> *   MYSQL\_ROOT\_PASSWORD（必选）  
>     此变量是必需的，并指定将为 MySQLroot超级用户帐户设置的密码。在上面的例子中，它被设置为my-secret-pw。

> *   MYSQL\_DATABASE  
>     此变量是可选的，允许您指定要在映像启动时创建的数据库的名称。如果提供了用户/密码（见下文），则该用户将被授予对此数据库的超级用户访问权限（对应于GRANT ALL）。

> *   MYSQL\_USER, MYSQL\_PASSWORD  
>     这些变量是可选的，用于创建新用户和设置该用户的密码。该用户将被授予MYSQL\_DATABASE变量指定的数据库的超级用户权限（见上文）。要创建用户，这两个变量都是必需的。  
>     请注意，无需使用此机制来创建超级用户超级用户，默认情况下会使用MYSQL\_ROOT\_PASSWORD变量指定的密码创建该用户。

> *   MYSQL\_ALLOW\_EMPTY\_PASSWORD  
>     这是一个可选变量。设置为非空值，例如yes，以允许使用 root 用户的空白密码启动容器。注意：yes除非您真的知道自己在做什么，否则不建议将此变量设置为，因为这将使您的 MySQL 实例完全不受保护，从而允许任何人获得完全的超级用户访问权限。

> *   MYSQL\_RANDOM\_ROOT\_PASSWORD  
>     这是一个可选变量。设置为非空值，例如yes，为 root 用户生成一个随机初始密码（使用pwgen）。生成的 root 密码将打印到 stdout ( GENERATED ROOT PASSWORD: …)。

> *   MYSQL\_ONETIME\_PASSWORD  
>     初始化完成后将root（不是MYSQL\_USER! 中指定的用户）用户设置为过期，强制在首次登录时更改密码。任何非空值都将激活此设置。注意：此功能仅在 MySQL 5.6+ 上受支持。在 MySQL 5.5 上使用此选项将在初始化期间引发适当的错误。

> *   MYSQL\_INITDB\_SKIP\_TZINFO  
>     默认情况下，入口点脚本会自动加载CONVERT\_TZ()函数所需的时区数据。如果不需要，任何非空值都会禁用时区加载。

> *   文件密码  
>     作为通过环境变量传递敏感信息的替代方法，\_FILE可以将其附加到先前列出的环境变量中，从而导致初始化脚本从容器中存在的文件中加载这些变量的值。特别是，这可用于从存储在/run/secrets/<secret\_name>文件中的Docker 机密中加载密码。例如：
> *   $ docker run --name some-mysql -e MYSQL\_ROOT\_PASSWORD\_FILE=/run/secrets/mysql-root -d mysql:tag  
>     目前，这仅支持MYSQL\_ROOT\_PASSWORD，MYSQL\_ROOT\_HOST，MYSQL\_DATABASE，MYSQL\_USER，和MYSQL\_PASSWORD。

幕
-

> *   留白 —<老吉>
> *   ~ 今 ~ ❀ ~ ❀❀❀❀❀❀❀❀❀❀ ❀❀❀❀❀❀❀❀❀❀ ❀❀❀❀❀❀❀

  

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[云原生入门技能树](https://edu.csdn.net/skill/cloud_native/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/cloud_native/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/cloud_native/?utm_source=csdn_ai_skill_tree_blog)16362 人正在系统学习中

本文转自 <https://blog.csdn.net/m0_37969197/article/details/122447630>，如有侵权，请联系删除。