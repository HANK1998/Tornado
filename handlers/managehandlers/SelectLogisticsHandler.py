# -*-coding:utf-8-*-
import json
from configs.config_errorcode import selectLogistics_error
from dal.dal_logistics import Dal_Logistics
from handlers.BaseHandler import BaseHandler

class SelectLogisticsHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("selectLogistics.html")
    def post(self,*args,**kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        logistics=Dal_Logistics().selectLogistics(post_data["companyId"])
        if logistics==None:
            respon={'errorCode':selectLogistics_error['logisticsInvaild']}
        else:
            respon={'errorCode':selectLogistics_error['success'],'logistics':logistics}
        respon_json=json.dumps(respon)
        self.write(respon_json)

class SelectAllMyLogGHandlers(BaseHandler):
    def get(self):
        self.render("page/selectAllMyLogG.html")

    def post(self):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        logistics = Dal_Logistics().selectMyLogG(post_data["id"])
        if logistics==None:
            respon={'errorCode':selectLogistics_error['logisticsInvaild']}
        else:
            respon={'errorCode':selectLogistics_error['success'],'result':logistics}
        respon_json=json.dumps(respon)
        self.write(respon_json)

class SelectAllMyLogPHandlers(BaseHandler):
    def get(self):
        self.render("page/selectAllMyLogP.html")

    def post(self):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        logistics = Dal_Logistics().selectMyLogP(post_data["id"])
        if logistics==None:
            respon={'errorCode':selectLogistics_error['logisticsInvaild']}
        else:
            respon={'errorCode':selectLogistics_error['success'],'result':logistics}
        respon_json=json.dumps(respon)
        self.write(respon_json)
