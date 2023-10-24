**SSM**（Spring+SpringMVC+MyBatis）框架集由Spring、MyBatis两个[开源框架](https://baike.baidu.com/item/开源框架/23724803?fromModule=lemma_inlink)整合而成（SpringMVC是Spring中的部分内容），常作为[数据源](https://baike.baidu.com/item/数据源/5198928?fromModule=lemma_inlink)较简单的web项目的框架。

**Spring**

Spring就像是整个项目中装配bean的大工厂，在[配置文件](https://baike.baidu.com/item/配置文件/286550?fromModule=lemma_inlink)中可以指定使用特定的参数去调用[实体类](https://baike.baidu.com/item/实体类/9766323?fromModule=lemma_inlink)的[构造方法](https://baike.baidu.com/item/构造方法/10455265?fromModule=lemma_inlink)来实例化对象。也可以称之为项目中的粘合剂。

Spring的核心思想是IoC（[控制反转](https://baike.baidu.com/item/控制反转/1158025?fromModule=lemma_inlink)），即不再需要[程序员](https://baike.baidu.com/item/程序员/62748?fromModule=lemma_inlink)去显式地`new`一个对象，而是让Spring框架帮你来完成这一切。

**SpringMVC**

SpringMVC在项目中拦截用户请求，它的核心Servlet即[DispatcherServlet](https://baike.baidu.com/item/DispatcherServlet/12740507?fromModule=lemma_inlink)承担中介或是前台这样的职责，将用户请求通过HandlerMapping去匹配Controller，Controller就是具体对应请求所执行的操作。SpringMVC相当于SSH框架中[struts](https://baike.baidu.com/item/struts/485073?fromModule=lemma_inlink)。

**mybatis**

mybatis是对[jdbc](https://baike.baidu.com/item/jdbc/485214?fromModule=lemma_inlink)的封装，它让数据库底层操作变的透明。mybatis的操作都是围绕一个sql[SessionFactory](https://baike.baidu.com/item/SessionFactory/6659145?fromModule=lemma_inlink)实例展开的。mybatis通过配置文件关联到各实体类的[Mapper](https://baike.baidu.com/item/Mapper/17330783?fromModule=lemma_inlink)文件，Mapper文件中配置了每个类对数据库所需进行的[sql语句](https://baike.baidu.com/item/sql语句/5714895?fromModule=lemma_inlink)映射。在每次与数据库交互时，通过sqlSessionFactory拿到一个sqlSession，[再执行](https://baike.baidu.com/item/再执行/8533454?fromModule=lemma_inlink)sql命令。

页面发送请求给控制器，控制器调用[业务层](https://baike.baidu.com/item/业务层/22287753?fromModule=lemma_inlink)处理逻辑，逻辑层向[持久层](https://baike.baidu.com/item/持久层/3584971?fromModule=lemma_inlink)发送请求，持久层与数据库交互，后将结果返回给业务层，业务层将处理逻辑发送给控制器，控制器再调用视图展现数据。 

### 整合分析

1、spring MVC ＋ spring +mybatis，是标准的MVC设计模式，将整个系统划分为显示层，Controller层，Service层，DAO层四层

(1）spring实现业务对象管理

(2）Spring MVC负责请求的转发和视图管理

(3）mybatis作为数据对象的持久化引擎。

2、Spring是一个开源框架，Spring是一个轻量级的控制反转（IoC）和面向切面（AOP）的容器框架，还能更好的让其他框架整合。

3、Spring MVC框架是有一个MVC框架，通过实现Model-View-Controller模式来很好地将数据、业务与展现进行分离。

4、MyBatis 是一个基于Java的持久层框架