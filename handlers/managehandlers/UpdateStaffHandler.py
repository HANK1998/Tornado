# -*-coding:utf-8-*-
import json

from configs.config_errorcode import updateStaff_error
from dal.dal_staff import Dal_Staff
from handlers.BaseHandler import BaseHandler
from tools.utils import Utils


# 修改职员信息/离职
class UpdateStaffHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("updateStaff.html")

    def post(self, *args, **kwargs):
        post_data = {}
        new = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        if (Dal_Staff().selectStaff(post_data['id']) == None):
            respon = {'errorCode': updateStaff_error['staffInvaild']}
        else:
            if post_data.has_key('name') != False and post_data['name']!='':
                new['name'] = post_data['name']
            if post_data.has_key('password') != False and post_data['password']!='':
                new['password'] = post_data['password']
            if post_data.has_key('type') != False and post_data['type']!='':
                new['type'] = post_data['type']
            if post_data.has_key('leaveTime') != False and post_data['leaveTime']!='':
                new['leaveTime'] = str(Utils().dbTimeCreate())
            if post_data.has_key('tel') != False and post_data['tel']!='':
                new['tel'] = post_data['tel']
            if post_data.has_key('photo') == False:
                Dal_Staff().updatePhoto(post_data['id'], self.request.files["photo"])

            if (Dal_Staff().updateStaff(post_data["id"], **new) == 1):
                respon = {'errorCode': updateStaff_error['success']}
            else:
                respon = {'errorCode': updateStaff_error['failed']}
        respon_json = json.dumps(respon)
        self.write(respon_json)
