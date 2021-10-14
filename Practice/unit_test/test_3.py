# coding=utf-8

import unittest
class TestCase_1(unittest.TestCase):
    def test_1(self):
        print("111")
    def test_2(self):
        print("111_1")
class TestCase_2(unittest.TestCase):
    def test_1(self):
        print("222")
    def test_2(self):
        print("222_2")
if __name__ == '__main__':
    suit_1 = unittest.TestLoader().loadTestsFromTestCase(TestCase_1)
    suit_2 = unittest.TestLoader().loadTestsFromTestCase(TestCase_2)
    suit = unittest.TestSuite([suit_1, suit_2])
    unittest.TextTestRunner(verbosity=2).run(suit)
