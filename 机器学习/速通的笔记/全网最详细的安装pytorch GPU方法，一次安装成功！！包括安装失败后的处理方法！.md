 

![在这里插入图片描述](https://img-blog.csdnimg.cn/4516cb2add6e414c814f6da07d796d98.png)

#### 文章目录

*   [前提---查看是否有NVIDIV英伟达显卡【笑哭】](#NVIDIV_8)
*   [一、查看电脑的显卡驱动版本](#_15)
*   *   [方法一：在\`cmd命令窗口\`中输入\`nvidia-smi\`，可以发现版本为12.2](#cmdnvidiasmi122_16)
    *   [方法2：点击NVIDIA控制面板→系统信息](#2NVIDIA_18)
*   [二、安装CUDA](#CUDA_23)
*   *   [方法1： 在pytorch官网https://pytorch.org/，直接复制命令进行安装](#1_pytorchhttpspytorchorg_25)
    *   [方法2：从官网下载对应版本的CUDA版本](#2CUDA_34)
*   [三，安装cuDNN，需要注册（可安装可不安装，因为cuDNN就是个加速器）](#cuDNNcuDNN_83)
*   [四，pytorch-GPU](#pytorchGPU_92)
*   *   [4.1 新建虚拟环境（推荐）](#41__93)
    *   [4.2 在官网下载pytorch](#42_pytorch_102)
*   [五，测试pytorch gpu是否可用](#pytorch_gpu_113)
*   [六，补充（针对安装失败的情况）](#_125)
*   *   [6.1 去\`conda清华源\`找到对应的pytorch、torchvision、torchaudio的版本，我的版本如下：](#61_condapytorchtorchvisiontorchaudio_128)
    *   [6.2 在对应的虚拟环境下安装这三个包](#62__140)
*   [总结](#_161)

* * *

前提—查看是否有NVIDIV英伟达显卡【笑哭】
-----------------------

在控制面板打开`设备管理器`  
![在这里插入图片描述](https://img-blog.csdnimg.cn/5bcd6704003f469b8f3045825b0d5418.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/1452d3a038c543268001f3c447507a96.png)

一、查看电脑的显卡驱动版本
-------------

### 方法一：在`cmd命令窗口`中输入`nvidia-smi`，可以发现版本为12.2

![在这里插入图片描述](https://img-blog.csdnimg.cn/c121fd55a10e4e34b7274f8383223488.png)

### 方法2：点击NVIDIA控制面板→系统信息

![在这里插入图片描述](https://img-blog.csdnimg.cn/3277a45b73204109a8e48ea040759454.png)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/7a0b6ce589fb4c5db21e545a7f385e53.png)

二、安装CUDA
--------

建`议电脑显卡驱动版本**`\>=`**安装的CUDA版本`

### 方法1： 在pytorch官网https://pytorch.org/，直接复制命令进行安装

![在这里插入图片描述](https://img-blog.csdnimg.cn/21add780d3914a41afe06944795e1973.png)  
在`命令窗口中直接输入命令--回车安装`

```python
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

如果安装失败，是因为`网速不够快`，建议用`手机热点`或者末尾`加一个镜像源`  
![在这里插入图片描述](https://img-blog.csdnimg.cn/b901807033a44233bdd83907be1ac465.png)

### 方法2：从官网下载对应版本的[CUDA版本](https://so.csdn.net/so/search?q=CUDA%E7%89%88%E6%9C%AC&spm=1001.2101.3001.7020)

`官网链接`  
链接: [https://developer.nvidia.com/cuda-toolkit-archive](https://developer.nvidia.com/cuda-toolkit-archive)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/302cc4a6c0c84b1b91ec4143dfc0f458.png)  
由于我的`显卡版本是12.2，我只要安装小于等于12.2均可以，我安装**11.8**`

![在这里插入图片描述](https://img-blog.csdnimg.cn/bcd0048f7f4b4cf49cf6c74193131d94.png)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/7627a10874084bd3b88010fe5f308484.png)

可以`修改安装路径`，因为`文件较大，我没有使用默认的路径`

![在这里插入图片描述](https://img-blog.csdnimg.cn/601a01b85817407cabff8a45c0a1802c.png)

下载完成开始安装，可以`安装在自定义的目录下`

![在这里插入图片描述](https://img-blog.csdnimg.cn/65a4dcc6aa9f4689ab4b287bb8775106.png)

同意`继续`  
![在这里插入图片描述](https://img-blog.csdnimg.cn/8a130f54662c4bbcb8f36ba3b2d41d84.png)  
选择`推荐的精简`

![在这里插入图片描述](https://img-blog.csdnimg.cn/de384313a49643cba2eef40248021a60.png)

点就完事！！

![在这里插入图片描述](https://img-blog.csdnimg.cn/b906102f756c42a9a49727f71bf1c7da.png)

开始`安装`！！

![在这里插入图片描述](https://img-blog.csdnimg.cn/cbace1395686476ea6c482c02eb03651.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/736a59ad42e647cf8c51d898f089b794.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/6605a81b59244ddf936a047583f2a652.png)

**查看是否`安装成功`**  
在命令窗口中输入`nvcc -V` 进行检查

```python
nvcc  -V
```

可以看到我们安装成功  
![在这里插入图片描述](https://img-blog.csdnimg.cn/29f2b2e404ec40fd9c15d3680b5031ab.png)

三，安装cuDNN，需要注册（可安装可不安装，因为cuDNN就是个加速器）
-------------------------------------

![在这里插入图片描述](https://img-blog.csdnimg.cn/6f4ac76a594149cb96d1ba29282f3724.png)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/559453fc43e54828a2c5f028e6bd3b96.png)  
下载`解压后的文件`  
![在这里插入图片描述](https://img-blog.csdnimg.cn/eee4c99d075849959e0345f198a54cde.png)  
将`解压文件复制到CUDA安装路径`下 ！！！就已经安装完成！！  
![在这里插入图片描述](https://img-blog.csdnimg.cn/9c9185f9557f4ac6a89445d322b9bc8b.png)

四，pytorch-GPU
-------------

### 4.1 新建虚拟环境（推荐）

若不想新建，也可以在以前的环境中安装，请`跳到下一步4.2`！！  
因为`CUDA 10.1 支持 Python 3.5 - 3.8，而 CUDA 11.0 则支持 Python 3.5 - 3.9`，所以我安装python3.9

```python
conda create -n pytorch-gpu python==3.9
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/83ccac33ba90467ab05793c6ef18a7bd.png)

### 4.2 在官网下载pytorch

官网链接 链接: [https://pytorch.org/](https://pytorch.org/)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/7a8c6e64b1974911aabd96a660dfa234.png)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/12d5ea6b1416456cb75bc8719329bf4d.png)

```python
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

我我在最后加了`镜像源下载，否则太慢，容易下载失败`。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/d9db6873411d46df8e16f35ec69ecf72.png)

五，测试pytorch gpu是否可用
-------------------

torch.cuda.is\_available() `为True`则`GPU可用`，`False表示不可用`

```python
import torch
print(torch.__version__)
print(torch.version.cuda)
print(torch.cuda.is_available())  #输出为True，则安装无误
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/3cf9b890cbc446a9a5c1d44d7215cf3b.png)

非常好用！！！

六，补充（针对安装失败的情况）
---------------

有粉丝私聊我，说他安装失败，我又想了一个办法！

### 6.1 去`conda清华源`找到对应的pytorch、torchvision、torchaudio的版本，我的版本如下：

![在这里插入图片描述](https://img-blog.csdnimg.cn/9eaf0e549d124f2d82a4473134ef3e7b.png)

清华大学`开源软件镜像站链接`如下：  
链接: [https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/](https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/)

![在这里插入图片描述](https://img-blog.csdnimg.cn/0d61562d97104d91a9510c47416cf409.png)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/d46994aa0b3745fb977a591b22c1201e.png)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/aecbb7837c35496989b3ecee2d6a525d.png)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/713a0a6a47444e08bd3cb7f0b2f0a794.png)

### 6.2 在对应的虚拟环境下安装这三个包

![在这里插入图片描述](https://img-blog.csdnimg.cn/a1d8181287414c37be8a5aba9ecdb3fe.png)

```python
conda install --offline pytorch-2.1.1-py3.9_cuda11.8_cudnn8_0.tar.bz2
```

```python
conda install --offline torchaudio-2.1.1-py39_cu118.tar.bz2
```

```python
conda install --offline torchvision-0.16.1-py39_cu118.tar.bz2
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/e110acad2d704b559387be89797de601.png)

* * *

总结
--

`PyTorch的GPU版本利用了NVIDIA的CUDA技术`，使得深度学习计算能够高效地在GPU上运行。使用GPU来执行深度学习计算可以显著加速计算，从而减少训练和推理时间。

`CUDA是NVIDIA推出的一种通用并行计算架构`，可以使GPU执行通用计算任务，而不仅仅是图形处理。在PyTorch中，可以使用CUDA来利用NVIDIA GPU的并行计算能力加速模型训练和推理。

`cuDNN是NVIDIA专门为深度学习模型设计的一个库`，它提供了高效的卷积操作和其他计算操作，可以进一步加速深度学习任务。在PyTorch中使用`cuDNN来优化深度学习模型的性能`。

总的来说，PyTorch的GPU版本通过与NVIDIA的`CUDA技术和cuDNN库`的深度集成，为深度学习研究和应用提供了强大、灵活且高效的计算能力。

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Python入门技能树](https://edu.csdn.net/skill/python/python-3-246?utm_source=csdn_ai_skill_tree_blog)[人工智能](https://edu.csdn.net/skill/python/python-3-246?utm_source=csdn_ai_skill_tree_blog)[深度学习](https://edu.csdn.net/skill/python/python-3-246?utm_source=csdn_ai_skill_tree_blog)390708 人正在系统学习中

本文转自 <https://blog.csdn.net/qlkaicx/article/details/134577555>，如有侵权，请联系删除。