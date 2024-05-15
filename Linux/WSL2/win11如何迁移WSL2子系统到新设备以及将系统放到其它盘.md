## 在原系统中打包构建好的WSL2子系统

查看wsl下的系统：

```
(base) PS C:\Users\11011> wsl -l
适用于 Linux 的 Windows 子系统分发版:
Ubuntu-20.04 (默认)
docker-desktop
docker-desktop-data
```

然后安装打包想要打包的wsl系统  

```
wsl --export Ubuntu20.04 D:/Ubuntu.tar
```

D:/Ubuntu.tar这个代表的是被打包出来的文件的位置以及名称



**注意：**如果是要安装在新的盘上而不是换一台设备就要注销原来的子系统：

```
wsl --unregister Ubuntu-20.04
```

查看wsl下的系统：

## 在新系统中使用该打包好的子系统

将打包好的这个包发送到新的系统当中想要放置的盘中

然后安装打包后的 Ubuntu20.04 :  
这里的D：、Ubuntu\_20\_04 就是我设置的安装目录。  
D:\\Ubuntu.tar 就是包的位置。  
–version 2 代表这个子系统以 wsl2 的形式安装。

```
wsl --import Ubuntu-20.04 D:\Ubuntu_20_04\ D:\export.tar --version 2
```

安装好后设置为默认系统：

```
wsl --setdefault Ubuntu-20.04 
```

执行wsl就进入子系统了

```
(base) PS C:\Users\11011> wsl
root@MAX2:/mnt/c/Users/11011#
```

### 打开后发现此时默认的是 root 用户。

如果我们要恢复默认普通的用户，我们原先的用户名为 orange. 安装的是Ubuntu-20.04 所以：

```
Ubuntu2004 config --default-user orange
```

再打开就恢复默认普通用户了。