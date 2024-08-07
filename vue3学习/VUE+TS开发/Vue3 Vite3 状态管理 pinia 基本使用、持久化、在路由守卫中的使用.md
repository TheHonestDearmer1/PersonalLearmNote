持续创作，加速成长！这是我参与「掘金日新计划 · 10 月更文挑战」的第4天，[点击查看活动详情](https://juejin.cn/post/7147654075599978532 "https://juejin.cn/post/7147654075599978532")

在《基于 vite 创建 vue3 项目》一文中整合了 _pinia_，有不少伙伴不知道 _pinia_ 是什么，本文简单介绍 _pinia_。主要包括三方面：

1.  _pinia_ 的基本用法，在《基于 vite 创建 vue3 项目》中 demo 的基础上简单重构。
2.  如何持久化 _pinia_ 中的数据，保证浏览器刷新时，_pinia_ 中的数据不丢失；
3.  在 _vue-router_ 路由守卫中如何使用 _pinia_。

文中的 demo 仍然基于 vite

1 pinia 的使用
-----------

### 1.1 pinia 是什么

在 vue 2.x 中，_vuex_ 是官方的状态管理库，并且 vue 3 中也有对应的 _vuex_ 版本。但 vue 作者尤大神看了 _pinia_ 后，强势推荐使用 _pinia_ 作为状态管理库。下图是 vue 官网 “生态系统”，_pinia_ 是 vue 生态之一。

![image-20221009142022897](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1bdf5a905604c13a5158d3c4889773e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

### 1.2 pinia 的特点

1.  支持 vue2 和 vue3，两者都可以使用 _pinia_；
2.  语法简洁，支持 vue3 中 _setup_ 的写法，不必像 _vuex_ 那样定义 _state_、_mutations_、_actions_、_getters_ 等，可以按照 _setup_ _Composition API_ 的方式返回状态和改变状态的方法，实现代码的扁平化；
3.  支持 vuex 中 _state_、_actions_、_getters_ 形式的写法，丢弃了 _mutations_，开发时候不用根据同步异步来决定使用 _mutations_ 或 _actions_，pinia 中只有 _actions_；
4.  对 _TypeScript_ 支持非常友好。

### 1.3 pinia 的使用

在《基于 vite 创建 vue3 项目》中已经整合了 pinia，现简单回顾并进行一些调整。

1.  安装 _pinia_ 依赖：

shell

复制代码

`yarn add pinia`

2.  创建 pinia 实例（根存储 root store）：

之前咱是在 _main.ts_ 中创建的，现将其抽取到独立的文件中：

_src/store/index.ts_：

typescript

复制代码

`import { createPinia } from 'pinia' const pinia = createPinia() export default pinia`

3.  在 _main.ts_ 中以插件的方式传递给 _App_ 实例。

typescript

复制代码

`... import pinia from '@/store' ... app.use(pinia) ...`

4.  在 _store/_ 目录下创建 _modules_ 目录，存储每个模块的状态，将之前的 demo.ts 移动到 _store/modules/_ 中。这里使用最新的 _Composition API_ _setup_ 的方式来定义状态。

_src/store/modules/demo.ts_：

typescript

复制代码

`import { defineStore } from 'pinia' import { ref } from 'vue' const useDemoStore = defineStore('demo', () => {   const counter = ref(0)   const increment = () => {     counter.value++   }   return {     counter,     increment   } }) export default useDemoStore`

5.  在组件 _about.vue_ 中使用 _demo_ 中的状态 _counter_ 和改变状态的函数 _increment_。代码和之前一样。

先引入 _demo.ts_ 中定义的 _useDemoStore_ 函数，通过该函数创建 _demoStore_ 实例。然后就可以调用 demoStore 的状态 _counter_ 和 _increment_ 函数了。这里需要注意，无论是 _pinia_ 还是 _vuex_，通过解构的方式获取状态，会导致状态失去响应性。如：

typescript

复制代码

`const { counter } = demoStore`

此时的 counter 会丢失响应性，当其值改变时，其他组件不会监听到。所以 _pinia_ 提供了 _storeToRefs_ 函数，使其解构出来的状态仍然具备响应性。

typescript

复制代码

`const { counter } = storeToRefs(demoStore)`

_src/views/about.vue_ 完整代码如下：

html

复制代码

`<template>   <div class="about">     <h1>This is an about page</h1>     <h3>counter: {{counter}}</h3>     <el-button @click="add">       <el-icon-plus></el-icon-plus>     </el-button> <div>   <svg-icon icon="http://www.yygnb.com/demo/car.svg"></svg-icon>   <svg-icon icon="car"></svg-icon>   <svg-icon class-name="icon" icon="http://www.yygnb.com/demo/car.svg"></svg-icon>   <svg-icon class-name="icon" icon="car"></svg-icon> </div>   </div> </template> <script lang="ts" setup> import useDemoStore from '@/store/modules/demo' import { storeToRefs } from 'pinia' import SvgIcon from '@/components/svg-icon/index.vue' const demoStore = useDemoStore() const { counter } = storeToRefs(demoStore) const add = () => {   demoStore.increment() } </script> <style scoped> .icon {   color: cornflowerblue;   font-size: 30px; } </style>`

最后在浏览器中访问 about 页面，可以正常运行，点击加号按钮，计数器会加1。

![image-20221009145753908](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08f6de8287764808904364cc40c9f087~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

2 持久化 pinia 状态
--------------

### 2.1 为什么需要持久化 pinia 状态

在上面的 demo 中，假设计数器加到 5，如果刷新浏览器，_counter_ 的值又会被初始化为 0。这是因为状态是存储在浏览器内存中的，刷新浏览器后，重新加载页面时会重新初始化 _vue_、 _pinia_，而 _pinia_ 中状态的值仅在内存中存在，而刷新导致浏览器存储中的数据没了，所以 _counter_ 的值就被初始化为 0。

在实际开发中，浏览器刷新时，有些数据希望是保存下来的。如用户登录后，用户信息会存储在全局状态中，如果不持久化状态，那么每次刷新用户都需要重新登录了。

要解决这个问题非常简单，在状态改变时将其同步到浏览器的存储中，如 _cookie_、_localStorage_、_sessionStorage_ 。每次初始化状态时从存储中去获取初始值即可。

说起来思路很简单，可真正实现起来就各种问题了，所以咱们就使用 _pinia_ 的插件 _pinia-plugin-persistedstate_ 来实现。

### 2.2 pinia-plugin-persistedstate

接下来就使用 _pinia-plugin-persistedstate_ 插件实现 _pinia_ 状态的持久化。

1.  安装依赖：

shell

复制代码

`yarn add pinia-plugin-persistedstate`

2.  引入该插件，在创建 _pinia_ 实例时传入该插件

_src/store/index.ts_：

typescript

复制代码

`import { createPinia } from 'pinia' import piniaPluginPersistedstate from 'pinia-plugin-persistedstate' const pinia = createPinia() pinia.use(piniaPluginPersistedstate) export default pinia`

3.  在需要持久化状态的模块中设置 _persist_。咱假设 _demo_ 模块需要对状态需要持久化，_defineStore_ 第一个参数定义唯一的模块名，第二个参数传递 _setup_，其实还有第三个参数 _options_，在 _options_ 中便可开启 _persist_：

_src/store/modules/demo.ts_：

typescript

复制代码

`... const useDemoStore = defineStore('demo', () => { 	... }, {   persist: true })`

此时改变 _counter_ 的值后，刷新浏览器，_counter_ 不会被重置为 0，仍然停留在刷新前的状态。

_persist_ 支持多种类型的值，最简单的就是传递 _true_，此时会将状态缓存在 _localStorage_ 中，该 _localStorage_ 的 key 为模块名（_defineStore_ 的第一个参数）,value 为该模块的状态对象，由于该模块只有一个状态 _counter_，故value为 _{"counter":8}_。如下图：

![image-20221009151822704](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4e960feae324f3a8375c94ff22c8f01~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

如果需要将其存储在 _sessionStorage_ 中，就需要设置 _persist_ 的值为一个对象：

typescript

复制代码

`... const useDemoStore = defineStore('demo', () => { 	... }, {   persist: {     key: 'aaa',     storage: sessionStorage   } })`

此时状态就会同步缓存到 sessionStorage 中，并且key 为咱们指定的 _key_：

![image-20221009152105536](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e0b935dc8d44da59f7703eb5c95ea14~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

_persist_ 对象类型为 _PersistedStateOptions_，上面演示了 _key_ 和 _storage_ 属性，该对象的其他属性如下：

typescript

复制代码

`} interface PersistedStateOptions {     /**      * Storage key to use.      * @default $store.id      */     key?: string;     /**      * Where to store persisted state.      * @default localStorage      */     storage?: StorageLike;     /**      * Dot-notation paths to partially save state. Saves everything if undefined.      * @default undefined      */     paths?: Array<string>;     /**      * Customer serializer to serialize/deserialize state.      */     serializer?: Serializer;     /**      * Hook called before state is hydrated from storage.      * @default null      */     beforeRestore?: (context: PiniaPluginContext) => void;     /**      * Hook called after state is hydrated from storage.      * @default undefined      */     afterRestore?: (context: PiniaPluginContext) => void; }`

3 在路由守卫中使用状态
------------

前面演示了在组件中使用 _pinia_，在组件外如何使用呢？这里演示在全局路由守卫中获取状态值。咱们创建一个路由守卫，在路由守卫中使用 nprogress 显示页面加载进度条。

### 3.1 创建全局路由守卫

1.  安装 _nprogress_

shell

复制代码

`yarn add nprogress yarn add @types/nprogress -D` 

2.  创建全局路由守卫

_src/router/guard/index.ts_：

typescript

复制代码

`import router from '@/router' import nProgress from 'nprogress' import 'nprogress/nprogress.css' nProgress.configure({   showSpinner: false }) // 全局前置守卫 router.beforeEach((to, from) => {   nProgress.start()   return true }) // 全局后置钩子 router.afterEach(() => {   nProgress.done(true) })`

3.  在 _main.ts_ 中引入全局路由守卫：

typescript

复制代码

`... import '@/router/guard/index' ...`

此时路由切换时，页面顶部会出现加载进度条，路由切换完成时该进度条消失。如果效果不明显，可在前置守卫中 _setTimeout_ 查看效果（个人觉得没这必要，画蛇添足）：

typescript

复制代码

`// 全局前置守卫 router.beforeEach((to, from) => {   nProgress.start()   return new Promise(resolve => {     setTimeout(() => {       resolve(true)     }, 1000)   }) })`

### 3.2 全局守卫中使用全局状态

实际开发中，路由切换时，可能需要从全局状态中获取 _token_ 等信息，判断是否能进入下一个页面。这里演示路由切换时获取 _demo_ 中的 _counter_ 的值。

首先试试在钩子函数外面使用全局状态：

typescript

复制代码

``... import useDemoStore from '@/store/modules/demo' import { storeToRefs } from 'pinia' ... const demoStore = useDemoStore() const { counter } = storeToRefs(demoStore) // 全局前置守卫 router.beforeEach((to, from) => {   nProgress.start()   // 从 store 中获取其他值，再决定返回值   // 这里演示获取 store 中 counter 的值   console.log(`counter：${counter}`)   return true }) ...``

此时浏览器控制台会报如下错误，这是因为 pinia 还没有挂载到 app 上。

![image-20221009155414238](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/793e692a1fde4be4a3b287c8ba73bf43~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

网上有些解决方案是直接实例化一个 _pinia_ 实例，传递给 _useDemoStore()_ 函数，如下：

typescript

复制代码

`... import useDemoStore from '@/store/modules/demo' import { storeToRefs } from 'pinia' import pinia from '@/store' ... const demoStore = useDemoStore(pinia) const { counter } = storeToRefs(demoStore) ...`

这样做，浏览器控制台不报错了，页面也可以正常加载，路由切换时，控制台会输出当前 _counter_ 的值。

但是如果刷新浏览器，_counter_ 的值又被初始化为 0，貌似前面设置的持久化插件 _pinia-plugin-persistedstate_ 失效了。那应该怎么处理呢？

### 3.3 正确的处理方式

上面这种传递 _pinia_ 对象给 _useDemoStore()_ 函数只是一种野路子，_pinia_ 官网已经清楚写明组件外应该如何使用 _pinia_:

![image-20221009160056386](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38839beeea6a4220ac6436785de3830b~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

在钩子函数外，_pinia_ 还没有被挂载，但是在前置守卫函数中，pinia 已经被挂载了，所以获取全局状态，需要在钩子函数中进行，正确的实现如下：

typescript

复制代码

``import router from '@/router' import nProgress from 'nprogress' import 'nprogress/nprogress.css' import useDemoStore from '@/store/modules/demo' import { storeToRefs } from 'pinia' nProgress.configure({   showSpinner: false }) // 全局前置守卫 router.beforeEach((to, from) => {   nProgress.start()   const demoStore = useDemoStore()   const { counter } = storeToRefs(demoStore)   // 从 store 中获取其他值，再决定返回值   // 这里演示获取 store 中 counter 的值   console.log(`counter：${counter.value}`)   return true }) // 全局后置钩子 router.afterEach(() => {   nProgress.done(true) })``

文中 demo 在 github 上搜索 _vue3-vite-archetype_，_main_ 分支可以直接 _yarn dev_ 启动运行； _template_ 分支是 _yyg-cli_ 执行 _yyg create_ 创建项目时拉取的模板。你也可以先执行 _npm install -g yyg-cli_ 安装 _yyg-cli_ 脚手架工具，然后通过 _yyg create xxx_ 创建项目，创建后的项目包含了 _vue3 vite_ 的全部demo。

感谢你阅读本文，如果本文给了你一点点帮助或者启发，还请三连支持一下，点赞、关注、收藏，作者会持续与大家分享更多干货

本文转自 <https://juejin.cn/post/7152774411571953677>，如有侵权，请联系删除。