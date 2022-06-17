# 这是一个注释（#为保证整齐，需要空一格）
print('hello world')

"""
PEP
这是多行注释（块注释）
绝对不要描述代码
"""

# 这是第二个注释
print('hello hello')  # 输出欢迎信息

# 行与缩进（缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数）
a = False
print("12345678")
if a:
    print("Answer")
    print("True")
else:
    print("Answer")
# print("False")


# 多行语句
item_one = "1"
item_two = "2"
item_thr = "3"
total = item_one + \
        item_two + \
        item_thr

# [] {} ()中的多行语句不用使用\
total = ["item_one", "item_two", "item_thr"]

# 字符串‘’ “” ''''''(指定多行字符串)
word = "字符串"
sentence = "这是一个句子"
paragraph = '''这是一个段落,
可以由多行组成
'''
# 反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。
# 如 r"this is a line with \n" 则 \n 会显示，并不是换行
print(r"这是一个转义字符\n")
print("是否换行")
# 字符串的截取 变量[头下标:尾下标:步长]
str = "1234567890"

print(str)
print(str[0:8])
print(str[8:])
print(str[0:8:2])
print(str * 2)
print(str + "hello")

print("-" * 20)
print("hello\nrunoob")
print(r"hello\nrunoob")

# 等待用户输入
# input("\n\n按下 enter 键后退出")

# 同一行显示多条语句(控制台输出会打印大小)
# import sys; x='runoob'; sys.stdout.write(x+'\n')

# print输出（默认输出是换行，不换行需要end=" "）
print("first", end=" ")
print("second", end=" ")

# 导入sys模块
import sys

print('=' * 20 + 'Python import mode' + '=' * 20)
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

# 导入sys模块的argv, path
from sys import argv, path

print('=' * 20 + 'Python import mode' + '=' * 20)
print('path:', path)
print('argv', argv)

# 运算符
print("对不起" * 100)
print(100 / 200)
print(100 // 2)
print(100 ** 2)
