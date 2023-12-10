 

### [ubuntu](https://so.csdn.net/so/search?q=ubuntu&spm=1001.2101.3001.7020)下route命令详解

1、显示路由表

    route -n


2、临时路由设置，重启网卡失效

    #添加一条路由(发往192.168.62这个网段的全部要经过网关192.168.1.1)
    route add -net 192.168.62.0 netmask 255.255.255.0 gw 192.168.1.1
    
    #删除一条路由　删除的时候不用写网关
    route del -net 192.168.122.0 netmask 255.255.255.0

 


```
使用 “route” 命令：

route -n
在输出结果中，找到标记为 “UG”（默认网关）的目标，对应的网关地址就是您的默认网关。

使用 “ip” 命令：

ip route show default
这会显示默认网关的详细信息，包括网关地址以及与之相关联的网络接口。
```

切换默认网卡路由，首先使用route查看路由表，再用ifconfig查看到对应的ip地址

```
sumengxian@sumengxian-VALLEYVIEW-C0-PLATFORM:~$ route
内核 IP 路由表
目标            网关            子网掩码        标志  跃点   引用  使用 接口
default         B70.lan         0.0.0.0         UG    600    0        0 wlx28f3662f4845
default         B70.lan         0.0.0.0         UG    601    0        0 wlx502b7310e607
10.147.17.0     0.0.0.0         255.255.255.0   U     0      0        0 zt2lruazkn
link-local      0.0.0.0         255.255.0.0     U     1000   0        0 wlx28f3662f4845
172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 docker0
192.168.123.0   0.0.0.0         255.255.255.0   U     600    0        0 wlx28f3662f4845
192.168.123.0   0.0.0.0         255.255.255.0   U     601    0        0 wlx502b7310e607
想要将wlx502b7310e607设为默认路由
sumengxian@sumengxian-VALLEYVIEW-C0-PLATFORM:~$ ifconfig

wlx28f3662f4845: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.123.115  netmask 255.255.255.0  broadcast 192.168.123.255
        inet6 fe80::3de6:4626:a9d2:10cd  prefixlen 64  scopeid 0x20<link>
        ether 28:f3:66:2f:48:45  txqueuelen 1000  (以太网)
        RX packets 968737  bytes 1443404687 (1.4 GB)
        RX errors 0  dropped 79759  overruns 0  frame 0
        TX packets 549596  bytes 59288228 (59.2 MB)
        TX errors 0  dropped 52 overruns 0  carrier 0  collisions 0

怎么设置默认走的网络
```

解决方法：

要设置默认走的网络，您需要使用"route"命令将默认路由设置为您要使用的网络接口。根据您提供的信息，看起来您想要将默认路由设置为网络接口"wlx502b7310e607"。

请在命令行中执行以下命令：

```
sudo route del default gw B70.lan dev wlx28f3662f4845
```

这将从现有的默认路由删除,同时del改成add就是添加

```
sudo route add default gw B70.lan dev wlx28f3662f4845
```



    #添加到主机的路由，删除将add换成del
    # route add –host 192.168.168.110 dev eth0
    # route add –host 192.168.168.119 gw 192.168.168.1
    
    #添加到网络的路由
    # route add –net IP netmask MASK eth0
    # route add –net IP netmask MASK gw IP
    # route add –net IP/24 eth1
    
    #添加默认网关
    # route add default gw IP
    
    #删除路由
    # route del –host 192.168.168.110 dev eth0
    
    #修改路由
    route change 192.168.3.98 netmask 255.255.255.0 192.168.3.45   #将目的ip为192.168.3.98且子网掩码为255.255.255.0的下一跳由x.x.x.x改为192.168.3.45


​    
