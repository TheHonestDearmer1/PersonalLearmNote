 

### Windows 访问 Linux 文件

**方法一**：通过 `\\wsl$` 访问 Linux 文件时将使用 WSL 分发版的默认用户。 因此，任何访问 Linux 文件的 Windows 应用都具有与默认用户相同的权限。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200809195209271.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0Nhb3lhbmdfSGU=,size_16,color_FFFFFF,t_70)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200809195236629.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0Nhb3lhbmdfSGU=,size_16,color_FFFFFF,t_70)

**方法二**：通过VS Code访问Linux文件

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200809195524622.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0Nhb3lhbmdfSGU=,size_16,color_FFFFFF,t_70)

> PS: 在任何情况下，请勿使用Windows应用程序，工具，脚本，控制台等在％LOCALAPPDATA％目录下访问，创建和/或修改Linux文件。

### Linux 访问 Windows 文件

在从 WSL 访问 Windows 文件时，可以直接使用`/mnt/{Windows盘符}`进入对应的盘中。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200809195120235.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0Nhb3lhbmdfSGU=,size_16,color_FFFFFF,t_70)

如果文件没有关联的元数据，则我们会将 Windows 用户的有效权限转换为读取/写入/执行位，并将其设置为对用户、组和其他用户而言相同的值。 例如，如果你的 Windows 用户帐户具有对该文件的读取和执行访问权限，但不具有对该文件的写入访问权限，则该帐户将对用户、组和其他对象显示为 **r-x**。 如果该文件在 Windows 中设有“只读”属性，则我们不会在 Linux 中授予写入权限。

当需要对Windows里面的文件进行写操作时，需要使用**管理员权限**运行WSL，并且使用`chmod 777 {文件}`修改文件的权限

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[CS入门技能树](https://edu.csdn.net/skill/gml/gml-1c31834f07b04bcc9c5dff5baaa6680c?utm_source=csdn_ai_skill_tree_blog)[Linux入门](https://edu.csdn.net/skill/gml/gml-1c31834f07b04bcc9c5dff5baaa6680c?utm_source=csdn_ai_skill_tree_blog)[初识Linux](https://edu.csdn.net/skill/gml/gml-1c31834f07b04bcc9c5dff5baaa6680c?utm_source=csdn_ai_skill_tree_blog)40249 人正在系统学习中

本文转自 <https://blog.csdn.net/Caoyang_He/article/details/107898883>，如有侵权，请联系删除。