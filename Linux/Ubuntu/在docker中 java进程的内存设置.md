 

[微服务](https://so.csdn.net/so/search?q=%E5%BE%AE%E6%9C%8D%E5%8A%A1&spm=1001.2101.3001.7020)和docker的结合应该是现在服务端的主流技术，随着springboot的出现，有很多公司已经把微服务迁移到了docker容器中，我们也不甘寂寞，也尝试了一把新技术，把以前的整体服务进行拆分以后，也全部上到了docker容器中。

问题
--

很久之前，业务部门利用springboot开发好一个app以后，就可以通过`java -jar` 的命令把程序丢给[docker](https://so.csdn.net/so/search?q=docker&spm=1001.2101.3001.7020)，然后在容器中启动起来，也不管到底系统给这个应用分配了多少内存。

后来由于java默认使用的内存是docker所在的宿主物理实体机 1/4 的物理内存**（注：不是free的内存，而是total 物理内存，包括被别的进程占用的）**，导致部署了很多应用以后，经常出现内存不足的情况，然后公司要求应用在启动的时候通过jvm的启动参数来限制java使用的内存来缓解内存消耗过快的问题。

再后来，我们的docker平台进行了升级， 有了可以让应用限制cpu个数和mem大小的参数设置，后面应用方把app的 `-Xmx`和docker的内存大小设置成同样大小， 比如2g。后面发现跑了一段时间以后，应用经常出现oom的情况，而被杀掉。

因为java使用的内存不仅仅是 `-Xmx`设置的大小， `-Xmx`设置的大小只是java进程堆的最大占用内存.

原因
--

为什么会出现上面这个问题呢？通过监控系统可以知道，docker获得的mem\_usage的大小是从外部得到的java进程的内存大小，不仅仅是 `-Xmx`设置的大小，如果 `-Xmx`和docker分配的内存一致的话，由于java应用其他的地方还要占用不少的内存，导致还没有到达 `-Xmx`的时候就没有可以用的内存了，所以被docker容器给干掉了，从而出现了oom的情况。

docker镜像服务的内存不能全部给“-Xmx”，因为JVM消耗的内存不仅仅是Heap。

1.  java程序的堆内存，最大就是 `-Xmx`设置的这个值
2.  Garbage collection在垃圾回收的时候使用的内存
3.  JIT optimization使用的内存
4.  java程序的Off-heap所使用的内存
5.  java程序的Metaspace所使用的内存
6.  JNI Code所占用的内存
7.  jvm启动的时候所占用的内存。

如何大体估算java进程使用的内存呢?

```cobol
Max memory = [-Xmx] + [-XX:MaxPermSize] + number_of_threads * [-Xss]
```

上面的公式大体得到了内存的占用，但是不是全部占用，网上有一些人做了一些试验，有两篇比较好的介绍文章:  
[https://plumbr.eu/blog/memory-leaks/why-does-my-java-process-consume-more-memory-than-xmx](https://link.jianshu.com?t=https://plumbr.eu/blog/memory-leaks/why-does-my-java-process-consume-more-memory-than-xmx)  
和  
[http://trustmeiamadeveloper.com/2016/03/18/where-is-my-memory-java/](https://link.jianshu.com?t=http://trustmeiamadeveloper.com/2016/03/18/where-is-my-memory-java/)

所以猜测在设置jvm启动参数的时候 `-Xmx`的这个值一般要小于docker限制内存数，个人觉得 `-Xmx`:`docker`的比例为 `4/5 ~ 3/4。`

**Docker环境下Java应用的最大内存和堆内存的设置的方法**

1、  设置应用允许使用的最大内存

通过docker run（创建一个新的容器并运行）命令中设置-m来进行设置。案例如下所示。

```bash
docker run -d --name test-service -m 800m --env LOG_LEVEL=ERROR -e "spring.profiles.active=dev" -p 8090:8090 test-service
```

  
2、设置java 最大堆内存

在Dockerfile里面，设置”-Xmx”参数。-Xmx用于指定堆(Heap)的最大值。案例如下所示。

```bash
CMD ["java", "-Xmx600m", "-jar", "/usr/local/test/data/test-1.0-SNAPSHOT.jar"]
```

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Java技能树](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)144479 人正在系统学习中

本文转自 <https://blog.csdn.net/bigtree_3721/article/details/108111187>，如有侵权，请联系删除。