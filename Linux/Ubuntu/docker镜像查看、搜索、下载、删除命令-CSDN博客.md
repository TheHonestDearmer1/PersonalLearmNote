 

> [docker](https://so.csdn.net/so/search?q=docker&spm=1001.2101.3001.7020) images

**列出本地所有镜像**  

![4424012-2ee7d1dafe694220.png](https://img-blog.csdnimg.cn/img_convert/bdd5cdda7292507f27071779a8fd8d20.png)

image.png

  
`docker images -a` 所有镜像  
`docker iamges -q` 所有镜像ID docker images -aq  
`docker images --digests` 显示摘要信息  
`docker iamges --digests -- no-trunc` 显示完整的摘要信息

> docker search XXXX

**搜索docker的镜像**  

![4424012-87f54b958977b2fb.png](https://img-blog.csdnimg.cn/img_convert/30258e6344061e15f37f4c852983e2b6.png)

image.png

`docker search -s 30 nginx` 显示stars超过30的信息  
`docker search -s 30 --no-trunc nginx` 显示完整的摘要信息  

![4424012-78b78e970dd23adb.png](https://img-blog.csdnimg.cn/img_convert/6bda6bd9e41a8a90f49a1b1b7de55821.png)

image.png

> docker pull xxx

**拉取镜像**  

![4424012-fb139311351c8892.png](https://img-blog.csdnimg.cn/img_convert/fd0348cf020a9572eae3fe546c60ecb5.png)

image.png

> docker rmi -f 镜像ID

**删除镜像ID**  
`docker rmi -f hello-world nginx` 删除多个  
`docker rmi -f $(docker iamges -qa)`删除全部

文章知识点与官方知识档案匹配，可进一步学习相关知识

[云原生入门技能树](https://edu.csdn.net/skill/cloud_native/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/cloud_native/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/cloud_native/?utm_source=csdn_ai_skill_tree_blog)16361 人正在系统学习中

本文转自 <https://blog.csdn.net/weixin_44694538/article/details/103345925>，如有侵权，请联系删除。