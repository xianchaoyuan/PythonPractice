"""
集合（set）是一个无序的不重复元素序列。
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。

基本功能是进行成员关系测试和删除重复元素。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""

set_test = {"abc", 123}
set_empty = set()
set_one = {"abc", 456}

print(type(set_test), type(set_empty))

if "abc" in set_test:
    print("abc 在集合中")
else:
    print("abc 不在集合中")

# set可以进行集合运算
print("原始", set_test)
print("差集", set_test - set_one)
print("并集", set_test | set_one)
print("交集", set_test & set_one)
print("不同", set_test ^ set_one)

# 增
set_test.add("add")
set_test.update("add")
print(set_test)

# 删
set_test.pop()  # 随机删除集合中的一个元素
set_test.remove("add")  # 元素不存在，报错
set_test.discard("add")  # 元素不存在，不报错
print(set_test)

# 改
# 查
if "abc" in set_test:
    print("set_test has abc")
set_test.update("abc")
set_new = {"abc"}
print(set_test.intersection(set_new))
