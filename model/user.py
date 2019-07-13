# -*- coding:utf-8 -*-

from orm.orm import Model, IntegerField, StringField

# 普通用户模型
class User(Model):
    __table__ = "user"
    __primary_key__ = "id"

    #用户编号
    id = IntegerField('id', False)
    #用户名
    name = StringField('name', True)
    #密码
    password = StringField('password', True)
    #联系方式
    tel = StringField('tel', True)
    #注册时间
    registerTime = StringField('registerTime', True)
