# -*-coding:utf-8-*-
import json
from configs.config_errorcode import selectWarehouse_error
from dal.dal_warehouse import Dal_Warehouse
from handlers.BaseHandler import BaseHandler

class SelectWarehouseHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("selectWarehouse.html")
    def post(self,*args,**kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        warehouse=Dal_Warehouse().selectWarehouse(post_data["id"])
        if warehouse==None:
            respon={'errorCode':selectWarehouse_error['warehouseInvaild']}
        else:
            respon={'errorCode':selectWarehouse_error['success'],'warehouse':warehouse}
        respon_json=json.dumps(respon)
        self.write(respon_json)