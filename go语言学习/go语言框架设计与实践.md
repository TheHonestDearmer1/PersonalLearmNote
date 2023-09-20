

## 字节跳动】第十四讲 HTTP框架修炼之道｜ 青训营笔记

发布于 2022-08-22 13:56:45

2300

举报

**讲师介绍**

伊旭然：

去年毕业于北京邮电大学计算机相关专业毕业，在校期间做过前端、后端、基础架构、游玩过全国2/3的省份

# **课程背景**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/c4e0f5e86e7ad8d5955067cbf3ba921c.png)

1.png

**目录**

1. 再谈HTTP协议
2. HTTP框架的设计与实现
3. 性能修炼之道
4. 企业实践

# **1. 再谈HTTP协议**

本节介绍：HTTP协议是什么、协议里有什么、请求流程、不足与展望

## **1.1 HTTP 协议是什么**

HTTP：超文本传输协议(Hypertext Transfer Protocol)

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/da4d8579677ea04cd45d5808c7014c9f.png)

2.png

**为什么需要协议？**

首先协议都是字符流，一定需要边界，有了边界我们需要知道内容的类型，就可以把内容放进消息对应的地方，之后进行传输，这就是简单的协议

## **1.2 协议里有什么**

一个常见的POST请求在协议层究竟做了什么？

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/3d2587353f557fe502ae6d347cf260b7.png)

3.png

```
讲师举了一个场景，你要和小姐姐交流去请她看电影。然后就是把请小姐姐看电影这句话，把它转换成一个真实的http协议。可以看到这个协议里面的第一行是从post开始打头，然后一个空格之后接上的URL然后接下来又是一个空格，然后接上一个HTTP1.1，这看着像是一个HD当前版本的一个描述。这就是协议里面的描述。然后再一个大空行之后，我们可以看到我们真实的一个想说的话，也就是body部分：lets watch a movie totogether tonight 那之后这个协议结束了。那我们可以看到那我们的协议的开始，那其实就是我们的这个post这一行开始，只要我们对端检测到这一行的内容后，就可以接收我们的协议了。那协议的结束就是我们这个Let‘s watch a movie together tonight 最后我们再加上那一个换行之后就结束掉了我们的这个协议。然后同时我们可以看到源数据里面有一个叫做content Length的一个描述，这个是协议的关键的一个header 它描述的是我们的body到底有多少个字节。所以我们的server 端就是我们的小姐姐端就能根据这个字节来指定去接收多少个字节的数据，这样就能拿到我们完整的一个消息了。OK这是我们请求的一个真实的场景。那我们小姐姐肯定会给我们一个回复对吧？那回复其实可以看到非常类似，我们回复其实也是有一个first line.first line 的话它是由我们的一个http 1.1是一个版本的开始，然后空格，然后200是一个状态码，然后再一个空格，然后又是一个OK OK的话就是一个我们对应200的一个状态码的一个文字描述，然后最后是一些源数据，然后最后是小姐姐回复的一个OK，这就是小姐姐响应的完整的协议了。
```

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/d4af789c81474c0a243776ce98e93dde.png)

4.png

```
首先是一个请求行，状态码，然后就是一些元数据请求头响应头。最后就是一个请求响应体。那针对我们的请求行，它是由方法名、URL和协议版本组成，那方法名其实就是比较多了，我们常见的方法名就是get 就是http 0.9里面唯一的一个方法。然后1.0里面扩充了header和post然后1.1里面又陆陆续续扩充了5个，然后从put开始到trace然后最终到一个patch。patch是1.1之后额外增加的一个方法名，但是使用比较广泛。
```

**pathc和put具体有些什么区别吗？**

pathc就是部分更新，put它的语义就是完整的更新，所以它一个比较细微的一个区别在（PUT是幂等的，而PATCH不是幂等的。）

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/36d4263854697040f10a73cbccbb9ed1.png)

5.png

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/651c9bf3c70851b9d1afa4b96e72f76c.png)

6.png

## **1.3 请求流程**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/6f239e0e23b78997bd35d907715465f0.png)

7.png

**根据上述小姐姐案例的一个请求流程**

## **1.4 不足与展望**

- HTTP1
  - 队头阻塞
  - 传输效率低
  - 明文传输不安全
- HTTP2
  - 多路复用
  - 头部压缩
  - 二进制协议
- QUIC
  - 基于UDP展现
  - 解决队头阻塞
  - 加密减少握手次数
  - 支持快速启动

## **1.5 小结**

- HTTP协议出现的背景
- 协议里有什么
- 请求流程
- 不足与展望

# **2. HTTP框架的设计与实现**

## **2.1 分层设计**

- 专注性
- 扩展性
- 复用性

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/8d99fb074e1029f41ec0aeddd3adf48a.png)

8.png

- 高内聚 低耦合
- 易复用
- 高扩展性

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/36eb3433d37971b1657c47b349299eca.png)

9.png

**从上往下总共分为五层，层与层之前使用接口解耦。**

- 第一层：应用层，跟用户之间打交道的一层，这一层会对请求进行一个抽象，包括request response context等等。这一层也会提供丰富的易用的API。
- 第二层：[中间件](https://cloud.tencent.com/product/tdmq?from_column=20420&from=20420)层，可以对请求有一些预处理和后处理的逻辑，像大一些accesslog，打一些耗时的点。其他中间件比如Reacovery中间件用于捕获Panic。
- 第三层：路由层，路由层的话就是我们会有一个原生的路由实现来提供大家类似于跟注册、路由寻址的一些操作。
- 第四层：协议层，现在的http1.1已经不能够满足我们所有的需求了，需要支持H2、Quic等等，甚至是在TLS握手之后的ALPN协商升级操作，那这些都需要能够很方便的支持。
- 第五层：网络层，不同的网络库使用的场景并不相同，我们也需要一个灵活替换网络库的能力。Common层主要放一些公共逻辑，这一部分可能每一层都会使用。

**两种设计进行对比：**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/36eb3433d37971b1657c47b349299eca.png)

11.png

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/b7c61f464e73c28842b5c8cff13fc62b.png)

10.png

**一个切实可行的复杂系统势必是从一个切实可行的简单系统发展而来的。从头开始设计的复杂系统根本不切实可行，无法修修补补让它切实可行。你必须由一个切实可行的简单系统重新开始。-- 盖尔定律**

## **2.2 应用层设计**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/49ca41836d5201dcf4ec0f6be791cac2.png)

12.png

**提供合理的 API**

- 可理解性：如ctx.Body(), ctx.GetBody(),不要用 ctx.BodyA()
- 简单性：如ctx.Request.Header.Peek(key) / ctx.GetHeader(key)
- 冗余性：不需要冗余或能通过其他API组合得到的API
- 兼容性：尽管避免break change，做好版本管理
- 可测性：写的接口是需要可测试的
- 可见性：最小暴露原则，不需要暴露的API不暴露，可以抽象为接口。

## **2.3 中间件设计**

**中间件需求：**

- 配合Handler实现一个完整的请求
- 拥有预处理逻辑与后处理逻辑
- 可以注册多中间件
- 对上层模块用户逻辑模块易用

**洋葱模型:**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/77a8db94119adf3e29af6066f0295586.png)

13.png

**适用场景：**

- 日志记录
- 性能统计
- 安全控制
- 事务处理
- 异常处理

**核心逻辑与通用逻辑分离**

举个例子：

打印每个请求的request 和 response

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/67781b2f8721d0bad8f060643cd625bd.png)

14.png

**1. 既然要实现预处理和后处理，那这个就很像调用了一个函数**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/7149f66e8dab0f02c4b145ca4c7e63d9.png)

15.png

**将nextMiddleware() 统称为Next()**   //nextMiddleware 下一个中间件

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/c8afa490e6e9ce782ce599c539457a6b.png)

16.png

**2. 路由上可以注册多个Middleware，同时也可以满足请求级别有效只需要将Middleware 设计为和业务和Handler相同即可。**

**3. 用户如果不主动调用下一个处理函数怎么办？**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/e3403434cd99cea40e000b22a76cb4c2.png)

17.png

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/a128e2ce027212a3424ce9c11a867b60.png)

18.png

**核心：在任何场景下index保证递增**

**4. 出现异常想停止怎么办？**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/840b102079c0f1cbc12950cfa23480f6.png)

19.png

**调用链：**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/3d3e1d7110922edc60745781a420f311.png)

20.png

有没有什么坑呢？

不在一个调用栈上

**适用场景：**

- 不调用Next：初始化逻辑且不需要在同一个调用栈
- 调用Next：后处理逻辑或需要在同一调用栈上

**思考：有没有其他实现中间件的方式**

## **2.4 路由设计**

框架路由实际上就是为了URL 匹配对应的处理函数（Handlers）

- 静态路由：/a/b/c、/a/b/d
- 参数路由：/a/:id/c (/a/b/c, /a/d/c)、/*all
- 路由修复：/a/b <-> /a/b/
- 冲突路由以及优先级：/a/b、/：id/c
- 匹配HTTP方法
- 多处理函数：方便添加中间件
- ...

**青铜：map[string]handlers**

/a/b/c、/a/b/d /a/:id/c、/*all

**黄金：前缀匹配树**

/a/b/c、/a/b/d

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/cc12ab8f73a2527705981afac1bfe772.png)

21.png

/a/b/c

/a/d/d

/a/:b/d

/a/:c/f

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/4a80833de2a5308e5516a8cae455d6b8.png)

22.png

**如何匹配HTTP方法？**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/4d97d0cb92af9f9320999b41e0d42bae.png)

路由映射表

**外层Map：根据method 进行初步筛选**

**如何实现添加多处理函数？**

**在每个节点上适用一个list存储handler**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/4f0c31f9879ab7802b0156300fbb02cc.png)

24.png

**思考：如何查找路由**

如何做设计

1. 明确需求：考虑清楚要解决什么问题、有哪些需求
2. 业界调研：业界都有哪些解决方案可供参考
3. 方案权衡：思考不同方案的取舍
4. 方案评审：相关同学对不同方案做评审
5. 确定开发：确定最合适的方案进行开发

## **2.5 协议层设计**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/19f7175bcd40959e7fa5ea4c3f2e06f8.png)

25.png

**抽象出合适的接口：**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/83a3671fa9fec04cc63dc09df0596ad7.png)

26.png

**官方说明：**

1. Do not store Contexts inside a struct type; instead, pass a Context explicitly to each function that needs it. The Context should be the first parameter.
2. 需要在连接上读写数据

## **2.6 网络层设计**

**BIO(阻塞IO)**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/e0c2d36d89d86097ee381d738d3b7ad5.png)

27.png

**NIO(非阻塞)**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/6146a897f27cb031e9c6bbc8cd3b0993.png)

28.png

**go net "BIO" 用户管理 buffer**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/dde7cf573d33f717b63a6340c5c26834.png)

29.png

**netpoll NIO 网络管理 buffer**

netpoll地址：https://github.com/cloudwego/netpoll

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/a2ea73d6583a8a7373dff64bc869510a.png)

30.png

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/017b0fc142cd2b4a905b5c62b3e4d0f3.png)

31.png

## **2.7 小结**

- API 设计：可理解性、简单性...
- 中间件设计：洋葱模型
- 路由设计：前缀匹配树
- 协议层设计：抽象出合适的接口
- 网络层设计：网络模型

# **3. 性能修炼之道**

- 针对网络库的优化
- 针对协议的优化

## **3.1 针对网络库的优化**

**go net "BIO"**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/1cc60b2935a0488e90d8679a6b881662.png)

32.png

go net

- 存下全部Heaher
- 减少系统调用次数
- 能够复用内存
- 能够多次读

**go net with bufio**

绑定一块缓冲区

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/0eb511e32bdb3fba91f98265f922e28d.png)

33.png

**netpoll**

存下全部Header 拷贝出完整的Body

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/6eb8de73b30d32fae10c73ad40e8a55b.png)

34.png

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/83675c261770e5aee15938748b23e1dc.png)

35.png

**go net**

- 流式友好
- 小包性能高

**netpoll**

- 中大包性能高
- 时延低

## **3.2 针对协议的优化 -- Headers 解析**

找到Header Line 边界: \r\n

对于这种情况也可以适用上课学习的知识例如kmp，当然这些算法也不是很快，对于边界处理也不是最优

所以我们先找到\n 再看它前一个是不是 \r

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/e6c9e68b8db3d54acac6cf80b8750240.png)

36.png

**有没有更快的找到\n的方法呢？SIMD？**

SIMD：全称Single Instruction Multiple Data，单指令多数据流，能够复制多个操作数，并把它们打包在大型寄存器的一组指令集。

相关代码链接：https://github.con/golang/go/blob/9abacc83c853c17700c44e336e2d3e2oOfe9a72b/ src/internal/bytealg/indexbyte_amd64. s#lL8

json解析库：Sonic，https://github.com/bytedance/sonic(由字节内部开源的，目前这个库是最快的)

**适用SIMD加速和未使用比较**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/a0ad11a78d7a9bdf2899730af101a192.png)

37.png

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/7d094f10c8af21f8f9ad7ff81fd63180.png)

38.png

**针对协议相关的Headers快速解析：**

1. 通过 Header key 首字母快速筛除掉完全不可能的key
2. 解析对应value到独立字段
3. 使用 byte slice 管理对应 header 存储，方便复用

**请求体中同样处理的Key：**

User-Agent、Content-Type、Content-Length、Connection、Transfer-Encoding

**取**

- 核心字段快速解析
- 使用byte slice存储
- 额外存储到成员变量中

**舍**

- 普通 header 性能较低
- 没有map结构

## **3.3 针对协议的优化 -- Header key 规范化**

aaa-bbb --> Aaa-Bbb

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/c34eaf88a3c17d900b2ad9242a83bcf2.png)

39.png

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/772da9b647397b3029b5f31df99b3b5d.png)

40.png

**取**

- 超高的转换效率
- 比net.http 提高40倍

**舍**

- 额外的内存开销
- 变更困难

## **3.4 热点资源池化**

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/2759670e55a2a77b028a7c3f25677f78.png)

41.png

![img](https://ask.qcloudimg.com/http-save/yehe-9978966/0d393b8f607f071004ba682b94adc8a1.png)

42.png

**取**

- 减少了内存分配
- 提高了内存复用
- 降低了GC压力
- 性能提升

**舍**

- 额外的Reset逻辑
- 请求内有效
- 问题定位难度增加

## **3.5 小结**

- 针对网络库的优化：buffer 设计
- 针对协议的优化：header解析、热点资源池化

# **4. 企业实践**

讲师进入公司以来一直学习的

- 追求性能
- 追求易用，减少误用
- 打通内部生态
- 文档建设、用户群建设

目前内部有HTTP框架：Hertz

1万+服务 3千万+QPS

# **课程总结**

- HTTP 协议的相关知识
- HTTP 框架的一般设计
- HTTP 框架的优化手段
- 企业实践

