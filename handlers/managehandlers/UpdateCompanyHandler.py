# -*-coding:utf-8-*-
import json

from configs.config_errorcode import updateCompany_error
from dal.dal_company import Dal_Company
from handlers.BaseHandler import BaseHandler


# 修改公司信息
class UpdateCompanyHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("updateCompany.html")

    def post(self, *args, **kwargs):
        post_data = {}
        new = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        if (Dal_Company().selectCompany(post_data['id']) == None):
            respon = {'errorCode': updateCompany_error['companyInvaild']}
        else:
            if post_data.has_key('name') != False and post_data['name']!='':
                new['name'] = post_data['name']
            if post_data.has_key('address') != False and post_data['address']!='':
                new['address'] = post_data['address']
            if post_data.has_key('profile') != False and post_data['profile']!='':
                new['profile'] = post_data['profile']
            if post_data.has_key('tel') != False and post_data['tel']!='':
                new['tel'] = post_data['tel']
            if post_data.has_key('blPhoto') == False:
                Dal_Company().updatePhoto(post_data['id'], self.request.files["blPhoto"], "b")
            if post_data.has_key('pcPhoto') == False:
                Dal_Company().updatePhoto(post_data['id'], self.request.files["pcPhoto"], "P")
            if post_data.has_key('scPhoto') == False:
                Dal_Company().updatePhoto(post_data['id'], self.request.files["scPhoto"], "s")

            if (Dal_Company().updateCompany(post_data["id"], **new) == 1):
                respon = {'errorCode': updateCompany_error['success']}
            else:
                respon = {'errorCode': updateCompany_error['failed']}
        respon_json = json.dumps(respon)
        self.write(respon_json)
