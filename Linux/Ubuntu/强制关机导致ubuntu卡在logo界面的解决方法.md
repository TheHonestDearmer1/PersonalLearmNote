 

最近一直因为各种问题重装[ubuntu](https://so.csdn.net/so/search?q=ubuntu&spm=1001.2101.3001.7020)系统。不得不说，win10系统的稳定性还是值得一赞的，大部分问题都可以通过重启解决。然而，ubuntu可不能随便重启。

造成ubuntu卡在logo界面的极大可能性就是：**文件受损**。fsck如果校对不上文件，就会一直悬挂，从而导致开机卡在logo那五个点。

那么首先需要弄清楚你受损的文件是什么。

1\. 在logo处按ctrl+alt+.重启系统；

2\. 在进入logo前，按esc进入高级模式，然后选择进入recovery模式；

3\. 选择root， 在命令行里输入：

```bash
sudo fsck -f /
```

这样你就可以看到是什么文件受损了。如果不是很重要的话，在root下删除那个文件就可以了。

我遇到的问题就是，anaconda文件夹有个.so文件有问题，我就将整个anaconda目录删除。reboot之后就能进系统了。

本文转自 <https://blog.csdn.net/leviopku/article/details/100094920>，如有侵权，请联系删除。