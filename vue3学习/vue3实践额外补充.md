# v-on

v-on检测鼠标移动悬浮：

```vue
<template>
  <div
    class="hover-view"
    @mouseover="mouseover"
    @mouseenter="mouseenter"
    @mousemove="mousemove"
    @mouseout="mouseout"
    @mouseleave="mouseleave"
    @mousedown="mousedown"
    @mouseup="mouseup"
  >
  </div>
</template>
 
<script>
export default {
  methods: {
    // 1、进入元素
    mouseover () {
      console.log('mouseover')
    },
    // 2、进入元素
    mouseenter () {
      console.log('mouseenter')
    },
    // 3、移动
    mousemove () {
      console.log('mousemove')
    },
    // 4、离开元素
    mouseout () {
      console.log('mouseout')
    },
    // 5、离开元素
    mouseleave () {
      console.log('mouseleave')
    },
    // 6、鼠标在元素上 按下
    mousedown () {
      console.log('mousedown')
    },
    // 7、鼠标在元素上 抬起
    mouseup () {
      console.log('mouseup')
    }
  }
}
</script>
 
<style>
.hover-view {
  width: 100px;
  height: 100px;
  background-color: red;
}
</style>
```

# v-bind

使用v-bind来决定元素处于什么状态：

```vue
<button
  v-for="(_, tab) in tabs"
  :key="tab"
  :class="['tab-button', { active: currentTab === tab }]"
  @click="currentTab.value = tab"
>
  {{ tab }}
</button>
```

`{ active: currentTab === tab }` 是一个动态绑定的对象，它用来控制当前选中的按钮是否展示为活动状态。

# 子组件传值，影响父组件

方法一（目前有问题）：

父组件可以通过 `v-on` 或 `@` **来选择性地监听子组件上抛的事件，就像监听原生 DOM 事件那**样：

```vue
<BlogPost
  ...
  @enlarge-text="postFontSize += 0.1"
 />
```

子组件可以通过调用内置的 [**`$emit`** 方法](https://cn.vuejs.org/api/component-instance.html#emit)，通过传入事件名称来抛出一个事件：

```vue
<!-- BlogPost.vue, 省略了 <script> -->
<template>
  <div class="blog-post">
    <h4>{{ title }}</h4>
    <button @click="$emit('enlarge-text')">Enlarge text</button>
  </div>
</template>
```

因为有了 `@enlarge-text="postFontSize += 0.1"` 的监听，父组件会接收这一事件，从而更新 `postFontSize` 的值。

因此，h4 字体大小的增加是通过点击按钮触发自定义事件 `enlarge-text`，在 App.vue 文件中执行 `postFontSize += 0.1` 操作，并将 `postFontSize` 的值作为字体大小的单位应用于具有样式类 `blog-post` 的 `<div>` 元素中。

[在演练场中尝试一下](https://play.vuejs.org/#eNp1Uk1PwkAQ/SuTxqQYgYp6ahaiJngzITHRA/UAZQor7W7TnaK16X93th8UEuHEvPdm5s3bls5Tmo4POTq+I0yYyZTAIOXpLFAySXVGUEKGEVQQZToBl6XukXqO9XahDbXc2OsAO5FlAIEKtWJByqCBqR01WFqiBLnxYTIEkhSjD+5rAV86zxQW8C1pB+88Aaphr73rtXbNVqrtBeV9r/zYFZYHacBoiHLFykB9Xgfq1NmLVvQmf7E1OGFaeE0anAMXhEkarwhtRWIjD+AbKmKcBk4JUdvtn8+6ARcTu87hLuCf6NJpSoDDKNIZj7BtIFUTUuB0tL/HomXHcnOC18d1TF305COqeJVtcUT4Q62mtzSF2/GkE8/E8b1qh8Ljw/if8I7nOkPn9En/+Ug2GEmFi0ynZrB0azOujbfB54kki5+aqumL8bING28Yr4xh+2vePrI39CnuHmZl2TwwVJXwuG6ZdU6kFTyGsQz33HyFvH5wvvyaB80bACwgvKbrYgLVH979DQc=)

**方法二：（可用）**

我们可以通过 [`defineEmits`](https://cn.vuejs.org/api/sfc-script-setup.html#defineprops-defineemits) 宏来声明需要抛出的事件：

在父组件中给子组件绑定v-on函数，双引号的是在父组件定义的函数enlarge-text：

```vue
<子组件 @enlarge-text="enlarge-text"></子组件>
```

在子组件中引用：

```vue
<script setup>
const emit = defineEmits(['enlarge-text'])

emit('enlarge-text', payload)//payload是子组件传给父组件函数的参数
</script>
```

TypeScript 用户请参考：[为组件 emits 标注类型](https://cn.vuejs.org/guide/typescript/composition-api.html#typing-component-emits)

方法三：

1. ```js
   import { getCurrentInstance } from 'vue';
   ```

2. 然后，通过使用 `getCurrentInstance()` 方法获取当前组件实例，并使用 `$emit` 方法来触发事件。这样，你可以在<script setup>代码中调用 `$emit`。

   ```js
   defineEmits(['eventName'])
   const instance = getCurrentInstance();
   instance.emit('eventName', payload);
   ```

   或者你也可以将其拆分为两个步骤：

   ```js
   const emit = instance.emit;
   emit('eventName', payload);
   ```

请确保在正确的上下文中使用 `$emit` 方法，并导入必要的依赖项以及获取当前组件实例。如果你仍然遇到问题，请提供更多的代码，以便我更好地帮助你解决问题。

在 Vue.js 中，父组件和子组件之间的通信可以通过 props 和自定义事件来实现。当父组件的按钮被点击时，可以触发一个自定义事件，并将需要传递的数据作为参数传递给子组件。子组件可以监听该事件，并在事件处理程序中接收到数据后进行相应的操作。



# 父代传值给子代的值能够正常跟着父代变化的写法：

App.vue(父代) setup写法

```vue
<script setup>
import { ref } from 'vue'
import Comp from "./Comp.vue"

const msg = ref(true)
function msg_change( ){
    msg.value = !msg.value
}
</script>

<template>
  <h1>父代:{{ msg }}</h1>
  <Comp :msg="msg"></Comp>
  <button @click="msg_change">改变</button>
</template>
```

去掉setup的写法：

```vue
<template>
  <h1>父代: {{ msg }}</h1>
  <Comp :msg="msg"></Comp>
  <button @click="msg_change">改变</button>
</template>

<script>
import Comp from "./Comp.vue"

export default {
  components: {
    Comp
  },
  data() {
    return {
      msg: true
    }
  },
  methods: {
    msg_change() {
      this.msg = !this.msg
    }
  }
}
</script>
```

Comp.vue子代setup写法：

```vue
<script setup>
const props = defineProps({
msg:{
type:Boolean,
requre: true
}
})
</script>

<template>
  <h1>子代:{{ props.msg }}</h1>
</template>
```

去掉setup的写法：

```vue
<script>
export default {
  props: {
    msg: Boolean
  },
  setup(props) {
  watch(()=>props.msg,()=>{alert("触发了")})
    return{
    props
    }
  }
}
import { watch } from 'vue'
</script>

<template>
  <h1>子代:{{ props.msg }}</h1>
</template>
```

在点击父代按钮的时候，父代子代的数值都产生了变化

注意不能解构 `props` 对象（取出value），否则会失去响应性

在去掉setup的方法中，msg.value写成this.value,如果使用了axio发起请求一定记得.then之后的函数要使用箭头函数()=>{}才能够正确读取this,因为在axios的回调函数中，`this`指向的不是Vue组件实例。为了解决这个问题，你可以使用箭头函数，箭头函数会继承所在上下文的this值。

如果你确实需要解构 `props` 对象，或者需要将某个 prop 传到一个外部函数中并保持响应性，那么你可以使用 [toRefs()](https://cn.vuejs.org/api/reactivity-utilities.html#torefs) 和 [toRef()](https://cn.vuejs.org/api/reactivity-utilities.html#toref) 这两个工具函数：

```js
import { toRefs, toRef } from 'vue'

export default {
  setup(props) {
    // 将 `props` 转为一个其中全是 ref 的对象，然后解构
    const { title } = toRefs(props)
    // `title` 是一个追踪着 `props.title` 的 ref
    console.log(title.value)

    // 或者，将 `props` 的单个属性转为一个 ref
    const title = toRef(props, 'title')
  }
}
```

使用watch追踪数据变化:

```js
import { watch } from 'vue'
watch(()=>props.msg,()=>{alert("触发了")})
```

h函数嵌套h函数

```js
render(row) {
    return h('div', [
    h(
        NButton,
        {
          strong: true,
          tertiary: true,
          size: 'medium',
          onClick: () => edit(row),
          style: {
            marginRight: '10px'
          }
        },
        () => '编辑'
      ),
      h(
        NButton,
        {
          strong: true,
          tertiary: true,
          size: 'medium',
          onClick: () => play(row),
          style: {
            marginLeft: '10px'
          }
        },
        () => '删除'
      )
    ]);
  }
```

