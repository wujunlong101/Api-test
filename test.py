# /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import json
from Api.common import *
from Api.HttpApi import *
from Api.LicesenCommon import *
class Testcreate(unittest.TestCase):
    def setUp(self):
        self.change = CommonMethod()
        self.http = HttpApi()
        self.liceseMethod = LicesenMethod()
        self.licesenUrl = "http://47.92.88.246:8999/"
        self.headers = {'content-type': 'application/json'}
        self.changeDate = {}
        # self.changeDate["liceseID"] = None
     # 新增正确d
    def testCreateAdd(self):
        self.changeDate["ID"] = "500"
        self.changeDate["userId"] = "500"
        url = self.licesenUrl+'it-license/it/license/create'
        fp = open("data/create.json")
        data = json.load(fp)
        newData = self.change.changeDate(data,self.changeDate)
        res = self.http.send_post(url, newData)
        print res['result']
        # self.assertEqual(res['errMessage'], "success", u'添加lincesen成功')
        #企业id为空
    # def testAddisNull(self):
    #     url = self.licesenUrl + 'it-license/it/license/create'
    #     fp = open("../data/create.json")
    #     data1 = json.load(fp)
    #     self.changeDate["ID"] = ""
    #     self.changeDate["usersId"] = self.userId
    #     data=change.changeDate(json.dumps(data1),self.changeDate)
    #     res= http.send_post(url, data)
    #    # print(res)
    #     self.assertEqual(res['errMessage'], "success",'测试失败')
    # #userId为空测试
    # def testAddUserIsNull(self):
    #     url = self.licesenUrl + 'it-license/it/license/create'
    #     fp = open("../data/create.json")
    #     data1 = json.load(fp)
    #     self.changeDate["ID"]=self.id
    #     self.changeDate["usersId"]=''
    #     data=change.changeDate(json.dumps(data1),self.changeDate)
    #     res = http.send_post(url, data)
    #     # print(res)
    #     self.assertEqual(res['errCode'], 301140002, '测试失败')
    # 正常查询
    # def testselect(self):
    #     url = self.licesenUrl + 'it-license/it/license/product/version'
    #     fp = open("../data/select.json")
    #     data1 = json.load(fp)
    #     self.changeDate["ID"] = self.id
    #     self.changeDate["usersId"] = self.userId
    #     data = change.changeDate(json.dumps(data1), self.changeDate)
    #     res = http.send_post(url, data)
    #     print json.dumps(res).decode("unicode-escape")
    #     self.tenantId = res['result']
    #     self.assertEqual(res['errMessage'], "success", '查询信息成功')
    #  id为空查询
    # def testselectidnull(self):
    #     url = self.licesenUrl + 'it-license/it/license/product/version'
    #     fp = open("../data/select.json")
    #     data1 = json.load(fp)
    #     self.changeDate["ID"] = ""
    #     self.changeDate["usersId"] = self.userId
    #     data = change.changeDate(json.dumps(data1), self.changeDate)
    #     res = http.send_post(url, data)
    #     print json.dumps(res).decode("unicode-escape")
    #     #self.tenantId = res['result']
    #     self.assertEqual(res['errMessage'], "invalid para：tenantId is null", '查询信息失败')
    # def testunpdate(self):
    #     url = self.licesenUrl + 'it-license/it/license/update'
    #     fp = open("data/update.json")
    #     data1 = json.load(fp)
    #     self.changeDate["ID"] = self.id
    #     self.changeDate["usersId"] = self.userId
    #     data = self.change.changeDate(json.dumps(data1), self.changeDate)
    #     res = self.http.send_post(url, data)
    #     return json.dumps(res).decode("unicode-escape")
    #     #self.tenantId = res['result']
    #     #self.assertEqual(res['errMessage'], "invalid para：tenantId is null", '查询信息失败')
    # def testdelete(self):
    #     url = self.licesenUrl + 'it-license/it/license/delete'
    #     fp = open("data/delete.json")
    #     data1 = json.load(fp)
    #     self.changeDate["ID"] = self.id
    #     self.changeDate["usersId"] = self.userId
    #     data = self.change.changeDate(json.dumps(data1), self.changeDate)
    #     res = self.http.send_post(url, data)
    #     print json.dumps(res).decode("unicode-escape")
    #     self.tenantId = res['result']
    #     self.assertEqual(res['errCode'], "301140003")
    # def tearDown(self):
    #     print(self.liceseID)
        #liceseMethod.deleteLicesen(self.id, self.userId, self.liceseID)

# if __name__ == '__main__':
#     unittest.main()
#     abc=unittest.TestSuite()
#     abc.addTest(Testcreate('testCreateAdd'))
#     abc.addTest(Testcreate('testAddisNull'))
#     abc.addTest(Testcreate('testAddUserIsNull'))
#     abc.addTest(Testcreate('testselect'))
#     abc.addTest(Testcreate('testselectidnull'))
#     abc.addTest(Testcreate('testunpdate'))
#     abc.addTest(Testcreate('testdelete'))
#     runner = unittest.TextTestRunner()
#     runner.run(abc)