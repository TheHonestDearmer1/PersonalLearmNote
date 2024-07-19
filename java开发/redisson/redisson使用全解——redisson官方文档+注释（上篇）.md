 

#### 文章目录

*   [官方文档](#_7)
*   [Redisson项目介绍](#Redisson_10)
*   [一、概述](#_27)
*   [二、配置方法](#_46)
*   *   [2.1. 程序化配置方法](#21__56)
    *   [2.2. 文件方式配置](#22__66)
    *   *   [2.2.1 通过YAML格式配置](#221_YAML_69)
    *   [2.3. 常用设置](#23__85)
    *   [2.4. 集群模式](#24__161)
    *   *   [2.4.1. 集群设置](#241__178)
        *   [2.4.2. 通过YAML文件配置集群模式](#242_YAML_315)
    *   [2.5. 云托管模式](#25__347)
    *   *   [2.5.1. 云托管模式设置](#251__363)
        *   [2.5.2. 通过YAML文件配置集群模式](#252_YAML_504)
    *   [2.6. 单Redis节点模式](#26_Redis_536)
    *   *   [2.6.1. 单节点设置](#261__547)
        *   [2.6.2. 通过YAML文件配置集群模式](#262_YAML_655)
    *   [2.7. 哨兵模式](#27__682)
    *   *   [2.7.1. 哨兵模式设置](#271__695)
        *   [2.7.2. 通过YAML文件配置集群模式](#272_YAML_833)
    *   [2.8. 主从模式](#28__865)
    *   *   [2.8.1. 主从模式设置](#281__878)
        *   [2.8.2. 通过YAML文件配置集群模式](#282_YAML_1016)
*   [三、程序接口调用方式](#_1050)
*   *   [3.1. 异步执行方式](#31__1076)
    *   [3.2. 异步流执行方式](#32__1099)
*   [四、数据序列化](#_1121)
*   [五、单个集合数据分片（Sharding）](#Sharding_1143)
*   [六、分布式对象](#_1157)
*   *   [6.1. 通用对象桶（Object Bucket）](#61_Object_Bucket_1176)
    *   [6.2. 二进制流（Binary Stream）](#62_Binary_Stream_1206)
    *   [6.3. 地理空间对象桶（Geospatial Bucket）](#63_Geospatial_Bucket_1222)
    *   [6.4. BitSet](#64_BitSet_1238)
    *   *   [6.4.1. BitSet数据分片（Sharding）（分布式RoaringBitMap）](#641_BitSetShardingRoaringBitMap_1249)
    *   [6.5. 原子整长形（AtomicLong）](#65_AtomicLong_1261)
    *   [6.6. 原子双精度浮点（AtomicDouble）](#66_AtomicDouble_1271)
    *   [6.7. 话题（订阅分发）](#67__1281)
    *   *   [6.7.1. 模糊话题](#671__1298)
    *   [6.8. 布隆过滤器（Bloom Filter）](#68_Bloom_Filter_1313)
    *   *   [6.8.1. 布隆过滤器数据分片（Sharding）](#681_Sharding_1324)
    *   [6.9. 基数估计算法（HyperLogLog）](#69_HyperLogLog_1339)
    *   [6.10. 整长型累加器（LongAdder）](#610_LongAdder_1350)
    *   [6.11. 双精度浮点累加器（DoubleAdder）](#611_DoubleAdder_1367)
    *   [6.12. 限流器（RateLimiter）](#612_RateLimiter_1385)
*   [七、分布式集合](#_1403)
*   *   [7.1. 映射（Map）](#71_Map_1404)
    *   *   [7.1.1. 映射（Map）的元素淘汰（Eviction），本地缓存（LocalCache）和数据分片（Sharding）](#711_MapEvictionLocalCacheSharding_1449)
        *   [7.1.2. 映射持久化方式（缓存策略）](#712__1572)
        *   [7.1.3. 映射监听器（Map Listener）](#713_Map_Listener_1605)
        *   [7.1.4. LRU有界映射](#714_LRU_1662)
    *   [7.2. 多值映射（Multimap）](#72_Multimap_1677)
    *   *   [7.2.1. 基于集（Set）的多值映射（Multimap）](#721_SetMultimap_1679)
        *   [7.2.2. 基于列表（List）的多值映射（Multimap）](#722_ListMultimap_1695)
        *   [7.2.3. 多值映射（Multimap）淘汰机制（Eviction）](#723_MultimapEviction_1712)
    *   [7.3. 集（Set）](#73_Set_1730)
    *   *   [7.3.1. 集（Set）淘汰机制（Eviction）](#731_SetEviction_1739)
        *   [7.3.2. 集（Set）数据分片（Sharding）](#732_SetSharding_1749)
    *   [7.4. 有序集（SortedSet）](#74_SortedSet_1761)
    *   [7.5. 计分排序集（ScoredSortedSet）](#75_ScoredSortedSet_1774)
    *   [7.6. 字典排序集（LexSortedSet）](#76_LexSortedSet_1791)
    *   [7.7. 列表（List）](#77_List_1804)
    *   [7.8. 队列（Queue）](#78_Queue_1814)
    *   [7.9. 双端队列（Deque）](#79_Deque_1824)
    *   [7.10. 阻塞队列（Blocking Queue）](#710_Blocking_Queue_1835)
    *   [7.11. 有界阻塞队列（Bounded Blocking Queue）](#711_Bounded_Blocking_Queue_1848)
    *   [7.12. 阻塞双端队列（Blocking Deque）](#712_Blocking_Deque_1869)
    *   [7.13. 阻塞公平队列（Blocking Fair Queue）](#713_Blocking_Fair_Queue_1883)
    *   [7.14. 阻塞公平双端队列（Blocking Fair Deque）](#714_Blocking_Fair_Deque_1897)
    *   [7.15. 延迟队列（Delayed Queue）](#715_Delayed_Queue_1918)
    *   [7.16. 优先队列（Priority Queue）](#716_Priority_Queue_1936)
    *   [7.17. 优先双端队列（Priority Deque）](#717_Priority_Deque_1951)
    *   [7.18. 优先阻塞队列（Priority Blocking Queue）](#718_Priority_Blocking_Queue_1967)
    *   [7.19. 优先阻塞双端队列（Priority Blocking Deque）](#719_Priority_Blocking_Deque_1984)

[redisson使用全解——redisson官方文档+注释（上篇）](https://blog.csdn.net/A_art_xiang/article/details/125525864)  
[redisson使用全解——redisson官方文档+注释（中篇）](https://blog.csdn.net/A_art_xiang/article/details/125536050)  
[redisson使用全解——redisson官方文档+注释（下篇）](https://blog.csdn.net/A_art_xiang/article/details/125538972)

官方文档
----

[redisson官方中文文档](https://github.com/redisson/redisson/wiki/%E7%9B%AE%E5%BD%95)

[Redisson](https://so.csdn.net/so/search?q=Redisson&spm=1001.2101.3001.7020)项目介绍
--------------------------------------------------------------------------------

Redisson是架设在Redis基础上的一个Java驻内存数据网格（In-Memory Data Grid）。充分的利用了Redis键值数据库提供的一系列优势，基于Java实用工具包中常用接口，为使用者提供了一系列具有分布式特性的常用工具类。使得原本作为协调单机多线程并发程序的工具包获得了协调分布式多机多线程并发系统的能力，大大降低了设计和研发大规模分布式系统的难度。同时结合各富特色的分布式服务，更进一步简化了分布式环境中程序相互之间的协作。

Redisson采用了基于NIO的Netty框架，不仅能作为Redis底层驱动客户端，具备提供对Redis各种组态形式的连接功能，对Redis命令能以同步发送、异步形式发送、异步流形式发送或管道形式发送的功能，LUA脚本执行处理，以及处理返回结果的功能，还在此基础上融入了更高级的应用方案，不但将原生的Redis Hash，List，Set，String，Geo，HyperLogLog等数据结构封装为Java里大家最熟悉的映射（Map），列表（List），集（Set），通用对象桶（Object Bucket），地理空间对象桶（Geospatial Bucket），基数估计算法（HyperLogLog）等结构，在这基础上还提供了分布式的多值映射（Multimap），本地缓存映射（LocalCachedMap），有序集（SortedSet），计分排序集（ScoredSortedSet），字典排序集（LexSortedSet），列队（Queue），阻塞队列（Blocking Queue），有界阻塞列队（Bounded Blocking Queue），双端队列（Deque），阻塞双端列队（Blocking Deque），阻塞公平列队（Blocking Fair Queue），延迟列队（Delayed Queue），布隆过滤器（Bloom Filter），原子整长形（AtomicLong），原子双精度浮点数（AtomicDouble），BitSet等Redis原本没有的分布式数据结构。不仅如此，Redisson还实现了Redis文档中提到像分布式锁Lock这样的更高阶应用场景。事实上Redisson并没有不止步于此，在分布式锁的基础上还提供了联锁（MultiLock），读写锁（ReadWriteLock），公平锁（Fair Lock），红锁（RedLock），信号量（Semaphore），可过期性信号量（PermitExpirableSemaphore）和闭锁（CountDownLatch）这些实际当中对多线程高并发应用至关重要的基本部件。正是通过实现基于Redis的高阶应用方案，使Redisson成为构建分布式系统的重要工具。

在提供这些工具的过程当中，Redisson广泛的使用了承载于Redis订阅发布功能之上的分布式话题（Topic）功能。使得即便是在复杂的分布式环境下，Redisson的各个实例仍然具有能够保持相互沟通的能力。在以这为前提下，结合了自身独有的功能完善的分布式工具，Redisson进而提供了像分布式远程服务（Remote Service），分布式执行服务（Executor Service）和分布式调度任务服务（Scheduler Service）这样适用于不同场景的分布式服务。使得Redisson成为了一个基于Redis的Java中间件（Middleware）。

Redisson Node的出现作为驻内存数据网格的重要特性之一，使Redisson能够独立作为一个任务处理节点，以系统服务的方式运行并自动加入Redisson集群，具备集群节点弹性增减的能力。然而在真正意义上让Redisson发展成为一个完整的驻内存数据网格的，还是具有将基本上任何复杂、多维结构的对象都能变为分布式对象的分布式实时对象服务（Live Object Service），以及与之相结合的，在分布式环境中支持跨节点对象引用（Distributed Object Reference）的功能。这些特色功能使Redisson具备了在分布式环境中，为Java程序提供了堆外空间（Off-Heap Memory）储存对象的能力。

Redisson提供了使用Redis的最简单和最便捷的方法。Redisson的宗旨是促进使用者对Redis的关注分离（Separation of Concern），从而让使用者能够将精力更集中地放在处理业务逻辑上。如果您现在正在使用其他的Redis的Java客户端，希望Redis命令和Redisson对象匹配列表 能够帮助您轻松的将现有代码迁徙到Redisson里来。如果目前Redis的应用场景还仅限于作为缓存使用，您也可以将Redisson轻松的整合到像Spring和Hibernate这样的常用框架里。除此外您也可以间接的通过Java缓存标准规范JCache API (JSR-107)接口来使用Redisson。

Redisson生而具有的高性能，分布式特性和丰富的结构等特点恰巧与Tomcat这类服务程序对会话管理器（Session Manager）的要求相吻合。利用这样的特点，Redisson专门为Tomcat提供了会话管理器（Tomcat Session Manager）。

在此不难看出，Redisson同其他Redis Java客户端有着很大的区别，相比之下其他客户端提供的功能还仅仅停留在作为数据库驱动层面上，比如仅针对Redis提供连接方式，发送命令和处理返回结果等。像上面这些高层次的应用则只能依靠使用者自行实现。

Redisson支持Redis 2.8以上版本，支持Java1.6+以上版本。

一、概述
----

Redisson是一个在Redis的基础上实现的Java驻内存数据网格（In-Memory Data Grid）。它不仅提供了一系列的分布式的Java常用对象，还提供了许多分布式服务。其中包括(BitSet, Set, Multimap, SortedSet, Map, List, Queue, BlockingQueue, Deque, BlockingDeque, Semaphore, Lock, AtomicLong, CountDownLatch, Publish / Subscribe, Bloom filter, Remote service, Spring cache, Executor service, Live Object service, Scheduler service) Redisson提供了使用Redis的最简单和最便捷的方法。Redisson的宗旨是促进使用者对Redis的关注分离（Separation of Concern），从而让使用者能够将精力更集中地放在处理业务逻辑上。

关于Redisson项目的详细介绍可以在官方网站找到。

每个Redis服务实例都能管理多达1TB的内存。

能够完美的在云计算环境里使用，并且支持AWS ElastiCache主备版，AWS ElastiCache集群版，Azure Redis Cache和阿里云（Aliyun）的云数据库Redis版

以下是Redisson的结构：

Redisson作为独立节点 可以用于独立执行其他节点发布到分布式执行服务 和 分布式调度任务服务 里的远程任务。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/4a8e3b77e40446d5abfbb5d6eff21dde.png)  
如果你现在正在使用其他的Redis的Java客户端，那么Redis命令和Redisson对象匹配列表 能够帮助你轻松的将现有代码迁徙到Redisson框架里来。

Redisson底层采用的是Netty 框架。支持Redis 2.8以上版本，支持Java1.6+以上版本。

欢迎试用高性能Redisson PRO版。

二、配置方法
------

引入pom：

```xml
<dependency>
    <groupId>org.redisson</groupId>
    <artifactId>redisson</artifactId>
    <version>3.12.3</version>
</dependency>
```

### 2.1. 程序化配置方法

Redisson程序化的配置方法是通过构建Config对象实例来实现的。例如：

```java
Config config = new Config();
config.setTransportMode(TransportMode.EPOLL); // 默认是NIO的方式
config.useClusterServers()
      //可以用"rediss://"来启用SSL连接，前缀必须是redis:// or rediss://
      .addNodeAddress("redis://127.0.0.1:7181");
```

### 2.2. 文件方式配置

Redisson既可以通过用户提供的YAML格式的文本文件来配置

#### 2.2.1 通过YAML格式配置

Redisson的配置文件可以是或YAML格式。 也通过调用config.fromYAML方法并指定一个File实例来实现读取YAML格式的配置：

```java
Config config = Config.fromYAML(new File("config-file.yaml"));
RedissonClient redisson = Redisson.create(config);
```

调用config.toYAML方法可以将一个Config配置实例序列化为一个含有YAML数据类型的字符串：

```java
Config config = new Config();
// ... 省略许多其他的设置
String jsonFormat = config.toYAML();
```

### 2.3. 常用设置

以下是关于org.redisson.Config类的配置参数，它适用于所有Redis组态模式（单机，集群和哨兵）

**codec（编码）**  
默认值: org.redisson.codec.JsonJacksonCodec

Redisson的对象编码类是用于将对象进行序列化和反序列化，以实现对该对象在Redis里的读取和存储。Redisson提供了以下几种的对象编码应用，以供大家选择：

| 编码类名称 | 说明 |
| --- | --- |
| org.redisson.codec.JsonJacksonCodec | Jackson JSON 编码 默认编码 |
| org.redisson.codec.AvroJacksonCodec | Avro 一个二进制的JSON编码 |
| org.redisson.codec.SmileJacksonCodec | Smile 另一个二进制的JSON编码 |
| org.redisson.codec.CborJacksonCodec | CBOR 又一个二进制的JSON编码 |
| org.redisson.codec.MsgPackJacksonCodec | MsgPack 再来一个二进制的JSON编码 |
| org.redisson.codec.IonJacksonCodec | Amazon Ion 亚马逊的Ion编码，格式与JSON类似 |
| org.redisson.codec.KryoCodec | Kryo 二进制对象序列化编码 |
| org.redisson.codec.SerializationCodec | JDK序列化编码 |
| org.redisson.codec.FstCodec | FST 10倍于JDK序列化性能而且100%兼容的编码 |
| org.redisson.codec.LZ4Codec | LZ4 压缩型序列化对象编码 |
| org.redisson.codec.SnappyCodec | Snappy 另一个压缩型序列化对象编码 |
| org.redisson.client.codec.JsonJacksonMapCodec | 基于Jackson的映射类使用的编码。可用于避免序列化类的信息，以及用于解决使用byte\[\]遇到的问题。 |
| org.redisson.client.codec.StringCodec | 纯字符串编码（无转换） |
| org.redisson.client.codec.LongCodec | 纯整长型数字编码（无转换） |
| org.redisson.client.codec.ByteArrayCodec | 字节数组编码 |
| org.redisson.codec.CompositeCodec | 用来组合多种不同编码在一起 |

**threads（线程池数量）**  
默认值: 当前处理核数量 \* 2

这个线程池数量被所有RTopic对象监听器，RRemoteService调用者和RExecutorService任务共同共享。

**nettyThreads （Netty线程池数量）**  
默认值: 当前处理核数量 \* 2

这个线程池数量是在一个Redisson实例内，被其创建的所有分布式数据类型和服务，以及底层客户端所一同共享的线程池里保存的线程数量。  
**executor（线程池）**  
单独提供一个用来执行所有RTopic对象监听器，RRemoteService调用者和RExecutorService任务的线程池（ExecutorService）实例。

**eventLoopGroup**  
用于特别指定一个EventLoopGroup. EventLoopGroup是用来处理所有通过Netty与Redis服务之间的连接发送和接受的消息。每一个Redisson都会在默认情况下自己创建管理一个EventLoopGroup实例。因此，如果在同一个JVM里面可能存在多个Redisson实例的情况下，采取这个配置实现多个Redisson实例共享一个EventLoopGroup的目的。

只有io.netty.channel.epoll.EpollEventLoopGroup或io.netty.channel.nio.NioEventLoopGroup才是允许的类型。

**transportMode（传输模式）**  
默认值：TransportMode.NIO

可选参数：  
TransportMode.NIO,  
TransportMode.EPOLL - 需要依赖里有netty-transport-native-epoll包（Linux）  
TransportMode.KQUEUE - 需要依赖里有 netty-transport-native-kqueue包（macOS）

**lockWatchdogTimeout（监控锁的看门狗超时，单位：毫秒）**  
默认值：30000

监控锁的看门狗超时时间单位为毫秒。该参数只适用于分布式锁的加锁请求中未明确使用leaseTimeout参数的情况。如果该看门口未使用lockWatchdogTimeout去重新调整一个分布式锁的lockWatchdogTimeout超时，那么这个锁将变为失效状态。这个参数可以用来避免由Redisson客户端节点宕机或其他原因造成死锁的情况。

**keepPubSubOrder（保持订阅发布顺序）**  
默认值：true

通过该参数来修改是否按订阅发布消息的接收顺序出来消息，如果选否将对消息实行并行处理，该参数只适用于订阅发布消息的情况。

**performanceMode（高性能模式）**  
默认值：HIGHER\_THROUGHPUT

用来指定高性能引擎的行为。由于该变量值的选用与使用场景息息相关（NORMAL除外）我们建议对每个参数值都进行尝试。

该参数仅限于Redisson PRO版本。

可选模式：  
HIGHER\_THROUGHPUT - 将高性能引擎切换到 高通量 模式。  
LOWER\_LATENCY\_AUTO - 将高性能引擎切换到 低延时 模式并自动探测最佳设定。  
LOWER\_LATENCY\_MODE\_1 - 将高性能引擎切换到 低延时 模式并调整到预设模式1。  
LOWER\_LATENCY\_MODE\_2 - 将高性能引擎切换到 低延时 模式并调整到预设模式2。  
NORMAL - 将高性能引擎切换到 普通 模式

### 2.4. 集群模式

集群模式除了适用于Redis集群环境，也适用于任何云计算服务商提供的集群模式，例如AWS ElastiCache集群版、Azure Redis Cache和阿里云（Aliyun）的云数据库Redis版。

程序化配置集群的用法:

```java
Config config = new Config();
config.useClusterServers()
    .setScanInterval(2000) // 集群状态扫描间隔时间，单位是毫秒
    //可以用"rediss://"来启用SSL连接，前缀必须是redis:// or rediss://
    // 以下两种写法效果是一样的
    .addNodeAddress("redis://127.0.0.1:7000", "redis://127.0.0.1:7001")
    .addNodeAddress("redis://127.0.0.1:7002");

RedissonClient redisson = Redisson.create(config);
```

#### 2.4.1. 集群设置

介绍配置Redis集群组态的文档在[这里](http://www.redis.cn/topics/cluster-tutorial.html)。 Redis集群组态的最低要求是必须有三个主节点。Redisson的集群模式的使用方法如下：

ClusterServersConfig clusterConfig = config.useClusterServers();

ClusterServersConfig 类的设置参数如下：

**nodeAddresses（添加节点地址）**  
可以通过host:port的格式来添加Redis集群节点的地址。多个节点可以一次性批量添加。

**scanInterval（集群扫描间隔时间）**  
默认值： 1000

对Redis集群节点状态扫描的时间间隔。单位是毫秒。

**slots（分片数量）**  
默认值： 231 用于指定数据[分片](https://so.csdn.net/so/search?q=%E5%88%86%E7%89%87&spm=1001.2101.3001.7020)过程中的分片数量。支持数据分片/框架结构有：集（Set）、映射（Map）、BitSet、Bloom filter, Spring Cache和Hibernate Cache等.

**readMode（读取操作的负载均衡模式）**  
默认值： SLAVE（只在从服务节点里读取）

注：在从服务节点里读取的数据说明已经至少有两个节点保存了该数据，确保了数据的高可用性。

设置读取操作选择节点的模式。 可用值为： SLAVE - 只在从服务节点里读取。 MASTER - 只在主服务节点里读取。 MASTER\_SLAVE - 在主从服务节点里都可以读取。

**subscriptionMode（订阅操作的负载均衡模式）**  
默认值：SLAVE（只在从服务节点里订阅）

设置订阅操作选择节点的模式。 可用值为： SLAVE - 只在从服务节点里订阅。 MASTER - 只在主服务节点里订阅。

**loadBalancer（负载均衡算法类的选择）**  
默认值： org.redisson.connection.balancer.RoundRobinLoadBalancer

在多Redis服务节点的环境里，可以选用以下几种负载均衡方式选择一个节点： org.redisson.connection.balancer.WeightedRoundRobinBalancer - 权重轮询调度算法 org.redisson.connection.balancer.RoundRobinLoadBalancer - 轮询调度算法  
org.redisson.connection.balancer.RandomLoadBalancer - 随机调度算法

**subscriptionConnectionMinimumIdleSize（从节点发布和订阅连接的最小空闲连接数）**  
默认值：1

多从节点的环境里，每个 从服务节点里用于发布和订阅连接的最小保持连接数（长连接）。Redisson内部经常通过发布和订阅来实现许多功能。长期保持一定数量的发布订阅连接是必须的。

**subscriptionConnectionPoolSize（从节点发布和订阅连接池大小）**  
默认值：50

多从节点的环境里，每个 从服务节点里用于发布和订阅连接的连接池最大容量。连接池的连接数量自动弹性伸缩。

**slaveConnectionMinimumIdleSize（从节点最小空闲连接数）**  
默认值：32

多从节点的环境里，每个 从服务节点里用于普通操作（非 发布和订阅）的最小保持连接数（长连接）。长期保持一定数量的连接有利于提高瞬时读取反映速度。

**slaveConnectionPoolSize（从节点连接池大小）**  
默认值：64

多从节点的环境里，每个 从服务节点里用于普通操作（非 发布和订阅）连接的连接池最大容量。连接池的连接数量自动弹性伸缩。

**masterConnectionMinimumIdleSize（主节点最小空闲连接数）**  
默认值：32

多从节点的环境里，每个 主节点的最小保持连接数（长连接）。长期保持一定数量的连接有利于提高瞬时写入反应速度。

**masterConnectionPoolSize（主节点连接池大小）**  
默认值：64

主节点的连接池最大容量。连接池的连接数量自动弹性伸缩。

**idleConnectionTimeout（连接空闲超时，单位：毫秒）**  
默认值：10000

如果当前连接池里的连接数量超过了最小空闲连接数，而同时有连接空闲时间超过了该数值，那么这些连接将会自动被关闭，并从连接池里去掉。时间单位是毫秒。

**connectTimeout（连接超时，单位：毫秒）**  
默认值：10000

同任何节点建立连接时的等待超时。时间单位是毫秒。

**timeout（命令等待超时，单位：毫秒）**  
默认值：3000

等待节点回复命令的时间。该时间从命令发送成功时开始计时。

**retryAttempts（命令失败重试次数）**  
默认值：3

如果尝试达到 retryAttempts（命令失败重试次数） 仍然不能将命令发送至某个指定的节点时，将抛出错误。如果尝试在此限制之内发送成功，则开始启用 timeout（命令等待超时） 计时。

**retryInterval（命令重试发送时间间隔，单位：毫秒）**  
默认值：1500

在某个节点执行相同或不同命令时，连续 失败 failedAttempts（执行失败最大次数） 时，该节点将被从可用节点列表里清除，直到 reconnectionTimeout（重新连接时间间隔） 超时以后再次尝试。

**password（密码）**  
默认值：null

用于节点身份验证的密码。

**subscriptionsPerConnection（单个连接最大订阅数量）**  
默认值：5

每个连接的最大订阅数量。

**clientName（客户端名称）**  
默认值：null

在Redis节点里显示的客户端名称。

**sslEnableEndpointIdentification（启用SSL终端识别）**  
默认值：true

开启SSL终端识别能力。

**sslProvider（SSL实现方式）**  
默认值：JDK

确定采用哪种方式（JDK或OPENSSL）来实现SSL连接。

**sslTruststore（SSL信任证书库路径）**  
默认值：null

指定SSL信任证书库的路径。

**sslTruststorePassword（SSL信任证书库密码）**  
默认值：null

指定SSL信任证书库的密码。

**sslKeystore（SSL钥匙库路径）**  
默认值：null

指定SSL钥匙库的路径。

**sslKeystorePassword（SSL钥匙库密码）**  
默认值：null

指定SSL钥匙库的密码。

#### 2.4.2. 通过YAML文件配置集群模式

配置集群模式可以通过指定一个YAML格式的文件来实现。以下是YAML格式的配置文件样本。文件中的字段名称必须与ClusterServersConfig和Config对象里的字段名称相符。

```javascript
---
clusterServersConfig:
  idleConnectionTimeout: 10000
  connectTimeout: 10000
  timeout: 3000
  retryAttempts: 3
  retryInterval: 1500
  password: null
  subscriptionsPerConnection: 5
  clientName: null
  loadBalancer: !<org.redisson.connection.balancer.RoundRobinLoadBalancer> {}
  slaveSubscriptionConnectionMinimumIdleSize: 1
  slaveSubscriptionConnectionPoolSize: 50
  slaveConnectionMinimumIdleSize: 32
  slaveConnectionPoolSize: 64
  masterConnectionMinimumIdleSize: 32
  masterConnectionPoolSize: 64
  readMode: "SLAVE"
  nodeAddresses:
  - "redis://127.0.0.1:7004"
  - "redis://127.0.0.1:7001"
  - "redis://127.0.0.1:7000"
  scanInterval: 1000
threads: 0
nettyThreads: 0
codec: !<org.redisson.codec.JsonJacksonCodec> {}
"transportMode":"NIO"
```

### 2.5. 云托管模式

云托管模式适用于任何由云计算运营商提供的Redis云服务，包括亚马逊云的AWS ElastiCache、微软云的Azure Redis 缓存和阿里云（Aliyun）的云数据库Redis版

程序化配置云托管模式的方法如下：

```java
Config config = new Config();
config.useReplicatedServers()
    .setScanInterval(2000) // 主节点变化扫描间隔时间
    //可以用"rediss://"来启用SSL连接
    .addNodeAddress("redis://127.0.0.1:7000", "redis://127.0.0.1:7001")
    .addNodeAddress("redis://127.0.0.1:7002");

RedissonClient redisson = Redisson.create(config);
```

#### 2.5.1. 云托管模式设置

Redisson的云托管模式的使用方法如下： ReplicatedServersConfig replicatedConfig = config.useReplicatedServers();

ReplicatedServersConfig 类的设置参数如下：

**nodeAddresses（节点地址）**  
可以通过host:port的格式来指定云托管模式的多个Redis集群节点的地址。多个节点可以一次性批量添加。所有的主从节点必须在配置阶段全部体现出来。

**scanInterval（主节点变化扫描间隔时间）**  
默认值： 1000

对主节点变化节点状态扫描的时间间隔。单位是毫秒。

**loadBalancer（负载均衡算法类的选择）**  
默认值： org.redisson.connection.balancer.RoundRobinLoadBalancer

在使用多个Elasticache Redis服务节点的环境里，可以选用以下几种负载均衡方式选择一个节点： org.redisson.connection.balancer.WeightedRoundRobinBalancer - 权重轮询调度算法 org.redisson.connection.balancer.RoundRobinLoadBalancer - 轮询调度算法 org.redisson.connection.balancer.RandomLoadBalancer - 随机调度算法

**dnsMonitoringInterval（DNS监控间隔，单位：毫秒）**  
默认值：5000

用来指定检查节点DNS变化的时间间隔。使用的时候应该确保JVM里的DNS数据的缓存时间保持在足够低的范围才有意义。用-1来禁用该功能。

**subscriptionConnectionMinimumIdleSize（从节点发布和订阅连接的最小空闲连接数）**  
默认值：1

多从节点的环境里，每个 从服务节点里用于发布和订阅连接的最小保持连接数（长连接）。Redisson内部经常通过发布和订阅来实现许多功能。长期保持一定数量的发布订阅连接是必须的。

**subscriptionConnectionPoolSize（从节点发布和订阅连接池大小）**  
默认值：50

多从节点的环境里，每个 从服务节点里用于发布和订阅连接的连接池最大容量。连接池的连接数量自动弹性伸缩。

**slaveConnectionMinimumIdleSize（从节点最小空闲连接数）**  
默认值：32

多从节点的环境里，每个 从服务节点里用于普通操作（非 发布和订阅）的最小保持连接数（长连接）。长期保持一定数量的连接有利于提高瞬时读取反映速度。

**slaveConnectionPoolSize（从节点连接池大小）**  
默认值：64

多从节点的环境里，每个 从服务节点里用于普通操作（非 发布和订阅）连接的连接池最大容量。连接池的连接数量自动弹性伸缩。

**masterConnectionMinimumIdleSize（主节点最小空闲连接数）**  
默认值：32

多从节点的环境里，每个 主节点的最小保持连接数（长连接）。长期保持一定数量的连接有利于提高瞬时写入反应速度。

**masterConnectionPoolSize（主节点连接池大小）**  
默认值：64

主节点的连接池最大容量。连接池的连接数量自动弹性伸缩。

**idleConnectionTimeout（连接空闲超时，单位：毫秒）**  
默认值：10000

如果当前连接池里的连接数量超过了最小空闲连接数，而同时有连接空闲时间超过了该数值，那么这些连接将会自动被关闭，并从连接池里去掉。时间单位是毫秒。

**readMode（读取操作的负载均衡模式）**  
默认值： SLAVE（只在从服务节点里读取）

注：在从服务节点里读取的数据说明已经至少有两个节点保存了该数据，确保了数据的高可用性。

设置读取操作选择节点的模式。 可用值为： SLAVE - 只在从服务节点里读取。 MASTER - 只在主服务节点里读取。 MASTER\_SLAVE - 在主从服务节点里都可以读取。

**subscriptionMode（订阅操作的负载均衡模式）**  
默认值：SLAVE（只在从服务节点里订阅）

设置订阅操作选择节点的模式。 可用值为： SLAVE - 只在从服务节点里订阅。 MASTER - 只在主服务节点里订阅。

**connectTimeout（连接超时，单位：毫秒）**  
默认值：10000

同任何节点建立连接时的等待超时。时间单位是毫秒。

**timeout（命令等待超时，单位：毫秒）**  
默认值：3000

等待节点回复命令的时间。该时间从命令发送成功时开始计时。

**retryAttempts（命令失败重试次数）**  
默认值：3

如果尝试达到 retryAttempts（命令失败重试次数） 仍然不能将命令发送至某个指定的节点时，将抛出错误。如果尝试在此限制之内发送成功，则开始启用 timeout（命令等待超时） 计时。

**retryInterval（命令重试发送时间间隔，单位：毫秒）**  
默认值：1500

在某个节点执行相同或不同命令时，连续 失败 failedAttempts（执行失败最大次数） 时，该节点将被从可用节点列表里清除，直到 reconnectionTimeout（重新连接时间间隔） 超时以后再次尝试。

**database（数据库编号）**  
默认值：0

尝试连接的数据库编号。

**password（密码）**  
默认值：null

用于节点身份验证的密码。

**subscriptionsPerConnection（单个连接最大订阅数量）**  
默认值：5

每个连接的最大订阅数量。

**clientName（客户端名称）**  
默认值：null

在Redis节点里显示的客户端名称。

**sslEnableEndpointIdentification（启用SSL终端识别）**  
默认值：true

开启SSL终端识别能力。

**sslProvider（SSL实现方式）**  
默认值：JDK

确定采用哪种方式（JDK或OPENSSL）来实现SSL连接。

**sslTruststore（SSL信任证书库路径）**  
默认值：null

指定SSL信任证书库的路径。

**sslTruststorePassword（SSL信任证书库密码）**  
默认值：null

指定SSL信任证书库的密码。

**sslKeystore（SSL钥匙库路径）**  
默认值：null

指定SSL钥匙库的路径。

**sslKeystorePassword（SSL钥匙库密码）**  
默认值：null

指定SSL钥匙库的密码。

#### 2.5.2. 通过YAML文件配置集群模式

配置云托管模式可以通过指定一个YAML格式的文件来实现。以下是YAML格式的配置文件样本。文件中的字段名称必须与ReplicatedServersConfig 和Config对象里的字段名称相符。

```java
---
replicatedServersConfig:
  idleConnectionTimeout: 10000
  connectTimeout: 10000
  timeout: 3000
  retryAttempts: 3
  retryInterval: 1500
  password: null
  subscriptionsPerConnection: 5
  clientName: null
  loadBalancer: !<org.redisson.connection.balancer.RoundRobinLoadBalancer> {}
  slaveSubscriptionConnectionMinimumIdleSize: 1
  slaveSubscriptionConnectionPoolSize: 50
  slaveConnectionMinimumIdleSize: 32
  slaveConnectionPoolSize: 64
  masterConnectionMinimumIdleSize: 32
  masterConnectionPoolSize: 64
  readMode: "SLAVE"
  nodeAddresses:
  - "redis://127.0.0.1:2812"
  - "redis://127.0.0.1:2815"
  - "redis://127.0.0.1:2813"
  scanInterval: 1000
threads: 0
nettyThreads: 0
codec: !<org.redisson.codec.JsonJacksonCodec> {}
"transportMode":"NIO"
```

### 2.6. 单Redis节点模式

程序化配置方法：

```java
// 默认连接地址 127.0.0.1:6379
RedissonClient redisson = Redisson.create();

Config config = new Config();
config.useSingleServer().setAddress("redis://myredisserver:6379");
RedissonClient redisson = Redisson.create(config);
```

#### 2.6.1. 单节点设置

Redis程序的配置和架设文档在[这里](http://www.redis.cn/topics/config.html)。Redisson的单Redis节点模式的使用方法如下： SingleServerConfig singleConfig = config.useSingleServer();

SingleServerConfig 类的设置参数如下：

**address（节点地址）**  
可以通过host:port的格式来指定节点地址。

**subscriptionConnectionMinimumIdleSize（发布和订阅连接的最小空闲连接数）**  
默认值：1

用于发布和订阅连接的最小保持连接数（长连接）。Redisson内部经常通过发布和订阅来实现许多功能。长期保持一定数量的发布订阅连接是必须的。

**subscriptionConnectionPoolSize（发布和订阅连接池大小）**  
默认值：50

用于发布和订阅连接的连接池最大容量。连接池的连接数量自动弹性伸缩。

**connectionMinimumIdleSize（最小空闲连接数）**  
默认值：32

最小保持连接数（长连接）。长期保持一定数量的连接有利于提高瞬时写入反应速度。

**connectionPoolSize（连接池大小）**  
默认值：64

在启用该功能以后，Redisson将会监测DNS的变化情况。

**dnsMonitoringInterval（DNS监测时间间隔，单位：毫秒）**  
默认值：5000

监测DNS的变化情况的时间间隔。

**idleConnectionTimeout（连接空闲超时，单位：毫秒）**  
默认值：10000

如果当前连接池里的连接数量超过了最小空闲连接数，而同时有连接空闲时间超过了该数值，那么这些连接将会自动被关闭，并从连接池里去掉。时间单位是毫秒。

**connectTimeout（连接超时，单位：毫秒）**  
默认值：10000

同节点建立连接时的等待超时。时间单位是毫秒。

**timeout（命令等待超时，单位：毫秒）**  
默认值：3000

等待节点回复命令的时间。该时间从命令发送成功时开始计时。

**retryAttempts（命令失败重试次数）**  
默认值：3

如果尝试达到 retryAttempts（命令失败重试次数） 仍然不能将命令发送至某个指定的节点时，将抛出错误。如果尝试在此限制之内发送成功，则开始启用 timeout（命令等待超时） 计时。

**retryInterval（命令重试发送时间间隔，单位：毫秒）**  
默认值：1500

在某个节点执行相同或不同命令时，连续 失败 failedAttempts（执行失败最大次数） 时，该节点将被从可用节点列表里清除，直到 reconnectionTimeout（重新连接时间间隔） 超时以后再次尝试。

**database（数据库编号）**  
默认值：0

尝试连接的数据库编号。

**password（密码）**  
默认值：null

用于节点身份验证的密码。

**subscriptionsPerConnection（单个连接最大订阅数量）**  
默认值：5

每个连接的最大订阅数量。

**clientName（客户端名称）**  
默认值：null

在Redis节点里显示的客户端名称。

**sslEnableEndpointIdentification（启用SSL终端识别）**  
默认值：true

开启SSL终端识别能力。

**sslProvider（SSL实现方式）**  
默认值：JDK

确定采用哪种方式（JDK或OPENSSL）来实现SSL连接。

**sslTruststore（SSL信任证书库路径）**  
默认值：null

指定SSL信任证书库的路径。

**sslTruststorePassword（SSL信任证书库密码）**  
默认值：null

指定SSL信任证书库的密码。

**sslKeystore（SSL钥匙库路径）**  
默认值：null

指定SSL钥匙库的路径。

**sslKeystorePassword（SSL钥匙库密码）**  
默认值：null

指定SSL钥匙库的密码。

#### 2.6.2. 通过YAML文件配置集群模式

配置单节点模式可以通过指定一个YAML格式的文件来实现。以下是YAML格式的配置文件样本。文件中的字段名称必须与SingleServerConfig和Config对象里的字段名称相符。

```java
---
singleServerConfig:
  idleConnectionTimeout: 10000
  connectTimeout: 10000
  timeout: 3000
  retryAttempts: 3
  retryInterval: 1500
  password: null
  subscriptionsPerConnection: 5
  clientName: null
  address: "redis://127.0.0.1:6379"
  subscriptionConnectionMinimumIdleSize: 1
  subscriptionConnectionPoolSize: 50
  connectionMinimumIdleSize: 32
  connectionPoolSize: 64
  database: 0
  dnsMonitoringInterval: 5000
threads: 0
nettyThreads: 0
codec: !<org.redisson.codec.JsonJacksonCodec> {}
"transportMode":"NIO"
```

### 2.7. [哨兵模式](https://so.csdn.net/so/search?q=%E5%93%A8%E5%85%B5%E6%A8%A1%E5%BC%8F&spm=1001.2101.3001.7020)

程序化配置哨兵模式的方法如下：

```java
Config config = new Config();
config.useSentinelServers()
    .setMasterName("mymaster")
    //可以用"rediss://"来启用SSL连接
    .addSentinelAddress("redis://127.0.0.1:26389", "redis://127.0.0.1:26379")
    .addSentinelAddress("redis://127.0.0.1:26319");

RedissonClient redisson = Redisson.create(config);
```

#### 2.7.1. 哨兵模式设置

配置Redis哨兵服务的官方文档在[这里](http://redis.cn/topics/sentinel.html)。Redisson的哨兵模式的使用方法如下： SentinelServersConfig sentinelConfig = config.useSentinelServers();

SentinelServersConfig 类的设置参数如下：

**dnsMonitoringInterval（DNS监控间隔，单位：毫秒）**  
默认值：5000

用来指定检查节点DNS变化的时间间隔。使用的时候应该确保JVM里的DNS数据的缓存时间保持在足够低的范围才有意义。用-1来禁用该功能。

**masterName（主服务器的名称）**  
主服务器的名称是哨兵进程中用来监测主从服务切换情况的。

**addSentinelAddress（添加哨兵节点地址）**  
可以通过host:port的格式来指定哨兵节点的地址。多个节点可以一次性批量添加。

**readMode（读取操作的负载均衡模式）**  
默认值： SLAVE（只在从服务节点里读取）

注：在从服务节点里读取的数据说明已经至少有两个节点保存了该数据，确保了数据的高可用性。

设置读取操作选择节点的模式。 可用值为： SLAVE - 只在从服务节点里读取。 MASTER - 只在主服务节点里读取。 MASTER\_SLAVE - 在主从服务节点里都可以读取。

**subscriptionMode（订阅操作的负载均衡模式）**  
默认值：SLAVE（只在从服务节点里订阅）

设置订阅操作选择节点的模式。 可用值为： SLAVE - 只在从服务节点里订阅。 MASTER - 只在主服务节点里订阅。

**loadBalancer（负载均衡算法类的选择）**  
默认值： org.redisson.connection.balancer.RoundRobinLoadBalancer

在使用多个Redis服务节点的环境里，可以选用以下几种负载均衡方式选择一个节点： org.redisson.connection.balancer.WeightedRoundRobinBalancer - 权重轮询调度算法 org.redisson.connection.balancer.RoundRobinLoadBalancer - 轮询调度算法 org.redisson.connection.balancer.RandomLoadBalancer - 随机调度算法

**subscriptionConnectionMinimumIdleSize（从节点发布和订阅连接的最小空闲连接数）**  
默认值：1

多从节点的环境里，每个 从服务节点里用于发布和订阅连接的最小保持连接数（长连接）。Redisson内部经常通过发布和订阅来实现许多功能。长期保持一定数量的发布订阅连接是必须的。

**subscriptionConnectionPoolSize（从节点发布和订阅连接池大小）**  
默认值：50

多从节点的环境里，每个 从服务节点里用于发布和订阅连接的连接池最大容量。连接池的连接数量自动弹性伸缩。

**slaveConnectionMinimumIdleSize（从节点最小空闲连接数）**  
默认值：32

多从节点的环境里，每个 从服务节点里用于普通操作（非 发布和订阅）的最小保持连接数（长连接）。长期保持一定数量的连接有利于提高瞬时读取反映速度。

**slaveConnectionPoolSize（从节点连接池大小）**  
默认值：64

多从节点的环境里，每个 从服务节点里用于普通操作（非 发布和订阅）连接的连接池最大容量。连接池的连接数量自动弹性伸缩。

**masterConnectionMinimumIdleSize（主节点最小空闲连接数）**  
默认值：32

多从节点的环境里，每个 主节点的最小保持连接数（长连接）。长期保持一定数量的连接有利于提高瞬时写入反应速度。

**masterConnectionPoolSize（主节点连接池大小）**  
默认值：64

主节点的连接池最大容量。连接池的连接数量自动弹性伸缩。

**idleConnectionTimeout（连接空闲超时，单位：毫秒）**  
默认值：10000

如果当前连接池里的连接数量超过了最小空闲连接数，而同时有连接空闲时间超过了该数值，那么这些连接将会自动被关闭，并从连接池里去掉。时间单位是毫秒。

**connectTimeout（连接超时，单位：毫秒）**  
默认值：10000

同任何节点建立连接时的等待超时。时间单位是毫秒。

**timeout（命令等待超时，单位：毫秒）**  
默认值：3000

等待节点回复命令的时间。该时间从命令发送成功时开始计时。

**retryAttempts（命令失败重试次数）**  
默认值：3

如果尝试达到 retryAttempts（命令失败重试次数） 仍然不能将命令发送至某个指定的节点时，将抛出错误。如果尝试在此限制之内发送成功，则开始启用 timeout（命令等待超时） 计时。

**retryInterval（命令重试发送时间间隔，单位：毫秒）**  
默认值：1500

在某个节点执行相同或不同命令时，连续 失败 failedAttempts（执行失败最大次数） 时，该节点将被从可用节点列表里清除，直到 reconnectionTimeout（重新连接时间间隔） 超时以后再次尝试。

**database（数据库编号）**  
默认值：0

尝试连接的数据库编号。

**password（密码）**  
默认值：null

用于节点身份验证的密码。

**subscriptionsPerConnection（单个连接最大订阅数量）**  
默认值：5

每个连接的最大订阅数量。

**clientName（客户端名称）**  
默认值：null

在Redis节点里显示的客户端名称。

**sslEnableEndpointIdentification（启用SSL终端识别）**  
默认值：true

开启SSL终端识别能力。

**sslProvider（SSL实现方式）**  
默认值：JDK

确定采用哪种方式（JDK或OPENSSL）来实现SSL连接。

**sslTruststore（SSL信任证书库路径）**  
默认值：null

指定SSL信任证书库的路径。

**sslTruststorePassword（SSL信任证书库密码）**  
默认值：null

指定SSL信任证书库的密码。

**sslKeystore（SSL钥匙库路径）**  
默认值：null

指定SSL钥匙库的路径。

**sslKeystorePassword（SSL钥匙库密码）**  
默认值：null

指定SSL钥匙库的密码。

#### 2.7.2. 通过YAML文件配置集群模式

配置哨兵模式可以通过指定一个YAML格式的文件来实现。以下是YAML格式的配置文件样本。文件中的字段名称必须与SentinelServersConfig和Config对象里的字段名称相符。

```java
---
sentinelServersConfig:
  idleConnectionTimeout: 10000
  connectTimeout: 10000
  timeout: 3000
  retryAttempts: 3
  retryInterval: 1500
  password: null
  subscriptionsPerConnection: 5
  clientName: null
  loadBalancer: !<org.redisson.connection.balancer.RoundRobinLoadBalancer> {}
  slaveSubscriptionConnectionMinimumIdleSize: 1
  slaveSubscriptionConnectionPoolSize: 50
  slaveConnectionMinimumIdleSize: 32
  slaveConnectionPoolSize: 64
  masterConnectionMinimumIdleSize: 32
  masterConnectionPoolSize: 64
  readMode: "SLAVE"
  sentinelAddresses:
  - "redis://127.0.0.1:26379"
  - "redis://127.0.0.1:26389"
  masterName: "mymaster"
  database: 0
threads: 0
nettyThreads: 0
codec: !<org.redisson.codec.JsonJacksonCodec> {}
"transportMode":"NIO"
```

### 2.8. 主从模式

程序化配置主从模式的用法:

```java
Config config = new Config();
config.useMasterSlaveServers()
    //可以用"rediss://"来启用SSL连接
    .setMasterAddress("redis://127.0.0.1:6379")
    .addSlaveAddress("redis://127.0.0.1:6389", "redis://127.0.0.1:6332", "redis://127.0.0.1:6419")
    .addSlaveAddress("redis://127.0.0.1:6399");

RedissonClient redisson = Redisson.create(config);
```

#### 2.8.1. 主从模式设置

介绍配置Redis主从服务组态的文档在[这里](http://redis.cn/topics/replication.html). Redisson的主从模式的使用方法如下： MasterSlaveServersConfig masterSlaveConfig = config.useMasterSlaveServers();

MasterSlaveServersConfig 类的设置参数如下：

**dnsMonitoringInterval（DNS监控间隔，单位：毫秒）**  
默认值：5000

用来指定检查节点DNS变化的时间间隔。使用的时候应该确保JVM里的DNS数据的缓存时间保持在足够低的范围才有意义。用-1来禁用该功能。

**masterAddress（主节点地址）**  
可以通过host:port的格式来指定主节点地址。

**addSlaveAddress（添加从主节点地址）**  
可以通过host:port的格式来指定从节点的地址。多个节点可以一次性批量添加。

**readMode（读取操作的负载均衡模式）**  
默认值： SLAVE（只在从服务节点里读取）

注：在从服务节点里读取的数据说明已经至少有两个节点保存了该数据，确保了数据的高可用性。

设置读取操作选择节点的模式。 可用值为： SLAVE - 只在从服务节点里读取。 MASTER - 只在主服务节点里读取。 MASTER\_SLAVE - 在主从服务节点里都可以读取。

**subscriptionMode（订阅操作的负载均衡模式）**  
默认值：SLAVE（只在从服务节点里订阅）

设置订阅操作选择节点的模式。 可用值为： SLAVE - 只在从服务节点里订阅。 MASTER - 只在主服务节点里订阅。

**loadBalancer（负载均衡算法类的选择）**  
默认值： org.redisson.connection.balancer.RoundRobinLoadBalancer

在使用多个Redis服务节点的环境里，可以选用以下几种负载均衡方式选择一个节点： org.redisson.connection.balancer.WeightedRoundRobinBalancer - 权重轮询调度算法 org.redisson.connection.balancer.RoundRobinLoadBalancer - 轮询调度算法 org.redisson.connection.balancer.RandomLoadBalancer - 随机调度算法

**subscriptionConnectionMinimumIdleSize（从节点发布和订阅连接的最小空闲连接数）**  
默认值：1

多从节点的环境里，每个 从服务节点里用于发布和订阅连接的最小保持连接数（长连接）。Redisson内部经常通过发布和订阅来实现许多功能。长期保持一定数量的发布订阅连接是必须的。

**subscriptionConnectionPoolSize（从节点发布和订阅连接池大小）**  
默认值：50

多从节点的环境里，每个 从服务节点里用于发布和订阅连接的连接池最大容量。连接池的连接数量自动弹性伸缩。

**slaveConnectionMinimumIdleSize（从节点最小空闲连接数）**  
默认值：32

多从节点的环境里，每个 从服务节点里用于普通操作（非 发布和订阅）的最小保持连接数（长连接）。长期保持一定数量的连接有利于提高瞬时读取反映速度。

**slaveConnectionPoolSize（从节点连接池大小）**  
默认值：64

多从节点的环境里，每个 从服务节点里用于普通操作（非 发布和订阅）连接的连接池最大容量。连接池的连接数量自动弹性伸缩。

**masterConnectionMinimumIdleSize（主节点最小空闲连接数）**  
默认值：32

多从节点的环境里，每个 主节点的最小保持连接数（长连接）。长期保持一定数量的连接有利于提高瞬时写入反应速度。

**masterConnectionPoolSize（主节点连接池大小）**  
默认值：64

主节点的连接池最大容量。连接池的连接数量自动弹性伸缩。

**idleConnectionTimeout（连接空闲超时，单位：毫秒）**  
默认值：10000

如果当前连接池里的连接数量超过了最小空闲连接数，而同时有连接空闲时间超过了该数值，那么这些连接将会自动被关闭，并从连接池里去掉。时间单位是毫秒。

**connectTimeout（连接超时，单位：毫秒）**  
默认值：10000

同任何节点建立连接时的等待超时。时间单位是毫秒。

**timeout（命令等待超时，单位：毫秒）**  
默认值：3000

等待节点回复命令的时间。该时间从命令发送成功时开始计时。

**retryAttempts（命令失败重试次数）**  
默认值：3

如果尝试达到 retryAttempts（命令失败重试次数） 仍然不能将命令发送至某个指定的节点时，将抛出错误。如果尝试在此限制之内发送成功，则开始启用 timeout（命令等待超时） 计时。

**retryInterval（命令重试发送时间间隔，单位：毫秒）**  
默认值：1500

在某个节点执行相同或不同命令时，连续 失败 failedAttempts（执行失败最大次数） 时，该节点将被从可用节点列表里清除，直到 reconnectionTimeout（重新连接时间间隔） 超时以后再次尝试。

**database（数据库编号）**  
默认值：0

尝试连接的数据库编号。

**password（密码）**  
默认值：null

用于节点身份验证的密码。

**subscriptionsPerConnection（单个连接最大订阅数量）**  
默认值：5

每个连接的最大订阅数量。

**clientName（客户端名称）**  
默认值：null

在Redis节点里显示的客户端名称。

**sslEnableEndpointIdentification（启用SSL终端识别）**  
默认值：true

开启SSL终端识别能力。

**sslProvider（SSL实现方式）**  
默认值：JDK

确定采用哪种方式（JDK或OPENSSL）来实现SSL连接。

**sslTruststore（SSL信任证书库路径）**  
默认值：null

指定SSL信任证书库的路径。

**sslTruststorePassword（SSL信任证书库密码）**  
默认值：null

指定SSL信任证书库的密码。

**sslKeystore（SSL钥匙库路径）**  
默认值：null

指定SSL钥匙库的路径。

**sslKeystorePassword（SSL钥匙库密码）**  
默认值：null

指定SSL钥匙库的密码。

#### 2.8.2. 通过YAML文件配置集群模式

配置主从模式可以通过指定一个YAML格式的文件来实现。以下是YAML格式的配置文件样本。文件中的字段名称必须与MasterSlaveServersConfig和Config对象里的字段名称相符。

```java
---
masterSlaveServersConfig:
  idleConnectionTimeout: 10000
  connectTimeout: 10000
  timeout: 3000
  retryAttempts: 3
  retryInterval: 1500
  failedAttempts: 3
  password: null
  subscriptionsPerConnection: 5
  clientName: null
  loadBalancer: !<org.redisson.connection.balancer.RoundRobinLoadBalancer> {}
  slaveSubscriptionConnectionMinimumIdleSize: 1
  slaveSubscriptionConnectionPoolSize: 50
  slaveConnectionMinimumIdleSize: 32
  slaveConnectionPoolSize: 64
  masterConnectionMinimumIdleSize: 32
  masterConnectionPoolSize: 64
  readMode: "SLAVE"
  slaveAddresses:
  - "redis://127.0.0.1:6381"
  - "redis://127.0.0.1:6380"
  masterAddress: "redis://127.0.0.1:6379"
  database: 0
threads: 0
nettyThreads: 0
codec: !<org.redisson.codec.JsonJacksonCodec> {}
"transportMode":"NIO"
```

三、程序接口调用方式
----------

RedissonClient、RedissonReactiveClient和RedissonRxClient实例本身和Redisson提供的所有分布式对象都是线程安全的。

Redisson为每个操作都提供了自动重试策略，当某个命令执行失败时，Redisson会自动进行重试。自动重试策略可以通过修改retryAttempts（默认值：3）参数和retryInterval（默认值：1000毫秒）参数来进行优化调整。当等待时间达到retryInterval指定的时间间隔以后，将自动重试下一次。全部重试失败以后将抛出错误。

Redisson框架提供的几乎所有对象都包含了同步和异步相互匹配的方法。这些对象都可以通过RedissonClient接口获取。同时还为大部分Redisson对象提供了满足[异步流处理标准](http://reactive-streams.org/)的程序接口RedissonReactiveClient。除此外还提供了RxJava2规范的RedissonRxClient程序接口。

以下是关于使用RAtomicLong对象的范例：

```java
RedissonClient client = Redisson.create(config);
RAtomicLong longObject = client.getAtomicLong('myLong');
// 同步执行方式
longObject.compareAndSet(3, 401);
// 异步执行方式
RFuture<Boolean> result = longObject.compareAndSetAsync(3, 401);

RedissonReactiveClient client = Redisson.createReactive(config);
RAtomicLongReactive longObject = client.getAtomicLong('myLong');
// 异步流执行方式
Mono<Boolean> result = longObject.compareAndSet(3, 401);
RedissonRxClient client = Redisson.createRx(config);
RAtomicLongRx longObject= client.getAtomicLong("myLong");
// RxJava2方式
Flowable<Boolean result = longObject.compareAndSet(3, 401);
```

### 3.1. 异步执行方式

几乎所有的Redisson对象都实现了一个异步接口，异步接口提供的方法名称与其同步接口的方法名称相互匹配。例如：

```java
// RAtomicLong接口继承了RAtomicLongAsync接口
RAtomicLongAsync longObject = client.getAtomicLong("myLong");
RFuture<Boolean> future = longObject.compareAndSetAsync(1, 401);
```

异步执行的方法都会返回一个实现了RFuture接口的对象。该对象同时提供了java.util.concurrent.CompletionStage和java.util.concurrent.Future两个异步接口。

```java

future.whenComplete((res, exception) -> {
    // ...
});
// 或者
future.thenAccept(res -> {
    // 处理返回
}).exceptionally(exception -> {
    // 处理错误
});
```

### 3.2. 异步流执行方式

Redisson为大多数分布式数据结构提供了满足Reactor项目的异步流处理标准的程序接口。该接口通过两种方式实现：

1.基于Project Reactor标准的实现方式。使用范例如下：

```java
RedissonReactiveClient client = Redisson.createReactive(config);
RAtomicLongReactive atomicLong = client.getAtomicLong("myLong");
Mono<Boolean> cs = longObject.compareAndSet(10, 91);
Mono<Long> get = longObject.get();

Publisher<Long> getPublisher = longObject.get();
```

2.基于RxJava2标准的实现方式。使用范例如下：

```java
RedissonRxClient client = Redisson.createRx(config);
RAtomicLongRx atomicLong = client.getAtomicLong("myLong");
Single<Boolean> cs = longObject.compareAndSet(10, 91);
Single<Long> get = longObject.get();
```

四、数据序列化
-------

Redisson的对象编码类是用于将对象进行序列化和反序列化，以实现对该对象在Redis里的读取和存储。Redisson提供了以下几种的对象编码应用，以供大家选择：

| 编码类名称 | 说明 |
| --- | --- |
| org.redisson.codec.JsonJacksonCodec | Jackson JSON 编码 默认编码 |
| org.redisson.codec.AvroJacksonCodec | Avro 一个二进制的JSON编码 |
| org.redisson.codec.SmileJacksonCodec | Smile 另一个二进制的JSON编码 |
| org.redisson.codec.CborJacksonCodec | CBOR 又一个二进制的JSON编码 |
| org.redisson.codec.MsgPackJacksonCodec | MsgPack 再来一个二进制的JSON编码 |
| org.redisson.codec.IonJacksonCodec | Amazon Ion 亚马逊的Ion编码，格式与JSON类似 |
| org.redisson.codec.KryoCodec | Kryo 二进制对象序列化编码 |
| org.redisson.codec.SerializationCodec | JDK序列化编码 |
| org.redisson.codec.FstCodec | FST 10倍于JDK序列化性能而且100%兼容的编码 |
| org.redisson.codec.LZ4Codec | LZ4 压缩型序列化对象编码 |
| org.redisson.codec.SnappyCodec | Snappy 另一个压缩型序列化对象编码 |
| org.redisson.client.codec.JsonJacksonMapCodec | 基于Jackson的映射类使用的编码。可用于避免序列化类的信息，以及用于解决使用byte\[\]遇到的问题。 |
| org.redisson.client.codec.StringCodec | 纯字符串编码（无转换） |
| org.redisson.client.codec.LongCodec | 纯整长型数字编码（无转换） |
| org.redisson.client.codec.ByteArrayCodec | 字节数组编码 |
| org.redisson.codec.CompositeCodec | 用来组合多种不同编码在一起 |

五、单个集合数据分片（Sharding）
--------------------

在集群模式下，Redisson为单个Redis集合类型提供了自动分片的功能。

Redisson提供的所有数据结构都支持在集群环境下使用，但每个数据结构只被保存在一个固定的槽内。Redisson PRO提供的自动分片功能能够将单个数据结构拆分，然后均匀的分布在整个集群里，而不是被挤在单一一个槽里。自动分片功能的优势主要有以下几点：

*   单个数据结构可以充分利用整个集群内存资源，而不是被某一个节点的内存限制。
*   将单个数据结构分片以后分布在集群中不同的节点里，不仅可以大幅提高读写性能，还能够保证读写性能随着集群的扩张而自动提升。

Redisson通过自身的分片算法，将一个大集合拆分为若干个片段（默认231个，分片数量范围是3 - 16834），然后将拆分后的片段均匀的分布到集群里各个节点里，保证每个节点分配到的片段数量大体相同。比如在默认情况下231个片段分到含有4个主节点的集群里，每个主节点将会分配到大约57个片段，同样的道理如果有5个主节点，每个节点会分配到大约46个片段。

目前支持的数据结构类型和服务包括集（Set）、映射（Map）、BitSet、布隆过滤器（Bloom Filter）、Spring Cache和Hibernate Cache。

该功能仅限于Redisson PRO版本。

六、分布式对象
-------

每个Redisson对象实例都会有一个与之对应的Redis数据实例，可以通过调用getName方法来取得Redis数据实例的名称（key）。

```java
RMap map = redisson.getMap("mymap");
map.getName(); // = mymap
```

所有与Redis key相关的操作都归纳在RKeys这个接口里：

```java
RKeys keys = redisson.getKeys();

Iterable<String> allKeys = keys.getKeys();
Iterable<String> foundedKeys = keys.getKeysByPattern('key*');
long numOfDeletedKeys = keys.delete("obj1", "obj2", "obj3");
long deletedKeysAmount = keys.deleteByPattern("test?");
String randomKey = keys.randomKey();
long keysAmount = keys.count();
```

### 6.1. 通用对象桶（Object Bucket）

Redisson的分布式RBucketJava对象是一种通用对象桶可以用来存放任类型的对象。 除了同步接口外，还提供了异步（Async）、反射式（Reactive）和RxJava2标准的接口。

```java
RBucket<AnyObject> bucket = redisson.getBucket("anyObject");
bucket.set(new AnyObject(1));
AnyObject obj = bucket.get();

bucket.trySet(new AnyObject(3));
bucket.compareAndSet(new AnyObject(4), new AnyObject(5));
bucket.getAndSet(new AnyObject(6));
```

还可以通过RBuckets接口实现批量操作多个RBucket对象：

```java
RBuckets buckets = redisson.getBuckets();
List<RBucket<V>> foundBuckets = buckets.find("myBucket*");
Map<String, V> loadedBuckets = buckets.get("myBucket1", "myBucket2", "myBucket3");

Map<String, Object> map = new HashMap<>();
map.put("myBucket1", new MyObject());
map.put("myBucket2", new MyObject());

// 利用Redis的事务特性，同时保存所有的通用对象桶，如果任意一个通用对象桶已经存在则放弃保存其他所有数据。
buckets.trySet(map);
// 同时保存全部通用对象桶。
buckets.set(map);
```

### 6.2. 二进制流（Binary Stream）

Redisson的分布式RBinaryStream Java对象同时提供了InputStream接口和OutputStream接口的实现。流的最大容量受Redis主节点的内存大小限制。

```java
RBinaryStream stream = redisson.getBinaryStream("anyStream");
byte[] content = ...
stream.set(content);

InputStream is = stream.getInputStream();
byte[] readBuffer = new byte[512];
is.read(readBuffer);

OutputStream os = stream.getOuputStream();
byte[] contentToWrite = ...
os.write(contentToWrite);
```

### 6.3. 地理空间对象桶（Geospatial Bucket）

Redisson的分布式RGeo Java对象是一种专门用来储存与地理位置有关的对象桶。除了同步接口外，还提供了异步（Async）、反射式（Reactive）和RxJava2标准的接口。

```java
RGeo<String> geo = redisson.getGeo("test");
geo.add(new GeoEntry(13.361389, 38.115556, "Palermo"),
        new GeoEntry(15.087269, 37.502669, "Catania"));
geo.addAsync(37.618423, 55.751244, "Moscow");

Double distance = geo.dist("Palermo", "Catania", GeoUnit.METERS);
geo.hashAsync("Palermo", "Catania");
Map<String, GeoPosition> positions = geo.pos("test2", "Palermo", "test3", "Catania", "test1");
List<String> cities = geo.radius(15, 37, 200, GeoUnit.KILOMETERS);
Map<String, GeoPosition> citiesWithPositions = geo.radiusWithPosition(15, 37, 200, GeoUnit.KILOMETERS);
```

### 6.4. BitSet

Redisson的分布式RBitSetJava对象采用了与java.util.BiteSet类似结构的设计风格。可以理解为它是一个分布式的可伸缩式位向量。需要注意的是RBitSet的大小受Redis限制，最大长度为4 294 967 295。除了同步接口外，还提供了异步（Async）、反射式（Reactive）和RxJava2标准的接口。

```java
RBitSet set = redisson.getBitSet("simpleBitset");
set.set(0, true);
set.set(1812, false);
set.clear(0);
set.addAsync("e");
set.xor("anotherBitset");
```

#### 6.4.1. BitSet数据分片（Sharding）（分布式RoaringBitMap）

基于Redis的Redisson集群分布式BitSet通过RClusteredBitSet接口，为集群状态下的Redis环境提供了BitSet数据分片的功能。通过优化后更加有效的分布式RoaringBitMap算法，突破了原有的BitSet大小限制，达到了集群物理内存容量大小。在这里可以获取更多的内部信息。

```java
RClusteredBitSet set = redisson.getClusteredBitSet("simpleBitset");
set.set(0, true);
set.set(1812, false);
set.clear(0);
set.addAsync("e");
set.xor("anotherBitset");
```

该功能仅限于Redisson PRO版本。

### 6.5. 原子整长形（AtomicLong）

Redisson的分布式整长形RAtomicLong对象和Java中的java.util.concurrent.atomic.AtomicLong对象类似。除了同步接口外，还提供了异步（Async）、反射式（Reactive）和RxJava2标准的接口。

```java
RAtomicLong atomicLong = redisson.getAtomicLong("myAtomicLong");
atomicLong.set(3);
atomicLong.incrementAndGet();
atomicLong.get();
```

### 6.6. 原子双精度浮点（AtomicDouble）

Redisson还提供了分布式原子双精度浮点RAtomicDouble，弥补了Java自身的不足。除了同步接口外，还提供了异步（Async）、反射式（Reactive）和RxJava2标准的接口。

```java
RAtomicDouble atomicDouble = redisson.getAtomicDouble("myAtomicDouble");
atomicDouble.set(2.81);
atomicDouble.addAndGet(4.11);
atomicDouble.get();
```

### 6.7. 话题（订阅分发）

Redisson的分布式话题RTopic(http://static.javadoc.io/org.redisson/redisson/3.10.0/org/redisson/api/RTopic.html对象实现了发布、订阅的机制。除了同步接口外，还提供了异步（Async(http://static.javadoc.io/org.redisson/redisson/3.10.0/org/redisson/api/RTopicAsync.html)）、反射式（Reactive(http://static.javadoc.io/org.redisson/redisson/3.10.0/org/redisson/api/RTopicReactive.html)）和RxJava2(http://static.javadoc.io/org.redisson/redisson/3.10.0/org/redisson/api/RTopicRx.html)标准的接口。

```java
RTopic topic = redisson.getTopic("anyTopic");
topic.addListener(SomeObject.class, new MessageListener<SomeObject>() {
    @Override
    public void onMessage(String channel, SomeObject message) {
        //...
    }
});

// 在其他线程或JVM节点
RTopic topic = redisson.getTopic("anyTopic");
long clientsReceivedMessage = topic.publish(new SomeObject());
```

在Redis节点故障转移（主从切换）或断线重连以后，所有的话题监听器将自动完成话题的重新订阅。

#### 6.7.1. 模糊话题

Redisson的模糊话题RPatternTopic对象可以通过正式表达式来订阅多个话题。除了同步接口外，还提供了异步（Async）、反射式（Reactive）和RxJava2标准的接口。

```java
// 订阅所有满足`topic1.*`表达式的话题
RPatternTopic topic1 = redisson.getPatternTopic("topic1.*");
int listenerId = topic1.addListener(Message.class, new PatternMessageListener<Message>() {
    @Override
    public void onMessage(String pattern, String channel, Message msg) {
         Assert.fail();
    }
});
```

在Redis节点故障转移（主从切换）或断线重连以后，所有的模糊话题监听器将自动完成话题的重新订阅。

### 6.8. 布隆过滤器（Bloom Filter）

Redisson利用Redis实现了Java分布式布隆过滤器（Bloom Filter）。所含最大比特数量为232。

```java
RBloomFilter<SomeObject> bloomFilter = redisson.getBloomFilter("sample");
// 初始化布隆过滤器，预计统计元素数量为55000000，期望误差率为0.03
bloomFilter.tryInit(55000000L, 0.03);
bloomFilter.add(new SomeObject("field1Value", "field2Value"));
bloomFilter.add(new SomeObject("field5Value", "field8Value"));
bloomFilter.contains(new SomeObject("field1Value", "field8Value"));
```

#### 6.8.1. 布隆过滤器数据分片（Sharding）

基于Redis的Redisson集群分布式布隆过滤器通过RClusteredBloomFilter接口，为集群状态下的Redis环境提供了布隆过滤器数据分片的功能。 通过优化后更加有效的算法，通过压缩未使用的比特位来释放集群内存空间。每个对象的状态都将被分布在整个集群中。所含最大比特数量为2^64。在这里可以获取更多的内部信息。

```java
RClusteredBloomFilter<SomeObject> bloomFilter = redisson.getClusteredBloomFilter("sample");
// 采用以下参数创建布隆过滤器
// expectedInsertions = 255000000
// falseProbability = 0.03
bloomFilter.tryInit(255000000L, 0.03);
bloomFilter.add(new SomeObject("field1Value", "field2Value"));
bloomFilter.add(new SomeObject("field5Value", "field8Value"));
bloomFilter.contains(new SomeObject("field1Value", "field8Value"));
```

该功能仅限于Redisson PRO版本。

### 6.9. 基数估计算法（HyperLogLog）

Redisson利用Redis实现了Java分布式基数估计算法（HyperLogLog）对象。该对象可以在有限的空间内通过概率算法统计大量的数据。除了同步接口外，还提供了异步（Async）、反射式（Reactive）和RxJava2标准的接口。

```java
RHyperLogLog<Integer> log = redisson.getHyperLogLog("log");
log.add(1);
log.add(2);
log.add(3);

log.count();
```

### 6.10. 整长型累加器（LongAdder）

基于Redis的Redisson分布式整长型累加器（LongAdder）采用了与java.util.concurrent.atomic.LongAdder类似的接口。通过利用客户端内置的LongAdder对象，为分布式环境下递增和递减操作提供了很高得性能。据统计其性能最高比分布式AtomicLong对象快 12000 倍。完美适用于分布式统计计量场景。

```java
RLongAdder atomicLong = redisson.getLongAdder("myLongAdder");
atomicLong.add(12);
atomicLong.increment();
atomicLong.decrement();
atomicLong.sum();
```

当不再使用整长型累加器对象的时候应该自行手动销毁，如果Redisson对象被关闭（shutdown）了，则不用手动销毁。

```java
RLongAdder atomicLong = ...
atomicLong.destroy();
```

### 6.11. 双精度浮点累加器（DoubleAdder）

基于Redis的Redisson分布式双精度浮点累加器（DoubleAdder）采用了与java.util.concurrent.atomic.DoubleAdder类似的接口。通过利用客户端内置的DoubleAdder对象，为分布式环境下递增和递减操作提供了很高得性能。据统计其性能最高比分布式AtomicDouble对象快 12000 倍。完美适用于分布式统计计量场景。

```java
RLongDouble atomicDouble = redisson.getLongDouble("myLongDouble");
atomicDouble.add(12);
atomicDouble.increment();
atomicDouble.decrement();
atomicDouble.sum();
```

当不再使用双精度浮点累加器对象的时候应该自行手动销毁，如果Redisson对象被关闭（shutdown）了，则不用手动销毁。

```java
RLongDouble atomicDouble = ...

_b6d2063_
atomicDouble.destroy();
```

### 6.12. 限流器（RateLimiter）

基于Redis的分布式限流器（RateLimiter）可以用来在分布式环境下现在请求方的调用频率。既适用于不同Redisson实例下的多线程限流，也适用于相同Redisson实例下的多线程限流。该算法不保证公平性。除了同步接口外，还提供了异步（Async）、反射式（Reactive）和RxJava2标准的接口。

```java
RRateLimiter rateLimiter = redisson.getRateLimiter("myRateLimiter");
// 初始化
// 最大流速 = 每1秒钟产生10个令牌
rateLimiter.trySetRate(RateType.OVERALL, 10, 1, RateIntervalUnit.SECONDS);

CountDownLatch latch = new CountDownLatch(2);
limiter.acquire(3);
// ...

Thread t = new Thread(() -> {
    limiter.acquire(2);
    // ...        
});
```

七、分布式集合
-------

### 7.1. 映射（Map）

基于Redis的Redisson的分布式映射结构的RMap Java对象实现了java.util.concurrent.ConcurrentMap接口和java.util.Map接口。与HashMap不同的是，RMap保持了元素的插入顺序。该对象的最大容量受Redis限制，最大元素数量是4 294 967 295个。

除了同步接口外，还提供了异步（Async）、反射式（Reactive）和RxJava2标准的接口。如果你想用Redis Map来保存你的POJO的话，可以考虑使用分布式实时对象（Live Object）服务。

在特定的场景下，映射缓存（Map）上的高度频繁的读取操作，使网络通信都被视为瓶颈时，可以使用Redisson提供的带有本地缓存功能的映射。

```java
RMap<String, SomeObject> map = redisson.getMap("anyMap");
SomeObject prevObject = map.put("123", new SomeObject());
SomeObject currentObject = map.putIfAbsent("323", new SomeObject());
SomeObject obj = map.remove("123");

map.fastPut("321", new SomeObject());
map.fastRemove("321");

RFuture<SomeObject> putAsyncFuture = map.putAsync("321");
RFuture<Void> fastPutAsyncFuture = map.fastPutAsync("321");

map.fastPutAsync("321", new SomeObject());
map.fastRemoveAsync("321");
```

映射的字段锁的用法：

```java
RMap<MyKey, MyValue> map = redisson.getMap("anyMap");
MyKey k = new MyKey();
RLock keyLock = map.getLock(k);
keyLock.lock();
try {
   MyValue v = map.get(k);
   // 其他业务逻辑
} finally {
   keyLock.unlock();
}

RReadWriteLock rwLock = map.getReadWriteLock(k);
rwLock.readLock().lock();
try {
   MyValue v = map.get(k);
   // 其他业务逻辑
} finally {
   keyLock.readLock().unlock();
}
```

#### 7.1.1. 映射（Map）的元素淘汰（Eviction），本地缓存（LocalCache）和数据分片（Sharding）

Redisson提供了一系列的映射类型的数据结构，这些结构按特性主要分为三大类：

*   元素淘汰（Eviction） 类 – 带有元素淘汰（Eviction）机制的映射类允许针对一个映射中每个元素单独设定 有效时间 和 最长闲置时间 。
    
*   本地缓存（LocalCache） 类 – 本地缓存（Local Cache）也叫就近缓存（Near Cache）。这类映射的使用主要用于在特定的场景下，映射缓存（MapCache）上的高度频繁的读取操作，使网络通信都被视为瓶颈的情况。Redisson与Redis通信的同时，还将部分数据保存在本地内存里。这样的设计的好处是它能将读取速度提高最多 45倍 。 所有同名的本地缓存共用一个订阅发布话题，所有更新和过期消息都将通过该话题共享。
    
*   数据分片（Sharding） 类 – 数据分片（Sharding）类仅适用于Redis集群环境下，因此带有数据分片（Sharding）功能的映射也叫集群分布式映射。它利用分库的原理，将单一一个映射结构切分为若干个小的映射，并均匀的分布在集群中的各个槽里。这样的设计能使一个单一映射结构突破Redis自身的容量限制，让其容量随集群的扩大而增长。在扩容的同时，还能够使读写性能和元素淘汰处理能力随之成线性增长。
    

以下列表是Redisson提供的所有映射的名称及其特性：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/d65be6081063465ab65c9f6a8483abc7.png)  
除此以外，Redisson还提供了Spring Cache和JCache的实现。

**元素淘汰功能（Eviction）**  
Redisson的分布式的RMapCache Java对象在基于RMap的前提下实现了针对单个元素的淘汰机制。同时仍然保留了元素的插入顺序。由于RMapCache是基于RMap实现的，使它同时继承了java.util.concurrent.ConcurrentMap接口和java.util.Map接口。Redisson提供的Spring Cache整合以及JCache正是基于这样的功能来实现的。

目前的Redis自身并不支持散列（Hash）当中的元素淘汰，因此所有过期元素都是通过org.redisson.EvictionScheduler实例来实现定期清理的。为了保证资源的有效利用，每次运行最多清理300个过期元素。任务的启动时间将根据上次实际清理数量自动调整，间隔时间趋于1秒到1小时之间。比如该次清理时删除了300条元素，那么下次执行清理的时间将在1秒以后（最小间隔时间）。一旦该次清理数量少于上次清理数量，时间间隔将增加1.5倍。

```java
RMapCache<String, SomeObject> map = redisson.getMapCache("anyMap");
// 有效时间 ttl = 10分钟
map.put("key1", new SomeObject(), 10, TimeUnit.MINUTES);
// 有效时间 ttl = 10分钟, 最长闲置时间 maxIdleTime = 10秒钟
map.put("key1", new SomeObject(), 10, TimeUnit.MINUTES, 10, TimeUnit.SECONDS);

// 有效时间 = 3 秒钟
map.putIfAbsent("key2", new SomeObject(), 3, TimeUnit.SECONDS);
// 有效时间 ttl = 40秒钟, 最长闲置时间 maxIdleTime = 10秒钟
map.putIfAbsent("key2", new SomeObject(), 40, TimeUnit.SECONDS, 10, TimeUnit.SECONDS);
```

**本地缓存功能（Local Cache）**

在特定的场景下，映射（Map）上的高度频繁的读取操作，使网络通信都被视为瓶颈时，使用Redisson提供的带有本地缓存功能的分布式本地缓存映射RLocalCachedMapJava对象会是一个很好的选择。它同时实现了java.util.concurrent.ConcurrentMap和java.util.Map两个接口。本地缓存功能充分的利用了JVM的自身内存空间，对部分常用的元素实行就地缓存，这样的设计让读取操作的性能较分布式映射相比提高最多 45倍 。以下配置参数可以用来创建这个实例：

```java
LocalCachedMapOptions options = LocalCachedMapOptions.defaults()
      // 用于淘汰清除本地缓存内的元素
      // 共有以下几种选择:
      // LFU - 统计元素的使用频率，淘汰用得最少（最不常用）的。
      // LRU - 按元素使用时间排序比较，淘汰最早（最久远）的。
      // SOFT - 元素用Java的WeakReference来保存，缓存元素通过GC过程清除。
      // WEAK - 元素用Java的SoftReference来保存, 缓存元素通过GC过程清除。
      // NONE - 永不淘汰清除缓存元素。
     .evictionPolicy(EvictionPolicy.NONE)
     // 如果缓存容量值为0表示不限制本地缓存容量大小
     .cacheSize(1000)
      // 以下选项适用于断线原因造成了未收到本地缓存更新消息的情况。
      // 断线重连的策略有以下几种：
      // CLEAR - 如果断线一段时间以后则在重新建立连接以后清空本地缓存
      // LOAD - 在服务端保存一份10分钟的作废日志
      //        如果10分钟内重新建立连接，则按照作废日志内的记录清空本地缓存的元素
      //        如果断线时间超过了这个时间，则将清空本地缓存中所有的内容
      // NONE - 默认值。断线重连时不做处理。
     .reconnectionStrategy(ReconnectionStrategy.NONE)
      // 以下选项适用于不同本地缓存之间相互保持同步的情况
      // 缓存同步策略有以下几种：
      // INVALIDATE - 默认值。当本地缓存映射的某条元素发生变动时，同时驱逐所有相同本地缓存映射内的该元素
      // UPDATE - 当本地缓存映射的某条元素发生变动时，同时更新所有相同本地缓存映射内的该元素
      // NONE - 不做任何同步处理
     .syncStrategy(SyncStrategy.INVALIDATE)
      // 每个Map本地缓存里元素的有效时间，默认毫秒为单位
     .timeToLive(10000)
      // 或者
     .timeToLive(10, TimeUnit.SECONDS)
      // 每个Map本地缓存里元素的最长闲置时间，默认毫秒为单位
     .maxIdle(10000)
      // 或者
     .maxIdle(10, TimeUnit.SECONDS);
```

```java
RLocalCachedMap<String, Integer> map = redisson.getLocalCachedMap("test", options);

String prevObject = map.put("123", 1);
String currentObject = map.putIfAbsent("323", 2);
String obj = map.remove("123");

// 在不需要旧值的情况下可以使用fast为前缀的类似方法
map.fastPut("a", 1);
map.fastPutIfAbsent("d", 32);
map.fastRemove("b");

RFuture<String> putAsyncFuture = map.putAsync("321");
RFuture<Void> fastPutAsyncFuture = map.fastPutAsync("321");

map.fastPutAsync("321", new SomeObject());
map.fastRemoveAsync("321");
```

当不再使用Map本地缓存对象的时候应该手动销毁，如果Redisson对象被关闭（shutdown）了，则不用手动销毁。

```java
RLocalCachedMap<String, Integer> map = ...
map.destroy();
```

**如何通过加载数据的方式来降低过期淘汰事件发布信息对网络的影响**  
代码范例:

```java
public void loadData(String cacheName, Map<String, String> data) {
    RLocalCachedMap<String, String> clearMap = redisson.getLocalCachedMap(cacheName, 
            LocalCachedMapOptions.defaults().cacheSize(1).syncStrategy(SyncStrategy.INVALIDATE));
    RLocalCachedMap<String, String> loadMap = redisson.getLocalCachedMap(cacheName, 
            LocalCachedMapOptions.defaults().cacheSize(1).syncStrategy(SyncStrategy.NONE));
    
    loadMap.putAll(data);
    clearMap.clearLocalCache();
}
```

**数据分片功能（Sharding）**  
Map数据分片是Redis集群模式下的一个功能。Redisson提供的分布式集群映射RClusteredMap Java对象也是基于RMap实现的。它同时实现了java.util.concurrent.ConcurrentMap和java.util.Map两个接口。

```java
RClusteredMap<String, SomeObject> map = redisson.getClusteredMap("anyMap");

SomeObject prevObject = map.put("123", new SomeObject());
SomeObject currentObject = map.putIfAbsent("323", new SomeObject());
SomeObject obj = map.remove("123");

map.fastPut("321", new SomeObject());
map.fastRemove("321");
```

#### 7.1.2. 映射持久化方式（缓存策略）

Redisson供了将映射中的数据持久化到外部储存服务的功能。主要场景有一下几种：

*   将Redisson的分布式映射类型作为业务和外部储存媒介之间的缓存。
*   或是用来增加Redisson映射类型中数据的持久性，或是用来增加已被驱逐的数据的寿命。
*   或是用来缓存数据库，Web服务或其他数据源的数据。

**Read-through策略**  
通俗的讲，如果一个被请求的数据不存在于Redisson的映射中的时候，Redisson将通过预先配置好的MapLoader对象加载数据。

**Write-through（数据同步写入）策略**  
在遇到映射中某条数据被更改时，Redisson会首先通过预先配置好的MapWriter对象写入到外部储存系统，然后再更新Redis内的数据。

**Write-behind（数据异步写入）策略**  
对映射的数据的更改会首先写入到Redis，然后再使用异步的方式，通过MapWriter对象写入到外部储存系统。在并发环境下可以通过writeBehindThreads参数来控制写入线程的数量，已达到对外部储存系统写入并发量的控制。

以上策略适用于所有实现了RMap、RMapCache、RLocalCachedMap和RLocalCachedMapCache接口的对象。

**配置范例：**

```java
MapOptions<K, V> options = MapOptions.<K, V>defaults()
                              .writer(myWriter)
                              .loader(myLoader);

RMap<K, V> map = redisson.getMap("test", options);
// 或
RMapCache<K, V> map = redisson.getMapCache("test", options);
// 或
RLocalCachedMap<K, V> map = redisson.getLocalCachedMap("test", options);
// 或
RLocalCachedMapCache<K, V> map = redisson.getLocalCachedMapCache("test", options);
```

#### 7.1.3. 映射监听器（Map Listener）

Redisson为所有实现了RMapCache或RLocalCachedMapCache接口的对象提供了监听以下事件的监听器：

事件 | 监听器 元素 添加 事件 | org.redisson.api.map.event.EntryCreatedListener  
元素 过期 事件 | org.redisson.api.map.event.EntryExpiredListener  
元素 删除 事件 | org.redisson.api.map.event.EntryRemovedListener  
元素 更新 事件 | org.redisson.api.map.event.EntryUpdatedListener

使用范例：

```java
RMapCache<String, Integer> map = redisson.getMapCache("myMap");
// 或
RLocalCachedMapCache<String, Integer> map = redisson.getLocalCachedMapCache("myMap", options);

int updateListener = map.addListener(new EntryUpdatedListener<Integer, Integer>() {
     @Override
     public void onUpdated(EntryEvent<Integer, Integer> event) {
          event.getKey(); // 字段名
          event.getValue() // 新值
          event.getOldValue() // 旧值
          // ...
     }
});

int createListener = map.addListener(new EntryCreatedListener<Integer, Integer>() {
     @Override
     public void onCreated(EntryEvent<Integer, Integer> event) {
          event.getKey(); // 字段名
          event.getValue() // 值
          // ...
     }
});

int expireListener = map.addListener(new EntryExpiredListener<Integer, Integer>() {
     @Override
     public void onExpired(EntryEvent<Integer, Integer> event) {
          event.getKey(); // 字段名
          event.getValue() // 值
          // ...
     }
});

int removeListener = map.addListener(new EntryRemovedListener<Integer, Integer>() {
     @Override
     public void onRemoved(EntryEvent<Integer, Integer> event) {
          event.getKey(); // 字段名
          event.getValue() // 值
          // ...
     }
});

map.removeListener(updateListener);
map.removeListener(createListener);
map.removeListener(expireListener);
map.removeListener(removeListener);
```

#### 7.1.4. LRU有界映射

Redisson提供了基于Redis的以LRU为驱逐策略的分布式LRU有界映射对象。顾名思义，分布式LRU有界映射允许通过对其中元素按使用时间排序处理的方式，主动移除超过规定容量限制的元素。

```java
RMapCache<String, String> map = redisson.getMapCache("map");
// 尝试将该映射的最大容量限制设定为10
map.trySetMaxSize(10);

// 将该映射的最大容量限制设定或更改为10
map.setMaxSize(10);

map.put("1", "2");
map.put("3", "3", 1, TimeUnit.SECONDS);
```

### 7.2. 多值映射（Multimap）

基于Redis的Redisson的分布式RMultimap Java对象允许Map中的一个字段值包含多个元素。 字段总数受Redis限制，每个Multimap最多允许有4 294 967 295个不同字段。

#### 7.2.1. 基于集（Set）的多值映射（Multimap）

基于Set的Multimap不允许一个字段值包含有重复的元素。

```java
RSetMultimap<SimpleKey, SimpleValue> map = redisson.getSetMultimap("myMultimap");
map.put(new SimpleKey("0"), new SimpleValue("1"));
map.put(new SimpleKey("0"), new SimpleValue("2"));
map.put(new SimpleKey("3"), new SimpleValue("4"));

Set<SimpleValue> allValues = map.get(new SimpleKey("0"));

List<SimpleValue> newValues = Arrays.asList(new SimpleValue("7"), new SimpleValue("6"), new SimpleValue("5"));
Set<SimpleValue> oldValues = map.replaceValues(new SimpleKey("0"), newValues);

Set<SimpleValue> removedValues = map.removeAll(new SimpleKey("0"));
```

#### 7.2.2. 基于列表（List）的多值映射（Multimap）

基于List的Multimap在保持插入顺序的同时允许一个字段下包含重复的元素。

```java
RListMultimap<SimpleKey, SimpleValue> map = redisson.getListMultimap("test1");
map.put(new SimpleKey("0"), new SimpleValue("1"));
map.put(new SimpleKey("0"), new SimpleValue("2"));
map.put(new SimpleKey("0"), new SimpleValue("1"));
map.put(new SimpleKey("3"), new SimpleValue("4"));

List<SimpleValue> allValues = map.get(new SimpleKey("0"));

Collection<SimpleValue> newValues = Arrays.asList(new SimpleValue("7"), new SimpleValue("6"), new SimpleValue("5"));
List<SimpleValue> oldValues = map.replaceValues(new SimpleKey("0"), newValues);

List<SimpleValue> removedValues = map.removeAll(new SimpleKey("0"));
```

#### 7.2.3. 多值映射（Multimap）淘汰机制（Eviction）

Multimap对象的淘汰机制是通过不同的接口来实现的。它们是RSetMultimapCache接口和RListMultimapCache接口，分别对应的是Set和List的Multimaps。

所有过期元素都是通过org.redisson.EvictionScheduler实例来实现定期清理的。为了保证资源的有效利用，每次运行最多清理100个过期元素。任务的启动时间将根据上次实际清理数量自动调整，间隔时间趋于1秒到2小时之间。比如该次清理时删除了100条元素，那么下次执行清理的时间将在1秒以后（最小间隔时间）。一旦该次清理数量少于上次清理数量，时间间隔将增加1.5倍。

RSetMultimapCache的使用范例：

```java
RSetMultimapCache<String, String> multimap = redisson.getSetMultimapCache("myMultimap");
multimap.put("1", "a");
multimap.put("1", "b");
multimap.put("1", "c");

multimap.put("2", "e");
multimap.put("2", "f");

multimap.expireKey("2", 10, TimeUnit.MINUTES);
```

### 7.3. 集（Set）

基于Redis的Redisson的分布式Set结构的RSet Java对象实现了java.util.Set接口。通过元素的相互状态比较保证了每个元素的唯一性。该对象的最大容量受Redis限制，最大元素数量是4 294 967 295个。

```java
RSet<SomeObject> set = redisson.getSet("anySet");
set.add(new SomeObject());
set.remove(new SomeObject());
```

Redisson PRO版本中的Set对象还可以在Redis集群环境下支持单集合数据分片。

#### 7.3.1. 集（Set）淘汰机制（Eviction）

基于Redis的Redisson的分布式RSetCache Java对象在基于RSet的前提下实现了针对单个元素的淘汰机制。由于RSetCache是基于RSet实现的，使它还集成了java.util.Set接口。

目前的Redis自身并不支持Set当中的元素淘汰，因此所有过期元素都是通过org.redisson.EvictionScheduler实例来实现定期清理的。为了保证资源的有效利用，每次运行最多清理100个过期元素。任务的启动时间将根据上次实际清理数量自动调整，间隔时间趋于1秒到2小时之间。比如该次清理时删除了100条元素，那么下次执行清理的时间将在1秒以后（最小间隔时间）。一旦该次清理数量少于上次清理数量，时间间隔将增加1.5倍。

```java
RSetCache<SomeObject> set = redisson.getSetCache("anySet");
// ttl = 10 seconds
set.add(new SomeObject(), 10, TimeUnit.SECONDS);
```

#### 7.3.2. 集（Set）数据分片（Sharding）

Set数据分片是Redis集群模式下的一个功能。Redisson提供的分布式RClusteredSet Java对象也是基于RSet实现的。在这里可以获取更多的信息。

```java
RClusteredSet<SomeObject> set = redisson.getClusteredSet("anySet");
set.add(new SomeObject());
set.remove(new SomeObject());
```

除了RClusteredSet以外，Redisson还提供了另一种集群模式下的分布式集（Set），它不仅提供了透明的数据分片功能，还为每个元素提供了淘汰机制。RClusteredSetCache 类分别同时提供了RClusteredSet 和RSetCache 这两个接口的实现。当然这些都是基于java.util.Set的接口实现上的。

该功能仅限于Redisson PRO版本。

### 7.4. 有序集（SortedSet）

基于Redis的Redisson的分布式RSortedSet Java对象实现了java.util.SortedSet接口。在保证元素唯一性的前提下，通过比较器（Comparator）接口实现了对元素的排序。

```java
RSortedSet<Integer> set = redisson.getSortedSet("anySet");
set.trySetComparator(new MyComparator()); // 配置元素比较器
set.add(3);
set.add(1);
set.add(2);

set.removeAsync(0);
set.addAsync(5);
```

### 7.5. 计分排序集（ScoredSortedSet）

基于Redis的Redisson的分布式RScoredSortedSet Java对象是一个可以按插入时指定的元素评分排序的集合。它同时还保证了元素的唯一性。

```java
RScoredSortedSet<SomeObject> set = redisson.getScoredSortedSet("simple");

set.add(0.13, new SomeObject(a, b));
set.addAsync(0.251, new SomeObject(c, d));
set.add(0.302, new SomeObject(g, d));

set.pollFirst();
set.pollLast();

int index = set.rank(new SomeObject(g, d)); // 获取元素在集合中的位置
Double score = set.getScore(new SomeObject(g, d)); // 获取元素的评分
```

### 7.6. 字典排序集（LexSortedSet）

基于Redis的Redisson的分布式RLexSortedSet Java对象在实现了java.util.Set接口的同时，将其中的所有字符串元素按照字典顺序排列。它公式还保证了字符串元素的唯一性。

```java
RLexSortedSet set = redisson.getLexSortedSet("simple");
set.add("d");
set.addAsync("e");
set.add("f");

set.lexRangeTail("d", false);
set.lexCountHead("e");
set.lexRange("d", true, "z", false);
```

### 7.7. 列表（List）

基于Redis的Redisson分布式列表（List）结构的RList Java对象在实现了java.util.List接口的同时，确保了元素插入时的顺序。该对象的最大容量受Redis限制，最大元素数量是4 294 967 295个。

```java
RList<SomeObject> list = redisson.getList("anyList");
list.add(new SomeObject());
list.get(0);
list.remove(new SomeObject());
```

### 7.8. 队列（Queue）

基于Redis的Redisson分布式无界队列（Queue）结构的RQueue Java对象实现了java.util.Queue接口。尽管RQueue对象无初始大小（边界）限制，但对象的最大容量受Redis限制，最大元素数量是4 294 967 295个。

```java
RQueue<SomeObject> queue = redisson.getQueue("anyQueue");
queue.add(new SomeObject());
SomeObject obj = queue.peek();
SomeObject someObj = queue.poll();
```

### 7.9. 双端队列（Deque）

基于Redis的Redisson分布式无界双端队列（Deque）结构的RDeque Java对象实现了java.util.Deque接口。尽管RDeque对象无初始大小（边界）限制，但对象的最大容量受Redis限制，最大元素数量是4 294 967 295个。

```java
RDeque<SomeObject> queue = redisson.getDeque("anyDeque");
queue.addFirst(new SomeObject());
queue.addLast(new SomeObject());
SomeObject obj = queue.removeFirst();
SomeObject someObj = queue.removeLast();
```

### 7.10. 阻塞队列（Blocking Queue）

基于Redis的Redisson分布式无界阻塞队列（Blocking Queue）结构的RBlockingQueue Java对象实现了java.util.concurrent.BlockingQueue接口。尽管RBlockingQueue对象无初始大小（边界）限制，但对象的最大容量受Redis限制，最大元素数量是4 294 967 295个。

```java
RBlockingQueue<SomeObject> queue = redisson.getBlockingQueue("anyQueue");
queue.offer(new SomeObject());

SomeObject obj = queue.peek();
SomeObject someObj = queue.poll();
SomeObject ob = queue.poll(10, TimeUnit.MINUTES);
```

poll, pollFromAny, pollLastAndOfferFirstTo和take方法内部采用话题订阅发布实现，在Redis节点故障转移（主从切换）或断线重连以后，内置的相关话题监听器将自动完成话题的重新订阅。

### 7.11. 有界阻塞队列（Bounded Blocking Queue）

基于Redis的Redisson分布式有界阻塞队列（Bounded Blocking Queue）结构的RBoundedBlockingQueue Java对象实现了java.util.concurrent.BlockingQueue接口。该对象的最大容量受Redis限制，最大元素数量是4 294 967 295个。队列的初始容量（边界）必须在使用前设定好。

```java
RBoundedBlockingQueue<SomeObject> queue = redisson.getBoundedBlockingQueue("anyQueue");
// 如果初始容量（边界）设定成功则返回`真（true）`，
// 如果初始容量（边界）已近存在则返回`假（false）`。
queue.trySetCapacity(2);

queue.offer(new SomeObject(1));
queue.offer(new SomeObject(2));
// 此时容量已满，下面代码将会被阻塞，直到有空闲为止。
queue.put(new SomeObject());

SomeObject obj = queue.peek();
SomeObject someObj = queue.poll();
SomeObject ob = queue.poll(10, TimeUnit.MINUTES);
```

poll, pollFromAny, pollLastAndOfferFirstTo和take方法内部采用话题订阅发布实现，在Redis节点故障转移（主从切换）或断线重连以后，内置的相关话题监听器将自动完成话题的重新订阅。

### 7.12. 阻塞双端队列（Blocking Deque）

基于Redis的Redisson分布式无界阻塞双端队列（Blocking Deque）结构的RBlockingDeque Java对象实现了java.util.concurrent.BlockingDeque接口。尽管RBlockingDeque对象无初始大小（边界）限制，但对象的最大容量受Redis限制，最大元素数量是4 294 967 295个。

```java
RBlockingDeque<Integer> deque = redisson.getBlockingDeque("anyDeque");
deque.putFirst(1);
deque.putLast(2);
Integer firstValue = queue.takeFirst();
Integer lastValue = queue.takeLast();
Integer firstValue = queue.pollFirst(10, TimeUnit.MINUTES);
Integer lastValue = queue.pollLast(3, TimeUnit.MINUTES);
```

poll, pollFromAny, pollLastAndOfferFirstTo和take方法内部采用话题订阅发布实现，在Redis节点故障转移（主从切换）或断线重连以后，内置的相关话题监听器将自动完成话题的重新订阅。

### 7.13. 阻塞公平队列（Blocking Fair Queue）

基于Redis的Redisson分布式无界阻塞公平队列（Blocking Fair Queue）结构的RBlockingFairQueue Java对象在实现Redisson分布式无界阻塞队列（Blocking Queue）结构RBlockingQueue接口的基础上，解决了多个队列消息的处理者在复杂的网络环境下，网络延时的影响使“较远”的客户端最终收到消息数量低于“较近”的客户端的问题。从而解决了这种现象引发的个别处理节点过载的情况。

以分布式无界阻塞队列为基础，采用公平获取消息的机制，不仅保证了poll、pollFromAny、pollLastAndOfferFirstTo和take方法获取消息的先入顺序，还能让队列里的消息被均匀的发布到处在复杂分布式环境中的各个处理节点里。

```java
RBlockingFairQueue queue = redisson.getBlockingFairQueue("myQueue");
queue.offer(new SomeObject());

SomeObject obj = queue.peek();
SomeObject someObj = queue.poll();
SomeObject ob = queue.poll(10, TimeUnit.MINUTES);
```

该功能仅限于Redisson PRO版本。

### 7.14. 阻塞公平双端队列（Blocking Fair Deque）

基于Redis的Redisson分布式无界阻塞公平双端队列（Blocking Fair Deque）结构的RBlockingFairDeque Java对象在实现Redisson分布式无界阻塞双端队列（Blocking Deque）结构RBlockingDeque接口的基础上，解决了多个队列消息的处理者在复杂的网络环境下，网络延时的影响使“较远”的客户端最终收到消息数量低于“较近”的客户端的问题。从而解决了这种现象引发的个别处理节点过载的情况。

以分布式无界阻塞双端队列为基础，采用公平获取消息的机制，不仅保证了poll、take、pollFirst、takeFirst、pollLast和takeLast方法获取消息的先入顺序，还能让队列里的消息被均匀的发布到处在复杂分布式环境中的各个处理节点里。

```java
RBlockingFairDeque deque = redisson.getBlockingFairDeque("myDeque");
deque.offer(new SomeObject());

SomeObject firstElement = queue.peekFirst();
SomeObject firstElement = queue.pollFirst();
SomeObject firstElement = queue.pollFirst(10, TimeUnit.MINUTES);
SomeObject firstElement = queue.takeFirst();

SomeObject lastElement = queue.peekLast();
SomeObject lastElement = queue.pollLast();
SomeObject lastElement = queue.pollLast(10, TimeUnit.MINUTES);
SomeObject lastElement = queue.takeLast();
```

该功能仅限于Redisson PRO版本。

### 7.15. 延迟队列（Delayed Queue）

基于Redis的Redisson分布式延迟队列（Delayed Queue）结构的RDelayedQueue Java对象在实现了RQueue接口的基础上提供了向队列按要求延迟添加项目的功能。该功能可以用来实现消息传送延迟按几何增长或几何衰减的发送策略。

```java
RQueue<String> distinationQueue = ...
RDelayedQueue<String> delayedQueue = getDelayedQueue(distinationQueue);
// 10秒钟以后将消息发送到指定队列
delayedQueue.offer("msg1", 10, TimeUnit.SECONDS);
// 一分钟以后将消息发送到指定队列
delayedQueue.offer("msg2", 1, TimeUnit.MINUTES);

```

在该对象不再需要的情况下，应该主动销毁。仅在相关的Redisson对象也需要关闭的时候可以不用主动销毁。

```java
RDelayedQueue<String> delayedQueue = ...
delayedQueue.destroy();
```

### 7.16. 优先队列（Priority Queue）

基于Redis的Redisson分布式优先队列（Priority Queue）Java对象实现了java.util.Queue的接口。可以通过比较器（Comparator）接口来对元素排序。

```java
RPriorityQueue<Integer> queue = redisson.getPriorityQueue("anyQueue");
queue.trySetComparator(new MyComparator()); // 指定对象比较器
queue.add(3);
queue.add(1);
queue.add(2);

queue.removeAsync(0);
queue.addAsync(5);

queue.poll();
```

### 7.17. 优先双端队列（Priority Deque）

基于Redis的Redisson分布式优先双端队列（Priority Deque）Java对象实现了java.util.Deque的接口。可以通过比较器（Comparator）接口来对元素排序。

```java
RPriorityDeque<Integer> queue = redisson.getPriorityDeque("anyQueue");
queue.trySetComparator(new MyComparator()); // 指定对象比较器
queue.addLast(3);
queue.addFirst(1);
queue.add(2);

queue.removeAsync(0);
queue.addAsync(5);

queue.pollFirst();
queue.pollLast();
```

### 7.18. 优先阻塞队列（Priority Blocking Queue）

基于Redis的分布式无界优先阻塞队列（Priority Blocking Queue）Java对象的结构与java.util.concurrent.PriorityBlockingQueue类似。可以通过比较器（Comparator）接口来对元素排序。PriorityBlockingQueue的最大容量是4 294 967 295个元素。

```java
RPriorityBlockingQueue<Integer> queue = redisson.getPriorityBlockingQueue("anyQueue");
queue.trySetComparator(new MyComparator()); // 指定对象比较器
queue.add(3);
queue.add(1);
queue.add(2);

queue.removeAsync(0);
queue.addAsync(5);

queue.take();
```

当Redis服务端断线重连以后，或Redis服务端发生主从切换，并重新建立连接后，断线时正在使用poll，pollLastAndOfferFirstTo或take方法的对象Redisson将自动再次为其订阅相关的话题。

### 7.19. 优先阻塞双端队列（Priority Blocking Deque）

基于Redis的分布式无界优先阻塞双端队列（Priority Blocking Deque）Java对象实现了java.util.Deque的接口。addLast、 addFirst、push方法不能再这个对里使用。PriorityBlockingDeque的最大容量是4 294 967 295个元素。

```java
RPriorityBlockingDeque<Integer> queue = redisson.getPriorityBlockingDeque("anyQueue");
queue.trySetComparator(new MyComparator()); // 指定对象比较器
queue.add(2);

queue.removeAsync(0);
queue.addAsync(5);

queue.pollFirst();
queue.pollLast();
queue.takeFirst();
queue.takeLast();
```

当Redis服务端断线重连以后，或Redis服务端发生主从切换，并重新建立连接后，断线时正在使用poll，pollLastAndOfferFirstTo或take方法的对象Redisson将自动再次为其订阅相关的话题。

本文转自 <https://blog.csdn.net/A_art_xiang/article/details/125525864>，如有侵权，请联系删除。