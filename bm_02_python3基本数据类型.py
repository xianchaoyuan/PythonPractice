counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "noob"  # 字符串
print(counter)
print(miles)
print(name)

# 多个变量赋值
a = b = c = 1
print(a, b, c)

a, b, c = 1, 'world', "hello"
print(a, b, c)

# 不可变数据（3个） Number(数字) String(字符串) Tuple(元组)
# Number int float bool complex(复数)
a, b, c, d = 100, 100.01, True, 3 + 5j
print(a, b, c, d)
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int))

'''
isinstance 和 type 的区别在于:
    type()不会认为子类是一种父类类型。
    isinstance()会认为子类是一种父类类型。
'''


class A:
    pass


class B(A):
    pass


# python所有的类都是<class 'type'>
print(type(B) == type(A))
print(type(B()) == type(A))
print(type(B()) == A)

print(isinstance(B(), A))

print(issubclass(B, A))
print(issubclass(bool, int))

# 数值运算
print("-" * 40)
print(5 + 4)
print(5 - 4)
print(5 * 4)
print(5 / 4)
print(5 % 4)  # 取余
print(5 // 4)  # 取整
print(5 ** 4)  # 乘方

# String
# 索引值：0开始 -1末尾
print("-" * 40)
str_test = "Hello World"

print(str_test)
print(str_test[0:8] == "12345")
print(str_test[0:-1])
print(str_test[0:])
print(str_test * 2)
print(str_test + "Test")

