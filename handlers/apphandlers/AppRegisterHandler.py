# -*-coding:utf-8-*-
import json
from handlers.BaseHandler import BaseHandler
from model.user import User
from tools.utils import Utils
from dal.dal_user import Dal_user
from configs.config_errorcode import userRegister_error

class AppRegisterHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("appRegister.html")

    def post(self, *args, **kwargs):
        post_data={}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        if(Dal_user().selectUserByNP(post_data['name'],post_data['password'])==True):
            respon={'errorCode':userRegister_error['userExist']}
        else:
            nowtime=Utils().dbTimeCreate()
            newUser = User(id=None, name=post_data['name'], password=post_data['password'],tel=post_data['tel'],registerTime=str(nowtime))
            id=Dal_user().addUser(newUser)
            if id == False:
                respon = {'errorCode': userRegister_error['failed']}
            else:
                respon = {'errorCode': userRegister_error['success'], 'id': id}
        respon_json=json.dumps(respon)
        self.write(respon_json)