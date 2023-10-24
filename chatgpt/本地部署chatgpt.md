Pandora简介
Pandora不愧是这三个月以来最为突出的项目之一，它完美解决了ChatGPT使用中经常遇到的种种问题，而且部署是相当简单，方便。项目地址：https://github.com/pengzhile/pandora

另外，今天（5.28）GPT再一次大范围风控，这似乎与sentry.io有一定的关联性，Pandora也可以避免封号的问题，当然你如果用全局模式问题不大。

Pandora能做什么
一、本地部署ChatGPT，Pandora绕过 Cloudflare，可以把ChatGPT部署在自己的电脑上，使用127.0.0.1即可使用官方的GPT（仅需登陆一次，即可正常使用14天左右）；

二、服务器部署ChatGPT，我们可以使用同样的方法，将Pandora程序安装在vps上，甚至可以使用自己的域名，无需设置网络即可使用，也不必担心IP问题；

三、我们可以使用Pandora，用多种方式使用GPT，例如命令行模式，web模式，其中web页面使用方法与官网一致，还能保存记录，非常完美。

Pandora部署方法
一、部署在本地电脑上
无论是windows、macOS或者linux系统，都可以用三个步骤把Pandora部署到本地：

1、安装docker并启动，到https://www.docker.com/get-started 下载docker；安装后启动；

2、命令行执行：

```
docker pull pengzhile/pandora 
```

```
docker run  -e PANDORA_CLOUD=cloud -e PANDORA_SERVER=0.0.0.0:8899 -p 8899:8899 -d pengzhile/pandora
```

3、本地浏览器访问 127.0.0.1:8899 即可访问，直接登陆或者使用Access Token，然后就能够正常的使用GPT了。


4、作者给出的获得Access Token的地址：http://chat.openai.com/api/auth/session

缺点：登陆或者获取Token一样需要设置网络；

二、部署在vps上
强调：在vps部署Pandora请使用国外主机，这样无论是电脑还是手机都可以使用GPT了，推荐：https://bbs.csdn.net/topics/610404063

1、安装docker环境（ubuntu系统）

```
apt update && apt install docker.io -y
```

2、拉取镜像

```
docker pull pengzhile/pandora
```

3、启动容器

（1）命令行模式：

```
docker run -it --rm pengzhile/pandora
```

（2）web模式

```
docker run  -e PANDORA_CLOUD=cloud -e PANDORA_SERVER=0.0.0.0:8899 -p 8899:8899 -d pengzhile/pandora
```

用这种方法搭建，流畅使用GPT，任何终端的浏览器均可使用，安全、方便。

三、绑定域名的方法
1、如果你使用的是nginx，编辑配置文件

vim /etc/nginx/nginx.conf

将其内容替换为：

        listen 80;    
        server_name fboth.pp.ua;        
    events {} 
    
    http 
    
    {    server { 
    
    
    location / {            
    
    proxy_pass http://127.0.0.1:8899;        
    
    }    
    
    } 
    
    }

如果你想用caddy，编辑 /etc/caddy/Caddyfile

xx.com  #这里是你解析的域名

encode gzip 

reverse_proxy 127.0.0.1:8899

总结
Pandora不愧是一个优秀的项目，除了docker安装，还可以pip，解决了GPT使用上的诸多问题，而且速度比官网还快，值得点赞！ 