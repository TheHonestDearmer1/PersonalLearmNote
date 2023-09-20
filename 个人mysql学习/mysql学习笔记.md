# MySQL 案例实战教程

### 案例1：MySQL的安装

![image-20230730121234798](图片/1.png)

### MySQL数据类型

int/bigint(java的long)

float/double

datetime/timestamp(可储存时间戳)

char(定长字符)/varchar(不定长字符)/text(大文本)

blob(字节数据类型，存储图片，音频等文件)

语法

### --建表

```sql
create table 表名（

    字段名 类型 约束（主键，非空，唯一，默认值），
    
    字段名 类型 约束（主键，非空，唯一，默认值），

）编码，存储引擎
```

### 约束和插入数据

- **NOT NULL**:规定某一列不能存储null值
- **UNIQUE**：保证某列的每行都有唯一的值
- **PRIMARY KEY**：NOT NULL和UNIQUE的组合
- **FOREIGN KEY**（尽量少用）：保证一个表中的数据匹配另一个表中的值的参照完全性
- **CHECK**：保证列中的值符合条件
- **DEFAULT**：规定没有列赋值时的默认值

```sql
DROP TABLE IF EXISTS `websites`;
CREATE TABLE `websites`(
    id int(11) NOT NULL AUTO_INCREMENT,
    name char(20) NOT NULL DEFAULT'' COMMENT'站点名称', /*COMMENT 添加 '站点名称'这个注释*/
    url varchar(255) NOT NULL DEFAULT '',/*代表网站的表*/
    alexa int(11) NOT NULL DEFAULT '0' COMMENT'Alexa排名',
    sal double COMMENT'广告收入',
    country char(10) NOT NULL DEFAULT'' COMMENT'国家',
    PRIMARY KEY(id)
)ENGINE=INNODB DEFAULT CHARSET=utf8;
插入

INSERT INTO websites(name,url,alexa,sal,country) VALUES("腾讯","https://www.qq.com",18,1000,'CN');
```



### 外键约束


数据库中的外键（Foreign Key）是用于建立表与表之间关系的一种机制。外键定义了两个表之间的引用关系，它指向另一个表中的主键，用于确保数据的完整性和一致性。

外键通常用于实现表与表之间的关联，常见的关联包括一对一、一对多和多对多关系。

举个例子，我们有两张表：订单表和客户表。其中订单表中有一个外键字段 `customer_id`，它引用了客户表的主键字段 `id`。这个外键可以确保每个订单都必须与一个现有的客户关联。

通过定义外键关系，数据库可以在执行插入、更新和删除操作时自动处理关系的一致性。例如，如果试图在订单表中插入一个未存在于客户表中的客户ID，数据库会拒绝插入操作，从而维护了表之间的关联性。

在创建表时，可以使用类似下面的 SQL 语句添加外键关系：

```sql
CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(100)
);

CREATE TABLE orders (
  id INT PRIMARY KEY,
  order_number VARCHAR(20),
  customer_id INT,
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```



在这个例子中，`customers` 表中的 `id` 字段是主键，`orders` 表中的 `customer_id` 字段是外键，引用了 `customers` 表的 `id` 字段。

通过引入外键关系，数据库可以提供数据的完整性和约束，确保关联的数据一致性，并提供便利的查询操作和数据管理。

### 删除

```sql
DELETE FROM websites WHERE id = 5;
```

### 更新

```sql
UPDATE websites SET sal = 2000 WHERE id = 3;
```

### 注释

```sql
-- 单行注释
-- UPDATE websites SET sal = 2000 WHERE id = 3;
/*多行注释*/
```

### 查询

```sql
DROP TABLE IF EXISTS `websites`;
CREATE TABLE `websites`(
    id int(11) NOT NULL AUTO_INCREMENT,
    name char(20) NOT NULL DEFAULT'' COMMENT'站点名称',
    url varchar(255) NOT NULL DEFAULT '',
    alexa int(11) NOT NULL DEFAULT '0' COMMENT'Alexa排名',
    sal double COMMENT'广告收入',
    country char(10) NOT NULL DEFAULT'' COMMENT'国家',
    PRIMARY KEY(id)
)ENGINE=INNODB DEFAULT CHARSET=utf8;

INSERT INTO `websites` VALUES
    (1,'Google', 'https://www.google.com/', '1',2000 , 'USA '),
    (2,'淘宝','https://www.taobao.com/','13',2050,'CN'),
    (3,'菜鸟教程', 'http://www.runoob.com/', '4689' ,0.0001,'CN'),
    (4,'微博', 'http://weibo.com/','20',50,'CN'),
    (5,'Facebook','https://www.facebook.com/','3',500, 'USA');
CREATE TABLE IF NOT EXISTS `access_log`(
    `aid` int(11) NOT NULL AUTO_INCREMENT,
    `site_id` int(11) NOT NULL DEFAULT '0' COMMENT '网站id',
    `count` int(11) NOT NULL DEFAULT '0' COMMENT '访问次数',
    `date` date NOT NULL,
    PRIMARY KEY (`aid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `access_log` (`aid`,`site_id`,
`count`,`date`) VALUES
(1,1,45,'2016-05-10'),
(2,3,100,'2016-05-13'),
(3,1,230,'2016-05-14'),
(4,2,10,'2016-05-14'),
(5,5,205,'2016-05-14'),
(6,4,13,'2016-05-15'),
(7,3,220,'2016-05-15'),
(8,5,545,'2016-05-16'),
(9,3,201,'2016-05-17'),
(10,88,9999,'2016-09-09');
```

### 查询语句

实际开发中尽量不要使用*作为查询

```sql
select * from websites

select id,name,url,alexa from websites
```

### 分页查询

```sql
select id,name,url,alexa from websites limit 2,3
-- 从第二条开始查，查三条，0，1，2下标
select * from video order by upload_time desc limit 30 
-- 以upload_time倒序查，限制最多查30条
```

### distinct去重

```sql
select distinct country from websites
```

### where语句

```sql
运算符> < >= <= <> != = 
is null    is not null
like in
```

> 在sql语句中 null值和任何东西比较 都为false，包括null
>

```sql
SELECT * FROM websites WHERE sal IS NOT NULL 
```

### 逻辑条件:and or

```sql
select * from websites where sal<=0 and sal>=2000;/*收入在0到2000之间*/
select * from websites where sal between 2000 and 0;/*和上面效果一样*/
select * from websites where sal<5 or sal is null; /*收入小于5或者没有收入*/
```

### 排序 order by

~~~sql
select * from websites order by sal asc,alexa desc;-- 先按sal升序，再按alexa降序
~~~

### like 通配符

```sql
select * from websites where name like '%O%'
select * from websites where name like '_O%'-- 匹配一个字符
```



### in 匹配多个条件

```sql
select * from websites where country in ('USA','鸟国','CN');
```

### 别名

```sql
select tt.name '网站名字' from websites tt -- tt是表的别名
```

### group by 分组查询

~~~sql

select avg(sal) '平均值' ,country from websites group by country;


select avg(sal) '平均值' ,country from websites group by country HAVING 平均值 > 1200;-- 分了组后，不能用where，只能用having;
~~~

> 子查询
>

> 把查询结果当做一个表来使用
>

### 连接查询

![image-20230802105221314](图片/image-20230802105221314.png)

```sql
/*过时写法*/
/*不加where的话会随意乱连*/
/*内连接*/
select name,a.count,a.date from websites w,access_log a where w.id=a.site_id
```

```sql
/*outer可以省*/
/*左外连接*/
select * from websites w left outer join access_log a
on w.id=a.site_id
union/*实现全连接*/
select * from websites w right join access_log a
on w.id=a.site_id
if null

select name,ifnull(count,0),ifnull(a.date,'无日期') from websites w left outer join access_log a
on w.id=a.site_id
```

### 练习题

```sql
CREATE TABLE dept(
    deptno        INT,
    dname        varchar(14),
    loc        varchar(13)
);
INSERT INTO dept values(10, 'ACCOUNTING', 'NEW YORK');
INSERT INTO dept values(20, 'RESEARCH', 'DALLAS');
INSERT INTO dept values(30, 'SALES', 'CHICAGO');
INSERT INTO dept values(40, 'OPERATIONS', 'BOSTON');

CREATE TABLE emp(
    empno INT,
    ename VARCHAR(50),
    job VARCHAR(50),
    mgr    INT,
    hiredate DATE,
    sal    DECIMAL(7,2),
    comm DECIMAL(7,2),
    deptno INT
) ;
INSERT INTO emp values(7369,'SMITH','CLERK',7902,'1980-12-17',800,NULL,20);
INSERT INTO emp values(7499,'ALLEN','SALESMAN',7698,'1981-02-20',1600,300,30);
INSERT INTO emp values(7521,'WARD','SALESMAN',7698,'1981-02-22',1250,500,30);
INSERT INTO emp values(7566,'JONES','MANAGER',7839,'1981-04-02',2975,NULL,20);
INSERT INTO emp values(7654,'MARTIN','SALESMAN',7698,'1981-09-28',1250,1400,30);
INSERT INTO emp values(7698,'BLAKE','MANAGER',7839,'1981-05-01',2850,NULL,30);
INSERT INTO emp values(7782,'CLARK','MANAGER',7839,'1981-06-09',2450,NULL,10);
INSERT INTO emp values(7788,'SCOTT','ANALYST',7566,'1987-04-19',3000,NULL,20);
INSERT INTO emp values(7839,'KING','PRESIDENT',NULL,'1981-11-17',5000,NULL,10);
INSERT INTO emp values(7844,'TURNER','SALESMAN',7698,'1981-09-08',1500,0,30);
INSERT INTO emp values(7876,'ADAMS','CLERK',7788,'1987-05-23',1100,NULL,20);
INSERT INTO emp values(7900,'JAMES','CLERK',7698,'1981-12-03',950,NULL,30);
INSERT INTO emp values(7902,'FORD','ANALYST',7566,'1981-12-03',3000,NULL,20);
INSERT INTO emp values(7934,'MILLER','CLERK',7782,'1982-01-23',1300,NULL,10);
INSERT INTO emp values(7981,'MILLER','CLERK',7788,'1992-01-23',2600,500,20);
```

# 数据库理论知识

## 数据模型

**数据模型分类:**

1. 从信息世界中抽象的数据模型称为概念数据模型
2. 从计算机世界中抽象出的DBMS支持的数据模型称为结构数据

**概念数据模型**:一般采用实体-联系方式（E-R方法）表示

**实体**:客观存在并可以互相区别的事物称为实体

**属性**:描述实体的特性称为属性

**码**:唯一标识实体的属性称为码

**域**:属性的取值范围称为该属性的域，性别域（男，女）

**联系**:实体（型）之间的对应关系称为联系

1:1 班与班之间是一对一联系
1:n 班与学生之间是一对多联系
m:n 课程和学生之间是多对多联系

**实体-联系方式**:E-R图
实体型用矩型表示，属性用椭圆形表示并用无向边将其与相应的实体联系起来；联系用菱形表示

**结构数据模型**
        结构数据模型是直接面向数据库的逻辑结构
 （2）**层次模型**
       **层次模型是用“树结构”来表示数据之间的联系**，是数据库系统最早使用的一种模型，它的数据结构是一棵“有向树”。
     **层次模型的特征**:1.仅有一个结点没有父结点，它就是根结点。
2.其他结点有且仅有一个父结点
（4）**关系模型**
       关系模型是一种用二维表格结构开表示实体与实体之间联系的数据模型。

## 三级模式和两级映像

不同数据的产品有很多，数据的存储结构也各不相同，但**体系结构**基本上都**具有相同的特征**，采用“**三级模式和两级映像”**。

**三级模式:外模式，概念模式，内模式。**
**对应:视图，基本表，储存文件**
**两级映像    模式=概念模式**

（1）模式/内模式映像  **物理独立性**
（2）外模式/模式映像 **逻辑独立性**

**关系**:一个关系就是一张二维表，每个关系有一个关系名。

**元组**:表中的一行即为一个元组，对应储存文件中的一个记录值。

**关系模式**:关系名（属性名1，属性名2，……属性名n）

**候选码**（或候选键）:属性或属性组合，其值能够唯一地标识一个元组

**主码**:在一个关系中可能有多个候选码，从中选择几个作为主码。

**外码或外键**:如果一个关系中的属性或属性组并非该关系的码，但它们是另外一个关系的码，则称为该关系的外码
     但它们是另外一个关系的码，则称为该关系的外码

## 2.1.2关系的数字定义

本节用集合代数给出二维表的关系定义。
    **1.笛卡尔积**
设D1,D2......Dn为任意集合，定义D1,D2......Dn的笛卡尔积为:D1xD2x......Dn={（d1,d2,......,dn）| di属于Di,i=1,......,n}
其中每个元素:{（d1,d2,......,dn）}叫做一个n元组。
D1={0,1},D2={a,b,c} D1的元素要与D2所有元素对齐
D1xD2={(0,a),(0,b),(0,c),(1,a),(1,b),(1,c)}
**4.投影**
     投影运算是从关系的垂直方向进行运算，在关系中选出若干属性列A组成新的关系记为πA（R）。
**5.选择**
    选择运算是从关系的水平方向进行运算，是从关系R中选择满足给定关系的诸元组，记作6f（R），其形式定义如下:   

![image-20230904230420876](图片/image-20230904230420876.png)

## 关系模型的定义

​    **关系的描述为关系模式，可以表示为R（U，D , dom , F ）**
​       简记为R(U)  R为关系名，U为属性名集合
U为属性名集合，D为属性的域，dom为属性向域的映像集合，F为属性间的依赖关系集合
​        关系模型由**数据结构**，**关系操作集合**和**关系完整性约束**三部分组成

​       (1)**关系模型中关系数据结构**

​       (3)**关系模型中的关系完整性约束**

​                 实体完整性：关系中主码的值不能为空或部分为空，也就是说，主码中属性即主属性不能取空值。

​                 参照完整性：如果关系R2的外码与关系R1的主码相对应，则外码X（每个值必须在关系R1中的主码的值中找到或者空值）的用户定义的完整性：指用户对某一具体数据指定的约束条件进行检验。

## 连接

从R与S的笛卡尔积中选取属性间满足一定条件的元组

![IMG_20230917_110311](./图片/IMG_20230917_110311.jpg)

5.外连接

​    外连接运算是连接运算的扩展，可以处理由于运算而缺失的信息。外连接运算有3种即左外连接，右外连接和全外连接![IMG_20230917_111116](./图片/IMG_20230917_111116.jpg)

## 自然连接

<img src="%E5%9B%BE%E7%89%87/IMG_20230917_111905.jpg" alt="IMG_20230917_111905"  />

## **除法运算**

在关系型数据库中，“除法运算”是指在两个关系之间执行一种特殊的查询操作，用于找出符合某种条件的组合。

假设我们有两个关系 R(A, B) 和 S(B, C)，其中 R 中的**属性 A 是主键**，S 中的属性 B 是**外键引用 R 的主键 A**。

除法运算的目标是找出符合条件的组合，也就是在 R 和 S 中，所有在 R 中的每个元组 A 在 S 中都可以找到对应的元组 B。换句话说，对于 R 中的每个元组 A，如果存在一个或多个 S 中的元组 B，使得 B 的 B 值与 A 的 A 值相等，则将这些组合作为结果返回。

SQL 中并没有直接支持除法运算的操作符，但可以使用其他查询操作来实现除法运算。下面是一个使用 SQL 查询实现关系除法的示例：

```sql
SELECT R.A
FROM R
WHERE NOT EXISTS (
  SELECT *
  FROM S
  WHERE S.B NOT IN (SELECT B FROM S WHERE S.B = R.A)
)
```



在这个例子中，我们使用子查询和 NOT EXISTS 条件来实现除法运算。首先，在外层查询中选择 R 表的主键 A。然后，在子查询中，我们检查 S 表中是否存在与 R 表中的 A 值相匹配的元组。如果找不到匹配的元组 B，则将 R 表中的 A 返回。

需要注意的是，除法运算在实际应用中相对较少使用，通常需要考虑性能和数据特征。在某些情况下，可能会使用其他查询操作或关系代数运算符来替代除法运算。

