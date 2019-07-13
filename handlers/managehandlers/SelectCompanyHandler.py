# -*-coding:utf-8-*-
import json
from configs.config_errorcode import selectCompany_error
from dal.dal_company import Dal_Company
from handlers.BaseHandler import BaseHandler

class SelectCompanyHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("selectCompany.html")
    def post(self,*args,**kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        company=Dal_Company().selectCompany(post_data["id"])
        if company==None:
            respon={'errorCode':selectCompany_error['companyInvaild']}
        else:
            respon={'errorCode':selectCompany_error['success'],'company':company}
        respon_json=json.dumps(respon)
        self.write(respon_json)