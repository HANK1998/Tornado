# -*-coding:utf-8-*-
import json

from configs.config_errorcode import deleteWarehouse_error
from dal.dal_warehouse import Dal_Warehouse
from handlers.BaseHandler import BaseHandler


# 删除仓储信息
class DeleteWarehouseHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("deleteWarehouse.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        if (Dal_Warehouse().deleteWarehouse(post_data['id']) == False):
            respon = {'errorCode': deleteWarehouse_error['warehouseInvaild']}
        else:
            respon = {'errorCode': deleteWarehouse_error['success']}
        respon_json = json.dumps(respon)
        self.write(respon_json)
