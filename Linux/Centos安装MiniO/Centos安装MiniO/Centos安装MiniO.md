### CentOS 快速部署 MinIO 教程

#### 一、安装部署

1. **安装基本工具**

    ```bash
    [root@localhost ~]# yum install -y wget vim
    ```

2. **创建目录**

    ```bash
    [root@localhost ~]# mkdir /opt/minio
    [root@localhost ~]# mkdir /opt/minio/data
    ```

3. **进入目录**

    ```bash
    [root@localhost ~]# cd /opt/minio
    ```

4. **下载 MinIO 二进制文件**

    ```bash
    [root@localhost ~]# wget https://dl.min.io/server/minio/release/linux-amd64/minio
    ```

5. **赋予执行权限**

    ```bash
    [root@localhost ~]# chmod +x minio
    ```

6. **启动 MinIO 服务器**

    - **直接启动**

        ```bash
        [root@localhost ~]# /opt/minio/minio server /opt/minio/data/
        ```

    - **后台启动并将输出重定向到日志文件**

        ​    创建文件夹赋予权限:

        ```
        mkdir -p /var/log/minio
        chown -R root:root /var/log/minio
        chmod 755 /var/log/minio
        ```

        ```bash
        [root@localhost ~]# nohup /opt/minio/minio server /opt/minio/data/ > /var/log/minio/nohup.out 2>&1 &
        ```

    - **自定义端口启动**

        ```bash
        [root@localhost ~]# nohup /opt/minio/minio server --address :9001 /opt/minio/data/ > /var/log/minio/nohup.out 2>&1 &
        ```

8. **启动成功**

    您应该能看到类似下面的输出：

    ```bash
    [root@iZ93t2q6je9ztdZ ~]# /opt/minio/minio server /opt/minio/data/
    API: http://XXX.XXX.XXX.XXX:9000  http://127.0.0.1:9000     
    RootUser: 账号
    RootPass: 密码 
    
    Console: http://XXX.XXX.XXX.XXX:39902 http://127.0.0.1:39902   
    RootUser: 账号 
    RootPass: 密码 
    ```

#### 二、MinIO 控制台登录

1. **在浏览器中输入控制台地址**

    输入 MinIO 控制台的 URL 地址：

    ```bash
    http://外网IP:39902/
    ```

    或者如果是在本地测试：

    ```bash
    http://127.0.0.1:39902/
    ```

2. **登录 MinIO 控制台**

    出现登录界面后，输入前面显示的账号和密码进行登录。

#### 三、挂起 MinIO 服务器并在 CentOS 中后台运行

1. **创建日志目录**

    确保 `/var/log/minio` 目录存在，并且具有正确的权限：

    ```bash
    mkdir -p /var/log/minio
    chown -R root:root /var/log/minio
    chmod 755 /var/log/minio
    ```

2. **后台启动 MinIO 并将输出重定向到日志文件**

    ```bash
    nohup /opt/minio/minio server /opt/minio/data/ > /var/log/minio/nohup.out 2>&1 &
    ```

3. **验证后台作业**

    使用以下命令确认 MinIO 服务器已经在后台运行： 或者使用 netstat -tuln | grep :端口

    ```bash
    jobs -l
    ```

4. **查看日志文件**

    使用以下命令查看 MinIO 日志文件：

    ```bash
    tail -f /var/log/minio/nohup.out
    ```

5. **停止 MinIO 服务器**

    如果需要停止 MinIO 服务器，可以使用以下命令：

    ```bash
    kill <job_number>
    ```

    其中 `<job_number>` 是 `jobs -l` 命令显示的作业编号。

参考：[记一次 Centos7 安装 Minio （文件服务器）_minio cpuv1-CSDN博客](https://blog.csdn.net/llwy1428/article/details/99618252)