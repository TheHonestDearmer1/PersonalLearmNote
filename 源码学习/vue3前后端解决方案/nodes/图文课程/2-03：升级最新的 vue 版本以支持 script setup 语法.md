# 升级最新的 vue 版本以支持 script setup 语法

同学们大家好！

因为使用 `@vue/cli-v4.5.13` 版本创建的项目中，`vue` 的版本为 `v 3.0.0` 。

但是我们的项目需要使用最新的 `script setup 语法`，该语法在 `v 3.0.0` 版本中是不支持的，所以我们需要升级 `vue` 版本。

大家可以通过以下指令进行升级：

执行：

```js
npm i vue@3.2.8 vue-router@4.0.11 vuex@4.0.2
```

升级之后，查看 `package.json` 得到的版本应为：

```json
"vue": "^3.2.8",
"vue-router": "^4.0.11",
"vuex": "^4.0.2"
```

