扫描指令：

```
nmcli device wifi list
```

![](https://pic3.zhimg.com/80/v2-0850fef222aac6d28b34ce85da079172_1440w.webp)

切换指令：[ubuntu命令连接wifi\_要不要买菜！的博客-CSDN博客\_ubuntu命令行连接wifi](https://link.zhihu.com/?target=https%3A//blog.csdn.net/qq_38312843/article/details/124054055)

```text
sudo nmcli device wifi connect "pang" password "123456789"
```

如果已经连接过的wifi就直接切换就行了

```
sudo nmcli device wifi connect "pang"
```

device不能写成dev,否则多张网卡的时候读不到