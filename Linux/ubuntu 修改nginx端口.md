 

在 [Ubuntu](https://so.csdn.net/so/search?q=Ubuntu&spm=1001.2101.3001.7020) 系统中修改 Nginx 服务器监听的默认端口（通常是 80 端口）的步骤如下：

1.  打开 [Nginx](https://so.csdn.net/so/search?q=Nginx&spm=1001.2101.3001.7020) 配置文件：
    
    ```bash
    sudo nano /etc/nginx/sites-available/default
    ```
    
2.  在 `server` 块内找到 `listen` 行，它通常会类似这样：
    
    ```
    listen 80 default_server;
    ```
    
    将 `80` 替换为你想要设置的新端口号，例如：
    
    ```
    listen 8080 default_server;
    ```
    
3.  如果你的配置文件中有 HTTPS 设置（即443端口），并且你也想更改HTTPS端口，查找对应的 `listen 443` 行并进行修改。
    
4.  保存并关闭编辑器。
    
5.  检查配置文件是否正确无误：
    
    ```bash
    sudo nginx -t
    ```
    
    这将检查配置文件的语法错误。如果没有错误，输出应该显示“configuration file syntax is OK”和“configuration file test is successful”。
    
6.  重新加载 Nginx 以应用新的配置更改：
    
    ```bash
    sudo systemctl reload nginx
    ```
    
    或者如果你的[系统](https://so.csdn.net/so/search?q=%E7%B3%BB%E7%BB%9F&spm=1001.2101.3001.7020)还在使用旧的服务管理命令：
    
    ```bash
    sudo service nginx reload
    ```
    

现在，Nginx 应该已经不再监听原来的 80 端口，而是开始监听你新指定的端口（如本例中的 8080 端口）。访问时，请确保在浏览器中输入相应的端口号。

请注意，在生产环境中，如果你不是为了调试或避免端口冲突而修改端口，一般建议保留 80 和 443 端口供 HTTP 和 HTTPS 使用，因为它们是标准的Web服务端口，并且大多数防火墙和客户端默认会连接这些端口。如果确实有冲突，应考虑调整其他服务的端口而非Nginx。

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[CS入门技能树](https://edu.csdn.net/skill/gml/gml-1c31834f07b04bcc9c5dff5baaa6680c?utm_source=csdn_ai_skill_tree_blog)[Linux入门](https://edu.csdn.net/skill/gml/gml-1c31834f07b04bcc9c5dff5baaa6680c?utm_source=csdn_ai_skill_tree_blog)[初识Linux](https://edu.csdn.net/skill/gml/gml-1c31834f07b04bcc9c5dff5baaa6680c?utm_source=csdn_ai_skill_tree_blog)39857 人正在系统学习中

本文转自 <https://blog.csdn.net/iteye_10392/article/details/136396073>，如有侵权，请联系删除。