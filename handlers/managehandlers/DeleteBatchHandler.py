# -*-coding:utf-8-*-
import json

from configs.config_errorcode import deleteBatch_error
from dal.dal_batch import Dal_Batch
from handlers.BaseHandler import BaseHandler


# 删除批次信息
class DeleteBatchHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("deleteBatch.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        if (Dal_Batch().deleteBatch(post_data['id']) == False):
            respon = {'errorCode': deleteBatch_error['batchInvaild']}
        else:
            respon = {'errorCode': deleteBatch_error['success']}
        respon_json = json.dumps(respon)
        self.write(respon_json)
