"""
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。

注意：
1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。
"""

dict_test = {}
dict_test["one"] = "这是第一个值"
dict_test[123] = "这是第二个值"
tiny_dict = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(tiny_dict)

dict_x = {x: x ** 2 for x in (2, 4, 6)}
print(dict_x)

print(dict_test["one"])
print(dict_test[123])
print(dict_test)
print(dict_test.keys())
print(dict_test.values())

# 增
dict_test["first"] = "name"
print(dict_test)

# 删
del dict_test["first"]
print(dict_test)

# 改
dict_test["one"] = "第一个值被修改"
print(dict_test)

# 查
print(dict_test.get(""))
