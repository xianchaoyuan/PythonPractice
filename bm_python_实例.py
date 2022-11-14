# # Hello World
# print("hello world")
#
# # 数字求和
# num1 = input("请输入一个数：")
# num2 = input("请输入一个数：")
#
# print("两数之和为：", float(num1) + float(num2))
#
# # 平方根
# num = float(input("请输入一个数字："))
# num_sqrt = num ** 0.5
#
# print("平方根：", num_sqrt)

# import cmath
#
# # 二次方程
# a = float(input("a:"))
# b = float(input("b:"))
# c = float(input("c:"))
#
# d = b ** 2 - 4 * a * c
# root1 = (-b + cmath.sqrt(d)) / 2 * a
# root2 = (-b - cmath.sqrt(d)) / 2 * a
# print("root1:", root1, "root2", root2)

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

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("{}*{}={}".format(j, i, i*j), end=" ")
#     print("")


"""
斐波那契数列
"""

# n1 = 0
# n2 = 1
# count = 2
# nterms = 10
# print(n1, ",", n2, end=",")
# while count < nterms:
#     nth = n1 + n2
#     print(nth, ",", end="")
#     n1 = n2
#     n2 = nth
#     count += 1


"""
阿姆斯特朗数
"""

# num = int(input("请输入一个整数："))
#
# sum = 0
# n = len(str(num))
#
# temp = num
# while temp > 0:
#     digit = temp%10
#     sum += digit**n
#     temp //= 10
#
# if num == sum:
#     print(num, "是阿姆斯特朗数")
# else:
#     print("{}不是阿姆斯特朗数".format(num))


"""
十进制转二进制，八进制，十六进制
"""

# dec = int(input("请输入一个整数："))
#
# print("十进制：", dec)
# print("二进制：", bin(dec))
# print("八进制：", oct(dec))
# print("十六进制：", hex(dec))


"""
ASCII码与字符相互转换
"""

# c = input("请输入一个字符：")
#
# a = int(input("请输入一个ASCII码："))
#
# print(c+" 的ASCII码为：", ord(c))
# print(a, " 对应的字符为：", chr(a))


"""
最大公约数
"""

# # 定义一个函数
# def hcf(x, y):
#     """该函数返回两个数的最大公约数"""
#
#     # 获取最小值
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#
#     for i in range(1, smaller + 1):
#         if (x % i == 0) and (y % i == 0):
#             hcf = i
#
#     return hcf
#
#
# # 用户输入两个数字
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))
#
# print(num1, "和", num2, "的最大公约数为", hcf(num1, num2))


"""
最小公倍数
"""

# # 定义函数
# def lcm(x, y):
#     #  获取最大的数
#     if x > y:
#         greater = x
#     else:
#         greater = y
#
#     while True:
#         if (greater % x == 0) and (greater % y == 0):
#             lcm = greater
#             break
#         greater += 1
#
#     return lcm
#
#
# # 获取用户输入
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))
#
# print(num1, "和", num2, "的最小公倍数为", lcm(num1, num2))


"""
简易计算器
"""

# # 定义函数
# def add(x, y):
#     """相加"""
#
#     return x + y
#
#
# def subtract(x, y):
#     """相减"""
#
#     return x - y
#
#
# def multiply(x, y):
#     """相乘"""
#
#     return x * y
#
#
# def divide(x, y):
#     """相除"""
#
#     return x / y
#
#
# # 用户输入
# print("选择运算：")
# print("1、相加")
# print("2、相减")
# print("3、相乘")
# print("4、相除")
#
# choice = input("输入你的选择(1/2/3/4):")
#
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))
#
# if choice == '1':
#     print(num1, "+", num2, "=", add(num1, num2))
#
# elif choice == '2':
#     print(num1, "-", num2, "=", subtract(num1, num2))
#
# elif choice == '3':
#     print(num1, "*", num2, "=", multiply(num1, num2))
#
# elif choice == '4':
#     print(num1, "/", num2, "=", divide(num1, num2))
# else:
#     print("非法输入")


"""
生成日历
"""

# import calendar
#
# yy = int(input("输入年份："))
# mm = int(input("输入月份："))
#
# print(calendar.month(yy, mm))


"""
递归实现斐波那契数列
"""

# def recur_fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return recur_fibo(n - 1) + recur_fibo(n - 2)
#
#
# # 获取用户输入
# nterms = int(input("您要输出几项? "))
#
# # 检查输入的数字是否正确
# if nterms <= 0:
#     print("输入正数")
# else:
#     print("斐波那契数列:")
#     for i in range(nterms):
#         print(recur_fibo(i))


"""
文件IO
"""

# # 写文件
# with open("test.txt", "wt") as out_file:
#     out_file.write("123444567890")
#
# # 读文件
# with open("test.txt", "rt") as in_file:
#     print(in_file.read())


"""
字符串判断
"""

# # 测试实例一
# print("测试实例一")
# str = "runoob.com"
# print(str.isalnum())  # 判断所有字符都是数字或者字母
# print(str.isalpha())  # 判断所有字符都是字母
# print(str.isdigit())  # 判断所有字符都是数字
# print(str.islower())  # 判断所有字符都是小写
# print(str.isupper())  # 判断所有字符都是大写
# print(str.istitle())  # 判断所有单词都是首字母大写，像标题
# print(str.isspace())  # 判断所有字符都是空白字符、\t、\n、\r
#
# print("------------------------")
#
# # 测试实例二
# print("测试实例二")
# str = "runoob"
# print(str.isalnum())
# print(str.isalpha())
# print(str.isdigit())
# print(str.islower())
# print(str.isupper())
# print(str.istitle())
# print(str.isspace())


"""
字符串大小写转换
"""

# str = "www.runoob.com"
# print(str.upper())          # 把所有字符中的小写字母转换成大写字母
# print(str.lower())          # 把所有字符中的大写字母转换成小写字母
# print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
# print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写


"""
计算每个月天数
"""

# import calendar
# monthRange = calendar.monthrange(2016, 9)
# print(monthRange)


"""
获取昨天日期
"""

# import datetime
# def get_yesterday():
#     today = datetime.date.today()
#     oneday = datetime.timedelta(days = 1)
#     yesterday = today - oneday
#     return yesterday
#
#
# print(get_yesterday())


"""
快速排序
"""


def partition(arr, low, high):
    """
    :param arr: 排序数组
    :param low: 起始索引
    :param high: 结束索引
    :return:
    """
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]

    for j in range(low, high):

        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("排序后的数组:", arr)