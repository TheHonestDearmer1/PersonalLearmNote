 

#### 1 执行以下命令更新系统库和依赖

```
	sudo rm /var/lib/apt/lists/lock
	sudo rm /var/lib/dpkg/lock
	sudo rm /var/lib/dpkg/lock-frontend
	sudo dpkg --configure -a
	sudo apt clean
	sudo apt update --fix-missing
	sudo apt install -f
	sudo dpkg --configure -a
	sudo apt upgrade
	sudo apt dist-upgrade
```

> 这样会重置系统相关设置和损坏的配置，但有大部分完好的程序和自动启动项会保留

#### 2 重启

`sudo reboot`

#### 3 如果使用 nvidia 驱动，需要手动重装一遍才能登录桌面

[安装CUDA及nvidia驱动官方教程](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)

本文转自 <https://blog.csdn.net/wmx843230304wmx/article/details/91962396>，如有侵权，请联系删除。