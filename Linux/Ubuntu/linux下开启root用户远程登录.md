 

**Ubuntu默认的root密码在每次重启后都是随机生成的。类似的还有RedHat、CentOS等系统。  
登录你所创建的任意用户，输入sudo passwd，然后输入当前用户密码，即可设置root固定密码了**

**一、允许root用户远程登录**

```
在某些发行版Linux系统下默认是关闭root用户远程登录的，例如：Ubuntu就是，那么怎么开启呢，这里需要找到系统的ssh服务配置文件，然后将PermitRootLogin后no改成yes即可。
```

```cpp
sudo vi /etc/ssh/sshd_config　
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210618132421110.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NoaHNoZGhoZA==,size_16,color_FFFFFF,t_70)  
**二、允许无密码登录**  
找到ssh服务配置文件，两种情况：

将PermitEmptyPasswords yes前面的#号去掉  
将PermitEmptyPasswords 参数值修改为yes，如下图：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210618132459218.png)  
将PermitEmptyPasswords参数值为yes，之后重启SSH服务，命令如下：

```c
service sshd restart # 或者 systemctl restart sshd

```

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[CS入门技能树](https://edu.csdn.net/skill/gml/gml-1c31834f07b04bcc9c5dff5baaa6680c?utm_source=csdn_ai_skill_tree_blog)[Linux入门](https://edu.csdn.net/skill/gml/gml-1c31834f07b04bcc9c5dff5baaa6680c?utm_source=csdn_ai_skill_tree_blog)[初识Linux](https://edu.csdn.net/skill/gml/gml-1c31834f07b04bcc9c5dff5baaa6680c?utm_source=csdn_ai_skill_tree_blog)39857 人正在系统学习中

本文转自 <https://blog.csdn.net/Shhshdhhd/article/details/118024281>，如有侵权，请联系删除。