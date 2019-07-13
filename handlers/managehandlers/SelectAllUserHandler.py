# -*-coding:utf-8-*-
import json
from configs.config_errorcode import selectUser_error
from dal.dal_user import Dal_user
from handlers.BaseHandler import BaseHandler


# 获取所有普通用户
class SelectAllUserHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("selectAllUser.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        user = Dal_user().selectAllUser(1 if (int(post_data["page"]) <= 0) else post_data["page"])
        respon = {'errorCode': selectUser_error['success'], 'user': user}
        respon_json = json.dumps(respon)
        self.write(respon_json)
