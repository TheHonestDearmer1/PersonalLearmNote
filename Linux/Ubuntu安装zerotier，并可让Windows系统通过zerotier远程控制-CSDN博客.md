 

### 需要注意的一点是，[ubuntu](https://so.csdn.net/so/search?q=ubuntu&spm=1001.2101.3001.7020)一定要确保配置了ssh。

### 0.Ubuntu配置SSH。

[ubuntu 安装ssh](https://segmentfault.com/a/1190000022103074)

```
sudo apt install openssh-server
```

验证安装是否成功并且SSH服务正在运行。

```
sudo systemctl status ssh
```

_这一步我忘了自己当时怎么操作的了，就在网上找了一个，但是没有验证。_

### 1.Ubuntu安装zerotier

```
curl -s https://install.zerotier.com | sudo bash
```

### 2.Ubuntu加入zerotier局域网

```
sudo zerotier-cli join 你的network ID
```

### 3.登入zerotier官网，进入你的局域网，在Ubuntu前面打勾，授权

> 可以将网络设置为公开就不用次次点进去了

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210118192406193.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTI0MjgxNjk=,size_16,color_FFFFFF,t_70)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210118192316666.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTI0MjgxNjk=,size_16,color_FFFFFF,t_70)

### 设备连不上的问题

通过贴吧的帮助，得知目前zerotier在IPV6的网络下能够ONLINE，在IPV4下就是OFFLINE，最后检查校园网发现校园网不支持IPV6（打开网页即可检测），随后打开手机热点（设置为IPV6：手机设置–更多–移动网络–接入点名称(APN)–进去找到APN协议–设置为ipv6），电脑连接热点，等待几分钟直到ONLINE，即可连接服务器

### 4.Ubuntu安装xrdp远程桌面

官网上下载[xrdp](http://www.c-nergy.be/products.html)  
设置脚本的可执行权限

```
$chmod +x ~/Downloads/xrdp-install-1.2.sh
```

`~/Downloads/xrdp-install-1.2.sh`是下载路径。其实也可以直接在授权前转入到下载路径下

```
$cd Downloads
$chmod +x xrdp-install-1.2.sh
```

以普通身份运行脚本

```
$./xrdp-install-1.2.sh 	
```

### 5.安装后重启Ubuntu，并从Windows远程登陆。重启Ubuntu后不要登陆Ubuntu。

第4步和第5步的详细步骤可以看这篇[Ubuntu18.04.4 安装XRDP远程桌面终极、最简方案](https://blog.csdn.net/weixin_43315707/article/details/107518380)。

如果你之前安装的xrdp有问题要卸载，或者单纯只是想卸载xrdp，可以看这篇  
[xrdp登录失败，最终卸载xrdp，重新安装解决](https://blog.csdn.net/gx262091291/article/details/71774482)。  
在windows系统中按住windows键和字母R弹出运行窗口。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/84b642ed28b44167bad13b0af0582785.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6LW35ZCN5a2X5LuA5LmI55qE5aW96Zq-,size_14,color_FFFFFF,t_70,g_se,x_16)  
输入mstsc，点击确定，或者直接按enter键。弹出远程连接窗口。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/53b81bed51254392844ed2e5f4937e25.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6LW35ZCN5a2X5LuA5LmI55qE5aW96Zq-,size_20,color_FFFFFF,t_70,g_se,x_16)  
点击连接  
![在这里插入图片描述](https://img-blog.csdnimg.cn/19e179fb3fe04ec7a1dc23942206c190.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6LW35ZCN5a2X5LuA5LmI55qE5aW96Zq-,size_20,color_FFFFFF,t_70,g_se,x_16)  
选择是，进入xrdp桌面。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/4c30732c5d5e49689d4513b55df85420.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6LW35ZCN5a2X5LuA5LmI55qE5aW96Zq-,size_20,color_FFFFFF,t_70,g_se,x_16)  
输入用户名和密码（登录Ubuntu电脑的用户名和密码）就可以进入Ubuntu桌面了。![在这里插入图片描述](https://img-blog.csdnimg.cn/5974ab09d8de4382a656a991e1d5bdff.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6LW35ZCN5a2X5LuA5LmI55qE5aW96Zq-,size_20,color_FFFFFF,t_70,g_se,x_16)

本文转自 <https://blog.csdn.net/u012428169/article/details/112792773>，如有侵权，请联系删除。