# Sass 教程

![img](img/sass.png)



Sass (英文全称：Syntactically Awesome Stylesheets) 是一个最初由 Hampton Catlin 设计并由 Natalie Weizenbaum 开发的层叠样式表语言。

Sass 是一个 CSS 预处理器。

Sass 是 CSS 扩展语言，可以帮助我们减少 CSS 重复的代码，节省开发时间。

Sass 完全兼容所有版本的 CSS。

Sass 扩展了 CSS3，增加了规则、变量、混入、选择器、继承、内置函数等等特性。

Sass 生成良好格式化的 CSS 代码，易于组织和维护。

Sass 文件后缀为 **.scss**。

## Sass 实例

```scss
/* 定义变量与值 */
$bgcolor: lightblue;
$textcolor: darkblue;
$fontsize: 18px;

/* 使用变量 */
body {
 **background-color**: $bgcolor;
 **color**: $textcolor;
 **font-size**: $fontsize;
}
```



## 阅读本教程前，您需要了解的知识：

阅读本教程，您需要有以下基础：

- [HTML 教程](https://www.runoob.com/html/html-tutorial.html)
- [CSS 教程](https://www.runoob.com/css/css-tutorial.html)

------

## 为什么使用 Sass?

CSS 本身语法不够强大，导致重复编写一些代码，无法实现复用，而且在代码也不方便维护。

Sass 引入合理的样式复用机制，增加了规则、变量、混入、选择器、继承、内置函数等等特性。

我们可以举个例子，我们会在 CSS 中重复使用很多次十六进制的颜色代码，当有了变量之后，如果要改变颜色代码，只要修改变量的值就好了：

## Sass 实例

```scss
/* 定义颜色变量，要修改颜色值，修改这里就可以了 */
$primary_1: #a2b9bc;
$primary_2: #b2ad7f;
$primary_3: #878f99;

/* 使用变量 */
.main-header {
 background-color: $primary_1;
}

.menu-left {
 background-color: $primary_2;
}

.menu-right {
 background-color: $primary_3;
}
```



------

## Sass 是如何工作的？

浏览器并不支持 Sass 代码。因此，你需要使用一个 Sass 预处理器将 Sass 代码转换为 CSS 代码。

# Sass 安装

本章节我们主要介绍 Sass 的安装与使用。

### NPM 安装

我们可以使用 npm（NPM 使用介绍）来安装 Sass。

```
npm install -g sass
```

**注：**国内 npm 建议使用淘宝镜像来安装，参考：[NPM 国内慢的问题解决](https://www.runoob.com/w3cnote/npm-slow-use-cnpm.html)

### Windows 上安装

我们可以使用 Windows 的包管理器 [Chocolatey](https://chocolatey.org/) 来安装：

```
choco install sass
```

### Mac OS X (Homebrew)安装

Mac OS 可以使用 [Homebrew](https://brew.sh/) 包管理器来安装：

```
brew install sass/sass/sass
```

更多安装方法可以查看官网：https://sass-lang.com/install

------

## 使用介绍

我们的教程使用的是 npm 安装的 sass，安装完成后可以查看版本：

$ sass --version 1.22.12 compiled with dart2js 2.5.0 接下来我们创建一个 runoob-test.scss 文件，内容为：

## runoob-test.scss 文件代码:

```scss
/* 定义变量与值 */
$bgcolor: lightblue;
$textcolor: darkblue;
$fontsize: 18px;

/* 使用变量 */
body {
 background-color: $bgcolor;
 color: $textcolor;
 font-size: $fontsize;
}
```

然后在命令行输入下面命令，即将 .scss 文件转化的 css 代码：

```scss
$ sass runoob-test.scss 
@charset "UTF-8";
/* 定义变量与值 */
/* 使用变量 */
body {
  background-color: lightblue;
  color: darkblue;
  font-size: 18px;
}
```

我们可以在后面再跟一个 .css 文件名，将代码保存到文件中：

```
$ sass runoob-test.scss runoob-test.css
```

这是会在当前目录下生成 runoob-test.css 文件，代码如下：

```scss
@charset "UTF-8";
/* 定义变量与值 */
/* 使用变量 */
body {
  background-color: lightblue;
  color: darkblue;
  font-size: 18px;
}

/*# sourceMappingURL=runoob-test.css.map */
```

# Sass 变量

变量用于存储一些信息，它可以重复使用。

Sass 变量可以存储以下信息：

- 字符串
- 数字
- 颜色值
- 布尔值
- 列表
- null 值

Sass 变量使用 **$** 符号：

```
$variablename: value;
```

以下实例设置了四个变量：myFont, myColor, myFontSize, 和 myWidth。

变量声明后我们就可以在代码中使用它：

## Sass 代码：

```scss
$myFont: Helvetica, sans-serif;
$myColor: red;
$myFontSize: 18px;
$myWidth: 680px;

body {
 font-family: $myFont;
 font-size: $myFontSize;
 color: $myColor;
}

#container {
 width: $myWidth;
}
```

将以上代码转换为 CSS 代码，如下所示：

## Css 代码：

```scss
body {
 font-family: Helvetica, sans-serif;
 font-size: 18px;
 color: red;
}

#container {
 width: 680px;
}
```

------

## Sass 作用域

Sass 变量的作用域只能在当前的层级上有效果，如下所示 h1 的样式为它内部定义的 green，p 标签则是为 red。

## Sass 代码：

```scss
$myColor: red;

h1 {
 $myColor: green;  *// 只在 h1 里头有用，局部作用域*
 color: $myColor;
}

p {
 color: $myColor;
}
```

将以上代码转换为 CSS 代码，如下所示：

## Css 代码：

```scss
h1 {
 color: green;
}

p {
 color: red;
}
```

### !global

当然 Sass 中我们可以使用 **!global** 关键词来设置变量是全局的：

## Sass 代码

```scss
$myColor: red;

h1 {
 $myColor: green !global; *// 全局作用域*
 color: $myColor;
}

p {
 color: $myColor;
}
```

现在 p 标签的样式就会变成 green。

将以上代码转换为 CSS 代码，如下所示：

## Css 代码

```scss
h1 {
 color: green;
}

p {
 color: green;
}
```

**注意：**所有的全局变量我们一般定义在同一个文件，如：**_globals.scss**，然后我们使用 **[@include](https://www.runoob.com/sass/sass-mixin-include.html)** 来包含该文件。

# Sass 嵌套规则与属性

Sass 嵌套 CSS 选择器类似于 HTML 的嵌套规则。

如下我们嵌套一个导航栏的样式：

## Sass 代码：

```scss
nav {
 ul {
  margin: 0;
  padding: 0;
  list-style: none;
 }
 li {
  display: inline-block;
 }
 a {
  display: block;
  padding: 6px 12px;
  text-decoration: none;
 }
}
```

实例中，ul, li, 和 a 选择器都嵌套在 nav 选择器中

将以上代码转换为 CSS 代码，如下所示：

## Css 代码：

```scss
nav ul {
 margin: 0;
 padding: 0;
 list-style: none;
}
nav li {
 display: inline-block;
}
nav a {
 display: block;
 padding: 6px 12px;
 text-decoration: none;
}
```



------

## Sass 嵌套属性

很多 CSS 属性都有同样的前缀，例如：font-family, font-size 和 font-weight ， text-align, text-transform 和 text-overflow。

在 Sass 中，我们可以使用嵌套属性来编写它们：

## Sass 代码：

```scss
font: {
 family: Helvetica, sans-serif;
 size: 18px;
 weight: bold;
}

text: {
 align: center;
 transform: lowercase;
 overflow: hidden;
}
```

将以上代码转换为 CSS 代码，如下所示：

## Css 代码：

```scss
font-family: Helvetica, sans-serif;
font-size: 18px;
font-weight: bold;

text-align: center;
text-transform: lowercase;
text-overflow: hidden;
```

# Sass @import

Sass 可以帮助我们减少 CSS 重复的代码，节省开发时间。

我们可以安装不同的属性来创建一些代码文件，如：变量定义的文件、颜色相关的文件、字体相关的文件等。

------

## Sass 导入文件

类似 CSS，Sass 支持 **@import** 指令。

@import 指令可以让我们导入其他文件等内容。

CSS @import 指令在每次调用时，都会创建一个额外的 HTTP 请求。但，Sass @import 指令将文件包含在 CSS 中，不需要额外的 HTTP 请求。

Sass @import 指令语法如下：

```scss
@import filename;
```

**注意：**包含文件时不需要指定文件后缀，Sass 会自动添加后缀 .scss。

此外，你也可以导入 CSS 文件。

导入后我们就可以在主文件中使用导入文件等变量。

以下实例，导入 variables.scss、colors.scss 和 reset.scss 文件。

## Sass 代码：

```scss
@import "variables";
@import "colors";
@import "reset";
```

接下来我们创建一个 reset.scss 文件：

## reset.scss 文件代码：

```scss
html,
body,
ul,
ol {
 margin: 0;
 padding: 0;
}
```

然后我们在 standard.scss 文件中使用 @import 指令导入 reset.scss 文件：

## standard.scss 文件代码：

```scss
@import "reset";

body {
 font-family: Helvetica, sans-serif;
 font-size: 18px;
 color: red;
}
```

将以上代码转换为 CSS 代码，如下所示：

## Css 代码：

```scss
html, body, ul, ol {
 margin: 0;
 padding: 0;
}

body {
 font-family: Helvetica, sans-serif;
 font-size: 18px;
 color: red;
}
```



------

## Sass Partials

如果你不希望将一个 Sass 的代码文件编译到一个 CSS 文件，你可以在文件名的开头添加一个下划线。这将告诉 Sass 不要将其编译到 CSS 文件。

但是，在导入语句中我们不需要添加下划线。

Sass Partials 语法格式：

```scss
_filename;
```

以下实例创建一个 _colors.scss 的文件，但是不会编译成 _colors.css 文件：

## _colors.scss 文件代码：

```scss
$myPink: #EE82EE;
$myBlue: #4169E1;
$myGreen: #8FBC8F;
```

如果要导入该文件，则不需要使用下划线：

## 实例

```scss
@import "colors";

body {
 font-family: Helvetica, sans-serif;
 font-size: 18px;
 color: $myBlue;
}
```

**注意：**请不要将带下划线与不带下划线的同名文件放置在同一个目录下，比如，_colors.scss 和 colors.scss 不能同时存在于同一个目录下，否则带下划线的文件将会被忽略。