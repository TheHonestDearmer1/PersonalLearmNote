 

在[docker](https://so.csdn.net/so/search?q=docker&spm=1001.2101.3001.7020)容器中访问宿主机端口有时候会显示连接失败。

宿主机明明有8080的服务，容器内确访问不到。

```cobol
localhost：8080
```

Docker有四种网络模式

1.host模式

容器和宿主机共享network，这时候localhost就可以访问宿主机端口了。

```scss
 docker run -d --network host --name nginx
```

2.[container](https://so.csdn.net/so/search?q=container&spm=1001.2101.3001.7020)模式

容器A和容器B共享network，就是说容器之间可以通过localhost直接访问。

```scss
 docker run -d --network container --name nginx
```

3.none模式

容器与宿主机隔绝，不能联网，安全性最高，一般很少用到。

```scss
 docker run -d --network none --name nginx
```

4.bridge模式(默认模式)

每个容器有自己的network，通过localhost访问不到宿主机

```sql
 docker run -d --name nginx
```

  
 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[云原生入门技能树](https://edu.csdn.net/skill/cloud_native/cloud_native-3eb56d157f784765b43f6f2ef0f28aac?utm_source=csdn_ai_skill_tree_blog)[容器(docker)](https://edu.csdn.net/skill/cloud_native/cloud_native-3eb56d157f784765b43f6f2ef0f28aac?utm_source=csdn_ai_skill_tree_blog)[安装docker](https://edu.csdn.net/skill/cloud_native/cloud_native-3eb56d157f784765b43f6f2ef0f28aac?utm_source=csdn_ai_skill_tree_blog)18115 人正在系统学习中

本文转自 <https://blog.csdn.net/ma726518972/article/details/108146218>，如有侵权，请联系删除。