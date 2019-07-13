# -*-coding:utf-8-*-
import json
from configs.config_errorcode import selectStaff_error
from dal.dal_staff import Dal_Staff
from handlers.BaseHandler import BaseHandler


# 获取所有职员
class SelectAllStaffHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("selectAllStaff.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        staff = Dal_Staff().selectAllStaff(1 if (int(post_data["page"]) <= 0) else post_data["page"])
        respon = {'errorCode': selectStaff_error['success'], 'staff': staff}
        respon_json = json.dumps(respon)
        self.write(respon_json)