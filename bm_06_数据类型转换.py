"""
隐式类型转换 - 自动完成（Python 会将较小的数据类型转换为较大的数据类型，以避免数据丢失。）
显式类型转换 - 需要使用类型函数来转换
"""

num_int = 123
num_float = 123.45

num_new = num_int + num_float
print("datatype of num_int", type(num_int))
print("datatype of num_float", type(num_float))

print("datatype of num_new", type(num_new))
print("value of num_new", num_new)

# int()强转
x = int(1)
y = int(2.8)
z = int("3")

print(x, y, z)

# float强转
x = float(1)
y = float(2.8)
z = float(3)

print(x, y, z)

# str强转
x = str(123)
y = str(2.8)
z = str("s1")

print(x, type(x), y, type(y), z, type(z))

if x != 123:
    print("x != 123")

x = 123
print(hex(x))
print(oct(x))
print(chr(123))  # 将一个整数转换为一个字符
print(ord('^'))  # 将一个字符转换为他的整数值
