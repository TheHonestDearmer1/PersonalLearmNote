# 使用 vue-cli 创建项目

同学们，这一小节我们需要创建一个 `vue3` 的项目，而创建项目的方式依然是通过 `vue-cli` 进行创建。

不过这里有一点大家需要注意，因为我们需要使用最新的模板，所以请保证你的 `vue-cli` 的版本在 `4.5.13` 以上，你可以通过以下的方式来查看你的 `vue-cli` 版本：

```
vue -V
------
@vue/cli 4.5.13 // 输出版本号
```

如果你需要升级版本，那么可以通过以下指令进行升级：

```
npm update -g @vue/cli
```

具体的方式也可以点击 [这里](https://cli.vuejs.org/zh/guide/installation.html) 进行参考。

升级之后，即可通过以下方式创建最新的 `vue3` 项目，终端输入 `vue create 项目名称` ，即可进入 **模板选择**

```js
// 利用 vue-cli 创建项目
vue create imooc-admin
// 进入模板选择
Vue CLI v4.5.13
? Please pick a preset:
  Default ([Vue 2] babel, eslint)
  Default (Vue 3) ([Vue 3] babel, eslint) 
> Manually select features  // 选择手动配置
// ----------------------------------------------------------
? Check the features needed for your project: 
 (*) Choose Vue version // 选择 vue 版本
 (*) Babel // 使用 babel
 ( ) TypeScript // 不使用 ts
 ( ) Progressive Web App (PWA) Support // 不使用 PWA
 (*) Router // 添加 vue-router
 (*) Vuex // 添加 vuex
>(*) CSS Pre-processors // 使用 css 预处理器
 (*) Linter / Formatter // 代码格式化
 ( ) Unit Testing // 不配置测试
 ( ) E2E Testing  // // 不配置测试
// ----------------------------------------------------------
 Choose a version of Vue.js that you want to start the project with 
  2.x
> 3.x // 选择 vue 3.0 版本
// ----------------------------------------------------------
 Use history mode for router? (Requires proper server setup for index fallback in production) (Y/n) n // 不使用 history模式 的路由
// ----------------------------------------------------------
 ? Pick a CSS pre-processor (PostCSS, Autoprefixer and CSS Modules are supported by default): 
> Sass/SCSS (with dart-sass) // 使用基于 dart-sass 的 scss 预处理器
  Sass/SCSS (with node-sass) 
  Less
  Stylus
// ----------------------------------------------------------
? Pick a linter / formatter config: 
  ESLint with error prevention only 
  ESLint + Airbnb config
> ESLint + Standard config // 使用 ESLint 标准代码格式化方案
  ESLint + Prettier 
// ----------------------------------------------------------
? Pick additional lint features: 
 (*) Lint on save //  
>(*) Lint and fix on commit  // 保存时 && 提交时，都进行 lint
// ----------------------------------------------------------
? Where do you prefer placing config for Babel, ESLint, etc.? (Use arrow keys)
> In dedicated config files // 单独的配置文件
  In package.json
// ----------------------------------------------------------
 Save this as a preset for future projects? (y/N) n // 不存储预设
```

等待片刻之后，你的项目就会生成成功。

生成之后，可以通过以下两个指令来运行你的项目：

```
cd 项目目录
npm run serve
```

执行成功之后，项目即可运行！