# coding=utf-8
# Testsuit()  测试套件

import unittest
class UCTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        pass
    def test_2(self):
        print('hello')
if __name__ == "__main__":
    suit = unittest.TestSuite()   # 创建一个测试套件测试集
    suit.addTest(UCTestCase("test_1"))  # 把需要执行测测试用例放在测试套件中
    suit.addTest(UCTestCase("test_2"))  # 把需要执行测测试用例放在测试套件中
#    suit.addTest([UCTestCase("test_1"), UCTestCase("test_2")])  # 添加多条测试用例

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suit)




