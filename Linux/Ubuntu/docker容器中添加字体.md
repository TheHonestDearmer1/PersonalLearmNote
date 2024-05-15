在腾讯云服务器中使用docker部署的Java后端服务，需要解决字体问题，解决方法如下：

1、从windows中拷贝字体文件，目录位置：C:\\Windows\\Fonts

2、将字体文件拷贝到宿主机，比方说我拷贝到了：/usr/local/share/fonts/目录下

3、在宿主机执行cp命令，将字体文件拷贝到容器中的对应位置 /usr/share/fonts/

```text
docker cp /usr/local/share/fonts/simsun.ttc rongqi:/usr/share/fonts/
```

4、进入容器，验证字体是否安装成功

```text
docker exec -it rongqi bash
```

验证字体是否安装成功使用命令fc-list，如果没有fc-list命令，需要做如下操作：

**Debian/Ubuntu:**

```text
apt-get update
apt-get install fontconfig
```

**CentOS/RHEL:**

```text
yum install fontconfig
```

**Alpine Linux:**

```text
apk update
apk add fontconfig
```

**确认字体目录：**

确保你的字体文件已经正确复制到容器内的 `/usr/share/fonts/` 目录。

**生成字体缓存：**

在容器内执行以下命令，以确保字体缓存已生成。

```text
fc-cache -fv
```

**验证字体：**

在容器内执行 `fc-list` 命令，查看是否能够列出已安装的字体

```text
fc-list
```

验证成功如下图所示

<img src="https://pic1.zhimg.com/v2-4d9625a6b85485ec8e6a9f46647db770\_b.jpg" data-caption="" data-size="normal" data-rawwidth="708" data-rawheight="96" class="origin\_image zh-lightbox-thumb" width="708" data-original="https://pic1.zhimg.com/v2-4d9625a6b85485ec8e6a9f46647db770\_r.jpg"/>

![](https://pic1.zhimg.com/80/v2-4d9625a6b85485ec8e6a9f46647db770_720w.webp)

本文转自 <https://zhuanlan.zhihu.com/p/649666094>，如有侵权，请联系删除。