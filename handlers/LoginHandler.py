# -*-coding:utf-8-*-
import json

from dal.dal_company import Dal_Company
from handlers.BaseHandler import BaseHandler
from configs.config_errorcode import adminLogin_error


##登陆
class LoginHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("adminLogin.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        msg=Dal_Company().selectCompanyByIP(post_data["id"], post_data["password"])
        if (msg == None):
            respon = {"errorCode": adminLogin_error['adminInvaild']}
        else:
            respon = {"errorCode": adminLogin_error['success'],"msg":msg}
        ##ensure_ascii=False  解决json打包中文时出现乱码问题
        respon_json = json.dumps(respon, ensure_ascii=False)
        self.write(respon_json)
