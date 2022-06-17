"""
Python 支持各种数据结构的推导式：

列表(list)推导式
字典(dict)推导式
集合(set)推导式
元组(tuple)推导式
"""

# 列表推导式
names = ["Bom", "Tom", "Jerry"]
new_names = [name.upper() for name in names if len(name) >= 3]
print(new_names)

# 计算30天内可以被3整除的整数
days = [i for i in range(30) if i % 3 == 0]
print(days)

# 字典推导式
list_demo = ["Google", "Baidu", "Tencent"]
new_dict = {key: len(key) for key in list_demo}
print(new_dict)

# 集合推导式
# 计算数字1，2，3的平方
set_test = {i ** 2 for i in (1, 2, 3)}
print(set_test)

# 元组推导式
# 注意：元组推导式返回的结果是一个生成器对象。
tuple_test = (x for x in range(0, 10))
print(tuple_test)
print(tuple(tuple_test))  # 使用 tuple() 函数，可以直接将生成器对象转换成元组
