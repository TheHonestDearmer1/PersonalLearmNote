## iframe无法显示

在index.html添加这一行meta

```
  <meta http-equiv=Content-Security-Policy content="default-src *; frame-src *; style-src * 'self' 'unsafe-inline' 'unsafe-eval';script-src * 'self' 'unsafe-inline' 'unsafe-eval';">
```

在config.xml添加下列：

```xml
    <access origin="*" subdomains="true" />
    <allow-navigation href="*" />
```

结果：

```xml
<?xml version='1.0' encoding='utf-8'?>
<widget id="io.cordova.hellocordova" version="1.0.0" xmlns="http://www.w3.org/ns/widgets" xmlns:cdv="http://cordova.apache.org/ns/1.0">
    <name>HelloCordova</name>  
    <description>Sample Apache Cordova App</description>
    <author email="dev@cordova.apache.org" href="https://cordova.apache.org">
        Apache Cordova Team
    </author>
    <content src="index.html" />
    <access origin="*" subdomains="true" />
    <allow-navigation href="*" />
    <allow-intent href="*" />
    <allow-navigation href="blob:*" />
    <allow-intent href="http://*/*" />
    <allow-intent href="https://*/*" />
</widget>

```



##  http请求不通

最近在使用[Cordova](https://so.csdn.net/so/search?q=Cordova&spm=1001.2101.3001.7020)和vue结合，开始移动端应用时，遇到一个问题，vue项目中的接口全部请求不通，怀疑是Android http接口访问不通的问题。在网上找了很多资料，也遇到了很多弯路，最后终于解决了。cordova调试非常麻烦，在真机上不输出错误。使用**Android Studio** 直接打开`platform/android`下的**Android studio**项目，连接模拟器调试才能看到日志信息。

### 开发环境

*   cordova 11.0.0
*   android 10.1.2

### 产生原因

##### Android 高版本默认不允许http

Android 高版本默认不允许http访问造成，首先查看了`platform/android`下的**Android studio**项目**AndroidManifest.xml**文件(MyApp\platforms\android\app\src\main\AndroidManifest.xml)

```xml
android:usesCleartextTraffic="true"
```

将这行代码添加到application标签上:

```
<application
 android:label="@string/app_name"
 ... 
 android:usesCleartextTraffic="true">
```

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

1. 将cordova的本地虚拟容器改为http的

   在`ConfigXmlParser.java` 文件中的原来是这样的(.\MyApp\platforms\android\CordovaLib\src\org\apache\cordova\ConfigXmlParser.java)：

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

**config.xml**中加入

```xml
<access origin="*" subdomains="true" />
```

将上面的`SCHEME_HTTPS = "https"`改为了`SCHEME_HTTPS = "http"`，然后运行android studio或者直接cordova打包，发现是没有问题的，http接口可以直接访问通。

