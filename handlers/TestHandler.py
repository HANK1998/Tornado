# -*-coding:utf-8-*-
import base64
import io
import json
import os

from PIL import Image

from dal.dal_company import Dal_Company
from handlers.BaseHandler import BaseHandler
from configs.config_errorcode import adminLogin_error


##登陆
class TestHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        img = Image.open('d:/img/4.jpg')
        img.show()
        img.save('d:/img/a.png')

    def post(self, *args, **kwargs):
        result=json.loads.body
        img=result['image']
        time=result['time']
        image=base64.b64decode(img)
        image1 = io.BytesIO(image)
        img = Image.open(image1)
        img.save('d:/img/'+str(time)+'.jpeg')



