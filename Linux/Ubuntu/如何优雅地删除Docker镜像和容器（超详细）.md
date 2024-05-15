 

### 一、前言


  大家是怎么删除Docker中的镜像和容器的呢，有没有考虑过如何优雅地删除呢？**本教程详细指导如何在优雅地删除Docker容器和镜像**。如需了解如何在Centos7系统里面安装Docker，可以参考教程【[最新Docker在Centos7下安装部署（参考官方教程文档）](https://blog.csdn.net/u014282578/article/details/127767385)】  

  **`本文由 @大白有点菜 原创，请勿盗用，转载请说明出处！如果觉得文章还不错，请点点赞，加关注，谢谢！`**  


### 二、优雅[删除镜像](https://so.csdn.net/so/search?q=%E5%88%A0%E9%99%A4%E9%95%9C%E5%83%8F&spm=1001.2101.3001.7020)（`推荐做法`）

##### 1、查看Docker要删除的镜像，如目标版本为`stable-perl`的`Nginx`，镜像ID（`IMAGE ID`）为 `df1998569adb`。

```shell
docker images
```

![查看Docker要删除的镜像](https://img-blog.csdnimg.cn/ea0a86e937704cdc830e91eda0d1fad9.png)

##### 2、使用命令“`docker rmi 镜像ID`”删除Nginx（stable-perl）的镜像，只取“`IMAGE ID`”的`前3个字符`即可。

```shell
docker rmi df1
```

![使用命令“docker rmi 镜像ID(IMAGE ID)”删除指定的镜像](https://img-blog.csdnimg.cn/ed8aeb95262948218f50a3ad99789a7a.png)   
  **报错内容如下，意思是`镜像（df1）`存在使用中的`容器（f66）`，不能强制删除镜像。官方的意思是要先停止容器运行，再进行镜像的删除操作吗？**

```shell
Error response from daemon: conflict: unable to delete df1998569adb (cannot be forced) - image is being used by running container f6678f2821c7
```

##### 3、查看Docker运行中的容器，如容器 `nginx:stable-perl` ，容器ID为 `f66`。

```shell
docker ps
```

![查看Docker运行中的容器](https://img-blog.csdnimg.cn/74235673069647708da131bd14102d1e.png)  


##### 4、先停止`nginx:stable-perl容器（f66）`运行，再去删除`Nginx（stable-perl）镜像（df1）`。

（1）停止容器（f66）运行。

```shell
docker stop f66
```

（1）删除容器（f66）运行。

```
sudo docker rm f66
```

（3）删除镜像（df1）。

```shell
docker rmi df1
```

![停止容器（f66）运行，再去删除镜像（df1）](https://img-blog.csdnimg.cn/016edef2c1834664b47114cc55505fce.png)   
  **What？都已经停止`容器（f66）`运行了，删除`镜像（df1）`怎么还报错啊！？其实，只停止容器的正常运行还不行，还有最重要的一步没做：`删除容器`。**

```shell
Error response from daemon: conflict: unable to delete df1998569adb (must be forced) - image is being used by stopped container f6678f2821c7
```

##### 5、查看Docker所有容器的状态（`包含运行中的和已停止的`），“STATUS”为“Exited(0)”代表停止运行。执行[删除容器](https://so.csdn.net/so/search?q=%E5%88%A0%E9%99%A4%E5%AE%B9%E5%99%A8&spm=1001.2101.3001.7020)命令“`docker rm f66`”，删除 nginx:stable-perl 容器，再查看 nginx:stable-perl 容器是否还在列表中。

（1）查看Docker所有容器的状态。

```shell
docker ps -a
```

（2）删除 nginx:stable-perl 容器。

```shell
docker rm f66
```

（3）再查看Docker所有容器的状态，发现 nginx:stable-perl `容器（f66）`已经不存在了。

```shell
docker ps -a
```

![查看Docker所有容器的状态并删除容器](https://img-blog.csdnimg.cn/6573ecfd4fba49df848207d12fdfb144.png)  


要查找已经停止的 Docker 容器，您可以使用以下命令：

```
sudo docker ps -a
```



该命令将显示所有的容器（包括正在运行和已经停止的容器）。如果容器的状态为 “Exited”，则表示该容器已经停止。

您可以根据容器的 ID 或名称来找到您感兴趣的容器。如果您希望只显示已经停止的容器，可以使用以下命令过滤结果：

```
sudo docker ps -a --filter "status=exited"
```



这将只显示已经停止的容器。请注意，使用此命令时不要忘记添加 `sudo` 前缀以获得 root 权限。

要进入 Docker 容器的 shell 中，请使用以下命令：

```
sudo docker exec -it <容器名称或ID> /bin/bash
```



该命令将启动一个新的 bash shell，并将其连接到正在运行的 Docker 容器中。您可以在此 shell 中执行任何命令，就像您在本地计算机的 shell 中一样。

请注意要在命令中替换 `<容器名称或ID>` 为您要进入的 Docker 容器的名称或 ID。如果您不确定要进入哪个容器，请运行 `docker ps` 命令以查看所有正在运行的容器列表。

另外，一些 Docker 镜像可能不包含 `/bin/bash` shell，这种情况下您可以尝试使用 `/bin/sh` 或其他默认 shell，请先查看 Docker 镜像的文档以了解支持的默认 shell。

希望这可以帮助您进入到 Docker 容器中！


### 五、总结

  **优雅地`删除镜像`的最佳做法是：`先停止容器，再删除容器，最后删除镜像`。**  

  **优雅地`删除容器`的最佳做法是：`先停止容器，再删除容器`。**

