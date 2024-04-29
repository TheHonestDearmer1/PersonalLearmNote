 

#### 目录

*   *   *   *   [导入所需模块](#_12)
            *   [解析XML文档](#XML_17)
            *   [获取元素](#_29)
            *   [遍历XML文档](#XML_51)
            *   [写入新的元素](#_61)
            *   [修改元素的内容和属性](#_72)
            *   [删除元素](#_81)
            *   [保存修改后的XML文档](#XML_91)
            *   [示例演示](#_101)
            *   [python操作xml的常用方法](#pythonxml_141)

XML是一种常见的[数据交换格式](https://so.csdn.net/so/search?q=%E6%95%B0%E6%8D%AE%E4%BA%A4%E6%8D%A2%E6%A0%BC%E5%BC%8F&spm=1001.2101.3001.7020)，在许多应用中都被广泛使用。通过掌握Python操作XML的基础知识，您将能够轻松地处理XML数据，从而实现数据的提取、修改和存储。

内容包括以下主要部分：

*   解析XML文档：学习如何使用Python解析XML文档，获取根元素和遍历子元素。  
    访问元素的内容：了解如何读取元素的标签、文本和属性，以及如何根据需要获取特定元素。
*   写入新的元素：学习如何创建新的元素对象，并设置其标签、文本和属性，然后将其添加到XML文档中。
*   修改元素的内容和属性：掌握如何通过修改元素的文本内容和属性值来更新XML文档。
*   删除元素：了解如何从XML文档中删除指定的元素，以及如何根据需求进行元素的删除操作。
*   保存修改后的XML文档：学习如何使用ElementTree对象的.write()方法将修改后的XML文档保存到文件中。

##### 导入所需模块

在开始之前，我们需要导入`xml.etree.ElementTree`模块，该模块提供了解析和操作[XML文档](https://so.csdn.net/so/search?q=XML%E6%96%87%E6%A1%A3&spm=1001.2101.3001.7020)的功能。

```python
import xml.etree.ElementTree as ET
```

##### 解析XML文档

使用`ElementTree`模块的`parse()`函数解析XML文档。该函数将返回一个`ElementTree`对象，表示整个XML文档的树结构。

```python
# 解析XML文件并返回ElementTree对象
tree = ET.parse('example.xml')

# 解析XML字符串并返回根元素的Element对象
xml_string = '<root><element>Value</element></root>'
root = ET.fromstring(xml_string)
```

##### 获取元素

```python
# 获取XML文档的根元素
root = tree.getroot()

# 查找具有指定标签的第一个子元素
element = root.find('element')

# 查找具有指定标签的所有子元素
elements = root.findall('element')

# 获取元素的指定属性值
attribute_value = element.get('attribute_name')

# 可以使用元素对象的`.text`属性访问元素的文本内容，使用`.attrib`属性访问元素的属性。
element = root.find('element_name')
if element is not None:
    text = element.text
    attributes = element.attrib

```

##### 遍历XML文档

通过遍历根元素和其子元素，可以访问XML文档中的各个元素和其属性。

```python
for child in root:
    print('Tag:', child.tag)
    print('Text:', child.text)
    print('Attributes:', child.attrib)
```

##### 写入新的元素

可以创建新的元素对象，使用`Element()`函数或直接构造`Element`对象，并设置其标签、文本和属性。然后使用根元素的`.append()`方法将新元素添加为子元素。

```python
new_element = ET.Element('new_element')
new_element.text = 'New element text'
new_element.set('attribute_name', 'attribute_value')
root.append(new_element)
```

##### 修改元素的内容和属性

可以使用元素对象的`.text`属性修改元素的文本内容，使用`.set()`方法修改元素的属性。

```python
element.text = 'Modified text'
element.set('attribute_name', 'new_value')
```

##### 删除元素

使用根元素的`.remove()`方法删除指定的子元素。

```python
child_to_remove = root.find('element_to_remove')
if child_to_remove is not None:
    root.remove(child_to_remove)
```

##### 保存修改后的XML文档

使用`ElementTree`对象的`.write()`方法将修改后的XML文档保存到文件中。

```python
tree.write('modified.xml')
```

这是一个简单的Python操作XML的教程，涵盖了读取、写入、修改和保存XML文档的基本步骤。您可以根据自己的需求进一步扩展和优化代码。

##### 示例演示

以下是一个示例代码，演示了上述实例中的关键步骤：

```python
import xml.etree.ElementTree as ET

# 1. 读取XML文档
tree = ET.parse('example.xml')
root = tree.getroot()

# 2. 遍历XML文档
for child in root:
    print('Tag:', child.tag)
    print('Text:', child.text)
    print('Attributes:', child.attrib)

# 3. 读取元素的内容
element = root.find('element_name')
if element is not None:
    text = element.text
    attributes = element.attrib

# 4. 写入新的元素
new_element = ET.Element('new_element')
new_element.text = 'New element text'
new_element.set('attribute_name', 'attribute_value')
root.append(new_element)

# 5. 修改元素的内容和属性
element.text = 'Modified text'
element.set('attribute_name', 'new_value')

# 6. 删除元素
child_to_remove = root.find('element_to_remove')
if child_to_remove is not None:
    root.remove(child_to_remove)

# 7. 保存修改后的XML文档
tree.write('modified.xml')
```

##### python操作xml的常用方法

1.  解析XML文档：
    *   `ET.parse(file_path)`：解析XML文件并返回`ElementTree`对象。
    *   `ET.fromstring(xml_string)`：解析XML字符串并返回根元素的`Element`对象。
2.  获取元素：
    *   `ElementTree.getroot()`：获取XML文档的根元素。
    *   `Element.find(tag)`：查找具有指定标签的第一个子元素。
    *   `Element.findall(tag)`：查找具有指定标签的所有子元素。
    *   `Element.get(key)`：获取元素的指定属性值。
3.  遍历元素：
    *   使用`for`循环遍历子元素，例如 `for child in root: ...`。
4.  操作元素的文本和属性：
    *   `Element.text`：获取或设置元素的文本内容。
    *   `Element.attrib`：获取或设置元素的属性字典。
    *   `Element.set(key, value)`：设置元素的指定属性值。
5.  创建新元素：
    *   `ET.Element(tag)`：创建一个具有指定标签的新元素对象。
    *   `Element.text`：设置新元素的文本内容。
    *   `Element.set(key, value)`：设置新元素的属性值。
6.  添加和删除元素：
    *   `Element.append(child)`：将子元素添加到父元素的末尾。
    *   `Element.remove(child)`：从父元素中删除指定的子元素。
7.  修改XML文档：
    *   更新元素的文本和属性，使用`Element.text`和`Element.set()`方法。
    *   添加新元素，使用`Element.append()`方法。
    *   删除元素，使用`Element.remove()`方法。
8.  保存XML文档：
    *   `ElementTree.write(file_path)`：将修改后的XML文档写入到文件中。

* * *

*   📢博客主页：[https://blog.csdn.net/qq233325332](https://blog.csdn.net/qq233325332)
*   📢欢迎点赞 👍 收藏 ⭐留言 📝 如有错误敬请指正！
*   📢本文由 陌北v1 原创，首发于 CSDN博客🙉
*   📢停下休息的时候不要忘了别人还在奔跑，希望大家抓紧时间学习，全力奔赴更美好的生活✨

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Python入门技能树](https://edu.csdn.net/skill/python/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/python/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/python/?utm_source=csdn_ai_skill_tree_blog)409178 人正在系统学习中

本文转自 <https://blog.csdn.net/qq233325332/article/details/130799948>，如有侵权，请联系删除。