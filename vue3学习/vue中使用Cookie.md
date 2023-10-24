## 一.安装

```cmd
npm install vue-cookies -s
```

## 二.全局配置

```js
// 全局配置cookie，组件调用方式：this.$cookies
import cookies from 'vue-cookies'
Vue.prototype.$cookies = cookies; 
//配置cookies生命周期，单位不区分大小写
this.$cookies.config('1d') //填的值1d为一天,1h为一小时,1min为一分钟,1s为1秒：如下表

// y    year（年）
// m    month（月）
// d    day（日）
// h    hour（时）
// min    minute（分）
// s    second（秒）
```

## 三.使用

```js
1.存储值：
this.$cookies.set(key,value)  -&gt;  this.$cookies.set('userName','张三')
2.获取值：
this.$cookies.get(key)
3.删除cookie值
this.$cookies.remove(key)
4.获取所有cookies返回为数组的形式:this.$cookies.keys(key)
5.检查某个cookies的value是否存在:this.$cookies.isKey(key)
6.删除后如果没有重启浏览器，cookies的key还在的,不过value为空。
```



## 4.其它模块中使用

```js
import cookies from 'vue-cookies'
cookies.set('userName','张三')
cookies.get('userName')
```

