
# Hello World
print("hello world")

# 数字求和
num1 = input("请输入一个数：")
num2 = input("请输入一个数：")

print("两数之和为：", float(num1) + float(num2))

# 平方根
num = float(input("请输入一个数字："))
num_sqrt = num ** 0.5

print("平方根：", num_sqrt)

import cmath

# 二次方程
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

d = b ** 2 - 4 * a * c
root1 = (-b + cmath.sqrt(d)) / 2 * a
root2 = (-b - cmath.sqrt(d)) / 2 * a
print("root1:", root1, "root2", root2)
"""
计算三角形面积
海伦公式：p = (a+b+c)/2
        A = (p*(p-a)*(p-b)*(p-c))**0.5
"""

# # 计算三角形的面积
# a = float(input("第一边长："))
# b = float(input("第二边长："))
# c = float(input("第三边长："))
#
# # 半周长
# p = (a + b + c) / 2
# print("半周长：", p)
#
# # 面积(海伦公式)
# A = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print("面积：", A)

"""
计算圆面积
S =  𝝅*r**2
"""

# def area(r):
#     PI = 3.1415
#     return PI * r ** 2
#
#
# print(area(5))

"""
随机数生成
"""

# import random
#
# print(random.randint(0, 9))

"""
摄氏度转华氏温度
celsius * 1.8 = fahrenheit - 32
"""

# celsius = float(input('输入摄氏温度：'))
#
# fahrenheit = (celsius * 1.8) + 32
# print("%0.1f 摄氏温度转为华氏温度为 %0.1f" % (celsius, fahrenheit))

"""
变量交换
"""
# x = float(input("输入x值："))
# y = float(input("输入y值："))
# print("交换前 x:%0.1f y:%0.1f" % (x, y))
#
# temp = x
# x = y
# y = temp
#
# print(f"交换后 x:{x} y:{y}")


"""
if语句输出正数负数和零
"""

# num = float(input("请输入一个数："))
# if num > 0:
#     print("正数")
# elif num == 0:
#     print("零")
# else:
#     print("负数")


"""
判断字符串是否为数字
"""

# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#
#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except(TypeError, ValueError):
#         pass
#
#     return False
#
#
# # 测试字符串和数字
# print(is_number('foo'))   # False
# print(is_number('1'))     # True
# print(is_number('1.3'))   # True
# print(is_number('-1.37')) # True
# print(is_number('1e3'))   # True
#
#
# # 测试 Unicode
# # 阿拉伯语 5
# print(is_number('٥'))  # True
# # 泰语 2
# print(is_number('๒'))  # True
# # 中文数字
# print(is_number('四')) # True
# # 版权号
# print(is_number('©'))  # False
#
# # 检测字符串是否只由数字组成
# print("1a22".isnumeric())


"""
判断奇偶数
"""

# num = int(input("num:"))
#
# if num%2 == 0:
#     print("{1} 是偶数".format(num, num))
# else:
#     print("{0} 是奇数".format(num))


"""
判断闰年
"""

# year = int(input("输入一个年份："))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("%d 年是闰年" % (year))
#         else:
#             print(f"{year} 年不是闰年")
#     else:
#         print("{0} 年是闰年".format(year))
# else:
#     print(f"{year} 年不是闰年")


"""
获取最大值函数
"""

# # 最简单的
# print(max(1, 2))
# print(max('a', 'b'))
#
# # 也可以对列表和元组使用
# print(max([1, 2]))
# print(max((1, 2)))
#
# # 更多实例
# print("80, 100, 1000 最大值为: ", max(80, 100, 1000))
# print("-20, 100, 400最大值为: ", max(-20, 100, 400))
# print("-80, -20, -10最大值为: ", max(-80, -20, -10))
# print("0, 100, -400最大值为:", max(0, 100, -400))


"""
判断一个数是不是质数
"""

# num = int(input("请输入一个数："))
#
# if num <= 1:
#     print("%d 不是质数" % (num))
# else:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print("%d 不是质数" % (num))
#
#     print(f"{num} 是质数")


"""
输出指定范围内的素数
"""

# lower = int(input("请输入一个最小数："))
# upper = int(input("请输入一个最大数："))
#
# for i in range(lower, upper + 1):
#     if i <= 1:
#         continue
#
#     for j in range(2, i):
#         if (i % j) == 0:
#             is_prime = False
#             break
#     else:
#         print(f"{i}")


"""
阶层实例
整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。
"""


# num = int(input("请输入一个整数："))
# factorial = 1
#
# if num < 0:
#     print("负数没有阶层")
# elif num == 0:
#     print(f"0的阶乘为{factorial}")
# else:
#     for i in range(1, num+1):
#         factorial = factorial*i
#     print("{0} 的阶乘为{1}".format(num, factorial))


"""
九九乘法表
"""

for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={}".format(j, i, i*j), end=" ")
    print("")

