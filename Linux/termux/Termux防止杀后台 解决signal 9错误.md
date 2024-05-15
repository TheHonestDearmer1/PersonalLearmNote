  

[

01:21

Termux "Process completed (signal 9)" 错误解决方式

8726 31

视频 Ivon\_Huang









](//www.bilibili.com/video/BV1aZ4y1C73E)

Android 12以上的设备只要Termux进后台，运行桌面环境这类占用高CPU的程序，便有可能被Android系统杀死。此时Termux会抛出一个"Process completed (signal 9) - press Enter"信息。

将Termux"上锁"(MIUI)或禁用电池优化是不管用的，Termux照样会被杀。这起因于一个新引进的系统机制，称作"Phantom Process Killing"，会限制后台程序占用。

Github上有一篇讨论Phantom Process Killing机制的文章：https://github.com/agnostic-apollo/Android-Docs/blob/master/en/docs/apps/processes/phantom-cached-and-empty-processes.md

总之，这对Temux来说是重大伤害，除了用悬浮窗让Termux挂在前台不触发Phantom Processes Killing以外，建议是用ADB命令永久停用"Phantom Process Killing"。

**以下命令可能会对设备造成损坏，或导致后台程序失控，风险自负。**  

1.  Android手机打开ADB调试
    
2.  Windows电脑至Android官网下载ADB工具: https://developer.android.com/studio/releases/platform-tools
    
    (如果没有电脑，可以试试Termux跑ADB远程调试：https://ivonblog.com/posts/termux-wireless-adb/)  
    
3.  解压，在platfrom\_tools文件夹按SHIFT+右键，打开Powershell
    

将手机接到Windows电脑，运行此命令配对，在手机上同意调试：

```shell
./adb devices
```

再来，按照系统版本输入命令，不需要root权限：

```shell
# Android 12L和Android 13
./adb shell "settings put global settings_enable_monitor_phantom_procs false"

# Android 12，无GMS
./adb shell "/system/bin/device_config put activity_manager max_phantom_processes 2147483647"

# Android 12，有GMS
./adb shell "/system/bin/device_config set_sync_disabled_for_tests persistent; /system/bin/device_config put activity_manager max_phantom_processes 2147483647"
```

重开机，Termux在后台运行时应该就不会被杀了。

本文转自 <https://www.bilibili.com/read/cv20060713/>，如有侵权，请联系删除。