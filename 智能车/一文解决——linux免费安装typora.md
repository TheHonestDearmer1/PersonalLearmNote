#一文解决——linux免费安装typora


#### 文章目录
- - - - 


## 下载

链接:  提取码: wew7

## 安装

```
tar xzvf Typora-linux-x64.tar.gz 
cd bin
sudo cp -ar Typora-linux-x64 /opt
cd /opt/Typora-linux-x64/
#启动
./Typora

```

下面为了在任意位置启动，我们设置下环境变量

```
sudo vim ~/.bashrc

```

打开.bashrc配置文件，添加：

```
#Typora环境变量
export PATH=$PATH:/opt/Typora-linux-x64

```

source以下，让配置生效

```
source ~/.bashrc

```

ok了，可以启动typora <img src="https://img-blog.csdnimg.cn/c4e147f3f6e34c78ad3a2db0efacba30.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2O5bGx5Luk54uQ5Yay44CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

## 添加桌面标

```
cd /usr/share/applications
sudo vim typora.desktop

```

添加以下内容：

```
[Desktop Entry]
Name=Typora
Comment=Typora
Exec=/opt/Typora-linux-x64/Typora
Icon=/opt/Typora-linux-x64/resources/app/asserts/icon/icon_256x256.png
Terminal=false
Type=Application
Categories=Developer;

```

后重启电脑就ok了 <img src="https://img-blog.csdnimg.cn/630e7fa752664073910b3fbc845e7bf5.png" alt="在这里插入图片描述">

## 右键打开

```
gedit ~/.config/mimeapps.list

```

添加text/markdown=typora.desktop; <img src="https://img-blog.csdnimg.cn/27e35686e41e48cc8c12830668247ed2.png" alt="在这里插入图片描述">
