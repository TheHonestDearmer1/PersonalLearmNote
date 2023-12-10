# LocalStorage

在本文中，您将了解 LocalStorage 在 JavaScript 中的理论和实际应用。

网络存储
----

Web 存储是 HTML5 的重要功能之一，它允许 Web 应用程序在用户浏览器中本地存储数据。 两种最常见的 Web 存储形式是 LocalStorage 和 Session Storage。这两种形式的网络存储之间的主要区别在于，保存在其中的数据`LocalStorage`永远不会离开浏览器，并且会一直保留在那里，直到您明确将其删除。相反，`Session Storage`一旦浏览器选项卡/窗口关闭，存储在其中的数据就会被删除。

什么是本地存储？
--------

LocalStorage 是浏览器提供的一种 Web 存储形式，它允许 Web 应用程序将数据本地存储在用户的浏览器中，并且没有过期日期。在这里，即使您关闭浏览器选项卡/窗口，存储的数据也将保持可用。

请注意，存储在 LocalStorage 中的数据仅保留在用户用于访问站点的设备上的浏览器中。因此，如果用户稍后使用不同的浏览器或在另一台设备上重新访问同一站点，他们将无法访问存储的数据。

本地存储用例
------

下面介绍一些 LocalStorage 的日常使用案例。

### 1\. 存储部分提交的表单数据

如果用户在线填写长表单，LocalStorage 可以成为存储用户输入的有用资源。在这种情况下，即使互联网在填写表单和提交表单之间断开连接，用户也不会丢失他们的输入，并且可以从他们离开的地方继续。

### 2.缓存

缓存是指在用户设备上存储诸如登录详细信息之类的数据，以便可以更快地处理未来对该数据的请求。您可以使用 LocalStorage 缓存整个网站，以便用户即使在离线时仍然可以访问该网站。

### 3\. 基础应用数据库

如前所述，数据存储最初只能通过后端与数据库通信来实现。但是现在，使用 LocalStorage，您可以在前端存储数据而无需数据库。因此 LocalStorage 有时可以作为基本应用程序的“小”数据库。

如何访问本地存储
--------

访问 LocalStorage 非常简单，只需几个步骤：

1.  转到任何网站或 Web 应用程序，然后按`F12`键盘打开浏览器控制台。
2.  接下来，单击**应用程序**选项卡，在左侧菜单中，您将`LocalStorage`在**存储**选项卡下看到如下所示。

[![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a890015dbe5e463092329f6f03c9ec99~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)](https://link.juejin.cn?target=https%3A%2F%2Fres.cloudinary.com%2Fpracticaldev%2Fimage%2Ffetch%2Fs--uXktZ8tl--%2Fc_limit%252Cf_auto%252Cfl_progressive%252Cq_auto%252Cw_880%2Fhttps%3A%2F%2Fi.imgur.com%2FxBVUgMh.png "https://res.cloudinary.com/practicaldev/image/fetch/s--uXktZ8tl--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/xBVUgMh.png")

1.  单击`LocalStorage`下拉菜单并进一步单击一个/下拉项目。![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b624fd26d3de49daa7ca5508587d3116~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

可以看出，有两列`key`， 和`value`。这是 LocalStorage 存储您保存到其中的所有数据的地方。

如何使用本地存储
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

您可以使用以下方法来管理 LocalStorage 中的数据。

| 方法 | 描述 |
| --- | --- |
| `setItem()` | 将数据存储在 LocalStorage 中。 |
| `getItem()` | 从 LocalStorage 获取或检索数据 |
| `removeItem()` | 使用密钥从 LocalStorage 中删除数据 |
| `key()` | 从指定索引处的 LocalStorage 检索数据 |

### setItem（）

此方法用于将数据存储在 LocalStorage 中。它接受一个键作为它的第一个参数，然后一个值作为第二个参数。

让我们`LocalStorage`使用以下内容添加数据。

perl

复制代码

``localStorage.setItem("name", "Mandy"); // `name`是键，`Mandy`是值``

前面提到过，LocalStorage 将数据存储为字符串，所以如果要保存对象和数组等数据，需要使用`JSON.stringify()`方法将它们转换为字符串。

让我们看看这是如何工作的！

```js
const user = {
  name: "小明",
  age: 23,
};

localStorage.setItem("user-info", JSON.stringify(user));
const names = ["小明", "小张", "小王"];
localStorage.setItem("names", JSON.stringify(names));
```

### getItem()

使用`getItem()`方法从 LocalStorage 中检索数据。此方法接受单个参数，`key`用于保存数据。

例如，要检索上述`user`对象等数据，您将使用以下语句：

`localStorage.getItem("user-info");`

上面的代码将返回一个`JSON`字符串，如下所示：

`"{name:"小明", age:"23"}"`

然后，您应该使用该`JSON.parse()`方法将其转换为对象。

`JSON.parse(localStorage.getItem('user-info'));`

### removeItem()

使用`removeItem()`方法从 LocalStorage 中删除数据。此方法接受 a`key`作为参数。

例如，您将使用以下语句`user`从 LocalStorage 中删除对象。

`localStorage.removeItem("user-info");`

### key()

使用`key(index)`方法从 LocalStorage 中检索数据，其中`index`表示`nth`要检索的数据。

`localStorage.key(2);`

### clear（）

使用该`clear()`方法清除或删除特定实例的 LocalStorage 中的所有数据。

`localStorage.clear()`  

项目
---

现在您已经了解了用于管理 LocalStorage 中数据的主要方法，让我们通过创建一个用户可以的 Web 应用程序来动手：

*   将数据保存到 LocalStorage
*   检索数据
*   使用删除/删除数据`key`
*   并清除 LocalStorage 中的所有数据。

让我们首先创建一个新文件夹并在代码编辑器中打开它。接下来，创建两个文件`index.html`，main.js\`。

### 进行编写吧

该`index.html`文件将包含 Web 应用程序的 HTML 标记。HTML 代码包含一个表单，该表单具有带有按钮的各种输入字段。

html

复制代码

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>Local Storage</title>
</head>

<body>
    <div id="form">
        <form id="userForm">
            <h1>LocalStorage</h1>
            <label for="userName">用户名</label>
            <input type="text" id="userName" placeholder="请输入用户名" required autofocus /><br />
            <label for="age">年龄</label>
            <input type="number" id="age" placeholder="请输入年龄" required /><br />
            <label for="key">Key</label>
            <input type="text" id="key" placeholder="请输入Key" required /><br />
            <button type="submit">保存用户</button>
        </form>
        <br />
        <label for="key">查找</label>
        <input type="text" id="retrieveKey" placeholder="请输入Key来查找密钥" required /><br />
        <button id="retrieveButton">查找用户</button>
        <br />
        <div id="userData"></div>
        <br />
        <label for="removeKey">删除</label>
        <input type="text" id="removeKey" placeholder="removeKey" required /><br />
        <button id="removeButton">删除用户</button>
        <br />
        <button id="clearButton">删除所有用户</button>
    </div>
</body>
<script type="text/javascript" src="main.js"></script>

</html>

```

这是`main.js`包含从 LocalStorage 存储、查找和删除数据的所有函数的文件。

JavaScript

```js
function store() {
  var userName = document.getElementById("userName").value;
  var age = document.getElementById("age").value;
  var key = document.getElementById("key").value;

  const user = {
    userName,
    age,
  };
  
  localStorage.setItem(key, JSON.stringify(user));
}

function retrieveUserData() {
  let key = document.getElementById("retrieveKey").value;
  console.log("retrive records");
  let userData = localStorage.getItem(key); //searches for the key in localStorage
  let paragraph = document.createElement("p");
  let info = document.createTextNode(userData);
  paragraph.appendChild(info);
  let element = document.getElementById("userData");
  element.appendChild(paragraph);
  retrieveKey.value = "";
}

function removeUserData() {
  var removeKey = document.getElementById("removeKey").value;
  localStorage.removeItem(removeKey);
  removeKey.value = "";
}

function deleteAllUserData() {
  localStorage.clear();
}

window.onload = function () {
  document.getElementById("userForm").onsubmit = store;
  document.getElementById("clearButton").onclick = deleteAllUserData;
  document.getElementById("removeButton").onclick = removeUserData;
  document.getElementById("retrieveButton").onclick = retrieveUserData;
};

```

结论
--

*   本地存储没有数据保护,因此存储敏感数据并不安全,因为任何人都可以访问它们。
*   本地存储最多只能在浏览器上存储 5MB 的数据。

本文转自 <https://juejin.cn/post/7149380173027573767>，如有侵权，请联系删除。

# Window sessionStorage 属性

[![JavaScript 存储对象](img/up.gif) JavaScript 存储对象](https://www.runoob.com/jsref/obj-storage.html)

## 实例

使用 sessionStorage 创建一个本地存储的 name/value 对，name="lastname" value="Smith", 然后检索 "lastname" 的值，并插入到 id="result" 的元素上:

```
// 存储
sessionStorage.setItem("lastname", "Smith");
// 检索
document.getElementById("result").innerHTML = sessionStorage.getItem("lastname");
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjsref_win_sessionstorage)

------

## 定义和使用

localStorage 和 sessionStorage 属性允许在浏览器中存储 key/value 对的数据。

sessionStorage 用于临时保存同一窗口(或标签页)的数据，在关闭窗口或标签页之后将会删除这些数据。

**提示:** 如果你想在浏览器窗口关闭后还保留数据，可以使用 [localStorage](https://www.runoob.com/jsref/prop-win-localstorage.html) 属性， 该数据对象没有过期时间，今天、下周、明年都能用，除非你手动去删除。

------

## 浏览器支持

表格中的数字表示支持该属性的第一个浏览器版本号。

| 属性           |      |      |      |      |      |
| :------------- | ---- | ---- | ---- | ---- | ---- |
| sessionStorage | 4.0  | 8.0  | 3.5  | 4.0  | 11.5 |

------

## 语法

```js
window.sessionStorage
```

保存数据语法：

```js
sessionStorage.setItem("key", "value");
```

读取数据语法：

```js
var lastname = sessionStorage.getItem("key");
```

删除指定键的数据语法：

```js
sessionStorage.removeItem("key");
```

删除所有数据：

```js
sessionStorage.clear();
```

------

## 技术细节

| 返回值: | 一个存储对象 |
| ------- | ------------ |
|         |              |

------

## 更多实例

## 实例

以下实例用于记录点击按钮的次数:

```js
if (sessionStorage.clickcount) {
    sessionStorage.clickcount = Number(sessionStorage.clickcount) + 1;
} else {
    sessionStorage.clickcount = 1;
}
document.getElementById("result").innerHTML = "你在按钮上已经点击了 " +
sessionStorage.clickcount + " 次。";
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjsref_win_sessionstorage2)