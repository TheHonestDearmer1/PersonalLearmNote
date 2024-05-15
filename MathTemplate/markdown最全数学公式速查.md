 

markdown最全数学公式
--------------

我们在用markdown写文档时有时候少不了需要插入一些公式，然而markdown公式输入远没有word这么直观，有很多复杂的格式和符号的英语缩写需要记忆，经常是刚用完，过几天不用又都忘记了，因此在这里将数学公式的[Latex](https://so.csdn.net/so/search?q=Latex&spm=1001.2101.3001.7020)编辑方式做一个整理，以方便自己和读者今后使用。

**分数，平方**

| 算式 | markdown |
| --- | --- |
| $\frac{7x+5}{1+y^2}$ | \\frac{7x+5}{1+y^2} |

**下标**

| 算式 | markdown |
| --- | --- |
| $z=z_l$ | z=z\_l |

**省略号**

| 省略号 | markdown |
| --- | --- |
| $\cdots$ | \\cdots |

**点乘**

| 点乘    | markdown |
| ------- | -------- |
| $\cdot$ | \cdot    |

**行间公式（使用两个$包含公式可以独立一行）**

| 行间公式 | markdown |
| --- | --- |
| $\frac{d}{dx}e^{ax}=ae^{ax}\quad \sum_{i=1}^{n}{(X_i - \overline{X})^2}$ | `$\frac{d}{dx}e^{ax}=ae^{ax}\quad \sum_{i=1}^{n}{(X_i - \overline{X})^2}$` |

**开根号**

| 算式 | markdown |
| --- | --- |
| $\sqrt{2};\sqrt[n]{3}$ | \\sqrt{2};\\sqrt\[n\]{3} |

**矢量**

|                           |                            |
| --- | --- |
| $\vec{a} \cdot \vec{b}=0$ | \\vec{a} \\cdot \\vec{b}=0 |

**微积分**

| 算式 | markdown |
| --- | --- |
| $\int ^2\_3 x^2 {\\rm d}x$ | \\int ^2\_3 x^2 {\\rm d}x |
| $\iint$ | \\iint |
| ∭∭ | \\iiint |
| ∮∮ | \\oint |
| $\oint$ | \\oint |
| $\mathrm{d}$ | \\mathrm{d} |
| $\prime$ | \\p |
| $\lim$ | \lim |
| $\infty$ | \infty |
| $\partial$ | \partial |
| ∂f(x,y)∂x∣∣x\=0∂f(x,y)∂x|x\=0\\left.\\frac{\\partial f(x,y)}{\\partial x}\\right|
| ∑∑\\sum | \\sum |

**极限**

| 算式 | markdown |
| --- | --- |
| $\lim_{n\rightarrow+\infty} n$ | \\lim\_{n\\rightarrow+\\infty} n |

**累加**

| 算式 | markdown |
| --- | --- |
| $\sum \frac{1}{i^2}$ | \\sum \\frac{1}{i^2} |

**累乘**

| 算式 | markdown |
| --- | --- |
| $\prod \frac{1}{i^2}$ | \\prod \\frac{1}{i^2} |

**给公式编号，如: (1)**  
`$$e^{i\theta}=cos\theta+\sin\theta i\tag{1}$$`  

$$e^{i\theta}=cos\theta+\sin\theta i\tag{1}$$

$e^{i\theta}=cos\theta+i\sin\theta\tag{1}$ 
**矩阵**

    $$
    \begin{matrix}
    1 & 2 & 3 \\
    4 & 5 & 6 \\
    7 & 8 & 9 
    \end{matrix} \tag{1}
    $$

$$
\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 
\end{matrix} \tag{1}
$$
**带括号的矩阵**

    $$
    \left[
    \begin{matrix}
    1 & 2 & 3 \\
    4 & 5 & 6 \\
    7 & 8 & 9 
    \end{matrix} \right]\tag{2}
    $$

$$
\left[
\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 
\end{matrix} \right]\tag{2}
$$

| 符号 | 形式 |
| --- | --- |
| pmatrix | (1324) |
| bmatrix | \[1324\] |
| Bmatrix | {1324} |
| vmatrix | |1324||1324|\\begin{vmatrix}1&3&2&4\\end{vmatrix} |
| Vmatrix | ||1 3 2 4|| |

**希腊字母**

| 大写 | markdown | 小写 | markdown |
| --- | --- | --- | --- |
| A | A | α | \\alpha |
| B | B | β | \\beta |
| Γ | \\Gamma | γ | \\gamma |
| Δ | \\Delta | δ | \\delta |
| E | E | ϵ | \\epsilon |
|  |  | ε | \\varepsilon |
| Z | Z | ζ | \\zeta |
| H | H | η | \\eta |
| Θ | \\Theta | θ | \\theta |
| I | I | ι | \\iota |
| K | K | κ | \\kappa |
| Λ | \\Lambda | λ | \\lambda |
| M | M | μ | \\mu |
| N | N | ν | \\nu |
| Ξ | \\Xi | ξ | \\xi |
| O | O | ο | \\omicron |
| Π | \\Pi | π | \\pi |
| P | P | ρ | \\rho |
| Σ | \\Sigma | σ | \\sigma |

| 大写 | markdown | 小写 | markdown |
| --- | --- | --- | --- |
| T | T | τ | \\tau |
| Υ | \\Upsilon | υ | \\upsilon |
| Φ | \\Phi | ϕ | \\phi |
|  |  | φ | \\varphi |
| X | X | χ | \\chi |
| Ψ | \\Psi | ψ | \\psi |
| Ω | \\Omega | ω | \\omega |

**三角函数**

| 三角函数 | markdown |
| --- | --- |
| sin | \\sin |

**对数函数**

**对数函数**

| 算式 | ma |
| --- | --- |
| $\ln15$ | \\ln15 |
| $\log2^{10}$ | \\log\_2^{10} |
| $\lg7$ | \\lg7 |

**关系运算符**

| 运算符 | markdown |
| --- | --- |
| ± | \pm |
| × | \\times |
| ÷ | \\div |
| ∑ | \\sum |
| ∏ | \\prod |
| ≠ | \\neq |
| ≤ | \\leq |
| ≥ | \\geq |
| $ \approx$ | \approx |

**括号**

| 运算符 | markdown |
| --- | --- |
| 大括号: {a+x} | \\lbrace a+x \\rbrace |
| 尖括号: $\langle x \rangle$ | \\langle x \\rangle |
| 上取整:$\lceil \frac{x}{2} \rceil$ | \\lceil \\frac{x}{2} \\rceil |
| 下取整: $\lfloor x \rfloor$ | \\lfloor x \\rfloor |
| 原始括号:$\lbrace\sum\_{i=0}^{n}    i^{2}=\frac{2a}{x^2+1} \rbrace$ | \\lbrace \\sum\_{i=0}^{n}i^{2}=\\frac{2a}{x^2+1} \\rbrace |
| 全包括号:$\left\lbrace \sum\_{i=0}^{n}i^{2}=\frac{2a}{x^2+1} \right\rbrace$ | \\left\\lbrace \\sum\_{i=0}^{n}i^{2}=\\frac{2a}{x^2+1} \\right\\rbrace |

**单边大括号**

```
 f(x)=\left\{
\begin{aligned}
x & =  \cos(t) \\
y & =  \sin(t) \\
z & =  \frac xy
\end{aligned}
\right.
```


$$
 f(x)=\left\{
\begin{aligned}
x & =  \cos(t) \\
y & =  \sin(t) \\
z & =  \frac xy
\end{aligned}
\right.
$$
**后续添加更新中**

文章知识点与官方知识档案匹配，可进一步学习相关知识

[CS入门技能树](https://edu.csdn.net/skill/gml/gml-e67e64c1c880432ab6bc1b0452124ec0?utm_source=csdn_ai_skill_tree_blog)[MarkDown入门](https://edu.csdn.net/skill/gml/gml-e67e64c1c880432ab6bc1b0452124ec0?utm_source=csdn_ai_skill_tree_blog)[MarkDown介绍](https://edu.csdn.net/skill/gml/gml-e67e64c1c880432ab6bc1b0452124ec0?utm_source=csdn_ai_skill_tree_blog)35993 人正在系统学习中

