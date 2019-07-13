# -*-coding:utf-8-*-
import json
from handlers.BaseHandler import BaseHandler
from model.company import Company
from tools.utils import Utils
from dal.dal_company import Dal_Company
from configs.config_errorcode import addCompany_error


# 添加新公司
class AddCompanyHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("addCompany.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        if (Dal_Company().selectCompanyByN(post_data['name']) != None):
            respon = {'errorCode': addCompany_error['companyExist']}
        else:

            ##图片上传
            blPath = Dal_Company().addPhoto(self.request.files["blPhoto"], "b")
            pcPath = Dal_Company().addPhoto(self.request.files["pcPhoto"], "P")
            scPath = Dal_Company().addPhoto(self.request.files["scPhoto"], "s")

            nowtime = Utils().dbTimeCreate()
            newCompany = Company(id=None, companyName=post_data['name'], address=post_data['address'],
                                 profile=post_data['profile'], blPath=blPath, pcPath=pcPath,
                                 scPath=scPath, tel=post_data['tel'], rTime=str(nowtime))
            id = Dal_Company().addCompany(newCompany)
            if id == False:
                respon = {'errorCode': addCompany_error['failed']}
            else:
                respon = {'errorCode': addCompany_error['success'], 'id': id}
        respon_json = json.dumps(respon)
        self.write(respon_json)
