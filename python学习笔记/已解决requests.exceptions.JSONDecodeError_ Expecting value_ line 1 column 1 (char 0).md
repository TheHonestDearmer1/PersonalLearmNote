 

已解决requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)  
  
  
  
  
  

* * *

#### 文章目录

*   [报错问题](#_18)
*   [报错翻译](#_49)
*   [报错原因](#_63)
*   [解决方法](#_80)
*   [千人全栈VIP答疑群联系博主帮忙解决报错](#VIP_122)

* * *

  
  
  

报错问题
----

  
  

粉丝群一个小伙伴，想用[Python爬取](https://so.csdn.net/so/search?q=Python%E7%88%AC%E5%8F%96&spm=1001.2101.3001.7020)网页，但是发生了报错（当时他心里瞬间凉了一大截，跑来找我求助，然后顺利帮助他解决了，顺便记录一下希望可以帮助到更多遇到这个bug不会解决的小伙伴）

  

![在这里插入图片描述](https://img-blog.csdnimg.cn/933e661f49f6435cbc610050d9eb4dbb.png)

```python
res = requests.post(post_url, headers=self.headers, json=data)
res.encoding = 'utf-8'
print(res.json())
```

  

**报错信息截图如下所示**：  
  

![在这里插入图片描述](https://img-blog.csdnimg.cn/efefa165d48b438f9a7cbc2bc98c1e2a.png)

  
  
  

报错翻译
----

  
  

**报错翻译如下：**  
  

请求.异常：JSON解码错误：应为值：第1行第1列（字符0）  
  
  
  
  
  

报错原因
----

  
  

**报错原因**：

这里是获取 response.json() 获取响应的json字典数据, 因为你请求返回的数据不是完整的[json数据格式](https://so.csdn.net/so/search?q=json%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F&spm=1001.2101.3001.7020), 所以从而导致报错

小伙伴按下面的方法分析判断自己代码的报错原因即可解决！！！  
  
  
  
  
  

解决方法
----

  
  

**第一步：首先得确定网页返回的是否是JSON数据，开发者工具 》网络 》响应头中查看响应类型：**  
  
  
![在这里插入图片描述](https://img-blog.csdnimg.cn/cf51fbbfcbfc451094e63d31db5aea51.png)

  

**第二步： `res.content.decode("utf-8")` 查看返回数据效果**

![在这里插入图片描述](https://img-blog.csdnimg.cn/397fb252e617460fab40eaca6e9b5764.png)  
可以看到上面红框部分返回不是完整的json数据,，反而多了一部分内容。说明不能用`res.json()`去打印  
  

**第三步：竟然不是一个完整的JSON数据，那我们是否可以那多余的那部分给替换掉为空就好了？**

```python
data = res.content.decode("utf-8")
# 1. 利用正则把开头多余的替换为空字符串
data = re.sub("jQuery180008241254755365413_1671790451896\(",'',data)
# 2. 正则把最后那个)给替换为空字符串
data = re.sub("\)$", '', data)
print(data)
print(type(data)) # 此时打印data的类型还是字符串：<class 'str'>
# 3. 利用eval将类型转换为字典
data = eval(data)
print(data)
print(type(data)) # 此时打印data的类型为：<class 'dict'>
```

  

**以上是此问题报错原因的解决方法，欢迎评论区留言讨论是否能解决，如果有用欢迎点赞收藏文章谢谢支持，博主才有动力持续记录遇到的问题！！！**

千人全栈VIP答疑群联系博主帮忙解决报错
--------------------

**由于博主时间精力有限，每天私信人数太多，没办法每个粉丝都及时回复，所以优先回复VIP粉丝，可以通过订阅限时9.9付费专栏[《100天精通Python从入门到就业》](https://blog.csdn.net/yuan2019035055/category_11466020.html)进入千人全栈VIP答疑群，获得优先解答机会（代码指导、远程服务），白嫖80G学习资料大礼包，专栏订阅地址：[https://blog.csdn.net/yuan2019035055/category\_11466020.html](https://blog.csdn.net/yuan2019035055/category_11466020.html)**

*   **优点**：作者优先解答机会（代码指导、远程服务），群里大佬众多可以抱团取暖（大厂内推机会），此专栏文章是专门针对零基础和需要进阶提升的同学所准备的一套完整教学，从0到100的不断进阶深入，后续还有实战项目，轻松应对面试！
    
*   **专栏福利**：简历指导、招聘内推、每周送实体书、80G全栈学习视频、300本IT电子书：Python、Java、前端、大数据、数据库、算法、爬虫、数据分析、机器学习、面试题库等等
    
*   **注意**：如果希望得到及时回复，和大佬们交流学习，订阅专栏后私信博主进千人VIP答疑群![在这里插入图片描述](https://img-blog.csdnimg.cn/b58bb765c2fc4b6abac91c2e433dd06f.png)  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/9c855cea92904ab5b9575e637bdf5ea4.png)
    

免费资料获取，更多粉丝福利，关注下方公众号获取

![在这里插入图片描述](https://img-blog.csdnimg.cn/a74f7d5d03234f7c8a635562034442a0.gif#pic_center)

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Python入门技能树](https://edu.csdn.net/skill/python/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/python/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/python/?utm_source=csdn_ai_skill_tree_blog)370667 人正在系统学习中

![](https://img-blog.csdnimg.cn/d0113d9d8ff64adba84b2f9528d0f6de.png)

袁袁袁袁满

![](https://g.csdnimg.cn/extension-box/1.1.6/image/weixin.png) 微信公众号 ![](https://g.csdnimg.cn/extension-box/1.1.6/image/ic_move.png)

商务合作 | 交流学习 | 资料领取

本文转自 <https://blog.csdn.net/yuan2019035055/article/details/128308170?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-1-128308170-blog-127053383.235%5Ev38%5Epc_relevant_sort&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-1-128308170-blog-127053383.235%5Ev38%5Epc_relevant_sort&utm_relevant_index=1>，如有侵权，请联系删除。