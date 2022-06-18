"""
如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了。
为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。
"""

import sys


def test():
    for i in sys.argv:
        print(i)

print(sys.path)  # Python解释器自动查找所需模块的路径的列表

a = [1]

# 每个模块都有一个__name__属性
if __name__ == "__main__":
    print("程序自身在运行")
else:
    print("我来自另一个模块")

# 内置函数dir()可以找到模块内定义的所有名称，以一个字符串列表的形式返回
print(dir())

# 为什么报错
# print(sys.ps1)
# print(sys.ps2)

print(__path__)