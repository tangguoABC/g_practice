# coding=utf-8
import unittest

class Mytest(unittest.TestCase): #继承自unittest.TestCase
    @classmethod
    def setUpClass(cls):
        print('所有测试前执行一次---111')
    @classmethod
    def tearDownClass(cls):
        print('所有测试后执行一次---222')

    def setUp(self):
        print("每个测试用例执行前执行一次---aaa")
    def tearDown(self):
        print("每个测试用例执行后执行一次---bbb")

    def test_a(self):
        self.assertEqual(1,1)
        print('1相等1')
    def test_b(self):
        self.assertEqual(2,2)
        print('2相等2')
if __name__ == '__main__':
    unittest.main()

