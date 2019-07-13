# -*-coding:utf-8-*-
import json
from handlers.BaseHandler import BaseHandler
from configs.config_errorcode import userLogin_error
from dal.dal_user import Dal_user


##用户登陆
class AppLoginHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("userLogin.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
            user=Dal_user().selectUser(post_data["id"])
        if (user== False):
            respon = {"errorCode": userLogin_error['userInvaild']}
        elif(user['password']!=post_data["password"]):
            respon = {"errorCode": userLogin_error['wrong_password']}
        else:
            respon = {"errorCode": userLogin_error['success']}
        ##ensure_ascii=False  解决json打包中文时出现乱码问题
        respon_json = json.dumps(respon, ensure_ascii=False)
        self.write(respon_json)
