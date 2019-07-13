# -*-coding:utf-8-*-
import json
from configs.config_errorcode import selectBatch_error
from dal.dal_batch import Dal_Batch
from handlers.BaseHandler import BaseHandler

class SelectBatchBsHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("page/selectBatch.html")
    def post(self,*args,**kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        batch=Dal_Batch().selectBatchBCid(post_data["id"])
        if batch==None:
            respon={'errorCode':selectBatch_error['batchInvaild']}
        else:
            respon={'errorCode':selectBatch_error['success'],'result':batch}
        respon_json=json.dumps(respon)
        self.write(respon_json)