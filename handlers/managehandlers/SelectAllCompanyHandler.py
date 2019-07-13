# -*-coding:utf-8-*-
import json
from configs.config_errorcode import selectCompany_error
from dal.dal_company import Dal_Company
from handlers.BaseHandler import BaseHandler


# 获取所有公司——分页
class SelectAllCompanyHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("selectAllCompany.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        company = Dal_Company().selectAllCompany(1 if (int(post_data["page"]) <= 0) else post_data["page"])
        respon = {'errorCode': selectCompany_error['success'], 'company': company}
        respon_json = json.dumps(respon)
        self.write(respon_json)
