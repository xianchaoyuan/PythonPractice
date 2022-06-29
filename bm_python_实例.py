
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
