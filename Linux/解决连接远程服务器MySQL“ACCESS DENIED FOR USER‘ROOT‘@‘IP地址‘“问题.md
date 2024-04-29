 

**用远程软件连接服务器上安装的MySQL，有时出现：Access denied for user ‘root’@‘IP地址’** **,出现这种问题，主要的原因就是权限配置的时候 没有配置正确。**

当用[Linux](https://so.csdn.net/so/search?q=Linux&spm=1001.2101.3001.7020)/unix的tty 登陆进MYSQL 时， mysql -u root -p 会提示你输入密码，输入正确的密码后正常登陆。然后在提示符下，打命令：**show grants;**  
会出现root如下的权限表示：

```sql
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY PASSWORD '565491d704013245' WITH GRANT OPTION
```

此时，注意看那个“@”后面的，是localhost 意思是本机登陆，此时，如果你用远程登陆软件来登陆的话，会出现错误提示：Access denied for user ‘root’@‘IP地址’。IP地址那块是你远程机器的IP地址。也就是服务器在告诉你，当你用“IP地址”登陆时，是拒绝的，因为，MYSQL权限设置里并没有给你对应你IP地址登陆的权限。因为刚才的SHOW GRANTS;命令结果已经告诉你了，仅限本机登陆。

**那解决方法如下：**

此时，你可以尝试用空密码连接，是可以连接进入的。或者你在服务器的tty 或者pts操作台中进入服务器后执行如下的命令：

```sql
grant all privileges on *.* to 'root'@'%' with grant option;  
```

意思是让root在所有机器都可以登陆到MYSQL服务器(拥有所有权限)。当执行完这条命令后，用客户端登陆，此时，是需要输入口令了。

```sql
GRANT ALL PRIVILEGES
```

（1）**改表法**。可能是你的帐号不允许从远程登陆，只能在localhost。这个时候只要在localhost的那台电脑，登入mysql后，更改 “mysql” 数据库里的 “user” 表里的 “host” 项，从"localhost"改称"%"

**执行的sql代码如下:**

```sql
1. mysql -u root -pvmwaremysql>use mysql;
2. mysql>update user set host = '%' where user = 'root';
3. mysql>select host, user from user;
 
```

（2）**授权法**。  
**\[1\]** 例如，你想myuser(**你数据库用户名:例如root**)使用mypassword(**你的数据库密码**)从任何主机连接到mysql服务器的话。(这种方法亲测有效)

sql代码:

```sql
1. GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'%' IDENTIFIED BY 'mypassword' WITH
GRANT OPTION;
2.FLUSH   PRIVILEGES;
```

**\[2\]** 如果你想允许用户myuser从ip为192.168.1.6的主机连接到mysql服务器，并使用mypassword作为密码

sql代码

```sql
1. GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'192.168.1.3' IDENTIFIED BY 'mypassword' WITH GRANT OPTION;
2. FLUSH   PRIVILEGES;
```

注意授权后必须FLUSH PRIVILEGES;否则无法立即生效。

另外一种方法.

在安装mysql的机器上运行：  
1、d:\\mysql\\bin>mysql -h localhost -u root  
//这样应该可以进入MySQL服务器  
2、mysql>GRANT ALL PRIVILEGES ON _._ TO ‘root’@’%’ WITH GRANT OPTION  
//赋予任何主机访问数据的权限  
3、mysql>FLUSH PRIVILEGES  
//修改生效  
4、mysql>EXIT  
//退出MySQL服务器  
这样就可以在其它任何的主机上以root身份登录啦！

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[MySQL入门技能树](https://edu.csdn.net/skill/mysql/mysql-753300de6ef94af7be40fb91a05421a6?utm_source=csdn_ai_skill_tree_blog)[SQL高级技巧](https://edu.csdn.net/skill/mysql/mysql-753300de6ef94af7be40fb91a05421a6?utm_source=csdn_ai_skill_tree_blog)[CTE和递归查询](https://edu.csdn.net/skill/mysql/mysql-753300de6ef94af7be40fb91a05421a6?utm_source=csdn_ai_skill_tree_blog)83928 人正在系统学习中

本文转自 <https://blog.csdn.net/m0_49102380/article/details/121325816>，如有侵权，请联系删除。