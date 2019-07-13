# -*-coding:utf-8-*-
import json
from configs.config_errorcode import selectBatch_error
from dal.dal_batch import Dal_Batch
from handlers.BaseHandler import BaseHandler


# 获取所有批次信息
class SelectAllBatchHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("selectAllBatch.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        batch = Dal_Batch().selectBatch(1 if (int(post_data["page"]) <= 0) else post_data["page"])
        respon = {'errorCode': selectBatch_error['success'], 'batch': batch}
        respon_json = json.dumps(respon)
        self.write(respon_json)