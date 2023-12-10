Obsidian使用数学公式方法

小提示：本篇文章约1800字，大约需8分钟阅读。

对于数学、物理、计算机的学生和工作者来说，笔记中参杂着公式是再正常不过的事情了。

以前的做法是在本地安装全套的 latex 写作环境，如 TeXLive。或者是在线上的 latex 环境写作：\[OverLeaf\]([https://www.overleaf.com/](https://link.zhihu.com/?target=https%3A//www.overleaf.com/))

在 latex 环境中写作时，**往往要兼顾内容和排版**，会使用大量与内容无关的标记，去控制内容在编译出的 pdf 文件中表现的形式，如字体、符号、间距、方框等等。

Markdown 或许是一个更适合记录相关笔记的载体。

我们应秉持 **内容和表现分开**的原则，先利用 Markdown 快速写下所有内容，有了内容后，再去为了出版、投刊的目的实现复杂的排版。

Markdown 支持 latex 语法，只要记笔记的人熟悉 latex 语法，就可以在当前笔记中渲染出复杂的公式。

成对的 \`$\` 代表内联公式，里面内容将会渲染在行中，与文字混合出现，一般用来记录数学符号或简短的公式。如 $a$、$e^{2i\\pi}=1$。它们将会被渲染为：

![](https://pic2.zhimg.com/80/v2-33a619505ae9b346625668eb6eb923dd_1440w.webp)

而成对的 \`$$\` 代表公式块，渲染的公式将单独占据一个自然段，如：

    $$\begin{vmatrix}a & b\\ c & d \end{vmatrix}=ad-bc$$

它将会被渲染为：

![](https://pic1.zhimg.com/80/v2-480d6abdc15eb8dee2eeb262b8cdc70c_1440w.webp)

更多可以在 Markdown 中使用的 latex 语法可参考：\[Cmd Markdown 公式指导手册 - 作业部落 Cmd Markdown 编辑阅读器\]([https://www.zybuluo.com/codeep/note/163962](https://link.zhihu.com/?target=https%3A//www.zybuluo.com/codeep/note/163962))

可能很多人和我以前一样，选择了 typora 来记录 Markdown 笔记，但是出于以下的考虑，我切换到了 Obsidian。

1\. 逻辑链路

2\. 相关插件

**逻辑链路**
--------

Typora 是文档类型 Markdown 编辑器，每份文档都相对分离。

但是知识并不是分离的，它是具有相关和因果等逻辑关系的，对于理科类比较讲究逻辑的学科来说，一个能够记录完备的知识体系的笔记软件能发挥更大的作用。

对于 Obsidian，我已经写了很多介绍，可以看看：[Obsidian画的饼，正在一步步实现](https://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzkzMDAwMTA4MA%3D%3D%26mid%3D2247484047%26idx%3D1%26sn%3D711a4e04629b8adbcaef6d9ccf9cec76%26chksm%3Dc201bb58f576324e16ad9b9b2a1867d8d620ff784424efde19670869ab7a8e9b7293dafddab2%26scene%3D21%23wechat_redirect)

**相关插件**
--------

Obsidian 自由的插件市场，可以为输入 latex 公式带来很多便利。

以下介绍两个与 latex 相关的插件

1\. templater

2\. Latex suite

### Templater

配合 Obsidian-templater 插件，我们可以快速输入固定的公式。

首先按照 [打开插件世界大门，看看Obsidian小白之友带来的丝滑编辑体验](https://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzkzMDAwMTA4MA%3D%3D%26mid%3D2247484186%26idx%3D1%26sn%3D1d4599f6fd155d8f26f6cccdabb40b09%26chksm%3Dc201bacdf57633dbfe9a7a19a048032452ea87504ae4dd383ee1f7fcf1cc9f05968d9cc1dc27%26scene%3D21%23wechat_redirect)介绍，在插件市场安装好 Obsidian-templater 插件。

提示：如果安装插件有问题，可以参考：[安装obsidian插件的多种方式大汇总](https://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzkzMDAwMTA4MA%3D%3D%26mid%3D2247484290%26idx%3D1%26sn%3D26b37149763e7e439181bdaa2092c32b%26chksm%3Dc201ba55f57633432e0342546e2a2f2fa838694dde1d08675160f86b49e1eb9c855effed5ef1%26scene%3D21%23wechat_redirect)。

安装好 Obsidian-templater 后，先不急着用，我们要进行基本的设置。

打开 Templater 的插件设置页面，只设置「Teplate folder location」选项，该选项确定了「模版」被放置的文件夹，一般我会将该文件夹命名为「Z-templates」。

![](https://pic2.zhimg.com/80/v2-eb8d97053560ee038a99de770391d311_1440w.webp)

Templater 是一个强大却复杂的插件，后续我会以一个个案例的形式逐渐讲解它所涉及的语法和用途，敬请期待。

我们在本篇可以只关注它的「插入模版」功能。「模版」即是之前设置的「Z-templates」下的文件，为了以后与其他类型的模版区分开，我还在其下建立了「math」的目录夹：



![](https://pic2.zhimg.com/80/v2-ada651812c7e41c44fa434f2efbbf67d_1440w.webp)

在 math 目录夹下我建立了两个公式的内容，来看一下其中的泰勒公式：



![](https://pic3.zhimg.com/80/v2-92b972bddfcbdb8ba09a91cb250e7806_1440w.webp)

可以看到该条公式比较长，如果平时都是自己手动录入的话，未免需要花费太多时间，然而只要我们将它建立好，放入「Z-templates」，以后就能通过「插入模版」功能快速插入该条公式。我们先新建一个「Templater 演示」的笔记，并打开它。然后，在「命令面板」中搜索关键字 templater，可以调用该功能和看到它的快捷键。

![](https://pic1.zhimg.com/80/v2-bea6b97c2bfbf0656b28c6057e59d178_1440w.webp)

「Enter」键确认调用该功能后，将会出现模版的选择对话框，这个对话框中将会显示所有在「Z-templates」文件夹下的文件名称。在该对话框中可以再次输入模版的「文件名」来筛选出具体的模版：

![](https://pic1.zhimg.com/80/v2-87437c1956557dd45caedceaf2756eec_1440w.webp)

让我们来选择「泰勒公式」：

![](https://pic4.zhimg.com/v2-5c65ceb5dac55d4f609ecbfc1595c96b_b.jpg)

可以看到在当前已打开的「Templater 演示」笔记中被填充了与「泰勒公式」一模一样的内容！

利用该功能就能 **将常用的公式封装起来**，避免每次重新录入公式，节约记录笔记的时间，将时间留给思考和更有意义的工作。

### Latex suite

Templater 带来的插入整块内容的便利，而 Latex suite 插件带来的是在录入公式时的便利。比如，我们通过输入：

    xsr

就能在 \`$\` 和 \`$$\` 公式块中转化为

    x^{2}

Latex suite 允许通过使用自定义片段，快速输入公式。

与 Templater 相比，这其实就是更细粒度的复用了自己封装的公式片段。

Latex suite 的语法可以参考以下内容：

1\. **cuman 大佬写的介绍**：[https://pkmer.cn/Pkmer-Docs/10-Obsidian/Obsidian%E7%A4%BE%E5%8C%BA%E6%8F%92%E4%BB%B6/Obsidian-latex-suite/](https://link.zhihu.com/?target=https%3A//pkmer.cn/Pkmer-Docs/10-Obsidian/Obsidian%25E7%25A4%25BE%25E5%258C%25BA%25E6%258F%2592%25E4%25BB%25B6/Obsidian-latex-suite/)

2.**Latex suite源代码及其介绍**：[https://github.com/artisticat1/Obsidian-latex-suite](https://link.zhihu.com/?target=https%3A//github.com/artisticat1/Obsidian-latex-suite)

**最后**
------

希望以上介绍能对你有所帮助和启发！

本文转自 <https://zhuanlan.zhihu.com/p/637380702>，如有侵权，请联系删除。