 

**Xpath常用的定位方法**

相信做过[selenium](https://so.csdn.net/so/search?q=selenium&spm=1001.2101.3001.7020) UI自动化的朋友都知道，工作中大部分的元素定位都是使用xpath进行定位，所以xpath是UI自动化工作中非常重要的一个环节，所以我单独整理出来一篇博客出来~~希望对大家有帮助~

**相对定位**

相对定位是两个杠表示“//”，相对路径易维护  
![在这里插入图片描述](https://img-blog.csdnimg.cn/2021033110111174.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)  
**绝对路径**

绝对定位用一个杠“/”， 绝对路径一个层级变化所有空间都有变化

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210331101234227.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)

```python
/html/body/div[1]/section/section/main/div[2]/div[2]/div[1]/div[2]/button[1]/span
```

**last()方法**  
当标签存在多个相同的时候，可以使用[xpath](https://so.csdn.net/so/search?q=xpath&spm=1001.2101.3001.7020)中的last()方法，定位到最后一个  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210330183135443.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)

```python
//标签名[last()]
//span/ul//li[last()]
```

如果我们要定位到倒数第二个，可以在last() 后面加上 -1，代表倒数第二个  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210330183212491.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)

```python
//标签名[last()-1]
//span/ul//li[last()-1]
```

**属性查找@**

如，这里我们以百度为例，如果我们要定位到百度的id元素，那么可以使用 //标签名\[@元素名称=‘元素值’\]  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210330183751992.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)

```python
 //标签名[@元素名称='元素值']
//input[@id='kw']
```

**xpath逻辑表达式-and**

当一个元素无法定位到唯一值得时候，我们可以使用and表达式，同一个标签下定位多个元素  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210330184131661.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)

```python

//标签名[@元素名称='元素值' and @元素名称='元素值']
//input[@id='kw' and @class='s_ipt']
```

**xpath表达式-or**

xpath 中 or的表达式和and很像，指的是当你元素满足其中一个条件的时候，就可以定位到，如图，在百度搜索框中，我们故意将@class='s\_t’元素写错，内容中并没有这个元素，

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210330184337690.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)

```python
// 标签名[@元素名称='元素值' or @元素名称='元素值']
//input[@id='kw' or @class='s_t']
```

**非查找控件**

如图，如果我们想要查找元素值不等于某个值的内容，可以使用！=方法，但是这个方法在工作中用的比较少，目前我还没有用到过，不过xapth提供了这个方法，可以结合场景使用~  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210330184818162.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)

```python
//标签名称[@元素名称 != '元素值']
//input[@class!='1111']
```

**Not查找**

```python
//标签名[not(.='元素值')
//year[not(.=2005)]
//div[not(@id="tab-AndroidVersions")]
```

这里没有找到合适的场景，意思就是查找year内容不为2005的内容 注：“.”就等于text()

**模糊匹配**

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210331095748860.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)

```python
//标签名[contains(text(), "内容"]
//div[contains(text(), "更新")]
```

这里的意思是模糊查询内容包含“更新”的元素

**精准匹配**

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210331100116791.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)

```python
//标签名[(text()='内容')]
//div[(text()='更新文案')]
```

**使用大于小于符号定位**

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210331100716514.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)

```python
//div[@class="cell" and text()>'1336']
//div[@class="cell" and text()<'1336']
```

如图，当我们商品列表中有多个商品ID，那我们想要定位到ID大于或者小于1336的数据，可以通过上面的方式。

**轴方式定位**

```python
轴表达式说明

parent::* ：表示当前节点的父节点元素

ancestor::* ：表示当前节点的祖先节点元素

child::* ：表示当前节点的子元素 /A/descendant::* 表示A的所有后代元素

self::* ：表示当前节点的自身元素

ancestor-or-self::* ：表示当前节点的及它的祖先节点元素

descendant-or-self::* ：表示当前节点的及它们的后代元素

following-sibling::* ：表示当前节点的后序所有兄弟节点元素

preceding-sibling::* ：表示当前节点的前面所有兄弟节点元素

following::* ：表示当前节点的后序所有元素

preceding::* ：表示当前节点的所有元素
```

1.  __parent::_ 当前节点的父节点元素_\*

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210331101924438.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)

```python
//div[@class="cell" and text()='1338']/parent::*
```

如图，我们要定位到ID为1338元素的父节点元素，可以使用如上xpath轴定位, “\*” 表示匹配所有

2.  **following-sibling::**

```python
/bookstore/book[1]/following-sibling::*
```

查找books1所有的同级元素都查找出来，“\*”表示所有

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210331104307440.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)

```python
//div[3]/table/tbody/tr[1]/td[1]/following-sibling::td[2]
```

查找td\[1\]下同级节点下的第二个节点  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210331104424368.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)  
3\. following-sibling::当前节点的前面所有兄弟节点元素

```python
/bookstore/book[2]/year/preceding-sibling::*
```

意思是：查找books\[2\]下year前的同级节点

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210331105636913.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)

4.  查找节点的父辈

```python
/bookstore/book[2]/year/parent::*
```

5.  查找节点的子辈

```python
/bookstore/book[2]/descendant::*
```

**使用position位置定位**

意思是定位到th标签下的第一个

```python
//th[@class="c-id " and position()=1]
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210331114507852.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)  
也可以//th\[@class="c-id " and position()<2\] 这样用~

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Python入门技能树](https://edu.csdn.net/skill/python/python-3-152?utm_source=csdn_ai_skill_tree_blog)[网络爬虫](https://edu.csdn.net/skill/python/python-3-152?utm_source=csdn_ai_skill_tree_blog)[Selenium](https://edu.csdn.net/skill/python/python-3-152?utm_source=csdn_ai_skill_tree_blog)369481 人正在系统学习中

本文转自 <https://blog.csdn.net/weixin_43865008/article/details/115332404>，如有侵权，请联系删除。