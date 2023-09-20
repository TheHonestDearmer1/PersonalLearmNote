# GO + Gin + GORM + MySql 实现最基础的 CRUD

## 什么是CRUD？ CRUD的操作

 CRUD是指在做计算处理时的增加(Create)、读取查询(Retrieve)、更新(Update)和删除(Delete)几个单词的首字母简写。主要被用在描述软件系统中DataBase或者[持久层](https://so.csdn.net/so/search?q=持久层&spm=1001.2101.3001.7020)的基本操作功能。

视频网址：[GO + Gin + GORM + MySql 实现最基础的 CRUD get请求全部数据和分页数据_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1GB4y1h7mz/?spm_id_from=333.999.top_right_bar_window_history.content.click&vd_source=a0e678f0a699f40cb533e1a6673f35fa)



## 准备工具

1.安装 go 的环境 https://www.runoob.com/go/go-environment.html

2.安装数据库mysql

3.安装一个测试工具，postman/apipost(apipost是中文，推荐)  [Apipost-API 文档、设计、调试、自动化测试一体化协作平台](https://www.apipost.cn/)

4. golang /vscode

5. gin和grom的中文文档

   https://www.kancloud.cn/shuangdeyu/gin_book/949412

   https://gorm.io/zh_CN/docs/

6. navicat 数据库的查询

## 功能介绍

使用测试工具发起请求

通过post请求127.0.0.1:3001/user/add 可以增加数据

通过delete请求127.0.0.1:3001/user/delete/id(这里填参数) 软删除数据

通过put请求127.0.0.1:3001/user/update/id(这里填参数) 更新数据

通过get请求127.0.0.1:3001/user/List 获取所有数据

通过get请求127.0.0.1:3001/user/List  传入pageSize query查询和 pageNUM query参数进行分页查询

Ctrl+ Shift+ N可以让vsc多开窗口

## 搭建服务端口

```go
package main

import (
	"fmt"
	"strconv"
	"time"

	"github.com/gin-gonic/gin" //加入gin
	"gorm.io/driver/mysql" //加入mysql
	"gorm.io/gorm"      //加入grom
	"gorm.io/gorm/schema" //加入grom
	//    "gorm.io/driver/sqlite"
)

func main() {
	//连接到数据库,用户名为root，密码为空，连接到的数据库名是curd-list
	dsn := "root:@tcp(127.0.0.1:3306)/curd-list?charset=utf8mb4&parseTime=True&loc=Local" //一般数据库的连接都是127.0.0.1:3306,不用改
	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{
		NamingStrategy: schema.NamingStrategy{
			SingularTable: true, // 使用单数表名，启用此选项后，“User”的表将为“Users”
		},
	})
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(db)

	sqlDB, err := db.DB()

	// SetMaxIdleConns设置空闲连接池中的最大连接数。
	sqlDB.SetMaxIdleConns(10)

	//SetMaxOpenConns设置数据库的最大打开连接数。
	sqlDB.SetMaxOpenConns(100)

	// SetConnMaxLifetime设置连接可以重复使用的最长时间。
	sqlDB.SetConnMaxLifetime(10 * time.Second) //十秒钟

	//定义表结构体
	type List struct {
		gorm.Model        //每次都要添加到结构体
		Name       string `gorm:"type:varchar(20); not null" json:"name" binding:"required"`
		State      string `gorm:"type:varchar(20); not null" json:"state" binding:"required"`
		Phone      string `gorm:"type:varchar(20); not null" json:"phone" binding:"required"`
		Email      string `gorm:"type:varchar(40); not null" json:"email" binding:"required"`
		Address    string `gorm:"type:varchar(200); not null" json:"address" binding:"required"` //binding:"required"是指这行数据必须填写
	}

	//1.主键没有    结构体添加gorm.Model
	//2.名称变成复数问题
	//AutoMigrate 会创建表、缺失的外键、约束、列和索引
	db.AutoMigrate(&List{}) //创建表

	//创建接口
	r := gin.Default()

	/*代码约定

	成功:200
	错误:400

	*/

	//测试
	r.GET("/", func(c *gin.Context) { //发起get请求，执行的函数操作
		c.JSON(200, gin.H{
			"message": "pong", //返回的json请求
		})
	})
    	//客户端的访问端口号  
	PORT := "3001"   //127.0.0.1:3001
	r.Run(":" + PORT) //运行端口 127.0.0.1:3001
}              
```

## POST增加接口

```go
	r.POST("/user/add", func(c *gin.Context) { //post请求访问127.0.0.1:3001/user/add
		var data List                  //创建List结构体对象
		err := c.ShouldBindJSON(&data) //ShouldBindJSON是gin框架提供的一个方法，用于将请求的JSON数据解析成结构体或map(传进data)，并将解析结果绑定到指定的变量上。

		//判断是否成功
		if err != nil {
			c.JSON(200, gin.H{
				"msg":  "添加失败",
				"data": gin.H{},
				"code": 400,
			})
		} else {
			//请求成功后进行数据库操作
			db.Create(&data) //在数据库中创建一条接收到的数据
			c.JSON(200, gin.H{
				"msg":  "添加成功",
				"data": gin.H{},
				"code": 200,
			})
		}
	})
```

## delete删除接口

```go
//删
	//1.找到对应的id所对应的条目
	//2.判断id是否存在
	//3.从数据库中删除
	//4.返回，id没有找到

	//restful 编码风格 风格

	//一般用 get和post ,实际上post和delete是一样的

	r.DELETE("/user/delete/:id", func(c *gin.Context) {
		//nam=name,:id,这样填，nam，id都是接收到的参数
		var data []List //创建表
		//接受 id
		id := c.Param("id")
		//判断 id是否存在
		db.Where("id= ?", id).Find(&data) //where为判断条件语句，如果存在，将参数传入data

		//id存在的情况，则删除，不存在则保存
		if len(data) == 0 {
			c.JSON(200, gin.H{
				"msg":  "id没有找到,删除失败",
				"code": 400,
			})

		} else {
			//操作数据库删除
			db.Where("id = ?", id).Delete(&data)
			c.JSON(200, gin.H{
				"msg":  "删除成功",
				"code": 200,
			})
		}
	})
```

## put修改接口

```go
//改
	//1.找到对应的id所对应的条目
	//2.判断id是否存在
	//3.更改条目
	//4.返回，id没有找到
	r.PUT("/user/update/:id", func(c *gin.Context) {
		var data List
		id := c.Param("id")                             //将参数传入id
		db.Select("id").Where("id = ?", id).Find(&data) //将找到的那一行id数据传入data
		if data.ID == 0 {                               //判断id是否存在
			c.JSON(200, gin.H{
				"msg":  "id不存在",
				"code": 400,
			})
		} else {
			err := c.ShouldBindJSON(&data) //将接收到的json参数传进data
			if err != nil {
				c.JSON(200, gin.H{
					"msg":  "更新失败",
					"code": 400,
				})
			} else {
				db.Where("id = ?", id).Updates(&data)
				c.JSON(200, gin.H{
					"msg":  "更新成功",
					"code": 200,
				})
			}
		}
	})

```

## get请求全部数据和分页数据

```go
//查 （条件查询，全部查询 / 分页查询）

	// 条件查询
	r.GET("/user/List/:name", func(c *gin.Context) {
		//获取路径参数
		name := c.Param("name")

		var dataList []List

		//查询数据库
		db.Where("name = ?", name).Find(&dataList)

		//判断是否查询到数据

		if len(dataList) == 0 {
			c.JSON(200, gin.H{
				"msg":  "找不到对应数据",
				"code": 400,
				"data": gin.H{},
			})
		} else {
			c.JSON(200, gin.H{
				"msg":  "找到对应数据",
				"code": 200,
				"data": dataList,
			})
		}

	})
	//全部查询
	r.GET("user/List", func(c *gin.Context) {
		var dataList []List
		var total int64 //总数据条数

		//查询全部数据，查询分页数据
		pageSize, _ := strconv.Atoi(c.Query("pageSize")) //Query意思是当json查询传入pageSize参数数据时候，返回的变量给pageSize
		pageNUM, _ := strconv.Atoi(c.Query("pageNUM"))   //int,_ = strconv.Atoi(string) 将string转成int类型
		//pageNUM 请求几条数据
		//Limit 限制页面大小，数据条数  Offset 翻页，第几页
		offsetVal := (pageNUM - 1) * pageSize //offsetVal 偏移值
		if pageSize == -1 && pageNUM == -1 {
			offsetVal = -1
		}
		//如果不需要翻页
		if pageSize == 0 {
			pageSize = -1
		}
		if pageNUM == 0 {
			pageNUM = -1
		}
		//查询数据
		db.Model(dataList).Count(&total).Limit(pageSize).Offset(offsetVal).Find(&dataList) //Limit(-1).Offset(-1)指的是查询所有数据，Model(dataList).Count(&total),Count记录数据条数,最后将数据传入dataList
		if len(dataList) == 0 {
			c.JSON(200, gin.H{
				"msg":  "没有查询到数据",
				"code": 400,
			})
		} else {
			c.JSON(200, gin.H{
				"msg":      "查询到数据",
				"code":     200,
				"data":     dataList,
				"total":    total,
				"pageSize": pageSize,
				"pageNUM":  pageNUM,
			})
		}
	})
```

## 完整代码

```go
package main

import (
	"fmt"
	"strconv"
	"time"

	"github.com/gin-gonic/gin"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
	"gorm.io/gorm/schema"
	//    "gorm.io/driver/sqlite"
)

func main() {
	//连接到数据库,用户名为root，密码为空，连接到的数据库名是curd-list
	dsn := "root:@tcp(127.0.0.1:3306)/curd-list?charset=utf8mb4&parseTime=True&loc=Local" //一般数据库的连接都是127.0.0.1:3306,不用改
	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{
		NamingStrategy: schema.NamingStrategy{
			SingularTable: true, // use singular table name, table for `User` would be `user` with this option enabled
		},
	})
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(db)

	sqlDB, err := db.DB()

	// SetMaxIdleConns设置空闲连接池中的最大连接数。
	sqlDB.SetMaxIdleConns(10)

	//SetMaxOpenConns设置数据库的最大打开连接数。
	sqlDB.SetMaxOpenConns(100)

	// SetConnMaxLifetime设置连接可以重复使用的最长时间。
	sqlDB.SetConnMaxLifetime(10 * time.Second) //十秒钟

	//结构体
	type List struct {
		gorm.Model        //每次都要添加到结构体
		Name       string `gorm:"type:varchar(20); not null" json:"name" binding:"required"`
		State      string `gorm:"type:varchar(20); not null" json:"state" binding:"required"`
		Phone      string `gorm:"type:varchar(20); not null" json:"phone" binding:"required"`
		Email      string `gorm:"type:varchar(40); not null" json:"email" binding:"required"`
		Address    string `gorm:"type:varchar(200); not null" json:"address" binding:"required"` //binding:"required"是指这行数据必须填写
	}

	//1.主键没有    结构体添加gorm.Model
	//2.名称变成复数问题
	//AutoMigrate 会创建表、缺失的外键、约束、列和索引
	db.AutoMigrate(&List{}) //创建表

	//接口
	r := gin.Default()

	/*代码约定

	成功:200
	错误:400

	*/

	//测试
	r.GET("/", func(c *gin.Context) { //发起get请求，执行的函数操作
		c.JSON(200, gin.H{
			"message": "pong", //返回的json请求
		})
	})

	//增

	r.POST("/user/add", func(c *gin.Context) {
		var data List                  //创建List结构体对象
		err := c.ShouldBindJSON(&data) //ShouldBindJSON是gin框架提供的一个方法，用于将请求的JSON数据解析成结构体或map(传进data)，并将解析结果绑定到指定的变量上。

		//判断是否成功
		if err != nil {
			c.JSON(200, gin.H{
				"msg":  "添加失败",
				"data": gin.H{},
				"code": 400,
			})
		} else {
			//请求成功后进行数据库操作
			db.Create(&data) //在数据库中创建一条接收到的数据
			c.JSON(200, gin.H{
				"msg":  "添加成功",
				"data": gin.H{},
				"code": 200,
			})
		}
	})
	/*{
	    "name":"张三",
	    "state":"在职",
	    "phone":"2445678",
	    "email":"234367@qq.com",
	    "address":"东莞",
	}
	//测试用的json
	*/

	//删
	//1.找到对应的id所对应的条目
	//2.判断id是否存在
	//3.从数据库中删除
	//4.返回，id没有找到

	//restful 编码风格 风格

	//一般用 get和post ,实际上post和delete是一样的

	r.DELETE("/user/delete/:id", func(c *gin.Context) {
		//nam=name,:id,这样填，nam，id都是接收到的参数
		var data []List //创建表
		//接受 id
		id := c.Param("id")
		//判断 id是否存在
		db.Where("id= ?", id).Find(&data) //where为判断条件语句，如果存在，将参数传入data

		//id存在的情况，则删除，不存在则保存
		if len(data) == 0 {
			c.JSON(200, gin.H{
				"msg":  "id没有找到,删除失败",
				"code": 400,
			})

		} else {
			//操作数据库删除
			db.Where("id = ?", id).Delete(&data)
			c.JSON(200, gin.H{
				"msg":  "删除成功",
				"code": 200,
			})
		}
	})
	//
	//改
	//1.找到对应的id所对应的条目
	//2.判断id是否存在
	//3.更改条目
	//4.返回，id没有找到
	r.PUT("/user/update/:id", func(c *gin.Context) {
		var data List
		id := c.Param("id")                             //将参数传入id
		db.Select("id").Where("id = ?", id).Find(&data) //将找到的那一行id数据传入data
		if data.ID == 0 {                               //判断id是否存在
			c.JSON(200, gin.H{
				"msg":  "id不存在",
				"code": 400,
			})
		} else {
			err := c.ShouldBindJSON(&data) //将接收到的json参数传进data
			if err != nil {
				c.JSON(200, gin.H{
					"msg":  "更新失败",
					"code": 400,
				})
			} else {
				db.Where("id = ?", id).Updates(&data)
				c.JSON(200, gin.H{
					"msg":  "更新成功",
					"code": 200,
				})
			}
		}
	})

	//查 （条件查询，全部查询 / 分页查询）

	// 条件查询
	r.GET("/user/List/:name", func(c *gin.Context) {
		//获取路径参数
		name := c.Param("name")

		var dataList []List

		//查询数据库
		db.Where("name = ?", name).Find(&dataList)

		//判断是否查询到数据

		if len(dataList) == 0 {
			c.JSON(200, gin.H{
				"msg":  "找不到对应数据",
				"code": 400,
				"data": gin.H{},
			})
		} else {
			c.JSON(200, gin.H{
				"msg":  "找到对应数据",
				"code": 200,
				"data": dataList,
			})
		}

	})
	//全部查询
	r.GET("user/List", func(c *gin.Context) {
		var dataList []List
		var total int64 //总数据条数

		//查询全部数据，查询分页数据
		pageSize, _ := strconv.Atoi(c.Query("pageSize")) //Query意思是当json查询传入pageSize参数数据时候，返回的变量给pageSize
		pageNUM, _ := strconv.Atoi(c.Query("pageNUM"))   //int,_ = strconv.Atoi(string) 将string转成int类型
		//pageNUM 请求几条数据
		//Limit 限制页面大小，数据条数  Offset 翻页，第几页
		offsetVal := (pageNUM - 1) * pageSize //offsetVal 偏移值
		if pageSize == -1 && pageNUM == -1 {
			offsetVal = -1
		}
		//如果不需要翻页
		if pageSize == 0 {
			pageSize = -1
		}
		if pageNUM == 0 {
			pageNUM = -1
		}
		//查询数据
		db.Model(dataList).Count(&total).Limit(pageSize).Offset(offsetVal).Find(&dataList) //Limit(-1).Offset(-1)指的是查询所有数据，Model(dataList).Count(&total),Count记录数据条数,最后将数据传入dataList
		if len(dataList) == 0 {
			c.JSON(200, gin.H{
				"msg":  "没有查询到数据",
				"code": 400,
			})
		} else {
			c.JSON(200, gin.H{
				"msg":      "查询到数据",
				"code":     200,
				"data":     dataList,
				"total":    total,
				"pageSize": pageSize,
				"pageNUM":  pageNUM,
			})
		}
	})

	//访问端口号
	PORT := "3002"
	r.Run(":" + PORT)
}

```

# 解决go build时error obtaining VCS status: exit status 128 Use -buildvcs=fals

[莫太冲](https://juejin.cn/user/272334613918430/posts)

2023-03-03 14:35319

当然是git有问题啦，你看看你的项目能不能`git pull` 我遇到这个问题是因为我的硬盘进行了挂载。 因为ubuntu desktop默认不是用root登录，而是用户自己创建的帐户登录。所以访问挂载硬盘上的文件属于root。用户在非root帐号操作git的时候，就遇到了问题，`ls -l `就可以看出问题所在。 现在网上有三种解决方案：

1. 降级成1.16
2. chown改文件所有权
3. `git config --global --add safe.directory '文件夹名'`

我用的第三种，匹配所有文件防止其它项目出错，命令如下，直接大力出奇迹。我都用ubuntu和git，还不知道自己下的什么东西么。

```bash
bash
复制代码git config --global --add safe.directory '*'
```
