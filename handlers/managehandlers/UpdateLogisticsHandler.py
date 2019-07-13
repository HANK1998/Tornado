# -*-coding:utf-8-*-
import json

from configs.config_errorcode import updateLogistics_error
from dal.dal_logistics import Dal_Logistics
from dal.dal_staff import Dal_Staff
from handlers.BaseHandler import BaseHandler


# 修改物流信息
class UpdateLogisticsHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("updateLogistics.html")

    def post(self, *args, **kwargs):
        post_data = {}
        new = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        if (Dal_Logistics().selectLogistics(post_data['id']) == None):
            respon = {'errorCode': updateLogistics_error['LogisticsInvaild']}
        else:
            staff=Dal_Staff().selectStaff(post_data['receiverId'])
            if(staff==None):
                respon = {'errorCode': updateLogistics_error['receiverInvaild']}
            else:
                if(staff['type']!='司机'):
                    respon = {'errorCode': updateLogistics_error['illegalAccess']}
                else:
                    if post_data.has_key('receiverId') != False and post_data['receiverId']!='':
                        new['receiverId'] = post_data['receiverId']
                    if post_data.has_key('endPlace') != False and post_data['endPlace'] != '':
                        new['endPlace'] = post_data['endPlace']
                    if (Dal_Logistics().updateLogistics(post_data["id"], **new) == 1):
                        respon = {'errorCode': updateLogistics_error['success']}
                    else:
                        respon = {'errorCode': updateLogistics_error['failed']}
        respon_json = json.dumps(respon)
        self.write(respon_json)
