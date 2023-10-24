# TypeScript介绍

## 什么是TypeScript？

1. 加强版的JavaScript
2. 加强了【Type】的部分
3. 开始完成后，最终还是需要编译成JavaScript
4. 适用于前端后端开发：react，express等框架

## 为什么需要TypeScript？

1.开始时的（type）类型检查

2.增强js，run起来才出错的缺点（不小心用子串做加减）

3.提高方案程序码的维护性



## 优点

- 减少程序码运行时Bug
- 提高方案的稳定性
- 看懂一些fuction参数等等



## 缺点

- 不是【真正】的类型检查
- 需要编译，CI/CD部署速度慢
- 花更多时间开始跟学习



# TypeScript搭建环境

安装Node.js

[TypeScript 中文网: 下载 (nodejs.cn)](https://ts.nodejs.cn/download)

全局安装：

```
npm install -g typescript
```

编译ts：

```
tsc 文件名.ts
```

修改档案：

```
tsc --init
```

就会出现一个json档案，可以指定输出内容

outDir和indir 输出输入

# 错误检查

JavaScript 中的每个值都有一组行为，你可以通过运行不同的操作来观察这些行为。 这听起来很抽象，但作为一个简单的例子，考虑我们可能在名为 `message` 的变量上运行的一些操作。

```
// Accessing the property 'toLowerCase'
// on 'message' and then calling it
message.toLowerCase();

// Calling 'message'
message();
```

如果我们将其分解，第一行可运行的代码会访问一个名为 `toLowerCase` 的属性，然后调用它。 第二个尝试直接调用 `message`。

但是假设我们不知道 `message` 的值 - 这很常见 - 我们不能可靠地说明尝试运行这些代码会得到什么结果。 每个操作的行为完全取决于我们最初拥有的值。

- `message` 可以调用吗？
- 它上面是否有一个名为 `toLowerCase` 的属性？
- 如果是这样，`toLowerCase` 甚至可以调用吗？
- 如果这两个值都是可调用的，它们会返回什么？

这些问题的答案通常是我们在编写 JavaScript 时牢记在心的事情，我们必须希望我们得到了正确的所有细节。

假设 `message` 是按以下方式定义的。

```
const message = "Hello World!";
```

正如你可能猜到的，如果我们尝试运行 `message.toLowerCase()`，我们将只得到相同的小写字符串。

那第二行代码呢？ 如果你熟悉 JavaScript，就会知道这会失败并出现异常：

```
TypeError: message is not a function
```

如果我们能避免这样的错误，那就太好了。

当我们运行我们的代码时，我们的 JavaScript 运行时选择做什么的方式是确定值的类型 - 它具有什么样的行为和能力。 这就是 `TypeError` 所暗示的部分内容 - 它表示字符串 `"Hello World!"` 不能作为函数调用。

对于某些值，例如原语 `string` 和 `number`，我们可以在运行时使用 `typeof` 运算符识别它们的类型。 但是对于其他的东西，比如函数，没有相应的运行时机制来识别它们的类型。 例如，考虑这个函数：

```
function fn(x) {
  return x.flip();
}
```

我们可以通过阅读代码观察到，这个函数只有在给定一个具有可调用 `flip` 属性的对象时才能工作，但 JavaScript 不会以我们可以在代码运行时检查的方式显示这些信息。 在纯 JavaScript 中，判断 `fn` 对特定值做了什么的唯一方法是调用它并查看会发生什么。 这种行为使得很难在代码运行之前预测代码将做什么，这意味着在编写代码时更难知道代码将要做什么。

这样看，类型就是描述哪些值可以传递给 `fn`，哪些会崩溃的概念。 JavaScript 仅真正提供动态类型 - 运行代码以查看发生了什么。

另一种方法是使用静态类型系统在运行之前预测预期的代码。



## 静态类型检查

回想一下我们之前尝试将 `string` 作为函数调用而得到的 `TypeError`。 大多数人不喜欢在运行他们的代码时遇到任何类型的错误 - 那些被认为是错误！ 当我们编写新代码时，我们会尽力避免引入新的错误。

如果我们只添加一点代码，保存我们的文件，重新运行代码，并立即看到错误，我们可能能够快速隔离问题； 但情况并非总是如此。 我们可能没有对这个功能进行足够彻底的测试，所以我们可能永远不会真正遇到可能抛出的潜在错误！ 或者，如果我们有幸目睹了这个错误，我们可能最终会进行大规模的重构并添加许多我们不得不挖掘的不同代码。

理想情况下，我们可以有一个工具来帮助我们在代码运行之前找到这些错误。 这就是像 TypeScript 这样的静态类型检查器所做的。 静态类型系统描述了当我们运行程序时我们的值的形状和行为。 像 TypeScript 这样的类型检查器使用这些信息并告诉我们什么时候事情可能会出轨。

```
const message = "hello!"; message();This expression is not callable.
  Type 'String' has no call signatures.This expression is not callable.
  Type 'String' has no call signatures.Try
```

在我们首先运行代码之前，使用 TypeScript 运行最后一个示例会给我们一个错误消息。



## 非异常故障

到目前为止，我们一直在讨论某些事情，比如运行时错误 - JavaScript 运行时告诉我们它认为某些事情是荒谬的情况。 出现这些情况是因为 [ECMAScript 规范](https://tc39.github.io/ecma262/) 明确说明了语言在遇到意外情况时应该如何表现。

例如，规范说尝试调用不可调用的东西应该会引发错误。 也许这听起来像 “明显的行为”，但你可以想象访问对象上不存在的属性也会引发错误。 相反，JavaScript 为我们提供了不同的行为并返回值 `undefined`：

```
const user = {
  name: "Daniel",
  age: 26,
};

user.location; // returns undefined
```

最终，静态类型系统必须调用其系统中应将哪些代码标记为错误，即使是不会立即抛出错误的 “valid” JavaScript。 在 TypeScript 中，以下代码会产生关于 `location` 未定义的错误：

```
const user = {
  name: "Daniel",
  age: 26,
};
 
user.location;Property 'location' does not exist on type '{ name: string; age: number; }'.Property 'location' does not exist on type '{ name: string; age: number; }'.Try
```

虽然有时这意味着在你可以表达的内容上进行权衡，但其目的是捕捉我们程序中的合法错误。 TypeScript 捕获了很多合法的错误。

例如： 错别字，

```
const announcement = "Hello World!";
 
// How quickly can you spot the typos?
announcement.toLocaleLowercase();
announcement.toLocalLowerCase();
 
// We probably meant to write this...
announcement.toLocaleLowerCase();Try
```

未调用的函数，

```
function flipCoin() {
  // Meant to be Math.random()
  return Math.random < 0.5;Operator '<' cannot be applied to types '() => number' and 'number'.Operator '<' cannot be applied to types '() => number' and 'number'.
}Try
```

或基本逻辑错误。

```
const value = Math.random() < 0.5 ? "a" : "b";
if (value !== "a") {
  // ...
} else if (value === "b") {This comparison appears to be unintentional because the types '"a"' and '"b"' have no overlap.This comparison appears to be unintentional because the types '"a"' and '"b"' have no overlap.
  // Oops, unreachable
}Try
```



## 工具类型

当我们在代码中出错时，TypeScript 可以捕获错误。 这很好，但 TypeScript 也可以从一开始就阻止我们犯这些错误。

类型检查器具有检查诸如我们是否正在访问变量和其他属性的正确属性之类的信息。 一旦有了这些信息，它还可以开始建议你可能想要使用哪些属性。

这意味着 TypeScript 也可以用于编辑代码，核心类型检查器可以在你在编辑器中键入时提供错误消息和代码完成。 这是人们在谈论 TypeScript 工具时经常提到的部分内容。

```
import express from "express";
const app = express();
 
app.get("/", function (req, res) {
  res.sen
         sendsendDatesendfilesendFilesendStatus
});
 
app.listen(3000);Try
```

TypeScript 非常重视工具，这超出了你键入时的完成和错误。 支持 TypeScript 的编辑器可以提供 “快速修复” 以自动修复错误、重构以轻松重新组织代码，以及用于跳转到变量定义或查找对给定变量的所有引用的有用导航功能。 所有这些都建立在类型检查器之上，并且是完全跨平台的，所以很可能是 [你最喜欢的编辑器支持 TypeScript](https://github.com/Microsoft/TypeScript/wiki/TypeScript-Editor-Support)。



## `tsc`，TypeScript 编译器

我们一直在谈论类型检查，但我们还没有使用我们的类型检查器。 让我们熟悉一下我们的新朋友 `tsc`，TypeScript 编译器。 首先，我们需要通过 npm 获取它。

```
npm install -g typescript
```

> 这将全局安装 TypeScript 编译器 `tsc`。 如果你希望从本地 `node_modules` 包运行 `tsc`，则可以使用 `npx` 或类似工具。

现在让我们移至一个空文件夹并尝试编写我们的第一个 TypeScript 程序： `hello.ts`：

```
// Greets the world.
console.log("Hello world!");Try
```

请注意这里没有多余的装饰； 这个 “你好世界” 程序看起来与你用 JavaScript 编写的 “你好世界” 程序完全相同。 现在让我们通过运行 `typescript` 包为我们安装的命令 `tsc` 来检查它。

```
tsc hello.ts
```

Tada!

等等，“tada” 到底是什么？ 我们运行了 `tsc`，但什么也没发生！ 好吧，没有类型错误，所以我们没有在控制台中得到任何输出，因为没有什么要报告的。

但再次检查 - 我们得到了一些文件输出。 如果我们查看当前目录，我们会在 `hello.ts` 旁边看到一个 `hello.js` 文件。 这是 `tsc` 编译或转换为纯 JavaScript 文件后我们的 `hello.ts` 文件的输出。 如果我们检查内容，我们会看到 TypeScript 在处理 `.ts` 文件后会吐出什么：

```
// Greets the world.
console.log("Hello world!");
```

在这种情况下，TypeScript 几乎不需要转换，所以它看起来和我们写的一样。 编译器试图触发看起来像人会写的东西的干净可读的代码。 虽然这并不总是那么容易，但 TypeScript 会始终如一地缩进，注意我们的代码何时跨越不同的代码行，并试图保留注释。

如果我们确实引入了类型检查错误怎么办？ 让我们重写 `hello.ts`：

```
// This is an industrial-grade general-purpose greeter function:
function greet(person, date) {
  console.log(`Hello ${person}, today is ${date}!`);
}
 
greet("Brendan");Try
```

如果我们再次运行 `tsc hello.ts`，请注意我们在命令行上收到错误！

```
Expected 2 arguments, but got 1.
```

TypeScript 告诉我们，我们忘记将参数传递给 `greet` 函数，这是理所当然的。 到目前为止，我们只编写了标准的 JavaScript，但类型检查仍然能够发现我们代码的问题。 感谢 TypeScript！



## 使用错误触发

从上一个示例中你可能没有注意到的一件事是我们的 `hello.js` 文件再次更改。 如果我们打开该文件，我们会看到内容与我们的输入文件看起来基本相同。 考虑到 `tsc` 报告了关于我们代码的错误，这可能有点令人惊讶，但这是基于 TypeScript 的核心价值之一： 很多时候，你会比 TypeScript 更了解。

重申一下，类型检查代码限制了你可以运行的程序种类，因此需要权衡类型检查器认为可以接受的类型。 大多数时候没关系，但在某些情况下，这些检查会妨碍你。 例如，假设你将 JavaScript 代码迁移到 TypeScript 并引入类型检查错误。 最终，你将开始为类型检查器清理东西，但原始的 JavaScript 代码已经可以工作了！ 为什么要将其转换为 TypeScript 会阻止你运行它？

所以 TypeScript 不会妨碍你。 当然，随着时间的推移，你可能希望对错误更加防御，并使 TypeScript 的行为更加严格。 在这种情况下，你可以使用 [`noEmitOnError`](https://ts.nodejs.cn/tsconfig#noEmitOnError) 编译器选项。 尝试更改你的 `hello.ts` 文件并使用该标志运行 `tsc`：

```
tsc --noEmitOnError hello.ts
```

你会注意到 `hello.js` 永远不会更新。



## 显式的类型

到目前为止，我们还没有告诉 TypeScript `person` 或 `date` 是什么。 让我们编辑代码来告诉 TypeScript `person` 是一个 `string`，而 `date` 应该是一个 `Date` 对象。 我们还将在 `date` 上使用 `toDateString()` 方法。

```
function greet(person: string, date: Date) {
  console.log(`Hello ${person}, today is ${date.toDateString()}!`);
}Try
```

我们所做的是在 `person` 和 `date` 上添加类型注释来描述可以使用哪些类型的值来调用 `greet`。 你可以将该签名读作 ”`greet` 采用 `string` 类型的 `person` 和 `Date` 类型的 `date`“。

有了这个，TypeScript 可以告诉我们 `greet` 可能被错误调用的其他情况。 例如…

```
function greet(person: string, date: Date) {
  console.log(`Hello ${person}, today is ${date.toDateString()}!`);
}
 
greet("Maddison", Date());Argument of type 'string' is not assignable to parameter of type 'Date'.Argument of type 'string' is not assignable to parameter of type 'Date'.Try
```

嗯？ TypeScript 在我们的第二个参数上报告了错误，但为什么呢？

也许令人惊讶的是，在 JavaScript 中调用 `Date()` 返回一个 `string`。 另一方面，用 `new Date()` 构造一个 `Date` 实际上给了我们所期望的结果。

无论如何，我们可以快速修复错误：

```
function greet(person: string, date: Date) {
  console.log(`Hello ${person}, today is ${date.toDateString()}!`);
}
 
greet("Maddison", new Date());Try
```

请记住，我们并不总是必须编写显式类型注释。 在许多情况下，TypeScript 甚至可以为我们推断（或 “弄清楚”）类型，即使我们省略它们。

```
let msg = "hello there!";
    
let msg: stringTry
```

即使我们没有告诉 TypeScript `msg` 有 `string` 类型，它也能够弄清楚这一点。 这是一个特性，当类型系统最终会推断出相同的类型时，最好不要添加注释。

> 注意： 如果你将鼠标悬停在该单词上，则上一个代码示例中的消息气泡是你的编辑器将显示的内容。



## 擦除的类型

让我们看看当我们用 `tsc` 编译上面的函数 `greet` 以输出 JavaScript 时会发生什么：

```
"use strict";
function greet(person, date) {
    console.log("Hello ".concat(person, ", today is ").concat(date.toDateString(), "!"));
}
greet("Maddison", new Date());
 Try
```

这里注意两点：

1. 我们的 `person` 和 `date` 参数不再有类型注释。
2. 我们的 “模板字符串” - 使用反引号（``` 字符）的字符串 - 被转换为带有连接的纯字符串。

稍后会详细介绍第二点，但现在让我们关注第一点。 类型注释不是 JavaScript 的一部分（或者 ECMAScript 是迂腐的），所以实际上没有任何浏览器或其他运行时可以在未经修改的情况下运行 TypeScript。 这就是 TypeScript 首先需要一个编译器的原因 - 它需要某种方式来剥离或转换任何 TypeScript 特定的代码，以便你可以运行它。 大多数特定于 TypeScript 的代码都被删除了，同样地，我们的类型注释也被完全删除了。

> **记住**： 类型注释永远不会改变程序的运行时行为。



## 降级

与上面的另一个区别是我们的模板字符串是从

```
`Hello ${person}, today is ${date.toDateString()}!`;
```

到

```
"Hello ".concat(person, ", today is ").concat(date.toDateString(), "!");
```

为什么会这样？

模板字符串是 ECMAScript 版本中的一项功能，称为 ECMAScript 2015（又名 ECMAScript 6、ES2015、ES6 等 - 不要问）。 TypeScript 能够将代码从较新版本的 ECMAScript 重写为较旧的版本，例如 ECMAScript 3 或 ECMAScript 5（又名 ES3 和 ES5）。 从 ECMAScript 的新版本或 “higher” 版本向下移动到旧版本或 “lower” 版本的过程有时称为降级。

默认情况下，TypeScript 以 ES3 为目标，这是一个非常旧的 ECMAScript 版本。 通过使用 [`target`](https://ts.nodejs.cn/tsconfig#target) 选项，我们可以选择更新一点的东西。 使用 `--target es2015` 运行将 TypeScript 更改为以 ECMAScript 2015 为目标，这意味着代码应该能够在任何支持 ECMAScript 2015 的地方运行。 所以运行 `tsc --target es2015 hello.ts` 会给我们以下输出：

```
function greet(person, date) {
  console.log(`Hello ${person}, today is ${date.toDateString()}!`);
}
greet("Maddison", new Date());
```

> 虽然默认目标是 ES3，但当前绝大多数浏览器都支持 ES2015。 因此，大多数开发者可以安全地将 ES2015 或更高版本指定为目标，除非与某些古老的浏览器的兼容性很重要。



## 严格性

不同的用户使用 TypeScript 在类型检查器中寻找不同的东西。 有些人正在寻找一种更宽松的选择加入体验，它可以帮助验证他们程序的某些部分，并且仍然拥有不错的工具。 这是 TypeScript 的默认体验，其中类型是可选的，推断采用最宽松的类型，并且不检查潜在的 `null`/`undefined` 值。 就像 `tsc` 在面对错误时触发的一样，这些默认设置是为了不妨碍你。 如果你要迁移现有的 JavaScript，那么这可能是理想的第一步。

相比之下，许多用户更喜欢让 TypeScript 尽可能多地立即验证，这就是该语言也提供严格设置的原因。 这些严格性设置将静态类型检查从开关（无论是否检查你的代码）变成更接近调节器的东西。 你把这个调节器调得越高，TypeScript 就会越多地为你检查。 这可能需要一些额外的工作，但一般来说，从长远来看，它会为自己付出代价，并且可以进行更彻底的检查和更准确的工具。 如果可能，新的代码库应始终打开这些严格性检查。

TypeScript 有几个可以打开或关闭的类型检查严格标志，除非另有说明，否则我们所有的示例都将在启用所有这些标志的情况下编写。 CLI 中的 [`strict`](https://ts.nodejs.cn/tsconfig#strict) 标志或 [`tsconfig.json`](https://ts.nodejs.cn/docs/handbook/tsconfig-json.html) 中的 `"strict": true` 会同时将它们全部打开，但我们可以单独选择退出它们。 你应该知道的两个最大的是 [`noImplicitAny`](https://ts.nodejs.cn/tsconfig#noImplicitAny) 和 [`strictNullChecks`](https://ts.nodejs.cn/tsconfig#strictNullChecks)。

## `noImplicitAny`

回想一下，在某些地方，TypeScript 不会尝试为我们推断类型，而是退回到最宽松的类型： `any`。 这并不是可能发生的最糟糕的事情 - 毕竟，回退到 `any` 只是简单的 JavaScript 体验。

然而，使用 `any` 通常会破坏使用 TypeScript 的初衷。 你的程序类型越多，你获得的验证和工具就越多，这意味着你在编写代码时遇到的错误就越少。 打开 [`noImplicitAny`](https://ts.nodejs.cn/tsconfig#noImplicitAny) 标志将对任何类型隐式推断为 `any` 的变量触发错误。

## `strictNullChecks`

默认情况下，像 `null` 和 `undefined` 这样的值可以分配给任何其他类型。 这可以使编写一些代码更容易，但忘记处理 `null` 和 `undefined` 是世界上无数错误的原因 - 有些人认为它是 [十亿美元的错误](https://www.youtube.com/watch?v=ybrQvs4x0Ps)！ [`strictNullChecks`](https://ts.nodejs.cn/tsconfig#strictNullChecks) 标志使处理 `null` 和 `undefined` 更加明确，让我们不必担心是否忘记处理 `null` 和 `undefined`。

# 基础类型

在本章中，我们将介绍 JavaScript 代码中一些最常见的值类型，并解释在 TypeScript 中描述这些类型的相应方法。 这不是一个详尽的列表，未来的章节将描述更多命名和使用其他类型的方法。

类型也可以出现在更多的地方，而不仅仅是类型注释。 当我们了解类型本身时，我们还将了解可以引用这些类型以形成新结构的地方。

我们将首先回顾你在编写 JavaScript 或 TypeScript 代码时可能遇到的最基本和最常见的类型。 这些稍后将形成更复杂类型的核心构建块。



## 原语：`string`、`number` 和 `boolean`

JavaScript 有三个非常常用的 [原语](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)： `string`、`number` 和 `boolean`。 每个在 TypeScript 中都有对应的类型。 如你所料，如果你对这些类型的值使用 JavaScript `typeof` 运算符，这些名称与你看到的名称相同：

- `string` 表示字符串值，如 `"Hello, world"`
- `number` 代表像 `42` 这样的数字。 JavaScript 对整数没有特殊的运行时值，因此没有等价于 `int` 或 `float` - 一切都只是 `number`
- `boolean` 代表 `true` 和 `false` 这两个值

> 类型名称 `String`、`Number` 和 `Boolean`（以大写字母开头）是合法的，但指的是一些很少出现在代码中的特殊内置类型。 始终使用 `string`、`number` 或 `boolean` 作为类型。



## 数组

要指定像 `[1, 2, 3]` 这样的数组类型，可以使用语法 `number[]`； 此语法适用于任何类型（例如，`string[]` 是一个字符串数组，等等）。 你也可以看到这个写成 `Array<number>`，意思是一样的。 当我们介绍泛型时，我们将了解更多关于语法 `T<U>` 的信息。

> 请注意，`[number]` 是另一回事； 请参阅 [元组](https://ts.nodejs.cn/docs/handbook/2/objects.html#tuple-types) 部分。

## `any`

TypeScript 也有一个特殊的类型，`any`，当你不希望某个特定的值导致类型检查错误时，你可以使用它。

当一个值的类型为 `any` 时，你可以访问它的任何属性（这又将是 `any` 类型），像函数一样调用它，将它分配给（或从）任何类型的值，或者几乎任何其他东西这在语法上是合法的：

```tsx
let obj: any = { x: 0 };
// None of the following lines of code will throw compiler errors.
// Using `any` disables all further type checking, and it is assumed
// you know the environment better than TypeScript.
obj.foo();
obj();
obj.bar = 100;
obj = "hello";
const n: number = obj;Try
```

当你不想写出一个长类型来让 TypeScript 相信特定的代码行是可以的时，`any` 类型很有用。

### `noImplicitAny`

当你没有指定类型，并且 TypeScript 不能从上下文推断它时，编译器通常会默认为 `any`。

不过，你通常希望避免这种情况，因为 `any` 没有经过类型检查。 使用编译器标志 [`noImplicitAny`](https://ts.nodejs.cn/tsconfig#noImplicitAny) 将任何隐式 `any` 标记为错误。



## 变量的类型注释

当你使用 `const`、`var` 或 `let` 声明变量时，你可以选择添加类型注释以显式指定变量的类型：

```tsx
let myName: string = "Alice";
```

> TypeScript 不使用像 `int x = 0;` 这样的 “左边的类型” 风格的声明。 类型注释将始终在输入的内容之后。

但是，在大多数情况下，这不是必需的。 TypeScript 会尽可能地尝试自动推断代码中的类型。 例如，变量的类型是根据其初始化程序的类型推断的：

```js
// No type annotation needed -- 'myName' inferred as type 'string'
let myName = "Alice";
```

在大多数情况下，你不需要明确学习推断规则。 如果你刚开始，请尝试使用比你想象的更少的类型注释 - 你可能会惊讶于 TypeScript 完全理解正在发生的事情需要多少。



# 函数

函数是在 JavaScript 中传递数据的主要方式。 TypeScript 允许你指定函数的输入和输出值的类型。



### 参数类型注解

声明函数时，可以在每个参数后面加上类型注解，声明函数接受哪些类型的参数。 参数类型注释在参数名称之后：

```tsx
// Parameter type annotation
function greet(name: string) {
  console.log("Hello, " + name.toUpperCase() + "!!");
}Try
```

当参数具有类型注释时，将检查该函数的参数：

```
// Would be a runtime error if executed!
greet(42);Argument of type 'number' is not assignable to parameter of type 'string'.Argument of type 'number' is not assignable to parameter of type 'string'.Try
```

> 即使你的参数上没有类型注释，TypeScript 仍会检查你是否传递了正确数量的参数。



### 返回类型注解

你还可以添加返回类型注释。 返回类型注释出现在参数列表之后：

```tsx
function getFavoriteNumber(): number {
  return 26;
}
```

与变量类型注解非常相似，你通常不需要返回类型注解，因为 TypeScript 会根据其 `return` 语句推断函数的返回类型。 上面例子中的类型注解并没有改变任何东西。 一些代码库将明确指定返回类型以用于文档目的，以防止意外更改，或仅出于个人喜好。



#### 返回 Promise 的函数

如果你想注释一个返回 Promise 的函数的返回类型，你应该使用 `Promise` 类型：

```tsx
async function getFavoriteNumber(): Promise<number> {
  return 26;
}
```



### 匿名函数

匿名函数与函数声明有点不同。 当一个函数出现在 TypeScript 可以确定如何调用它的地方时，该函数的参数会自动被赋予类型。

这是一个例子：

```tsx
const names = ["Alice", "Bob", "Eve"];
 
// Contextual typing for function - parameter s inferred to have type string
names.forEach(function (s) {
  console.log(s.toUpperCase());
});
 
// Contextual typing also applies to arrow functions
names.forEach((s) => {
  console.log(s.toUpperCase());
});Try
```

即使参数 `s` 没有类型注释，TypeScript 还是使用 `forEach` 函数的类型以及推断的数组类型来确定 `s` 将具有的类型。

这个过程称为上下文类型，因为函数发生的上下文告知它应该具有什么类型。

与推断规则类似，你不需要明确了解这是如何发生的，但了解它确实发生可以帮助你注意到何时不需要类型注释。 稍后，我们将看到更多关于值出现的上下文如何影响其类型的示例。



## 对象类型



除了原语之外，你会遇到的最常见的类型是对象类型。 这指的是任何带有属性的 JavaScript 值，几乎是所有属性！ 要定义对象类型，我们只需列出其属性及其类型。

例如，这是一个接受点状对象的函数：

```tsx
// The parameter's type annotation is an object type
function printCoord(pt: { x: number; y: number }) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}
printCoord({ x: 3, y: 7 });Try
```

在这里，我们使用具有两个属性的类型注释参数 - `x` 和 `y` - 这两个属性都是 `number` 类型。 你可以使用 `,` 或 `;` 来分隔属性，最后一个分隔符是可选的。

每个属性的类型部分也是可选的。 如果不指定类型，则假定为 `any`。



### 可选属性

对象类型还可以指定它们的部分或全部属性是可选的。 为此，请在属性名称后添加 `?`：

```tsx
function printName(obj: { first: string; last?: string }) {
  // ...
}
// Both OK
printName({ first: "Bob" });
printName({ first: "Alice", last: "Alisson" });
```



在 JavaScript 中，如果你访问一个不存在的属性，你将获得值 `undefined` 而不是运行时错误。 因此，当你从可选属性中读取数据时，你必须在使用它之前检查 `undefined`。

```tsx
function printName(obj: { first: string; last?: string }) {
  // Error - might crash if 'obj.last' wasn't provided!
  console.log(obj.last.toUpperCase());'obj.last' is possibly 'undefined'.'obj.last' is possibly 'undefined'.
  if (obj.last !== undefined) {
    // OK
    console.log(obj.last.toUpperCase());
  }
 
  // A safe alternative using modern JavaScript syntax:
  console.log(obj.last?.toUpperCase());
}Try
```



## 联合类型

TypeScript 的类型系统允许你使用各种运算符从现有类型中构建新类型。 现在我们知道如何编写几种类型，是时候开始以有趣的方式组合它们了。



### 定义联合类型

你可能会看到的第一种组合类型的方法是联合类型。 联合类型是由两种或多种其他类型组成的类型，表示可能是这些类型中的任何一种的值。 我们将这些类型中的每一种都称为联合的成员。

让我们编写一个可以对字符串或数字进行操作的函数：

```tsx
function printId(id: number | string) {
  console.log("Your ID is: " + id);
}
// OK
printId(101);
// OK
printId("202");
// Error
printId({ myID: 22342 });Argument of type '{ myID: number; }' is not assignable to parameter of type 'string | number'.Argument of type '{ myID: number; }' is not assignable to parameter of type 'string | number'.Try
```



### 使用联合类型

提供与联合类型匹配的值很容易 - 只需提供与联合的任何成员匹配的类型即可。 如果你有一个联合类型的值，你如何处理它？

TypeScript 只有在对联合的每个成员都有效的情况下才允许操作。 例如，如果你有联合 `string | number`，则不能使用仅在 `string` 上可用的方法：

```tsx
function printId(id: number | string) {  console.log(id.toUpperCase());Property 'toUpperCase' does not exist on type 'string | number'.
  Property 'toUpperCase' does not exist on type 'number'.Property 'toUpperCase' does not exist on type 'string | number'.
  Property 'toUpperCase' does not exist on type 'number'.}
```

解决方案是用代码缩小联合，就像在没有类型注释的 JavaScript 中一样。 当 TypeScript 可以根据代码的结构为某个值推断出更具体的类型时，就会发生缩小。

例如，TypeScript 知道只有 `string` 值才会有 `typeof` 值 `"string"`：

```tsx
function printId(id: number | string) {
  if (typeof id === "string") {
    // In this branch, id is of type 'string'
    console.log(id.toUpperCase());
  } else {
    // Here, id is of type 'number'
    console.log(id);
  }
}
```

另一个例子是使用像 `Array.isArray` 这样的函数：

```tsx
function welcomePeople(x: string[] | string) {
  if (Array.isArray(x)) {
    // Here: 'x' is 'string[]'
    console.log("Hello, " + x.join(" and "));
  } else {
    // Here: 'x' is 'string'
    console.log("Welcome lone traveler " + x);
  }
}
```

请注意，在 `else` 分支中，我们不需要做任何特别的事情 - 如果 `x` 不是 `string[]`，那么它一定是 `string`。

有时你会有一个联合，所有成员都有共同点。 例如，数组和字符串都有一个 `slice` 方法。 如果联合中的每个成员都有一个共同的属性，则可以使用该属性而不会缩小类型：

```tsx
// Return type is inferred as number[] | string
function getFirstThree(x: number[] | string) {
  return x.slice(0, 3);
}
```

> 类型的联合似乎具有这些类型的属性的交集，这可能会令人困惑。 这不是偶然的 - 联合这个名字来源于类型论。 联合 `number | string` 是通过取每种类型的值的联合组成的。 请注意，给定两个具有关于每个集合的相应事实的集合，只有这些事实的交集适用于集合本身的并集。 例如，如果我们有一个房间里有戴帽子的高个子，而另一个房间里有戴帽子的说西班牙语的人，在组合这些房间后，我们对每个人的唯一了解就是他们必须戴帽子。



## 类型别名(type)

我们一直通过直接在类型注释中编写对象类型和联合类型来使用它们。 这很方便，但通常**希望多次使用同一个类型并用一个名称引用它**。

类型别名就是这样 - 任何类型的名称。 类型别名的语法是：

```tsx
type Point = {
  x: number;
  y: number;
};
 
// Exactly the same as the earlier example
function printCoord(pt: Point) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}
 
printCoord({ x: 100, y: 100 });
```

实际上，你可以使用类型别名来为任何类型命名，而不仅仅是对象类型。 例如，类型别名可以命名联合类型：

```tsx
type ID = number | string;
```

请注意，别名只是别名 - 你不能使用类型别名来创建相同类型的不同的或独特的 “versions”。 当你使用别名时，就好像你已经编写了别名类型。 换句话说，这段代码可能看起来非法，但根据 TypeScript 是可以的，因为这两种类型都是同一类型的别名：

```tsx
type UserInputSanitizedString = string;
 
function sanitizeInput(str: string): UserInputSanitizedString {
  return sanitize(str);
}
 
// Create a sanitized input
let userInput = sanitizeInput(getInput());
 
// Can still be re-assigned with a string though
userInput = "new input";
```



## 接口

接口声明是命名对象类型的另一种方式：

```tsx
interface Point {
  x: number;
  y: number;
}
 
function printCoord(pt: Point) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}
 
printCoord({ x: 100, y: 100 });Try
```

就像我们在上面使用类型别名时一样，该示例就像我们使用匿名对象类型一样工作。 TypeScript 只关心我们传递给 `printCoord` 的值的结构 - 它只关心它是否具有预期的属性。 **只关心类型的结构和功能是我们称 TypeScript 为结构类型类型系统的原因**。



### 类型别名和接口的区别

类型别名和接口非常相似，在很多情况下你可以在它们之间自由选择。 `interface` 的几乎所有功能都在 `type` 中可用，主要区别在于无法重新打开类型以添加新属性，而接口始终可扩展。

| `Interface`                                                  | `Type`                                                       |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| 扩展接口`interface Animal {  name: string; } interface Bear extends Animal {  honey: boolean; } const bear = getBear(); bear.name; bear.honey;        ` | 通过交集扩展类型`type Animal = {  name: string; } type Bear = Animal & {   honey: boolean; } const bear = getBear(); bear.name; bear.honey;        ` |
| 向现有接口添加新字段`interface Window {  title: string; } interface Window {  ts: TypeScriptAPI; } const src = 'const a = "Hello World"'; window.ts.transpileModule(src, {});        ` | 类型创建后无法更改`type Window = {  title: string; } type Window = {  ts: TypeScriptAPI; } // Error: Duplicate identifier 'Window'.        ` |

你将在后面的章节中了解有关这些概念的更多信息，因此如果你不能立即理解所有这些概念，请不要担心。

- 在 TypeScript 4.2 版之前，类型别名 [可能出现在错误信息中](https://ts.nodejs.cn/play?#code/PTAEGEHsFsAcEsA2BTATqNrLusgzngIYDm+oA7koqIYuYQJ56gCueyoAUCKAC4AWHAHaFcoSADMaQ0PCG80EwgGNkALk6c5C1EtWgAsqOi1QAb06groEbjWg8vVHOKcAvpokshy3vEgyyMr8kEbQJogAFND2YREAlOaW1soBeJAoAHSIkMTRmbbI8e6aPMiZxJmgACqCGKhY6ABGyDnkFFQ0dIzMbBwCwqIccabcYLyQoKjIEmh8kwN8DLAc5PzwwbLMyAAeK77IACYaQSEjUWZWhfYAjABMAMwALA+gbsVjoADqgjKESytQPxCHghAByXigYgBfr8LAsYj8aQMUASbDQcRSExCeCwFiIQh+AKfAYyBiQFgOPyIaikSGLQo0Zj-aazaY+dSaXjLDgAGXgAC9CKhDqAALxJaw2Ib2RzOISuDycLw+ImBYKQflCkWRRD2LXCw6JCxS1JCdJZHJ5RAFIbFJU8ADKC3WzEcnVZaGYE1ABpFnFOmsFhsil2uoHuzwArO9SmAAEIsSFrZB-GgAjjA5gtVN8VCEc1o1C4Q4AGlR2AwO1EsBQoAAbvB-gJ4HhPgB5aDwem-Ph1TCV3AEEirTp4ELtRbTPD4vwKjOfAuioSQHuDXBcnmgACC+eCONFEs73YAPGGZVT5cRyyhiHh7AAON7lsG3vBggB8XGV3l8-nVISOgghxoLq9i7io-AHsayRWGaFrlFauq2rg9qaIGQHwCBqChtKdgRo8TxRjeyB3o+7xAA)，有时代替等效的匿名类型（可能需要也可能不需要）。 接口将始终在错误消息中命名。
- 类型别名不得参与 [在声明合并中，但接口可以](https://ts.nodejs.cn/play?#code/PTAEEEDtQS0gXApgJwGYEMDGjSfdAIx2UQFoB7AB0UkQBMAoEUfO0Wgd1ADd0AbAK6IAzizp16ALgYM4SNFhwBZdAFtV-UAG8GoPaADmNAcMmhh8ZHAMMAvjLkoM2UCvWad+0ARL0A-GYWVpA29gyY5JAWLJAwGnxmbvGgALzauvpGkCZmAEQAjABMAMwALLkANBl6zABi6DB8okR4Jjg+iPSgABboovDk3jjo5pbW1d6+dGb5djLwAJ7UoABKiJTwjThpnpnGpqPBoTLMAJrkArj4kOTwYmycPOhW6AR8IrDQ8N04wmo4HHQCwYi2Waw2W1S6S8HX8gTGITsQA)。
- 接口只能用于 [声明对象的形状，而不是重命名基元](https://ts.nodejs.cn/play?#code/PTAEAkFMCdIcgM6gC4HcD2pIA8CGBbABwBtIl0AzUAKBFAFcEBLAOwHMUBPQs0XFgCahWyGBVwBjMrTDJMAshOhMARpD4tQ6FQCtIE5DWoixk9QEEWAeV37kARlABvaqDegAbrmL1IALlAEZGV2agBfampkbgtrWwMAJlAAXmdXdy8ff0Dg1jZwyLoAVWZ2Lh5QVHUJflAlSFxROsY5fFAWAmk6CnRoLGwmILzQQmV8JmQmDzI-SOiKgGV+CaYAL0gBBdyy1KCQ-Pn1AFFplgA5enw1PtSWS+vCsAAVAAtB4QQWOEMKBuYVUiVCYvYQsUTQcRSBDGMGmKSgAAa-VEgiQe2GLgKQA)。
- 接口名称将在错误消息中显示为 [总是以原来的形式出现](https://ts.nodejs.cn/play?#code/PTAEGEHsFsAcEsA2BTATqNrLusgzngIYDm+oA7koqIYuYQJ56gCueyoAUCKAC4AWHAHaFcoSADMaQ0PCG80EwgGNkALk6c5C1EtWgAsqOi1QAb06groEbjWg8vVHOKcAvpokshy3vEgyyMr8kEbQJogAFND2YREAlOaW1soBeJAoAHSIkMTRmbbI8e6aPMiZxJmgACqCGKhY6ABGyDnkFFQ0dIzMbBwCwqIccabcYLyQoKjIEmh8kwN8DLAc5PzwwbLMyAAeK77IACYaQSEjUWY2Q-YAjABMAMwALA+gbsVjNXW8yxySoAADaAA0CCaZbPh1XYqXgOIY0ZgmcK0AA0nyaLFhhGY8F4AHJmEJILCWsgZId4NNfIgGFdcIcUTVfgBlZTOWC8T7kAJ42G4eT+GS42QyRaYbCgXAEEguTzeXyCjDBSAAQSE8Ai0Xsl0K9kcziExDeiQs1lAqSE6SyOTy0AKQ2KHk4p1V6s1OuuoHuzwArMagA)，但仅当它们被名称使用时。

在大多数情况下，你可以根据个人喜好进行选择，TypeScript 会告诉你是否需要其他类型的声明。 如果你想要启发式方法，请使用 `interface`，直到你需要使用 `type` 中的功能。



## 类型断言( as )

有时你会得到关于 TypeScript 无法知道的值类型的信息。

例如，如果你使用的是 `document.getElementById`，TypeScript 只知道这将返回某种 `HTMLElement`，但你可能知道你的页面将始终具有具有给定 ID 的 `HTMLCanvasElement`。

在这种情况下，你可以使用类型断言来指定更具体的类型：

```tsx
const myCanvas = document.getElementById("main_canvas") as HTMLCanvasElement;
```

与类型注释一样，类型断言被编译器删除，不会影响代码的运行时行为。

你还可以使用尖括号语法（除非代码在 `.tsx` 文件中），它是等效的：

```tsx
const myCanvas = <HTMLCanvasElement>document.getElementById("main_canvas");
```

> 提醒： 因为类型断言在编译时被删除，所以没有与类型断言关联的运行时检查。 如果类型断言错误，则不会产生异常或 `null`。

TypeScript 只允许类型断言转换为更具体或更不具体的类型版本。 此规则可防止 “impossible” 强制，例如：

```tsx
const x = "hello" as number;Conversion of type 'string' to type 'number' may be a mistake because neither type sufficiently overlaps with the other. If this was intentional, convert the expression to 'unknown' first.Conversion of type 'string' to type 'number' may be a mistake because neither type sufficiently overlaps with the other. If this was intentional, convert the expression to 'unknown' first.
```

有时，此规则可能过于保守，并且不允许可能有效的更复杂的强制转换。 如果发生这种情况，你可以使用两个断言，首先是 `any`（或 `unknown`，我们稍后会介绍），然后是所需的类型：

```tsx
const a = expr as any as T;Try
```



## 字面类型

除了通用类型 `string` 和 `number` 之外，我们还可以在类型位置引用特定的字符串和数字。

考虑这一点的一种方法是考虑 JavaScript 如何使用不同的方法来声明变量。 `var` 和 `let` 都允许更改变量中保存的内容，而 `const` 不允许。 这反映在 TypeScript 如何为字面创建类型。

```tsx
let changingString = "Hello World";
changingString = "Olá Mundo";
// Because `changingString` can represent any possible string, that
// is how TypeScript describes it in the type system
changingString;
      
let changingString: string
 
const constantString = "Hello World";
// Because `constantString` can only represent 1 possible string, it
// has a literal type representation
constantString;
      
const constantString: "Hello World"
```

就其本身而言，字面类型并不是很有价值：

```tsx
let x: "hello" = "hello";
// OK
x = "hello";
// ...
x = "howdy";Type '"howdy"' is not assignable to type '"hello"'.Type '"howdy"' is not assignable to type '"hello"'.Try
```

变量只能有一个值并没有多大用处！

但是通过将字面组合成联合，你可以表达一个更有用的概念 - 例如，只接受一组已知值的函数：

```tsx
function printText(s: string, alignment: "left" | "right" | "center") {
  // ...
}
printText("Hello, world", "left");
printText("G'day, mate", "centre");Argument of type '"centre"' is not assignable to parameter of type '"left" | "right" | "center"'.Argument of type '"centre"' is not assignable to parameter of type '"left" | "right" | "center"'.
```

数字字面类型的工作方式相同：

```tsx
function compare(a: string, b: string): -1 | 0 | 1 {
  return a === b ? 0 : a > b ? 1 : -1;
}Try
```

当然，你可以将这些与非字面类型结合使用：

```tsx
interface Options {
  width: number;
}
function configure(x: Options | "auto") {
  // ...
}
configure({ width: 100 });
configure("auto");
configure("automatic");Argument of type '"automatic"' is not assignable to parameter of type 'Options | "auto"'.Argument of type '"automatic"' is not assignable to parameter of type 'Options | "auto"'.
```

还有一种字面类型： 布尔字面量。 只有两种布尔字面类型，正如你可能猜到的，它们是 `true` 和 `false` 类型。 类型 `boolean` 本身实际上只是联合 `true | false` 的别名。



### 字面推断

当你使用对象初始化变量时，TypeScript 假定该对象的属性可能会在以后更改值。 例如，如果你编写如下代码：

```tsx
const obj = { counter: 0 };
if (someCondition) {
  obj.counter = 1;
}
```

TypeScript 不假定将 `1` 分配给先前具有 `0` 的字段是错误的。 另一种说法是 `obj.counter` 必须具有 `number` 类型，而不是 `0`，因为类型用于确定读取和写入行为。

这同样适用于字符串：

```tsx
declare function handleRequest(url: string, method: "GET" | "POST"): void;
 
const req = { url: "https://example.com", method: "GET" };
handleRequest(req.url, req.method);Argument of type 'string' is not assignable to parameter of type '"GET" | "POST"'.Argument of type 'string' is not assignable to parameter of type '"GET" | "POST"'.
```

在上面的例子中，`req.method` 被推断为 `string`，而不是 `"GET"`。 因为可以在 `req` 的创建和 `handleRequest` 的调用之间评估代码，这可以将一个新的字符串（如 `"GUESS"` 分配给 `req.method`），TypeScript 认为此代码有错误。

有两种方法可以解决这个问题。

1. 你可以通过在任一位置添加类型断言来更改推断：

   ```tsx
   // Change 1:
   const req = { url: "https://example.com", method: "GET" as "GET" };
   // Change 2
   handleRequest(req.url, req.method as "GET");
   ```

   更改 1 表示 “我打算让 `req.method` 始终具有 _ 字面类型 _`"GET"`“，防止之后可能将 `"GUESS"` 分配给该字段。 更改 2 表示 “由于其他原因，我知道 `req.method` 的值为 `"GET"`“。

2. 你可以使用 `as const` 将整个对象转换为类型字面：

   ```tsx
   const req = { url: "https://example.com", method: "GET" } as const;
   handleRequest(req.url, req.method);
   ```

`as const` 后缀的作用类似于 `const`，但用于类型系统，确保为所有属性分配字面类型，而不是更通用的版本，如 `string` 或 `number`。



## `null` 和 `undefined`

JavaScript 有两个原始值用于表示值不存在或未初始化的值： `null` 和 `undefined`。

TypeScript 有两个对应的同名类型。 这些类型的行为取决于你是否启用了 [`strictNullChecks`](https://ts.nodejs.cn/tsconfig#strictNullChecks) 选项。



### `strictNullChecks` 关闭

关闭 [`strictNullChecks`](https://ts.nodejs.cn/tsconfig#strictNullChecks)，可能是 `null` 或 `undefined` 的值仍然可以正常访问，并且值 `null` 和 `undefined` 可以分配给任何类型的属性。 这类似于没有空检查的语言（例如 C#、Java）的行为方式。 缺乏对这些值的检查往往是错误的主要来源； 如果在他们的代码库中这样做是可行的，我们总是建议人们打开 [`strictNullChecks`](https://ts.nodejs.cn/tsconfig#strictNullChecks)。



### `strictNullChecks` 开启

启用 [`strictNullChecks`](https://ts.nodejs.cn/tsconfig#strictNullChecks) 时，当值为 `null` 或 `undefined` 时，你需要在对该值使用方法或属性之前测试这些值。 就像在使用可选属性之前检查 `undefined` 一样，我们可以使用缩小来检查可能是 `null` 的值：

```tsx
function doSomething(x: string | null) {
  if (x === null) {
    // do nothing
  } else {
    console.log("Hello, " + x.toUpperCase());
  }
}Try
```



### 非空断言运算符（后缀 `!`）

TypeScript 还具有一种特殊的语法，可以在不进行任何显式检查的情况下从类型中删除 `null` 和 `undefined`。 在任何表达式之后写 `!` 实际上是一个类型断言，该值不是 `null` 或 `undefined`：

```tsx
function liveDangerously(x?: number | null) {
  // No error
  console.log(x!.toFixed());
}Try
```

就像其他类型断言一样，这不会改变代码的运行时行为，所以当你知道值不能是 `null` 或 `undefined` 时，只使用 `!` 很重要。



## 枚举

枚举是 TypeScript 添加到 JavaScript 的一项功能，它允许描述一个值，该值可能是一组可能的命名常量之一。 与大多数 TypeScript 功能不同，这不是对 JavaScript 的类型级添加，而是添加到语言和运行时的东西。 正因为如此，这是一个你应该知道存在的功能，但除非你确定，否则可能会推迟使用。 你可以在 [枚举参考页](https://ts.nodejs.cn/docs/handbook/enums.html) 中阅读有关枚举的更多信息。



## 不太常见的原语

值得一提的是类型系统中表示的 JavaScript 中的其他原语。 虽然我们不会在这里深入。

#### `bigint`

从 ES2020 开始，JavaScript 中有一个原语用于非常大的整数，`BigInt`：

```tsx
// Creating a bigint via the BigInt function
const oneHundred: bigint = BigInt(100);
 
// Creating a BigInt via the literal syntax
const anotherHundred: bigint = 100n;
```

你可以在 [TypeScript 3.2 发行说明](https://ts.nodejs.cn/docs/handbook/release-notes/typescript-3-2.html#bigint) 中了解有关 BigInt 的更多信息。

#### `symbol`

JavaScript 中有一个原语用于通过函数 `Symbol()` 创建全局唯一引用：

```js
const firstName = Symbol("name");
const secondName = Symbol("name");
 
if (firstName === secondName) {This comparison appears to be unintentional because the types 'typeof firstName' and 'typeof secondName' have no overlap.This comparison appears to be unintentional because the types 'typeof firstName' and 'typeof secondName' have no overlap.
  // Can't ever happen
}
```

# 类型缩小(typeof)

假设我们有一个名为 `padLeft` 的函数。

```
function padLeft(padding: number | string, input: string): string {
  throw new Error("Not implemented yet!");
}Try
```

如果 `padding` 是 `number`，它会将其视为我们想要添加到 `input` 的空格数。 如果 `padding` 是 `string`，它应该只是将 `padding` 前置到 `input`。 让我们尝试实现当 `padLeft` 为 `padding` 传递 `number` 时的逻辑。

```
function padLeft(padding: number | string, input: string) {  return " ".repeat(padding) + input;Argument of type 'string | number' is not assignable to parameter of type 'number'.
  Type 'string' is not assignable to type 'number'.Argument of type 'string | number' is not assignable to parameter of type 'number'.
  Type 'string' is not assignable to type 'number'.}Try
```

哦，我们在 `padding` 上遇到错误。 TypeScript 警告我们，我们正在将类型为 `number | string` 的值传递给 `repeat` 函数，它只接受 `number`，这是正确的。 换句话说，我们没有先明确检查 `padding` 是否是 `number`，也没有处理它是 `string` 的情况，所以让我们这样做。

```tsx
function padLeft(padding: number | string, input: string) {
  if (typeof padding === "number") {
    return " ".repeat(padding) + input;
  }
  return padding + input;
}Try
```

如果这看起来像是无趣的 JavaScript 代码，那就是重点。 除了我们放置的注释之外，这个 TypeScript 代码看起来像 JavaScript。 这个想法是 TypeScript 的类型系统旨在使编写典型的 JavaScript 代码尽可能容易，而无需向后兼容以获得类型安全。

虽然它看起来可能不多，但实际上在幕后发生了很多事情。 就像 TypeScript 如何使用静态类型分析运行时值一样，它在 JavaScript 的运行时控制流结构（如 `if/else`、条件三元组、循环、真实性检查等）上进行类型分析，这些都会影响这些类型。

在我们的 `if` 检查中，TypeScript 看到 `typeof padding === "number"` 并将其理解为一种称为类型保护的特殊形式的代码。 TypeScript 遵循我们的程序可以采用的可能执行路径来分析给定位置的值的最具体的可能类型。 它着眼于这些特殊检查（称为类型保护）和赋值，将类型精炼为比声明的更具体的类型的过程称为缩小。 在许多编辑器中，我们可以观察这些类型的变化，我们甚至会在示例中这样做。

```tsx
function padLeft(padding: number | string, input: string) {
  if (typeof padding === "number") {
    return " ".repeat(padding) + input;
                        
(parameter) padding: number
  }
  return padding + input;
           
(parameter) padding: string
}Try
```

TypeScript 可以理解几种不同的结构来缩小类型。



## `typeof` 类型保护

正如我们所见，JavaScript 支持 `typeof` 运算符，它可以提供关于我们在运行时拥有的值类型的非常基本的信息。 TypeScript 期望它返回一组特定的字符串：

- `"string"`
- `"number"`
- `"bigint"`
- `"boolean"`
- `"symbol"`
- `"undefined"`
- `"object"`
- `"function"`

就像我们在 `padLeft` 中看到的那样，这个运算符经常出现在许多 JavaScript 库中，TypeScript 可以理解它来缩小不同分支中的类型。

在 TypeScript 中，检查 `typeof` 返回的值是一种类型保护。 因为 TypeScript 编码了 `typeof` 如何对不同的值进行操作，所以它知道它在 JavaScript 中的一些怪癖。 例如，请注意在上面的列表中，`typeof` 不返回字符串 `null`。 查看以下示例：

```tsx
function printAll(strs: string | string[] | null) {
  if (typeof strs === "object") {
    for (const s of strs) {'strs' is possibly 'null'.'strs' is possibly 'null'.
      console.log(s);
    }
  } else if (typeof strs === "string") {
    console.log(strs);
  } else {
    // do nothing
  }
}Try
```

在 `printAll` 函数中，我们尝试检查 `strs` 是否为对象以查看它是否为数组类型（现在可能是强化数组是 JavaScript 中的对象类型的好时机）。 但事实证明，在 JavaScript 中，`typeof null` 实际上是 `"object"`！ 这是历史上不幸的事故之一。

有足够经验的用户可能不会感到惊讶，但并不是每个人都在 JavaScript 中遇到过这种情况； 幸运的是，TypeScript 让我们知道 `strs` 只缩小到 `string[] | null` 而不是 `string[]`。

这可能是我们称之为 “truthiness” 检查的一个很好的转义。



# 真实性缩小

真实性可能不是你在字典中可以找到的词，但你会在 JavaScript 中听到很多东西。

在 JavaScript 中，我们可以在条件、`&&`、`||`、`if` 语句、布尔否定 (`!`) 等中使用任何表达式。 例如，`if` 语句不希望它们的条件总是具有 `boolean` 类型。

```tsx
function getUsersOnlineMessage(numUsersOnline: number) {
  if (numUsersOnline) {
    return `There are ${numUsersOnline} online now!`;
  }
  return "Nobody's here. :(";
}Try
```

在 JavaScript 中，像 `if` 这样的构造首先将它们的条件 “coerce” 到 `boolean` 以理解它们，然后根据结果是 `true` 还是 `false` 来选择它们的分支。 像这样的值

- `0`
- `NaN`
- `""` （空字符串）
- `0n` （`bigint` 版本零）
- `null`
- `undefined`

全部强制转换为 `false`，其他值强制转换为 `true`。 你始终可以通过 `Boolean` 函数或使用较短的双布尔否定来将值强制为 `boolean`。 （后者的优点是 TypeScript 推断出一个缩小的字面布尔类型 `true`，而将第一个推断为类型 `boolean`。）

```
// both of these result in 'true'
Boolean("hello"); // type: boolean, value: true
!!"world"; // type: true,    value: trueTry
```

利用这种行为相当流行，尤其是在防范 `null` 或 `undefined` 之类的值时。 例如，让我们尝试将它用于我们的 `printAll` 函数。

```tsx
function printAll(strs: string | string[] | null) {
  if (strs && typeof strs === "object") {
    for (const s of strs) {
      console.log(s);
    }
  } else if (typeof strs === "string") {
    console.log(strs);
  }
}Try
```

你会注意到我们已经通过检查 `strs` 是否为真消除了上面的错误。 这至少可以防止我们在运行以下代码时出现可怕的错误：

```
TypeError: null is not iterable
```

请记住，尽管对原语进行真实性检查通常容易出错。 例如，考虑编写 `printAll` 的不同尝试

```tsx
function printAll(strs: string | string[] | null) {
  // !!!!!!!!!!!!!!!!
  //  DON'T DO THIS!
  //   KEEP READING
  // !!!!!!!!!!!!!!!!
  if (strs) {
    if (typeof strs === "object") {
      for (const s of strs) {
        console.log(s);
      }
    } else if (typeof strs === "string") {
      console.log(strs);
    }
  }
}Try
```

我们将函数的整个主体封装在真实检查中，但这有一个微妙的缺点： 我们可能不再正确处理空字符串的情况。

TypeScript 在这里根本不会伤害我们，但如果你不太熟悉 JavaScript，这种行为就值得注意了。 TypeScript 通常可以帮助你及早发现错误，但如果你选择对值不做任何事情，那么它可以做的事情就只有这么多，而不会过于规范。 如果你愿意，你可以确保使用 linter 处理此类情况。

关于真实性缩小的最后一句话是带有 `!` 的布尔否定从否定分支中过滤掉。

```tsx
function multiplyAll(
  values: number[] | undefined,
  factor: number
): number[] | undefined {
  if (!values) {
    return values;
  } else {
    return values.map((x) => x * factor);
  }
}Try
```



## 相等性缩小

TypeScript 还使用 `switch` 语句和 `===`、`!==`、`==` 和 `!=` 等相等性检查来缩小类型。 例如：

```tsx
function example(x: string | number, y: string | boolean) {
  if (x === y) {
    // We can now call any 'string' method on 'x' or 'y'.
    x.toUpperCase();
          
(method) String.toUpperCase(): string
    y.toLowerCase();
          
(method) String.toLowerCase(): string
  } else {
    console.log(x);
               
(parameter) x: string | number
    console.log(y);
               
(parameter) y: string | boolean
  }
}Try
```

当我们在上面的示例中检查 `x` 和 `y` 是否相等时，TypeScript 知道它们的类型也必须相等。 由于 `string` 是 `x` 和 `y` 都可以采用的唯一常见类型，TypeScript 知道 `x` 和 `y` 在第一个分支中必须是 `string`。

检查特定的字面值（而不是变量）也可以。 在我们关于真实性缩小的部分中，我们编写了一个容易出错的 `printAll` 函数，因为它意外地没有正确处理空字符串。 相反，我们可以做一个特定的检查来阻止 `null`，TypeScript 仍然正确地从 `strs` 的类型中删除 `null`。

```
function printAll(strs: string | string[] | null) {
  if (strs !== null) {
    if (typeof strs === "object") {
      for (const s of strs) {
                       
(parameter) strs: string[]
        console.log(s);
      }
    } else if (typeof strs === "string") {
      console.log(strs);
                   
(parameter) strs: string
    }
  }
}Try
```

JavaScript 对 `==` 和 `!=` 的更宽松的相等性检查也正确地缩小了类型。 如果你不熟悉，检查某事 `== null` 是否实际上不仅检查它是否具体是值 `null` - 它还检查它是否可能是 `undefined`。 这同样适用于 `== undefined`： 它检查一个值是 `null` 还是 `undefined`。

```
interface Container {
  value: number | null | undefined;
}
 
function multiplyValue(container: Container, factor: number) {
  // Remove both 'null' and 'undefined' from the type.
  if (container.value != null) {
    console.log(container.value);
                           
(property) Container.value: number
 
    // Now we can safely multiply 'container.value'.
    container.value *= factor;
  }
}Try
```



## `in` 运算符缩小

JavaScript 有一个运算符来确定对象或其原型链是否具有名称属性： `in` 运算符。 TypeScript 将这一点视为缩小潜在类型的一种方式。

例如，使用代码： `"value" in x`。 其中 `"value"` 是字符串字面，`x` 是联合类型。 “true” 分支缩小了 `x` 具有可选或必需属性 `value` 的类型，而 “false” 分支缩小了具有可选或缺少属性 `value` 的类型。

```tsx
type Fish = { swim: () => void };
type Bird = { fly: () => void };
 
function move(animal: Fish | Bird) {
  if ("swim" in animal) {
    return animal.swim();
  }
 
  return animal.fly();
}
```

重申一下，可选属性将存在于两侧以进行缩小。 例如，一个人可以游泳和飞行（使用合适的设备），因此应该出现在 `in` 检查的两侧：

```tsx
type Fish = { swim: () => void };
type Bird = { fly: () => void };
type Human = { swim?: () => void; fly?: () => void };
 
function move(animal: Fish | Bird | Human) {
  if ("swim" in animal) {
    animal;
      
(parameter) animal: Fish | Human
  } else {
    animal;
      
(parameter) animal: Bird | Human
  }
}Try
```



## `instanceof` 缩小

JavaScript 有一个运算符用于检查一个值是否是另一个值的 “instance”。 更具体地说，在 JavaScript 中，`x instanceof Foo` 检查 `x` 的原型链是否包含 `Foo.prototype`。 虽然我们不会在这里深入探讨，并且当我们进入类时你会看到更多内容，但它们对于可以使用 `new` 构造的大多数值仍然很有用。 你可能已经猜到了，`instanceof` 也是一个类型保护，TypeScript 缩小了由 `instanceof` 保护的分支。

```tsx
function logValue(x: Date | string) {
  if (x instanceof Date) {
    console.log(x.toUTCString());
               
(parameter) x: Date
  } else {
    console.log(x.toUpperCase());
               
(parameter) x: string
  }
}Try
```



## 赋值

正如我们前面提到的，当我们为任何变量赋值时，TypeScript 会查看赋值的右侧并适当地缩小左侧。

```tsx
let x = Math.random() < 0.5 ? 10 : "hello world!";
   
let x: string | number
x = 1;
 
console.log(x);
           
let x: number
x = "goodbye!";
 
console.log(x);
           
let x: stringTry
```

请注意，这些分配中的每一个都是有效的。 即使在我们第一次分配后观察到的 `x` 类型更改为 `number`，我们仍然能够将 `string` 分配给 `x`。 这是因为 `x` 的声明类型 - `x` 开始的类型 - 是 `string | number`，并且始终根据声明的类型检查可分配性。

如果我们将 `boolean` 分配给 `x`，我们会看到一个错误，因为它不是声明类型的一部分。

```tsx
let x = Math.random() < 0.5 ? 10 : "hello world!";
   
let x: string | number
x = 1;
 
console.log(x);
           
let x: number
x = true;Type 'boolean' is not assignable to type 'string | number'.Type 'boolean' is not assignable to type 'string | number'.
 
console.log(x);
           
let x: string | numberTry
```



## 控制流分析

到目前为止，我们已经通过一些基本示例来了解 TypeScript 如何在特定分支中缩小类型。 但是除了从每个变量中走出来并在 `if`、`while`、条件等中寻找类型保护之外，还有更多的事情要做。例如

```tsx
function padLeft(padding: number | string, input: string) {
  if (typeof padding === "number") {
    return " ".repeat(padding) + input;
  }
  return padding + input;
}Try
```

`padLeft` 从其第一个 `if` 块内返回。 TypeScript 能够分析此代码并发现在 `padding` 是 `number` 的情况下，正文的其余部分 (`return padding + input;`) 是不可访问的。 结果，它能够从 `padding` 的类型中删除 `number`（从 `string | number` 缩小到 `string`）以用于其余的功能。

这种基于可达性的代码分析称为控制流分析，TypeScript 在遇到类型保护和赋值时使用这种流分析来缩小类型。 当分析一个变量时，控制流可以一次又一次地分裂和重新合并，并且可以观察到该变量在每个点具有不同的类型。

```tsx
function example() {
  let x: string | number | boolean;
 
  x = Math.random() < 0.5;
 
  console.log(x);
             
let x: boolean
 
  if (Math.random() < 0.5) {
    x = "hello";
    console.log(x);
               
let x: string
  } else {
    x = 100;
    console.log(x);
               
let x: number
  }
 
  return x;
        
let x: string | number
}Try
```



## 使用类型谓词

到目前为止，我们已经使用现有的 JavaScript 结构来处理类型缩小，但是有时你希望更直接地控制类型在整个代码中的变化方式。

要定义用户定义的类型保护，我们只需要定义一个返回类型为类型谓词的函数：

```
function isFish(pet: Fish | Bird): pet is Fish {
  return (pet as Fish).swim !== undefined;
}Try
```

`pet is Fish` 是本例中的类型谓词。 谓词采用 `parameterName is Type` 的形式，其中 `parameterName` 必须是当前函数签名中的参数名称。

任何时候使用某个变量调用 `isFish` 时，如果原始类型兼容，TypeScript 就会将该变量缩小到该特定类型。

```
// Both calls to 'swim' and 'fly' are now okay.
let pet = getSmallPet();
 
if (isFish(pet)) {
  pet.swim();
} else {
  pet.fly();
}Try
```

请注意，TypeScript 不仅知道 `pet` 是 `if` 分支中的 `Fish`； 它还知道在 `else` 分支中，你没有 `Fish`，所以你必须有 `Bird`。

你可以使用类型保护 `isFish` 过滤 `Fish | Bird` 的数组并获得 `Fish` 的数组：

```
const zoo: (Fish | Bird)[] = [getSmallPet(), getSmallPet(), getSmallPet()];
const underWater1: Fish[] = zoo.filter(isFish);
// or, equivalently
const underWater2: Fish[] = zoo.filter(isFish) as Fish[];
 
// The predicate may need repeating for more complex examples
const underWater3: Fish[] = zoo.filter((pet): pet is Fish => {
  if (pet.name === "sharkey") return false;
  return isFish(pet);
});Try
```

另外，类可以 [使用 `this is Type`](https://ts.nodejs.cn/docs/handbook/2/classes.html#this-based-type-guards) 来缩小他们的类型。



## 断言函数

也可以使用 [断言函数](https://ts.nodejs.cn/docs/handbook/release-notes/typescript-3-7.html#assertion-functions) 缩小类型。



# 判别联合

到目前为止，我们看到的大多数示例都集中在使用简单类型（如 `string`、`boolean` 和 `number`）来缩小单个变量的作用域。 虽然这很常见，但大多数时候在 JavaScript 中我们将处理稍微复杂的结构。

出于某种动机，假设我们正在尝试对圆形和正方形等形状进行编码。 圆记录它们的半径，正方形记录它们的边长。 我们将使用一个名为 `kind` 的字段来判断我们正在处理的形状。 这是定义 `Shape` 的第一次尝试。

```
interface Shape {
  kind: "circle" | "square";
  radius?: number;
  sideLength?: number;
}Try
```

请注意，我们使用的是字符串字面类型的联合： `"circle"` 和 `"square"` 分别告诉我们应该将形状视为圆形还是方形。 通过使用 `"circle" | "square"` 而不是 `string`，我们可以避免拼写错误的问题。

```
function handleShape(shape: Shape) {
  // oops!
  if (shape.kind === "rect") {This comparison appears to be unintentional because the types '"circle" | "square"' and '"rect"' have no overlap.This comparison appears to be unintentional because the types '"circle" | "square"' and '"rect"' have no overlap.
    // ...
  }
}Try
```

我们可以编写一个 `getArea` 函数，根据它是处理圆形还是正方形来应用正确的逻辑。 我们将首先尝试处理圈子。

```
function getArea(shape: Shape) {
  return Math.PI * shape.radius ** 2;'shape.radius' is possibly 'undefined'.'shape.radius' is possibly 'undefined'.
}Try
```

在 [`strictNullChecks`](https://ts.nodejs.cn/tsconfig#strictNullChecks) 下给我们一个错误 - 这是适当的，因为 `radius` 可能没有定义。 但是如果我们对 `kind` 属性进行适当的检查呢？

```
function getArea(shape: Shape) {
  if (shape.kind === "circle") {
    return Math.PI * shape.radius ** 2;'shape.radius' is possibly 'undefined'.'shape.radius' is possibly 'undefined'.
  }
}Try
```

嗯，TypeScript 还是不知道在这里做什么。 我们已经达到了比类型检查器更了解我们的值的地步。 我们可以尝试使用非空断言（`shape.radius` 之后的 `!`）来表示 `radius` 肯定存在。

```
function getArea(shape: Shape) {
  if (shape.kind === "circle") {
    return Math.PI * shape.radius! ** 2;
  }
}Try
```

但这感觉并不理想。 我们不得不用那些非空断言（`!`）对类型检查器大喊大叫，以说服它定义了 `shape.radius`，但是如果我们开始移动代码，这些断言很容易出错。 此外，在 [`strictNullChecks`](https://ts.nodejs.cn/tsconfig#strictNullChecks) 之外，我们无论如何都可以意外访问这些字段中的任何一个（因为在读取它们时假定可选属性始终存在）。 我们绝对可以做得更好。

这种 `Shape` 编码的问题在于，类型检查器无法根据 `kind` 属性知道是否存在 `radius` 或 `sideLength`。 我们需要将我们所知道的信息传达给类型检查器。 考虑到这一点，让我们再次定义 `Shape`。

```
interface Circle {
  kind: "circle";
  radius: number;
}
 
interface Square {
  kind: "square";
  sideLength: number;
}
 
type Shape = Circle | Square;Try
```

在这里，我们已经正确地将 `Shape` 分成了 `kind` 属性具有不同值的两种类型，但是 `radius` 和 `sideLength` 在它们各自的类型中被声明为必需的属性。

让我们看看当我们尝试访问 `Shape` 的 `radius` 时会发生什么。

```
function getArea(shape: Shape) {  return Math.PI * shape.radius ** 2;Property 'radius' does not exist on type 'Shape'.
  Property 'radius' does not exist on type 'Square'.Property 'radius' does not exist on type 'Shape'.
  Property 'radius' does not exist on type 'Square'.}Try
```

就像我们对 `Shape` 的第一个定义一样，这仍然是一个错误。 当 `radius` 是可选的时，我们得到一个错误（启用 [`strictNullChecks`](https://ts.nodejs.cn/tsconfig#strictNullChecks)），因为 TypeScript 无法判断该属性是否存在。 现在 `Shape` 是一个联合，TypeScript 告诉我们 `shape` 可能是一个 `Square`，而 `Square` 上没有定义 `radius`！ 两种解释都是正确的，但是无论 [`strictNullChecks`](https://ts.nodejs.cn/tsconfig#strictNullChecks) 是如何配置的，只有 `Shape` 的联合编码会导致错误。

但是，如果我们再次尝试检查 `kind` 属性会怎样？

```
function getArea(shape: Shape) {
  if (shape.kind === "circle") {
    return Math.PI * shape.radius ** 2;
                      
(parameter) shape: Circle
  }
}Try
```

这摆脱了错误！ 当联合中的每个类型都包含具有字面类型的公共属性时，TypeScript 认为这是一个可区分的联合，并且可以缩小联合的成员。

在这种情况下，`kind` 是该公共属性（这被认为是 `Shape` 的判别属性）。 检查 `kind` 属性是否为 `"circle"` 删除了 `Shape` 中没有 `"circle"` 类型的 `kind` 属性的所有类型。 这将 `shape` 缩小到 `Circle` 类型。

同样的检查也适用于 `switch` 语句。 现在我们可以尝试编写完整的 `getArea` 而不需要任何讨厌的 `!` 非空断言。

```
function getArea(shape: Shape) {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
                        
(parameter) shape: Circle
    case "square":
      return shape.sideLength ** 2;
              
(parameter) shape: Square
  }
}Try
```

这里重要的是 `Shape` 的编码。 向 TypeScript 传达正确的信息 - `Circle` 和 `Square` 实际上是具有特定 `kind` 字段的两种不同类型 - 至关重要。 这样做可以让我们编写类型安全的 TypeScript 代码，看起来与我们以其他方式编写的 JavaScript 没有什么不同。 从那里，类型系统能够做 “right” 的事情并找出我们 `switch` 语句的每个分支中的类型。

> 顺便说一句，尝试使用上面的示例并删除一些返回关键字。 你会看到类型检查有助于避免在 `switch` 语句中意外遇到不同子句时出现错误。

判别联合不仅仅用于讨论圆形和正方形。 它们非常适合在 JavaScript 中表示任何类型的消息传递方案，例如通过网络发送消息（客户端/服务器通信）或在状态管理框架中编码突变。



# `never` 类型

缩小类型时，你可以将联合的选项减少到你已消除所有可能性并且一无所有的程度。 在这些情况下，TypeScript 将使用 `never` 类型来表示不应该存在的状态。



# 穷举检查

`never` 类型可分配给每个类型； 但是，没有类型可分配给 `never`（`never` 本身除外）。 这意味着你可以使用缩小范围并依靠出现的 `never` 在 `switch` 语句中进行详尽检查。

例如，将 `default` 添加到我们的 `getArea` 函数中，尝试将形状分配给 `never`，当处理完所有可能的情况时，不会引发错误。

```
type Shape = Circle | Square;
 
function getArea(shape: Shape) {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.sideLength ** 2;
    default:
      const _exhaustiveCheck: never = shape;
      return _exhaustiveCheck;
  }
}Try
```

向 `Shape` 联合添加新成员，将导致 TypeScript 错误：

```
interface Triangle {
  kind: "triangle";
  sideLength: number;
}
 
type Shape = Circle | Square | Triangle;
 
function getArea(shape: Shape) {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.sideLength ** 2;
    default:
      const _exhaustiveCheck: never = shape;Type 'Triangle' is not assignable to type 'never'.Type 'Triangle' is not assignable to type 'never'.
      return _exhaustiveCheck;
  }
}
```