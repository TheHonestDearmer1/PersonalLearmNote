# 在Ubuntu使用802.11ac USB 无线wifi接收器

```shell
sudo apt update
sudo apt install build-essential git dkms
git clone https://github.com/brektrou/rtl8821CU.git
cd rtl8821CU
make
sudo make install
#装载到内核
sudo modprobe 8821cu
#查看usb设备列表
lsusb

reboot 
```

通过lsusb命令返回的设备ID   0bda：a192 

因为这个网卡是带储存的，系统没有将这个设备识别成网卡，而是当成了USB存储。

现在需要执行usb\_modeswitch命令切换设备模式：

```bash
sudo usb_modeswitch -KW -v 0bda -p a192 lsusb
```

已经能够正常识别为网卡了。

但是在重新插拔、换了接口位置或者重启系统之后，还得手动切换模式才行。

在 lib/udev/rules.d/40-usb\_modeswitch.rules 中追加指令

```bash
sudo vim lib/udev/rules.d/40-usb_modeswitch.rules
```

```bash
# Realtek 8192F Wifi AC USB
ATTR{idVendor}=="0bda", ATTR{idProduct}=="c811", RUN+="/usr/sbin/usb_modeswitch -K -v 0bda -p c811"
```

保存退出，就可以愉快的使用了。

重启结束后就可以使用`x nmcli device wifi list `看到usb wifi

  

