# -*-coding:utf-8-*-
import json

from configs.config_errorcode import updateManifest_error
from dal.dal_manifest import Dal_Manifest
from handlers.BaseHandler import BaseHandler
from dal.dal_logistics import Dal_Logistics
from dal.dal_warehouse import Dal_Warehouse
from model.warehouse import Warehouse
from dal.dal_batch import Dal_Batch
from tools.utils import Utils

class UpdateManifestHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("updateManifest.html")

    def post(self, *args, **kwargs):
        post_data = {}
        new={}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        if(Dal_Manifest().selectManifest(post_data['id'])==None):
            respon = {'errorCode': updateManifest_error['manifestInvaild']}
        else:
            if post_data.has_key('confirm') == False:
                new['confirm'] = "Y"
            if(Dal_Manifest().updateManifest(post_data["id"],**new)==1):
                respon={'errorCode':updateManifest_error['success']}
            else:
                respon={'errorCode':updateManifest_error['failed']}
        respon_json = json.dumps(respon)
        self.write(respon_json)

class UpdateLogisticsHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("page/updateLogistics.html")

    def post(self, *args, **kwargs):
        post_data = {}
        new = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        l_id = post_data['id']
        l_res = Dal_Logistics().selectLogistics(l_id)
        if (l_res == None):
            respon = {'errorCode': "1"}#未知物流
        else:
            if post_data.has_key('comfirm') == False:
                new['comfirm'] = "Y"
            if (Dal_Logistics().updateLogistics(post_data["id"], **new) == 1):
                respon = {'errorCode': updateManifest_error['success']}

                #入库操作

                pname = Dal_Batch().selectBatch(l_res['amount'])
                nowtime = Utils().dbTimeCreate()
                b_res = Dal_Batch().selectBatch(l_res['amount'])
                ware = Warehouse(
                    id=None,
                    p_name=pname['p_name'],
                    p_id=l_res['amount'],
                    inTime=str(nowtime),
                    outTime=None,
                    w_id=l_res['endPlace'],
                    in_c_id=l_res['startPlace'],
                    out_c_id=None,
                    stock=b_res['amount']
                )
                new_ware = Dal_Warehouse().addWarehouse(ware)
            else:
                respon = {'errorCode': updateManifest_error['failed']}
        respon_json = json.dumps(respon)
        self.write(respon_json)