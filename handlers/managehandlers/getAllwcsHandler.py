# -*-coding:utf-8-*-

import json
from dal.dal_company import Dal_Company
from dal.dal_staff import Dal_Staff
from handlers.BaseHandler import BaseHandler


class getAllwcsHandlers(BaseHandler):

    def gettypename(self,type):
        if type == '0':
            return "warehouse"#采购
        else:
            return "production"#产品
    def getstafftype(self,type):
        if type == '0':
            return "采购员"#采购
        else:
            return "仓管员"#产品


    def get(self):
        self.render("test.html")

    def post(self):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        type = post_data['type']#判断类型
        typename = self.gettypename(type)#获取操作类型

        com_id = post_data['cid']#当前操作公司id
        if typename == 'warehouse':
            com_list = Dal_Company().getCompanyNameByType(typename)#获取公司列表
        elif typename == 'production':
            com_list = Dal_Company().getCompanyNameByDType(typename)  # 获取公司列表

        staff_list = Dal_Staff().selectStaffByCT(com_id,self.getstafftype(type))

        data = {"errorcode":"0","company":com_list,"staff":staff_list}

        dataarray = json.dumps(data)
        self.write(dataarray)

