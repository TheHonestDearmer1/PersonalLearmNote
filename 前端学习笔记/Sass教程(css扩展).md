# Sass 教程

![](img/sass.png)



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

# Sass @mixin 与 @include

@mixin 指令允许我们定义一个可以在整个样式表中重复使用的样式。

@include 指令可以将混入（mixin）引入到文档中。

------

## 定义一个混入

混入(mixin)通过 @mixin 指令来定义。 @mixin name { property: value; property: value; ... }

以下实例创建一个名为 "important-text" 的混入：

## Sass 代码：

```scss
@mixin important-text {
 color: red;
 font-size: 25px;
 font-weight: bold;
 border: 1px solid blue;
}
```

**注意：**Sass 的连接符号 - 与下划线符号 _ 是相同的，也就是 @mixin important-text { } 与 @mixin important_text { } 是一样的混入。

### 使用混入

@include 指令可用于包含一混入：

## Sass @include 混入语法：

```scss
selector {
 @include mixin-name;
}
```

因此，包含 important-text 混入代码如下：

## 实例

```scss
.danger {
 @include important-text;
 background-color: green;
}
```

将以上代码转换为 CSS 代码，如下所示：

## Css 代码：

```scss
.danger {
 color: red;
 font-size: 25px;
 font-weight: bold;
 border: 1px solid blue;
 background-color: green;
}
```

混入中也可以包含混入，如下所示：

## 实例

```scss
@mixin special-text {
 @include important-text;
 @include link;
 @include special-**border**;
}
```



------

## 向混入传递变量

混入可以接收参数。

我们可以向混入传递变量。

定义可以接收参数的混入：

## 实例

```scss
/* 混入接收两个参数 */
@mixin bordered($color, $width) {
 border: $width solid $color;
}

.myArticle {
 @include bordered(blue, 1px); // 调用混入，并传递两个参数*
}

.myNotes {
 @include bordered(red, 2px); // 调用混入，并传递两个参数*
}
```

以上实例的混入参数为设置边框的属性 (color 和 width) 。

将以上代码转换为 CSS 代码，如下所示：

## Css 代码：

```scss
.myArticle {
 border: 1px solid blue;
}

.myNotes {
 border: 2px solid red;
}
```

混入的参数也可以定义默认值，语法格式如下：

## 实例

```scss
@mixin bordered($color: blue, $width: 1px) {
 border: $width solid $color;
}
```

在包含混入时，你只需要传递需要的变量名及其值：

## 实例

```scss
@mixin sexy-**border**($color, $width: 1in) {
 border: {
  color: $color;
  width: $width;
  style: dashed;
 }
}
p { @include sexy-**border**(blue); }
h1 { @include sexy-**border**(blue, 2in); }
```

将以上代码转换为 CSS 代码，如下所示：

## Css 代码：

```scss
p {
 border-color: blue;
 border-width: 1in;
 border-style: dashed; }

h1 {
 border-color: blue;
 border-width: 2in;
 border-style: dashed;
}
```



### 可变参数

有时，不能确定一个混入（mixin）或者一个函数（function）使用多少个参数，这时我们就可以使用 **...** 来设置可变参数。

例如，用于创建盒子阴影（box-shadow）的一个混入（mixin）可以采取任何数量的 box-shadow 作为参数。

## 实例

```scss
@mixin box-shadow($shadows...) {
   -moz-box-shadow: $shadows;
   -webkit-box-shadow: $shadows;
   box-shadow: $shadows;
}

.shadows {
 @include box-shadow(0px 4px 5px #666, 2px 6px 10px #999);
}
```

将以上代码转换为 CSS 代码，如下所示：

## Css 代码：

```scss
.shadows {
 -moz-box-shadow: 0px 4px 5px #666, 2px 6px 10px #999;
 -webkit-box-shadow: 0px 4px 5px #666, 2px 6px 10px #999;
 box-shadow: 0px 4px 5px #666, 2px 6px 10px #999;
}
```



------

## 浏览器前缀使用混入

浏览器前缀使用混入也是非常方便的，如下实例：

## 实例

```scss
@mixin transform($property) {
 -webkit-transform: $property;
 -ms-transform: $property;
 transform: $property;
}

.myBox {
 @include transform(rotate(20deg));
}
```

将以上代码转换为 CSS 代码，如下所示：

## Css 代码：

```scss
.myBox {
 -webkit-transform: rotate(20deg);
 -ms-transform: rotate(20deg);
 transform: rotate(20deg);
}
```

# Sass @extend 与 继承

@extend 指令告诉 Sass 一个选择器的样式从另一选择器继承。

如果一个样式与另外一个样式几乎相同，只有少量的区别，则使用 @extend 就显得很有用。

以下 Sass 实例中，我们创建了一个基本的按钮样式 .button-basic，接着我们定义了两个按钮样式 .button-report 与 .button-submit，它们都继承了 .button-basic ，它们主要区别在于背景颜色与字体颜色，其他的样式都是一样的。

## Sass 代码：

```scss
.button-basic  {
 border: none;
 padding: 15px 30px;
 text-align: center;
 font-size: 16px;
 cursor: pointer;
}

.button-report  {
 @extend .button-basic;
 background-color: red;
}

.button-submit  {
 @extend .button-basic;
 background-color: green;
 color: white;
}
```

将以上代码转换为 CSS 代码，如下所示：

## Css 代码：

```scss
.button-basic, .button-report, .button-submit {
 border: none;
 padding: 15px 30px;
 text-align: center;
 font-size: 16px;
 cursor: pointer;
}

.button-report {
 background-color: red;
}

.button-submit {
 background-color: green;
 color: white;
}
```

使用 @extend 后，我们在 HTML 按钮标签中就不需要指定多个类 class="button-basic button-report" ，只需要设置 class="button-report" 类就好了。

@extend 很好的体现了代码的复用。

# Sass String(字符串) 函数

[![](img/up.gif) Sass 函数](https://www.runoob.com/sass/sass-functions.html)

Sass String(字符串) 函数用于处理字符串并获取相关信息。

Sass 字符串的起始索引值从 1 开始，记住不是 0。

下表列出了 Sass 的字符串函数：

| 函数                                    | 描述 & 实例                                                  |
| :-------------------------------------- | :----------------------------------------------------------- |
| quote(*string*)                         | 给字符串添加引号。  **实例:** quote(runoob) 结果: "runoob"   |
| str-index(*string*, *substring*)        | 返回 substring 子字符串第一次在 string 中出现的位置。如果没有匹配到子字符串，则返回 null。  `str-index(abcd, a)  => 1 str-index(abcd, ab) => 1 str-index(abcd, X)  => null str-index(abcd, c)  => 3` |
| str-insert(*string*, *insert*, *index*) | 在字符串 string 中 index 位置插入 insert。  **实例:** str-insert("Hello world!", " runoob", 6) 结果: "Hello runoob world!" |
| str-length(*string*)                    | 返回字符串的长度。  **实例:** str-length("runoob") 结果: 6   |
| str-slice(*string*, *start*, *end*)     | 从 string 中截取子字符串，通过 start-at 和 end-at 设置始末位置，未指定结束索引值则默认截取到字符串末尾。  `str-slice("abcd", 2, 3)   => "bc" str-slice("abcd", 2)      => "bcd" str-slice("abcd", -3, -2) => "bc" str-slice("abcd", 2, -2)  => "bc"` |
| to-lower-case(*string*)                 | 将字符串转成小写  **实例:** to-lower-case("RUNOOB") 结果: "runoob" |
| to-upper-case(*string*)                 | 将字符串转成大写  **实例:** to-upper-case("runoob") 结果: "RUNOOB" |
| unique-id()                             | 返回一个无引号的随机字符串作为 id。不过也只能保证在单次的 Sass 编译中确保这个 id 的唯一性。  **实例:** unique-id() Result: uad053b1c |
| unquote(*string*)                       | 移除字符串的引号  **实例:** unquote("runoob") 结果: runoob   |

# Sass 数字函数

[![](img/up-16981418525203.gif) Sass 函数](https://www.runoob.com/sass/sass-functions.html)

Sass 数字函数用于处理一些数值。

下表列出了 Sass 的数字函数：

| 函数                       | 描述 & 实例                                                  |
| :------------------------- | :----------------------------------------------------------- |
| abs(*number*)              | 返回一个数值的绝对值。  **实例:** abs(15) 结果: 15 abs(-15) 结果: 15 |
| ceil(*number*)             | 向上取整  **实例:** ceil(15.20) 结果: 16                     |
| comparable(*num1*, *num2*) | 返回一个布尔值，判断 *num1* 与 *num2* 是否可以进行比较  **实例:** comparable(15px, 10px) 结果: true comparable(20mm, 1cm) 结果: true comparable(35px, 2em) 结果: false |
| floor(*number*)            | 向下取整  **实例:** floor(15.80) 结果: 15                    |
| max(*number...*)           | 返回最大值  **实例:** max(5, 7, 9, 0, -3, -7) 结果: 9        |
| min(*number...*)           | 返回最小值  **实例:** min(5, 7, 9, 0, -3, -7) 结果: -7       |
| percentage(*number*)       | 将数字转化为百分比的表达形式。  **实例:** percentage(1.2) 结果: 120 |
| random()                   | 返回 0-1 区间内的小数，  **实例:** random() 结果: 0.45673    |
| random(*number*)           | 返回 1 至 number 之间的整数，包括 1 和 limit。  **实例:** random(6) 结果: 4 |
| round(*number*)            | 返回最接近该数的一个整数，四舍五入。  **实例:** round(15.20) 结果: 15 round(15.80) 结果: 16 |

# Sass 列表(List)函数

[![](img/up-16981418717436.gif) Sass 函数](https://www.runoob.com/sass/sass-functions.html)

Sass 列表(List)函数用于处理列表，可以访问列表中的值，向列表添加元素，合并列表等。

Sass 列表是不可变的，因此在处理列表时，返回的是一个新的列表，而不是在原有的列表上进行修改。

列表的起始索引值为 1，记住不是 0。

下表列出了 Sass 的列表函数：

| 函数                                             | 描述 & 实例                                                  |
| :----------------------------------------------- | :----------------------------------------------------------- |
| append(*list*, *value*, [*separator*])           | 将单个值 *value* 添加到列表尾部。*separator* 是分隔符，默认会自动侦测，或者指定为逗号或空格。  **实例: **append((a b c), d) 结果: a b c d append((a b c), (d), comma) 结果: a, b, c, d |
| index(*list*, *value*)                           | 返回元素 *value* 在列表中的索引位置。  **实例:** index(a b c, b) 结果: 2 index(a b c, f) 结果: null |
| is-bracketed(*list*)                             | 判断列表中是否有中括号  **实例:** is-bracketed([a b c]) 结果: true is-bracketed(a b c) 结果: false |
| join(*list1*, *list2*, [*separator, bracketed*]) | 合并两列表，将列表 *list2* 添加到列表 *list1* 的末尾。*separator* 是分隔符，默认会自动侦测，或者指定为逗号或空格。 *bracketed* 默认会自动侦测是否有中括号，可以设置为 true 或 false。  **实例:** join(a b c, d e f) 结果: a b c d e f join((a b c), (d e f), comma) 结果: a, b, c, d, e, f join(a b c, d e f, $bracketed: true) 结果: [a b c d e f] |
| length(*list*)                                   | 返回列表的长度  **实例:** length(a b c) 结果: 3              |
| list-separator(*list*)                           | 返回一列表的分隔符类型。可以是空格或逗号。  **实例:** list-separator(a b c) 结果: "space" list-separator(a, b, c) 结果: "comma" |
| nth(*list*, *n*)                                 | 获取第 *n* 项的值。  **实例:** nth(a b c, 3) 结果: c         |
| set-nth(*list*, *n*, *value*)                    | 设置列表第 *n* 项的值为 *value*。  **实例:** set-nth(a b c, 2, x) 结果: a x c |
| zip(*lists*)                                     | 将多个列表按照以相同索引值为一组，重新组成一个新的多维度列表。  **实例:** zip(1px 2px 3px, solid dashed dotted, red green blue) 结果: 1px solid red, 2px dashed green, 3px dotted blue |

# Sass Map(映射)函数

[![](img/up-16981418874089.gif) Sass 函数](https://www.runoob.com/sass/sass-functions.html)

Sass Map(映射)对象是以一对或多对的 key/value 来表示。

Sass Map 是不可变的，因此在处理 Map 对象时，返回的是一个新的 Map 对象，而不是在原有的 Map 对象上进行修改。

下表列出了 Sass 的 Map 函数：

| 函数                         | 描述 & 实例                                                  |
| :--------------------------- | :----------------------------------------------------------- |
| map-get(*map*, *key*)        | 返回 Map 中 *key* 所对应的 value(值)。如没有对应的 key，则返回 null 值。  **实例:** $font-sizes: ("small": 12px, "normal": 18px, "large": 24px) map-get($font-sizes, "small") 结果: 12px |
| map-has-key(*map*, *key*)    | 判断 *map* 是否有对应的 *key*，存在返回 true，否则返回 false。  **实例:** $font-sizes: ("small": 12px, "normal": 18px, "large": 24px) map-has-key($font-sizes, "big") 结果: false |
| map-keys(*map*)              | 返回 *map* 中所有的 key 组成的队列。  **实例:** $font-sizes: ("small": 12px, "normal": 18px, "large": 24px) map-keys($font-sizes) 结果: "small", "normal, "large" |
| map-merge(*map1*, *map2*)    | 合并两个 map 形成一个新的 map 类型，即将 *map2* 添加到 *map1*的尾部  **实例:** $font-sizes: ("small": 12px, "normal": 18px, "large": 24px) $font-sizes2: ("x-large": 30px, "xx-large": 36px) map-merge($font-sizes, $font-sizes2) 结果: "small": 12px, "normal": 18px, "large": 24px, "x-large": 30px, "xx-large": 36px |
| map-remove(*map*, *keys...*) | 移除 *map* 中的 keys，多个 key 使用逗号隔开。  **实例:** $font-sizes: ("small": 12px, "normal": 18px, "large": 24px) map-remove($font-sizes, "small") 结果: ("normal": 18px, "large": 24px) map-remove($font-sizes, "small", "large") 结果: ("normal": 18px) |
| map-values(*map*)            | 返回 *map* 中所有的 value 并生成一个队列。  **实例:** $font-sizes: ("small": 12px, "normal": 18px, "large": 24px) map-values($font-sizes) 结果: 12px, 18px, 24px |

# Sass 选择器函数

[![](img/up-169814190372912.gif) Sass 函数](https://www.runoob.com/sass/sass-functions.html)

Sass 选择器函数用于查看与处理选择器。

下表列出了 Sass 的 选择器函数：

| 函数                                                    | 描述 & 实例                                                  |
| :------------------------------------------------------ | :----------------------------------------------------------- |
| is-superselector(*super*, *sub*)                        | 比较两个选择器匹配的范围，即判断 *super* 选择器是否包含了 *sub* 选择器所匹配的范围，是的话返回 true，否则返回 false。  **实例:** is-superselector("div", "div.myInput") 结果: true is-superselector("div.myInput", "div") 结果: false is-superselector("div", "div") 结果: true |
| selector-append(*selectors*)                            | 将第二个 (也可以有多个) 添加到第一个选择器的后面。 selector.  **实例:** selector-append("div", ".myInput") 结果: div.myInput selector-append(".warning", "__a") 结果: .warning__a |
| selector-extend(*selector*, *extendee*, *extender*)     |                                                              |
| selector-nest(*selectors*)                              | 返回一个新的选择器，该选择器通过提供的列表选择器生成一个嵌套的列表。  **实例:** selector-nest("ul", "li") 结果: ul li selector-nest(".warning", "alert", "div") 结果: .warning div, alert div |
| selector-parse(*selector*)                              | 将字符串的选择符 *selector* 转换成选择器队列。  **实例: **selector-parse("h1 .myInput .warning") 结果: ('h1' '.myInput' '.warning') |
| selector-replace(*selector*, *original*, *replacement*) | 给定一个选择器，用replacement 替换 original 后返回一个新的选择器队列。  **实例:** selector-replace("p.warning", "p", "div") 结果: div.warning |
| selector-unify(*selector1*, *selector2*)                | 将两组选择器合成一个复合选择器。如两个选择器无法合成，则返回 null 值。  **实例:** selector-unify("myInput", ".disabled") 结果: myInput.disabled selector-unify("p", "h1") 结果: null |
| simple-selectors(*selectors*)                           | 将合成选择器拆为单个选择器。  **实例:** simple-selectors("div.myInput") 结果: div, .myInput simple-selectors("div.myInput:before") 结果: div, .myInput, :before |

# Sass Introspection 函数

[![](img/up-169814193810615.gif) Sass 函数](https://www.runoob.com/sass/sass-functions.html)

Sass Introspection 函数比较少用于构建样式表，一般用于代码的调试上。

下表列出了 Sass 的 Introspection 函数：

| 函数                                     | 描述 & 实例                                                  |
| :--------------------------------------- | :----------------------------------------------------------- |
| call(*function*, *arguments*...)         | 函数的动态调用，即调用函数 function 参数为 arguments，并返回结果。 |
| content-exists()                         | 查看当前的混入是否传递 @content 块。                         |
| feature-exists(*feature*)                | 检查当前的 Sass 实现是否支持该特性。  **实例:** feature-exists("at-error"); 结果: true |
| function-exists(*functionname*)          | 检测指定的函数是否存在  **实例:** function-exists("nonsense") 结果: false |
| get-function(*functionname*, css: false) | 返回指定函数。如果 css 为 true，则返回纯 CSS 函数。          |
| global-variable-exists(*variablename*)   | 检测某个全局变量是否定义。  **实例:** variable-exists(a) 结果: true |
| inspect(*value*)                         | 返回一个字符串的表示形式，value 是一个 sass 表达式。         |
| mixin-exists(*mixinname*)                | 检测指定混入 (mixinname) 是否存在。  **实例:** mixin-exists("important-text") 结果: true |
| type-of(*value*)                         | 返回值类型。返回值可以是 number, string, color, list, map, bool, null, function, arglist。  **实例:** type-of(15px) 结果: number type-of(#ff0000) 结果: color |
| unit(*number*)                           | 返回传入数字的单位（或复合单位）。  **实例:** unit(15px) 结果: px |
| unitless(*number*)                       | 返回一个布尔值，判断传入的数字是否带有单位。  **实例:** unitless(15px) 结果: false unitless(15) 结果: true |
| variable-exists(*variablename*)          | 判断变量是否在当前的作用域下。  **实例:** variable-exists(b) 结果: true |

# Sass 颜色函数

[![](img/up-169814195817718.gif) Sass 函数](https://www.runoob.com/sass/sass-functions.html)

Sass 颜色函数可以分为三个部分：颜色设置、颜色获取以及颜色操作。

下表列出了 Sass 的颜色函数：

### Sass 颜色设置

| 函数                                            | 描述 & 实例                                                  |
| :---------------------------------------------- | :----------------------------------------------------------- |
| rgb(*red*, *green*, *blue*)                     | 创建一个 Red-Green-Blue (RGB) 色。其中 R 是 "red" 表示红色，而 G 是 "green" 绿色，B 是 "blue" 蓝色。  **实例:** rgb(0, 0, 255); |
| rgba(*red*, *green*, *blue*, *alpha*)           | 根据红、绿、蓝和透明度值创建一个颜色。  **实例:** rgba(0, 0, 255, 0.3); |
| hsl(*hue*, *saturation*, *lightness*)           | 通过色相（hue）、饱和度(saturation)和亮度（lightness）的值创建一个颜色。  **实例:** hsl(120, 100%, 50%); // 绿色 hsl(120, 100%, 75%); // 浅绿色 hsl(120, 100%, 25%); // dark green hsl(120, 60%, 70%); // 柔和的绿色 |
| hsla(*hue*, *saturation*, *lightness*, *alpha*) | 通过色相（hue）、饱和度(saturation)、亮度（lightness）和透明（alpha）的值创建一个颜色。  **实例:** hsl(120, 100%, 50%, 0.3); // 绿色带有透明度 hsl(120, 100%, 75%, 0.3); // 浅绿色带有透明度 |
| grayscale(*color*)                              | 将一个颜色变成灰色，相当于 desaturate( color,100%)。  **实例:** grayscale(#7fffd4); 结果: #c6c6c6 |
| complement(*color*)                             | 返回一个补充色，相当于adjust-hue($color,180deg)。  **实例:** complement(#7fffd4); 结果: #ff7faa |
| invert(*color*, *weight*)                       | 返回一个反相色，红、绿、蓝色值倒过来，而透明度不变。  **实例:** invert(white); 结果: black |

### Sass 颜色获取

| 函数                | 描述 & 实例                                                  |
| :------------------ | :----------------------------------------------------------- |
| red(*color*)        | 从一个颜色中获取其中红色值（0-255）。  **实例:** red(#7fffd4); 结果: 127 red(red); 结果: 255 |
| green(*color*)      | 从一个颜色中获取其中绿色值（0-255）。  **实例:** green(#7fffd4); 结果: 255 green(blue); 结果: 0 |
| blue(*color*)       | 从一个颜色中获取其中蓝色值（0-255）。  **实例:** blue(#7fffd4); 结果: 212 blue(blue); 结果: 255 |
| hue(*color*)        | 返回颜色在 HSL 色值中的角度值 (0deg - 255deg)。  **实例:** hue(#7fffd4); 结果: 160deg |
| saturation(*color*) | 获取一个颜色的饱和度值(0% - 100%)。  **实例:** saturation(#7fffd4); 结果: 100% |
| lightness(*color*)  | 获取一个颜色的亮度值(0% - 100%)。  **实例:** lightness(#7fffd4); 结果: 74.9% |
| alpha(*color*)      | Returns the alpha channel of *color* as a number between 0 and 1.  **实例:** alpha(#7fffd4); 结果: 1 |
| opacity(*color*)    | 获取颜色透明度值(0-1)。  **实例:** opacity(rgba(127, 255, 212, 0.5); 结果: 0.5 |

### Sass 颜色操作

| 函数                                                         | 描述 & 实例                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| mix(*color1*, *color2*, *weight*)                            | 把两种颜色混合起来。 *weight* 参数必须是 0% 到 100%。默认 weight 为 50%，表明新颜色各取 50% color1 和 color2 的色值相加。如果 weight 为 25%，那表明新颜色为 25% color1 和 75% color2 的色值相加。 |
| adjust-hue(*color*, *degrees*)                               | 通过改变一个颜色的色相值（-360deg - 360deg），创建一个新的颜色。  **实例:** adjust-hue(#7fffd4, 80deg); 结果: #8080ff |
| adjust-color(*color*, *red*, *green*, *blue*, *hue*, *saturation*, *lightness*, *alpha*) | 这个函数能够调整给定色彩的一个或多个属性值，包括 RGB 和 HSL 色彩的各项色值参数，另外还有 alpha 通道的取值。这些属性值的调整依赖传入的关键值参数，通过这些参数再与给定颜色相应的色彩值做加减运算。  **实例:** adjust-color(#7fffd4, blue: 25); 结果: |
| change-color(*color*, *red*, *green*, *blue*, *hue*, *saturation*, *lightness*, *alpha*) | 跟上面 adjust-color 类似，只是在该函数中传入的参数将直接替换原来的值，而不做任何的运算。  **实例:** change-color(#7fffd4, red: 255); 结果: #ffffd4 |
| scale-color(*color*, *red*, *green*, *blue*, *saturation*, *lightness*, *alpha*) | 另一种实用的颜色调节函数。adjust-color 通过传入的参数简单的与本身的色值参数做加减，有时候可能会导致累加值溢出，当然，函数会把结果控制在有效的阈值内。而 scale-color 函数则避免了这种情况，可以不必担心溢出，让参数在阈值范围内进行有效的调节。  举个例子，一个颜色的亮度 lightness 取值在 0% ~ 100% 之间，假如执行 scale-color($color, $lightness: 40%)，表明该颜色的亮度将有 (100 - 原始值) × 40% 的增幅。  另一个例子，执行 scale-color($color, $lightness: -40%)，表明这个颜色的亮度将减少 (原始值 - 0) × 40% 这么多的值。  所有传参的取值范围都在 0% ~ 100% 之间，并且 RGB 同 HSL 的传参不能冲突。  `scale-color(hsl(120, 70%, 80%), $lightness: 50%) => hsl(120, 70%, 90%) scale-color(rgb(200, 150, 170), $green: -40%, $blue: 70%) => rgb(200, 90, 229) scale-color(hsl(200, 70%, 80%), $saturation: -90%, $alpha: -30%) => hsla(200, 7%, 80%, 0.7)` |
| rgba(*color*, *alpha*)                                       | 根据红、绿、蓝和透明度值创建一个颜色。  **实例:** rgba(#7fffd4, 30%); 结果: rgba(127, 255, 212, 0.3) |
| lighten(*color*, *amount*)                                   | 通过改变颜色的亮度值（0% - 100%），让颜色变亮，创建一个新的颜色。 |
| darken(*color*, *amount*)                                    | 通过改变颜色的亮度值（0% - 100%），让颜色变暗，创建一个新的颜色。 |
| saturate(*color*, *amount*)                                  | 提高传入颜色的色彩饱和度。等同于 adjust-color( color, saturation: amount) |
| desaturate(*color*, *amount*)                                | 调低一个颜色的饱和度后产生一个新的色值。同样，饱和度的取值区间在 0% ~ 100%。等同于 adjust-color(color, saturation: -amount) |
| opacify(*color*, *amount*)                                   | 降低颜色的透明度，取值在 0-1 之。等价于 adjust-color(color, alpha: amount) |
| fade-in(*color*, *amount*)                                   | 降低颜色的透明度，取值在 0-1 之。等价于 adjust-color(color, alpha: amount) |
| transparentize(*color*, *amount*)                            | 提升颜色的透明度，取值在 0-1 之间。等价于 adjust-color(color, alpha: -amount) |
| fade-out(*color*, *amount*)                                  | 提升颜色的透明度，取值在 0-1 之间。等价于 adjust-color(color, alpha: -amount) |