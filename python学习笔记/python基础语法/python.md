# **Python 基础语法**

## 输出

```python
# 1. 基础操作
age = 20
print(age)
print(1 + 1)
print('Hello world!')
```

## if语句

```
# 2. 条件判断if
if 1 == 2: # 如果 if 跟随的条件为 假 则不执行 if 的语句，然后寻找 else 语句执行
    print("假的")
else: 
    print("1 == 2 是假的")
```

## for语句

```
# 3. 循环操作---for
for i in range(2,5):
    print(i)
```

## while语句

```
# 3. 循环操作---while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)
```

## break语句

```
# 4. break、continue、pass
# break语句可以跳出 for and while 的循环体
n = 1
while n <= 100:
    if n > 10:
        break
    print (n)
    n += 1
```

## continue语句

```
# continue语句跳过当前循环，直接进行下一个循环
n = 1
while n <= 10:
    n  = n + 1
    if n % 2 == 0:
        continue
    print(n)
```

## pass语句

```
# pass是空语句，一般用作占位语句，不能做任何事情
for letter in 'Room':
    if letter == 'o':
        pass
        print('pass')
    print(letter)
```

## 数据类型Number

```
# 5. 数据类型---Number(数字)
# Python支持 int，float，complex三种不同的数据类型
a = 3
b = 3.14
c = 3 + 4j
print(type(a),type(b),type(c))
```

## 数据类型String

```
# 5. 数据类型---String(字符串)
# 支持字符串拼接、截取等多种运算
a = "Hello"
b = "Python"
# 拼接
print("a + b 输出结果：", a + b)
# 截取,[]左闭右开
print("a[1:4] 输出结果：", a[1:4])
```

## 数据类型List

```
# 5. 数据类型---List（列表）
# 列表是写在方括号之间[]之间、用逗号分隔开的元素列表
# 列表索引值以 0 为开始值，-1 为末尾的开始值
list = ['abcd', 786 , 2.23 , 'runoob', 70.2]
#print(list[1:3])
tinylist = [123,'runoob']
print(list + tinylist)
```

## 数据类型set

```
# 5. 数据类型---set（集合）,常用作去重操作
# set 与 dict 类似，也是一组key的集合，但不存储value。由于key不能重复，所以不可重复
# set是无序的，重复元素在set中自动过滤。
s = set([1, 1, 2, 2, 3, 3])
print(s)
```

# **Python 进阶**

# 数字

Python Number数据类型用于存储数值，包括整型，长整型，浮点型，复数

**(1)Python Number 模块：** Python中数学运算常用的函数基本都在math模块

In [5]

```
import math
print(math.ceil(4.1))  # 返回数字的上入整数，5
print(math.floor(4.9))  # 返回数字的下舍整数，4
print(math.fabs(-10))  # 返回数字的绝对值，10
print(math.sqrt(9))  # 返回数字的正平方根，3
print(math.exp(2))  # 返回e的2次幂
```

**（2）Python随机数**

首先import random，使用random（）方法即可随之生成一个[0,1)范围内的实数

In [10]

```
import random
ran = random.random()
print(ran)
```

调用random.random()生成随机数时，每一次生成的数是随机的。但是，预先使用random.seed(x)设定好种子之后，其中的x可以是任意数字，此时使用random（）生成的随机数将会是同一个。

In [14]

```
print("------- 设置种子 seed -------")
random.seed(10)
print("Random number with seed 10 : ", random.random())

# 生成同一个随机数
random.seed(10)
print("Random number with seed 10 : ", random.random())
```

randint()生成一个随机整数

In [17]

```
ran = random.randint(1,20)
print(ran)
```

# 字符串

字符串连接：+

In [18]

```
a = "Hello "
b = "World "
print(a + b)
```

重复输出字符串：*

In [20]

```
print(a * 3)
```

通过索引获取字符串中字符[]

In [21]

```
print(a[0])
```

字符串截取[:] 牢记：左开右闭

In [23]

```
print(a[1:4])
```

判断字符串中是否包含给定的字符：in/not in

In [24]

```
print('e' in a)
print('e' not in a)
```

join():以字符作为分隔符，将字符串中所有的元素合并为一个新的字符串

In [25]

```
new_str = '-'.join('Hello')
print(new_str)
```

字符串单引号，双引号，三引号

In [26]

```
print('Hello World!')
print("Hello World!")
```

转义字符\

In [27]

```
print("The \t is a tab")
print('I\'m going to the movies')
```

三引号可以用来规避引号和特殊字符串的冲突，所见即所得

In [28]

```
print('''I'm going to the movies''')
```

# 列表（数组）

作用；类似其他语言中的数组

声明一个列表，并通过下标或索引获得元素

| 正向 | 0    | 1    | 2    | 3    | 4    |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 反向 | -5   | -4   | -3   | -2   | -1   |

In [29]

```
# 声明一个列表
names = ['jack','tom','tonney','superman','jey']

# 通过下标或索引获取元素
print(names[0])
print(names[1])
```

In [30]

```
# 获取最后一个元素
print(names[-1])
print(names[len(names)-1])
```

In [34]

```
# 获取第一个元素
print(names[0])
print(names[-5])
```

In [35]

```
# 遍历列表，获取元素
for name in names:
    print(name)
```

In [39]

```
# 查询names里是否有某个元素
for name in names:
    if name == 'superman':
        print('有')
        break
else:
    print('没有')  
```

In [40]

```
# 另一种方法查询names里是否有某个元素
if 'superman' in names:
    print('有')
else:
    print('没有')
```

列表元素添加

In [42]

```
# 声明一个空列表
girls =[]

# append()，末尾追加
girls.append('宁静')
print(girls)
```

In [43]

```
# extend()，一次添加多个，把一个列表添加到另一个列表，列表合并
models = ['刘雯','雎晓雯']
girls.extend(models)
# girls = girls + models
print(girls)
```

In [44]

```
# insert():指定位置添加
girls.insert(1,'虞书欣')
print(girls)
```

列表元素修改，通过下标找到元素，然后用=赋值

In [48]

```
fruits = ['apple','pear','pineapple','banana','草莓']
print(fruits)

fruits[-1] = 'strawberry'
print(fruits)
```

In [51]

```
# 将fruits 列表中的‘香蕉’替换为‘banana’
for i in range (len(fruits)):
    if 'banana' in fruits[i]:
        fruits[i] = '香蕉'
        break
print(fruits)
```

列表元素删除

In [52]

```
words = ['apple','pear','pineapple','banana','strawberry']
del words[1]
print(words)
```

In [ ]

```
words = ['apple','pear','pineapple','banana','strawberry']
words.remove('apple')
print(words)
```

In [53]

```
words = ['apple','pear','pineapple','banana','strawberry']
words.pop(1)
print(words)
```

列表切片

- 在Python中处理列表的部分元素，称之为切片。
- 创建切片，可指定要使用的第一个元素和最后一个元素的索引。注意：左开右闭
- 将截取的结果再次存放在一个列表中，所以还是返回列表

| **元素** | **cat** | **dog** | **tiger** | **snake** | **mouse** | **bird** |
| :------- | :------ | :------ | :-------- | :-------- | :-------- | :------- |
| 正向     | 0       | 1       | 2         | 3         | 4         | 5        |
| 反向     | -6      | -5      | -4        | -3        | -2        | -1       |

In [55]

```
animals = ['cat','dog','tiger','snake','mouse','bird']
print(animals[2:5])
print(animals[-1:])
print(animals[-3:-1])
print(animals[-5:-1:2])  # 从[-5,-1)间隔一个取值
print(animals[::2])  # 全部间隔一个取值
```

列表排序

- 随机生成10个不同的整数，并进行排序

In [61]

```
import random

random_list = []
i = 0
while i < 10:
    ran = random.randint(1,20)
    if ran not in random_list:
        random_list.append(ran)
        i += 1
print(random_list)
```

In [62]

```
# 默认升序
new_list = sorted(random_list)
print(new_list)

# 降序
new_list = sorted(random_list,reverse = True)
print(new_list)
```

长度

在 Python 中，要查看数组（或其他可迭代对象）的长度，可以使用内置函数 `len()`。

以下是使用 `len()` 函数查看数组长度的示例：

```
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print("数组的长度是:", length)
```



# 元组

与列表类似，元组中的内容不可修改

In [65]

```
tuple1 =()
print(type(tuple1))
```

In [64]

```
tuple2 =('hello')
print(type(tuple2))
```

注意：元组中只有一个元素时，需要在后面加逗号！

In [66]

```
tuple3 =('hello',)
print(type(tuple3))
```

元组不能修改，不存在往元组里加入元素

In [69]

```
import random

random_list = []
for i in range(10):
    ran = random.randint(1,20)
    random_list.append(ran)
print(random_list)

random_tuple = tuple(random_list)
print(random_tuple)
```

In [71]

```
print(random_tuple)
print(random_tuple[0])
print(random_tuple[-1])
print(random_tuple[1:3])
print(random_tuple[::-1]) # 从后往前依次打印元素
```

元组的修改：

In [72]

```
t1 = (1,2,3) + (4,5)
print(t1)
```

In [73]

```
t2 = (1,2,3)*2
print(t2)
```

元组中的一些函数：

In [75]

```
print(max(random_tuple))
print(min(random_tuple))
print(sum(random_tuple))
print(len(random_tuple))
```

In [77]

```
# 统计元组中的4的个数
print(random_tuple.count(4))
```

In [78]

```
# 元组中4所对应的下标，如果不存在，则会报错
print(random_tuple.index(4))
```

In [80]

```
# 判断元组中是否存在1这个元素
print(4 in random_tuple)

# 返回元组中4所对应的下标，不会报错
if(4 in random_tuple):
    print(random_tuple.index(4))
```

元组的装包与拆包

In [81]

```
# 定义一个元组
t3 = (1,2,3)

# 将元组赋值给变量a，b，c
a,b,c = t3

# 打印a，b，c
print(a,b,c)
```

In [88]

```
# 当元组中元素个数与变量个数不一致时
# 定义一个元组，包含5个元素
t4 = (1,2,3,4,5)

# 将t4[0]，t4[1]分别赋值给a，b；其余的元素装包后赋值给c
a,b,*c = t4
print(a,b,c)
print(c)
print(*c)
```

## 元组添加数据方式

在 Python 中，元组是不可变的数据结构，意味着一旦创建，就无法修改其内容。因此，无法直接向空元组添加元素。但是，你可以通过合并两个元组来创建一个新的元组，其中包含原来的元素以及要添加的新元素。

以下是向空元组添加元素的示例代码：

```python
# 创建一个空元组
empty_tuple = ()

# 添加元素
new_tuple = empty_tuple + (new_element,)

# 打印新元组
print(new_tuple)
```

在这个示例中，我们首先创建了一个空元组 `empty_tuple`。然后，通过将空元组与包含要添加的新元素的元组进行合并操作 `empty_tuple + (new_element,)`，创建了一个新的元组 `new_tuple`。最后，我们打印了新的元组。

请注意，在合并元组时要使用逗号 `,` 来确保将元素视为一个元组而不是单个元素。这是因为括号本身不足以创建一个元组，需要至少包含一个逗号。

需要注意的是，虽然我们不能直接修改元组，但是我们可以通过重新赋值的方式改变元组变量的引用，例如 `empty_tuple = empty_tuple + (new_element,)`。这将创建一个新的元组并赋值给 `empty_tuple`，从而实现了向元组中添加新元素的效果。

# 字典（对象）

In [89]

```
# 定义一个空字典
dict1 = {}
dict2 = {'name':'宁静','weight':45,'age':25}
print(dict2['name'])
```

In [92]

```
# list可以转成字典，但前提是列表中元素都要成对出现
dict3 = dict([('name','宁静'),('weight',45)])
print(dict3)
```

In [91]

```
dict4 = {}
dict4['name'] = '宁静'
dict4['weight'] = 45
print(dict4)
```

In [93]

```
dict4['weight'] = 44
print(dict4)
```

In [2]

```
# 字典里的函数 items() keys() values()
dict5 = {'宁静':165,'张雨绮':166,'万茜':164}
print(dict5.items())
for key,value in dict5.items():
    if value > 165:
        print(key)
```

In [3]

```
# values()取出字典中所有的值，保存到列表中
results = dict5.values()
print(results)
```

In [4]

```
# 求平均身高
heights = dict5.values()
print(heights)
total = sum(heights)
avg = total/len(heights)
print(avg)
```

In [5]

```
names = dict5.keys()
print(names)
```

In [8]

```
# print(dict5['张含韵'])
print(dict5.get('张含韵'))  # 如果没有该值，返回None
print(dict5.get('张含韵',170))  # 如果能够取到值，则返回字典中的值，否则返回默认值170
```

In [10]

```
dict6 = {'宁静':165,'张雨绮':166,'万茜':164}
del dict6['张雨绮']
print(dict6)
```

In [11]

```
result = dict6.pop('万茜')  # 返回value值
print(result) 
print(dict6)  # 返回剩余的dict内容
```

# **Python 面向对象**

定义一个类Animals:
(1)init()定义构造函数，与其他面向对象语言不同的是，Python语言中，会明确得把代表自身实例的self作为第一个参数传入
(2)创建一个实例化对象 cat，init()方法接收参数
(3)使用点号，来访问对象的属性

In [14]

```
class Animals:
    def __init__(self,name):  # self 代表实例本身
        self.name = name
        print('动物名称实例化')
    def eat(self):
        print(self.name + '要吃东西啦！')
    def drink(self):
        print(self.name + '要喝水啦！')

cat = Animals('熊猫')
print(cat.name)
cat.eat()
cat.drink()
```

In [15]

```
class Person:
    def __init__(self,name):
        self.name = name
        print('调用父类构造函数')
    
    def eat(self):
        print('调用父类方法')

class Student(Person):  # 定义子类
    def __init__(self):
        print('调用子类构造方法')

    def study(self):
        print('调用子类方法')

s = Student()  # 实例化子类
s.study()  # 调用子类方法
s.eat()  # 调用父类方法
```



# 类

Python中的类是一种抽象数据类型，用于创建具有相似行为和属性的对象。类定义了对象的结构和行为，并允许从该类创建多个对象。下面是Python类的详细解释和示例：

1. 类的定义：
   在Python中，可以使用`class`关键字定义一个类。类由属性和方法组成。属性是类的数据成员，方法是类的函数成员。

```python
class MyClass:
    attribute = "Hello, World!"  # 类属性

    def method(self):  # 类方法
        print(self.attribute)
```

2. 对象的创建：
   通过使用类来创建实际的对象，这个对象可以访问类定义的属性和方法。

```python
my_object = MyClass()  # 创建对象

print(my_object.attribute)  # 访问类属性
my_object.method()  # 调用类方法
```

3. 属性和方法：
   类的属性是类的数据成员，它们保存对象中的数据。类的方法是类的函数成员，用于操作或访问对象的数据。

```python
class Circle:
    def __init__(self, radius):  # 初始化方法
        self.radius = radius

    def area(self):  # 计算面积的方法
        return 3.14 * self.radius ** 2

    def circumference(self):  # 计算周长的方法
        return 2 * 3.14 * self.radius


my_circle = Circle(5)  # 创建Circle对象，传递半径为5

print(my_circle.area())  # 输出面积
print(my_circle.circumference())  # 输出周长
```

在上面的示例中，`__init__`是一个特殊方法，用于在创建对象时初始化对象的属性。`area`和`circumference`是类的方法，用于计算圆的面积和周长。

4. 继承：
   继承是一种面向对象编程中重要的概念。它允许一个类继承另一个类的属性和方法。

```python
class Animal:
    def sound(self):
        print("The animal makes a sound.")


class Dog(Animal):
    def sound(self):
        print("The dog barks.")


my_dog = Dog()
my_dog.sound()  # 输出"The dog barks."
```

在上面的示例中，`Dog`类继承了`Animal`类。`Dog`类可以访问和调用`Animal`类中定义的方法。

`self` 是一个特殊的参数，在定义类的方法时使用。它表示对象实例本身，可以用来访问该实例的属性和方法。

在Python中，当你调用一个对象的方法时，Python会自动将对应的对象实例作为第一个参数传递给该方法。这个参数通常被命名为 `self`，但其实你可以使用任何合法的变量名来代表这个参数。

通过使用 `self` 这个参数，你可以在类的方法内部访问和操作对象实例的属性。同时，也可以调用该类的其他方法。

以下是一个示例：

```python
class MyClass:
    def __init__(self, x):
        self.x = x

    def method(self):
        print("x =", self.x)

    def update_x(self, new_x):
        self.x = new_x

my_object = MyClass(5)
my_object.method()  # 输出 "x = 5"

my_object.update_x(10)
my_object.method()  # 输出 "x = 10"
```



在上面的示例中，我们定义了一个名为 `MyClass` 的类，其中包含一个初始化方法 `__init__`、一个打印属性值的方法 `method`，以及一个更新属性值的方法 `update_x`。

当创建 `my_object` 对象时，我们将值 `5` 传递给了初始化方法，并赋值给了实例变量 `x`。然后，我们通过调用 `method` 方法输出了属性 `x` 的值。

接着，我们调用了 `update_x` 方法，修改了属性 `x` 的值为 `10`。再次调用 `method` 方法，可以看到属性值已经被更新了。

总之，`self` 参数是一个表示对象实例的引用，它让你可以在类的方法中访问和操作该实例的属性和方法。

# 多文件编程

在Python中，可以将代码拆分成多个文件进行编程，这样有助于组织和维护大型程序。以下是一些常用的方法：

- 模块导入：将代码划分成几个逻辑上相似的文件，然后使用import语句导入需要使用的模块。
- 包：将相关的模块放到同一个文件夹内，并加上一个名为`__init__.py`的空文件，这个文件会被解释器视为包，可以通过“包.模块”的方式来导入模块。
- from...import语句：可以从某个模块中导入指定的函数或变量，这样就可以避免重复输入模块名。
- __name__变量：该变量用来判断是否在当前模块内运行代码，如果是，则执行一些初始化操作，如果不是，则直接导入该模块。

下面是一个简单的示例，演示如何在Python中进行多文件编程：假设我们有两个文件：index.py和router.py，其中router.py在相对于index.py路径下的admin文件夹中，包含了一个函数InitRouter()

router.py：

```python
from flask import render_template
from flask import Blueprint
from flask import request
def InitRouter(app): //函数
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/admin')
    def admin():
        username = request.cookies.get('username')
        # 当没有登录的时候跳转到登录界面
        if username == None:
            return render_template('login.html')
        # 当已经登录，跳转到管理界面
```

main.py文件内容如下：

```python
from flask import Flask
import  pymysql
from admin.router import InitRouter #调用该函数
from flask import url_for

app = Flask(__name__)


#初始化扩展，传入app 创建db
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='blog')

InitRouter(app)
db.close()

```

**注意：**如果在flask框架中调用函数，都是以根目录为准

## 读取另一个 Python 脚本中的变量

要在一个 Python 脚本中读取另一个 Python 脚本中的变量，可以使用模块（Module）的方式。

假设你有两个 Python 脚本文件 `script1.py` 和 `script2.py`。如果你想在 `script2.py` 中读取 `script1.py` 中定义的变量，你可以按照以下步骤进行操作：

1. 在 `script1.py` 中，定义你希望共享的变量，例如：

   ```
   # script1.py
   variable = "Hello, World!"
   ```

   

2. 在 `script2.py` 中，通过导入 `script1` 模块来访问 `script1.py` 中定义的变量，例如：

   ```
   # script2.py
   import script1
   
   value = script1.variable
   print(value)  # 输出 "Hello, World!"
   ```

   

在这个例子中，我们首先在 `script2.py` 中使用 `import script1` 来导入 `script1.py` 文件。然后，我们可以通过 `script1.variable` 来访问 `script1.py` 中定义的变量。

请确保 `script1.py` 和 `script2.py` 在相同的目录下，或者在 Python 解释器能够找到的路径下。

值得注意的是，在读取其他 Python 脚本中的变量时，被导入的脚本会在首次导入时执行，因此如果 `script1.py` 中存在执行语句，会在导入时被执行。

# try和 except(可以用于回滚事件)

`try` 和 `except` 是 Python 中用于异常处理的关键字。i

`try` 代码块用于包含可能会触发异常的代码。如果在 `try` 代码块中出现异常，那么程序的执行流程将会跳转到 `except` 代码块。

`except` 代码块用于捕获并处理异常。你可以在 `except` 代码块中指定要捕获的异常类型，并在处理异常时执行相应的操作。

以下是 `try` 和 `except` 的基本语法结构：

```python
try:
    # 可能会触发异常的代码
    # ...
except ExceptionType1:
    # 处理 ExceptionType1 类型的异常
    # ...
except ExceptionType2:
    # 处理 ExceptionType2 类型的异常
    # ...
finally:
    # 可选的 finally 代码块
    # ...
```



在上述语法中，`ExceptionType1` 和 `ExceptionType2` 是异常类的名称，用于指定你想要捕获和处理的具体异常类型。你可以根据自己的需求捕获不同类型的异常并执行相应的操作。

另外，`finally` 是一个可选的代码块，在 `try` 和 `except` 块之后执行。无论是否发生异常，`finally` 代码块中的代码总是会被执行。

下面是一个简单的示例，演示了如何使用 `try` 和 `except` 来捕获和处理异常：

```python
try:
    num = int(input("输入一个整数: "))
    result = 10 / num
    print("结果: ", result)
except ValueError:
    print("输入无效的整数")
except ZeroDivisionError:
    print("除数不能为0")
finally:
    print("程序执行完毕")
```



在上述示例中，我们尝试将用户输入的字符串转换为整数，并进行除法运算。如果用户输入的是无效的整数或除数为0，将会捕获相应的异常并打印相关的错误消息。最后，无论是否发生异常，最后一行的代码都会被执行。

希望这个解释能够帮助你理解 `try` 和 `except` 的概念和用法。如果你有更多疑问，请随时提问。

# 数字与字母转换

要将数字 0、1、2 和 3 分别转换为字母 A、B、C 和 D，可以使用 Python 的内置函数 `chr()` 和 `ord()`。

下面是一个示例，演示如何将数字转换为相应的字母：

```python
number = 0

# 将数字转换为字母
letter = chr(ord('A') + number)

print(letter)
```



这个示例中，我们首先设置变量 `number` 的值为 0，表示要将数字 0 转换为字母。然后，我们使用 `ord('A')` 获取大写字母 A 的 ASCII 码值，再加上 `number`，即 0。最后，我们使用 `chr()` 函数将得到的 ASCII 码值转换回相应的字母。

输出结果：

```
A
```



如果你想将数字 1、2 和 3 分别转换为字母 B、C 和 D，只需将 `number` 的值分别设置为 1、2 和 3 即可。

```python
number = 1
letter = chr(ord('A') + number)
print(letter)  # 输出 B

number = 2
letter = chr(ord('A') + number)
print(letter)  # 输出 C

number = 3
letter = chr(ord('A') + number)
print(letter)  # 输出 D
```

# 获取 Python 的简单 for 循环中索引的问题


Python 的 for 循环相比其他语言而言更加简单，比如经常会有如下这样类似的例子。我们可以直接对列表进行遍历，获取列表的某个元素，并对这个元素进行相应的操作。

```python
testList = ['nice', 'to', 'meet', 'you']
for x in testList:
   print(x)
```

运行结果如下：

```
nice
to
meet
you
```

但是，如果我们在上面的 for 循环中，除了想要获取对应元素 x 以外，还想知道对于这个元素在列表中的索引的话该怎么办呢？难道就没有其他的方法了吗？

人生苦短，我用 Python。天无绝人之路，设计者早就想到了，虽然一般在 Python 当中来说，循环中要获取遍历元素的索引的情况并不算很多，但是还是有方法来解决的，那就是Python当中自带的enumerate函数，让我们来看看到底怎么用的吧！

```python
testList = ['nice', 'to', 'meet', 'you']
for i, x in enumerate(testList):
   print(i, x)
```

其中循环中的i就是对应元素x在列表中的索引啦，运行结果如下：

```
0 nice
1 to
2 meet
3 you
```

# 函数实现本身放到字典当中

你可以使用 Python 的 lambda 表达式（匿名函数）将 `Get_ERNIE` 函数以字符串形式直接嵌入到字典中，如下所示：

```python
AI_set = {
    'GPT': {
        
    },
    'ERNIE': {
        'payload': lambda AnswerData: {
            "messages": [
                {
                    "role": "user",
                    "content": AnswerData
                }
            ]
        }
    }
}
```

在上述代码中，使用 `lambda` 表达式将函数体直接嵌入到了字典中，替代了之前用函数名作为值的做法。`lambda` 表达式的语法为：

```
lambda arguments: expression
```

其中 `arguments` 为函数的参数，可以包括多个参数，用逗号隔开；`expression` 为函数体，通常是一个表达式，该表达式的返回值即为 `lambda` 函数的返回值。在本例中，`lambda` 表达式中只有一个参数 `AnswerData`，函数体和 `Get_ERNIE` 保持一致。

这种方式可以在不需要重复使用函数时以更简洁的方式来实现

## Python isalpha() 函数判断是否中英文

### *原文:* [Python isalpha()方法](http://www.runoob.com/python/att-string-isalpha.html)

中文的汉字会被 isalpha 判定为 True：增加UTF-8

```
#!/usr/bin/python
# -*- coding: UTF-8 -*-

s = u"中国"
print s.isalpha()  # True
```

如果想区分中文和英文可以使用 unicode。

中文的范围为：**['/u4e00'，'/u9fa5']**。

判断是否是全英文：

```
#!/usr/bin/python
# -*- coding: UTF-8 -*-

s = u"中国"
print s.encode( 'UTF-8' ).isalpha()  # False
```

判断是否是全数字：

```
s.encode( 'UTF-8' ).isdigit()
```

# _\_init\_\_.py 文件

\_\_init\_\_.py 文件的作用是将文件夹变为一个Python模块,Python 中的每个模块的包中，都有\_\_init\_\_.py 文件。

通常\_\_init\_\_.py 文件为空，但是我们还可以为它增加其他的功能。我们在导入一个包时，实际上是导入了它的\_\_init\_\_.py文件。这样我们可以在\_\_init\_\_.py文件中批量导入我们所需要的模块，而不再需要一个一个的导入。

```haskell
# package
# __init__.py
import re
import urllib
import sys
import os

# a.py
import package 
print(package.re, package.urllib, package.sys, package.os)
```

注意这里访问\_\_init\_\_.py文件中的引用文件，需要加上包名。

\_\_init\_\_.py中还有一个重要的变量，\_\_all\_\_, 它用来将模块全部导入。

```python
# __init__.py
__all__ = ['os', 'sys', 're', 'urllib']

# a.py
from package import *
```

这时就会把注册在\_\_init\_\_.py文件中\_\_all\_\_列表中的模块和包导入到当前文件中来。

可以了解到，\_\_init\_\_.py主要控制包的导入行为。要想清楚理解\_\_init\_\_.py文件的作用，还需要详细了解一下import语句引用机制：

可以被import语句导入的对象是以下类型：

*   模块文件（.py文件）
*   C或C++扩展（已编译为共享库或DLL文件）
*   包（包含多个模块）
*   内建模块（使用C编写并已链接到Python解释器中）

当导入模块时，解释器按照sys.path列表中的目录顺序来查找导入文件。

```python
import sys
>>> print(sys.path)

# Linux:
['', '/usr/local/lib/python3.4',
 '/usr/local/lib/python3.4/plat-sunos5',
 '/usr/local/lib/python3.4/lib-tk',
 '/usr/local/lib/python3.4/lib-dynload',
 '/usr/local/lib/python3.4/site-packages']

# Windows:
['', 'C:\\WINDOWS\\system32\\python34.zip', 'C:\\Documents and Settings\\weizhong', 'C:\\Python34\\DLLs', 'C:\\Python34\\lib', 'C:\\Python34\\lib\\plat-win', 'C:\\Python34\\lib\\lib-tk', 'C:\\Python34\\Lib\\site-packages\\pythonwin', 'C:\\Python34', 'C:\\Python34\\lib\\site-packages', 'C:\\Python34\\lib\\site-packages\\win32', 'C:\\Python34\\lib\\site-packages\\win32\\lib', 'C:\\Python34\\lib\\site-packages\\wx-2.6-msw-unicode']
```

其中list第一个元素空字符串代表当前目录。

**关于.pyc 文件 与 .pyo 文件**

.py文件的汇编,只有在import语句执行时进行，当.py文件第一次被导入时，它会被汇编为字节代码，并将字节码写入同名的.pyc文件中。后来每次导入操作都会直接执行.pyc 文件（当.py文件的修改时间发生改变，这样会生成新的.pyc文件），在解释器使用-O选项时，将使用同名的.pyo文件，这个文件去掉了断言（assert）、断行号以及其他调试信息，体积更小，运行更快。（使用-OO选项，生成的.pyo文件会忽略文档信息）

**导入模块**

模块通常为单独的.py文件，可以用import直接引用，可以作为模块的文件类型有.py、.pyo、.pyc、.pyd、.so、.dll

在导入模块时，解释器做以下工作：

1.  已导入模块的名称创建新的命名空间，通过该命名空间就可以访问导入模块的属性和方法。

2.  在新创建的命名空间中执行源代码文件。

3.  创建一个名为源代码文件的对象，该对象引用模块的名字空间，这样就可以通过这个对象访问模块中的函数及变量

import 语句可以在程序的任何位置使用，你可以在程序中多次导入同一个模块，但模块中的代码仅仅在该模块被首次导入时执行。后面的import语句只是简单的创建一个到模块名字空间的引用而已。

sys.modules字典中保存着所有被导入模块的模块名到模块对象的映射。

**导入包**

多个相关联的模块组成一个包，以便于维护和使用，同时能有限的避免命名空间的冲突。一般来说，包的结构可以是这样的：

```less
package
  |- subpackage1
	  |- __init__.py
	  |- a.py
  |- subpackage2
	  |- __init__.py
	  |- b.py
```

有以下几种导入方式：

```css
import subpackage1.a # 将模块subpackage.a导入全局命名空间，例如访问a中属性时用subpackage1.a.attr
from subpackage1 import a #　将模块a导入全局命名空间，例如访问a中属性时用a.attr_a
from subpackage.a import attr_a # 将模块a的属性直接导入到命名空间中，例如访问a中属性时直接用attr_a
```

使用from语句可以把模块直接导入当前命名空间，from语句并不引用导入对象的命名空间，而是将被导入对象直接引入当前命名空间。

## 注意

如果是多包编写，一定要在__init__.py里面加上，否则会报错找不到包：

```
import sys,os
script_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(script_path)
```

# 高级函数

## zip()

for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):

这行代码使用了 `zip()` 函数将 `classIds`、`confs` 和 `bbox` 三个数组进行打包，然后通过迭代解压缩的方式分别将每个数组中的元素赋值给 `classId`、`confidence` 和 `box`。

- `classIds` 是一个一维数组，包含了每个检测到的对象的类别标签。
- `confs` 是一个一维数组，包含了每个检测到的对象的置信度。
- `bbox` 是一个二维数组，每行包含了每个检测到的对象的边界框坐标（左上角和右下角坐标）。

通过使用 `zip()` 函数将这三个数组打包在一起，并使用 `for` 循环进行迭代，我们可以方便地对每个检测到的对象进行处理。

例如，可以将 `classId` 作为对象的类别标签，`confidence` 作为对象的置信度，`box` 作为对象的边界框坐标，来进行后续的操作，例如绘制边界框、标签等。

## flatten()

for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):

`flatten()` 是用于将多维数组（例如二维数组）转换为一维数组的方法。

在上述代码中，`classIds.flatten()` 和 `confs.flatten()` 是将 `classIds` 和 `confs` 两个数组转换为一维数组的操作。

`classIds` 和 `confs` 都是数组，其中 `classIds` 用于存储每个检测到的对象的类别标签，`confs` 用于存储每个对象的置信度。

通过调用 `flatten()` 方法，我们可以将这些数组重新构造为一维的形式，便于进行后续的操作，例如使用 `zip()` 函数进行迭代、或者进行其他一维数组操作。

希望这个解释对您有所帮助。如果还有其他问题，请随时提问。
