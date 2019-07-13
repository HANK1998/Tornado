# -*-coding:utf-8-*-
import json

from configs.config_errorcode import updateWarehouse_error
from dal.dal_staff import Dal_Staff
from dal.dal_warehouse import Dal_Warehouse
from handlers.BaseHandler import BaseHandler
from tools.utils import Utils


class UpdateWarehouseHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("updateWarehouse.html")

    def post(self, *args, **kwargs):
        respon=None
        post_data = {}
        new={}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        result=Dal_Warehouse().selectWarehouseByCS(post_data['code'],post_data['shelvesId'])
        if(result==None):
            respon = {'errorCode': updateWarehouse_error['warehouseInvaild']}
        else:
            if post_data.has_key('takerId') != False and post_data['takerId']!='':
                if (Dal_Staff().selectStaff(post_data['takerId']) == None):
                    respon = {'errorCode': updateWarehouse_error['staffInvaild']}
                else:
                    new['takerId'] = post_data['takerId']
                    new['outTime']= str(Utils().dbTimeCreate())
            if post_data.has_key('newShelvesId') != False and post_data['newShelvesId']!='':
                if(Dal_Shelves().selectShelves(post_data['newShelvesId'])==None):
                    respon = {'errorCode': updateWarehouse_error['shelvesInvaild']}
                else:
                    new['shelvesId'] = post_data['newShelvesId']
            if(respon==None):
                if(Dal_Warehouse().updateWarehouse(result['id'],**new)==1):
                    respon={'errorCode':updateWarehouse_error['success']}
                else:
                    respon={'errorCode':updateWarehouse_error['failed']}
        respon_json = json.dumps(respon)
        self.write(respon_json)