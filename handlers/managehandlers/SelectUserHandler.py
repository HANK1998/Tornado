# -*-coding:utf-8-*-
import json
from configs.config_errorcode import selectUser_error
from dal.dal_user import Dal_user
from handlers.BaseHandler import BaseHandler

class SelectUserHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("selectUser.html")
    def post(self,*args,**kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        user=Dal_user().selectUser(post_data["id"])
        if user==None:
            respon={'errorCode':selectUser_error['userInvaild']}
        else:
            respon={'errorCode':selectUser_error['success'],'user':user}
        respon_json=json.dumps(respon)
        self.write(respon_json)