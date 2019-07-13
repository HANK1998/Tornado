# -*-coding:utf-8-*-
import json

from configs.config_errorcode import deleteCompany_error
from dal.dal_company import Dal_Company
from handlers.BaseHandler import BaseHandler


# 删除公司信息
class DeleteCompanyHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("deleteCompany.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        if (Dal_Company().deleteCompany(post_data['id']) == False):
            respon = {'errorCode': deleteCompany_error['companyInvaild']}
        else:
            respon = {'errorCode': deleteCompany_error['success']}
        respon_json = json.dumps(respon)
        self.write(respon_json)
