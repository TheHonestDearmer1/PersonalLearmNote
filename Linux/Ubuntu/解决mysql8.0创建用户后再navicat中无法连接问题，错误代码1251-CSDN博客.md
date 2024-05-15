 

### 一、连接出错场景

![](https://img-blog.csdnimg.cn/20200114084038852.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDM5MTAxMQ==,size_16,color_FFFFFF,t_70)

这个错误是由mysql8.0创建密码时所采用的密码策略所导致的，mysql在创建用户时默认使用 caching\_sha2\_password 策略，而这种方式在[navicat](https://so.csdn.net/so/search?q=navicat&spm=1001.2101.3001.7020)中是无法连接的

![](https://img-blog.csdnimg.cn/20200114084252270.png)

###  二、解决办法

         mysql8.0以前的版本可以使用 mysql\_native\_password 策略，所以可以将caching\_sha2\_password 修改为mysql\_native\_password

>         执行命令：alter user root@'%' identified with mysql\_native\_password;

        ![](https://img-blog.csdnimg.cn/20200114090235686.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDM5MTAxMQ==,size_16,color_FFFFFF,t_70)

        可是修改后在连接时出现1045错误

        ![](https://img-blog.csdnimg.cn/20200114085143366.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDM5MTAxMQ==,size_16,color_FFFFFF,t_70)

       原因在于执行alter user root@'%' identified with mysql\_native\_password;时，root@'%'用户的密码被重新初始化，所以需要对用户密码进行修改

> alter user root@'%' identified with mysql\_native\_password by '123456';

       如果继续出现1251错误，可能是同名不同主机的用户存在权限叠加问题，可以执行 drop user root@'localhost';把出错用户删掉。

本文转自 <https://blog.csdn.net/weixin_40391011/article/details/103967170>，如有侵权，请联系删除。