"""

# 练习1：华氏温度转换为摄氏温度。
# 提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。

f = float(input("输入华氏温度："))
c =(f - 32) / 1.8
print('%s华氏度 = %s摄氏度' % (f, c))
print( "{}华氏度 = {}摄氏度".format(f,c))

"""

"""
# 输入圆的半径计算计算周长和面积。
r = float(input("输入半径r"))
s = 2 * r * 3.14
area = 3.14 * r**2
print('周长: %s' % s )
print('面积: {}'.format(area))

"""

"""
# 公历闰年的简单计算方法（符合以下条件之一的年份即为闰年，反之则是平年）。
#
# 1、能被4整除而不能被100整除。
# 2、能被100整除也能被400整除

# 输入年份判断是不是闰年
y = int(input("输入年份："))
if  y%4 ==0 and y%100!= 0:
    print('%s闰年'%y)
elif  y%100 ==0 and y%400 ==0:
    print('%s闰年'%y)
else:
    print('%s不是闰年'%y)
"""

"""
# 分支嵌套
y = int(input("输入年份："))
if  y%4 ==0 and y%100!= 0:
    print('%s闰年'%y)
else:
    if  y%100 ==0 and y%400 ==0:
        print('%s闰年'%y)
    else:
        print('%s不是闰年'%y)
"""


"""
#  用for循环实现1~100求和  用for循环实现1~100之间的偶数求和
s = 0
for i in range (101):
    s = s+i
print(s)

m = 0
for i in range (0 , 101 , 2):
    m = m + i
print(m)
"""
"""
# 猜数字游戏
import random

m = random.randint(0,101)
n = 0
while True:
    n = n+1
    num = int(input("number:"))
    if num > m:
        print("big")
    elif num < m:
        print("small")
    else:
        print("√")
        break
print('你总共猜了%s次' % n)

"""
"""
# 输出乘法口诀表(九九表)
for i in range (1,10):
    for j in range (1,i+1):
        print("%d*%d = %d" %(i,j,i*j),end = '\t')
    print()
"""
"""

# 输入一个正整数判断是不是素数。
# 素数一般指质数。质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。
number = int (input('请输入一个正整数:'))
if number > 2:
    for x in range (2,number+1):
        if number % x == 0:
            break
    if x == number:
        print (number,'是素数')
    else:
        print (number,'不是素数')
else:
    print('?请输入正整数???还要大于2?')
"""

# 输入两个正整数，计算它们的最大公约数和最小公倍数。
# 两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。
"""


# 打印如下所示的三角形图案。
for i in range (5):
    for j in range(i+1):
        print('*',end = '\t')
    print()
"""

"""
for i in range(5):
    for j in range(5):
        if j < 5 - i - 1:
            print(' ', end='')
        if j > 4-i:
            print('*', end='')
    print()

"""
"""
# 水仙花数
for num in range(100, 1000):
    bai = num // 100
    shi = num // 100 % 10
    ge = num % 10
    if num == bai ** 3 + shi ** 3 + ge ** 3:
        print(num)
"""















































































