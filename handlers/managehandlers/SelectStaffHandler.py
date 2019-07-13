# -*-coding:utf-8-*-
import json
from configs.config_errorcode import selectStaff_error
from dal.dal_company import Dal_Company
from dal.dal_staff import Dal_Staff
from handlers.BaseHandler import BaseHandler

class SelectStaffHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("selectStaff.html")
    def post(self,*args,**kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        staff=Dal_Staff().selectStaff(post_data["id"])
        if staff==None:
            respon={'errorCode':selectStaff_error['staffInvaild']}
        else:
            company=Dal_Company().selectCompany(staff['companyId'])
            staff['companyName']=company['name']
            respon={'errorCode':selectStaff_error['success'],'staff':staff}
        respon_json=json.dumps(respon)
        self.write(respon_json)