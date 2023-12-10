**注意：以下命令是有可能导致系统重启后 进入黑屏状态的。如果你对Linux系统不熟悉不建议操作。**

**操作导致重启黑屏，不会导致数据丢失。只是Linux 启动项失败。从另外的电脑 ssh 到这个机器，是可以连上的。所以操作配置，强烈建议 配置好 ssh ，可以从别的机器进行配置恢复（**sudo systemctl set-default graphical.target**）**  
\----------------------

ubuntu 可以设置默认不进入图形界面，20.04 上测试验证成功

```text
sudo systemctl set-default multi-user.target
```

重启后会直接进入控制台，如果想从控制台进入图形界面

```text
sudo systemctl start gdm3.service
```

恢复默认开机启动图形界面

```text
sudo systemctl set-default graphical.target
```

在一些情况以下会导致无法进入系统，处于黑屏状态。这时候可以按 ctrl+alt+f1 可以进入一个控制台。或安 alt + 左 或右 方向键 切换控制台。

再执行

```text
sudo systemctl start gdm3.service 
```

可以进入桌面。

这种情况是 设置默认进入控制台失败了。原因可能和内核版本有关。

可以恢复默认开机启动图形界面

```text
sudo systemctl set-default graphical.target
```

本文转自 <https://zhuanlan.zhihu.com/p/344347732>，如有侵权，请联系删除。