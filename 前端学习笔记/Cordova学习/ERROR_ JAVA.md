 

我相信这个一个很简单很基础的配置，但是如果不注意，你就入坑啦，等着花3-4个小时吧。

这里说一下，如果要在cmd打开控制台，输入[gradle](https://so.csdn.net/so/search?q=gradle&spm=1001.2101.3001.7020)命令的话，那就必定要配置gradle环境变量。  
我相信做过javaWeb开发的同志们都会配置JAVA\_HOME了，所以我就按照当时候配置JAVA\_HOME的[Flow](https://so.csdn.net/so/search?q=Flow&spm=1001.2101.3001.7020)来配置 GRADLE\_HOME了，结果？你猜猜遇到什么问题了吗？

先上图啦，遇到这个问题了。

![这里写图片描述](https://img-blog.csdn.net/20171027113055188?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzkzMzcyMA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

问题：gradle配置失败了，已经很明显的告诉你JAVA\_HOME配置有错误，是一个无效的目录

配置Gradle如何配置
------------

### 首先来看看JAVA\_HOME如何配置

1，找到JDK目录，找到bin目录，打开bin  
![这里写图片描述](https://img-blog.csdn.net/20171027113716925?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzkzMzcyMA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

2,配置JAVA\_HOME  
JAVA\_HOME=C:\\Program Files\\Java\\jdk1.8.0\_73\\bin  
![这里写图片描述](https://img-blog.csdn.net/20171027113916931?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzkzMzcyMA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

3,把%JAVA\_HOME%放进系统环境变量Path里面

4,cmd java -version  
![这里写图片描述](https://img-blog.csdn.net/20171027114319324?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzkzMzcyMA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  
成功了

### 配置GRADLE\_HOME

#### 和配置JAVA\_HOME一样配置GRADLE\_HOME

结果如何？  
![这里写图片描述](https://img-blog.csdn.net/20171027114432993?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzkzMzcyMA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

失败了，卧槽。你以为是跟以前配置JAVA\_HOME一样配置它,那就错了。

错误问题：JAVA\_HOME设置错误无效的目录，那就是说JAVA\_HOME环境变量目录有问题

解决方法：修改JAVA\_HOME路径

#### 正确配置GRADLE\_HOME

1，JAVA\_HOME,后面不能带bin目录,也不能打分号;  
![这里写图片描述](https://img-blog.csdn.net/20171027115746279?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzkzMzcyMA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

2，GRADLE\_HOME配置需要带bin  
;%GRADLE\_HOME%\\bin;

![这里写图片描述](https://img-blog.csdn.net/20171027120839611?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzkzMzcyMA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

3,把JAVA\_HOME,GRADLE\_HOME两个配置好的环境设置到系统环境Path下:

4，成功了  
![这里写图片描述](https://img-blog.csdn.net/20171027121057267?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzkzMzcyMA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Java技能树](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)140188 人正在系统学习中

本文转自 <https://blog.csdn.net/u013933720/article/details/78363509>，如有侵权，请联系删除。