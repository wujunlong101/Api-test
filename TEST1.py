# coding:utf-8
import unittest
import HTMLTestRunner
import HTML
if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(HTML.CreateTest("test_delok"))
    suit.addTest(HTML.CreateTest("test_delok01"))
    file = open("D:\\diyige.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(file, title=u"接口测试", description=u"测试报告")
    runner.run(suit)
    file.close()