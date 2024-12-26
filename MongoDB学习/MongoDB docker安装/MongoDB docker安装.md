# docker快速安装与配置mongoDB

### 拉取 MongoDB Docker 映像

```bash
docker pull mongodb/mongodb-community-server:latest
```

### 将映像作为 container 运行

```bash
docker run --restart=always --name mongodb -p 27017:27017 --privileged=true  -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=你的密码 -d mongodb/mongodb-community-server:latest 
```

此命令中的 `-p 27017:27017` 会将容器端口映射到主机端口。这样即可使用一个 `localhost:27017` 连接字符串连接到 MongoDB。

> --restart=always: 这个选项指定了容器的重启策略。always 意味着无论容器退出状态如何，Docker 都会尝试重启该容器。这通常用于确保服务的高可用性。
>
> --name mongodb: 给新创建的容器指定一个名称，这里将容器命名为 mongodb。为容器命名有助于后续对容器进行管理和操作。
>
> -p 27017:27017: 将主机的 27017 端口映射到容器的 27017 端口。MongoDB 默认监听 27017 端口，这样可以从主机访问容器内的 MongoDB 服务。
>
> --privileged=true: 给予容器扩展的权限。通常情况下，除非有特殊需求，否则不建议使用这个选项，因为它可能会带来安全风险。对于 MongoDB 容器来说，通常不需要这个选项。
>
> -e MONGO_INITDB_ROOT_USERNAME=root: 设置环境变量 MONGO_INITDB_ROOT_USERNAME 的值为 root。这是 MongoDB 初始化数据库时使用的管理员用户名。
>
> -e MONGO_INITDB_ROOT_PASSWORD=你的密码: 设置环境变量 MONGO_INITDB_ROOT_PASSWORD 的值为 你的密码。这是与上述管理员用户名关联的密码。请将 你的密码 替换为你希望设置的实际密码。

要安装特定版本的 MongoDB，请在 Docker run 命令中的 `:` 后面指定版本。Docker 会拉取并运行指定的版本。

### 检查 container 正在运行

```bash
docker container ls
```

(base) [root@VM-20-6-centos home]# docker container ls
CONTAINER ID   IMAGE                                                  COMMAND                  CREATED         STATUS         PORTS                                                       NAMES
e6a4c0674343   mongodb/mongodb-community-server:latest                "python3 /usr/local/…"   7 minutes ago   Up 7 minutes   0.0.0.0:27017->27017/tcp, :::27017->27017/tcp               mongodb

### 进入mongo容器

```bash
docker exec -it mongodb mongosh        #5.0之后的版本使用这个命令
docker exec -it mongodb mongo admin    #5.0之前的版本使用这个命令
```

### 添加账号

按照刚刚的配置，默认就能够使用root，你的密码，验证数据库是admin来进行登录，如果还想添加的话可以由如下方法:

#### 1. 创建管理员用户

```javascript
db.createUser({
  user: 'admin',
  pwd: 'm0ngoDb',
  roles: [{ role: 'root', db: 'admin' }]
});
```

- **`user: 'admin'`**: 指定用户名为 `admin`。
- **`pwd: '你的密码'`**: 指定用户的密码。你需要将 `'你的密码'` 替换为你实际想要设置的密码。
- **`roles: [{ role: 'root', db: 'admin' }]`**: 指定用户的角色。`root` 角色是MongoDB中最强大的角色，拥有所有数据库的所有权限。`db: 'admin'` 表示这个角色是在 `admin` 数据库中定义的。

#### 2. 认证管理员用户

```javascript
db.auth('admin', '密码');
```

- **`db.auth('admin', '密码')`**: 用于验证用户身份。`admin` 是用户名，`密码` 是你之前设置的密码。如果认证成功，返回值为 `1`；如果失败，返回值为 `0`。

#### 3. 创建具有读写权限的用户

```javascript
db.createUser({
  user: 'test',
  pwd: '你的密码',
  roles: [{ role: 'readWrite', db: 'elec_safe' }]
});
```

- **`user: 'test'`**: 指定用户名为 `test`。
- **`pwd: '你的密码'`**: 指定用户的密码。你需要将 `'你的密码'` 替换为你实际想要设置的密码。
- **`roles: [{ role: 'readWrite', db: 'elec_safe' }]`**: 指定用户的角色。`readWrite` 角色允许用户对指定数据库（这里是 `elec_safe`）进行读写操作。

#### 4. 认证读写用户

```javascript
db.auth('test', '密码');
```

- **`db.auth('test', '密码')`**: 用于验证用户身份。`test` 是用户名，`密码` 是你之前设置的密码。如果认证成功，返回值为 `1`；如果失败，返回值为 `0`。

参考:
[docker安装mongoDB详细步骤-CSDN博客](https://blog.csdn.net/qhl_904463348/article/details/120284218)

[使用 Docker 安装 MongoDB Community — MongoDB 手册 v8.0](https://www.mongodb.com/zh-cn/docs/manual/tutorial/install-mongodb-community-with-docker/)

[mongodb用户权限管理最全攻略：用户的创建、查看、删除与修改，mongodb入坑之旅_mongo db 添加和查看用户-CSDN博客](https://blog.csdn.net/zhanghongshuang/article/details/117461225)