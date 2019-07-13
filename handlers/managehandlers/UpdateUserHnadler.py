# -*-coding:utf-8-*-
import json

from configs.config_errorcode import updateUser_error
from dal.dal_user import Dal_user
from handlers.BaseHandler import BaseHandler


class UpdateUserHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("updateUser.html")

    def post(self, *args, **kwargs):
        post_data = {}
        new={}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        if(Dal_user().selectUser(post_data['id'])==None):
            respon = {'errorCode': updateUser_error['userInvaild']}
        else:
            if post_data.has_key('name') != False and post_data['name']!='':
                new['name'] = post_data['name']
            if post_data.has_key('password') != False and post_data['password']!='':
                new['password'] = post_data['password']
            if post_data.has_key('tel') != False and post_data['tel']!='':
                new['tel'] = post_data['tel']
            if(Dal_user().updateUser(post_data["id"],**new)==1):
                respon={'errorCode':updateUser_error['success']}
            else:
                respon={'errorCode':updateUser_error['failed']}
        respon_json = json.dumps(respon)
        self.write(respon_json)