# -*-coding:utf-8-*-
import json
from configs.config_errorcode import selectWarehouse_error
from dal.dal_warehouse import Dal_Warehouse
from handlers.BaseHandler import BaseHandler
from dal.dal_company import Dal_Company


# 获取所有库存信息
class SelectAllWarehouseHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("page/selectAllWarehouse.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        c_id = post_data['id']
        comp = Dal_Company().selectCompany(c_id)
        type = str(comp['type'])
        if type == 'warehouse':
            w_res = Dal_Warehouse().getAllProdWa(c_id)
        elif type == 'manifest':
            w_res = Dal_Warehouse().getAllProdMa(c_id)
        else:
            w_res = Dal_Warehouse().getAllProdWa(c_id)

        data = {"errorcode":0,'result':w_res}
        data = json.dumps(data)
        self.write(data)