你[是否正在使用基于 Ubuntu 的系统，然后发现无法连接网络](https://link.zhihu.com/?target=https%3A//itsfoss.com/fix-no-wireless-network-ubuntu/)？你一定会很惊讶，很多的问题都可以简单地通过重启服务解决。

在这篇文章中，我会介绍在 Ubuntu 或者其他 Linux 发行版中重启网络的几种方法，你可以根据自身需要选择对应的方法。这些方法基本分为两类：

**通过命令行方式重启网络**
---------------

如果你使用的 Ubuntu 服务器版，那么你已经在使用命令行终端了。如果你使用的是桌面版，那么你可以通过快捷键 `Ctrl+Alt+T` [Ubuntu 键盘快捷键](https://link.zhihu.com/?target=https%3A//itsfoss.com/ubuntu-shortcuts/) 打开命令行终端。

在 Ubuntu 中，有多个命令可以重启网络。这些命令，一部分或者说大部分，也适用于在 Debian 或者其他的 Linux 发行版中重启网络。

`1、network manager 服务`
----------------------

这是通过命令行方式重启网络最简单的方法。它相当于是通过图形化界面重启网络（重启 Network-Manager 服务）。

```text
sudo service network-manager restart
```

此时，网络图标会消失一会儿然后重新显示。

`2、systemd`
-----------

`service` 命令仅仅是这个方式的一个封装（同样的也是 init.d 系列脚本和 Upstart 相关命令的封装）。`systemctl` 命令的功能远多于 `service` 命令。通常我更喜欢使用这个命令。

```text
sudo systemctl restart NetworkManager.service
```

这时，网络图标又会消失一会儿。 如果你想了解 `systemctl` 的其他选项, 可以参考 man 帮助文档。

`3、nmcli`
---------

这是 Linux 上可以管理网络的另一个工具。这是一个功能强大而且实用的工具。很多系统管理员都喜欢使用该工具，因为它非常容易使用。

这种方法有两个操作步骤：关闭网络，再开启网络。

```text
sudo nmcli networking off
```

这样就会关闭网络，网络图标会消失。接下来，再开启网络：

```text
sudo nmcli networking on
```

你可以通过 man 帮助文档了解 nmcli 的更多用法。

`4、ifup & ifdown`
-----------------

这两个命令直接操作网口，切换网口是否可以收发包的状态。这是 [Linux 中最应该了解的网络命令](https://link.zhihu.com/?target=https%3A//itsfoss.com/basic-linux-networking-commands/) 之一。

使用 `ifdown` 关闭所有网口，再使用 `ifup` 重新启用网口。

通常推荐的做法是将这两个命令一起使用。

```text
sudo ifdown -a && sudo ifup -a
```

注意：这种方法不会让网络图标从系统托盘中消失，另外，各种网络连接也会断。

`补充工具： nmtui`
-------------

这是系统管理员们常用的另外一种方法。它是在命令行终端中管理网络的文本菜单工具。

```text
nmtui
```

打开如下菜单：

  

<img src="https://pic4.zhimg.com/v2-52d19fba2f9d9f1ce542b165cac0f7ff\_b.png" data-size="normal" data-rawwidth="800" data-rawheight="602" class="origin\_image zh-lightbox-thumb" width="800" data-original="https://pic4.zhimg.com/v2-52d19fba2f9d9f1ce542b165cac0f7ff\_r.jpg"/>

![](https://pic4.zhimg.com/80/v2-52d19fba2f9d9f1ce542b165cac0f7ff_720w.webp)

nmtui Menu

  

注意：在 nmtui 中，可以通过 `up` 和 `down` 方向键选择选项。

选择 “Activate a connection”：

  

<img src="https://pic1.zhimg.com/v2-60b90ea950037057e24278606695cb90\_b.png" data-size="normal" data-rawwidth="799" data-rawheight="579" class="origin\_image zh-lightbox-thumb" width="799" data-original="https://pic1.zhimg.com/v2-60b90ea950037057e24278606695cb90\_r.jpg"/>

![](https://pic1.zhimg.com/80/v2-60b90ea950037057e24278606695cb90_720w.webp)

nmtui Menu Select &quot;Activate a connection&quot;

  

按下回车键，打开 “connections” 菜单。

  

<img src="https://pic1.zhimg.com/v2-74cb9b9460c818dec51ce55c96c565d0\_b.png" data-size="normal" data-rawwidth="800" data-rawheight="585" class="origin\_image zh-lightbox-thumb" width="800" data-original="https://pic1.zhimg.com/v2-74cb9b9460c818dec51ce55c96c565d0\_r.jpg"/>

![](https://pic1.zhimg.com/80/v2-74cb9b9460c818dec51ce55c96c565d0_720w.webp)

nmtui Connections Menu

  

接下来，选择前面带星号（\*）的网络。在这个例子中，就是 MGEO72。

  

<img src="https://pic4.zhimg.com/v2-96e9623fe7557b787cecc358507a8dab\_b.png" data-size="normal" data-rawwidth="800" data-rawheight="576" class="origin\_image zh-lightbox-thumb" width="800" data-original="https://pic4.zhimg.com/v2-96e9623fe7557b787cecc358507a8dab\_r.jpg"/>

![](https://pic4.zhimg.com/80/v2-96e9623fe7557b787cecc358507a8dab_720w.webp)

Select your connection in the nmtui connections menu.

  

按下回车键。 这就将“停用”你的网络连接。

  

<img src="https://pic2.zhimg.com/v2-7275ed8c2382caa9523d9577f21cff25\_b.png" data-size="normal" data-rawwidth="800" data-rawheight="572" class="origin\_image zh-lightbox-thumb" width="800" data-original="https://pic2.zhimg.com/v2-7275ed8c2382caa9523d9577f21cff25\_r.jpg"/>

![](https://pic2.zhimg.com/80/v2-7275ed8c2382caa9523d9577f21cff25_720w.webp)

nmtui Connections Menu with no active connection

  

选择你要连接的网络：

  

<img src="https://pic1.zhimg.com/v2-f3910c1fd5843d4f5109b80f9ad14378\_b.png" data-size="normal" data-rawwidth="800" data-rawheight="566" class="origin\_image zh-lightbox-thumb" width="800" data-original="https://pic1.zhimg.com/v2-f3910c1fd5843d4f5109b80f9ad14378\_r.jpg"/>

![](https://pic1.zhimg.com/80/v2-f3910c1fd5843d4f5109b80f9ad14378_720w.webp)

Select the connection you want in the nmtui connections menu.

  

按下回车键。这样就重新激活了所选择的网络连接。

  

<img src="https://pic1.zhimg.com/v2-74cb9b9460c818dec51ce55c96c565d0\_b.png" data-size="normal" data-rawwidth="800" data-rawheight="585" class="origin\_image zh-lightbox-thumb" width="800" data-original="https://pic1.zhimg.com/v2-74cb9b9460c818dec51ce55c96c565d0\_r.jpg"/>

![](https://pic1.zhimg.com/80/v2-74cb9b9460c818dec51ce55c96c565d0_720w.webp)

nmtui Connections Menu

  

按下 `Tab` 键两次，选择 “Back”：

  

<img src="https://pic1.zhimg.com/v2-27acc5d6e9eda36cad525b73aa15d8c8\_b.png" data-size="normal" data-rawwidth="800" data-rawheight="585" class="origin\_image zh-lightbox-thumb" width="800" data-original="https://pic1.zhimg.com/v2-27acc5d6e9eda36cad525b73aa15d8c8\_r.jpg"/>

![](https://pic1.zhimg.com/80/v2-27acc5d6e9eda36cad525b73aa15d8c8_720w.webp)

Select &quot;Back&quot; in the nmtui connections menu.

  

按下回车键，回到 nmtui 的主菜单。

  

<img src="https://pic1.zhimg.com/v2-60b90ea950037057e24278606695cb90\_b.png" data-size="normal" data-rawwidth="799" data-rawheight="579" class="origin\_image zh-lightbox-thumb" width="799" data-original="https://pic1.zhimg.com/v2-60b90ea950037057e24278606695cb90\_r.jpg"/>

![](https://pic1.zhimg.com/80/v2-60b90ea950037057e24278606695cb90_720w.webp)

nmtui Main Menu

  

选择 “Quit” ：

  

<img src="https://pic1.zhimg.com/v2-710c6cad6da298fb38c29e5d2ec62648\_b.png" data-size="normal" data-rawwidth="800" data-rawheight="580" class="origin\_image zh-lightbox-thumb" width="800" data-original="https://pic1.zhimg.com/v2-710c6cad6da298fb38c29e5d2ec62648\_r.jpg"/>

![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='800' height='580'></svg>)

nmtui Quit Main Menu

  

退出该界面，返回到命令行终端。

就这样，你已经成功重启网络了。

**通过图形化界面重启网络**
---------------

显然，这是 Ubuntu 桌面版用户重启网络最简单的方法。如果这个方法不生效，你可以尝试使用前文提到的命令行方式重启网络。

NM 小程序是 [NetworkManager](https://link.zhihu.com/?target=https%3A//wiki.gnome.org/Projects/NetworkManager) 的系统托盘程序标志。我们将使用它来重启网络。

首先，查看顶部状态栏。你会在系统托盘找到一个网络图标 （因为我使用 Wi-Fi，所以这里是一个 Wi-Fi 图标）。

接下来，点击该图标（也可以点击音量图标或电池图标）。打开菜单。选择 “Turn Off” 关闭网络。

  

<img src="https://pic4.zhimg.com/v2-52edcdce835486c687d95ba40c05cb7b\_b.jpg" data-size="normal" data-rawwidth="800" data-rawheight="400" class="origin\_image zh-lightbox-thumb" width="800" data-original="https://pic4.zhimg.com/v2-52edcdce835486c687d95ba40c05cb7b\_r.jpg"/>

![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='800' height='400'></svg>)

Restart network in Ubuntu

  

网络图标会在状态栏中消失，这表示你已经成功关闭网络了。

再次点击系统托盘重新打开菜单，选择 “Turn On”，重新开启网络。

  

<img src="https://pic1.zhimg.com/v2-9334ec33a8aa059219b72ca5e48ef958\_b.jpg" data-size="normal" data-rawwidth="800" data-rawheight="400" class="origin\_image zh-lightbox-thumb" width="800" data-original="https://pic1.zhimg.com/v2-9334ec33a8aa059219b72ca5e48ef958\_r.jpg"/>

![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='800' height='400'></svg>)

Restarting network in Ubuntu

  

恭喜！你现在已经重启你的网络了。

`其他提示：刷新可用网络列表`
---------------

如果你已经连接上一个网络，但是你想连接到另外一个网络，你如何刷新 WiFi 列表，查找其他可用的网络呢？我来向你展示一下。

Ubuntu 没有可以直接 “刷新 WiFi 网络” 的选项，它有点隐蔽。

你需要再次打开配置菜单，然后点击 “Select Network” 。

  

<img src="https://pic1.zhimg.com/v2-03d99858d286bee09e4152aa280ef114\_b.jpg" data-size="normal" data-rawwidth="800" data-rawheight="400" class="origin\_image zh-lightbox-thumb" width="800" data-original="https://pic1.zhimg.com/v2-03d99858d286bee09e4152aa280ef114\_r.jpg"/>

![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='800' height='400'></svg>)

Refresh wifi network list in Ubuntu

  

选择对应的网络修改你的 WiFi 连接。

你无法马上看到可用的无线网络列表。打开网络列表之后，大概需要 5 秒才会显示其它可用的无线网络。

  

<img src="https://pic3.zhimg.com/v2-2bb0f04d7c1c41138795ada72b89a82a\_b.jpg" data-size="normal" data-rawwidth="800" data-rawheight="400" class="origin\_image zh-lightbox-thumb" width="800" data-original="https://pic3.zhimg.com/v2-2bb0f04d7c1c41138795ada72b89a82a\_r.jpg"/>

![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='800' height='400'></svg>)

Select another wifi network in Ubuntu

  

等待大概 5 秒钟，看到其他可用的网络。

现在，你就可以选择你想要连接的网络，点击连接。这样就完成了。

**总结**
------

重启网络连接是每个 Linux 用户在使用过程中必须经历的事情。

我们希望这些方法可以帮助你处理这样的问题！

你是如何重启或管理你的网络的？我们是否还有遗漏的？请在下方留言。

* * *

via: [https://itsfoss.com/restart-network-ubuntu](https://link.zhihu.com/?target=https%3A//itsfoss.com/restart-network-ubuntu)

作者：[Sergiu](https://link.zhihu.com/?target=https%3A//itsfoss.com/author/sergiu/) 选题：[lujun9972](https://link.zhihu.com/?target=https%3A//github.com/lujun9972) 译者：[bodhix](https://link.zhihu.com/?target=https%3A//github.com/bodhix) 校对：[wxy](https://link.zhihu.com/?target=https%3A//github.com/wxy)

本文由 [LCTT](https://link.zhihu.com/?target=https%3A//github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://link.zhihu.com/?target=https%3A//linux.cn/) 荣誉推出

本文转自 <https://zhuanlan.zhihu.com/p/64456541>，如有侵权，请联系删除。