![](//upload-images.jianshu.io/upload_images/6262006-51550150f8518686.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

pypi

写过 Python 程序的小伙伴们都知道，需要 import 个非 Python 自带的软件包时，都要用到 **pip** 这个程序。平时我们都是用 pip，如果我们写好了一个程序，想让大家都能用的到，那么是不是也可以通过 pip 发布出去呢？

答案当然是可以了，这篇文章我们就来看看如何用 pip 发布一个 python 程序。

1\. 环境准备
--------

要用 pip 发布 python 程序，首先当然是要安装 Python 和 pip 这两个软件了，以 Ubuntu 16.04 为例：

    $ sudo apt update 
    $ sudo apt install -y python python-pip


CentOS 和 RedHat 因为 RPM 体系需要依赖于 python，更是默认就安装好了。

另外发布 Pypi，还需要安装一个发布工具，**twine**，以及其所依赖的 setuptools、wheel：

    $ sudo pip install --upgrade twine setuptools wheel


好，到这环境就已经就绪了。

2\. 注册帐号
--------

pip 上传代码包是最终保存在 **[https://pypi.org](https://pypi.org)** 这个网站上的，所以要用 pip 发布程序，就需要在这个网站上注册一个帐号。

访问该网址进行注册：`https://pypi.org/account/register/`

![](//upload-images.jianshu.io/upload_images/6262006-549dffd70041dec3.png?imageMogr2/auto-orient/strip|imageView2/2/w/420/format/webp)

pypi

注册后还需要进行邮箱验证，流程和普通网站没有任何区别，所以具体步骤就不在这里详细介绍了。

3\. 代码结构
--------

要发布 Python 程序，程序的结构必须符合特定的要求，假设要发布的程序名为 example-pkg，基本的目录结构如下：

    /example-pkg
      /example-pkg
        __init__.py
      setup.py
      LICENSE
      README.md


说一下目录和文件的含义：

*   首先最外层要建立一个和发出程序同名的文件夹：**/example-pkg**
*   该文件夹下还要再简历一个同名文件夹，用来存放程序代码：**/example-pkg/example-pkg**
*   Python 的老规矩，example-pkg/example-pkg 目录下当然要有一个 `__init__.py` 文件。
*   **/example-pkg** 目录下要有一个叫 **setup.py** 的文件，如果下载过 Python 代码包，应该都知道这个文件，需要通过这个文件进行 Python 代码的编译（可能会有依赖的其他代码包或者依赖的 C 文件）和安装。
*   LICENSE 文件：这个文件就是用来保存代码所使用的开源许可证。
*   README.md：这个是软件行业的惯例了，帮助文档。

对于 setup.py 文件，还有必要好好说说，先贴个例子，下面这个例子中，主要是实现了从 `/example-pkg/example-pkg/__init__.py` 文件中读取 ****version**** 参数，来配置当前软件的版本，并指定了代码包名（name）、作者（author）、邮箱（author\_email）、描述信息（long\_description、long\_description\_content\_type）、依赖（install\_requires），以及哪些文件不会被打包到程序中（exclude\_package\_data）。

另外需要提醒大家一点，**给程序起名字不要带下划线（\_）**，python import 代码包时，是不支持下划线包名的，出现这种情况就比较尴尬，代码装上了，还是用不了。

    #!/usr/bin/env python
    
    import re
    import setuptools
    
    version = ""
    with open('example-pkg/__init__.py', 'r') as fd:
        version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                            fd.read(), re.MULTILINE).group(1)
    
    with open("README.md", "r") as fh:
        long_description = fh.read()
        
    setup(
        name='jparser',  # 包的名字
        author='zhouxinfei',  # 作者
        version='0.1.0',  # 版本号
        license='MIT',
    
        description='project describe',  # 描述
        long_description='''long description''',
        author_email='wyxczhou@163.com',  # 你的邮箱**
        url='https://blog.csdn.net/xc_zhou',  # 可以写github上的地址，或者其他地址
        # 包内需要引用的文件夹
        # packages=setuptools.find_packages(exclude=['url2io',]),
        packages=["jparser"],
        # keywords='NLP,tokenizing,Chinese word segementation',
        # package_dir={'jieba':'jieba'},
        # package_data={'jieba':['*.*','finalseg/*','analyse/*','posseg/*']},
    
        # 依赖包
        install_requires=[
            'requests >= 2.19.1',
            "lxml >= 3.7.1",
        ],
        classifiers=[
            # 'Development Status :: 4 - Beta',
            # 'Operating System :: Microsoft'  # 你的操作系统  OS Independent      Microsoft
            'Intended Audience :: Developers',
            # 'License :: OSI Approved :: MIT License',
            # 'License :: OSI Approved :: BSD License',  # BSD认证
            'Programming Language :: Python',  # 支持的语言
            'Programming Language :: Python :: 3',  # python版本 。。。
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Topic :: Software Development :: Libraries'
        ],
        zip_safe=True,
    )


4\. 上传和检查
---------

一切准备就绪，下面就可以执行打包命令，产生要上传的代码包了：

    $ python setup.py sdist bdist_wheel


执行结束后，会产生如下目录和文件：

    /example-pkg/dist/
      example-pkg-0.0.1-py3-none-any.whl
      example-pkg-0.0.1.tar.gz


包有了，就差上传了，执行第一步中安装的 twine 命令：

    $ twine upload dist/*
    Uploading distributions to https://upload.pypi.org/legacy/
    Enter your username: <your pypi.org username>
    Enter your password: <your pypi.org password>
    Uploading example-pkg-0.0.1-py3-none-any.whl
    100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 45.0k/45.0k [00:01<00:00, 24.0kB/s]
    Uploading example-pkg-0.0.1.tar.gz
    100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 43.8k/43.8k [00:00<00:00, 46.2kB/s]

上传完毕！不过这里有一点需要注意，上传新版本后，很可能 `pip search` 还没法查到版本的更新，这是正常的，我理解是  
`pip search` 命令依赖于缓存，所以不会立刻生效。

## Token上传法

在pypi创建一个token

**然后用户名使用**

```
__token__
```

**密码使用在pypi创建的token**



接下来就让我们下载自己刚刚上传的 python 试试吧：

    $ pip install example-pkg
    $ python
    >>> import example-pkg
    >>> example-pkg.name
    'example-pkg'


最后再补充一点，上传可能会失败，提示无法上传指定的代码包，此时很大的可能是 pypi 中已经有了相同的代码包，所以建议在上传之前，先搜索一下是否有重名的代码包，选择一个不冲突的名字，再上传。

例如下面这个例子，example-pkg 已经存在了，如果要再上传，那当然会失败，换个名字就解决了。

    $ pip search example-pkg
    example-pkg (0.0.7)                                            - A small example package
    ......

在你的项目文件夹的工作目录下，新建setup.py文件，然后在里面添加如下内容：

2、在setup.py目录下执行

    python setup.py sdist

复制

最终生成一个dist文件夹，在文件夹里面就有一个创建好的安装包，格式为xxx.tar.gz的压缩包

3、安装xxx.tar.gz包

    pip install xxx.tar.gz

4、检查是否安装成功

    pip list   # 显示所有已安装的包

5\. 参考文档
--------

*   [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)

本文转自 <https://www.jianshu.com/p/daf3a574e0f5>，如有侵权，请联系删除。