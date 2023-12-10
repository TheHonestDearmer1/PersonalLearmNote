 

### 1、简要说明

近日，在使用`flask`框架获取前端的请求时获取参数时，遇到了几个问题；之前的项目也有使用这部分，当时程序没有问题就没再深究，直到遇到了问题。果然，遇到问题才会成长！`^_^`

因此，对`GET`和`POST`两种请求方式的参数获取方式进行梳理。

`request`对象是从客户端向服务器发出请求，包括用户提交的信息以及客户端的一些信息。客户端可通过HTML表单或在网页地址后面提供参数的方法提交数据，然后通过`request`对象的相关方法来获取这些数据。

`request`请求总体分为两类：

1.  **`get`请求**  
    `GET`把参数包含在`URL`中，访问时会在地址栏直接显示参数不安全，且参数大小比较小
    
2.  **`post`请求**  
    参数通过`request body`传递
    

### 2、常见的方式

在最初使用时，上网一搜，得到的结果大致如下：

**flask获取参数方式：**

```python
	request.form.get("key", type=str, default=None) # 获取表单数据
	request.args.get("key") # 获取get请求参数
	request.values.get("key") # 获取所有参数
```

> 上述是三种方式，可以满足基本的使用，但是并不是万能的！

### 3、`GET`请求方式获取参数

当采用`GET`请求方式时，参数直接显示在请求连接中，可以使用两种获取参数的方式：

*   `request.args.get('key')`
*   `request.values.get('key')`

在`route`装饰器语句中，通过`methods`指定请求方式，如下：

```python
@app.route("/", methods=["GET"])
```

**获取参数**

```python
if request.method == "GET":
    comment = request.args.get("content")
    comment = request.values.get("content")
```

### 4、`POST`请求方式获取参数

客户端在发送`post`请求时，数据可以使用不同的`Content-Type` 来发送。

比如：

*   以 `application/json` 的方式 ，请求`body`体的内容就是`{"a": "b", "c": "d"}`
*   以 `application/x-www-form-urlencoded` 的方式，则`body`体的内容就是 `a=b&c=d`

在`Postman`软件中，可以方便的查看参数是以什么形式发送的，对应的`Content-Type`是什么。

*   `Body`中选择`“raw”`，则对应的Headers中的`“Content-Type”`是`“application/json”`，参数形式是`{"content":"很好"}`
    
*   `Body`中选择`“x-www-form-urlencoded”`，则对应的Headers中的`“Content-Type”`是`“application/x-www-form-urlencoded”`，参数形式是Key-Value形式。
    
*   `Body`中选择`“form-data”`， 则对应的Headers中的`“Content-Type”`是`“multipart/form-data”`，参数形式是Key-Value。
    
    具体位置如下图：  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200724154926816.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpbmc2MjA=,size_16,color_FFFFFF,t_70)
    

#### `POST`请求不同`Content-Type`的处理方式

1.  **`Content-Type`为 `application/json`，获取`json`参数**
    
    ```python
    request.get_json()['content']
    # 或者
    request.json.get('centent')
    ```
    
    获取的是序列化后的参数，一般情况下满足使用，不需要`json.loads()`来序列化。  
    打印出结果就是`json`串，如`{'name':'lucy', 'age':22}`
    
2.  **`Content-Type`为 `application/json`，获取json原始参数**
    
    ```python
    request.get_data()
    ```
    
    `request.get_data()`获取的原始参数，接受的是type是`'bytes`’的对象，如：`b{'name':'lucy', 'age':22}`
    
3.  **`Content-Type`为`application/x-www-form-urlencoded`**
    
    ```py
    request.values.get('key')
    ```
    
4.  **`Content-Type`为`multipart/form-data` ，获取表单参数**
    
    可以使用`request.form.get('content')` 或者 `request.form['content']`来获取参数
    
    ```py
    request.form.get('key')
    # 或者
    request.form['key']
    ```
    

#### 代码示例

```python
if request.method == "POST":
     if request.content_type.startswith('application/json'):            
         # comment = request.get_json()["content"]
         comment = request.json.get('content')
     elif request.content_type.startswith('multipart/form-data'):
         comment = request.form.get('content')
     else:
         comment = request.values.get("content")
```

### 5、完整示例

```py
@app.route("/", methods=["GET", "POST"])
def process():
    if request.method == "GET":
        comment = request.args.get("content")
        # comment = request.values.get("content")
    if request.method == "POST":
        if request.content_type.startswith('application/json'):            
            # comment = request.get_json()["content"]
            comment = request.json.get('content')
        elif request.content_type.startswith('multipart/form-data'):
            comment = request.form.get('content')
        else:
            comment = request.values.get("content")
    logger.debug('%s'%comment)
```

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Python入门技能树](https://edu.csdn.net/skill/python/python-3-139?utm_source=csdn_ai_skill_tree_blog)[Web应用开发](https://edu.csdn.net/skill/python/python-3-139?utm_source=csdn_ai_skill_tree_blog) [Flask](https://edu.csdn.net/skill/python/python-3-139?utm_source=csdn_ai_skill_tree_blog)372251 人正在系统学习中

本文转自 <https://blog.csdn.net/ling620/article/details/107562294>，如有侵权，请联系删除。