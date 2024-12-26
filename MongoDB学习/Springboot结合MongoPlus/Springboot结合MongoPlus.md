## Springboot结合MongoPlus操作MongoDB

这是官方仓库链接,可以自己看看最新版本是多少：

[Maven Repository: com.gitee.anwena » mongo-plus-boot-starter](https://mvnrepository.com/artifact/com.gitee.anwena/mongo-plus-boot-starter)

这是官方文档：

[快速上手 | MongoPlus](https://www.mongoplus.cn/docs/started.html)

### 添加依赖:

```xml
        <dependency>
            <groupId>com.gitee.anwena</groupId>
            <artifactId>mongo-plus-boot-starter</artifactId>
            <version>2.1.4</version>
        </dependency>
```

### 配置数据库信息：

在 `application.yml` 配置文件中添加 MongoPlus 相关配置：

yaml

```yml
# DataSource Config
mongo-plus:
  data:
    mongodb:
      host: 127.0.0.1   #ip
      port: 27017   #端口
      database: test    #数据库名
      username: test    #用户名，没有可不填（若账号中出现@,!等等符号，不需要再进行转码！！！）
      password: test    #密码，同上（若密码中出现@,!等等符号，不需要再进行转码！！！）
      authenticationDatabase: admin     #验证数据库
      connectTimeoutMS: 50000   #在超时之前等待连接打开的最长时间（以毫秒为单位）
```

