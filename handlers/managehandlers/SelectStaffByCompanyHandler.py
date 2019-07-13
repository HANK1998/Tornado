# -*-coding:utf-8-*-
import json
from configs.config_errorcode import selectStaff_error,selectCompany_error
from dal.dal_company import Dal_Company
from dal.dal_staff import Dal_Staff
from handlers.BaseHandler import BaseHandler

class SelectStaffByCompanyHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("selectStaffByCompany.html")
    def post(self,*args,**kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        company=Dal_Company().selectCompany(post_data["companyId"])
        if company==None:
            respon={'errorCode':selectCompany_error['companyInvaild']}
        else:
            staff=Dal_Staff().selectStaffByCid(int(post_data['companyId']))
            if(staff=={}):
                respon = {'errorCode':selectStaff_error['staffInvaild']}
            else:
                respon={'errorCode':selectStaff_error['success'],'staff':staff}
        respon_json=json.dumps(respon)
        self.write(respon_json)