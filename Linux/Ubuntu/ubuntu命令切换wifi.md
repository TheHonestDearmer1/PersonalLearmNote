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

查看网络适配器情况：

```
nmcli connection show
```

```
sumengxian@sumengxian-VALLEYVIEW-C0-PLATFORM:~$ nmcli connection show
NAME        UUID                                  TYPE    DEVICE
306_5       44d9ae93-017d-49f3-9e3f-bd99cbc986b7  wifi    wlx502b7310e607
docker0     2996f2ad-efd5-434c-a022-ef6b8f428115  bridge  docker0
zt2lruazkn  2b522dc4-7ac5-452a-9918-6be1e3946903  tun     zt2lruazkn
306         061b425c-cc2a-4173-b5c3-b4f4b963f42d  wifi    --
Mi 10       8a8fd8f8-26cf-4cf5-835a-a326ef61f8e6  wifi    --
```

关闭指定适配器连接：

要在终端中断开特定的 WiFi 连接，您可以使用以下命令：

```
sudo nmcli dev disconnect ifname wlan0
```

请将 “wlan0” 替换为您当前正在使用的网络接口名称。这条命令会断开当前网络连接。