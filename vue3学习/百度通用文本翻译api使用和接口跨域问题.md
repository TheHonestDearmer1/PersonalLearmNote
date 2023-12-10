 

[百度翻译](https://so.csdn.net/so/search?q=%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91&spm=1001.2101.3001.7020)平台：[http://api.fanyi.baidu.com/product/113](http://api.fanyi.baidu.com/product/113)

申请通用[文本翻译](https://so.csdn.net/so/search?q=%E6%96%87%E6%9C%AC%E7%BF%BB%E8%AF%91&spm=1001.2101.3001.7020)api，需要先认证后才能申请接口使用，其中**通用翻译API标准版免费调用量调整为5万字符/月，高级版免费调用量调整为100万字符/月**，选择高级版就可以了免费使用。

申请完毕，右上角进入开发者信息栏目获取**appid和密钥**  
![在这里插入图片描述](https://img-blog.csdnimg.cn/aa5dd6bbfb3d4235ab8e7051e220f4ad.png)

如果害怕超过免费额度收费的情况，可以选择-我的服务-选中开通对应的翻译服务进行开启**免费额度用量的提醒**

![在这里插入图片描述](https://img-blog.csdnimg.cn/2fdcbdb1f17f454680d99b581b54e351.png)

### 进入接口使用操作阶段

1.  通用翻译API HTTPS 地址：

> https://fanyi-api.baidu.com/api/trans/vip/translate

2.  必填参数：

![在这里插入图片描述](https://img-blog.csdnimg.cn/42a1e64ea4cc4fa2b964b06f7a9f306c.png)

*   其中sign字段的md5(appid+q+salt+密钥),其中salt随机数可以任意填写，sign字段的参数通过md5加密会生成**32位的字符串**。
    
*   其中，可使用 GET 或 POST 方式，如使用 POST 方式，**Content-Type  
    必须为application/x-www-form-urlencoded**，如涉及跨域问题，需要前端配置跨域处理，或在请求头设置**Access-Control-Allow-Origin为**\*
    

> headers:{  
> ‘Access-Control-Allow-Origin’:‘\*’,  
> ‘Content-Type’:‘application/x-www-form-urlencoded’  
> }

完整代码：  
（vue3+vite）index.vue

```vue
<template>
	<div>
		<button @click="translate">翻译</button>
	</div>
</template>
```


```vue
<script setup>
import { reactive } from 'vue'
import md5 from 'md5'//需要安装npm包：npm install md5
import axios from 'axios'//npm包：npm install axios
async function translate() {
    const keySercet = 'R**************T_'//自己的秘钥
    const signNature = reactive(
        {
            q: '香蕉',//翻译文本
            appid: '20**********70',//设置自己的appid
            salt: '12345678',//随机数任意填写
        })
    // 字符串1：appid+q+salt+密钥
    // sign:md5(字符串1) -32位
    const signData = signNature.appid + signNature.q + signNature.salt + keySercet
    // console.log(md5(signData));//
    // console.log(md5(signData).length);//32位
    const transData = {
        q: signNature.q,
        from: 'zh',
        to: 'en',
        appid: '20230915001817870',//appid
        salt: '12345678',//随机数
        sign: md5(signData)
    }
    axios({
        headers:{
		'Access-Control-Allow-Origin':'*',//允许跨域
        'Content-Type':'application/x-www-form-urlencoded'
    },
    //proxy代理，此处位百度翻译api接口,如果不涉及跨域问题和原本没有接入后端接口		   的，直接把此处的url换为百度翻译api接(https://fanyiapi.baidu.com/api/trans/vip/translate),不用配置和执行vite.config.js操作
        url: '/demo',
        method: 'post',
        data:transData
    }).then((res) => {
        console.log(res);
        console.log(res.data.trans_result[0].dst);
    })

}
</script>
```


vite.config.js

```js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  server:{
    proxy: { 
      '/demo': {
       target: "https://fanyi-api.baidu.com/api/trans/vip/translate",
       changeOrigin: true,
       rewrite: (path) => path.replace(/^\/demo/, '')
      }
    }
  }
})
```


![在这里插入图片描述](https://img-blog.csdnimg.cn/f4aea777a8284d8888923b9c217164e2.png)

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Vue入门技能树](https://edu.csdn.net/skill/vue/vue-8b655094a3f04f89be87fceae83515db?utm_source=csdn_ai_skill_tree_blog)[Node.js和npm](https://edu.csdn.net/skill/vue/vue-8b655094a3f04f89be87fceae83515db?utm_source=csdn_ai_skill_tree_blog)[Node安装与配置](https://edu.csdn.net/skill/vue/vue-8b655094a3f04f89be87fceae83515db?utm_source=csdn_ai_skill_tree_blog)38248 人正在系统学习中

本文转自 <https://blog.csdn.net/m0_47814717/article/details/132914750?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-2-132914750-blog-102769793.235%5Ev38%5Epc_relevant_sort&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-2-132914750-blog-102769793.235%5Ev38%5Epc_relevant_sort&utm_relevant_index=5>，如有侵权，请联系删除。