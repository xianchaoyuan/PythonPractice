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
# 关键字参数
# 默认参数
# 不定长参数

# 必须参数(必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。)
def print_me(str):
    print(str)


print_me("yuanxianchao")


# 关键字参数
def print_me(str1, str2):
    print(str1, end=",")
    print(str2)

print_me("1", 2)
