# CSS的选择器

## 选择器（selector）的作用

- **找出页面中的元素，以便给他们设置样式（name,id）**
- 使用多种方式去选择元素

1. **按照标签名，类名或者ID**
2. 按照属性
3. 按照DOM树中的位置
4. ![](%E5%9B%BE%E7%89%87/image-20230827112118556.png)

**在html中使用样式的多种方法：**

```html
<link rel="stylesheet" href="/assets/style.css"> <!--外链-->
<style></style> <!--嵌入-->
<p style="margin:len 0 "></p> <!--内联-->
```

## 通配选择器

*{}   *指代所有标签

p/h1....标签指定样式

## id选择器 （#）

id作为全局属性，可以给任一标签设定id来使用style直接引用id设定样式（id要唯一)

 [CodePen Embed - 青训营/CSS/ID选择器](https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fwebzhao%2Fembed%2FrNGqBBL%3Fdefault-tab%3Dhtml%2Cresult%26editable%3Dtrue%26theme-id%3D40116)

## 类选择器 （.）

给同一类型的HTML标签设定样式的时候，可以给这些同一类型设定全局属性class来方便设定这一类的统一样式（同样使用style来实现） class可以出现多次，比较常用

[CodePen Embed - 青训营/CSS/类选择器](https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fwebzhao%2Fembed%2FYzrJKyL%3Fdefault-tab%3Dhtml%2Cresult%26editable%3Dtrue%26theme-id%3D40116)

## 属性选择器

通过一些标签的属性去选择标签设定样式，例如input的disable就可以使用style的[disable]去选中标签设定样式，表示有disable这个属性就可以去选中它
[CodePen Embed - 青训营/CSS/属性选择器](https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fwebzhao%2Fembed%2FgOGBYMZ%3Fdefault-tab%3Dhtml%2Cresult%26editable%3Dtrue%26theme-id%3D40116)

```html
<style>
  [disabled] {
    background: #eee;
    color: #999;
  }
</style>
```

如果想让**选定属性是一个特定的值时**再选中进行样式显示的话，我们可以写成如下 [CodePen Embed - 青训营/CSS/属性选择器2](https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fwebzhao%2Fembed%2FjOGeNGb%3Fdefault-tab%3Dhtml%2Cresult%26editable%3Dtrue%26theme-id%3D40116)

```html
<style>
  input[type="password"] {
    border-color: red;
    color: red;
  }
</style>
```

## 选择器的优先级

CSS中可以写很多选择器，可以根据id更改内容的样式，也可以改整个标签内容的样式。当多个选择器作用在同一个元素的时候，元素样式将根据选择器特异度变化。这里特异度指的是越特殊的选择器，优先级越高。

![](%E5%9B%BE%E7%89%87/3e9f21beca5344af8238d68156024a54tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.webp)

**上图中，id、伪类、标签数量越多，特异度越高**。

举例： 利用选择器的优先级，可以很好地实现按钮复用（只需更改样式，便能区分两个相同的按钮）**简单来说就是利用优先级来进行样式覆盖**

## 继承

某些属性会自动继承其父元素的计算值，除非显式指定一个值



# 伪类（pseudo-classes）选择器 状态 结构性 

还可以不通过属性选择属性，我们通过伪类（pseudo-classes）这种去选择标签元素

- 不基于标签和属性定位元素
- 分为状态伪类和结构性伪类

## 状态伪类（不同状态不同样式）

状态型的伪类不是说具体指某个元素，这个元素还要处与某种特定的状态下，才会被选中
举例子，链接分为访问过的链接（跟非访问的颜色不一样）和非访问过的链接，鼠标选中链接（一般移到链接上面会变黄），和没有选中的不同状态都可以使用伪类进行修改样式

- a:link**默认样式**
- a:visited**访问过的样式**
- a:hover**鼠标移上去之后显示的样式**
- a:active**鼠标按下去之后的显示样式**

除了链接之外，其他标签也有多种状态，比如输入框input
默认状态，没点过、点击文字框之后可以输入文字的focus状态
:focus{outline:2px solid orange} **outline是选定边框的属性**，当被选中时，设定2像素橘色边框，值得注意是链接在按下去之后，**也是focus状态**。



## 结构性伪类（位置）

根据dom结点在dom树中出现的相对位置来决定是否选中这个标签（来改变样式）

1. 阿凡达
2. 泰坦尼克号
3. 星球大战：原力觉醒
4. 复仇者联盟 3
5. 侏罗纪世界

对于这样的有序列表来说，我们想给排名第一的列表项目加样式，其他排名就不动，这么做呢?
使用**li:first-child来选中它**，也可以用**li:last-child来选中排名最后一名的列表项目**， border-bottom:none;表示没有下边框的意思

```html
<ol>
  <li>阿凡达</li>
  <li>泰坦尼克号</li>
  <li>星球大战：原力觉醒</li>
  <li>复仇者联盟 3</li>
  <li>侏罗纪世界</li>
</ol>

<style>
li {
  list-style-position: inside;
  border-bottom: 1px solid;
  padding: 0.5em
}

li:first-child {
  color: coral
}

li:last-child {
  border-bottom: none;
}
</style>
```

# 组合

### 组合简介

快速构建页面结构和CSS样式

| 名称       | 语法  | 说明                       | 示例        |
| ---------- | ----- | -------------------------- | ----------- |
| 直接结合   | AB    | 满足A同时满足B             | input:focus |
| 后代组合   | A B   | 选中B,如果它是A的子孙      | nav a       |
| 亲子组合   | A > B | 选中B,如果它是A的子元素    | section > p |
| 兄弟选择器 | A ~ B | 选中B,如果它在A后且和A同级 | h2 ~ p      |
| 相邻选择器 | A + B | 选中B,如果它紧跟在A后面    | h2 + p      |

使用例子：
article p{}**表示article下的所有p标签**
article >p**表示article下直接的p标签**（article嵌套里面遇到的第一个p标签）
h2+p表示h2后紧跟着的p标签

### 选择器组

有些时候想同时设定多个选择器，可以用,分隔

```css
body,h1,h2,h3,h4,h5,h6,ul,ol,li{
   margin: 0;
   padding: 0;
}

[type='checkbox'],[type=radio]{ //表示选择所有类型为复选框（checkbox）和单选按钮（radio）的输入元素
    box-mizin:border-box;
    padding:0;
}
```

# 颜色

### RGB的组成

都是0即是黑色
都是255即是白色
具体怎么写颜色的值呢？rgb(红0-255,绿0-255,蓝0-255)
或者#红红绿绿蓝蓝（每个颜色都是2个16进制字符（转化成10进制还是0-255的范围），#8fac87,不区分大小写）
[CodePen - 青训营/CSS/RGB (cdpn.io)](https://link.juejin.cn/?target=https%3A%2F%2Fcdpn.io%2Fwebzhao%2Fdebug%2FbGomNLx)

### 颜色-HSL

H代表Hue（色相），色彩的基本属性，取值0-360
S代表Saturation（饱和度）,色彩的鲜艳程度，越高越鲜艳，0-100%
L代表Lightness(亮度),色彩的明亮程度，越高颜色越亮，范围0-100%
即通过Hsl来设定颜色，更加直观的可以调整hsl(Hue,Saturation,Lightness)

调整按钮颜色的话，点击变色的效果，用hsl该后面二个颜色的参数就更方便一些

还可以指定元素的名字（值），但是不常用，因为一般记不住，只能记很纯的颜色 [CodePen - 青训营/CSS/HSL (cdpn.io)](https://link.juejin.cn/?target=https%3A%2F%2Fcdpn.io%2Fwebzhao%2Fdebug%2FMWEPYMY)
[CodePen - 青训营/CSS/颜色关键字 (cdpn.io)](https://link.juejin.cn/?target=https%3A%2F%2Fcdpn.io%2Fwebzhao%2Fdebug%2FvYeVJaJ)

### 颜色-透明度

alpha(透明度)可以理解成不透明度，因为调低是透明（0透明），调高不透明（1不透明）
表现方式#ff0000ff
rgba(255,0,0,1)
hsla(0,100%,50%,1)
a可以省略实际生（新版浏览器）
[CodePen - 青训营/CSS/alpha (cdpn.io)](

# 字体

### 字体的使用 font-family

通过font-family来设置字体
[CodePen Embed - RwLeLWy](https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fwebzhao%2Fembed%2FRwLeLWy%3Fdefault-tab%3Dhtml%2Cresult%26editable%3Dtrue%26theme-id%3D40116)
为什么要设置多个字体？因为要在不同的设备上面使用，不同的设备可以有的字体是有限的，所以我们可以指定多个字体，多个字体从前到后设备有的就用，没有就往后面换
sans-serif不是具体的字体，实际上是一个通用的字体组，CSS有5种的通用的字体组

暂时不具体写，用到的时候再记录

# 属性

### font-size属性（字体大小）

[CodePen Embed - 青训营/CSS/font-size](https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fwebzhao%2Fembed%2FoNGaGoq%3Fdefault-tab%3Dhtml%2Cresult%26editable%3Dtrue%26theme-id%3D40116)

- 关键字：small,medium,large
- 长度:px,em
- 百分数：相对于父元素字体的大小

section将其中全部的字体大小设置为20像素
section h1的2em是相对的概念，即20*2=40像素的字体大小（与父元素字体大小相×）
section .note将类为note的字体大小设置为父级大小的80%

## font-style属性（字体类型）

front-style:italic（表示斜体） normal（正常)

## font-weight属性

weight属性(从100-900)字重的意思（**粗细程度）**
用来设置字体的粗细 正常normal表示400
粗体bold表示700
设置无效，可能是字体本身就没设计出这么多字重在字体库里面

## line-height(行高)

**二行文字**的**基准线之间的距离**
行高一般表示字体大小的多少倍，h1大小30,行高45，即1.5倍的行高

**前面的所有属性都可以变成一个属性(即font) 在font里面这些属性都可以写进去**：

斜体 粗细 大小/行高 字体族

```css
font: bold 14px/1.7 Helvetica,sans-serif
```

### 空格处理(white-space)

HTML对连续的多个空格会合成一个
怎么处理？

- normal吃空格，多个只显示一个空格
- nowrap强制不换行
- pre保留所有的格式
- pre-wrap一行显示不下，会自动换行，同时保留空格
- pre-line需要合并空格，但是保留换行（你怎么换就怎么显示

示例：

```css
white-space:pre
```

### 初始值

- CSS中，每个属性都有一个初始值

  background-color的初始值为transparent

  margin-left的初始值为0

- 可以使用initial关键字显式重置为初始值

  background-color：initial

### 

# CSS盒模型

CSS盒模型是CSS布局的基础，它将每个HTML元素看作是一个矩形的盒子，包含内容、内边距、边框和外边距。理解盒模型对于控制页面布局和样式非常重要。

### 盒模型示意图

下图展示了一个典型的CSS盒模型：

![](%E5%9B%BE%E7%89%87/242fa1d9532b498ebff6752076abd15btplv-k3u1fbpfcp-zoom-in-crop-mark1512000.webp)

- Content（内容区）：显示元素的实际内容，如文字、图片等。
- Padding（内边距）：位于内容区和边框之间，用于增加元素内部的空白区域。
- Border（边框）：围绕在内容区和内边距外部，显示元素的边界。
- Margin（外边距）：位于边框以外，用于控制元素与其他元素之间的间距

## 盒模型的宽度和高度计算

当设置元素的宽度和高度时，需要考虑到不同盒模型的计算方式。

## 标准盒模型

标准盒模型的宽度和高度仅包含内容区的大小，不包括内边距、边框和外边距。示例代码如下：

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <div class="box-standard"></div>

</body>
</html>
/* styles.css */
.box-standard {
  width: 200px;
  height: 100px;
  padding: 20px;
  border: 2px solid black;
  margin: 10px;
}
```

在上述示例中，元素的实际宽度计算为：200px (内容宽度) + 2 * 20px (左右内边距) + 2 * 2px (左右边框) + 2 * 10px (左右外边距) = 254px

元素的实际高度计算为：100px (内容高度) + 2 * 20px (上下内边距) + 2 * 2px (上下边框) + 2 * 10px (上下外边距) = 154px

## 布局技巧

在实际前端开发中，CSS的布局是最常用的技巧之一。以下是一些常见的CSS布局技巧：

### 居中一个元素

居中一个元素是前端开发中常见的需求。可以使用以下方法实现水平和垂直居中。

### 水平居中

可以使用`margin: 0 auto;`将元素水平居中。例如：

```css
/* styles.css */
.container {
  width: 300px;
  margin: 0 auto;
}
```

上述代码中，设置了容器的宽度为300px，并使用`margin: 0 auto;`将容器水平居中。

### 垂直居中

可以使用CSS的`flexbox`或`grid`布局来实现垂直居中。例如，使用`flexbox`布局：

```css
/* styles.css */
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 300px;
}
```

上述代码中，将容器设置为`flex`布局，通过`justify-content: center;`和`align-items: center;`将内容在容器中垂直居中。

### 响应式布局

**响应式布局**是指网页能够根据不同设备的屏幕大小和分辨率**自动调整布局**，以适应不同的屏幕。这样可以使网页在手机、平板和电脑等多种设备上都能良好地显示。

可以使用CSS的`@media`查询来设置不同的样式规则。例如，当屏幕宽度小于等于768px时，设置元素的宽度为100%：

```css
/* styles.css */
.container {
  width: 80%;
}

@media (max-width: 768px) {
  .container {
    width: 100%;
  }
}
```

上述代码中，当屏幕宽度小于等于768px时，容器的宽度将被设置为100%。

## 布局（Layout）

布局相关技术：

| 常规流  | 常规流   | 常规流   |
| ------- | -------- | -------- |
| 行级    | 块级     | 表格布局 |
| FlexBox | Grid布局 |          |

| 其他     |
| -------- |
| 浮动     |
| 绝对定位 |

![](%E5%9B%BE%E7%89%87/f9b505212de348628599c2759a8f6738tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.webp)

说明：width 指定content box**宽度**，取值为长度、百分数、auto，aotu由浏览器根据其他属性确定，百分数相对于容器的content box宽度。容器有指定的高度时，百分数才生效。

说明：padding 指定元素四个方向的**内边距**，百分数相对于容器宽度（顺时针）。 border 指定容器边框样式、粗细和颜色

margin：auto水平居中

margin collapse 外边距叠加，上下两div(上定义有margin-bottom, 下有margin-top): 叠加取较大的margin值margin在垂直方向上有边界的合并。

**文字超出部分**可以用overflow  -visible -hidden -scroll

overflow-wrap ： break-word 一个单词超出容器长度就会换行

### 行级vs块级

- **块级不和其他盒子并列摆放，适用所有的盒模型属性**
- **行级和其他盒子一起放在一行或拆开成多行，盒模型中的width、height不适用**

#### display属性

- block 块级盒子
- inline 行级盒子
- inline-block 本身是行级，可以放在行盒中；可以设置宽高；作为一个整体不会被拆散成多行
- flex 弹性盒子布局
- none 排版时完全被忽略

#### 行级排版上下文(inline)

简称IFC 只包含行级盒子的容器会创建一个IFC IFC内的排版规则：

- 盒子在一行内水平摆放
- 一行放不下会换行
- text-align决定一行盒子内的水平对齐
- vertical-align垂直对齐，会避开浮动元素

#### 块级排版上下文(block)

简称BFC BFC内的排版规则：

- 盒子从上到下摆放
- 垂直margin合并
- BFC内盒子的margin不会与外面的合并
- BFC不会和浮动元素重叠 

### FlexBox(display: flex;)

一种新的排版上下文，它可以控制子级盒子的**摆放流向**、**摆放顺序**、**盒子的宽度和高度**、水**平和垂直方向的对齐**、**是否允许折行**

#### 对齐

flex根据内容确定宽度高度，摆放从左至右

分为主轴与侧轴

![](%E5%9B%BE%E7%89%87/image-20230904082710117.png)

justify-content   主轴     justify 使齐行 

```css
justify-content: center /*方块内内容主轴居中（横向）*/
```

![](%E5%9B%BE%E7%89%87/image-20230904082848564.png)

align-items 侧轴     align 排整齐

```css
align-items: center /*方块内内容侧轴居中（竖向向）*/
```

**space-around** - 每个项目两侧的间隔相等。所以，项目之间的间隔比项目与容器边框的间隔大一倍

**space-between** - 项目与项目的间隔相等，项目与容器边框之间没有间隔

**space-evenly** - 项目与项目的间隔相等，项目与容器边框之间也是同样长度的间隔

**stretch** - 项目大小没有指定时，拉伸占据整个网格容器

### Grid布局

二维   display：grid使元素生成一个块级的Grid容器

![](%E5%9B%BE%E7%89%87/image-20230904084138674.png)

![](%E5%9B%BE%E7%89%87/image-20230904084356207.png)

- **grid-template-columns 属性设置列数和列宽**
- **grid-template-rows 属性设置行数和行高**
- **数值个数代表列或行数，数值大小代表列宽或者行高**

```css
grid-template-columns: 100px 100px 200px /*三列，列宽*/
grid-template-rows: 100px 100px /*两行，行宽*/
```

![](%E5%9B%BE%E7%89%87/image-20230904090618928.png)

使用grid-template相关属性将容器划分为网格

1、 **repeat() 函数**：可以简化重复的值，例：repeat(3,1fr) //3行或列，都设置为1fr的宽度（1fr 1fr 1fr）

2、**auto-fill 关键字**：表示自动填充，让一行（或者一列）中尽可能的容纳更多的单元格。例如：

grid-template-columns: repeat(auto-fill, 200px);

3、**fr 关键字**（比例）：Grid
grid-template-columns: 200px 1fr 2fr 表示第一个列宽设置为200px，后面剩余的宽度分为两部分，宽度分别为剩余宽度的 1/3 和 2/3。 

例如：grid-template-columns:200px 1fr 2fr;

4、**minmax() 函数**：我们有时候想给网格元素一个最小和最大的尺寸，minmax() 函数产生一个长度范围，表示长度就在这个范围之中都可以应用到网格项目中。它接受两个参数，分别为最小值和最大值。grid-template-columns: 1fr 1fr minmax(300px, 2fr) 的意思是，第三个列宽最少也是要 300px，但是最大不能大于第一第二列宽的两倍。

5、**auto 关键字**：由浏览器决定长度。通过 auto 关键字，我们可以轻易实现三列或者两列布局。grid-template-columns: 100px auto 100px 表示第一第三列为 100px，中间由浏览器决定长度

         6. **百分比**

#### 网格间距（Column Gap）

**网格间距（Column Gap）指的是两个网格单元之间的网格横向间距或网格纵向间距**

可以使用以下属性来调整间隙大小：

- grid-column-gap

- grid-row-gap

- grid-gap

  ![](%E5%9B%BE%E7%89%87/grid_gaps.png)

#### 按行列划分网格

##### **grid line网格线**（空隙）:

##### 用线的方式来指定项目的位置

**grid-column-start 属性、grid-column-end 属性、grid-row-start 属性以及grid-row-end 属性**

可以指定网格项目所在的四个边框，分别定位在哪根网格线，用线的方式来指定项目的位置：

![](%E5%9B%BE%E7%89%87/image-20230905092602036.png)

- "grid-row-start: 1;" 表示网格项的起始行为第一行线。
- "grid-column-start: 1;" 表示网格项的起始列为第一列线。
- "grid-row-end: 3;" 表示网格项的结束行为第三行线。
- "grid-column-end: 3;" 表示网格项的结束列为第三列线。
- 可以使用grid-column和grid-row简写，grid-column: 1/3  //代表1号线开始，3号线结束

[13分钟彻底弄懂CSS Grid基础布局 / CSS Grid 入门教程_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1w84y1r7X8/?spm_id_from=333.337.search-card.all.click&vd_source=a0e678f0a699f40cb533e1a6673f35fa)

使用前先在容器中指定网格数量：

```css
grid-template-columns: 100px 100px 200px /*三列，列宽*/
grid-template-row: 100px 100px /*两行，行宽*/
```

更简便的方法：
使用grid-area对每个块进行标记，再使用grid-template-area对标记的块进行排版

![](%E5%9B%BE%E7%89%87/image-20230905103823850.png)

### 浮动（float）

实现文字环绕图片效果

float:left

![](%E5%9B%BE%E7%89%87/image-20230905084400073.png)

### 绝对定位

**position属性：**

- static 默认值，非定位元素
- relative相对于原本位置偏离
- absolute找父级定位，非本身
- fixed总是相对于窗口定位

**position: relative**

- 在常规流里面布局
- 相对于自己本应该在的位置进行偏移
- 使用 top、left、bottom、right 设置偏移长度
- 流内其它元素当它没有偏移一样布局

![](%E5%9B%BE%E7%89%87/image-20230905085302482.png)

**position: absolute**

- 脱离常规流
- 相对于**最近的非 static 祖先(容器)**定位
- 不会对流内元素布局造成影响

![](%E5%9B%BE%E7%89%87/image-20230905085509238.png)

**position: fixed **（脱离常规流根据屏幕位置定位）：

```css
    position: fixed;
    top: 40%;
    left: 50%;
```

相对于屏幕固定，不会随滚动变化

![](%E5%9B%BE%E7%89%87/image-20230905090058476.png)

nav为自定义标签

![](%E5%9B%BE%E7%89%87/image-20230905091710203.png)

### CSS过渡动画

创建 CSS 过渡动画，你可以使用 CSS 的 `transition` 属性和其他相关属性来定义过渡效果。

下面是一个简单的例子，展示如何使用 CSS 过渡动画来淡入一个元素：

HTML:

```html
<div id="myElement">Hello, world!</div>
```



CSS:

```css
#myElement {
  opacity: 0; /* 设置初始透明度为 0 */
  transition: opacity 0.5s; /* 使用 transition 属性定义过渡效果 */
}

#myElement.fade-in {
  opacity: 1; /* 过渡结束时的透明度为 1 */
}
```



JavaScript:

```js
const element = document.getElementById("myElement");
element.classList.add("fade-in"); // 添加 CSS 类，触发过渡效果
```



在上述代码中，我们先为 `myElement` 元素设置了初始的透明度为 0，并定义了过渡效果。然后，通过 JavaScript，我们给元素添加了一个名为 `fade-in` 的 CSS 类，这将触发过渡效果并使元素淡入。

你可以根据需要来调整过渡的属性（如 `transition-duration`，`transition-property` 等），以及定义其他的过渡效果（如平移、旋转、缩放等），具体取决于你的设计需求。

请记住，CSS 过渡动画主要通过使用 CSS 的 `transition` 属性和添加、移除 CSS 类来实现，这样可以让浏览器自动应用过渡效果。使用 JavaScript 来操作 CSS 类可以在需要时触发过渡动画。

### label

**HTML `<label>` 元素**（标签）表示用户界面中某个元素的说明。

[ - HTML（超文本标记语言） | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/label)

![](%E5%9B%BE%E7%89%87/image-20230911120626107.png)

当你点击label中的文本的时候，就相当于点击for中绑定的imput

# `<body>` 占满整个屏幕空间

要让 `<body>` 占满整个屏幕空间，你可以使用 CSS 来设置相关样式。以下是一种常见的方法：

1. 首先，设置 `<html>` 和 `<body>` 的高度为 100%：

```css
html, body {
  height: 100%;
}
```

这将使 `<html>` 和 `<body>` 元素的高度扩展到整个浏览器窗口的高度。

1. 接下来，将 `<body>` 的外边距和内边距设置为 0：

```css
body {
  margin: 0;
  padding: 0;
}
```

这样可以消除默认的外边距和内边距，确保 `<body>` 元素与浏览器边界之间没有间隙。

1. 最后，将子元素（例如 `<div>`）的高度设置为 100%：

```css
div {
  height: 100%;
}
```

这将使 `<div>` 元素占据其父元素（即 `<body>`）的整个高度。

# 调试CSS

**浏览器快捷键F12和cttrl+shift+I看下面的样式就可以看CSS代码了**

# 标签样式修改

a{text-decoration:none};去掉a标签的下划线

当一个输入框（input）被选中时，可以使用 CSS 的 `:focus` 伪类来应用样式。这个伪类用于匹配处于焦点状态的元素。你可以通过设置不同的样式来突出显示被选中的输入框。

以下是一些常见的针对被选中输入框的 CSS 样式：

```css
input:focus {
  outline: none; /* 取消选中时的默认外观 */
  border: 2px solid blue; /* 设置选中时的边框样式 */
  background-color: lightblue; /* 设置选中时的背景色 */
  /* 可以继续添加其他样式 */
}
```

在上面的示例中，`input:focus` 选择器会选择被选中的输入框，然后可以根据需要进行样式设置。`outline: none;` 会取消默认的选中外观，`border` 和 `background-color` 属性可以设置选中时的边框样式和背景色。

## 阴影

要给元素添加阴影效果，你可以使用 CSS 的 `box-shadow` 属性。`box-shadow` 使你能够创建元素的阴影效果，可以控制阴影的颜色、大小、模糊度等。

下面是一个示例，展示如何为一个 `<div>` 元素添加阴影效果：

```css
div {
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}
```

在这例子中，`box-shadow` 的值包含四个参数，分别是：

- 水平偏移量：2px
- 垂直偏移量：2px
- 模糊度：4px
- 阴影颜色：rgba(0, 0, 0, 0.3)

你可以调整这些参数来得到你想要的阴影效果。水平偏移量和垂直偏移量可以为负值，表示阴影在元素的左上方，而不是右下方。

`box-shadow` 属性还支持多个阴影效果的叠加，通过以逗号分隔的方式，你可以指定多个阴影效果。例如：

```css
div {
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3),
              -2px -2px 4px rgba(255, 255, 255, 0.3);
}
```

这个例子中，该 `<div>` 元素将同时具有一个白色的内阴影和一个黑色的外阴影效果。

通过调整 `box-shadow` 的参数和添加额外的阴影效果，你可以创建出各种不同的阴影效果来适应你的设计需求。

**一 在原页面嵌入其他页面**

1、使用**iframe**框架

客户端页面嵌套可以使用iframe的方法，弊端是必须事先想好被嵌套的页面在首页中要占多大的位置。

如果被嵌套页面太大，超过事先定义的宽度或高度，则首页会出现滚动条。这也许正是你所需要的，

但也许会完全破坏主页的设计。

  **< iframe >------ < / iframe >**

例： **<iframe src="text.asp" height="200" width="600">**  

​                       <a href="text.asp">

​             **你的浏览器不支持iframe页面嵌套，请点击这里访问页面内容。**

​            **</a>**

​       **</ifrmae >**
