# coding:utf-8
import requests
import unittest
import HTMLTestRunner
import json


class Workflow(unittest.TestCase):

    def setUp(self):
        self.url="http://192.168.0.2:8080/paas/crm/associate/object"

    def test01(self):
        # url ="http://192.168.0.2:8080/paas/crm/associate/object"
        data ={"context": {"appId": "CRM", "tenantId": "71584", "userId": "1000"}, "enable": True, "type": "workflow"}
        re = requests.post(self.url,json=data)
        res = re.json()
        self.assertEqual(res["errCode"],200)

    def test02(self):
        # url = "http://192.168.0.2:8080/paas/crm/associate/object"
        data ={"context": {"appId": "CRM", "tenantId": "71584", "userId": "1000"}, "enable": True, "type": "approvalflow"}
        re = requests.post(self.url, json=data)
        print re.text

    def test03(self):
        # url ="http://192.168.0.2:8080/paas/crm/associate/object"
        data = {"context": {"appId": "CRM", "tenantId": "71584", "userId": "1000"}, "enable": True, "type": "workflow_bpm"}
        re = requests.post(self.url,json=data)
        print re.text

    def test04(self):
        # url = "http://192.168.0.2:8080/paas/crm/associate/object"
        data = {"context": {"appId": "CRM", "tenantId": "71584", "userId": "1000"}, "enable": True, "type": "null"}
        re = requests.post(self.url,json=data)
        print re.text

    def test05(self):
        # url = "http://192.168.0.2:8080/paas/crm/associate/object"
        data = {"context": {"appId": "CRM", "tenantId": "71584", "userId": "1000"}, "enable": True, "type": ""}
        re = requests.post(self.url,jsom=data)
        print re.text

    def test06(self):
        # url = "http://192.168.0.2:8080/paas/crm/associate/object"
        data = {"context": {"appId": "CRM", "tenantId": "71584", "userId": "1000"}, "enable": True, "type": "bpm"}
        re = requests.post(self.url,json=data)
        print re.text

    def test07(self):
        # url = "http://192.168.0.2:8080/paas/crm/associate/object"
        data = {"context": {"appId": "CRM", "tenantId": "71584", "userId": "1000"}, "enable": True, "type": "approvalflow"}
        re = requests.post(self.url,json=data)
        print re

    def test08(self):
        # url = "http://192.168.0.2:8080/paas/crm/associate/object"
        data = {"context": {"appId": "CRM", "tenantId": "71584", "userId": "1000"}, "enable":False, "type": "approvalflow"}
        re = requests.post(self.url,json=data)
        print re.text

    def test09(self):
        # url = "http://192.168.0.2:8080/paas/crm/associate/object"
        data ={"context": {"appId": "CRM", "tenantId": "71584", "userId": "1000"}, "enable": True, "type": "approvalflow"}
        re = requests.post(self.url,json=data)
        print re.text
    def tearDown(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Workflow("test01"))
    suite.addTest(Workflow("test02"))
    suite.addTest(Workflow("test03"))
    suite.addTest(Workflow("test04"))
    suite.addTest(Workflow("test05"))
    suite.addTest(Workflow("test06"))
    suite.addTest(Workflow("test07"))
    suite.addTest(Workflow("test08"))
    fp = open("D:\\wode.html","wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告",description=u"用例测试情况")
    runner.run(suite)
    fp.close()