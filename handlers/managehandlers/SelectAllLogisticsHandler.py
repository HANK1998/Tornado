# -*-coding:utf-8-*-
import json
from configs.config_errorcode import selectLogistics_error
from dal.dal_batch import Dal_Batch
from dal.dal_company import Dal_Company
from dal.dal_logistics import Dal_Logistics
from dal.dal_staff import Dal_Staff
from handlers.BaseHandler import BaseHandler


# 获取所有物流信息
class SelectAllLogisticsHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("page/selectAllLogistics.html")

    def post(self, *args, **kwargs):
        respon={}
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        company = Dal_Company().selectCompany(post_data['id'])
        if(company==None):
            respon = {'errorCode': selectLogistics_error['companyInvaild']}
        else:
            page=1 if (int(post_data["page"]) <= 0) else int(post_data["page"])
            a = Dal_Logistics().selectAllLogistics(page,str(post_data['type']),int(post_data['id']))
            logistics = a
            total=logistics['total']
            logistics.pop('total')
            for k,v in logistics.items():
                driver=Dal_Staff().selectStaff(v['driverId'])
                company=Dal_Company().selectCompany(v['startPlace'])
                nextCompany=Dal_Company().selectCompany(v['endPlace'])
                amount=v['amount']
                num = amount.count(':')
                amount_list=amount.split(':')
                amount=''
                while num>=0:
                    batch=Dal_Batch().selectBatch(amount_list[num])
                    if batch==None:
                        respon = {'errorCode': selectLogistics_error['batchInvaild']}
                    else:
                        amount+=batch['p_name']+','
                    num-=1
                v['amount']=amount[0:-1]
                v['driverId']=driver['name']
                v['startPlace']=company['name']
                v['endPlace']=nextCompany['name']
            if(logistics=={} and respon!={}):
                respon = {'errorCode': selectLogistics_error['logisticsInvaild']}
            else:
                respon = {'errorCode': selectLogistics_error['success'],'total':total,'result':logistics}
        respon_json = json.dumps(respon)
        self.write(respon_json)