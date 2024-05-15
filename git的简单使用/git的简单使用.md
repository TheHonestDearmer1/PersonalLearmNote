# git命令的简单使用

### 上传和更新仓库文件

在安装好git的基础上，首先打开浏览器登录自己的github账号，新建一个文件夹，在文件夹里面右键git bash here

#### 使用git命令克隆仓库到本地：

```bash
git clone 仓库地址
```

然后会将项目克隆下来，并且在项目中生成.git隐藏文件，版本库的信息都包含在里面

如果出现SSL报错，只需要执行下面命令就可以解决：

```bash
git config --global http.sslVerify false
```

#### 修改并提交到本地项目：

使用ls命令可以查看当前的目录，先cd进要修改的文件目录，将文件替换后，执行：

```bash
git add 文件
```

cd ../ 退回到上一层文件夹，如果是新增文件夹也是：

```bash
git add 文件夹
```

直接添加所有文件：

```
git add .
```

然后执行命令提交修改：

```bash
git commit
```

如果没有账号，名称信息的按照要求填写就好

此时进入到vim编辑界面，写入此次更新的内容，esc退出编辑模式，此时键入:wq则可以退出commit

#### 更新到远程项目：

当全部内容更新完毕后，输入命令传到远程项目仓库：

```bash
git push
```

cd进项目可以使用git status命令查看项目状态

git强制覆盖本地代码（与git远程仓库保持⼀致）
git强制覆盖：

```
git fetch --all
git reset --hard origin/master
git pull
```

git强制覆盖本地命令（单条执⾏）：

```
 git fetch --all &&  git reset --hard origin/master && git pull
```

第⼀个是：拉取所有更新，不同步；
第⼆个是：本地代码同步线上最新版本(会覆盖本地所有与远程仓库上同名的⽂件)；
第三个是：再更新⼀次（其实也可以不⽤，第⼆步命令做过了其实）
备注： 命令连接符 && 的意思是 前⼀条命令执⾏成功才执⾏后⼀条命令。





