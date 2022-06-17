"""
列表
列表都可以进行的操作包括索引，切片，加，乘，检查成员。
列表的数据项不需要具有相同的类型
"""

# 列表
list_test = ["abc", "bcd", "cde", "def"]
tiny_list = [123, "run"]

print(list_test)
print(list_test[2])
print(list_test[1:3])
print(list_test[1:7:2])
print(list_test * 2)
list_test[3] = []
list_test.append("123444")
print(list_test + tiny_list)


def reverseWords(input):
    word_list = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素d
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    word_list = word_list[-1::-1]

    output = " ".join(word_list)
    return output


if __name__ == "__main__":
    input_str = "I like you"
    print(reverseWords(input_str))

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

# 增
list1.append("efg")
print(list1)

# 删
list1.pop(0)
print(list1)
del list1[2]
print(list1)

# 改
list1[0] = "new"
print(list1)

# 查
print("new" in list1)
print(list1.count("new"))
print(list1.index("efg"))
