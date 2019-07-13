# -*-coding:utf-8-*-
import json

from configs.config_errorcode import searchProduction_error
from dal.dal_company import Dal_Company
from dal.dal_staff import Dal_Staff
from handlers.BaseHandler import BaseHandler
from dal.dal_batch import Dal_Batch

#以溯源码查询信息
class SearchProductionByCodeHandlers(BaseHandler):
    def get(self):
        result_goods={}
        code=self.get_query_argument('code')
        #将12位的溯源码分为前后4位
        code_front=code[0:4]
        code_back=code[4:]
        #获取商品基本信息
        production=Dal_Production().selectProduction(code_front)
        batch=Dal_Batch().selectBatch(code_back)
        if production == None:
            respon = {"errorCode": searchProduction_error['productionInvaild']}
        else:
            if batch==None:
                respon={"errorCode":searchProduction_error['batchInvaild']}
            else:
                staff=Dal_Staff().selectStaff(batch['producterId'])
                if(staff==None):
                    respon = {"errorCode": searchProduction_error['staffInvaild']}
                else:
                    company=Dal_Company().selectCompany(staff["companyId"])
                    if(company==None):
                        respon = {"errorCode": searchProduction_error['companyInvaild']}
                    else:
                        # 将信息放入字典
                        result_goods["code"]=str
                        result_goods["title"] = production['name']
                        result_goods["date"] = batch['time']
                        result_goods["size"] = production['format']
                        result_goods["intro"] = production['abstract']
                        result_goods["photo"] = production['photopath']
                        result_goods["company_name"] =company["name"]
                        result_goods["principal"] = staff["name"]

                        respon = {"errorCode": searchProduction_error['success']}
                        respon["message"]=result_goods
        respon_json = json.dumps(respon)
        self.write(respon_json)