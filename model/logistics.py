# -*-coding:utf-8-*-
from orm.orm import Model, IntegerField, StringField


##物流信息模型
class Logistics(Model):
    __table__ = "logistics"
    __primary_key__ = "id"

    # 物流编号
    id = IntegerField('id', False)
    # 司机Id
    driverId = StringField('driverId', True)
    # 车牌号
    plateNum = StringField('plateNum', True)
    # 出发公司
    startPlace = StringField('startPlace', True)
    # 目的公司
    endPlace = StringField('endPlace', True)
    # 该条物流产生时间
    time = StringField('time', True)
    # 物流状态
    comfirm = StringField('comfirm',True)
    # 运输批次号
    amount = StringField('amount',True)
