import unittest
import math
import re
class demoTest(unittest.TestCase):
    def test_1(self):  # 基本断言
        self.assertEqual(4+4, 8)
        self.assertNotEqual(2, 3)  # a == b

        self.assertTrue(3+2 == 5, "true")
        self.assertNotEqual(3+2 == 20 , "assertion fails")  # bool(x) is true

        self.assertIn( "百度", self.driver.title)
        self.assertNotIn(3, [1,2])   #  in \ not in 区间

    def test_2(self):  # 比较断言
        self.assertAlmostEqual(22/7,3.142857143,places = 7) # 验证first约等于second。 palces: 指定精确到小数点后多少位，默认为7
        self.assertNotAlmostEqual(10/3,3,places = 7)
        self.assertGreater(math.pi,3) # 　验证first > second，否则fail
        self.assertGreaterEqual (first, second, msg = None) # 验证first ≥ second，否则fail
        self.assertLess (first, second, msg = None) # 验证first < second，否则fail
        self.assertLessEqual (first, second, msg = None)# 验证first ≤ second，否则fail
        self.assertRegexpMatches (text, regexp, msg = None)# 　验证正则表达式regexp搜索匹配的文本text。 regexp：通常使用re.search()
        self.assertNotRegexpMatches (text, regexp, msg = None) # 验证正则表达式regexp搜索不匹配的文本text。 regexp：通常使用re.search()
    def test_3(self):  # 复杂断言
        self.assertListEqual(list1,list2, msg = None) #验证list1 = list2 不等则fail报错
        self.assertTupleEqual(toupe1,toupe2,msg=None) #验证tuple1 = toupe2 不等则fail报错
        self.assertSetEqual(set1,set2,msg=None) #验证set1 = set2 不等则fail报错
        self.assertDictEqual(zd1,zd2, msg=None) #验证字典1 = 字典2 不等则fail报错

if __name__ == '__main__':
    unittest.main()


