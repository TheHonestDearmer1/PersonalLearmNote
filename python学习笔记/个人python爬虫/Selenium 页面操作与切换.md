# 不废话简单易懂的Selenium 页面操作与切换

本人在操作Selenium由于之前没有总结笔记，做各种操作的时候总是要查资料查来查去，所以总结一下一些常用的Selenium操作方法和基础配置，如果需要针对html进行内容截取和操作，可以同时看本人的lxml操作笔记食用:

[python简单易懂的lxml读取HTML节点及常用操作方法-CSDN博客](https://blog.csdn.net/qq_74177889/article/details/142207376?spm=1001.2014.3001.5502)

## 基础配置

### 基础包安装

我一般用清华源下载

Selenium基础包安装,注意版本不同，语法也会有所变化，我使用的python版本是3.19

```
pip3 install selenium~=4.23.1 -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```

方便快速下载对应chrome驱动包的工具下载

```
pip3 install webdriver_manager=4.0.2
```

### 初始化

```python
        # 初始化自动化爬虫
        # 配置参数
        chrome_options = Options()
        # 设置日志级别为 FATAL
        chrome_options.add_argument('--log-level=3')
        # 忽略证书错误
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--headless")  # 启用无头模式，隐藏浏览器界面
        chrome_options.add_argument("--no-sandbox")  # 防止一些潜在问题
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--window-size=1800,3000") # 防止页面某些元素可能不被点到

        # 添加user-agent，避免被当作爬虫脚本,使得无头模式下能够正常爬取
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
        executable_path = ChromeDriverManager().install() # 安装chrome驱动并自动获取地址返回
        service = ChromeService(
            executable_path=executable_path)
        driver = webdriver.Chrome(service=service, options=chrome_options) # 得到驱动器
```

## 基础操作

### 打开链接url

**从当前页面打开链接:**

```python
driver.get(url)
```

**新建一个标签页并打开链接（注意此时句柄还是上一个页面，需要手动切换）：**

```python
 # 打开新标签页
driver.execute_script("window.open('{}');".format(link))
```

### 获取句柄与切换关闭标签页

句柄代表的是一个页面，切换句柄来获取每个页面的信息进行操作

#### **获取当前句柄：**

```py
page_list_handle = driver.current_window_handle
```

#### **获取全部句柄：**

获取到的是句柄的数组列表

```python
all_handles = driver.window_handles
```

#### **切换句柄(切换标签页)：**

切换回一开始保存的句柄

```python
self.driver.switch_to.window(page_list_handle)
```

切换到当前的最后一个句柄，也就是新创建的句柄:

```python
self.driver.switch_to.window(all_handles[-1])
```

#### **关闭指定标签页：**

此时被关闭的是当前选中的句柄，就自然关闭了标签页

```python
driver.close()
```

### 获取当前句柄的网页html

```python
driver.page_source  # 获取当前页面的HTML源代码
```

### 获取当前句柄的网页链接

```python
driver.current_url
```

通过js去获取当前网页链接

```js
current_url = driver.execute_script("return window.location.href;")
```

### 执行所有操作完毕关闭驱动

```python
driver.quit()  # 关闭驱动程序，释放资源
```

### 元素选择和点击，输入

#### 按钮

按钮可以通过xpath定位获取，driver.find_element是定位一个元素，driver.find_elements是定位多个元素

```python
next_button = driver.find_element(By.XPATH, "//*[contains(@id, 'next') or contains(@name, 'next') or contains(@class, 'next')]")
```

**点击**

```python
next_button.click()
```

当一般的点击操作无法生效的时候可以使用js单击法

```python
driver.execute_script("arguments[0].click();", next_button)
```

#### 文本框

**获取多个文本框的其中一个文本框**

```python
input_element = driver.find_elements(By.XPATH, ".//input")[0]
```

**清除文本框内容**

```python
# 清除输入框中的默认文本（如果有的话）
input_element.clear()
```

**如果发现无法清除，则最好用js方法清除**

```python
driver.execute_script("arguments[0].value='';", input_element)
```

**输入内容**

```python
# 输入数字
input_element.send_keys(page_num)
```

**获取文本框内容**

注意，获得的数字的值可能是string类型，要手动转int

```python
current_value = input_element.get_attribute('value')
```

**模拟键盘操作(回车)**

```python
# 模拟回车键
input_element.send_keys(Keys.RETURN)
```

