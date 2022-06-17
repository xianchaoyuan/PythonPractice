right_num = 7
guess_num = -1

# while guess_num != right_num:
#     guess_num = int(input("请输入你猜测的值 "))
#     if guess_num == right_num:
#         print("you are right!")
#     elif guess_num < right_num:
#         print("the number is low!")
#     elif guess_num > right_num:
#         print("the number is too high!")

# 计算1-100总和
i, j = 1, 0
while i <= 100:
    j += i
    i += 1
print("1-100总和为:", j)

# while循环使用else语句
count = 0
while count < 0:
    print("count < 0")
else:
    print("count >= 0")

# for循环遍历列表
list_test = ["a", "b", "c"]
for val in list_test:
    print(val)
else:
    print("list_test is empty!")

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

# range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长')
# for i in range(0, 100, 1):
#     print(i)

for i in range(-10, -100, -10):
    print(i, end=" ")
