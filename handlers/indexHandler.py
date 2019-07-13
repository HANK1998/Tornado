#-*-coding:utf-8-*-
import logging
import json
import tornado.log
import tornado.web
from tornado.log import access_log

# import protobuf.user_pb2
# from protobuf.user_pb2 import UserModel


class IndexHandlers(tornado.web.RequestHandler):
     def post(self):
        self.write("Hello, world hahaha")
        #entity = Entity.get('王宁的服务器')
        #self.redirect('h5/musicgame.max.html')
        #self.render('index.html')
        #self.render('musicgame.max.html')







        post_data = {}
        # auguments=self.request.body
        # # for key in self.request.arguments: ##从请求的参数中获取关键字 key
        # #     post_data[key] = self.get_arguments(key)[0]
        # # print post_data
        # entitydesc=protobuf.user_pb2.UserModel()
        # # strtest = str(post_data['a'])
        # # # entitydesc.ParseFromString(str(post_data['a'], encoding = "utf-8"))
        # # entitydesc.cyUserno="jjj"
        # # entitydesc.cyPassWord='blx12'
        # # entitydesc.cyStatus="2"
        # # ttt = entitydesc.SerializeToString(auguments)
        #
        # entitydesc.ParseFromString(auguments)
        #     str(b, encoding = "utf-8")      entitydesc.ParseFromString(bytearray(str(post_data['a'])))
        # post_data['a']=list(post_data['a'])[0]  entitydesc.cyStatus
        # entitydescs=entitydesc.ParseFromString(post_data['a'])  str(bytearray(str(post_data['a'])))


        # entitydescs=entitydesc.ParseFromArray(post_data['a'])



        self.set_header("Access-Control-Allow-Origin","*")

        self.write("hello,world!!")

     def get(self):
        self.write("hahaha,helloworld")