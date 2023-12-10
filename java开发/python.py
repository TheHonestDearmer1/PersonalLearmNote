import os
import re

print("开始执行")
directory = os.getcwd()  # 获取当前目录
md_files = []  # 存储以.md结尾的文件

# 遍历目录树
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.md'):  # 只处理以.md结尾的文件
            file_path = os.path.join(root, file)
            md_files.append(file_path)

replaced = True  # 设置一个标志变量，用于判断是否替换成功

for file in md_files:
    replaced = True  # 在每次循环开始时，将标志变量设置为True
    print(file)
    num=0
    while replaced:
        num += 1
        print(num)
        file_path = os.path.join(directory, file)  # 获取文件路径
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 使用正则表达式进行替换
        new_content = re.sub(r'<img src="(.*?)"[^>]*>', r'![\1](\1)', content)
        if content == new_content:
            # 如果替换前后的内容相同，则没代表找到了要替换的内容
            replaced = False
            # 将替换后的内容写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            print("写入成功")

print("全部替换完成")


