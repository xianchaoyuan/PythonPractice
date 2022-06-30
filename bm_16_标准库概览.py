# # 访问互联网
# from urllib.request import urlopen
#
# for line in urlopen('https://www.runoob.com/python/python-variable-types.html'):
#     line = line.decode('utf-8')
#     if 'EST' in line or 'EDT' in line:
#         print(line)
#
# # 注意第二个例子需要本地有一个在运行的邮件服务器。
# import smtplib
#
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
#                 """To: jcaesar@example.org
#                 From: soothsayer@example.org
#
#                 Beware the Ides of March.
#                 """)
# server.quit()


# 日期和时间
from datetime import date

now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %y is a %A on the %d day of %B."))
birthday = date(1995, 1, 22)
age = now - birthday
print(age.days)

# 数据压缩(数据很小时压缩后反而更大)
import zlib

s = b'witch which has has which which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

print(zlib.decompress(t))
print(zlib.crc32(s))

# 性能度量(相对于 timeit 的细粒度，:mod:profile 和 pstats 模块提供了针对更大代码块的时间度量工具。)
from timeit import Timer

print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a, b = b, a', 'a=1; b=2').timeit())


# 测试模块
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


import doctest

doctest.testmod()  # 自动验证嵌入测试

import unittest


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)


unittest.main()  # Calling from the command line invokes all tests
