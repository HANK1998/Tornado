# -*-coding:utf-8-*-
import json

from configs.config_errorcode import deleteLogistics_error
from dal.dal_logistics import Dal_Logistics
from handlers.BaseHandler import BaseHandler


# 删除物流信息
class DeleteLogisticsHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("deleteLogistics.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        if (Dal_Logistics().deleteLogistics(post_data['id']) == False):
            respon = {'errorCode': deleteLogistics_error['logisticsInvaild']}
        else:
            respon = {'errorCode': deleteLogistics_error['success']}
        respon_json = json.dumps(respon)
        self.write(respon_json)
