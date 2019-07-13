# -*-coding:utf-8-*-
import json

from dal.dal_company import Dal_Company
from handlers.BaseHandler import BaseHandler
from model.staff import Staff
from tools.utils import Utils
from dal.dal_staff import Dal_Staff
from configs.config_errorcode import addStaff_error


# 添加新职员
class AddStaffHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("addStaff.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        if (Dal_Staff().selectStaffByNPT(post_data['name'], post_data['type']) == True):
            respon = {'errorCode': addStaff_error['staffExist']}
        else:
            company = Dal_Company().selectCompanyByN(post_data['companyName'])
            if (company == None):
                respon = {'errorCode': addStaff_error['companyInvaild']}
            else:
                companyId = company['id']
                photoPath = ''
                ##图片上传
                if (self.request.files != ''):
                    photo_img = self.request.files["photo"]
                    photoPath = Dal_Staff().addPhoto(photo_img)

                nowtime = Utils().dbTimeCreate()
                newStaff = Staff(id=None, name=post_data['name'], tel=post_data['tel'],
                                 type=post_data['type'], photoPath=photoPath, companyId=companyId,
                                 entryTime=nowtime
                                 )
                id = Dal_Staff().addStaff(newStaff)
                if id == False:
                    respon = {'errorCode': addStaff_error['failed']}
                else:
                    respon = {'errorCode': addStaff_error['success'], 'id': id}
        respon_json = json.dumps(respon)
        self.write(respon_json)
