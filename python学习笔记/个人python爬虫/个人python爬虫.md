# python爬虫

```python
#编码和文件操作
open("XXX",mode="abc",encoding="utf-8") 
#从库中导入模块
form urllib.request import urlopen
```

### 写第一个爬虫程序

```python
from urllib.request import urlopen

url = "http://www.baidu.com"
resp=urlopen(url) #打开这个网址，得到响应
print(resp.read().decode("utf-8"))#read打印响应，decode解码响应，当要打印在文件的时候这个要去掉，不然打印不出来
with open("baidu.html",mode="w",encoding="utf-8") as f:  #打印在文件中
    f.write(resp.read().decode("utf-8"))   #将文本打进在文件中
```

1.服务器渲染：在服务器那百年直接把数据和html整合在一起，统一返回给浏览器。在页面源代码中能看到数据

2.客户端渲染：第一次请求只要一个html骨架，第二次请求拿到数据，进行数据展示。在页面源代码看不到数据。

熟练使用浏览器开发工具，可以监控网络请求

### HTTP协议

超文本传输协议，也就是传输html

请求：

```
请求行  url
请求头  附加内容
请求体  参数
```



响应：

```
状态行  协议  状态码
响应头  附加信息

响应体  服务器返回的真正客户端内容（html，json）
```

header里面需要的：

```
请求头中最常⻅的⼀些重要内容(爬⾍需要):

1. User-Agent : 请求载体的身份标识(⽤啥发送的请求)

2. Referer: 防盗链(这次请求是从哪个⻚⾯来的? 反爬会⽤到)

3. cookie: 本地字符串数据信息(⽤户登录信息, 反爬的token)

响应头中⼀些重要的内容:

1. cookie: 本地字符串数据信息(⽤户登录信息, 反爬的token)

2. 各种神奇的莫名其妙的字符串(这个需要经验了, ⼀般都是token

字样, 防⽌各种攻击和反爬)

请求⽅式:

GET: 显示提交POST: 隐示提交
```



### requests入门

#### 第一小节（get）

在前⾯⼩节中, 我们使⽤urllib来抓取⻚⾯源代码. 这个是python内置

的⼀个模块. 但是, 它并不是我们常⽤的爬⾍⼯具. 常⽤的抓取⻚⾯的

模块通常使⽤⼀个第三⽅模块requests. 这个模块的优势就是⽐urllib

还要简单, 并且处理各种请求都⽐较⽅便.

既然是第三⽅模块, 那就需要我们对该模块进⾏安装, 安装⽅法:

```python
pip install requests
```

如果安装速度慢的话可以临时使用国内的源进⾏下载安装.

```python
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
```

![image-20230713162722914](图片/1.png)

标准爬虫

```python
import  requests

url = "https://www.baidu.com/s?tn=44004473_8_oem_dg&ie=utf-8&wd=周杰伦"

header={
    "User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79" #模仿浏览器运行
}
resp=requests.get(url,headers=header) #地址栏写着的地址
print(resp.text)
```

给搜索加变量

```python
import  requests

query = input("输入搜索")
url = f"https://www.baidu.com/s?tn=44004473_8_oem_dg&ie=utf-8&wd={query}"

header={
  "cookie":"ssuid=940679152; SUID=D23AE7781F49910A00000000639ACC7E; IPLOC=CN4403; cuid=AAH+mBAFRgAAAAqHS07gkAEANgg=; SUV=1689238283241317; browerV=3; osV=1; ABTEST=5|1689238286|v17; SNUID=E6AF88700700065C771F641F07FB38FE; sst0=286; LSTMV=106%2C28; LCLKINT=2712"
    ,
    "User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79" #模仿浏览器运行
}
resp=requests.get(url,headers=header) #地址栏写着的地址
print(resp.text)
```

#### 第二小节（post）

post请求是在开发人员工具中网络调试看到网页动态变化出来的数据的请求

from data （表单数据）

在headers（标头）旁边（右边），有一个[payload](https://so.csdn.net/so/search?q=payload&spm=1001.2101.3001.7020)（负载），在这里有from data数据

```python
# 案例2.抓取百度翻译数据

# 准备参数
kw = input("请输⼊你要翻译的英语单词:")
dic = {
 "kw": kw # 这⾥要和抓包⼯具⾥的参数⼀致.
 }
 # 请注意百度翻译的sug这个url. 它是通过post⽅式进⾏提交
的. 所以我们也要模拟post请求
resp =
requests.post("https://fanyi.baidu.com/sug",
data=dic)
10
 # 返回值是json 那就可以直接解析成json
 resp_json = resp.json()
 # {'errno': 0, 'data': [{'k': 'Apple', 'v': 'n.
苹果公司，原称苹果电脑公司'....
 print(resp_json['data'][0]['v']) # 拿到返回字典中的
内容
```

#### 第三小节 （params）

get请求，标题params，如果请求文本没有数据就说明被反爬虫了

```python
import  requests

url = "https://movie.douban.com/j/chart/top_list"

#重新封装参数
param = {
"type": "24",
"interval_id": "100:90",
"action": "",
"start": 0,
"limit:": 20
}
#反反爬虫
headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.86"
}
resp=requests.get(url=url,params=param,headers=headers) #地址栏写着的地址,data是要发送的数据
for i in range(20) :
 print(resp.json())
resp.close()#关掉resp,不然容易被封
```

### 数据分析

#### 正则表达式

Regular Expression, 正则表达式, ⼀种使⽤表达式的⽅式对字符串

进⾏匹配的语法规则.

我们抓取到的⽹⻚源代码本质上就是⼀个超⻓的字符串, 想从⾥⾯提

取内容.⽤正则再合适不过了.

正则的优点: 速度快, 效率⾼, 准确性⾼ 正则的缺点: 新⼿上⼿难度有

点⼉⾼.

不过只要掌握了正则编写的逻辑关系, 写出⼀个提取⻚⾯内容的正则

其实并不复杂

正则的语法: 使⽤元字符进⾏排列组合⽤来匹配字符串 在线测试正

则表达式https://tool.oschina.net/regex/

元字符: 具有固定含义的特殊符号 常⽤元字符:

```python
1 . 匹配除换⾏符以外的任意字符
2 \w 匹配字⺟或数字或下划线
3 \s 匹配任意的空⽩符
4 \d 匹配数字
5 \n 匹配⼀个换⾏符
6 \t 匹配⼀个制表符
7 \r 回车
8 ^ 匹配字符串的开始
9 $ 匹配字符串的结尾
10
11 \W 匹配⾮字⺟或数字或下划线
12 \D 匹配⾮数字
13 \S 匹配⾮空⽩符
14 a|b 匹配字符a或字符b
15 () 匹配括号内的表达式，也表示⼀个组
16 [...] 匹配字符组中的字符        *
17 [^...] 匹配除了字符组中字符的所有字符       *
```

量词: 控制前⾯的元字符出现的次数

```python
1 * 重复零次或更多次
2 + 重复⼀次或更多次
3 ? 重复零次或⼀次
4 {n} 重复n次
5 {n,} 重复n次或更多次
6 {n,m} 重复n到m次
```

贪婪匹配和惰性匹配

```python
1 .* 贪婪匹配
2 .*? 惰性匹配
```

这两个要着重的说⼀下. 因为我们写爬⾍⽤的最多的就是这个惰性匹配.

先看案例

```python
1 str: 玩⼉吃鸡游戏, 晚上⼀起上游戏, ⼲嘛呢? 打游戏啊
2 reg: 玩⼉.*?游戏
3
4 此时匹配的是: 玩⼉吃鸡游戏
5
6 reg: 玩⼉.*游戏 
7 此时匹配的是: 玩⼉吃鸡游戏, 晚上⼀起上游戏, ⼲嘛呢? 打游
戏 
8 
9 
10 str: <div>胡辣汤</div>
11 reg: <.*>
12 结果: <div>胡辣汤</div>
13
14
15 str: <div>胡辣汤</div>
16 reg: <.*?>
17 结果:
```

#### re模块

```python
import re
# findall: 匹配字符串中所有的符合正则的内容
lst = re.findall(r"\d+","我的电话号是：10086")
print(lst)  #结果为['10086']

#finditer: 匹配字符串中所有的内容[返回的是迭代器]
it = re.finditer(r"\d+","我的电话号是：10086")
for i in it:
    print(i) #结果为<_sre.SRE_Match object; span=(7, 12), match='10086'>
    print(i.group()) #结果为10086
    
    #rearch: 匹配字符串中所有的内容[返回的是迭代器],找到一个结果就返回
it = re.rearch(r"\d+","我的电话号是：10086") #找到一个结果就返回
for i in it:
    print(i) #结果为<_sre.SRE_Match object; span=(7, 12), match='10086'>
    print(i.group()) #结果为10086
    
        #match:匹配开头就是数字的
it = re.match(r"\d+","10086") #找到一个结果就返回
    print(i.group()) #结果为10086
    
    #预加载正则表达式
    obj = re.compile(r"\d+")
    
    ret = obj.finditer("我的电话号是:10086,我女朋友的电话号码是:10010")
    for it in ret:
        print(it.group()) #10086 10010
```

```python
S = """
<div class='jay'><span id= '1'>郭麒麟</span></div>
<div class='jj'>espan id='2'>宋铁</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡说八道</span></div>
"""
obj = re.compile(r"<div class=',*?'><span id='(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>", re.S) # re.S能够识别换行
result = obj.finditer(s)
for it in result:
    print(it.group("wahaha"))
    print(it.group("id"))
    
    
    #结果为郭麒麟 1 宋铁 2 大聪明 3 范思哲 4 胡说八道 5
```

#### ⼿刃⾖瓣TOP250电影信息

⽬标: 抓取"电影名称","上映年份","评分","评分⼈数"四项内容.

怎么做呢? ⾸先, 先看⼀下⻚⾯源代码. 数据是否是直接怼在源代码

上的?

很明显, 我们想要的数据全部都在⻚⾯源代码中体现了. 所以, 我们不

需要考虑js动态加载数据的情况了. 那么接下来就是编写爬⾍代码的

第⼀步了. 拿到⻚⾯源代码:

```python
#拿到页面源代码.requests
#通过re来提取想要的有效信息 re

import requests
import re
#反爬虫
url="https://movie.douban.com/top250"
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.86"
}

resp=requests.get(url,headers=headers)
text=resp.text #拿到网页文本
#解析数据
obj = re.compile(r' <li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)' 
                 r'</span>.*?<div class="bd">.*?<p class="">.*?<br>(?P<year>.*?)&nbsp;'  #r只是换行，好看
                 r'.*?<span class="rating_num" property="v:average">(?P<pingfen>.*?)</span>'
                 r'.*?<span>(?P<num>.*?)</span>', re.S)  # re.S能够识别换行，这四行东西为同一行内容,.*?跳到最近的文本
result = obj.finditer(text)
for it in result:
    print(it.group("name"))
    print(it.group("year").strip())  #.strip()分行顶置
    print(it.group("pingfen").strip())
    print(it.group("num").strip())
```

将数据存入csv格式的文件，方便数据分析

```python
#拿到页面源代码.requests
#通过re来提取想要的有效信息 re

import requests
import re
import csv
url="https://movie.douban.com/top250"
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.86"
}

resp=requests.get(url,headers=headers)
text=resp.text
#解析数据
obj = re.compile(r' <li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<div class="bd">.*?<p class="">.*?<br>(?P<year>.*?)&nbsp;'  #r只是换行，好看
                 r'.*?<span class="rating_num" property="v:average">(?P<pingfen>.*?)</span>'
                 r'.*?<span>(?P<num>.*?)</span>', re.S)  # re.S能够识别换行
result = obj.finditer(text)
f = open("data.csv",mode="w")
csvwriter = csv.writer(f)

for it in result:
  dic=it.groupdict()#以字典的形式存储
  dic['year'] = dic['year'].strip() #在year的后面去掉空格
  csvwriter.writerow(dic.values()) #写入字典的value
f.close() #关闭文件
resp.close() #关闭网页
```

使用while循环爬完整250条数据

```python
import requests
import re
import csv
nums=0
f = open("data.csv",mode="w") #在写入数据前先打开文件，不然重复打开会覆盖数据
while nums<=250:
    url=f"https://movie.douban.com/top250?start={nums}&filter="
    headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.86"
}
    resp=requests.get(url,headers=headers)
    text=resp.text
#解析数据
    obj = re.compile(r' <li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<div class="bd">.*?<p class="">.*?<br>(?P<year>.*?)&nbsp;'  #r只是换行，好看
                 r'.*?<span class="rating_num" property="v:average">(?P<pingfen>.*?)</span>'
                 r'.*?<span>(?P<num>.*?)</span>', re.S)  # re.S能够识别换行
    result = obj.finditer(text)
    csvwriter = csv.writer(f)
    for it in result:
           dic=it.groupdict()#以字典的形式存储
           dic['year'] = dic['year'].strip() #在year的后面去掉空格
           csvwriter.writerow(dic.values()) #写入字典的value
           resp.close() #用完一个网页，关闭网页
    nums+=25
    print(str(int(nums/2.5)-10)+"%")

f.close() #写完数据后，关闭文件 
```

#### bs4模块（熟悉html）

bs4模块安装

```python
pip install bs4
```

不论是find还是find_all 参数⼏乎是⼀致的.

语法:

find(标签, 属性=值)

意思是在⻚⾯中查找 xxx标签, 并且标签的xxx属性必须是xxx值

例:

find('div', age=18) 含义: 在⻚⾯中查找div标签, 并且属性age必须是18的这个标签.

find_all()的⽤法和find()⼏乎⼀致. find()查找1个. find_all()查找⻚⾯中所有的.

但是这种写法会有些问题. ⽐如html标签中的class属性

```python
 <div class="honor"> 

page.find("div", class="honor")
#注意, python中class是关键字. 会报错的. 怎么办呢? 可以在class后⾯加个下划线
page.find("div", class_="honor")
```

我们可以使⽤第⼆种写法来避免这类问题出现

```python
page.find("div", attrs={"class": "honor"})
```

完整代码

```python
import requests
from bs4 import BeautifulSoup
import csv

resp =
requests.get("http://www.xinfadi.com.cn/marke
tanalysis/0/list/1.shtml")

page = BeautifulSoup(resp.text)

 table = page.find("table", class_="hq_table")

 f = open("新发地.csv", mode="w",
encoding="utf-8")
 cv_writer = csv.writer(f)
 # 提取到所有tr
 tr_list = table.find_all("tr")[1:] # 注意,第⼀
⾏并不是我想要的数据. (第⼀⾏是表头)
 for tr in tr_list:
 td_list = tr.find_all("td")
 name = td_list[0].text # 获取⽂本内容
 low = td_list[1].text
 avg = td_list[2].text
 high = td_list[3].text
 gui = td_list[4].text
 dan = td_list[5].text
 day = td_list[6].text
 cv_writer.writerow([name, low, avg, high,
gui, dan, day])

 f.close()
 print("搞定")
```

#### 使用bs4爬图片,下载

也就是说, 想要下载该⽹站图⽚(⾼清⼤图), 需要三步,

第⼀步, 在主⻚⾯中拿到每⼀个图⽚的⼦⻚⾯链接

第⼆步, 在⼦⻚⾯中找到真正的图⽚下载地址第三步, 下载图⽚

⼀个⼀个⼲!

```python
# 1.拿到主页面的源代码。然后提取到子页面的链接地址，herf
# 2.通过href拿到子页面的内容。从子页面中找到图片的下载地址 img -> src
# 3.下载图片
import requests
from bs4 import BeautifulSoup
import time
url="https://www.umei.cc/bizhitupian/weimeibizhi/" #主页面
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.86"
}
resp = requests.get(url,headers=headers)
resp.encoding="utf-8" #处理乱码

#print(resp.text)
#把源代码交给bs
main_page = BeautifulSoup(resp.text,"html.parser")
alist = main_page.find("div",class_="Clbc_Game").find_all("a") #找到列表中包含所有a的div
#print(alist)
nums=0
for a in alist:  #循环提取a
    href = a.get('href') #直接通过get就可以拿到属性的值
    #拿到子页面的源代码
    child_page_resp = requests.get("https://www.umei.cc"+href) #当href文本包含的链接并不完整时要补上
    child_page_resp.encoding='utf-8'
    child_page_text = child_page_resp.text
    #从子页面中拿到图片的下载路径
    child_page = BeautifulSoup(child_page_text,"html.parser")
    div=child_page.find("div",class_="big-pic") #找到离img最近而独立的标签
    img = div.find("img") #标签内找到图片的值
    src = img.get("src")
    #下载图片
    img_resp = requests.get(src)
    img_resp.content #拿到的是文件的字节，将字节写入文件当中，就是图片了
    img_name = str(nums)+'.'+src.split(".")[-1]#拿到url最后一个.以后的内容,图片名称为1,2,3...
    with open("img/"+img_name,mode="wb") as f: #img/ 放入下一层img文件夹中
        f.write(img_resp.content)#将图片内容写入文件
    nums+=1
    time.sleep(1)
    print("done")

```

### Xpath入门(找数据最方便)

#### 第一节

```python
#xpath 是在XML文档中搜索内容的一门语言
#html是xml的一个子集
#可以通过父子节点查找
"""
<book>
 <id>1</id>
 <name>野花遍地⾹</name>
 <price>1.23</price>
 <author>
 <nick>周⼤强</nick>
 <nick>周芷若</nick>
 </author>
</book>
"""
#安装lxml模块
#pip install lxml
```

⽤法:

1. 将要解析的html内容构造出etree对象.

2. 使⽤etree对象的xpath()⽅法配合xpath表达式来完成对数据的提取

```python
 from lxml import etree

 html = """
 <book>
 <id>1</id>
 <name>野花遍地⾹</name>
 <price>1.23</price>
 <nick>臭⾖腐</nick>
 <author>
 <nick id="10086">周⼤强</nick>
 <nick id="10010">周芷若</nick>
 <nick class="joy">周杰伦</nick>
 <nick class="jolin">蔡依林</nick>
 <div>
 <nick>惹了</nick>
 </div>
 </author>

 <partner>
 <nick id="ppc">胖胖陈</nick>
 <nick id="ppbc">胖胖不陈</nick>
 </partner>
 </book>
 """

 et = etree.XML(html) #如果是html文本就用html
 # 根据节点进⾏搜索
 # result = et.xpath("/book")
 # result = et.xpath("/book/id") # /在开头表示⽂档最开始, /在中间表示⼉⼦
 # result = et.xpath("/book//nick") # //表示所有后代
 result = et.xpath("/book/*/nick") # *表示通配符，该层级什么都匹配

 print(result)
```

html

```html
1 <!DOCTYPE html>
2 <html lang="en">
3 <head>
4 <meta charset="UTF-8" />
5 <title>Title</title>
6 </head>
7 <body>
8 <ul>
9 <li><a href="http://www.baidu.com">百度
</a></li>
10 <li><a href="http://www.google.com">⾕
歌</a></li>
11 <li><a href="http://www.sogou.com">搜狗
</a></li>
12 </ul>
13 <ol>
14 <li><a href="feiji">⻜机</a></li>
15 <li><a href="dapao">⼤炮</a></li>
16 <li><a href="huoche">⽕⻋</a></li>
17 </ol>
18 <div class="job">李嘉诚</div>
19 <div class="common">胡辣汤</div>
20 </body>
21 </html>
```

指定某一个，属性，文本   在编辑网页源代码可以右键复制文本的xpath路径

```python
from lxml import etree

 tree = etree.parse("1.html")
 result = tree.xpath("/html/body/ul/li/a/@href")#@href取到href里面的文本
 print(result)

 result = tree.xpath("/html/body/ul/li")
 for li in result:
 print(li.xpath("./a/@href")) # 局部解析

 result = tree.xpath("//div[@class='job']/text()")
# [@class='xxx']属性选取 text()获取⽂本
 print(result)
```

### requests进阶

1. 模拟浏览器登录->处理cookie

2. 防盗链处理-> 抓取梨视频数据

3. 代理 -> 防⽌被封IP

#### 处理用户cookie信息登录（session）

在登录的时候监听网络，可以看到发送给请求的位置和参数（数据）

登录的请求很快会消失，可以勾选保留日志选项

```python
#登录 -> 得到cookie
#带着cookie 去请求到书架url -> 书架上的内容

#必须得把上面的两个操作连起来
#我们可以使用session进行请求 -> session你可以认为是一连串的请求，在这个过程中的cookie不会丢失
import requests

#会话
session = requests.session()
data={
"loginName":"15627526991",
"password":"z1o2m3b4i5e6"
}
#1.登录
url="https://passport.17k.com/ck/user/login"
session.post(url,data=data) #只是执行登录操作
#print(resp.cookies)#登录成功后获得cookies
#2.拿书架上的数据
#resp=session.get("https://user.17k.com/www/bookshelf/") #输入书架的链接，看不到书架上的信息，可以通过网络请求
#resp.encoding="utf-8"
#print(resp.text)
resp = requests.get("https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919",headers={ #将登录后的url的cookie放进来获取到书架的内容
    "Cookie":"GUID=5db58413-d870-4a46-8ca3-907e4c322ff0; c_referer_17k=https://www.baidu.com/link?url=N57D5186LErS-3UqAWmEQUWl77KhSVcMdAvndzMQcIW&wd=&eqid=af2d1e9d00002b280000000664b8e827; sajssdk_2015_cross_new_user=1; BAIDU_SSP_lcr=https://www.baidu.com/link?url=tr28aRFqY_3PHU-ztzeRH4E5pkK9c3pFHNXsavfUT-q&wd=&eqid=af2d1e9d00002b280000000664b8e827; Hm_lvt_9793f42b498361373512340937deb2a0=1689839662; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F09%252F29%252F07%252F100640729.jpg-88x88%253Fv%253D1689839715000%26id%3D100640729%26nickname%3D%25E4%25B9%25A6%25E5%258F%258B74188FGE7%26e%3D1705391802%26s%3D3f305c375e94a78b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22100640729%22%2C%22%24device_id%22%3A%22189724ae6ef10ce-0bd673f53800ca-7e565470-1580468-189724ae6f01b49%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%225db58413-d870-4a46-8ca3-907e4c322ff0%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1689841047"})


print(resp.json()["data"][0]["bookName"])#获取到书架的内容,返回值是josn(),["data"][0]["bookName"],在data字典中提取0位上key为bookName的值
length = len(resp.json()["data"]) #获取json中字典的元素个数
for i in range(0,int(length)) :   #将字典的元素个数转换成int形式
    print(resp.json()["data"][i]["bookName"]) #通过for循环输出书架上的所有书本名称
```

#### 防盗链Refer（抓取视频）

```python
#1.拿到contId
#2.拿到videoStatus返回的json.-> srcURL
#3.srcURL里面的内容进行修整
#4.下载视频
import requests
url = "https://www.pearvideo.com/video_1713901"
contId = url.split("_")[1] #切下1713901
print(contId)
videoStatus_url =f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.8770894467476524"
headers = {
 "User-Agent": "Mozilla/5.0 (Macintosh; Intel
Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like
Gecko) Chrome/87.0.4280.141 Safari/537.36",
 "Referer": url                        # 防盗链,意义:本次请求是由哪个url产⽣的
}
resp = requests.get(videoStatus_url,headers=headers)
dic = resp.json()
# print(dic)
 systemTime = dic['systemTime']
 videoUrl = dic["videoInfo"]['videos']['srcUrl'] #字典
 videoUrl = videoUrl.replace(systemTime, "cont-"+contId) # 拼接真正的视频url地址
 # print(videoUrl)

 # 下载视频
20 with open(f"{contId}.mp4", mode="wb") as f:
 f.write(requests.get(videoUrl).content)
```

#### 代理(proxies)

当我们反复抓取⼀个⽹站时, 由于请求过于频繁, 服务器很可能会将

你的IP进⾏封锁来反爬. 应对⽅案就是通过⽹络代理的形式进⾏伪

装。

 对于⽬标⽹站来说. 是通过代理服务器发送的请求.

也就可以避免你的IP被封锁了.

*可以通过爬取免费的代理网站的ip来进行多次攻击操作

```python
import requests

headers = {
 "User-Agent": "Mozilla/5.0 (Macintosh; Intel
Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like
Gecko) Chrome/87.0.4280.141 Safari/537.36",
 }
 proxies = {  
 "https": "https://27.148.248.203:80"  #代理
 }

 resp = requests.get("https://www.baidu.com",headers=headers, proxies=proxies)
 print(resp.text)
```

### 多线程

进程是资源单位，每个进程至少要有一个进程

线程是执行单位，进程包含多个线程。

python中实现多线程⾮常简单. 我们要借助Thread类来完成.

先看单线程效果

`if __name__ == '__main__':`是Python中的一个常用条件判断语句，用于判断当前脚本是否正在作为主程序运行，而不是被作为模块导入到其他脚本中。

在一个Python脚本中，当它被直接执行时，`__name__`的值为`'__main__'`。而当它被作为模块导入到其他脚本中时，`__name__`的值为该模块的名称。

通常，我们会将一些在脚本直接执行时需要执行的代码放在`if __name__ == '__main__':`条件判断的代码块中，这样可以确保这部分代码仅在脚本直接执行时才会运行，而在被导入时不会运行。

```python
def func():
 for i in range(1000):
 print("func", i)

if __name__ == '__main__':
 func()
 for i in range(1000):
 print("main", i)
```

执⾏过程: 程序启动 --> 加载func() --> 执⾏main --> 调⽤func() -->

func执⾏完毕, 继续执⾏main中的内容

整个过程是⼀条线跑下来的, 这就是单线程.

**多线程**:

```python
from threading import Thread #多线程要使用的模块
def func():
for i in range(1000):
print("func", i)

if __name__ == '__main__':
t = Thread(target=func) #创建线程
t.start() #启动线程
for i in range(1000):
print("main", i)

#func和主函数一起进行                                                                                                                                                                                 
```

### 多进程

启动进程和线程的方式是一样的

```python
from multiprocessing import Process #进程
from threading import Thread


# def func():
#     for i in range(1000):
#         print("子进程", i)
#
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()
#     for i in range(1000):
#         print("主进程", i)


def func(name):  # ??
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    t1 = Thread(target=func, args=("周杰伦",))  # 传递参数必须是元组
    t1.start()

    t2 = Thread(target=func, args=("王力宏",))
    t2.start()
```

### 线程池和进程池入门

线程池：一次性开辟一些线程。我们用户直接给线程池子提交任务。线程任务的调度交给线程池来完成。

```python
# 线程池: 一次性开辟一些线程. 我们用户直接给线程池子提交任务. 线程任务的调度交给线程池来完成
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor #导入模块


def fn(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t: #创建有50个线程的线程池
        for i in range(100): #100个任务，前五十个任务同时执行完之后再执行后50个进程
            t.submit(fn, name=f"线程{i}") #提交任务，提交每个线程的名字
    # 等待线程池中的任务全部执行完毕. 才继续执行(守护)
    print("123")

```

```
driver.quit() #主浏览器要在全部任务进行完成之后才关闭，否则读取到的字典信息会变成文本而无法拿出其中的链接
```

实战

```python
# 1. 如何提取单个页面的数据
# 2. 上线程池,多个页面同时抓取
import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f = open("data.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)


def download_one_page(url):
    # 拿到页面源代码
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    table = html.xpath("/html/body/div[2]/div[4]/div[1]/table")[0]
    # trs = table.xpath("./tr")[1:]
    trs = table.xpath("./tr[position()>1]")
    # 拿到每个tr
    for tr in trs:
        txt = tr.xpath("./td/text()")
        # 对数据做简单的处理: \\  / 去掉
        txt = (item.replace("\\", "").replace("/", "") for item in txt)
        # 把数据存放在文件中
        csvwriter.writerow(txt)
    print(url, "提取完毕!")


if __name__ == '__main__':
    # for i in range(1, 14870):  # 效率及其低下
    #     download_one_page(f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")

    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):  # 199 * 20 = 3980
            # 把下载任务提交给线程池
            t.submit(download_one_page, f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")

    print("全部下载完毕!")
```

### 协程

```python
# import time
#
#
# def func():
#     print("我爱黎明")
#     time.sleep(3)  # 让当前的线程处于阻塞状态. CPU是不为我工作的
#     print("我真的爱黎明")
#
#
# if __name__ == '__main__':
#     func()
#
# """
# # input() 程序也是处于阻塞状态
# # requests.get(bilibili) 在网络请求返回数据之前, 程序也是处于阻塞状态的
# # 一般情况下, 当程序处于 IO操作的时候. 线程都会处于阻塞状态
#
# # 协程: 当程序遇见了IO操作的时候. 可以选择性的切换到其他任务上.
# # 在微观上是一个任务一个任务的进行切换. 切换条件一般就是IO操作
# # 在宏观上,我们能看到的其实是多个任务一起在执行
# # 多任务异步操作
#
# # 上方所讲的一切. 都是在单线程的条件下
# """

```

示例

先上⼿来⼀下.

```python
1 async def func():

2 print("我是协程")

3

4

5 if __name__ == '__main__':

6 # print(func()) # 注意, 此时拿到的是⼀个协程对象,和⽣成器差不多.该函数默认是不会这样执⾏的

7

8 coroutine = func()

9 asyncio.run(coroutine) # ⽤asyncio的run来执⾏协程.

10 # lop = asyncio.get_event_loop()

11 # lop.run_until_complete(coroutine) # 这两句顶上⾯⼀句
```

效果不明显, 继续加码

```python
import time

 # await: 当该任务被挂起后,CPU会⾃动切换到其他任务中4 async def func1():
async def func1():
 print("func1, start")

 await asyncio.sleep(3)

 print("func1, end")


 async def func2():

 print("func2, start")

 await asyncio.sleep(4)

print("func2, end")



 async def func3():
     print("func3, start")

 await asyncio.sleep(2)

 print("func3, end")


 if __name__ == '__main__':

 start = time.time()

 tasks = [ # 协程任务列表
 func1(), # 创建协程任务
 func2(),
 func3()
 ]

 lop = asyncio.get_event_loop()30 # 我要执⾏这个协程任务列表中的所有任务

 lop.run_until_complete(asyncio.wait(tasks))# 我要执⾏这个协程任务列表中的所有任务

 print(time.time() - start)

妙不妙~~
```

上⾯的程序还可以写成这样

```python
 async def main():

 print("start")

 # # 添加协程任务

 # t1 = asyncio.create_task(func1())

 # t2 = asyncio.create_task(func2())

 # t3 = asyncio.create_task(func3())


 # ret1 = await t1

 # ret2 = await t2

 # ret3 = await t3

 tasks = [
 func1(),
 func2(),
 func3()
 ]
 # ⼀次性把所有任务都执⾏18 done, pedding = await asyncio.wait(tasks)

 

 print("end")



 if __name__ == '__main__':

 start = time.time()

 asyncio.run(main())

 print(time.time() - start)
```

模拟⼀下爬⾍怎么样~

```python
 async def download(url):
 print("开始抓取")
 await asyncio.sleep(3) # 我要开始下载了
 print("下载结束", url)
 return "⽼⼦是源码你信么"

 async def main():
 urls = [
 "http://www.baidu.com",
 "http://www.h.com",
 "http://luoyonghao.com"
 ]
 # ⽣成任务列表
 tasks = [download(url) for url in urls]
 done, pedding = await asyncio.wait(tasks)
 for d in done:
    print(d.result())
    
 if __name__ == '__main__':
    asyncio.run(main())
```

### aiohttp多任务异步协程

aiohttp是python的⼀个⾮常优秀的第三⽅异步http请求库. 我们可以⽤aiohttp来编写异步爬⾍(协程)

安装:

```python
 pip install aiohttp
```

实例代码:

```python
import aiohttp
import asyncio
import time
import requests
# 异步下载
async def aiodownload(url, session):
 name = url.split("/")[-1]

 # 发送请求, 这⾥和requests.get()⼏乎没区别, 除了代
理换成了proxy
 async with session.get(url) as resp:
 # 读取数据. 如果想要读取源代码. 直接
resp.text()即可. ⽐原来多了个()
 content = await resp.content.read()
 # 写⼊⽂件, 有兴趣可以参考aiofiles, 我这⾥根本
不需要.
 with open(name, mode="wb") as f:
 f.write(content)


 async def main():
 # 创建session对象 -> 相当于requsts对象
 async with aiohttp.ClientSession() as
session:
 # 添加下载任务
 tasks =
[asyncio.create_task(aiodownload(url, session))
for url in urls]
 # 等待所有任务下载完成
 await asyncio.wait(tasks)


 # 同步⽅式下载图⽚
 def download(url):
 name = url.split("/")[-1]
 resp = requests.get(url)
 content = resp.content
 with open(name, mode="wb") as f:
 f.write(content)

 # 我故意弄了⼀堆url做测试
 urls = [
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/26b7e178e987be6d914bf81af120890.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/191468637cab2f0206f7d1d9b175ac81.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
  "http://kr.shanghai￾jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/26b7e178e987be6d914bf8d1af120890.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/191468637cab2f0206f7d1d9b175ac81.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/26b7e178e987be6d914bf8d1af120890.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/191468637cab2f0206f7d1d9b175ac81.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghai￾jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghaijiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghaijiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghaijiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghaijiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 "http://kr.shanghaijiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
 ]

 if __name__ == '__main__':
 t2 = time.time()
 for url in urls:
 download(url)
 print(time.time() - t2)
 t1 = time.time()
 # 异步爬⾍
 asyncio.run(main())
```

### selenium概述(自动化脚本)

我们在抓取⼀些普通⽹⻚的时候requests基本上是可以满⾜的. 但是,如果遇到⼀些特殊的⽹站. 它的数据是经过加密的. 但是呢, 浏览器却能够正常显示出来. 那我们通过requests抓取到的内容可能就不是我们想要的结果了。

selenium, 它本身是⼀个⾃动化测试的⼯具. 可以启动⼀个全新的浏览器.并从浏览器中提取到你想要的内容. 随着各种⽹站的反爬机制的出现. selenium越来越受到各位爬sir的喜爱.

selenium最⼤的缺点其实就⼀个, 慢! 你想啊. 他要启动⼀个第三⽅的软件(浏览器), 并且还要等待浏览器把数据渲染完毕. 这个过程必然是

很耗时的. 所以它慢.

就像其他第三⽅库⼀样, selenium直接⽤pip就可以安装了

```
pip install selenium
```

但是呢, 它与其他库不同的地⽅是他要启动你电脑上的浏览器, 这就需要⼀个驱动程序来辅助.

[(85条消息) chromedriver驱动的下载和安装！亲测有效！_JOKERCDD的博客-CSDN博客](https://blog.csdn.net/weixin_46064809/article/details/131082448)

安装成功后测试代码

```python
from selenium import webdriver
# 打开百度
# 创建浏览器对象
driver = webdriver.Chrome()
url = 'https://www.baidu.com/'
driver.get(url)
driver.maximize_window()

print(driver.title) # 在控制台打印title
# 控制台输入任意内容结束
input()
driver.quit()
```

selenium不但可以打开浏览器. 还可以对浏览器各种操作. ⽐如, 点击, 查找. 都可以

![image-20230723205826612](图片/3.png)

实现点击百度页面上这个按一按的按钮

```python
from selenium import webdriver
# 打开百度
driver = webdriver.Chrome()
url = 'https://www.baidu.com/'
driver.get(url)
driver.maximize_window() #全屏


btn=driver.find_element_by_xpath('//*[@id="hotsearch-refresh-btn"]') #使用xpath定位按钮
btn.click() #模拟人点击按钮
input() 
driver.quit()
```

于是就看到按钮被点击了！

搜索python，实现搜索内容，首先定位到文本框，在里面输入内容再点击回车

![image-20230723210113250](图片/4.png)

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 导入Keys模块
import time
# 打开百度
driver = webdriver.Chrome()
url = 'https://www.baidu.com/'
driver.get(url)
driver.maximize_window()

# 控制台输入任意内容结束
driver.find_element_by_xpath('//*[@id="kw"]').send_keys("python",Keys.ENTER) #在文本框输入python，并回车
time.sleep(2) # 让浏览器反应⼀会⼉
#driver.find_element_by_xpath('//*[@id="su"]').click() #点击搜索按钮
input()
driver.quit()
```

爬取小说内容

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 导入Keys模块
import time
# 打开百度
driver = webdriver.Chrome()
url = 'https://www.ibiquges.net/0/54386/'
driver.get(url)
driver.maximize_window()

#点击小说第一章
driver.find_element_by_xpath('//*[@id="list"]/dl/dd[1]/a').click()
#获取小说中的文本元素
#标题
title = driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/div[2]/h1').text
#正文
text = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[3]').text  #读取文本，如果读取的元素多的话要用elements
#拼接
complete = title +'\n' + '\n' + text #标题和正文拼接
print(complete)
input()
driver.quit()
```

### selenium完整抓取小说实例

```python
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException #当搜索不到元素的时候可以停止循环
import time
# 主链接
driver = webdriver.Chrome()
url = 'https://www.ibiquges.net/'
driver.get(url)
driver.maximize_window()
name=input("请输入你要下载的小说名")
name.encode(encoding="utf-8")
#搜索小说
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/input').send_keys(name)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/button').click()
try:  #尝试能否找到小说
    a=driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/form/table/tbody/tr[2]/td[1]/a').get_attribute("href")
except NoSuchElementException:
    print("没有该小说")
    driver.quit()

if name != driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/form/table/tbody/tr[2]/td[1]/a').text :
    print("没有该小说")
    driver.quit()
print(a)
driver.get(a)#跳转到小说页面
#创建文件
f = open(f"{name}.txt",mode="w")
#点击小说第一章
driver.find_element_by_xpath('/html/body/div/div[7]/div/dl/dd[1]/a').click()
#获取小说中的文本元素
#标题
title = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/h1').text
#正文
text = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[3]').text
#拼接
complete = title[4:] +'\n' + '\n' + text #标题和正文拼接,[4:]切断正文卷和''使得小说在软件中可以自动分章
f.write(complete) #将一章写入文本
print(title[4:] + "下载完成")
time.sleep(2) #防止太快，无法访问
while True:
        try:
            # 寻找下一章按钮并跳转
            btn = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div[1]/a[4]')
            btn.click()
            time.sleep(2)
            # 获取小说中的文本元素
            # 标题
            title = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/h1').text
            # 正文
            text = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[3]').text
            # 拼接
            complete = '\n' + '\n' + title[4:] + '\n' + '\n' + text  # 标题和正文拼接
            f.write(complete)
            print(title[4:] + "下载完成")
        except NoSuchElementException:
            # 如果找不到文本元素，退出循环
            break

    # 如果无法找到所需元素，则执行停止循环的操作,表明小说已经下载完成
print("小说下载完成")
f.close()
print(complete)
driver.quit()
```

```
driver.quit() #主浏览器要在全部任务进行完成之后才关闭，否则读取到的字典信息会变成文本而无法拿出其中的链接
```



要在Selenium中进行页面跳转，可以使用`get()`方法或`navigate()`对象的方法来导航到新的URL。

get_attribute("href")来获取属性中d文本

1. 使用`try-except`块来捕获可能出现的`NoSuchElementException`异常。
2. 在`try`块中，首先寻找下一章按钮并点击。如果找到按钮，则说明还有下一章内容可以继续下载。
3. 获取当前章节的标题和正文内容。
4. 将标题和正文拼接成完整的章节内容，并将其写入文件中。
5. 输出下载完成的章节标题。
6. 如果找不到下一章按钮，会抛出`NoSuchElementException`异常，进入`except`块。
7. 在`except`块中，执行`break`语句退出循环，结束小说下载。

这样，循环会一直执行直到无法找到下一章按钮为止，确保每一章的内容都被下载。

使用elements获取多个元素的数组（可以写进度条）

```
len=len(driver.find_elements_by_xpath('/html/body/div/div[7]/div/dl/dd')) #获取章节数
```

在Python中，您可以使用`return`语句来直接跳到代码的最后。`return`语句用于终止函数的执行并将结果返回给调用它的地方

要将Selenium WebDriver设置为在后台运行浏览器，可以使用以下方法：

1. 使用Headless模式运行浏览器：一些浏览器（如Chrome和Firefox）提供了Headless模式，这意味着它们可以在没有可见界面的情况下运行。使用Headless模式运行浏览器可以减少资源消耗，并且在后台运行。

对于Chrome浏览器，可以使用ChromeOptions类来设置Headless模式。示例代码如下：

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # 设置Headless模式
driver = webdriver.Chrome(options=chrome_options)
```

#### 没有弹窗版抓取小说代码,有进度条版（selenium）

```python
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException #当搜索不到元素的时候可以停止循环
from selenium.webdriver.chrome.options import Options
import time

# 打开百度
chrome_options = Options()
chrome_options.add_argument("--headless")  # 设置Headless模式
driver = webdriver.Chrome(options=chrome_options)
url = 'https://www.ibiquges.net/'
driver.get(url)
name=input("请输入你要下载的小说名")
name.encode(encoding="utf-8")
#搜索小说
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/input').send_keys(name)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/button').click()
try:  #尝试能否找到小说
    a=driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/form/table/tbody/tr[2]/td[1]/a').get_attribute("href")
except NoSuchElementException:
    print("没有该小说")
    driver.quit()

if name != driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/form/table/tbody/tr[2]/td[1]/a').text :
    print("没有该小说")
    driver.quit()
print(a)
driver.get(a)#跳转到小说页面
len=len(driver.find_elements_by_xpath('/html/body/div/div[7]/div/dl/dd')) #获取章节数
#创建文件
f = open(f"{name}.txt",mode="w",encoding='utf-8')
#点击小说第一章
driver.find_element_by_xpath('/html/body/div/div[7]/div/dl/dd[1]/a').click()
#获取小说中的文本元素
#标题
title = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/h1').text
#正文
text = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[3]').text
#拼接
complete = title[4:] +'\n' + '\n' + text #标题和正文拼接,[4:]切断正文卷和''使得小说在软件中可以自动分章
f.write(complete) #将一章写入文本
print(title[4:] + "下载完成")
time.sleep(2) #防止太快，无法访问
nums=1
while True:
        try:
            # 寻找下一章按钮并跳转
            btn = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div[1]/a[4]')
            btn.click()
            time.sleep(2)
            # 获取小说中的文本元素
            # 标题
            title = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/h1').text
            # 正文
            text = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[3]').text
            # 拼接
            complete = '\n' + '\n' + title[4:] + '\n' + '\n' + text  # 标题和正文拼接
            f.write(complete)
            print(title[4:] + "下载完成")
            print("下载进度为"+str(int(nums/len*100))+"%") #进度条
            nums+=1
        except NoSuchElementException:
            # 如果找不到文本元素，退出循环
            print("下载进度为100%")
            break

    # 如果无法找到所需元素，则执行停止循环的操作,表明小说已经下载完成
print("小说下载完成")
f.close()
driver.quit()
```

### python打开excel

要使用openpyxl库读取Excel文件中的C列数据，你可以按照以下步骤进行操作：

```python
import openpyxl

# 打开Excel文件
workbook = openpyxl.load_workbook('path/to/file.xlsx')

# 选择指定的工作表
worksheet = workbook['Sheet1']

# 读取C列的数据
for cell in worksheet['C']:
    print(cell.value)
```

确保将`'path/to/file.xlsx'`替换为你实际的Excel文件路径。以上代码将打开指定的Excel文件，并选择名为'Sheet1'的工作表。然后它将遍历C列的所有单元格，并打印每个单元格的值。

注意，openpyxl库中的工作表（worksheet）是基于1索引的，所以'Sheet1'表示第一个工作表。如果你的文件中有其他工作表，请根据需要进行调整。
