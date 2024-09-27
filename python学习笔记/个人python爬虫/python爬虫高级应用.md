## lxml读取HTML节点及操作方法

### 1. 初始化和基本概念
- `lxml` 是一个强大的库，用于处理XML和HTML文档。
- 它提供了类似BeautifulSoup的功能，但性能更高。
- 在使用`lxml`时，通常会先解析HTML或XML文档，得到一个ElementTree对象。

### 2. 解析HTML文档
- 使用`lxml.html.fromstring(html)`来从字符串中创建一个ElementTree对象。
- 示例：
  ```python
  from lxml import html
  html_content = '<html><body><p>Hello world!</p></body></html>'
  tree = html.fromstring(html_content)
  ```

### 3. XPath选择器
- XPath是一种用于在XML文档中查找信息的语言。
- `lxml`支持XPath选择器，可以用来定位文档中的元素。
- 示例：
  ```python
  # 获取所有的段落标签
  paragraphs = tree.xpath('//p')
  ```

好的，让我们详细解释一下这段代码，并将其作为笔记整理出来。这段代码展示了如何构建包含子节点及其属性的XPath路径。以下是详细的笔记：

#### 构建包含属性的XPath路径

流程:

##### 1. 获取子节点的XPath路径

首先，我们遍历一个节点的所有子节点，并获取每个子节点的XPath路径。

```python
for child in node.getchildren():
    xpath_path = '/' + node.getroottree().getpath(child)
```

##### 2. 获取子节点的所有属性

对于每个子节点，我们获取其所有属性：

```python
attributes = child.attrib
```

##### 3. 构建包含属性的XPath路径

接下来，我们根据子节点的属性构建一个完整的XPath路径。如果子节点有属性，我们会在XPath路径后面加上属性条件。

##### 3.1 属性存在时

如果子节点有属性，我们构建一个包含所有属性的XPath路径：

```python
if attributes:
    xpath_with_attributes = xpath_path + "["
    for i, (key, value) in enumerate(attributes.items()):
        xpath_with_attributes += f"@{key}='{value}'"
        if i < len(attributes) - 1:
            xpath_with_attributes += " and "
    xpath_with_attributes += "]"
```

- `attributes.items()` 返回一个迭代器，其中包含了属性的键值对。
- `enumerate(attributes.items())` 为每个属性分配一个索引。
- `f"@{key}='{value}'"` 构建一个XPath条件，表示属性 `key` 的值为 `value`。
- 如果不是最后一个属性，则添加 `" and "` 以连接多个条件。
- 最后添加 `"]"` 来结束XPath条件。

##### 3.2 属性不存在时

如果子节点没有属性，我们直接使用原始的XPath路径：

```python
else:
    xpath_with_attributes = xpath_path
```

##### 综合示例

下面是一个完整的示例代码，展示了如何遍历节点的子节点并构建包含属性的XPath路径：

```python
from lxml import html

html_content = '''
<html>
    <body>
        <div id="container" class="main">
            <p>Hello, world!</p>
            <a href="/link" id="example">Example Link</a>
        </div>
    </body>
</html>
'''

tree = html.fromstring(html_content)
root_node = tree.xpath('//div[@id="container"]')[0]

# 遍历根节点的所有子节点
for child in root_node.getchildren():
    xpath_path = '/' + root_node.getroottree().getpath(child)

    # 获取子节点的所有属性
    attributes = child.attrib

    # 构建包含所有属性的XPath路径
    if attributes:
        xpath_with_attributes = xpath_path + "["
        for i, (key, value) in enumerate(attributes.items()):
            xpath_with_attributes += f"@{key}='{value}'"
            if i < len(attributes) - 1:
                xpath_with_attributes += " and "
        xpath_with_attributes += "]"
    else:
        xpath_with_attributes = xpath_path

    print(f"XPath Path: {xpath_path}")
    print(f"XPath with Attributes: {xpath_with_attributes}")
    print("Attributes:", attributes)
    print("")

# 输出：
# XPath Path: /html/body/div/p
# XPath with Attributes: /html/body/div/p
# Attributes: {}
#
# XPath Path: /html/body/div/a
# XPath with Attributes: /html/body/div/a[@href='/link' and @id='example']
# Attributes: {'href': '/link', 'id': 'example'}
```

##### 详细解释

1. **获取子节点的XPath路径**：
   - `node.getchildren()` 返回节点的所有子节点。
   - `node.getroottree().getpath(child)` 获取子节点的XPath路径。
   - 我们在路径前加上 `/` 来确保路径格式正确。

2. **获取子节点的所有属性**：
   - `child.attrib` 返回子节点的所有属性及其值。

3. **构建包含属性的XPath路径**：
   - 如果子节点有属性，我们构建一个包含所有属性的XPath路径。
   - 使用 `enumerate` 来为每个属性分配一个索引，以便在多个属性之间添加 `and`。
   - 如果子节点没有属性，我们直接使用原始的XPath路径。



### 4. 遍历节点

- `iter_node()` 函数可以用来遍历一个节点的所有子节点。
- 示例：
  ```python
  for node in iter_node(body):
      # 处理每个节点
      pass
  ```

### 5. 获取节点属性
- 使用`.attrib`属性来获取节点的所有属性。
- 示例：
  ```python
  class_name = node.attrib.get('class', '')
  ```

在使用`lxml`处理HTML或XML文档时，获取节点的属性和属性值是非常常见的需求。下面详细解释如何获取标签的全部属性以及如何分别获取单个属性和属性值。

#### 1. 获取标签的全部属性

在`lxml`中，你可以通过访问节点的`attrib`属性来获取所有属性。`attrib`是一个字典，键是属性名，值是属性值。

##### 示例代码：

```python
from lxml import html

html_content = '''
<div id="content" class="main-content">
    <p>Hello, world!</p>
</div>
'''

tree = html.fromstring(html_content)
div_node = tree.xpath('//div')[0]

# 获取所有属性
all_attributes = div_node.attrib
print("All attributes:", all_attributes)

# 输出：
# All attributes: {'id': 'content', 'class': 'main-content'}
```

#### 2. 分别获取单个属性和属性值

如果你只需要获取某个特定属性的值，可以直接通过键访问字典中的值。如果属性不存在，则可以使用`get`方法提供一个默认值。

##### 示例代码：

```python
# 获取单个属性
id_attribute = div_node.attrib.get('id', 'default-id')
print("ID attribute:", id_attribute)

class_attribute = div_node.attrib.get('class', 'default-class')
print("Class attribute:", class_attribute)

# 输出：
# ID attribute: content
# Class attribute: main-content
```

#### 3. 获取属性值

如果属性名已知，可以直接通过键访问字典中的值。如果属性名未知或需要处理多个属性，可以遍历`attrib`字典来获取所有属性及其值。

##### 示例代码：

```python
# 遍历所有属性
for attr_name, attr_value in div_node.attrib.items():
    print(f"Attribute: {attr_name}, Value: {attr_value}")

# 输出：
# Attribute: id, Value: content
# Attribute: class, Value: main-content
```

#### 4. 处理特殊情况

在某些情况下，属性可能包含空格分隔的多个值（例如`class`属性），这时你可以使用`split`方法来分割字符串。

##### 示例代码：

```python
# 处理包含多个值的属性
class_values = div_node.attrib.get('class', '').split()
print("Class values:", class_values)

# 输出：
# Class values: ['main-content']
```

#### 5. 综合示例

下面是一个综合示例，展示了如何获取节点的所有属性、单个属性以及如何处理特殊情况下的属性值。

```python
from lxml import html

html_content = '''
<div id="content" class="main-content secondary">
    <p>Hello, world!</p>
</div>
'''

tree = html.fromstring(html_content)
div_node = tree.xpath('//div')[0]

# 获取所有属性
all_attributes = div_node.attrib
print("All attributes:", all_attributes)

# 获取单个属性
id_attribute = div_node.attrib.get('id', 'default-id')
print("ID attribute:", id_attribute)

class_attribute = div_node.attrib.get('class', 'default-class')
print("Class attribute:", class_attribute)

# 遍历所有属性
for attr_name, attr_value in div_node.attrib.items():
    print(f"Attribute: {attr_name}, Value: {attr_value}")

# 处理包含多个值的属性
class_values = div_node.attrib.get('class', '').split()
print("Class values:", class_values)

# 输出：
# All attributes: {'id': 'content', 'class': 'main-content secondary'}
# ID attribute: content
# Class attribute: main-content secondary
# Attribute: id, Value: content
# Attribute: class, Value: main-content secondary
# Class values: ['main-content', 'secondary']
```

通过这些方法，你可以轻松地获取和处理`lxml`中节点的属性及其值。希望这能帮助你更好地理解和使用`lxml`进行HTML或XML解析。

### 6. 获取节点文本

- 使用`.text`属性来获取节点的文本内容。
- 示例：
  ```python
  node_text = node.text
  ```

或者如果下面还有子节点的话，最好是用：

```python
# 将所有的文本拼接起来
link_name = ''.join(child.itertext()).strip().replace('\n', '').strip()
# 去掉过多的空格
link_name = re.sub(r'\s+', ' ', link_name ).strip()
```

### 7. 获取节点路径

- 使用`.getroottree().getpath(node)`来获取节点的完整XPath路径。
- 示例：
  ```python
  path = node.getroottree().getpath(node)
  ```

#####  1.获取最末尾节点路径

```python
               # 提取最后一个 '/' 后面的元素
                last_element = path.split('/')[-1] if '/' in path else path
```

### 8. 检查节点类型(标签名)

- 通过`.tag`属性来检查节点的标签名。
- 示例：
  ```python
  if node.tag == 'p':
      # 处理段落节点
      pass
  ```

### 9. 子节点操作

- 使用`.getchildren()`来获取节点的所有子节点，node.getparent()获取节点的所有父节点。
- 示例：
  ```python
  children = node.getchildren()
  ```

### 10. 提取属性值
- 使用`@属性名`来提取属性值。
- 示例：
  ```python
  image_srcs = node.xpath('.//img/@src')
  ```

### 11. 节点转换为字符串HTML
- 使用`etree.tostring(node)`来将节点转换为字符串形式。
- 示例：
  ```python
  node_html = etree.tostring(node, pretty_print=True, encoding='unicode')
  ```

### 12. 计算文本密度
- 文本密度是指文本相对于其他非文本内容（如图片、链接）的比例。
- 通过计算节点中的文本长度与节点总长度的比例来估算文本密度。
- 示例：
  ```python
  text_density = len(node.text_content()) / len(etree.tostring(node))
  ```

### 13. 处理列表页面
- 在处理列表页面时，有时候需要检查是否有特定的类名来进行对应操作，如`'list'`。
- 示例：
  ```python
  if 'list' in a_element[0].get('class', '').lower():
      # 处理列表节点
      pass
  ```

## Selenium 页面操作与切换

### 1. 初始化 WebDriver

在开始任何操作之前，你需要初始化一个WebDriver实例。这通常是通过指定一个浏览器驱动程序来完成的。

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# 配置无头模式
chrome_options = Options()
# 设置日志级别为 FATAL
chrome_options.add_argument('--log-level=3')
# 忽略证书错误
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--headless")  # 启用无头模式
chrome_options.add_argument("--no-sandbox")  # 防止一些潜在问题
chrome_options.add_argument('--disable-dev-shm-usage')
# 避免有些元素无法正常读取
chrome_options.add_argument("--window-size=1800,3000")
# 添加user-agent，避免在无头模式中被当作爬虫脚本,使得无头模式下能够正常爬取
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
executable_path = ChromeDriverManager().install()
service = ChromeService(executable_path=executable_path)
self.driver = webdriver.Chrome(service=service, options=chrome_options)
```

### 2. 加载页面

使用`get`方法加载目标网页。

```python
driver.get('http://example.com')
```

### 3. 获取当前窗口的句柄或者全部句柄

在进行页面操作之前，获取当前窗口的句柄，以便后续可以在操作后返回到当前窗口。

```python
original_window = driver.current_window_handle
```

获取全部句柄的列表，方便后续切换：

```python
all_handles = driver.window_handles
```

### 4. 定位并点击元素

使用XPath定位页面元素并点击。

```python
xpath_with_attributes = "your_xpath_here"

not_success_click = True
# 防止有时候页面没有加载完成而点不到
while not_success_click:
    try:
        element = driver.find_element(By.XPATH, xpath_with_attributes)
        element.click()
        not_success_click = False
    except:
        not_success_click = True
```

### 5. 处理新标签页

如果点击元素后打开了新的标签页，需要切换到新标签页并处理。

```python
all_handles = driver.window_handles
new_tab = False
if len(all_handles) > 1:
    new_tab = True
    driver.switch_to.window(all_handles[-1])
```

### 6. 等待URL变化

等待页面URL的变化，确保页面已经加载完成。

```python
WebDriverWait(driver, 10).until(EC.url_changes(self.search_url))
```

### 7. 获取新URL

获取新打开页面的URL。

```python
new_url = "data:,"
start_time = time.time()  # 记录开始时间
while "data:," in new_url or "about:blank" in new_url:
    new_url = driver.execute_script("return window.location.href;")
```

### 8. 关闭新窗口并切换回原窗口

关闭新窗口，并切换回原来的窗口。

```python
original_window = driver.current_window_handle
all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
driver.close()  # 关闭新窗口
driver.switch_to.window(original_window)  # 切换回原窗口
```

### 9. 获取元素文本

获取元素的文本内容，并清理文本。

```python
link_name = ''.join(child.itertext()).strip().replace('\n', '').strip()
link_name = re.sub(r'\s+', ' ', link_name).strip()
```

### 综合示例

下面是一个综合示例，展示了如何使用Selenium进行页面操作与切换：

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm
import time
import re

class ContentExtractor:
    def __init__(self):
        options = Options()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def auto_get_list(self, result):
        node = etree.fromstring(result["html"])
        link_list = {}
        description = "获取标签进度"
        old_child = node.getchildren()[0]

        # 获取当前窗口的句柄,以方便跳转回来
        original_window = self.driver.current_window_handle

        for child in tqdm(node.getchildren(), desc=description):
            new_tab = False

            # 防止出现意外区块
            if child.tag != old_child.tag:
                continue

            xpath_path = ('/' + node.getroottree().getpath(child))
            attributes = child.attrib

            # 构建包含所有属性的XPath路径
            xpath_with_attributes = build_xpath_with_attributes(xpath_path, attributes)

            not_success_click = True
            while not_success_click:
                try:
                    row = self.driver.find_element(By.XPATH, xpath_with_attributes)
                    not_success_click = False
                except:
                    not_success_click = True

            click_state = True
            while click_state:
                try:
                    row.click()
                    all_handles = self.driver.window_handles
                    if len(all_handles) > 1:
                        new_tab = True
                    click_state = False
                except:
                    click_state = True

            if not new_tab:
                WebDriverWait(self.driver, 10).until(EC.url_changes(self.search_url))
                new_url = "data:,"
                time.sleep(1)
                while "data:," in new_url:
                    new_url = self.driver.current_url
                    if "data:," in new_url:
                        self.driver.back()
                        time.sleep(1)
                        row.click()

                self.driver.back()
            else:
                all_handles = self.driver.window_handles
                self.driver.switch_to.window(all_handles[-1])
                start_time = time.time()
                new_url = "data:,"
                while "data:," in new_url or "about:blank" in new_url:
                    new_url = self.driver.execute_script("return window.location.href;")

                # 关闭新窗口
                self.driver.close()
                # 选定初始界面权柄
                self.driver.switch_to.window(original_window)

            try:
                link_name = ''.join(child.itertext()).strip().replace('\n', '').strip()
                link_name = re.sub(r'\s+', ' ', link_name).strip()
                link_list[link_name] = new_url
            except:
                continue

        return link_list

    def build_xpath_with_attributes(self, xpath_path, attributes):
        if attributes:
            xpath_with_attributes = xpath_path + "["
            for i, (key, value) in enumerate(attributes.items()):
                xpath_with_attributes += f"@{key}='{value}'"
                if i < len(attributes) - 1:
                    xpath_with_attributes += " and "
            xpath_with_attributes += "]"
        else:
            xpath_with_attributes = xpath_path
        return xpath_with_attributes
```

### 详细解释

1. **初始化 WebDriver**：
   - 使用 `webdriver.Chrome` 创建一个新的Chrome WebDriver实例。
   - `Service` 和 `ChromeDriverManager` 用于管理Chrome驱动程序。

2. **加载页面**：
   - 使用 `driver.get(url)` 方法加载指定的URL。

3. **获取当前窗口的句柄**：
   - `driver.current_window_handle` 返回当前窗口的句柄。

4. **定位并点击元素**：
   - 使用 `find_element(By.XPATH, xpath)` 方法定位元素。
   - 使用 `element.click()` 方法点击元素。

5. **处理新标签页**：
   - `driver.window_handles` 返回所有窗口的句柄。
   - 使用 `switch_to.window(handle)` 方法切换到指定的窗口。

6. **等待URL变化**：
   - 使用 `WebDriverWait(driver, timeout).until(EC.url_changes(current_url))` 等待URL发生变化。

7. **获取新URL**：
   - 使用 `driver.current_url` 获取当前页面的URL。
   - 使用 `driver.execute_script("return window.location.href;")` 获取动态加载后的URL。

8. **关闭新窗口并切换回原窗口**：
   - 使用 `driver.close()` 关闭当前窗口。
   - 使用 `switch_to.window(handle)` 切换回指定的窗口。

9. **获取元素文本**：
   - 使用 `itertext()` 方法获取元素的文本内容，并使用正则表达式清理文本。

10. **收集链接信息**：
    - 将链接名称和URL存储在一个字典中。

通过这些方法，你可以有效地使用Selenium进行页面操作与切换。希望这些笔记能帮助你更好地理解和应用这些技术。