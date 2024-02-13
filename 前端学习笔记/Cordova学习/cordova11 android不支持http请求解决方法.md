 

最近在使用[Cordova](https://so.csdn.net/so/search?q=Cordova&spm=1001.2101.3001.7020)和vue结合，开始移动端应用时，遇到一个问题，vue项目中的接口全部请求不通，怀疑是Android http接口访问不通的问题。在网上找了很多资料，也遇到了很多弯路，最后终于解决了。cordova调试非常麻烦，在真机上不输出错误。使用**Android Studio** 直接打开`platform/android`下的**Android studio**项目，连接模拟器调试才能看到日志信息。

### 开发环境

*   cordova 11.0.0
*   android 10.1.2

### 产生原因

##### Android 高版本默认不允许http

最初怀疑是Android 高版本默认不允许http访问造成，查看了`platform/android`下的**Android studio**项目**AndroidManifest.xml**文件，看到其中已经加了

```xml
android:usesCleartextTraffic="true"
```

很显然不是这个原因造成的。

##### cordova 虚拟了一个https的本地服务器

使用Android studio调试时，在控制台发现，分析是cordova将assets目录下的html相关资源，虚拟成了一个本地的容器，而且是**https**的

```bash
D/CordovaWebViewImpl: onPageDidNavigate(https://localhost/index.html)
```

当在这个https的页面访问http端口时，就出现了下面的不允许访问http接口的错误

```bash
I/chromium: [INFO:CONSOLE(1)] "Mixed Content: The page at 'https://localhost/index.html#/' was loaded over HTTPS, but requested an insecure XMLHttpRequest endpoint 'http://......'. This request has been blocked; the content must be served over HTTPS.", source: https://localhost/static/js/0.0dc00ee6938f5903a61a.js (1)
```

### 解决办法

1.  网上有人说在`SystemWebViewEngine.java`这个文件中的`initWebViewSettings`方法中，增加
    
    ```java
    settings.setMixedContentMode(WebSettings.MIXED_CONTENT_COMPATIBILITY_MODE);
    ```
    
    亲测无效，建议不要浪费时间
    
2.  自己设想，将cordova的本地虚拟容器改为http的，是不是就可以了？
    
    在`ConfigXmlParser.java` 文件中的原来是这样的：
    
    ```java
        private static String SCHEME_HTTP = "http";
        private static String SCHEME_HTTPS = "https";
        private static String DEFAULT_HOSTNAME = "localhost";
    ........
        private String getLaunchUrlPrefix() {
            if (prefs.getBoolean("AndroidInsecureFileModeEnabled", false)) {
                return "file:///android_asset/www/";
            } else {
                String scheme = prefs.getString("scheme", SCHEME_HTTPS).toLowerCase();
                String hostname = prefs.getString("hostname", DEFAULT_HOSTNAME);
    
                if (!scheme.contentEquals(SCHEME_HTTP) && !scheme.contentEquals(SCHEME_HTTPS)) {
                    LOG.d(TAG, "The provided scheme \"" + scheme + "\" is not valid. " +
                        "Defaulting to \"" + SCHEME_HTTPS + "\". " +
                        "(Valid Options=" + SCHEME_HTTP + "," + SCHEME_HTTPS + ")");
    
                    scheme = SCHEME_HTTPS;
                }
    
                return scheme + "://" + hostname + '/';
            }
        }
    ```
    

最外层  
**config.xml**中加入

```xml
<access origin="*" subdomains="true" />
```

于是，我将上面的`SCHEME_HTTPS = "https"`改为了`SCHEME_HTTPS = "http"`，然后运行android studio或者直接cordova打包，发现是没有问题的，http接口可以直接访问通。

### 感想

1.  cordova的网上解决问题的资料真的是比较少，其中靠谱的更少

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[网络技能树](https://edu.csdn.net/skill/network/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/network/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/network/?utm_source=csdn_ai_skill_tree_blog)42719 人正在系统学习中

![](https://img-blog.csdnimg.cn/252241d39b3e4f0394ad7162f472b9db.jpeg)

GIS领域研发者

![](https://g.csdnimg.cn/extension-box/1.1.6/image/qq.png) QQ名片

![](https://g.csdnimg.cn/extension-box/1.1.6/image/ic_move.png)

本文转自 <https://blog.csdn.net/GISuuser/article/details/125103594>，如有侵权，请联系删除。