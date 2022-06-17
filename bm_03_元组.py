"""
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

元组中的元素类型也可以不相同：
注意：下角标取值超界会报错，但切片不会
"""
tuple_test = ("abc", 123, 5 + 6j, True)
tiny_tuple = ("456",)

# 元组里面的元素不可修改
# tuple_test[0] = "1212"

# del删除元组对象引用
# del tuple_test

print("abc" not in tuple_test)
print(tuple_test.index("abc"))
print(tuple_test.count("abc"))

print(tuple_test[3])
print(tuple_test[0:2])
print(tuple_test[2:])
print(tuple_test * 3)
print(tuple_test + tiny_tuple)

tuple_empty = ()      # 空元组
tuple_one = ("123",)  # 一个元素需要在结尾加 ,
