# 安装

[安装 — Flask中文文档(2.3.x) (dormousehole.readthedocs.io)](https://dormousehole.readthedocs.io/en/latest/installation.html#flask)

## Python 版本

我们推荐使用最新版本的 Python 。 Flask 支持 Python 3.8 以上版本。

## 依赖

当安装 Flask 时，以下配套软件会被自动安装。

- [Werkzeug](https://palletsprojects.com/p/werkzeug/) 用于实现 WSGI ，应用和服务之间的标准 Python 接口。
- [Jinja](https://palletsprojects.com/p/jinja/) 用于渲染页面的模板语言。
- [MarkupSafe](https://palletsprojects.com/p/markupsafe/) 与 Jinja 共用，在渲染页面时用于避免不可信的输入，防止注 入攻击。
- [ItsDangerous](https://palletsprojects.com/p/itsdangerous/) 保证数据完整性的安全标志数据，用于保护 Flask 的 session cookie.
- [Click](https://palletsprojects.com/p/click/) 是一个命令行应用的框架。用于提供 `flask` 命令，并允许添加 自定义管理命令。
- [Blinker](https://blinker.readthedocs.io/) 提供对于 [信号](https://dormousehole.readthedocs.io/en/latest/signals.html) 的支持。

### 可选依赖

以下配套软件不会被自动安装。如果安装了，那么 Flask 会检测到这些软件。

- [python-dotenv](https://github.com/theskumar/python-dotenv#readme) 当运行 `flask` 命令时为 [通过 dotenv 设置环境变量](https://dormousehole.readthedocs.io/en/latest/cli.html#dotenv) 提供支持。
- [Watchdog](https://pythonhosted.org/watchdog/) 为开发服务器提供快速高效的重载。

### greenlet

您可以选择使用 gevent 或者 eventlet 来服务您的应用。在这种情况下， greenlet>=1.0 是必须的。当使用 PyPy 时， PyPy>=7.3.7 是必须的。

上述版本是指支持的最小版本，应当尽量使用最新的版本。

## 虚拟环境

建议在开发环境和生产环境下都使用虚拟环境来管理项目的依赖。

为什么要使用虚拟环境？随着你的 Python 项目越来越多，你会发现不同的项目 会需要不同的版本的 Python 库。同一个 Python 库的不同版本可能不兼容。

虚拟环境可以为每一个项目安装独立的 Python 库，这样就可以隔离不同项目之 间的 Python 库，也可以隔离项目与操作系统之间的 Python 库。

Python 内置了用于创建虚拟环境的 [`venv`](https://docs.python.org/3/library/venv.html#module-venv) 模块。



### 创建一个虚拟环境

创建一个项目文件夹，然后创建一个虚拟环境。创建完成后项目文件夹中会有一 个 `.venv` 文件夹：

Windows

```
> mkdir myproject
> cd myproject
> py -3 -m venv .venv
```



### 激活虚拟环境

在开始工作前，先要激活相应的虚拟环境：

1. 在PowerShell中首次运行以下命令：`Set-ExecutionPolicy RemoteSigned`。这将允许运行本地脚本和远程数字签名过的脚本。

Windows

```
> .venv\Scripts\activate
```

激活后，你的终端提示符会显示虚拟环境的名称。



## 安装 Flask

在已激活的虚拟环境中可以使用如下命令安装 Flask：

```
$ pip install Flask
```

[解决pip下载速度过慢的问题_pip下载太慢_一个默默无闻的小程序员的博客-CSDN博客](https://blog.csdn.net/m0_52529907/article/details/127196390)

# 快速上手

等久了吧？本文会给您好好介绍如何上手 Flask 。 这里假定您已经安装好了 Flask ，否则请先阅读《 [安装](https://dormousehole.readthedocs.io/en/latest/installation.html) 》。

## 一个最小的应用

一个最小的 Flask 应用如下：

```py
from flask import Flask //导入了 flask类

app = Flask(__name__)      //创建一个该类的实例

@app.route("/")   //告诉 Flask 触发函 数的 URL
def hello_world():   //函数返回需要在用户浏览器中显示的信息
    return "<p>Hello, World!</p>"
```

那么，这些代码是什么意思呢？

1. 首先我们导入了 [`Flask`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask) 类。该类的实例将会成为我们的 WSGI 应用。
2. 接着我们创建一个该类的实例。第一个参数是应用模块或者包的名称。 `__name__` 是一个适用于大多数情况的快捷方式。有了这个参数， Flask 才能知道在哪里可以找到模板和静态文件等东西。
3. 然后我们使用 [`route()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask.route) 装饰器来告诉 Flask 触发函 数的 URL 。
4. 函数返回需要在用户浏览器中显示的信息。默认的内容类型是 HTML ，因此 字符串中的 HTML 会被浏览器渲染。

把它保存为 `hello.py` 或其他类似名称。请不要使用 `flask.py` 作为应用名称，这会与 Flask 本身发生冲突。

可以使用 `flask` 命令或者 `python -m flask` 来运行这个应 用。你需要使用 `--app` 选项告诉 Flask 哪里可以找到应用。

```
$ flask --app hello run
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

应用发现行为

作为一个捷径，如果文件名为 `app.py` 或者 `wsgi.py` ，那么您不 需要使用 `--app` 。详见 [命令行接口](https://dormousehole.readthedocs.io/en/latest/cli.html) 。

这样就启动了一个非常简单的内建的服务器。这个服务器用于测试应该是足够 了，但是用于生产可能是不够的。关于部署的有关内容参见 [生产部署](https://dormousehole.readthedocs.io/en/latest/deploying/index.html) 。

现在在浏览器中打开 http://127.0.0.1:5000/ ，应该可以看到 Hello World! 字样。

如果其他程序已经占用了 5000 端口，那么在尝试启动服务器时会看到 `OSError: [Errno 98]` 或者 `OSError: [WinError 10013]` ， 如何解决这个问题请参阅 [地址已被占用](https://dormousehole.readthedocs.io/en/latest/server.html#address-already-in-use) 。

外部可见的服务器

运行服务器后，会发现只有您自己的电脑可以使用服务，而网络中的其他电 脑却不行。缺省设置就是这样的，因为在调试模式下该应用的用户可以执行 您电脑中的任意 Python 代码。

如果您关闭了调试器或信任您网络中的用户，那么可以让服务器被公开访问。 只要在命令行上简单的加上 `--host=0.0.0.0` 即可:

```
$ flask run --host=0.0.0.0
```

这行代码告诉您的操作系统监听所有公开的 IP 。



**WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.**

这个警告是在使用开发服务器进行部署时显示的。它是提醒您不要在生产环境中使用开发服务器，而应该使用生产级别的 WSGI 服务器。

开发服务器通常是用于开发和测试目的，它可能不具备生产服务器所需的稳定性、安全性和性能。在生产环境中，建议使用专门的 WSGI 服务器，如 Gunicorn、uWSGI 或者 Nginx + uWSGI。这些服务器可以更好地处理并发请求、提供更好的性能和安全性。

如果您正在开发阶段，并且只是在本地测试或调试您的应用程序，那么开发服务器是可以接受的。但是，一旦准备将应用程序部署到生产环境，务必使用适当的生产级别服务器以确保应用程序的可靠性和安全性。

## 调试模式

`flask run` 命令不只可以启动开发服务器。如果您打开调试模式，那么服 务器会在修改应用代码之后自动重启，并且当请求过程中发生错误时还会在浏 览器中提供一个交互调试器。

![The interactive debugger in action.](%E5%9B%BE%E7%89%87/debugger.png)

Warning

调试器允许执行来自浏览器的任意 Python 代码。虽然它由一个 pin 保护， 但仍然存在巨大安全风险。不要在生产环境中运行开发服务器或调试器。

如果要打开调试模式，请使用 `--debug` 选项。

```
$ flask --app hello run --debug
 * Serving Flask app 'hello'
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn
```

另见：

- [开发服务器](https://dormousehole.readthedocs.io/en/latest/server.html) 和 [命令行接口](https://dormousehole.readthedocs.io/en/latest/cli.html) 包含有关调试模式运行的内容。
- [调试应用程序错误](https://dormousehole.readthedocs.io/en/latest/debugging.html) 包含有关内置调试器和其他调试器的内容。
- [日志](https://dormousehole.readthedocs.io/en/latest/logging.html) 和 [应用错误处理](https://dormousehole.readthedocs.io/en/latest/errorhandling.html) 包含有关日志记录和显示友 好的出错信息页面的内容

## HTML 转义

当返回 HTML （ Flask 中的默认响应类型）时，为了防止注入攻击，所有用户 提供的值在输出渲染前必须被转义。使用 Jinja （这个稍后会介绍）渲染的 HTML 模板会自动执行此操作。

在下面展示的 `escape()` 可以手动转义。因为保持简洁的 原因，在多数示例中它被省略了，但您应该始终留心处理不可信的数据。

```python
from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
```

如果一个用户想要提交其名称为 `<script>alert("bad")</script>` ，那么 宁可转义为文本，也好过在浏览器中执行脚本。

路由中的 `<name>` 从 URL 中**捕获值**并将其传递给视图函数。这些变量规则 见下文。

### 传递多个参数

要传递多个变量到 Flask 路由中，可以在路由路径中使用多个动态参数（dynamic parameter）。

以下是一个示例，展示如何传递多个变量到路由中：

```python
from markupsafe import escape
from flask import Flask

app = Flask(__name__)

@app.route("/<name>/<age>")
def hello(name, age):
    return f"Hello, {escape(name)}! Your age is {age}."

if __name__ == '__main__':
    app.run()
```



在这个示例中，我们定义了一个包含两个动态参数 `<name>` 和 `<age>` 的路由。当用户访问 `/John/25` 时，变量 `name` 将被赋值为 `"John"`，变量 `age` 将被赋值为 `"25"`。然后，我们可以在返回的响应中使用这两个变量。

## 路由

现代 web 应用都使用有意义的 URL ，这样有助于用户记忆，网页会更得到用 户的青睐，提高回头率。

使用 [`route()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask.route) 装饰器来把函数绑定到 URL:

```python
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```

但是能做的不仅仅是这些！您可以动态变化 URL 的某些部分， 还可以为一个函数指定多个规则。

### 蓝图（Blueprint）实现路由组

蓝图允许你将相关的路由和视图函数组织在一起，以便更好地管理和维护代码。

下面是在 Flask 中实现类似功能的代码示例：

我们先定义了 `user_bp` 蓝图，然后在蓝图定义后面定义了相应的路由函数。最后，我们在 `InitRouter` 结束之前注册了 `user_bp` 蓝图。

1. 创建蓝图：

```python
from flask import Blueprint

# 创建名为 user 的蓝图
user_bp = Blueprint('user', __name__)

@user_bp.route('/1.html')
def user1():
    return 'user1'

@user_bp.route('/2.html')
def user2():
    return 'user2'

# 将蓝图和前缀路径绑定，将蓝图注册到 Flask 应用中
app.register_blueprint(user_bp, url_prefix='/user')
```

**注意**：1.先使用了 `@admin_bp.route` 装饰器来定义蓝图的路由，最后再注册路由否则会报错

​            2.注意注册蓝图的名称user和定义的路由函数user_bp的名称不能相同



在这个示例中，我们使用 `@user_bp.route` 装饰器来定义具体的路由和视图函数。这些路由将会以 `/user` 前缀开始。注意，在视图函数上使用的装饰器是 `@user_bp.route` 而不是 `@app.route`。

最后，你可以像往常一样运行 Flask 应用，并访问 `/user/1.html` 和 `/user/2.html` 路径来触发对应的视图函数。

### 变量规则(指定类型)

通过把 URL 的一部分标记为 `<variable_name>` 就可以在 **URL 中添加变量**。 标记的部分会作为关键字参数传递给函数。通过使用 `<converter:variable_name>` ，可以选择性的加上一个转换器，为**变量指 定规则**。请看下面的例子:

```python
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # 显示该用户的用户配置文件
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #显示具有给定id的post，id是一个整数
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    #显示/path/之后的子路径
    return f'Subpath {escape(subpath)}'
```

转换器类型：

| `string` | （缺省值） 接受任何不包含斜杠的文本 |
| -------- | ----------------------------------- |
| `int`    | 接受正整数                          |
| `float`  | 接受正浮点数                        |
| `path`   | 类似 `string` ，但可以包含斜杠      |
| `uuid`   | 接受 UUID 字符串                    |

## 重定向url（应用笔记）

在 Flask 中，可以使用 `redirect` 函数来重新定位页面的 URL。该函数会返回一个新的响应对象，将用户重定向到指定的 URL。

以下是一个简单的示例：

```python
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # 重定向到 /new_url 路由
    return redirect(url_for('new_url')) #因为分文件编写，所以有时候读取不到可以不用url_for，直接写/new_url就行了

@app.route('/new_url')
def new_url():
    return '新的页面'

if __name__ == '__main__':
    app.run()
```

在上述示例中，我们创建了一个路由 `/`，当访问该路由时执行 `index()` 函数。在该函数中，我们使用 `redirect` 函数将用户重定向到 `/new_url` 路由，通过使用 `url_for` 函数来获取 `/new_url` 路由的 URL。

在 `/new_url` 路由中，我们返回一个简单的文本，代表重定向后的新页面。





## 如何在重定向的同时进行cookie操作

将重定向函数redirect绑定在make_response即可

```python
  resp = make_response(redirect('/admin')) #将要重定向的函数绑定在make_response中返回
        resp.set_cookie('username', username)
        resp.set_cookie('password', password)
        return resp
```



## 唯一的 URL / 重定向行为(重新定位url)

以下两条规则的不同之处在于是否使用尾部的斜杠。:

```python
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

`projects` 的 URL 是中规中矩的，尾部有一个斜杠，看起来就如同一个文 件夹。访问一个没有斜杠结尾的 URL （ `/projects` ）时 Flask 会自动进 行重定向，帮您在尾部加上一个斜杠（ `/projects/` ）。

`about` 的 URL 没有尾部斜杠，因此其行为表现与一个文件类似。如果访问 这个 URL 时添加了尾部斜杠（ `/about/` ）就会得到一个 404 “未找到” 错误。**这样可以保持 URL 唯一**，并有助于搜索引擎重复索引同一 页面。

### URL 构建

[`url_for()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.url_for) 函数用于**构建指定函数的 URL**。它把**函数名称作为第 一个参数**。它可以接受任意个关键字参数，每个关键字参数对应 URL 中的变量。 未知变量将添加到 URL 中作为查询参数。

为什么不在把 URL 写死在模板中，而要使用反转函数 [`url_for()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.url_for) 动态构建？

1. 反转通常比硬编码 URL 的描述性更好。
2. 您可以只在一个地方改变 URL ，而不用到处乱找。
3. URL 创建会为您处理特殊字符的转义，比较直观。
4. 生产的路径总是绝对路径，可以避免相对路径产生副作用。
5. 如果您的应用是放在 URL 根路径之外的地方（如在 `/myapplication` 中，不在 `/` 中）， [`url_for()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.url_for) 会为您妥善处理。

例如，这里我们使用 [`test_request_context()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask.test_request_context) 方法来尝 试使用 [`url_for()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.url_for) 。 [`test_request_context()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask.test_request_context) 告诉 Flask 正在处理一个请求， 而实际上也许我们正处在交互 Python shell 之中，并没有真正的请求。参见 [本地环境](https://dormousehole.readthedocs.io/en/latest/quickstart.html#context-locals) 。

```python
from flask import url_for //导入 url_for()

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```

**在测试请求上下文中，`url_for` 函数将生成以下输出（服务器端）：**

在服务器开始的时候会执行一次

`url_for` 函数接受视图函数名作为参数，并返回匹配该视图函数的 URL。在使用 `url_for` 函数之前，需要创建一个模拟请求上下文，以便函数能够正常工作

```
/
/login
/login?next=/
/user/John%20Doe
```

第一个 `url_for('index')` 生成了根路由 `/` 对应的 URL。由于根路径没有其他参数，因此它只返回 `/`。

第二个 `url_for('login')` 生成了 `/login` 路由对应的 URL。

第三个 `url_for('login', next='/')` 生成了带有查询参数的 URL，其中 `next` 参数的值为 `/`，在这种情况下，生成的 URL 为 `/login?next=%2F`。注意，`/` 在 URL 中被转义为 `%2F`。

最后一个 `url_for('profile', username='John Doe')` 生成了 `/user/<username>` 路由对应的 URL，并将 `<username>` 替换为给定的名称，生成的 URL 为 `/user/John%20Doe`。注意，空格被转义为 `%20`。

请注意，这些输出是在模拟请求上下文下生成的结果，在实际的应用程序中，您可能需要将 `url_for` 函数用于模板渲染或重定向等情况。

- `'index'`：在 `url_for()` 函数中传递的参数是视图函数的名称，这里是 `'index'`，表示要生成指向名为 `'index'` 的视图函数的 URL。

### HTTP 方法

Web 应用使用不同的 HTTP 方法处理 URL 。当您使用 Flask 时，应当熟悉 HTTP 方法。缺省情况下，一个路由只回应 `GET` 请求。可以使用 [`route()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask.route) 装饰器的 `methods` 参数来处理不同的 HTTP 方法。

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

上例中把路由的所有方法都放在同一个函数中，当每个方法都使用一些共同的 数据时，这样是有用的。

#### 将方法放入函数中返回

你也可以把**不同方法**所对应的视图分别放在**独立的函数**中。 Flask 为每个常用 的 HTTP 方法提供了捷径，如 [`get()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask.get) 、 [`post()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask.post) 等等。

```python
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()
```

如果当前使用了 `GET` 方法， Flask 会自动添加 `HEAD` 方法支持，并 且同时还会按照 [HTTP RFC](https://www.ietf.org/rfc/rfc2068.txt) 来处理 `HEAD` 请求。同样， `OPTIONS` 也会自动实现。

## 静态文件

动态的 web 应用也需要静态文件，一般是 CSS 和 JavaScript 文件。理想情 况下您的服务器已经配置好了为您的提供静态文件的服务。但是在开发过程中， Flask 也能做好这项工作。只要在您的包或模块旁边创建一个名为 `static` 的文件夹就行了。静态文件位于应用的 `/static` 中。

使用特定的 `'static'` 端点就可以生成相应的 URL

```python
url_for('static', filename='style.css')
```

这个静态文件在文件系统中的位置应该是 `static/style.css` 。

**使用静态文件**

1. 在网页的 HTML 代码中使用生成的 URL 来引用静态文件。您可以在 `<link>` 或 `<script>` 标签中使用 `href` 或 `src` 属性来指定静态文件的 URL。例如：

   ```
   <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
   <script src="{{ url_for('static', filename='script.js') }}"></script>
   ```

   

   在上面的示例中，`{{ url_for('static', filename='style.css') }}` 和 `{{ url_for('static', filename='script.js') }}` 分别会被替换为生成的静态文件的 URL。

现在，当网页加载时，会从指定的 URL 加载并应用静态文件（例如 CSS 文件和 JavaScript 文件）。请确保在 Flask 应用程序的模板中正确使用生成的静态文件 URL，使浏览器能够正确加载和渲染这些文件

## 请求的方式来访问静态文件（客户端访问）

通过请求的方式来访问静态文件，可以使用 Flask 提供的 `send_from_directory` 函数。以下是进行该操作的步骤：

1. 确保您的静态文件位于 Flask 应用程序的指定静态文件夹内。默认情况下，静态文件夹为 `static`，可在 Flask 应用程序中使用 `app.static_folder` 获取静态文件夹的路径。

2. 导入 `send_from_directory` 函数，并使用它处理请求并发送静态文件。在视图函数中，使用 `send_from_directory` 函数将请求的静态文件发送给客户端。例如，下面是一个处理音频文件的示例：

   ```python
   from flask import Flask, send_from_directory
   
   app = Flask(__name__)
   
   @app.route('/audio/<filename>')
   def get_audio(filename):
       # 通过 send_from_directory 发送请求的静态文件
       return send_from_directory('static', filename, mimetype='audio/mp3')
   //'static' (./static) 指定静态文件夹的路径，filename 特定的文件，`mimetype` 设置响应的 MIME 类型
   ```

   

   在上面的示例中，`/audio/<filename>` 定义了一个带有动态路由参数的路由。请求路径中的 `<filename>` 部分将作为参数传递给 `get_audio` 视图函数。

3. 当客户端通过 `/audio/<filename>` 访问特定的音频文件时，会触发 `get_audio` 视图函数，并使用 `send_from_directory` 函数发送对应的静态文件。使用 `send_from_directory` 函数时，可以指定静态文件夹的路径（`app.static_folder`）、文件名和适当的 MIME 类型。

请注意，使用此方法访问静态文件需要在视图函数中处理请求，并确保静态文件夹和文件所在的路径正确配置。此外，还要根据需要指定正确的 MIME 类型，以确保浏览器能够正确解析和处理请求的静态文件。

`mimetype` 是在 Flask 中用于设置响应的 MIME 类型（即 Multipurpose Internet Mail Extensions 类型）的参数。MIME 类型指示了在 Web 上传输的文件的内容类型。根据不同的文件类型，可以使用不同的 MIME 类型来确保客户端正确解析和处理文件。

**以下是一些常见的 MIME 类型示例：**

- `"text/html"`: 表示 HTML 文档。
- `"application/json"`: 表示 JSON 数据。
- `"application/pdf"`: 表示 PDF 文档。
- `"image/jpeg"`: 表示 JPEG 图像。
- `"audio/mp3"`: 表示 MP3 音频文件。
- `"video/mp4"`: 表示 MP4 视频文件。

## 渲染模板(传输页面和修改页面)

在 Python 内部生成 HTML 不好玩，且相当笨拙。因为您必须自己负责 HTML 转义，以确保应用的安全。因此， Flask 自动为您配置 [Jinja2](https://palletsprojects.com/p/jinja/) 模板引擎。

模板可被用于生成任何类型的文本文件。对于 web 应用来说，主要用于生成 HTML 页面，但是也可以生成 markdown 、用于电子邮件的纯文本等等。

HTML 、 CSS 和其他 web API ，请参阅 [MDN Web 文档](https://developer.mozilla.org/) 。

使用 [`render_template()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.render_template) 方法可以渲染模板，您只要提供模板 名称和需要作为参数传递给模板的变量就行了。下面是一个简单的模板渲染例 子:

```python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>') 
def hello(name=None): #name=None 表示 hello 视图函数的 name 参数的默认值为 None
    return render_template('hello.html', name=name) 
#hello.html包含在templates文件夹中，在根目录下创建templates文件夹
```

当访问 `/hello/` 路由时，会调用 `hello` 视图函数，并渲染 `hello.html` 模板。当访问 `/hello/<name>` 路由时，会将 URL 中的 `name` 参数传递给视图函数，并在模板中显示。**在模板中**，可以使用 `{{ name }}` 来显示传递的 `name` 参数的值。



Flask 会在 **templates**文件夹内寻找模板。因此，如果您的应用是一 个模块，那么模板文件夹应该在模块旁边；如果是一个包，那么就应该在包里 面：

**情形 1** : 一个模块:

```python
/application.py
/templates
    /hello.html
```

**情形 2** : 一个包:

```python
/application
    /__init__.py
    /templates
        /hello.html
```

您可以充分使用 Jinja2 模板引擎的威力。更多内容，详见官方 [Jinja2 模板文档](https://jinja.palletsprojects.com/templates/) 。

### **使用判断语句生成不同页面**

模板示例：

```html
<!doctype html>
<title>Hello from Flask</title>
{% if name %} //判断语句，如果存在name则输出不存在则到else
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```

1. `<!doctype html>`：声明该 HTML 文档类型为 HTML5。
2. `<title>Hello from Flask</title>`：设置页面的标题为 “Hello from Flask”。
3. `{% if name %}` 和 `{% else %}`：这是 Flask 模板引擎中的条件语句。它判断 `name` 变量是否存在或为真。
4. `<h1>Hello {{ name }}!</h1>`：如果 `name` 变量存在或为真，则在页面上显示 `<h1>` 标签内的文本 "Hello "，后面跟着 `name` 变量的值，最后是感叹号。
5. `<h1>Hello, World!</h1>`：如果 `name` 变量不存在或为假，则在页面上显示 `<h1>` 标签内的文本 “Hello, World!”。

通过模板中的条件语句，根据 `name` 参数的值来显示不同的欢迎消息。如果传递了 `name` 参数，就会显示 “Hello [name]!”，否则显示 “Hello, World!”。这种动态生成 HTML 内容的能力使得页面能够根据不同的情况呈现不同的内容。



在模板内部可以像使用 [`url_for()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.url_for) 和 [`get_flashed_messages()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.get_flashed_messages) 函数一样访问 [`config`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask.config) 、 [`request`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.request) 、 [`session`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.session) 和 [`g`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.g) [1](https://dormousehole.readthedocs.io/en/latest/quickstart.html#id11) 对象。

模板在继承使用的情况下尤其有用。其工作原理参见 [模板继承](https://dormousehole.readthedocs.io/en/latest/patterns/templateinheritance.html) 。简单的说，模板继承可以使每个页 面的特定元素（如页头、导航和页尾）保持一致。

自动转义默认开启。因此，如果 `name` 包含 HTML ，那么会被自动转义。 如果您可以信任某个变量，且知道它是安全的 HTML （例如变量来自一个把 wiki 标记转换为 HTML 的模块），那么可以使用 `Markup` 类把它标记为安全的，或者在模板中使用 `|safe` 过滤器。更多例子参见 Jinja 2 文档。

下面 `Markup` 类的基本使用方法:

```python
>>> from markupsafe import Markup
>>> Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
Markup('<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')
>>> Markup.escape('<blink>hacker</blink>')
Markup('&lt;blink&gt;hacker&lt;/blink&gt;')
>>> Markup('<em>Marked up</em> &raquo; HTML').striptags()
'Marked up » HTML'
```

这段代码演示了在 Flask 中使用 `markupsafe` 模块中的 `Markup` 类来处理 HTML 字符串，以确保安全显示和渲染 HTML 内容。

以下是对这段代码的解释：

```python
from markupsafe import Markup

Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
```



这里使用 `Markup` 类创建了一个包含 HTML 标签的字符串，`%` 运算符用于将 `%s` 占位符替换为 `'<blink>hacker</blink>'`。由于使用了 `Markup` 类，字符串内容会被转义，确保 `<blink>` 标签不会被执行，而是以纯文本形式显示。

```python
Markup('<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')
```



这行代码展示了使用了 `Markup.escape` 方法来转义 HTML 字符串，将其中的特殊字符变为实体编码。这样可以确保 HTML 内容以纯文本形式显示，而不会被浏览器解释为标签。

```python
Markup.escape('<blink>hacker</blink>')
```



这行代码展示了使用 `Markup.escape` 方法将字符串中的 HTML 字符转义为实体编码。它对 `<blink>hacker</blink>` 中的特殊字符进行转义，将其变为 `<blink>hacker</blink>`。

```python
Markup('<em>Marked up</em> &raquo; HTML').striptags()
```



这行代码展示了使用 `Markup.striptags` 方法去除 HTML 字符串中的所有标签，并返回纯文本形式的内容。结果为 `'Marked up » HTML'`，其中 `»` 被转换为对应的字符 `»`。

`markupsafe` 模块中的 `Markup` 类提供了一种安全处理和显示 HTML 内容的方法，可以防止潜在的跨站脚本攻击 (XSS)。通过转义或去除 HTML 标签，可以确保 HTML 内容以纯文本形式呈现，而不会被浏览器解析为标签。这有助于保护应用程序的安全性。

*Changed in version 0.5:* 自动转义不再为所有模板开启，只为扩展名为 `.html` 、 `.htm` 、 `.xml` 和 `.xhtml` 开启。从字符串载入的模板会关闭自动转义。

- [1](https://dormousehole.readthedocs.io/en/latest/quickstart.html#id10)

  不确定 [`g`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.g) 对象是什么？它是某个可以根据需要储存 信息的东西，详见 [`g`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.g) 对象的文档和 [使用 SQLite 3](https://dormousehole.readthedocs.io/en/latest/patterns/sqlite3.html) 。

。

## 操作请求数据

对于 web 应用来说对客户端向服务器发送的数据作出响应很重要。在 Flask 中由全局对象 [`request`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.request) 来提供请求信息。如果您有一些 Python 基础，那么可能 会奇怪：既然这个对象是全局的，怎么还能保持线程 安全？答案是本地环境：

### 本地环境

内部信息

如果您想了解工作原理和如何使用本地环境进行测试，那么请阅读本节， 否则可以跳过本节。

某些对象在 Flask 中是全局对象，但不是通常意义下的全局对象。这些对象实 际上是特定环境下本地对象的代理。真拗口！但还是很容易理解的。

设想现在处于处理线程的环境中。一个请求进来了，服务器决定生成一个新线 程（或者叫其他什么名称的东西，这个下层的东西能够处理包括线程在内的并 发系统）。当 Flask 开始其内部请求处理时会把当前线程作为活动环境，并把 当前应用和 WSGI 环境绑定到这个环境（线程）。它以一种聪明的方式使得一 个应用可以在不中断的情况下调用另一个应用。

这对您有什么用？基本上您可以完全不必理会。这个只有在做单元测试时才有 用。在测试时会遇到由于没有请求对象而导致依赖于请求的代码会突然崩溃的 情况。对策是自己创建一个请求对象并绑定到环境。最简单的单元测试解决方 案是使用 [`test_request_context()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask.test_request_context) 环境管理器。通过使 用 `with` 语句可以绑定一个测试请求，以便于交互。例如:

```python
from flask import request

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'
```

另一种方式是把整个 WSGI 环境传递给 [`request_context()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask.request_context) 方法:

```python
with app.request_context(environ):
    assert request.method == 'POST'
```

### 请求对象（POST,GET）

请求对象在 API 一节中有详细说明这里不细谈（参见 [`Request`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Request) ）。这里简略地谈一下最常见的操作。首先，您必 须从 `flask` 模块导入请求对象:

```python
from flask import request
```

通过使用 [`method`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Request.method) 属性可以操作当前请求方法，通过 使用 [`form`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Request.form) 属性处理表单数据（在 `POST` 或者 `PUT` 请求中传输的数据）。以下是使用上述两个属性的例子:

```python
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
            #如果请求方法
            #为GET或凭据无效
    return render_template('login.html', error=error)
```

当 `form` 属性中不存在这个键时会发生什么？会引发一个 [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError) 。如果您不像捕捉一个标准错误一样捕捉 [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError) ， 那么会显示一个 HTTP 400 Bad Request 错误页面。因此，多数情况下您不必 处理这个问题。

要操作 URL （如 `?key=value` ）中提交的参数可以使用 [`args`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Request.args) 属性:

```
searchword = request.args.get('key', '')
```

用户可能会改变 URL 导致出现一个 400 请求出错页面，这样降低了用户友好 度。因此，我们推荐使用 get 或通过捕捉 [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError) 来访问 URL 参数。

完整的请求对象方法和属性参见 [`Request`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Request) 文档。

### POST,GET接收方式

在 Flask 中，要接收通过 POST 请求发送的数据，您可以使用 `request.form` 或 `request.json` 来访问请求的表单数据或 JSON 数据。

以下是一个在 Flask 中**post**接收数据的示例代码：

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/admin/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    repassword = request.form.get("repassword")

    # 处理注册逻辑...

    return jsonify(message="注册成功")

if __name__ == "__main__":
    app.run()
```

在上述示例中，我们使用 `request.form.get()` 来获取通过 POST 请求发送的表单数据。`request.form.get("参数名")` 方法可以访问请求中指定参数的值。

如果您发送的是 JSON 数据，您可以改用 `request.json.get()` 方法来获取 JSON 数据中的值。示例如下：

```python
@app.route("/admin/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    repassword = data.get("repassword")

    # 处理注册逻辑...

    return jsonify(message="注册成功")
```

在上述示例中，我们首先使用 `request.json` 来访问整个 JSON 数据对象，然后使用 `data.get("参数名")` 来获取指定参数的值。

请根据您发送请求的方式（表单数据或 JSON 数据）选择使用适当的方式来接收数据，并进行相应的处理。

**GET：**

在 Flask 中，您可以使用 `request.args` 来接收 Vue.js 发来的 GET 请求中的参数。下面是一个简单的示例：

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['GET'])
def handle_get_request():
    name = request.args.get('name')  # 通过传递的参数名获取值
    age = request.args.get('age')

    # 在这里可以进行进一步的处理

    return f"Name: {name}, Age: {age}"

if __name__ == '__main__':
    app.run()
```



在上述示例中，我们创建了一个路由 `/submit` 并通过 GET 方法处理请求。使用 `request.args.get()` 方法来获取 GET 请求中传递的参数值。

### 文件上传

用 Flask 处理文件上传很容易，只要确保不要忘记在您的 HTML 表单中设置 `enctype="multipart/form-data"` 属性就可以了。否则浏览器将不会传送 您的文件。

已上传的文件被储存在内存或文件系统的临时位置。您可以通过请求对象 `files` 属性来访问上传的文件。每个上传的文件都储 存在这个字典型属性中。这个属性基本和标准 Python `file` 对象一 样，另外多出一个用于把上传文件保存到服务器的文件系统中的 [`save()`](https://werkzeug.palletsprojects.com/en/2.3.x/datastructures/#werkzeug.datastructures.FileStorage.save) 方法。下例展示其如 何运作:

```python
from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file'] #用对象 `files` 属性来访问上传的文件
        f.save('/var/www/uploads/uploaded_file.txt') #保存文件位置
    ...
```

如果想要知道**文件上传**之前其在客户端系统中的**名称**，可以使用 [`filename`](https://werkzeug.palletsprojects.com/en/2.3.x/datastructures/#werkzeug.datastructures.FileStorage.filename) 属性。但是请牢 记这个值是可以伪造的，永远不要信任这个值。如果想要把客户端的文件名作 为服务器上的文件名，可以通过 Werkzeug 提供的 [`secure_filename()`](https://werkzeug.palletsprojects.com/en/2.3.x/utils/#werkzeug.utils.secure_filename) 函数:

```python
from werkzeug.utils import secure_filename #secure_filename()需要包含的包

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")
    ...
```

更好的例子参见 [上传文件](https://dormousehole.readthedocs.io/en/latest/patterns/fileuploads.html) 。

### Cookies

要访问 cookies ，可以使用 [`cookies`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Request.cookies) 属性。可以使 用响应对象 的 [`set_cookie`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Response.set_cookie) 方法来设置 cookies 。 请求对象的 [`cookies`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Request.cookies) 属性是一个包含了客户端传输 的所有 cookies 的字典。在 Flask 中，如果使用 [会话](https://dormousehole.readthedocs.io/en/latest/quickstart.html#sessions) ，那么就 不要直接使用 cookies ，因为 [会话](https://dormousehole.readthedocs.io/en/latest/quickstart.html#sessions) 比较安全一些。

**读取 cookies:**

```python
from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username') #这个方法会从请求中的 Cookie 数据中查找名为 'username' 的 Cookie，并返回其值
    #使用cookies。get（key）而不是cookies[key]不获取
    #如果cookie丢失，则KeyError。
```

如果cookie中无username值，则返回的是None

**储存 cookies:**

使用flask中的make_response

```python
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username',3600) #用于在响应对象中设置 cookie。它接受两个参数，第一个是 cookie 的名称，第二个是 cookie 的值。max_age(可选，为过期时间),3600是指一小时后过期
    return resp #返回响应对象，响应将会包含设置的 cookie
```

注意， cookies 设置在响应对象上。通常只是从视图函数返回字符串， Flask 会把它们转换为响应对象。如果您想显式地转换，那么可以使用 [`make_response()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.make_response) 函数，然后再修改它。

使用 doc:patterns/deferredcallbacks 方案可以在没有响应对象的情况下 设置一个 cookie 。

另见 [关于响应](https://dormousehole.readthedocs.io/en/latest/quickstart.html#about-responses) 。

## 删除cookie

要删除 Flask 中的 Cookie，可以使用 `make_response()` 方法来创建一个响应对象，然后调用其 `delete_cookie()` 方法来删除指定的 Cookie。

以下是一个简单的示例：

```python
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response('原本return要接收的返回值')
    resp.delete_cookie('my_cookie')
    return resp

if __name__ == '__main__':
    app.run()
```



在上述示例中，我们创建了一个路由 `/`，当访问该路由时执行 `index()` 函数。在该函数中，我们使用 `make_response()` 创建一个响应对象，并传入要返回的内容。然后，我们通过 `delete_cookie()` 方法来删除名为 `my_cookie` 的 Cookie。最后，我们返回这个响应对象。

通过调用 `delete_cookie()` 方法来删除指定的 Cookie，需要传入要删除的 Cookie 的名称作为参数。

## 重定向和错误

使用 [`redirect()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.redirect) 函数可以重定向。使用 [`abort()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.abort) 可以更早退出请求，并返回错误代码:

```python
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
```

上例实际上是没有意义的，它让一个用户从索引页重定向到一个无法访问的页 面（401 表示禁止访问）。但是上例可以说明重定向和出错跳出是如何工作的。

缺省情况下每种出错代码都会对应显示一个黑白的出错页面。使用 [`errorhandler()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask.errorhandler) 装饰器可以定制出错页面:

## 定制出错页面

```python
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```

注意 [`render_template()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.render_template) 后面的 `404` ，这表示页面对就的 出错代码是 404 ，即页面不存在。缺省情况下 200 表示：一切正常。

详见 [应用错误处理](https://dormousehole.readthedocs.io/en/latest/errorhandling.html) 。

## 关于响应

**视图函数**的返回值会自动转换为一个响应对象。如果返回值是一个**字符串**，那 么会被转换为一个**包含作为响应体的字符串**、一个 `200 OK` 出错代码 和一 个 *text/html* 类型的响应对象。如果返回值是一个**字典或者列表**， 那么会调用 `jsonify()` 来产生一个响应。以下是转换的规则：

1. 如果视图返回的是一个**响应对象**，那么就直接返回它。
2. 如果返回的是一个**字符串**，那么根据这个字符串和缺省参数生成一个用于 返回的响应对象。
3. 如果返回的是一个**迭代器或者生成器**，那么返回字符串或者字节，作为流 响应对待。
4. 如果返回的是一个字典或者列表，那么使用 [`jsonify()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.json.jsonify) 创建一个响应对象。
5. 如果返回的是一个元组，那么元组中的项目可以提供额外的信息。元组中 必须至少包含一个项目，且项目应当由 `(response, status)` 、 `(response, headers)` 或者 `(response, status, headers)` 组 成。 `status` 的值会重载状态代码， `headers` 是一个由额外头部 值组成的列表或字典。
6. 如果以上都不是，那么 Flask 会假定返回值是一个有效的 WSGI 应用并把 它转换为一个响应对象。

如果想要在视图内部掌控响应对象的结果，那么可以使用 [`make_response()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.make_response) 函数。

设想有如下视图:

```python
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
```

可以使用 [`make_response()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.make_response) 包裹返回表达式，获得响应对象， 并对该对象进行修改，然后再返回:

```python
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
```

### JSON 格式的 API响应

JSON 格式的响应是常见的，用 Flask 写这样的 API 是很容易上手的。如果从 视图返回一个 `dict` 或者 `list` ，那么它会被转换为一个 JSON 响应。

```python
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }
```

如果 `dict` 还不能满足需求，还需要创建其他类型的 JSON 格式响应，可 以使用 [`jsonify()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.json.jsonify) 函数。该函数会序列化任何支持的 JSON 数据类型。也可以研究研究 Flask 社区扩展，以支持更复杂的应用。

```python
@app.route("/users")
def users_api():
    users = get_all_users()
    return [user.to_json() for user in users]
```

这是一个向 [`jsonify()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.json.jsonify) 函数传递数据的捷径，可以序列化 任何支持的 JSON 数据类型。这也意味着在字典和列表中的所有数据必须可以 被序列化。

对于复杂的数据类型，如数据库模型，你需要使用序列化库先把数据转换为合 法的 JSON 类型。有许多库，以及社区维护的 Flask API 扩展可以处理复杂数 据类型，

## 会话

除了请求对象之外还有一种称为 [`session`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.session) 的对象，允许您在 不同请求之间储存信息。这个对象相当于用密钥签名加密的 cookie ，即用户 可以查看您的 cookie ，但是如果没有密钥就无法修改它。

使用会话之前您必须设置一个密钥。举例说明:

```python
from flask import session

# 将密钥设置为一些随机字节。保守这个秘密！
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:  #判断用户是否已登录
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index')) #这行代码的目的是将用户的请求重定向到名为 'index' 的视图函数所对应的 URL。用户在登录后，将被重定向到该 URL 所指定的页面
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form> 
    '''    #'''模板语法

@app.route('/logout') #登出
def logout():
    # 从会话中删除username（如果存在）
    session.pop('username', None)
    return redirect(url_for('index'))
```

### 如何生成一个好的密钥

生成随机数的关键在于一个好的随机种子，因此一个好的密钥应当有足够 的随机性。操作系统可以有多种方式基于密码随机生成器来生成随机数据。 使用下面的命令可以快捷的为 `Flask.secret_key` （ 或者 [`SECRET_KEY`](https://dormousehole.readthedocs.io/en/latest/config.html#SECRET_KEY) ）生成值:

```
$ python -c 'import secrets; print(secrets.token_hex())'
'192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
```

基于 cookie 的会话的说明： Flask 会取出会话对象中的值，把值序列化后储 存到 cookie 中。在打开 cookie 的情况下，如果需要查找某个值，但是这个 值在请求中没有持续储存的话，那么不会得到一个清晰的出错信息。请检查页 面响应中的 cookie 的大小是否与网络浏览器所支持的大小一致。

除了缺省的客户端会话之外，还有许多 Flask 扩展支持服务端会话。

## Python实现JWT-Token详解

### 引言

>   Token是目前广泛使用的一种保持会话状态的技术，与以前的cookie、session共同存在于如今各大网站架构中。本篇中，我们着重来讲解在python中，怎样实现token。 


首先，我们来看一下`session`的主要缺点：

当我们在使用`session`保持会话状态，同时验证用户的合法性时，有两个问题存在:

- 性能问题
  因为`session`的实现过程，需要用户在每次请求中携带`sessionid`，服务端收到后，对比数据库中的`sessionid`是否一致。而我们知道，数据库的操作往往是服务端最常见的性能瓶颈。
- 扩展性问题
  当用户量变多后，后端往往采用多个服务器，多个节点。但多个节点都要访问`session`，这样就要去数据库服务能被多个节点访问，不方便分库以提高性能。

而`Token`可以很好的解决这些问题

### 原理

`session`的机制是把数据信息放在服务端，正常情况下，服务端数据是无法被篡改的，从而保证验证的可靠性。

而`Token`是将拼接好的数据信息传给客户端，客户每次请求携带过来给服务端。服务端直接根据携带的数据信息进行校验。

那为什么，`token`将信息存放在客户端，而不会有被篡改的风险呢？服务端又是怎么验证`token`数据的完整性的呢？？

目前，`JWT(Json Web Token)`是目前运用最广泛的认证解决方案，由于非常靠谱，已经被写入行业标准`RFC 7519`

### python实现JWT-token

在Python中，有一个包`pyjwt`，专门用来生成token，接下来，我们使用这个包，快速的生成我们想要的token

安装：

```cmd
pip install pyjwt
```

#### **生成Token**

```python
import jwt
import time

# 生成一个字典，包含我们的具体信息
d = {<!-- -->
    # 公共声明
    'exp':time.time()+3000, # (Expiration Time) 此token的过期时间的时间戳，移除可以设置无过期时间
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

#### 解码token

```python
import jwt
jwt_encode = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjI2MDQ3MTguNjczNjgzNiwiaWF0IjoxNjIyNjAxNzE4LjY3MzY4MzYsImlzcyI6Iklzc3VlciIsImRhdGEiOnsidXNlcm5hbWUiOiJ4amoiLCJ0aW1lc3RhbXAiOjE2MjI2MDE3MTguNjczNjgzNn19.ASgB9-1U9ADhv6AmBH7p8leEtWMTMhaDQJSaZ9z9kZg'

jwt_decode = jwt.decode(jwt_encode, '123456', issuer='Issuer',  algorithms=['HS256'])

print(jwt_decode)
# 打印解密后信息
# {'exp': 1622604718.6736836, 'iat': 1622601718.6736836, 'iss': 'Issuer', 'data': {'username': 'xjj', 'timestamp': 1622601718.6736836}}

```

使用现成的`pyjwt`，我们就可以像这样快速的生成token。

## 消息闪现

一个好的应用和用户接口都有良好的反馈，否则到后来用户就会讨厌这个应用。 Flask 通过闪现系统来提供了一个易用的反馈方式。闪现系统的基本工作原理 是在请求结束时记录一个消息，提供且只提供给下一个请求使用。通常通过一 个布局模板来展现闪现的消息。

[`flash()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.flash) 用于闪现一个消息。在模板中，使用 [`get_flashed_messages()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.get_flashed_messages) 来操作消息。完整的例子参见 [消息闪现](https://dormousehole.readthedocs.io/en/latest/patterns/flashing.html) 。

## 日志

<details class="changelog"><summary style="cursor: pointer; font-style: italic; margin-bottom: 10px;">Changelog</summary><div class="versionadded"><p style="hyphens: auto; line-height: 1.4;"><span class="versionmodified added" style="font-style: italic;"></span></p></div></details>

有时候可能会遇到数据出错需要纠正的情况。例如因为用户篡改了数据或客户 端代码出错而导致一个客户端代码向服务器发送了明显错误的 HTTP 请求。多 数时候在类似情况下返回 `400 Bad Request` 就没事了，但也有不会返回的 时候，而代码还得继续运行下去。

这时候就需要使用日志来记录这些不正常的东西了。自从 Flask 0.3 后就已经 为您配置好了一个日志工具。

以下是一些日志调用示例:

```
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')
```

[`logger`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask.logger) 是一个标准的日志 [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger) 类，更多信息详见官方的 [`logging`](https://docs.python.org/3/library/logging.html#module-logging) 文档。

参见 [应用错误处理](https://dormousehole.readthedocs.io/en/latest/errorhandling.html) 。

## 集成 WSGI 中间件

如果想要在应用中添加一个 WSGI 中间件，那么可以用应用的 `wsgi_app` 属性来包装。例如，假设需要在 Nginx 后面使用 [`ProxyFix`](https://werkzeug.palletsprojects.com/en/2.3.x/middleware/proxy_fix/#werkzeug.middleware.proxy_fix.ProxyFix) 中间件，那么可以这样 做:

```
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)
```

用 `app.wsgi_app` 来包装，而不用 `app` 包装，意味着 `app` 仍旧 指向您的 Flask 应用，而不是指向中间件。这样可以继续直接使用和配置 `app` 。

## 使用 Flask 扩展

扩展是帮助完成公共任务的包。例如 Flask-SQLAlchemy 为在 Flask 中轻松使 用 SQLAlchemy 提供支持。

更多关于 Flask 扩展的内容请参阅 [扩展](https://dormousehole.readthedocs.io/en/latest/extensions.html) 。

## 部署到网络服务器

已经准备好部署您的新 Flask 应用了？请移步 [生产部署](https://dormousehole.readthedocs.io/en/latest/deploying/index.html) 。A

#pymysql的基本使用
PyMySQL是在 Python3.x 版本中用于连接 MySQL 服务器的一个库。 接下来将介绍一些PyMySQL的一些基本操作。

# 数据库连接

### 1.数据库连接

**安装pymysql**

```python
pip install pymysql
```

```python
import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='testuser',
                     password='test123',
                     database='TESTDB')
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()

```

cursor 光标 execute执行

### 2.创建新的数据库表

```python
import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='testuser',
                     password='test123',
                     database='TESTDB')
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute() 方法执行 SQL，如果（EMPLOYEE）表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
 
# 使用预处理语句创建（EMPLOYEE）表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
 
cursor.execute(sql)
 
# 关闭数据库连接
db.close()

```

### 3.插入数据

```python
import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='testuser',
                     password='test123',
                     database='TESTDB')
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 插入语句
#sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
      # LAST_NAME, AGE, SEX, INCOME) \
       #VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
       #('Mac', 'Mohan', 20, 'M', 2000) 
#使用参数化更好
 sql = "INSERT INTO user(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES (%s, %s, %s,  %s,  %s)"
 cursor.execute(sql, ('Mac', 'Mohan', 20, 'M', 2000) )
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交事务，否则数据库中不会出现数据
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()
 
# 关闭数据库连接
db.close()

```

使用参数化防止sql注入：

```py
 sql = "INSERT INTO user(username, password) VALUES (%s, %s)"
            cursor.execute(sql, (username, password))
   db.commit()
```

执行语句之后一定要记得提交事务db.commit()

而面对要插入多条数据时，我们需要换一下操作。

```python
import pymysql
 
# 建立连接
conn = pymysql.connect(
    host="192.168.0.103",
    port=3306,
    user="root",
    password="123",
    database="xing",
    charset="utf8"
)
# 获取一个光标
cursor = conn.cursor()
# 定义将要执行的SQL语句
sql = "insert into userinfo (user, pwd) values (%s, %s);"
name = "wuli"
pwd = "123456789"
# 并执行SQL语句
cursor.execute(sql, [name, pwd])
# 涉及写操作注意要提交
conn.commit()
# 关闭连接
 
# 获取最新的那一条数据的ID
last_id = cursor.lastrowid
print("最后一条数据的ID是:", last_id)
 
cursor.close()
conn.close()

```

### 4.删除数据

```python
import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='testuser',
                     password='test123',
                     database='TESTDB')
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE &gt; %s" % (20)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()
 
# 关闭连接
db.close()

```

### 5.更新数据

```python
import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='testuser',
                     password='test123',
                     database='TESTDB')
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()
 
# 关闭数据库连接
db.close()

```



### 6.查询数据

```python
import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='testuser',
                     password='test123',
                     database='TESTDB')
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 查询语句
#sql = "SELECT * FROM EMPLOYEE \
       #WHERE INCOME &gt; %s" % (1000)

try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表(数组)
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
       # 打印结果
      print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fetch data")
 
# 关闭数据库连接
db.close()

```

这里就是数据库的一些基本操作，能够满足pymysql的基本使用。

检测当查询不到数据的情况：

```sql
SREACHTSQL = f"UPDATE banner_table SET {SetTitle} {SetDescription} {SetHref} WHERE ID = %s;"
DBCONN = g.db.cursor()
params.append(banners_id)
DBCONN.execute(SREACHTSQL, params)
g.db.commit()

if DBCONN.rowcount == 0:
    # 处理ID不存在的情况，可以抛出异常或返回自定义错误信息
    raise Exception("Banner ID not found")
```

**参数化**：

```python
sql = "SELECT * FROM user WHERE username = %s"
DBCONN.execute(sql, (username))
```

### Flask将变量绑定到上下文中

要在 Flask 中将变量绑定到上下文中，你可以使用 Flask 的上下文对象和上下文处理器。

Flask 提供了两种类型的上下文：应用上下文（Application Context）和请求上下文（Request Context）。应用上下文是全局的，用于存储应用程序级别的变量，而请求上下文是与每个请求相关的，用于存储请求级别的变量。

下面是关于如何将变量绑定到上下文的示例：

```python
import pymysql
from flask import Flask, g, request

app = Flask(__name__)

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='blog')

# 使用上下文处理器将数据库连接对象绑定到请求上下文中
@app.before_request
def before_request():
    g.db = db

@app.route('/')
def index():
    # 在视图函数中可以通过 g 对象访问请求上下文中的数据库连接对象
    print(g.db)  # 输出：数据库连接对象
    return "Hello World"

if __name__ == '__main__':
    app.run()
```



在这个修改后的代码中，我们使用 `@app.before_request` 装饰器定义了一个在每个请求之前执行的函数 `before_request`。在该函数中，我们将数据库连接对象 `db` 绑定到 `g` 对象上，使其可以在整个请求上下文中访问。

防止在上下文传递中数据库断开连接：

```python
if not g.db.open:
    g.db.ping(reconnect=True)
```

# 写项目的时候遇到的一些错误

## **防止在上下文传递中数据库断开连接：**

在上下文中加上：

```
if not g.db.open:
    g.db.ping(reconnect=True)
```

## 删表和建表操作要分开写：

```python
cursor.execute("DROP TABLE IF EXISTS `custom_table`;")
CustomSql = """CREATE TABLE `custom_table`  (
  `ID` int(10) PRIMARY KEY,
  `title` varchar(32) NOT NULL,
  `description` varchar(200) NOT NULL,
  `src` varchar(300) NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;
"""
cursor.execute(CustomSql)
```

## POST请求要加上methods才能够被读取：

```python
@admin_bp.route('/banners/action/change/<id>/<mod>', methods=['POST', 'GET'])
def banners_change(id,mod):
    return Change_Banners(id,mod)
```

## 重新定向的时候开头的斜杠也要写：

```py
redirect('/admin/custom')
```

## 保存文件的文档相对位置开头不用写斜杠：

```python
file.save(f"static/{FileName}")
```

设置cookie过期时间防止页面卡在cookie设置的地方

## flask加载网页时css美化效果加载不出来的解决方法

在主项目根目录文件夹下面创建一个“static”文件夹存放图片、css、js等文件，此时我将美化主页面的login.css文件存在“static”文件夹下面的“css”文件夹里

flask响应后进入的主页面文件login.html存放在“templates”文件夹下public文件夹中
使用url_for来定位文件样式位置：

```html
 <link rel="stylesheet" type="text/css" href= "{{ url_for('static', filename = 'css/login.css') }}">
```

然后在路由的py文件中包含url_for包，同时使用render_template返回html模板

```python
    @app.route('/interface/<filename>')
    def OtherFile(filename):
        return render_template(f"public/{filename}")
```

## 处理跨域请求

在 Flask 中，您可以使用 `flask_cors` 扩展来配置跨域资源共享（CORS）设置，以允许跨域请求。以下是一个使用 `flask_cors` 允许跨域请求的示例：

1. 首先，确保已经在您的 Flask 项目中安装了 `flask_cors` 扩展：

```cmd
pip install flask_cors
```

2. 在您的 Flask 应用程序中导入并初始化 `CORS` 扩展：

```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
```

在上面的示例中，我们导入了 `Flask` 和 `CORS`，然后通过传递 `app` 实例来初始化 `CORS` 扩展。这将为您的应用程序自动配置一组默认的 CORS 头部，以允许跨域请求。

3. 在需要启用 CORS 的路由或视图函数上使用 `@cross_origin()` 装饰器：

```python
from flask import jsonify
from flask_cors import cross_origin

@app.route("/admin/register", methods=["POST"])
@cross_origin()
def register():
    # 处理注册逻辑...
    return jsonify(message="注册成功")
```

在上面的示例中，我们在 `/admin/register` 路由上使用了 `@cross_origin()` 装饰器。这将为该路由启用 CORS，以允许来自任何源的跨域请求访问该路由。

您可以根据需要配置 `@cross_origin()` 装饰器的参数，如 `origins`、`methods`、`headers` 等，以更细粒度地控制跨域请求的配置。例如：

```python
@cross_origin(origins=["http://localhost:5173"], methods=["POST", "OPTIONS"], headers=["Content-Type"])
```

在上述示例中，我们限制了只允许来自 `http://localhost:5173` 源的请求进行跨域访问，并指定了允许的请求方法和头部。

请注意，在实际生产环境中，根据安全性和可信任性的考虑，您应该根据需要进行相应的配置，并限制允许的请求源、方法和头部。

使用 `flask_cors` 扩展可以方便地为您的 Flask 应用程序启用和配置 CORS 设置，以便处理跨域请求。

## 接收后端发来的请求

在 Flask 中，要接收通过 POST 请求发送的数据，您可以使用 `request.form` 或 `request.json` 来访问请求的表单数据或 JSON 数据。

以下是一个在 Flask 中接收数据的示例代码：

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/admin/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    repassword = request.form.get("repassword")

    # 处理注册逻辑...

    return jsonify(message="注册成功")

if __name__ == "__main__":
    app.run()
```

在上述示例中，我们使用 `request.form.get()` 来获取通过 POST 请求发送的表单数据。`request.form.get("参数名")` 方法可以访问请求中指定参数的值。

如果您发送的是 JSON 数据，您可以改用 `request.json.get()` 方法来获取 JSON 数据中的值。示例如下：

```python
@app.route("/admin/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    repassword = data.get("repassword")

    # 处理注册逻辑...

    return jsonify(message="注册成功")
```

在上述示例中，我们首先使用 `request.json` 来访问整个 JSON 数据对象，然后使用 `data.get("参数名")` 来获取指定参数的值。

请根据您发送请求的方式（表单数据或 JSON 数据）选择使用适当的方式来接收数据，并进行相应的处理。

