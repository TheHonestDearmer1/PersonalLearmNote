 

### 一、概述

       Promise是[异步编程](https://so.csdn.net/so/search?q=%E5%BC%82%E6%AD%A5%E7%BC%96%E7%A8%8B&spm=1001.2101.3001.7020)的一种解决方案，可以替代传统的解决方案--回调函数和事件。ES6统一了用法，并原生提供了Promise对象。作为对象，Promise有以下两个特点：

(1)对象的状态不受外界影响。

(2)一旦状态改变了就不会再变，也就是说任何时候Promise都只有一种状态。

### 二、Promise的状态

       Promise有三种状态，分别是 Pending (进行中)、Resolved (已完成)、Rejected (已失败)。Promise从Pending状态开始，如果成功就转到成功态，并执行resolve回调函数；如果失败就转到失败状态并执行reject回调函数。

Promise 提供了链式调用的方法，例如 then 、catch 和 finally。通过这些方法，可以在 Promise 完成或失败后执行相应的操作。then 方法接收两个回调函数作为参数，第一个回调函数在 Promise 被 Fulfilled 时执行，接收成功的结果作为参数；第二个回调函数在 Promise 被 Rejected 时执行，接收错误信息作为参数。catch 方法用于捕获发生的错误，而 finally 方法则在 Promise 完成后无论成功或失败都会执行。例如：

```js
promise
  .then((result) => {
    // 处理成功的结果
  })
  .catch((error) => {
    // 处理错误信息
  })
  .finally(() => {
    // 执行清理操作
  });
```



### 三、基本用法

       可以通过Promise的构造函数创建Promise对象

```javascript
var promise = new Promise((resolve,reject) => {
  setTimeout(()=>{
    console.log("hello world")
}, 2000)
})
```

       Promise构造函数接受一个函数作为参数，该函数的两个参数是 resolve ，reject，它们由JavaScript引擎提供。其中 resolve 函数的作用是当Promise对象转移到成功，调用resolve并将操作结果作为其参数传递出去；reject 函数的作用是当Promise对象的状态变为失败时，将操作报出的错误作为参数传递出去。如如下代码：

```javascript
function greet(){  
    var promise = new Promise(function(resolve,reject){ 
        var greet = "hello world"    
        resolve(greet)
    }) 
    return promise
}
greet().then(
    v=>{  
        console.log(v)//*
    })
```

上面的 \* 行的输出就是greet的值，也就是 resolve() 传递出来的参数。

> **注意：**创建一个Promise对象会立即执行里面的代码，所以为了更好的控制代码的运行时刻，可以将其包含在一个函数中，并将这个Promise作为函数的返回值。

### 四、Promise的then方法

       promise的then方法带有一下三个参数：成功的回调，失败的回调，前进的回调。一般情况下只需要实现第一个，后面的是可选的。Promise中最为重要的状态，通过then的状态传递可以实现的回调函数链式操作的实现。先执行以下代码：

```javascript
function greet () {
  var promise = new Promise (function(resolve, reject){
    var greet = "hello world"
    resolve(greet)
  })
  return promise
}
var p = greet().then(v => {
  console.log(v)  // hello world
})
console.log(p)  // Promise { <pending> }
```

       从中可以看出promise执行then还是一个promise，并且Promise的执行是异步的。因为 hello world 在最后一条输出语句的前面就打印出来了，且Promise的状态为pending(进行中)。

因为Promise执行then后还是Promise，所以就可以根据这一特性，不断的链式调用回调函数。下面是一个例子：

```javascript
function greet () {
  var promise = new Promise(function (resolve, reject){
    var greeet = "hello world"
    resolve(greet)
  })
  return promise
}
greet().then(v => {
  console.log(v+1)
  return v
})
.then (v => {
  console.log(v+2)
  return v
})
.then (v => {
  console.log(v+3)
})
```

### 五、Promise的其他方法

#### reject用法

 reject的作用就是把Promise的状态从pending置为rejected，这样在then中就能捕捉到reject的回调函数

```javascript
function judgeNumber (num) {
  var promise = new Promise (function(resolve, reject) {
    num = 5
    if(num < 5){
      resolve("num小于5，值为" + num)
    } else {
      reject("num不小于5，值为" + num)
    }
  })
  return promise
}
 
judgeNumber().then(
  function (message) {
    console.log(message)
  },
  funtion (message) {
    console.log(message)
  }
)
```

.then 后包含有两个方法，前一个执行resolve回调的参数，后一个执行reject回调的参数

#### catch用法

```javascript
function judgeNumber(num){
    var promise1 = new Promise(function(resolve,reject){
        num =5;
        if(num<5){
            resolve("num小于5，值为："+num);
        }else{
            reject("num不小于5，值为："+num);
        }
    });
    return promise1;
}
 
judgeNumber().then(
    function(message){
        console.log(message);
    }
)
.catch(function(message){
    console.log(message);
})
```

       这个时候`catch`执行的是和`reject`一样的，也就是说如果Promise的状态变为reject时，会被catch捕捉到，不过需要特别注意的是如果前面设置了reject方法的回调函数，·则catch不会捕捉到状态变为`reject`的情况。`catch`还有一点不同的是，如果在`resolve`或者`reject`发生错误的时候，会被`catch`捕捉到，这与java，c++的错误处理时一样的，这样就能避免程序卡死在回调函数中了。

#### all用法

Promise的all方法提供了并行执行异步操作的能力，在all中所有异步操作结束后才执行回调。

```javascript
function p1(){
    var promise1 = new Promise(function(resolve,reject){
        console.log("p1的第一条输出语句");
        console.log("p1的第二条输出语句");
        resolve("p1完成");
    })
    return promise1;
}
 
function p2(){
    var promise2 = new Promise(function(resolve,reject){
        console.log("p2的第一条输出语句");
        setTimeout(()=>{console.log("p2的第二条输出语句");resolve("p2完成")},2000);
 
    })
    return promise2;
}
 
function p3(){
    var promise3 = new Promise(function(resolve,reject){
        console.log("p3的第一条输出语句");
        console.log("p3的第二条输出语句");
        resolve("p3完成")
    });
    return  promise3;
}
 
Promise.all([p1(),p2(),p3()]).then(function(data){
    console.log(data);
})
```

#### race用法

       在all中的回调函数中，等到所有的Promise都执行完，再来执行回调函数，race则不同，它等到第一个Promise改变状态就开始执行回调函数。将上面的\`all\`改为\`race\`,得到

```javascript
Promise.race([p1(),p2(),p3()]).then(function(data){
    console.log(data);
})
```

> 这里还需要注意一个问题，promise的执行时异步的，比如下面这样：

```javascript
var i
 
var promise = new Promise(function(resolve,reject){
    resolve("hello");
})
 
promise.then(data=>{
    i = 2;
 
})
console.log(i);
```

       得到的结果是undefined,这不是因为promise不能改变外部的值，而是因为当执行`console.log(i)`时，`then()`方法还没执行完。如果你将console.log(i)延迟输出就可以得到正确的结果：

```javascript
setTimeout(()=>console.log(i),1000);
```

       所以不要在promise后面执行一些依赖promise改变的代码，因为可能promise中的代码并未执行完，或者你可以将其延迟输出。

本文转自 <https://blog.csdn.net/zyf971020/article/details/127015351>，如有侵权，请联系删除。