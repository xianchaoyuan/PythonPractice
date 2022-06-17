"""
迭代是Python最强大的功能之一，是访问集合元素的一种方式。

迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：iter() 和 next()
"""


# list_test = [1, 2, 3, 4]
# it = iter(list_test)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# # print(next(it))  # 超界报错
#
# it = iter(list_test)
# for x in it:
#     print(x, end=" ")
#
# # 使用next遍历
# import sys
#
# it = iter(list_test)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


# 创建一个迭代器
import sys


class MyIter:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


# myclass = MyIter()
# it = iter(myclass)
# print(next(it))
# print(next(it))

# 生成器
# 使用了 yield 的函数被称为生成器（generator）


def fibonacci(n):
    """
    :param n: 值个数
    :return:
    """
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        a, b = b, a + b
        yield a
        counter += 1


f = fibonacci(10)
while True:
    try:
        print(next(f), end=",")
    except StopIteration:
        sys.exit()
