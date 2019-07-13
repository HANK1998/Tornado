# -*-coding:utf-8-*-
import json

from configs.config_errorcode import deleteStaff_error
from dal.dal_staff import Dal_Staff
from handlers.BaseHandler import BaseHandler


# 删除职员信息
class DeleteStaffHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("deleteStaff.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        if (Dal_Staff().deleteStaff(post_data['id']) == False):
            respon = {'errorCode': deleteStaff_error['staffInvaild']}
        else:
            respon = {'errorCode': deleteStaff_error['success']}
        respon_json = json.dumps(respon)
        self.write(respon_json)
