 

#### 什么是命名空间？

Vuex为了解决状态特别多造成store对象非常复杂的时候，允许将store分割成模块(module)  
每个模块都可以拥有自己的state、mutation、action、getter

#### 使用示例

namespaced 命名空间关键字（用在模块的js文件里）

```js
	namespaced : true
```

#### store 文件夹下新建modules文件夹

*   新建home.js

```js
	export default const homeModule ={
		namespaced:true ,// 命名空间
		state(){
			return {
				homeCounter:100,
			}
		},
		getters:{
			// 命名空间里面，getters,新增了2个参数 rooteState,rootGetters
			doubleHomeCounter(state){
				return state.homeCounter*2
			}
		},
		mutations:{
			increment(state,payload){
				state.homeCounter++
			}
		},
		actions:{
			incrementAction({commit}){
				commit("increment")
				commit("increment",null,{root:true}) // 在模块里调用state根的mutations里面的方法
			}
		}
	}
```

store 文件夹下 index.js

```js
	import {createStore} from 'vuex'
	import homeModule from './modules/home'
	
	const store = createStore({
		state(){
			return{
				rootCounter:0
			}
		},
		mutaions:{
			increment(state){
				state.rootCounter++
			}
		},
		modules:{
			home:homeModule
		}
	})
	export default store
```

##### home组件内使用state 属性和 homeModule 模块属性

```js
	<template>
		<h2> state根数据: {{$store.state.rootCounter}}</h2>
		<h2>home 模块中的数据：{{$store.state.home.homeCoutner}}</h2>  
		<h2> doubleCounter {{$store.getters["home/doubleHomeCounter"]}}</h2>
		
		<button @click='homeIncrement'>homeCounter + 1</button>
		<button @click='homeIncrementAction' > homeCounter +1 </button>
	</template>
	<script>
			export default{
				methods:{
					homeIncrement(){
						this.$store.commit("home/increment") 
						// 直接调用mutations里方法修改homeCounter
						 //如果不加模块名home,那么模块里和根里 同名increment会造成多个state值改变。用了命名空间就不会了
					},
					homeIncrementAction(){
						this.$store.dispatch("home/incrementAction") // 通过actions里方法调用mutatons修改homeCounter
					}
				}
			}
	</script>
```

*   使用createNamespacedHelpers

关键代码 :

```js
	const {mapState,mapGetters,mapMutations,mapActions} = createNamespacedHelpers("home")
```

```js
	<template>
		<h2>{{homeCounter}} </h2>
		<h2> {{doubleHomeCounter}} </h2>
		<button @click='increment'>homeCounter+1</button>
		<button @click='incrementAction'>homeCounter+1</button>
	</template>
	<script>
		import {createNamespacedHelpers} from 'vuex'
		import {useState,useGetters} from '../ hooks/index'
		const { mapState, mapGetters, mapMutations, mapActions } = createNamespacedHelpers("home")
		export default{
			computed:{
				...mapState(["homeCounter"]),
				...mapGetters(["doubleHomeCounter"])
			},
			methods:{
				...mapMutations(["increment"]),
				...mapActions(["incrementAction"])
				
			},
			或者
			setup(){
				const state = useState(["rootCounter"]) // 根数据
				const rootGetters = useGetters(["doubleRootCounter"])

				const homeCounter = useState("home",["homeCounter"]) // home模块的数据
				const doubleHomeCounter = useGetter("home,["doubleHomeCounter"])
				const increment = mapMutations(["increment"])
				const incrementAction = mapActions(["incrementAction"])
				
				return{
					...state,
					...rootGetters,
					...homeCounter,
					...doubleHomeCounter,
					...increment,
					...incrementAction
				}
			}
		}
	</script>
```

#### 补充

组件内使用模块的三种写法

*   写法一

```js
	computed:{
		...mapState({
			homeCounter:state => state.homeCounter
		}),
		...mapGetters({
			doubleHomeCounter :"home/doubleHomeCounter"
		})
	}
	methods:{
		...mapMutations({
			increment:"home/increment"
		}),
		...mapActions({
			incrementAction:"home/incrementAction"
		})
	}
```

*   写法二

```js
	computed:{
		...mapState("home",["homeCounter"]),
		...mapGetters("home",["doubleHomeCounter"])
	},
	methods:{
		...mapMutations("home",["increment"]),
		...mapActions("home",["incrementAction"]),
	}
```

*   写法三

```js
	import {createNamespacedHelpers} from 'vuex'
	const {mapState,mapGetters,mapMutatons,mapActions}  = createNamespacedHelpers("home")

	computed:{
		...mapState(["homeCounter"]),
		...mapGetters(["doubleHomeCounter"])
	},
	methods:{
		 ...mapMutations(["increment"]),
         ...mapActions(["incrementAction"]),
	}
	在 setup里使用

	setup(){
		const state = useState(["homeCounter"])
        const getters = useGetters(["doubleHomeCounter"])
		const mutations = mapMutations(["increment"])
		const actions = mapActions(["incrementAction"])
		retrn{
			...state,
			...getters,
			...mutations,
			...actions
		}
	}
```

##### 改造之前的hooks

[useState](https://so.csdn.net/so/search?q=useState&spm=1001.2101.3001.7020).js 支持模块化数据

```js
	import {mapState,createNamespacedHelpers} from 'vuex'
	import {useMappers} from './useMappers'
	export function useState(moduleName,mapper){
		let mapperFn = mapState 
		if(typeof moduleName === 'string' && moduleName.length>0){
			mapperFn = createNamespacedHelpers(moduleName).mapState ;// moduleName 就是模块的名字
		}else{
			mapperFn = moduleName
		}
		return useMapper(mapper,mapperFn)		
	}
```

useMapper.js (没改）

```js
	import {computed} from 'vue'
	import {useStore} from 'vuex'
	export function useMapper(mapper,mapFn){
		const store = useStore()
		const storeStateFns = mapFn(mapper) // 如果是useState调用的，那么这里就相当于 mapState(传过来的要拿的state名称,可能是数组可能是对象，返回结果是一个对象 {name:function,age:function}
		
		const storeState = {}
		Object.keys(storeStateFns).forEach(fnKey =>{
			const fn = storeStateFns[fnKey].bind({$store:store})
			storeState[fnKey] = computed(fn)
		})
		return storeState
	}
```

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Vue入门技能树](https://edu.csdn.net/skill/vue/vue-fbae70777d8d4a8fb2a47231ee301eef?utm_source=csdn_ai_skill_tree_blog)[VueX状态管理](https://edu.csdn.net/skill/vue/vue-fbae70777d8d4a8fb2a47231ee301eef?utm_source=csdn_ai_skill_tree_blog)[VueX是什么？](https://edu.csdn.net/skill/vue/vue-fbae70777d8d4a8fb2a47231ee301eef?utm_source=csdn_ai_skill_tree_blog)38561 人正在系统学习中

本文转自 <https://blog.csdn.net/weixin_39137100/article/details/122874831>，如有侵权，请联系删除。