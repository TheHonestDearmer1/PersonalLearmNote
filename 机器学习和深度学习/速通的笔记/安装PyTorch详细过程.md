 

#### 安装[PyTorch](https://so.csdn.net/so/search?q=PyTorch&spm=1001.2101.3001.7020)过程

*   [安装anaconda](#anaconda_2)
*   [环境管理](#_23)
*   [PyTorch安装](#PyTorch_43)
*   [检验安装](#_57)

安装[anaconda](https://so.csdn.net/so/search?q=anaconda&spm=1001.2101.3001.7020)
------------------------------------------------------------------------------

登录anaconda的官网下载，anaconda是一个集成的工具软件不需要我们再次下载。[anaconda官网](https://www.anaconda.com/)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508135324971.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)点击下载  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508135444442.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)跳转到这个页面如果你的Python版本正好是3.8版，那便可以直接根据系统去选择自己相应的下载版本就可以了。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508141348945.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)但是如果你的Python版本号不是当前页面的版本号，那我建议你去选择相对应的版本号。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/2021050814175086.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)点击archive你就会跳转到下面的页面

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508141841387.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)你可以访问这篇[博客](https://blog.csdn.net/yuejisuo1948/article/details/81043823)去找到当前与你python版本号相对应的anaconda（比如我的python是3.7.2版本的，因为这个版本在那篇博客中没有对应的anaconda的版本所以我便选择了Anaconda3-2019.03，而这个版本对应的是python3.7.3版，新的版本对旧的版本具有包容性，虽然有的人说运用最新的版本对现在所有的python版本都可以兼容，但是我没有试过，如果有试过的可以告诉我）。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508142816106.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)如果不知道怎么查找版本号？同时按住win+R进入cmd输入命令: python --version

下载完便开始安装，根据你的需求去选择，看你是商业用途还是个人用途，我选择的是个人  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508142125178.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)一定要记住自己安装的路径  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508143408434.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)  
点击对勾将anaconda的默认值设置为python3.7  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508143815465.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508143836980.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)剩下的默认就可以了。  
安装完成以后点击win图片，在最近添加和anaconda包中都能找到anaconda prompt。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508150235433.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)  
出现（base）便表示成功  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508150416774.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)

环境管理
----

在我们做项目的时候可以能需要不同环境的python版本，有时候要1.0版本，有的需要3.0版本的拿在这里我们就需要建立不同的环境，在不同的需要的时候去使用。

```
(base) PS C:\Users\11011> python --version
Python 3.11.5
```

这个是在Anaconda Prompt下操作的  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508152241795.png)

> conda create -n

这是创建的格式  
"pytorch"是这个环境变量的名字  
"python=3.7"是我们要确定的当前环境的版本数  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508152416325.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)告诉我们创建这个环境需要这些包加入，同意就输入y  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508152914260.png)  
这样就操作成功。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508153109367.png)  
我们输入activate pytorch（pytorch是你定义的这个环境的名字），左边的环境就从base（基本环境），变成了pytorch环境。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508153341530.png)  
输入pip list，查看当前环境下面有哪些包，我们发现没有pytorch，那么下面我们就需要安装它。

PyTorch安装
---------

进入[pytorch官网](https://pytorch.org/)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508161707359.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508162534838.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)复制这一段操作指令。（这种情况是需要电脑上有单独的英伟达的显卡、或者英伟达的显卡和集显这两种情况都是可以的。）  
![在这里插入图片描述](https://img-blog.csdnimg.cn/2021050816354463.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)  
进入命令符号窗口，输入nvidia-smi,查看当前驱动的版本号，观察Driver Version的值是否大于400，如果小于请更新显卡驱动。推荐使用驱动精灵更新，虽然驱动精灵的版本没有官网的更新的那么及时但是驱动精灵更新简单，不需要过多的操作。当然也可以去[英伟达显卡驱动更新](https://www.nvidia.cn/Download/index.aspx?lang=cn)去下载。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508164345952.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)选择自己显卡相对应的系列，括号中Notebooks是笔记本。

```
conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
```

将上边复制的代码粘贴进去。**注意此事的环境是pytorch**  
![在这里插入图片描述](https://img-blog.csdnimg.cn/2021050817315023.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)  
输入y  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508173243684.png)便开始下载了（下载时间较长请耐心等待）  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508184647793.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01DWVpTRg==,size_16,color_FFFFFF,t_70)  
下载完成后我们再次输入pip list，查看到已经有[torch](https://so.csdn.net/so/search?q=torch&spm=1001.2101.3001.7020)的存在。

检验安装
----

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210508185135569.png)先输入python，然后输入import torch，如果输入后没有任何报错，没有任何显示那就是成功了，然后再输入torch.cuda.is\_available()，返回的是True，那便是完成了整个操作。

上述步骤参考[https://www.bilibili.com/video/BV1hE411t7RN?t=734](https://www.bilibili.com/video/BV1hE411t7RN?t=734)，中间参杂自己操作时的一些操作和思考。

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Python入门技能树](https://edu.csdn.net/skill/python/python-3-246?utm_source=csdn_ai_skill_tree_blog)[人工智能](https://edu.csdn.net/skill/python/python-3-246?utm_source=csdn_ai_skill_tree_blog)[深度学习](https://edu.csdn.net/skill/python/python-3-246?utm_source=csdn_ai_skill_tree_blog)390673 人正在系统学习中

本文转自 <https://blog.csdn.net/MCYZSF/article/details/116525159>，如有侵权，请联系删除。