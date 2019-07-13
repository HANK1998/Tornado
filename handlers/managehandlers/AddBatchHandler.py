# -*-coding:utf-8-*-
import json

from handlers.BaseHandler import BaseHandler
from model.batch import Batch
from tools.utils import Utils
from dal.dal_batch import Dal_Batch


# 添加新批次
class AddBatchHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("page/addBatch.html")

    def post(self, *args, **kwargs):
        post_data = {}
        nowtime = Utils().dbTimeCreate()
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        photoPath = ''
        ##图片上传
        if (self.request.files != ''):
            photo_img = self.request.files["pro_img"]
            photoPath = Dal_Batch().addPhoto(photo_img)
        newBatch = Batch(id=None,
                         prodtime=post_data['prodtime'],
                         pc_id=post_data['id'],
                         p_name=post_data['p_name'],
                         mat_list=None,
                         exptime=post_data['exptime'],
                         intro=post_data['intro'],
                         man_id=post_data['man_id'],
                         log_id=None,
                         pro_img=photoPath,
                         qr_img=None,
                         br_img=None,
                         amount=post_data['amount'],
                         time=nowtime
                         )
        ba_id = Dal_Batch().addBatch(newBatch)
        result = Dal_Batch().selectBatch(ba_id)
        respon = {'errorcode':0}
        respon_json = json.dumps(respon)
        self.write(respon_json)
