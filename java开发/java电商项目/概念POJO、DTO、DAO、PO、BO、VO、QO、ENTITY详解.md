 

在java开发过程中，新手总是被DAO、[PO](https://so.csdn.net/so/search?q=PO&spm=1001.2101.3001.7020)、BO、VO等等概念弄得晕头转向。  
下面我查找了很多资料，总结如下：

一、POJO（Plain Ordinary Java Object 简单Java对象）
-------------------------------------------

实际就是普通JavaBeans，是为了避免和[EJB](https://so.csdn.net/so/search?q=EJB&spm=1001.2101.3001.7020)（Enterprise Java Beans 企业级JavaBeans）混淆所创造的简称，也称为（**Plain Old Java Object 又普通又老的对象**）。

相比于EJB来说，的确是老的对象，因为[ORM](https://so.csdn.net/so/search?q=ORM&spm=1001.2101.3001.7020)中间件的日趋流行，POJO又重新焕发了光彩。

POJO的内在含义是指：那些没有继承任何类、也没有实现任何接口，更没有被其它框架侵入的java对象。  
它仅包含自身的属性以及自身属性的getter和setter方法，这意味者POJO可以方便的从一个框架迁移到另一个框架中，或者框架升级也会对代码毫无影响，因此而得到复用。

```java
//例如在该实体EJB中，实体包含业务逻辑，同时也包含自身的持久化逻辑
//当更换数据源，或改变中间件框架时，则需要修改大量代码
public class Customer {
	private Long id;
	private String name;
	private Set<Order> orders = new HashSet();
	//省略业务逻辑
	//数据库访问方法
	public void remove(){
		//通过不同方式访问数据库，例如JDBC，Mybaits，JPA
	}
	public Customer load(){...}
	public Customer create(){...}
}
//当改为POJO时，则可以运行在任一JAVA环境中
public class Customer {
	private Long id;
	private String name;
	private Set<Order> orders = new HashSet();
	//省略getter和setter
}
```

一般，当需要持久化对象时，人们喜欢将该对象放在名为xxxPOJO的目录中。当然，不建议这样命名。  
POJO实际上是包括BO/VO/PO/DO等一系列对象的总称。有的团队规定禁止命名成xxxPOJO。

二、PO(persistence object 持久层对象)
------------------------------

PO是在ORM（对象关系映射）中与数据表的一条记录相匹配，自身属性与数据表字段一一对应。可以将数据表中的一条记录作为一个对象处理，并可以转化为其它对象。  
面对不同的数据源时，比如文档型数据库，对象型数据库等时，顾名思义PO是DAO层为进行持久化操作而准备的对象。

*   包含getter、setter方法。
*   不包含业务逻辑与数据库的访问方法。因为数据库本身不包含业务逻辑。
*   PO平常不一定需要实现序列化，只是当采用分布式存储或者需要作为前端输出及远程调用使用时，应该实现序列化

```java
//示例代码
public class User implements Serializable {
    //序列化版本，通过IDEA自动生成
    private static final long serialiVersionUID = 1L；
	private Long id;
    private String username;
    private String password;    
    //省略getter和setter方法
}
```

在《阿里巴巴开发手册》中，PO也叫DO（Data Object）数据对象，与数据库表结构一一对应，通过DAO层向上传输数据源对象。

三、DAO(data access object 数据访问对象)
--------------------------------

包含对数据的访问，负责持久层的操作 。通常需要结合PO来访问数据库，主要用来封装对数据的访问，并不转化成其它对象。  
在基于“事务脚本”的业务设计时，它包含业务逻辑。否则，一般只包含持久化的封装。

```java
public interface Dao{
    int insert(User user);
    User selectById(long id);
}
```

四、DTO（Data Transfer Object 数据传输对象）
----------------------------------

数据传输对象，是在应用网络层需要传输的对象，是一个为了减少方法调用次数而在进程间传输数据的对象。

在《阿里巴巴开发手册中》规定是Service 或 Manager 向外传输的对象。

> 某些人称这个为“**值对象**”，当然还是有稍许区别。值对象追求对象不可变，DTO的对象是可修改，可改变的。

###### 1.什么是DTO?

**从输入来看**，在进行请求时，应用在接口接收传入对象，然后又转换成实体进行持久化。在此过程中，传入的对象就是DTO。  
它的命名方式可能是Param、Query 、Command、等。Param 为查询参数对象，适用于各层，一般用做接受前端参数对象。Param 和 Query 的出现是为了不使用 Map 做为接收参数的对象。  
**从输出来看**，在进行返回响应时，若数据表有100个字段，那么PO中就有100个属性，而界面可能只需要其中10个属性，那么查询数据库后，对象就需要由PO转化成DTO。  
DTO可能还需要组合多个表查询到的对象成为一个大对象，以便减少网络的调用，或者给前端传输一些不在数据库中查到的属性，所以需要添加属性。

```java
//示例代码，继承实体类，从查询到的PO中添加属性返回给前端
public class UserDTO extends User {
    //序列化版本
    private static final long serialiVersionUID = 2L；
    //用户标识
    private String username;
    public String getUsername(){return username;}
    public void setUsername(String username){this.username= username;}
    //添加额外属性
    private HashMap<String, Object> extProperties;        
    public HashMap<String, Object> getExtProperties() {
        return extProperties;
    }
    public void setExtProperties(HashMap<String, Object> extProperties) {
        this.extProperties = extProperties;
    }
}
```

###### 2.DTO里面有什么？

一般不建议创建DTO，因为里面就一些属性和getter、setter方法，业务价值小，作用仅仅是在一次调用中传输几部分信息。  
其中，属性必须为原始数据类型，因为DTO需要被序列化以便能在连接中传播。  
它只包含自身数据的存储，而不包含业务逻辑。  
在不同的客户端之间，通常需要**DTO组装器**完成领域对象和DTO之间的转化。

```java
public interface DTOAssembler {
	public DTO createDTO(DO domainObject);
	public void updateDO(DTO  dataTransferObject);
	public DO createDO(DTO  dataTransferObject);
}
```

###### 3.DTO怎么使用？

对于不同的客户端展现，可以选择**一次封装**所有可能的数据组成DTO，也可以为每种展现**创建不同**的DTO。各有利弊。

*   单个大DTO，减少调用次数，只用创建一次，但是难以掌握传输的数据
    
*   不同的小DTO，要创建很多DTO，传输数据很清晰
    

对于输入方和输出方，可以共用一个DTO，也可以各准备一个DTO，视情况而定。

有部分团队 RPC 的请求和响应参数都通过 DTO 来承载，通过 XXRequestDTO 和 XXResponseDTO 来表示。

五、Entity（实体）
------------

实体，顾名思义，实体需要给予一个唯一标识，以区分其它实体，而值对象VO不需要。  
实体应该有一个生命周期，是有状态的，例如抽象订单有一个唯一识别号，订单有从下单创建到最后交货完成的生命周期，实体对象的状态可以变化。

1.与VO(值对象)的区别：  
只要两个实体对象的唯一标识相等，就判断两个对象相等，即使其他属性不同。可以修改实体状态。  
而VO(值对象）没有标识，所有属性相等，才判断两个对象相等。只能创建新的值对象，不能修改。

2.与PO（持久化对象）的区别：  
PO与数据表的一条记录对应，通常为了方便存储，会给PO赋予了一个主键ID。  
从而，PO也像实体一样具有了标识，Martin Flowler称之为**委派标识**，区别于实体标识。  
例如身份证号作为身份证的实体标识，唯一区分其他身份证。但是存储在数据库中，依然可能分配自增主键ID(1,2,3,…)。若值对象需要持久化，也会被分配委派标识，方便查询，或与外键关联。  
实体的标识与业务有关，PO的委派标识仅方便存储，与技术有关。

```java
//示例代码
public class Entity{
    private int id;
    int getId(){return id;}
}
```

六、VO(value object 值对象）
----------------------

值对象，通常用于业务层之间的数据传递，仅仅包含自身的数据。  
与实体的区别是，没有唯一标识，无生命周期，内部值是不变的。  
与PO的区别是，PO只在数据层，作为存储。VO在商业逻辑层和表示层，作为一个概念整体。

*   值对象通常是小而简单的对象，如货币、日期或地址这样的对象，判断相等时不根据标识ID。比如，年月日相同，就判断这两个对象相等。
*   值对象易于创建，参数传递时通常是传递值，而不是传递引用。
*   值对象不应被持久化，这个对象被创建后只能被引用，当没有引用时交给垃圾回收自动处理。

```java
//示例代码,比如Address这样无唯一标识的就是值对象
public class Address{
    private String country;
    private String province;
    private String city;
    public Address(String country, String province, String city) {
        this.country= country;
        this.province= province;
        this.city= city;
    }
    //省略equals方法
}
//调用值对象，若要修改值对象，值对象不用维护，直接创建一个全新的Address对象
//原对象直接被抛弃，而不是在原对象上进行修改
public Address changeAddress(String newCity, String newProvince, String newCity) {
    return new Address(newCity, newProvince, newCity);
}
```

理解了VO的意思，也就明白了，某些DTO也是一种值对象。历史上，在Martin Flowler称“值对象”的术语，在J2EE社团中称为“数据传输对象”，这在设计模式界引起了一场混乱。

七、VO（ View Object 显示层对象）
------------------------

Value Object和View Object的简写都是VO，可能容易弄混。View Object的含义是通常是Web向模板渲染引擎层传输的对象。《阿里巴巴开发手册》中建议把输出的显示层对象命名为VO。当然，也有人把这个对象命名为DTO作为传输。

```java
//Controller层
public HttpResult list(@RequestBody XXParam param){
    HttpResult vo=HttpResultUtils.convert(XXDTO);
    return vo;
}
```

由于很多页面需要额外数据，比如错误码、提示信息、分页信息等，查询的DTO之后需要再封装成View Object 显示层对象再显示出来

```json
{
	errcode: "00000",
	errmsg: "ok",
	data: {
		pageNum: 1, 
		pageSize: 10, 
		totalPage: 1, 
		total: 4, 
		list: [...]
	}
}
```

八、BO(business object 业务对象)
--------------------------

业务对象，就是把业务逻辑封装为一个对象（注意是对象本身的业务逻辑，而不是协调其它对象的逻辑），这个业务对象可以包括一个或多个其它的对象。

一般，实现业务的通常方式之一，是包括数据而不包含行为的领域对象（所谓“贫血模型”）+Service类来实现的。其中，业务逻辑是包含在service层里，随着业务不断演进，service类里的逻辑越来越复杂，越来越重，不利于重用。

而在《面向领域驱动设计》中，将对象本身的逻辑也封装在对象中（所谓“充血模型”），而service类仅仅起协调作用，比如对领域对象的调用及其它工具的调用，不包含业务本身的逻辑，是轻量级的薄薄一层，名为应用服务层。当业务不断演进时，通常只需要关注业务对象（BO）即可，而应用层面较少变化。  
因此，业务对象，也是领域对象（Domain Object）的另一说法。

业务对象（BO）通常是**实体**，或者是**聚合根**，包含多个实体或值对象，内部实现业务逻辑。

它是工具类Utils、服务类Service，像Controller，Service，Mapper等也可被称为业务对象（BO）。

此对象在实际使用中有不一样的理解，有的团队将 BO 当作 Service 返回给上层的 “专用 DTO” 使用；而有的团队则当作 Service 层内保存中间信息数据的 “DTO” 或者上下文对象来使用（建议采用这种理解）。

```java
//示例代码
public class User implements Serializable{
    private String name;
    private String password;
    //对象自身的业务逻辑
    public void changePassword(String newPassword){
        this.setPassword(newPassword);
    }
    //省略getter和setter方法
}
```

九、QO(query object 查询对象）
-----------------------

数据查询对象，各层接收上层的查询请求。注意，【强制】如果超过2个参数的查询封装，则禁止使用Map类传输。  
查询对象用于 Controller 层方法接收客户端的请求参数。

```java
public class MyQO {
  private String param1;
  private String param2;
  ...
}
@PostMapping("/post")
public String post(@RequestBody MyQO qo) {
  ......
}
```

以创建简历对象为例，简历可分为教育经历、工作经历、项目经历。先填写查询对象的信息，转换为业务对象，分成不同的表进行存储。

```java
MyBO bo = service.createBO(qo);//创建业务对象
bo.dosomething();
//将业务对象存储在不同的表中
MyPO po1 = service.createPO1(bo);
dao1.save(po1);
MyPO po2 = service.createPO2(bo);
dao2.save(po2);
MyPO po3 = service.createPO3(bo);
dao3.save(po3);
```

十、AO (Application Object 应用对象)
------------------------------

一般用在控制层和服务层之间。有些团队会将前端查询的属性和保存的属性几乎一致的对象封装为 AO，如读取用户属性传给前端，用户在前端编辑了用户属性后传回后端。这种用法将 AO 用做 Param 和 VO 或 Param 和 DTO 的组合。

```java
//Controller层
public HttpResult update(@RequestBody XXAO ao1){
	XXAO ao2 = XXService.update(ao1);
    HttpResult vo = HttpResultUtils.convert(ao2);
    return vo;
}
```

* * *

十一、总结
-----

POJO：简单Java对象，它没有任何限制和特定的约定，是一个普通的Java对象。  
DTO：数据传输对象，它是一个数据传输结构，通常用于不同进程间的数据传输，在不同层之间传递数据的对象。  
DAO：数据访问对象，是一个数据访问模式，在应用程序中它通常扮演着对数据库的访问。  
PO：持久化对象，通常指ORM（对象关系映射）中映射的数据库表对应的实体类。  
BO：业务对象，是应用程序中业务逻辑的实现。  
VO：值对象，它是一个用于存储数据的对象，通常是与UI/界面模型相关的对象。  
QO（Query）：查询对象，它主要用于定义查询条件和规则，用于接收前端传递的查询条件参数。  
ENTITY：实体对象，是一个与业务相关的对象，通常是与应用程序领域模型相关的对象。  
Param：表示请求参数，用于接收前端传递的参数  
Command：表示命令，用于接收前端传递的命令参数

> **各对象的命名习惯：**
> 
> *   PO通常放在名为bean、entity、model目录中。
> *   DAO本身就是一层，通常是DAO、mapper、repository目录。
> *   BO通常在service、manager、business，domain，model目录中。
> *   DTO通常在command、representation、DTO目录中。

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Java技能树](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)136371 人正在系统学习中

本文转自 <https://blog.csdn.net/qq_40610003/article/details/109007539>，如有侵权，请联系删除。