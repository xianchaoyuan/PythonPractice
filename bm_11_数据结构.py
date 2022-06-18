"""
列表：列表可以修改，而字符串和元组不能。
"""
list_test = [1, 2, 3]

"""
把一个元素添加到列表结尾
相当于list_test[len(list_test):] = [10]
"""
list_test.append(10)

"""
通过添加指定列表的所有元素来扩充列表
相当于a[len(a)] = L
"""
list_test.extend([123, 3, 4, 5])

"""
在指定位置插入一个元素
"""
list_test.insert(0, 100)
list_test.insert(2, 111)

"""
删除列表中值为x的第一个元素，如果没有，返回错误
"""
list_test.remove(100)
# list_test.remove(11111)


"""
从列表指定位置移除元素，并将其返回
不指定索引将删除最后一个元素
"""
list_test.pop()
list_test.pop(3)

"""
移除列表中的所有项
"""
# list_test.clear()


"""
返回列表中第一个值为x的元素的索引
如果没有，返回错误
"""
list_test.index(3)

"""
返回x在列表中出现的次数
"""
print(list_test.count(3))

"""
对列表的元素进行排序
"""
list_test.sort()

"""
倒排列表中的元素
"""
list_test.reverse()

"""
返回列表的浅拷贝
"""
print(id(list_test))
list1 = list_test.copy()
print(id(list1))

print(list_test)

"""
将列表当做堆栈使用
"""
list2 = [1]
list2.append(2)
list2.append(3)

list2.pop()
list2.pop()

print(list2)

"""
把列表当做队列使用
"""
list3 = [1, 2]
list3.append(3)

list3.pop(0)
print(list3)

from collections import deque

queue_test = deque(["rensiwen", "yuanxianchao"])
queue_test.append("xiaochao")
queue_test.popleft()
print(queue_test)

# 列表推导式
list4 = [x for x in range(10)]
print(list4)

list5 = [[x, y] for x in range(3) for y in range(10)]
print(list5)

# 嵌套列表解析
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print([[row[i] for row in matrix] for i in range(4)])

# 另外一种实现
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

# 另外一种实现
transposed = []
for i in range(4):
    sub = []
    for row in matrix:
        sub.append(row[i])
    transposed.append(sub)

print(transposed)

# del语句
a = [1, 2, 3]
del a[0]
print(a)

del a[:]
print(a)

"""
集合：一个无序不重复元素的集
基本功能包括 关系测试，消除重复元素
"""
a = {1, 2, 3}
b = {1, 2, 4, 5}
print(a - b)
print(a & b)
print(a | b)
print(a ^ b)  # 在a或b中的字母，但不同时在a和b中

# 结合推导式
a = {x for x in "abcracda" if x not in "abc"}
print(a)


"""
字典：以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值
无序的键值对集合
在同一字典内，关键字必须是互不相同的
"""
dict_test = {"yuanxianchao":28, "rensiwen":28}
print(dict_test["rensiwen"])

del dict_test["yuanxianchao"]

for val in dict_test:
    print(val)

print("rensiwen" in dict_test)
print("yuanxianchao" not in dict_test)

# 推导式构建
dict_test = {x:x**2 for x in (2, 4, 6)}
print(dict_test)

# 如果关键字只是简单的字符串，使用关键字参数指定键值对更方便
dict_test = dict(a=12, b=13, c=77)
print(dict_test)

# 遍历技巧
for i, v in dict_test.items():
    print(i, v)

# 在序列中遍历，索引位置和对应值可以使用enumerate()函数同时得到
for i, v in enumerate(["a", "b", "c"]):
    print(i, v)

# 同时遍历两个或者多个序列(个数不同以少的为主)
for a, b in zip(['a', 'b', 'c'], ['d', 'e', 'f']):
    print(a, b)

# 反向遍历一个序列
for x in reversed(('a', 'b', 'c')):
    print(x)

# 按顺序遍历一个序列
for x in (1, 3, 2, 100, 33):
    print(x, end=",")
print('')

for x in sorted((1, 3, 2, 100, 33)):
    print(x, end=",")