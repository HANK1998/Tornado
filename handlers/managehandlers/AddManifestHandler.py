# -*-coding:utf-8-*-
import json
from dal.dal_manifest import Dal_Manifest
from handlers.BaseHandler import BaseHandler
from model.manifest import Manifest
from configs.config_errorcode import addManifest_error
from dal.dal_staff import Dal_Staff
from dal.dal_company import Dal_Company

from tools.utils import Utils


# 添加订单信息
class AddManifestHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("addManifest.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        staff_id = Dal_Staff().selectStaffByCName(post_data['cg_name'],post_data['cid'])
        place_id = Dal_Company().selectCompanyByNID(post_data['place'])

        if staff_id != None and place_id != None:
            nowtime = Utils().dbTimeCreate()
            newManifest = Manifest(id=None, time=str(nowtime),
                            originatorId=staff_id['id'],
                            amount=post_data['amount'],
                            place=place_id,
                            confirm='N',
                            prod_name=post_data['prod_name'])
            id = Dal_Manifest().addManifest(newManifest)
            if id == False:
                respon = {'errorCode': addManifest_error['failed']}
            else:
                respon = {'errorCode': addManifest_error['success'], 'id': id}
        else:
            respon = {'errorCode': addManifest_error['staffInvaild']}
        respon_json = json.dumps(respon)
        self.write(respon_json)
