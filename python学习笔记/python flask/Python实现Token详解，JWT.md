
## Python实现Token详解

### 一、引言

>  
 Token是目前广泛使用的一种保持会话状态的技术，与以前的cookie、session共同存在于如今各大网站架构中。本篇中，我们着重来讲解在python中，怎样实现token。 


首先，我们来看一下`session`的主要缺点：

当我们在使用`session`保持会话状态，同时验证用户的合法性时，有两个问题存在:
- 性能问题
因为`session`的实现过程，需要用户在每次请求中携带`sessionid`，服务端收到后，对比数据库中的`sessionid`是否一致。而我们知道，数据库的操作往往是服务端最常见的性能瓶颈。
- 扩展性问题
当用户量变多后，后端往往采用多个服务器，多个节点。但多个节点都要访问`session`，这样就要去数据库服务能被多个节点访问，不方便分库以提高性能。

而`Token`可以很好的解决这些问题

### 二、原理

`session`的机制是把数据信息放在服务端，正常情况下，服务端数据是无法被篡改的，从而保证验证的可靠性。

而`Token`是将拼接好的数据信息传给客户端，客户每次请求携带过来给服务端。服务端直接根据携带的数据信息进行校验。

那为什么，`token`将信息存放在客户端，而不会有被篡改的风险呢？服务端又是怎么验证`token`数据的完整性的呢？？

目前，`JWT(Json Web Token)`是目前运用最广泛的认证解决方案，由于非常靠谱，已经被写入行业标准`RFC 7519`

### 三、python实现JWT-token

在Python中，有一个包`pyjwt`，专门用来生成token，接下来，我们使用这个包，快速的生成我们想要的token

安装：

```
pip install pyjwt

```

Demo：生成Token

```python
import jwt
import time

# 生成一个字典，包含我们的具体信息
d = {<!-- -->
    # 公共声明
    'exp':time.time()+3000, # (Expiration Time) 此token的过期时间的时间戳
    'iat':time.time(), # (Issued At) 指明此创建时间的时间戳
    'iss':'Issuer', # (Issuer) 指明此token的签发者
    
    # 私有声明
    'data':{<!--需要加密的内容 -->
        'username':'xjj',
        'timestamp':time.time()
    }
}

jwt_encode = jwt.encode(d,'123456',algorithm='HS256')

print(jwt_encode)
# 打印token串
#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjI2MDQ3MTguNjczNjgzNiwiaWF0IjoxNjIyNjAxNzE4LjY3MzY4MzYsImlzcyI6Iklzc3VlciIsImRhdGEiOnsidXNlcm5hbWUiOiJ4amoiLCJ0aW1lc3RhbXAiOjE2MjI2MDE3MTguNjczNjgzNn19.ASgB9-1U9ADhv6AmBH7p8leEtWMTMhaDQJSaZ9z9kZg

```

`pyjwt`提供的`jwt.encode(payload,key,algorithm)`方法可以让我们快速的生成`token`；需要提供三个参数

|参数|说明
|**payload**|公有声明和私有声明组成的字典，根据需要进行添加
|**key**|自定义的加密key。重要，不能外泄
|**algorithm**|声明需要使用的加密算法，如’HS256’

生成完毕后，还可以进行`jwt.decode()`解密

```python
import jwt
jwt_encode = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjI2MDQ3MTguNjczNjgzNiwiaWF0IjoxNjIyNjAxNzE4LjY3MzY4MzYsImlzcyI6Iklzc3VlciIsImRhdGEiOnsidXNlcm5hbWUiOiJ4amoiLCJ0aW1lc3RhbXAiOjE2MjI2MDE3MTguNjczNjgzNn19.ASgB9-1U9ADhv6AmBH7p8leEtWMTMhaDQJSaZ9z9kZg'

jwt_decode = jwt.decode(jwt_encode, '123456', issuer='Issuer',  algorithms=['HS256'])

print(jwt_decode)
# 打印解密后信息
# {'exp': 1622604718.6736836, 'iat': 1622601718.6736836, 'iss': 'Issuer', 'data': {'username': 'xjj', 'timestamp': 1622601718.6736836}}

```

使用现成的`pyjwt`，我们就可以像这样快速的生成token。

现在我们知道了api的调用，那JWT具体加密的实现步骤是怎样的呢？作为一个加密认证算法，`JWT`是怎样得到所有人的认可，成为一个行业标准的呢？

接下来我们来具体实现他的加密步骤。

### 四、JWT - Json-Web-Token

#### 4.1具体组成

首先，JWT由三部分组成：`header`、`payload`、`signature`

<img src="https://img-blog.csdnimg.cn/20210602122127905.png#pic_center" alt="在这里插入图片描述">
- header
格式为字典

```
{<!-- -->'alg':'HS256', 'typ':'JWT'}
# alg代表要使用的 算法
# typ表明该token的类别 - 此处必须为 大写的 JWT

```

该部分数据需要转成json串并用base64进行加密
- payload
格式为字典，此部分分为共有声明和私有声明

**共有声明**：JWT提供用于描述常见的问题，如:

```
{<!-- -->'exp':xxx, # Expiration Time 此token的过期时间的时间戳
 'iss':xxx，# (Issuer) Claim 指明此token的签发者
 'iat':xxx, # (Issued At) Claim 指明此创建时间的时间戳
 'aud':xxx, # (Audience) Claim	指明此token签发面向群体
}

```

此部分均为可选项，用户可以根据自己需求，按需添加key。

**私有声明**：自定义添加key、value

```
{<!-- -->'username':'xjj'}

```

公有声明和私有声明均在同一个字典中；转成json串并用base64加密
- signature签名
签名规则如下：

根据header中的alg确定具体算法，以下用HS256为例

```
HS256(自定义的key,base64后的header+'.'+base64后的payload)

```

#### 4.2具体实现

`jwt`组成格式：`base64(header)+'.'+base64(payload)+'.'base64(sign)`

首先，明确一下需求，我们需要用到三个组成部分，其中header、payload都需要base64加密，sign本身需要经过HS256哈希后，再进行base64加密。

代码如下：

```python
import time
import hashlib
import json
import base64


def base64_util(d):
    # 封装通用base64加密
    s = d.encode()
    b_s = base64.b64encode(s)
    return b_s


def hmac_util(key, s):
    # 封装HS256计算
    m = hashlib.sha256(key)
    m.update(s)
    return m.hexdigest()


class JwtDemo:
    def __init__(self, header, payload, key):
        self.header = header
        self.payload = payload
        self.key = key

    def sign(self):
        bs_header = base64_util(self.header)
        bs_payload = base64_util(self.payload)
        s_group = bs_header + b'.' + bs_payload
        return hmac_util(self.key, s_group)

    def jwt_res(self):
        jwt_res = base64_util(self.header) + b'.' + base64_util(self.payload) + b'.' + base64_util(self.sign())
        return jwt_res



if __name__ == '__main__':
    h = json.dumps({<!-- -->'alg': 'HS256', 'typ': 'JWT'})
    p = json.dumps({<!-- -->'exp': time.time() + 3600,  # Expiration Time 此token的过期时间的时间戳
                    'iss': 'Issuer',  # (Issuer) Claim 指明此token的签发者
                    'iat': time.time(),  # (Issued At) Claim 指明此创建时间的时间戳
                    'data': {<!-- -->
                        'username': 'xjj',
                    }
                    })
    k = b'123456'
    
    j = JwtDemo(header=h, payload=p, key=k)
    print(j.jwt_res())
    #b'eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJleHAiOiAxNjIyNjEwMTM4LjU3MTk5MDUsICJpc3MiOiAiSXNzdWVyIiwgImlhdCI6IDE2MjI2MDY1MzguNTcxOTkwNSwgImRhdGEiOiB7InVzZXJuYW1lIjogInhqaiJ9fQ==.NmFjMzMxNmZlNzdhMDBmZTQxMWFjODQxOGVkNDViNzBlZWVmZGJjNDUyMmY3MjkyN2EwMTdlNTEwNTZjYTU4ZQ=='

```

这样，我们按照规范，经过封装一系列方法，自己生成了一个token~

#### 4.3校验JWT

生成token后，我们可以在进行验证。

进入网站后，往下拉，在Debugger区域，可以看到如下图所示：

<img src="https://img-blog.csdnimg.cn/20210602122225220.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyODMxNDY2,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">
- 第一步，将我们生成的token串，填入①位置。- 第二步，将我们使用的私有秘钥key，填入②位置。此处打钩为base64转换- 第三步，在右上方显示的，就是我们的header和公有信息，私有信息了- 在左下方，会提示token串是否合规
五、结语


