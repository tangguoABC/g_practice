import time
# 时间戳   是从公元1970 年到现在所经历的秒数
print(time.time())
time.sleep(1)

 #打印出来的默认的是当前时间 tm_wday(星期，从0开始，取得是索引值)
#                          #tm_yday (今天是今年的第几天)  tm_isday (是否为夏令时)
print(time.localtime())
#括号里边可以些时间戳 ，打印的是时间戳的时间。
print(time.localtime(0))
#将时间格式化为标准时间，默认格式化标注时间
print(time.strftime('%Y %m %d %H-%M-%S %w %j'))

#将时间转换为时间戳。
print(time.mktime((2018,12,3,12,0,0,0,0,0)))



# 将时间元组转换为字符串
print(time.asctime())
print(time.asctime((2019, 1, 1, 9, 23, 30, 1, 1, 0)))

# 将纪元以来的时间(以秒为单位)转换为本地时间中的字符串
print(time.ctime())
print(time.clock())

"""
#输入一个日期（年月日）要求输出本日期的前一天。
"""
x = input("???").split(",")
m = time.mktime((int(x[0]),int(x[1]),int(x[2]),0,0,0,0,0,0))
n = time.localtime(m-86400)
print(time.strftime('%Y %m %d %H-%M-%S %w %j',n))

n = int(input('year'))
y=int(input('month'))
r=int(input('day'))
a = time.mktime((n,y,r,0,0,0,0,0,0))
b = time.localtime(a-86400)
print(time.strftime('%Y,%m,%d',b))








