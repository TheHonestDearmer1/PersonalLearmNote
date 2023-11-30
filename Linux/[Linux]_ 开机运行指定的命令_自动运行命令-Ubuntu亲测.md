 

#### \[Linux\]: 开机自启动命令


很多时候需要Ubuntu在开机的时候执行一些指定的命令，这里对操作方法进行记录。

1.  在 /etc/init.d/ 中创建自己的开机运行脚本

```shell
# 这里的文件名 mystart 可以修改为任何你喜欢的名称，但是必须放在/etc/init.d/目录中
cd /etc/init.d
sudo vim /etc/init.d/mystart.sh
#sudo nano /etc/init.d/mystart.sh   #也行
```

2.  写入需要执行的命令,

```shell
#!/bin/bash
### BEGIN INIT INFO
# Provides:          tuzixini
# Required-Start:    $local_fs $network
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: self define auto start
# Description:       self define auto start
### END INIT INFO
# 上面的部分也必须写上，后面放上你需要开机执行的命令，这里是挂载一个硬盘
sudo mount /dev/sdb1 /opt/disk

```

3.  修改脚本文件权限(将命令中的mystart.sh替换成实际的脚本文件名称)

```shell
sudo chmod 755 /etc/init.d/mystart.sh
```

4.  加入开机启动(将命令中的mystart.sh替换成实际的脚本文件名称)

```shell
sudo update-rc.d mystart.sh defaults 90
```

5.  移除ubuntu脚本

```shell
cd /etc/init.d
sudo update-rc.d -f start_test.sh remove
```

6.  服务的启动与停止

```shell
sudo service --status-all
```

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[CS入门技能树](https://edu.csdn.net/skill/gml/gml-107df6e5ed9b4bef8b035e0649b2449e?utm_source=csdn_ai_skill_tree_blog)[Linux进阶](https://edu.csdn.net/skill/gml/gml-107df6e5ed9b4bef8b035e0649b2449e?utm_source=csdn_ai_skill_tree_blog)[新增用户](https://edu.csdn.net/skill/gml/gml-107df6e5ed9b4bef8b035e0649b2449e?utm_source=csdn_ai_skill_tree_blog)36974 人正在系统学习中

本文转自 <https://blog.csdn.net/qq_41897558/article/details/120084797>，如有侵权，请联系删除。