# -*-coding:utf-8-*-
import json
from dal.dal_warehouse import Dal_Warehouse
from handlers.BaseHandler import BaseHandler

class SelectAllProdHandlers(BaseHandler):
    def get(self):
        self.render("page/selectAllProd.html")

    def post(self):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        c_id = post_data['id']
        ware_prod = Dal_Warehouse().getAllProd(c_id)
        if ware_prod != {}:
            res = {"errorcode":0,"result":ware_prod}
        else:
            res = {"errorcode": 1}
        resa = json.dumps(res)
        self.write(resa)

class SelectProdByNameHandlers(BaseHandler):
    def get(self):
        self.render("page/selectProdBN.html")

    def post(self):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)
        c_id = post_data['id']
        p_name = post_data['name']
        ware_prod = Dal_Warehouse().getProdBN(c_id,p_name)
        if ware_prod != {}:
            res = {"errorcode":0,"result":ware_prod}
        else:
            res = {"errorcode": 1}
        resa = json.dumps(res)
        self.write(resa)