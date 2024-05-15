#小满Router（第一章入门）
## 1，前言

router 路由

应为vue是单页应用不会有那么多html 让我们跳转 所有要使用路由做页面的跳转

Vue 路由允许我们通过不同的 URL 访问不同的内容。通过 Vue 可以实现多视图的单页Web应用

## 2.安装

 构建前端项目

```
npm init vue@latest
//或者
npm init vite@latest
```

使用Vue3 安装对应的router4版本

使用Vue2安装对应的router3版本

```
npm install vue-router@4
```

在src目录下面新建router 文件 然后在router 文件夹下面新建 index.js

```js
//引入路由对象
import { createRouter, createWebHistory } from 'vue-router'

// 定义一些路由
// 每个路由都需要映射到一个组件。
const routes = [
  {
    path: '/',
    component: () => import('../components/a.vue')
  },
  {
    path: '/register',
    component: () => import('../components/b.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

//导出router
export default router
```

`router-link`

请注意，我们没有使用常规的 `a` 标签，而是使用一个自定义组件 `router-link` 来创建链接。这使得 Vue Router 可以在不重新加载页面的情况下更改 URL，处理 URL 的生成以及编码。我们将在后面看到如何从这些功能中获益。

#### `router-view`

`router-view` 将显示与 url 对应的组件。你可以把它放在任何地方，以适应你的布局。

app.vue中

```vue
<script setup> 
</script>

<template>
<router-view></router-view>
</template>
```

或者

```vue
<router-view />
```

最后在main.js 挂载

```js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
createApp(App).use(router).mount('#app')
```

