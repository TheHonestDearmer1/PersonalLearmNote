 

之前利用[selenium](https://so.csdn.net/so/search?q=selenium&spm=1001.2101.3001.7020)写了个脚本利用pyinstaller打包exe文件，但是打包时没有集成chromedriver.exe，导致的问题就两个exe要放在同一文件夹下，否则调用不到chromedriver.exe程序会闪退。

后来参考了：https://blog.csdn.net/xiaofeixia666888/article/details/107258470/  
的做法，把chromedriver.exe文件作为附加文件打包进去。

```typescript
pyinstaller -F --add-binary "chromedriver.exe";"."  myScript.py
```

但是该文章作者只讲了一半，按照文章所述修改spec文件的方法，exe文件是一并打包进去了，但是exe调用还是有问题。经检查，问题出在代码里，需要修改代码中引用chromedriver.exe的解压路径。

解决问题的关键词：sys.\_MEIPASS

附上代码：

```python
def getDriver():
    if getattr(sys, 'frozen', False):
        # 从exe包里找chromedriver依赖驱动的情况
        chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
        driver = webdriver.Chrome(chromedriver_path)
    else:
        # 普通情况下从本地文件路径找依赖的情况
        driver = webdriver.Chromedriver(executable_path='本地chromedriver的路径') 
    return  driver
    
if __name__ == '__main__':
    driver = getDriver()
	driver.get('https://www.baidu.com')
	#无论是本地调试还是打包成exe都不会再报错了。	
```

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Python入门技能树](https://edu.csdn.net/skill/python/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/python/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/python/?utm_source=csdn_ai_skill_tree_blog)372480 人正在系统学习中

本文转自 <https://blog.csdn.net/sinat_36797467/article/details/120288627>，如有侵权，请联系删除。