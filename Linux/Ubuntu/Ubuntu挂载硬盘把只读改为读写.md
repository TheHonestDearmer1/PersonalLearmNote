 

打开控制台，输入mount会出现一堆东西，找到想要改的硬盘得到路径，比如我的是/dev/sdb1

再输入

sudo mount -o rw,remount /dev/sdb1

输入密码解决root问题。

最后输入mount看一下硬盘括号后的读写情况是否变为rw。

如果变为rw就完事了。

本文转自 <https://blog.csdn.net/webmater2320/article/details/114397962>，如有侵权，请联系删除。