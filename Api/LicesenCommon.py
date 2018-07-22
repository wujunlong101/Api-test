# -*- coding:utf-8 -*-
import json
from common import *
from HttpApi import *
class LicesenMethod:
    def __init__(self):
        self.chageData = CommonMethod()
        self.http = HttpApi()
        self.headers = {'content-type': 'application/json'}
        self.licesenUrl="http://47.92.88.246:8999/"
        self.change={}
    #创建licesen
    def createLicesen(self,ID,usersId):
        self.change['ID'] = ID
        self.change['usersId'] = usersId
        url = self.licesenUrl+'it-license/it/license/create'
        fp = open("..\data\create.json")
        data = json.load(fp)
        newData = self.chageData.changeDate(json.dumps(data), self.change)
        print(newData)
        res = self.http.send_post(url, newData)
        return res['result']
    #删除lisencen
    def deleteLicesen(self,ID,usersId,DataID):
        self.change['ID'] = ID
        self.change['usersId'] = usersId
        self.change['DataID'] = DataID
        url = self.licesenUrl+'it-license/it/license/delete'
        fp = open("..\data\delete.json")
        if DataID!=None:
            data = json.load(fp)
            newData = self.chageData.changeDate(json.dumps(data), self.change)
            res = self.http.send_post(url=url, data=newData)
            print(res)