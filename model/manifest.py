# -*-coding:utf-8-*-
from orm.orm import Model, IntegerField, StringField,FloatField


##订单信息模型
class Manifest(Model):
    __table__ = "manifest"
    __primary_key__ = "id"

    # 订单识别码
    id = IntegerField('id', False)
    # 采购商品名
    prod_name = StringField('prod_name', True)
    # 采购员id
    originatorId = StringField('originatorId', True)
    # 采购量
    amount = FloatField('amount', True)
    # 采购时间
    time = StringField('time', True)
    # 采购地点
    place=StringField('place',True)
    # 订单状态
    confirm=StringField('confirm',True)    