"""
错误与异常

try:
    可能发生异常的语句
except[异常 as 别名:]
    出现异常的准备手段
else:
    未出现异常应做的事情
finally:
    不管出不出现异常都会做的事情
"""

# import sys
#
# while True:
#     try:
#         x = int(input("请输入一个数字："))
#         break
#     except ValueError:
#         print("输入有误，请重新输入！".format(ValueError))
#
# try:
#     f = open('bm_13_文件.py')
#     s = f.readline()
#     i = int(s.strip())
#     print(i)
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise
#
# # try/except 语句还有一个可选的 else 子句，
# # 如果使用这个子句，那么必须放在所有的 except 子句之后。
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#         print(f.readlines())
#     except IOError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()
#
# # try-finally 语句无论是否发生异常都将执行最后的代码。
# try:
#     print("try-finally")
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)
# finally:
#     print('这句话，无论异常是否发生都会执行。')
#
#
# # Python 使用 raise 语句抛出一个指定的异常。
# # raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）
# # x = 10
# # if x > 5:
# #     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
#
# # try:
# #     raise NameError('HiThere')
# # except NameError:
# #     print('An exception flew by!')
# #     raise
#
#
# # 用户自定义异常
# # 你可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承，例如
# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return repr(self.value)
#
#
# try:
#     raise MyError(2 * 2)
# except MyError as e:
#     print('My exception occurred, value:', e.value)
#
# # 定义清理行为
# # try:
# #     raise KeyboardInterrupt
# # finally:
# #     print('Goodbye, world!')
#
#
# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finally clause")
#
# divide(1, 2)
#
#
# # 预定义的清理行为
# 当执行完毕，文件并不会关闭
for line in open("bm_13_文件.py"):
    print(line)

# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法
with open("bm_13_文件.py") as f:
    for line in f:
        print(line, end="")
