# -*-coding:utf-8-*-
import json

from dal.dal_batch import Dal_Batch
from dal.dal_company import Dal_Company
from dal.dal_logistics import Dal_Logistics
from dal.dal_staff import Dal_Staff
from handlers.BaseHandler import BaseHandler
from model.logistics import Logistics
from configs.config_errorcode import addLogistics_error
import qrcode
import barcode
from barcode.writer import ImageWriter


# 添加物流信息
from tools.utils import Utils


class AddLogisticsHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("page/addLogistics.html")

    def post(self, *args, **kwargs):
        post_data = {}
        new = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        company=Dal_Company().selectCompanyByN(post_data['companyName'])
        if(company==None):
            respon = {'errorCode': addLogistics_error['companyInvaild']}
        else:
            nextcompany=Dal_Company().selectCompanyByN(post_data['nextCompanyName'])
            if(nextcompany==None):
                respon = {'errorCode': addLogistics_error['companyInvaild']}
            else:
                driver = Dal_Staff().selectStaffByName(post_data['name'])
                if (driver == None):
                    respon = {'errorCode': addLogistics_error['driverInvaild']}
                else:
                    batch = Dal_Batch().selectBatch(post_data['amount'])
                    if(batch==None):
                        respon = {'errorCode': addLogistics_error['batchInvaild']}
                    else:
                        nowtime = Utils().dbTimeCreate()
                        newLogistics = Logistics(id=None, driverId=driver['id'],
                                         plateNum=post_data['plateNum'],
                                         startPlace =company['id'],
                                         endPlace =nextcompany['id'],
                                         time = str(nowtime),
                                         comfirm = 'N',
                                         amount = post_data['amount']
                                         )
                        id = Dal_Logistics().addLogistics(newLogistics)
                        if id == False:
                            respon = {'errorCode': addLogistics_error['failed']}
                        else:
                            new['log_id'] = id
                            batch_id = str(post_data["amount"])
                            if (Dal_Batch().updateBatch(batch_id, **new) == 1):
                                respon = {'errorCode': addLogistics_error['success']}
                                c_id = str(company['id'])
                                c_id = str(c_id.zfill(4))
                                batch_id = str(batch_id.zfill(5))
                                text = "690"+c_id+batch_id
                                self.make_qrcode(text,batch_id)
                                self.make_brcode(text,batch_id)
        respon_json = json.dumps(respon)
        self.write(respon_json)

    #条形码方法
    def make_brcode(self,text,batch_id):
        Code = barcode.get_barcode_class('ean13')
        imagewriter = ImageWriter()
        text = str(text)
        bar = Code(text, writer=imagewriter, add_checksum=False)
        a = "C:\Users\Administrator\Desktop\Traceability\static\BarCode_img\\"+batch_id
        bar.save(a)
        new = {}
        new["br_img"] = batch_id + ".png"
        Dal_Batch().updateBatch(batch_id, **new)

    #二维码方法
    def make_qrcode(self,text,batch_id):
        qr = qrcode.QRCode(version=5,
                           error_correction=qrcode.constants.ERROR_CORRECT_L,
                           box_size=10,
                           border=4,
                           )
        # 加密
        # text = Dal_Logistics().decrypt(text, '1938762450')
        # 添加数据
        qr.add_data(text)
        # 生成二维码
        qr.make(fit=True)
        img = qr.make_image()
        a = "C:\Users\Administrator\Desktop\Traceability\static\BarCode_img\\"+batch_id+".png"
        img.save(a)
        # img.show()
        new = {}
        new["qr_img"] = batch_id+".png"
        Dal_Batch().updateBatch(batch_id,**new)