# coding:utf-8
from Api.common import *
import json
import unittest
import requests
import HTMLTestRunner
class CreateTest(unittest.TestCase):

    def setUp(self):
        pass
    #
    def test_delok(self):
        url="http://47.92.88.246:8999/it-license/it/license/delete"
        data={"context": { "tenantId": "1000", "appId": "CRM","userId": "1000"}, "productLicenseIdList": [ "" ]}
        re =requests.post(url,json=data)
        res = re.json()
        self.assertEqual(res["errMessage"],"success")

    def test_delok01(self):
        url = "http://47.92.88.246:8999/it-license/it/license/delete"
        data = {"context": {"tenantId": "1000", "appId": "CRM", "userId": "1000"}, "productLicenseIdList": ["100"]}
        re = requests.post(url, json=data)
        res =re.json()
        self.assertEqual(res["errCode"], 301140003)

    def tearDown(self):
        pass

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(CreateTest("test_delok"))
    suit.addTest(CreateTest("test_delok1"))
    file = open("D:\\diyige.html","wb")
    runner = HTMLTestRunner.HTMLTestRunner(file,title=u"接口测试",description=u"测试报告")
    runner.run(suit)
    file.close()