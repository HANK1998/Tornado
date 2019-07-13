# -*-coding:utf-8-*-
import json
from dal.dal_warehouse import Dal_Warehouse
from handlers.BaseHandler import BaseHandler
from model.warehouse import Warehouse
from configs.config_errorcode import addWarehouse_error

# 添加新仓储信息
from tools.utils import Utils


class AddWarehouseHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("addWarehouse.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        if (Dal_Warehouse().selectWarehouseByC(post_data['code'],post_data['shelvesId']) != None):
            respon = {'errorCode': addWarehouse_error['warehouseExist']}
        else:
            # shelves=Dal_Shelves().selectShelves(post_data['shelvesId'])
            if(shelves==None):
                respon={'errorCode':addWarehouse_error['shelvesInvaild']}
            else:
                nowtime = Utils().dbTimeCreate()
                newWarehouse = Warehouse(id=None, code=post_data['code'], inTime=str(nowtime),
                                         shelvesId=post_data['shelvesId'])
                id = Dal_Warehouse().addWarehouse(newWarehouse)
                if id == False:
                    respon = {'errorCode': addWarehouse_error['failed']}
                else:
                    respon = {'errorCode': addWarehouse_error['success'], 'id': id}
        respon_json = json.dumps(respon)
        self.write(respon_json)
