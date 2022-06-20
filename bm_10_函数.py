"""
不可变对象：strings tuples numbers
可变对象：list dict

不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：
不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
"""


# 比较两个数，返回最小值
def min_num(a, b):
    if a < b:
        return a
    elif b < a:
        return b


print(min_num(1, 100))
print(min_num("abc", "345"))

# 更改列表数据
list_test = [1, 2, 3]


def list_append(list1):
    list1.pop()


list_append(list_test)
print(list_test)


# 传递不可变对象
def change(val):
    print(id(val))
    val = 10
    print(id(val))


a = 1
print(id(a))
change(a)


# 传递可变对象
def change(val):
    print(id(val))
    val.append(3)
    print(id(val))


list_test = [1, 2]
print(id(list_test))
change(list_test)


# 参数
# 以下是调用函数时可使用的正式参数类型：
#
# 必需参数
# 默认参数

# 不定长参数
# 关键字参数


# 必须参数(必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。)
def print_me(str1):
    print(str1)


print_me(str1="12121")
print_me("yuanxianchao")
print_me("123456")


# 关键字参数(允许函数调用时参数的顺序与声明不一致，因为python解释器能够用参数名匹配)
def print_me(str1, str2):
    print(str1, end=",")
    print(str2)


print_me("1", 2)
print_me(str2="1", str1="2")


# 默认参数
def print_info(name, age=15):
    """打印任何传入的字符串"""
    print("名字：", name)
    print("年龄：", age)


print_info("mujunlong", 18)
print_info("yuanxianchao", 14)
print_info('zhuwenchao')


# 不定长参数(*的参数会以tuple的形式导入，存放所有未命名的变量参数)
def print_info(arg1, *args):
    print(type(args))
    print(arg1, args)


print_info(123, 1213, 122222)


def print_info(arg1, *args):
    print("输出")
    print(f"args={arg1}")
    for val in args:
        print(val, type(val))


print_info(123)
print_info(10, 20, {1, 2, 3}, 40, {121212})


# 连个**的参数会以字典的形式导入
def print_info(arg1, **kwargs):
    print("输出：")
    print(arg1)
    print(kwargs)


print_info(123, key=123)


# 可接收任意参数
def print_info(*args, **kwargs):
    print("输出：")
    print(args)
    print(kwargs)


print_info(11, 22, a=23, key="123")


# *也可以单独出现，则*后的参数必须用关键字传入
def print_info(a, b, *, c):
    print(a, b, c)


print_info(1, 2, c=3)


def print_info(a, b, **kwargs):
    print(type(kwargs))
    print(a, b, kwargs)


print_info(1, 2, c=100)

"""
匿名函数
lambda 只是一个表达式，函数体比 def 简单很多。
lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
"""
func = lambda b: b + 10
print(func)
print(func(100))

func = lambda a, b: a + b
print(func(1, 2))


def my_func(n):
    return lambda a: a * n


my_lambda1 = my_func(2)
my_lambda2 = my_func(3)

print(type(my_lambda1), my_lambda1(1))
print(type(my_lambda2), my_lambda2(2))


# 强制位置参数(3.8以后支持)
# def print_info(a, b, /, c, d , *, e, f):
#     print(a, b, c, d, e, f)