# -*- coding:utf-8 -*-
import unittest
class testDemo(unittest.TestCase):
    def setUp(self):
        print("setUp")
    def test001(self):
        print("第一个")
    def test002(self):
        print("第二个")
    def tearDown(self):
        print("tearDown")

if __name__ == '__main__':
    unittest.main()