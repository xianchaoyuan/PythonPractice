"""
文件 打开 读取 写入 关闭
"""

# 打开文件
import time

f = open('D:/MyProject/PythonPractice/test.txt', 'a', encoding='UTF-8')
print(type(f))

# 读取文件
# content1 = f.read(10)
# print(f'读取前10个字节的结果：{type(content1)}{content1}')
# content2 = f.read()
# print(f'读取剩余全部内容：{type(content2)}{content2}')
# content3 = f.readlines()
# print(f'读取文件全部内容：{type(content3)}{content3}')
# content4 = f.readline()
# print(f'第一行数据：{type(content4)}{content4}')
# 循环读取
# for line in f:
#     print(f'每一行数据为：{line}')

# time.sleep(50000)

# 自动解除关闭
# with open('D:/MyProject/PythonPractice/test.py', 'r', encoding='UTF-8') as f:
#     for line in f:
#         print(f'每一行数据为：{line}')

# 文件写入
f.write('test')
f.flush()

# 文件关闭
f.close()
