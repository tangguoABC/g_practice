# def split(self, sep=None, maxsplit=-1):  # real signature unknown; restored from __doc__
#     """
#     S.split(sep=None, maxsplit=-1) -> list of strings
#
#     Return a list of the words in S, using sep as the
#     delimiter string.  If maxsplit is given, at most maxsplit
#     splits are done. If sep is not specified or is None, any
#     whitespace string is a separator and empty strings are
#     removed from the result.
#     """
#     return []

a = '1234567890'

b, c = a.split('5')
print(b)
print(c)

"""
字符串切割操作 变成列表 查询百度 selenium 有多少个结果
"""
import time
from selenium import webdriver

class GetString(object):
    def get_search_result(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.baidu.com")
        driver.find_element_by_id('kw').send_keys('selenium')
        driver.find_element_by_id('su').click()
        time.sleep(5)
        a = driver.find_element_by_xpath("//*[@class='nums_text']").text
        m = a.split("约")[1]  # 第一次切割得到 xxxx个，[1]代表切割右边部分
        n = m.split("个")[0]   # 第二次切割，得到我们想要的数字 [0]代表切割参照参数的左边部分
        print(n)
getstring = GetString()
getstring.get_search_result()
















