# -*-coding:utf-8-*-
import json
from configs.config_errorcode import selectManifest_error
from dal.dal_manifest import Dal_Manifest
from handlers.BaseHandler import BaseHandler


class SelectManifestHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("selectManifest.html")

    def post(self, *args, **kwargs):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        manifest = Dal_Manifest().selectManifest(post_data["id"])
        if manifest == None:
            respon = {'errorCode': selectManifest_error['manifestInvaild']}
        else:
            respon = {'errorCode': selectManifest_error['success'], 'manifest': manifest}
        respon_json = json.dumps(respon)
        self.write(respon_json)
