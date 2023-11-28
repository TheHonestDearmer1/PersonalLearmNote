**from** PIL **import** Image  
**import** pytesseract  
**import** numpy **as** np  
**import** cv2  
**import** matplotlib.pyplot **as** plt  
_#上面都是导包，只需要下面这一行就能实现图片文字识别_  
img = Image.open(**'image/望月.png'**)  
print(type(img))  
_\# 使用numpy类型进行传窗效果不好_  
_\# img = np.array(img)_  
_\# 使用OpenCV的cv2.imread进行读取传参效果也不好，_  
_\# cv2.imshow('img',img)_  
_\# cv2.waitKey()_  
_\# 最后还是使用Image.open()进行读取效果不错_  
_\# plt.imshow(img)_  
_\# plt.show()_  
text=pytesseract.image\_to\_string(img,lang=**'chi\_sim'**)  
print(text)

<img src="https://pic2.zhimg.com/v2-50eaea949ac63de5d5a84813d9efe491\_b.jpg" data-caption="" data-size="normal" data-rawwidth="476" data-rawheight="390" class="origin\_image zh-lightbox-thumb" width="476" data-original="https://pic2.zhimg.com/v2-50eaea949ac63de5d5a84813d9efe491\_r.jpg"/>

![](https://pic2.zhimg.com/80/v2-50eaea949ac63de5d5a84813d9efe491_1440w.webp)

<img src="https://pic3.zhimg.com/v2-f4344fc98c4b0b361105cf32c331742a\_b.jpg" data-caption="" data-size="normal" data-rawwidth="772" data-rawheight="284" class="origin\_image zh-lightbox-thumb" width="772" data-original="https://pic3.zhimg.com/v2-f4344fc98c4b0b361105cf32c331742a\_r.jpg"/>

![](https://pic3.zhimg.com/80/v2-f4344fc98c4b0b361105cf32c331742a_1440w.webp)

下面我们要注意的主要步骤是安装配置tesseract.exe 连接：

[帐号登录​blog.csdn.net/haluoluo211/article/details/53304900](https://link.zhihu.com/?target=https%3A//blog.csdn.net/haluoluo211/article/details/53304900)

这个挺不错的，做开发可以使用到其他的小程序应用上面。提升客户体验。

本文转自 <https://zhuanlan.zhihu.com/p/41023317>，如有侵权，请联系删除。