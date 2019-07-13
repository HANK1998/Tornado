# -*-coding:utf-8-*-
import json
from configs.config_errorcode import selectManifest_error
from dal.dal_manifest import Dal_Manifest
from handlers.BaseHandler import BaseHandler
from dal.dal_staff import Dal_Staff


# 获取所有订单信息
class SelectAllManifestHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("selectAllManifest.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
            Manifest = Dal_Manifest().selectAllManifest(1 if (int(post_data["page"]) <= 0) else post_data["page"])
        respon = {'errorCode': selectManifest_error['success'], 'Manifest': Manifest}
        respon_json = json.dumps(respon)
        self.write(respon_json)

#公司查找自己所有发送的订单信息
class SelectAllManifestByCHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("selectAllManifestBc.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        cid = post_data['cid']
        res = Dal_Staff().selectStaffByCid(cid)
        result = {}
        i = 0

        for value in res.values():
            result[i] = Dal_Manifest().selectManifestBySID(value['id'])
            i += 1
        if self.sortArr(result) != '':
            result = {"errorCode": 0, "res": self.sortArr(result)}
        else:
            result = {"errorCode": 1}
        self.write(json.dumps(result))

    def sortArr(self,res):
        data = {}
        a = 0
        for value in res.values():
            for j in value.values():
                if j != '':
                    data[a] = j
                    a += 1
        return data

# 公司查找自己所有发送的订单信息
class SelectAllManifestByPHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("selectAllManifestBc.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        cid = int(post_data['cid'])
        c_list = Dal_Manifest().selectManifestByCId(cid)
        if self.sortArr(c_list) != '':
            result = {"errorCode": 0, "res": self.sortArr(c_list)}
        else:
            result = {"errorCode": 1}
        self.write(json.dumps(result))

    def sortArr(self,res):
        data = {}
        a = 0
        for j in res.values():
            if j != '':
                data[a] = j
                a += 1
        return data