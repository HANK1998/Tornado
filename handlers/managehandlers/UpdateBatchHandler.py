# -*-coding:utf-8-*-
import json

from configs.config_errorcode import updateBatch_error
from dal.dal_batch import Dal_Batch
from handlers.BaseHandler import BaseHandler
from tools.utils import Utils


# 修改批次信息
class UpdateBatchHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("updateBatch.html")

    def post(self, *args, **kwargs):
        post_data = {}
        new = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        if (Dal_Batch().selectBatch(post_data['id']) == None):
            respon = {'errorCode': updateBatch_error['batchInvaild']}
        else:
            if post_data.has_key('saleAddress') != False and post_data['saleAddress']!='':
                new['saleAddress'] = post_data['saleAddress']
                new['saleTime']=str(Utils().dbTimeCreate())

            if (Dal_Batch().updateBatch(post_data["id"], **new) == 1):
                respon = {'errorCode': updateBatch_error['success']}
            else:
                respon = {'errorCode': updateBatch_error['failed']}
        respon_json = json.dumps(respon)
        self.write(respon_json)
