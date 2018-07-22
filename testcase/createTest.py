# -*- coding:utf-8 -*-
import unittest
import json
from Api.common import CommonMethod
from Api.HttpApi import *
from Api.LicesenCommon import *
change = CommonMethod()
http=HttpApi()
liceseMethod=LicesenMethod()
class createTest(unittest.TestCase):
    def setUp(self):
        self.url='http://47.92.88.246:8999/it-license/it/license/create'
        createFile = open("..\data\create.json")
        self.jsonData = json.load(createFile)
        self.changeDate = {}
        self.id = '500'
        self.userId = '500'
        self.liceseID=None
    #正常添加
    def testAddLicesen(self):
        self.changeDate["ID"]=self.id
        self.changeDate["usersId"]=self.userId
        data=change.changeDate(json.dumps(self.jsonData),self.changeDate)
        res= http.send_post(self.url,data)
        #print(res)
        self.liceseID = res['result']
        self.assertEqual(res['errMessage'],"success1",'添加lincesen失败')

    # #企业id为空
    # def testAddisNull(self):
    #
    #     self.changeDate["ID"]=''
    #     self.changeDate["usersId"]=self.userId
    #     data=change.changeDate(json.dumps(self.jsonData),self.changeDate)
    #     res= http.send_post(self.url,data)
    #    # print(res)
    #     self.assertEqual(res['errCode'],301140002,'测试失败')
    # #userId为空测试
    # def testAddUserIsNull(self):
    #     self.changeDate["ID"]=self.id
    #     self.changeDate["usersId"]=''
    #     data=change.changeDate(json.dumps(self.jsonData),self.changeDate)
    #     res = http.send_post(self.url, data)
    #     #print(res)
    #     self.assertEqual(res['errCode'], 301140002, '测试失败')
    def tearDown(self):
        print(self.liceseID)
        liceseMethod.deleteLicesen(self.id,self.userId,self.liceseID)
if __name__ == '__main__':
    unittest.main