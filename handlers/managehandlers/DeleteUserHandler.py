# -*-coding:utf-8-*-
import json

from configs.config_errorcode import deleteUser_error
from dal.dal_user import Dal_user
from handlers.BaseHandler import BaseHandler


# 删除普通用户
class DeleteUserHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("deleteUser.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        if (Dal_user().deleteUser(post_data['id']) == False):
            respon = {'errorCode': deleteUser_error['userInvaild']}
        else:
            respon = {'errorCode': deleteUser_error['success']}
        respon_json = json.dumps(respon)
        self.write(respon_json)
