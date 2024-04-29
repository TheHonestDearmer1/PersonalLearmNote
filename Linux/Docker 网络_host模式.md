本文转自[https://www.freeaihub.com/article/host-module-in-docker-network.html](https://www.freeaihub.com/article/host-module-in-docker-network.html),该页可在线运行
--------------------------------------------------------------------------------------------------------------------------------------------------------

![docker网络](https://freeaihub.com/article/images/docker-network.jpg)

当我们准备将Docker技术应用到生产级别的场景时，我们需要了解很多网络方面的知识。网络是Docker中相对比较薄弱的部分，我们有必要了解Docker的网络知识，以满足更高的网络需求。本节先对Docker网络模型中的host模型进行理论介绍，再通过案例的实操，让您更好地去理解docker网络模型。

Docker网络
--------

当你安装完Docker时，它会自动创建三个网络。你可以使用以下`docker network ls`命令列出这些网络：

```bash
docker network ls
```

结果应如下

```sql
NETWORK ID          NAME                DRIVER              SCOPE
594430d2d4bb        bridge              bridge              local
d855b34c5d51        host                host                local
b1ecee29ed5e        none                null                local
```

Docker内置这三个网络，运行容器时，你可以使用该来指定容器应连接到哪些网络。

我们在使用docker run创建Docker容器时，可以用`--network`标志 选项指定容器的网络模式，Docker有以下4种网络模式：

host模式：使用 --net=host 指定。

none模式：使用 --net=none 指定。

bridge模式：使用 --net=bridge 指定，默认设置。

container模式：使用 --net=container:NAME\_or\_ID 指定。

host模式
------

Docker使用了Linux的Namespaces技术来进行资源隔离，如PID Namespace隔离进程，Mount Namespace隔离文件系统，Network Namespace隔离网络等。一个Network Namespace提供了一份独立的网络环境，包括网卡、路由、Iptable规则等都与其他的Network Namespace隔离。

host模式类似于Vmware的桥接模式，与宿主机在同一个网络中，但没有独立IP地址。一个Docker容器一般会分配一个独立的Network Namespace。但如果启动容器的时候使用host模式，那么这个容器将不会获得一个独立的Network Namespace，而是和宿主机共用一个Network Namespace。容器将不会虚拟出自己的网卡，配置自己的IP等，而是使用宿主机的IP和端口。

如下图所示：容器与主机在相同的网络命名空间下面，使用相同的网络协议栈，容器可以直接使用主机的所有网络接口

![docker-host](https://freeaihub.com/article/images/docker-host.jpg)

案例验证
----

查看主机链路接口

```bash
ip a
```

我们右侧云环境主机的IP为`{host0.ip}/24`上用host模式启动nginx容器，监听它的tcp80端口。

使用`--net host`参数来指定网络模型使用host模式

```bash
docker run --name=nginx --net=host -p 80:80 -d nginx
```

查看容器链路接口，与主机一致

```bash
docker exec -it nginx cat /etc/hosts
```

这时外界要访问容器中的应用，则直接使用`{host0.ip}:80`即可，不用任何NAT转换，就像直接跑在宿主机中一样。但是，容器的其他方面，如文件系统、进程列表等还是和宿主机隔离的。

```bash
curl {host0.ip}
```

总结
--

host 模式简单并且性能高，host 模式下面的网络模型是最简单和最低延迟的模式，容器进程直接与主机网络接口通信，与物理机性能一致，host 不利于网络自定配置和管理，并且所有主机的容器使用相同的IP。也不利于主机资源的利用。对网络性能要求比较高，可以使用该模式。否则应该使用其他模式

本文转自 <https://www.cnblogs.com/freeaihub/p/13197292.html#Host%E6%A8%A1%E5%BC%8F>，如有侵权，请联系删除。